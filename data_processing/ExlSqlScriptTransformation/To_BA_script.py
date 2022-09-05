import pandas as pd
import pyodbc
from styleframe import StyleFrame, Styler, utils



# extract the Schema and Table from SET...ON line 
def GetSchema(data):
    list = []
    str_set = 'SET'
    str_on = 'ON'
    bp = 'IDENTITY_INSERT '
    bp2 = ' '
    for l in data:
        if (str_set and str_on and bp) in l:
            right = l.split(bp, 1)[1]
            SchemaAndTable = right.split(bp2, 1)[0]
            SchemaAndTable = SchemaAndTable.replace("[", "").replace("]", "")
            list.append(SchemaAndTable)
    list = list[::2]
    return list


# only keep "INSERT" line and remove "INSERT", "VALUES" --> output new file 
def DataCleaning(data, new_path):
    str_insert = "INSERT "
    str_value = "VALUES "
    str_set = 'SET'

    # only keep the INSERT lines
    with open(new_path, "w") as new_file:
        for l in data:
            if (str_insert in l) and (str_value in l) and (str_set not in l):
                l = l.replace(str_insert, "").replace(str_value, "")
                new_file.write(l)
    

# read new file and extract [schema].[table], columns, values and convert them into dataframe: df and process [Values]
def NewFileToDF(data):
    cut_f = " ("
    cut_s = ") ("
    dict = {}
    list_schemaAndtable = []
    list_columns = []
    list_values = []
    for l in data:
        schema_table = l.split(cut_f, 1)[0].replace("[", "").replace("]", "")
        out_of_SandT = l.split(cut_f, 1)[1]
        columns = out_of_SandT.split(cut_s, 1)[0].replace("[", "").replace("]", "")
        values = out_of_SandT.split(cut_s, 1)[1]
        values = values[:-2]

        list_schemaAndtable.append(schema_table)        
        list_columns.append(columns)        
        list_values.append(values)    

    dict['Schema & Table'] = list_schemaAndtable
    dict['Columns'] = list_columns
    dict['Values'] = list_values
    df = pd.DataFrame(dict)

    # remove N'', CAST...AS DATETIME, CAST...AS DECIMAL
    for i in range(len(df)):
        values = df['Values'].iloc[i].split(", ")  # a list

        # remove '8))'
        for k in range(len(values)):
            if ")" in values[k] and "(" not in values[k]:
                values.remove(values[k])
                break

        for j in range(len(values)):

            if 'CAST' and ' AS DateTime' in values[j]:
                values[j] = values[j].replace('CAST', "").replace(' AS DateTime', "").replace("(", "").replace(")", "").replace("-", "/").replace("T", " ")
                values[j] = values[j].replace("N'", "").replace("'", "")

            elif 'CAST' and ' AS Decimal' in values[j]:
                values[j] = values[j].split('(', 1)[1]
                values[j] = values[j].split(' AS', 1)[0]
                
            elif str(values[j]) == "N'N'":
                values[j] = "N"
            
            elif "N'" in values[j]:
                values[j] = values[j].replace("N'", "").replace("'", "")

        df['Values'].iloc[i] = ', '.join(values)
    return df


# connect to SQL server and get TableName, ColName, ColDescription from db
def SqlDataToDF():
    server = 'tcp:misql-sigv-sit04.6c276a28d249.database.windows.net' 
    database = 'ibm_dev_my_collection'
    username = 'IBM_DBA' 
    password = 'IBM_DBA' 
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
    cursor = cnxn.cursor()
    schema = 'collection'
    query = f"""
    -- USE {database};
    SELECT
        a.Table_schema + '.' + a.Table_name,
        b.COLUMN_NAME,
        CAST((SELECT value
        FROM sys.fn_listextendedproperty (NULL, 'schema', a.Table_schema, 'table', a.TABLE_NAME, 'column', default)
        WHERE name='MS_Description' and objtype='COLUMN'
            and objname Collate Chinese_Taiwan_Stroke_CI_AS = b.COLUMN_NAME) as nvarchar)
    FROM INFORMATION_SCHEMA.TABLES  a
        LEFT JOIN INFORMATION_SCHEMA.COLUMNS b ON a.TABLE_NAME = b.TABLE_NAME
    WHERE TABLE_TYPE='BASE TABLE' 
        and a.Table_schema='{schema}'
    ORDER BY a.TABLE_NAME, b.ORDINAL_POSITION
    """
    dict = {}
    list_TableName = []
    list_ColumnName = []
    list_ColumnDescrip = []

    data = cursor.execute(query).fetchall()   # each data: (Schema.Table, ColName, ColDescription)
    
    # convert SqlData into dataframe 
    for i in data:
        list_TableName.append(i[0])
        list_ColumnName.append(i[1])
        list_ColumnDescrip.append(i[2])
    dict['表格名稱'] = list_TableName
    dict['欄位名稱'] = list_ColumnName
    dict['欄位描述'] = list_ColumnDescrip
    df = pd.DataFrame(dict)
    return df


