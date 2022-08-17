from tkinter.ttk import Style
from types import NoneType
import pandas as pd
import numpy as np
import xlsxwriter
import pyodbc
from openpyxl import Workbook, load_workbook
from styleframe import StyleFrame, Styler, utils


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


# extract the Schema and Table name from SET...ON line 
list_SAT = []
for l in lines:
    if (str_set and str_on and bp) in l:
        right = l.split(bp, 1)[1]
        SchemaAndTable = right.split(bp2, 1)[0]
        SchemaAndTable = SchemaAndTable.replace("[", "").replace("]", "")
        list_SAT.append(SchemaAndTable)
list_SAT = list_SAT[::2]
# print(list_SAT)

# only keep "INSERT" line and remove "INSERT", "VALUES" --> output new file 
with open(new_path, "w") as new_file:
    for l in lines:
        if filter_str in l and str_set not in l:
            l = l.replace(filter_str, "").replace(str_value, "")
            new_file.write(l)


# read new file and extract [schema].[table], columns, values and convert them into dataframe: df
cut_f = " ("
cut_s = ") ("
dic = {}
list_schemaAndtable = []
list_columns = []
list_values = []
with open(new_path, "r") as new_file:
    new_lines = new_file.readlines()
    for l in new_lines:
        schema_table = l.split(cut_f, 1)[0].replace("[", "").replace("]", "")
        out_of_SandT = l.split(cut_f, 1)[1]
        columns = out_of_SandT.split(cut_s, 1)[0].replace("[", "").replace("]", "")
        values = out_of_SandT.split(cut_s, 1)[1]
        values = values[:-2]

        list_schemaAndtable.append(schema_table)        
        list_columns.append(columns)        
        list_values.append(values)    

# dataframe:  (1)Schema & Table  (2)Columns  (3)Values
dic['Schema & Table'] = list_schemaAndtable
dic['Columns'] = list_columns
dic['Values'] = list_values
df = pd.DataFrame(dic)


# connect to SQL server and get TableName, ColName, ColDescription from db
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
    a.Table_schema + '.' + a.Table_name as VVV,
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
data = cursor.execute(query).fetchall()   # (Schema.Table, ColName, ColDescription)


# convert SqlData into dataframe 
dic2 = {}
list_TableName = []
list_ColumnName = []
list_ColumnDescrip = []
for i in data:
    list_TableName.append(i[0])
    list_ColumnName.append(i[1])
    list_ColumnDescrip.append(i[2])
dic2['表格名稱'] = list_TableName
dic2['欄位名稱'] = list_ColumnName
dic2['欄位描述'] = list_ColumnDescrip
df_SqlData = pd.DataFrame(dic2)

    
# get the column names and descriptions of those schema that are present in the SQL file
dic3 = {}
for schema in list_SAT:
    list_TmpCN = []
    list_TmpDes = []

    for i in range(len(df_SqlData)):
        if df_SqlData['表格名稱'].iloc[i] == schema :
            list_TmpCN.append(df_SqlData['欄位名稱'].iloc[i])
            list_TmpDes.append(df_SqlData['欄位描述'].iloc[i])

    dic3[schema+'_column'] = list_TmpCN
    dic3[schema+'_description'] = list_TmpDes

df_columnAnddesciption = pd.DataFrame({ key:pd.Series(value) for key, value in dic3.items() })  


# write excel
dic_AllDF = {}
export_file = 'MultiDF3.xlsx'
writer = pd.ExcelWriter(export_file, engine='openpyxl')   
str_CAST = 'CAST'
str_AsDatetime = ' AS DateTime'
for schema in list_SAT:

    tmp_ColData = df_columnAnddesciption[schema + '_column']
    tmp_DescripData = df_columnAnddesciption[schema + '_description']

    isStr_col = [True if isinstance(i, str) == True or isinstance(i, NoneType) == True else False for i in tmp_ColData]
    isStr_descrip = [True if isinstance(i, str) == True or isinstance(i, NoneType) == True else False for i in tmp_DescripData]

    ColumnNames = tmp_ColData[isStr_col]
    Descriptions = tmp_DescripData[isStr_descrip].values

    list_TmpVal = []

    tmp_df = pd.DataFrame(columns=ColumnNames)   # set column names as headers
    tmp_df.loc[0] = Descriptions  # set columns descriptions as first row data

    # Get the values to be inserted using schema as the keys
    for i in range(len(df)):
        if df['Schema & Table'].iloc[i] == schema:
            list_TmpVal.append(df['Values'].iloc[i].split(","))        
    

    for j in range(len(list_TmpVal)):  # iterations: the number of value lines to be INSERTED
        insert_dic = {}

        for k in range(len(list_TmpVal[j])):  # iterations: the number of values in one line
            if ")" in list_TmpVal[j][k] and "(" not in list_TmpVal[j][k]:
                list_TmpVal[j][k-1] = list_TmpVal[j][k-1] + ", " + list_TmpVal[j][k]
                list_TmpVal[j].remove(list_TmpVal[j][k])
                break

        for c in range(len(ColumnNames)):  # iterations: the number of columns

            # data processing
            if str_CAST and str_AsDatetime in list_TmpVal[j][c]:
                list_TmpVal[j][c] = list_TmpVal[j][c].replace(str_CAST, "").replace(str_AsDatetime, "").replace("(", "").replace(")", "").replace("-", "/").replace("T", " ")
                list_TmpVal[j][c] = list_TmpVal[j][c].replace("N'", "").replace("'", "")

            elif str(list_TmpVal[j][c]) == " N'N'":
                list_TmpVal[j][c] = "N"
            
            else:
                list_TmpVal[j][c] = list_TmpVal[j][c].replace("N'", "").replace("'", "")

            insert_dic[ColumnNames[c]] = list_TmpVal[j][c]

        
        # add values to be inserted as row data
        tmp_df.loc[len(tmp_df)] = insert_dic
    
    dic_AllDF[schema] = tmp_df

start_row = 0
pre_len = 0
for key, value in dic_AllDF.items():
    start_row += pre_len

    df_schema = pd.DataFrame({'Schema.Table': key}, index=[0])
    sf_schema = StyleFrame(df_schema, Styler(border_type=None, fill_pattern_type=None))
    sf_schema.apply_column_style(cols_to_style=['Schema.Table'], styler_obj=Styler(font_size=18))
    sf_schema.to_excel(writer, sheet_name='sheet1', startrow=start_row, startcol=0, index=False, header=False) 
    
    sf_value = StyleFrame(value, Styler(border_type=None, fill_pattern_type=None))
    sf_value.apply_headers_style(styler_obj=Styler(bg_color=utils.colors.yellow))
    sf_value.to_excel(writer, sheet_name='sheet1', startrow=start_row+1, startcol=0, index=False)

    pre_len = len(value)+3

writer.save() 


