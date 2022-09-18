from cmath import nan
import pandas as pd
import numpy as np
from openpyxl import load_workbook
import csv
# import To_BA_script
from To_BA_script import dict_label



# calculate the number of tables
def CalculateNumTables(df):
    empty_count = 0
    for i in range(len(df)):
        if str(df.iloc[i][0]) == 'nan':
            empty_count += 1
    num_schema = empty_count + 1  # number of schema in exl == 24
    return num_schema


# calculate the number of rows of different tables
def CalculateNumRows(num_schema, df):
    list_len_table = []
    row = 0
    first_table = True
    for num in range(num_schema):
        while row <= len(df)-1 and str(df.iloc[row][0]) != 'nan':
            row += 1
        if first_table:
            list_len_table.append(row)
            row += 1
            first_table = False
        else:
            list_len_table.append(row - sum(list_len_table[:num]) - num)
            row += 1
    return list_len_table
    # print(len(list_len_table), '\n')
    # print(list_len_table)


# # append all the data to dictionary, get the data ready to be writre to txt file
# def AggregateData(num_schema, list_len_table, df):
#     start_row = 0
#     dict = {}
#     for i in range(num_schema):  # iterations: number of schema (24)
#         list_current_table_str = []
#         if str(df.iloc[start_row][0]) == 'nan':  # jump to the nonempty line
#             start_row += 1
        
#         # convert exl file data to the string that are ready to be inserted 
#         for j in range(list_len_table[i]+1):  # iterations: length of current table -> [7, 13, 11, 82, 4, 354, 1018, 41, 1018, 9, 7, 6, 8, 13, 5, 795, 194, 7, 8, 4, 5, 8, 16, 13]

#             # SET ... ON
#             # GO
#             if j == 0:  # insert schema.table
#                 schema = df.iloc[start_row][0].split(".")
#                 schema = "[" + schema[0] + "]" + "." + "[" + schema[1] + "]"  # [collection].[ProductType]
#                 set_script = 'SET IDENTITY_INSERT ' + schema + ' ON'
#                 list_current_table_str.append(set_script)
#                 list_current_table_str.append("GO")
            
#             # get column names
#             elif j == 1 :
#                 col_names = df.iloc[start_row].dropna().values
#                 col_names = ", ".join("[" + item + "]" for item in col_names)  # [ProductTypeId], [ProductTypeName], ... 
#                 col_names = "(" + col_names + ")"
            
#             # ignore the descriptions
#             elif j == 2: 
#                 pass

#             # get values
#             elif j >= 3 and j <= list_len_table[i]-1:
#                 values = df.iloc[start_row].dropna().values
#                 values = ", ".join(item for item in values)
#                 values = "(" + values + ")"
#                 insert_script = "INSERT " + schema + " " + col_names + " VALUES " + values
#                 list_current_table_str.append(insert_script)
#                 list_current_table_str.append("GO")
            
#             # SET ... OFF
#             # GO
#             else:
#                 set_script_final = 'SET IDENTITY_INSERT ' + schema + ' OFF'
#                 list_current_table_str.append(set_script_final)
#                 list_current_table_str.append("GO")
            
#             start_row += 1
        
#         dict[f'Schema{i+1}'] = list_current_table_str
    
#     return dict


def RetrieveValue(df, schema):
    for col in df.columns:
        key = schema + '.' + col
        if key in dict_label:
            # 2021/06/11 00:00:00.000
            # to
            # ex: CAST(N'2021-06-11T00:00:00.000' AS DateTime)
            if dict_label[key] == 'datetime':
                # recover the datetime format
                list_newDt = []
                for dt in df[col]:
                    dt = dt.replace("/", "-").replace(" ", "T")
                    list_newDt.append(dt)
                df[col] = list_newDt
                df[col] = "CAST(N'" + df[col] + " AS DateTime)"

            # 1.00000000
            # to
            # ex: CAST(1.00000000 AS Decimal(12, 8))
            elif dict_label[key] == 'decimal':
                df[col] = "CAST(" + df[col] + " AS Decimal(12, 8))"
            
            elif dict_label[key] == 'N':
                df[col] = "N'" + df[col] + "'"
    return df



