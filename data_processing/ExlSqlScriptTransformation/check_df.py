from tkinter.ttk import Style
from types import NoneType
import pandas as pd
import numpy as np
import xlsxwriter
import pyodbc
from openpyxl import Workbook, load_workbook
from styleframe import StyleFrame, Styler, utils


# extract the Schema and Table name from SET...ON line 
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
    with open(new_path, "w") as new_file:
        for l in data:
            if (str_insert in l) and (str_value in l) and (str_set not in l):
                l = l.replace(str_insert, "").replace(str_value, "")
                new_file.write(l)
        

# read new file and extract [schema].[table], columns, values and convert them into dataframe: df
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

    # for i in range(len(df)):
        



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


# # aggregate data
# def AggregateData(list_s, df_sql):
#     dict = {}
#     for schema in list_s:
#         list_cols = []
#         list_desc = []
#         list_vals = []
#         list_pack = []
#         for i in range(len(df_sql)):
#             if df_sql['表格名稱'].iloc[i] == schema:





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
    # DataCleaning(lines, new_path)

    # read new txt file
    with open(new_path, "r") as new_file:
        new_lines = new_file.readlines()

    # convert new txt file to dataframe:  (1)Schema & Table  (2)Columns  (3)Values
    df_newFile = NewFileToDF(new_lines)
        
    # connect to SQL server and get TableName, ColName, ColDescription from db and convert them to dataframe
    df_sqlData = SqlDataToDF()

    data = df_newFile['Values'].iloc[5].split(", ")
    print(data)
    # for i in data:
    #     print(i)