# aggregate data
def AggregateData(list_s, df_sql, df_txt):
    dict = {}
    dict_p = {}
    list_pack = []
    list_pack_p = []
    list_s_p = []
    for schema in list_s[:]:
        list_cols = []
        list_desc = []
        list_vals = []

        # store colNames and descriptions
        for i in range(len(df_sql)):
            if df_sql['表格名稱'].iloc[i] == schema:
                list_cols.append(df_sql['欄位名稱'].iloc[i])
                list_desc.append(df_sql['欄位描述'].iloc[i])

        # store values
        for j in range(len(df_txt)):
            if df_txt['Schema & Table'].iloc[j] == schema:
                list_vals.append(df_txt['Values'].iloc[j].split(", "))
        
        # check if the length of data from SQL DB and SQL file are identical
        notIdentical = False
        for k in list_vals:
            if len(k) != len(list_cols):  # the number of columns from DB and the one to be inserted are not the same
                list_s_p.append(schema) 
                list_s.remove(schema)  # drop the schema with problems
                list_coll = [list_cols, list_desc, list_vals]
                list_pack_p.append(list_coll)
                notIdentical = True
                break
        if not notIdentical:
            list_coll = [list_cols, list_desc, list_vals]
            list_pack.append(list_coll)

    # append lists with problems to dictionary by schema
    if list_s_p:
        for p in range(len(list_s_p)):
            dict_p[list_s_p[p]] = list_pack_p[p]

    # append lists to dictionary by schema    
    for k in range(len(list_s)):
        dict[list_s[k]] = list_pack[k]
    
    return dict, dict_p


def WriteExl(dict_aggregate, writer, start_row, pre_len, dict_problems):
    for key, value in dict_aggregate.items():  # make dataframes
        tmp_df = pd.DataFrame(columns=value[0])  # column names
        tmp_df.loc[0] = pd.Series(value[1]).values  # column descriptions

        for i in range(len(value[2])):  # values
            # convert value list to dictionary
            dict = {}
            for j in range(len(value[0])):  # number of columns
                dict[value[0][j]] = value[2][i][j]
            
            tmp_df.loc[len(tmp_df)] = dict

        start_row += pre_len

        # schema to excel
        df_schema = pd.DataFrame({'Schema.Table': key}, index=[0])
        sf_schema = StyleFrame(df_schema, Styler(border_type=None, fill_pattern_type=None))
        sf_schema.apply_column_style(cols_to_style=['Schema.Table'], styler_obj=Styler(font_size=18))
        sf_schema.to_excel(writer, sheet_name='sheet1', startrow=start_row, startcol=0, index=False, header=False) 
        
        # convert the left to excel
        sf_value = StyleFrame(tmp_df, Styler(border_type=None, fill_pattern_type=None))
        sf_value.apply_headers_style(styler_obj=Styler(bg_color=utils.colors.yellow))
        sf_value.to_excel(writer, sheet_name='sheet1', startrow=start_row+1, startcol=0, index=False)

        pre_len = len(tmp_df)+3

    # if there are any abnormal data
    if dict_problems:
        start_row_p = start_row + pre_len
        for key, value in dict_problems.items():
            # df: colNames and descriptions
            tmp_df_p = pd.DataFrame(columns=value[0])  # column names
            tmp_df_p.loc[0] = pd.Series(value[1]).values  # column descriptions

            df_values = pd.DataFrame(columns=range(len(value[2][0])))  # give it a random column names
            for i in range(len(value[2])):  # values   
                # convert value list to dictionary
                dict_p = {}
                for j in range(len(value[2][0])):  # number of columns
                    dict_p[df_values.columns.values[j]] = value[2][i][j]
                
                df_values.loc[len(df_values)] = dict_p

            # schema to excel
            df_schema_p = pd.DataFrame({'Schema.Table': key}, index=[0])
            sf_schema_p = StyleFrame(df_schema_p, Styler(border_type=None, fill_pattern_type=None))
            sf_schema_p.apply_column_style(cols_to_style=['Schema.Table'], styler_obj=Styler(font_size=18))
            sf_schema_p.to_excel(writer, sheet_name='sheet1', startrow=start_row_p, startcol=0, index=False, header=False)
            start_row_p += len(df_schema_p) 
            
            # convert the colNames and descriptions to excel
            sf_nameAndDesc = StyleFrame(tmp_df_p, Styler(border_type=None, fill_pattern_type=None))
            sf_nameAndDesc.apply_headers_style(styler_obj=Styler(bg_color=utils.colors.red))
            sf_nameAndDesc.to_excel(writer, sheet_name='sheet1', startrow=start_row_p, startcol=0, index=False)
            start_row_p += len(tmp_df_p)+1

            # convert the values to excel
            sf_value_p = StyleFrame(df_values, Styler(border_type=None, fill_pattern_type=None))
            sf_value_p.to_excel(writer, sheet_name='sheet1', startrow=start_row_p, startcol=0, index=False, header=False)
            start_row_p += len(df_values)+1 
            
    writer.save() 



if __name__ == "__main__":
    path = 'DML_Ru.txt'
    new_path = 'DML_Ru_InsertOnly.txt'
    str_set = 'SET'
    str_on = 'ON'
    bp = 'IDENTITY_INSERT '
    bp2 = ' '
    filter_str = "INSERT "
    str_value = "VALUES "

    # read txt file
    with open(path, "r") as ori_file:
        lines = ori_file.readlines()

    # get schema
    list_schema = GetSchema(lines)

    # clean the data and write it as new file
    DataCleaning(lines, new_path)

    # read new txt file
    with open(new_path, "r") as new_file:
        new_lines = new_file.readlines()

    # convert new txt file to dataframe:  (1)Schema & Table  (2)Columns  (3)Values
    df_newFile = NewFileToDF(new_lines)
        
    # connect to SQL server and get TableName, ColName, ColDescription from db and convert them to dataframe
    # [表格名稱] [欄位名稱] [欄位描述]
    df_sqlData = SqlDataToDF()

    # aggregate colNames, descriptions, values
    dict_aggregate, dict_problems = AggregateData(list_schema, df_sqlData, df_newFile)

    # write excel
    export_file = 'MultiDF.xlsx'
    writer = pd.ExcelWriter(export_file, engine='openpyxl')  
    start_row = 0
    pre_len = 0
    WriteExl(dict_aggregate, writer, start_row, pre_len, dict_problems)
    
    
    