# append all the data to dictionary, get the data ready to be writre to txt file
def AggregateData(num_schema, list_len_table, df):
    start_row = 0
    dict_allDf = {}
    for i in range(num_schema):  # iterations: number of schema (24)
        if str(df.iloc[start_row][0]) == 'nan':  # jump to the nonempty line
            start_row += 1
        
        # make dataframe
        # col_names = []
        for j in range(list_len_table[i]):  # iterations: length of the current table in excel -> [7, 13, 11, 82, 4, 354, 1018, 41, 1018, 9, 7, 6, 8, 13, 5, 795, 194, 7, 8, 4, 5, 8, 16, 13]
            # if col_names:
            #     curr_df = pd.DataFrame(columns=col_names)
            # get schema name
            if j == 0:
                schema = df.iloc[start_row][0]
                # print(schema)
                
            # get column names: ProductTypeId, ProductTypeName ... 
            # create dataframe
            elif j == 1 :
                col_names = df.iloc[start_row].dropna().values  # pd.Series
                curr_df = pd.DataFrame(columns=col_names)
                # print(col_names)
                # print(curr_df)
            
            # ignore the descriptions row
            elif j == 2: 
                pass

            # get values
            elif j >= 3:
                values = df.iloc[start_row][:len(col_names)]  # pd.Series
                isNull = values.isnull()
                values[isNull] = "NULL"
                # values = pd.Series(values, index=None, dtype=None, name=None)
                # print(values)
                curr_df.loc[len(curr_df)] = list(values)  # pd.Series要轉成list!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                # print(curr_df)
            
            start_row += 1
        # print(values)
        # print(curr_df)
        # dict_allDf[schema] = curr_df

        # recover the value (e.g. CAST ... AS ... , N'')
        new_df = RetrieveValue(curr_df, schema)

        # store current dataframe to the dictionary
        dict_allDf[schema] = new_df

    return dict_allDf


def FormatSetScript(schema):
    schema_add_brackets = "[" + schema.split(".")[0] + "]" + "." + "[" + schema.split(".")[1] + "]"
    first_line = "SET IDENTITY_INSERT " + schema_add_brackets + " ON"
    final_line = first_line.replace("ON", "OFF")
    return schema_add_brackets, first_line, final_line

# "INSERT [collection].[ProductType] ([ProductTypeId], [ProductTypeName]) VALUES (1, Motor)"
def FormatInsertScript(schema, df):
    list_insertScript = []
    columns = '(' + str(list(df.columns)).replace("'", "") + ')'
    for i in range(len(df)):
        values = str(tuple(df.iloc[i]))  #dtype = pd.Series
        script = f'INSERT {schema} {columns} VALUES {values}'
        list_insertScript.append(script)
    return list_insertScript


def WriteScript(dict_allDf, export_path):
    #SET IDENTITY_INSERT [collection].[ProductType] ON
    # list_oneScript = []
    with open(export_path, 'w') as export_file:
        writer = csv.writer(export_file)
    for schema, df in dict_allDf.items():
        schema_add_brackets, first_line, final_line = FormatSetScript(schema)
        list_insertScript = FormatInsertScript(schema_add_brackets, df)

        # write script to txt file row by row
        writer.writerows(first_line)
        writer.writerows("GO")
        for rows in range(len(list_insertScript)):
            writer.writerows(list_insertScript[rows])
            writer.writerows("GO")
        writer.writerows(final_line)
        writer.writerows("GO")
        
        

        

            
# export excel file from BA to txt file(SQL script)
if __name__ == "__main__":
    xlsx_file_path = 'MultiDF.xlsx'
    export_path = 'test.txt'
    # empty_count = 0
    df_excel = pd.read_excel(xlsx_file_path, header=None)
    # print(df_excel)
    # for i in range(7):
    #     print(df_excel.iloc[i])
    
    
    # get number of schema
    num_schema = CalculateNumTables(df_excel)

    # create the list that stores row numbers of different tables
    list_len_table = CalculateNumRows(num_schema, df_excel)
    # print(list_len_table)

    # aggregate the data to be wrote
    dict_allDf = AggregateData(num_schema, list_len_table, df_excel)
    for k, v in dict_allDf.items():
        print(k)
        print(v)
        print('\n')

    


    # # write to txt file
    # with open(export_path, 'w') as export_file:
    #     writer = csv.writer(export_file)
    #     for schema, script in dict_allDf.items():
    #         for lines in script:
    #             writer.writerow([lines])




