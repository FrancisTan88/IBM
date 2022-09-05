from cmath import nan
import pandas as pd
import numpy as np
from openpyxl import load_workbook
import csv





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


# append all the data to dictionary, get the data ready to be writre to txt file
def AggregateData(num_schema, list_len_table, df):
    start_row = 0
    dict = {}
    for i in range(num_schema):  # iterations: number of schema (24)
        list_current_table_str = []
        if str(df.iloc[start_row][0]) == 'nan':  # jump to the nonempty line
            start_row += 1
        
        # convert exl file data to the string that are ready to be inserted 
        for j in range(list_len_table[i]+1):  # iterations: length of current table -> [7, 13, 11, 82, 4, 354, 1018, 41, 1018, 9, 7, 6, 8, 13, 5, 795, 194, 7, 8, 4, 5, 8, 16, 13]

            # SET ... ON
            # GO
            if j == 0:  # insert schema.table
                schema = df.iloc[start_row][0].split(".")
                schema = "[" + schema[0] + "]" + "." + "[" + schema[1] + "]"  # [collection].[ProductType]
                sql_script = 'SET IDENTITY_INSERT ' + schema + ' ON'
                list_current_table_str.append(sql_script)
                list_current_table_str.append("GO")
            
            # get column names
            elif j == 1 :
                col_names = df.iloc[start_row].dropna().values
                col_names = ", ".join("[" + item + "]" for item in col_names)  # [ProductTypeId], [ProductTypeName], ... 
                col_names = "(" + col_names + ")"
            
            # ignore the descriptions
            elif j == 2: 
                pass

            # get values
            elif j >= 3 and j <= list_len_table[i]-1:
                values = df.iloc[start_row].dropna().values
                values = ", ".join(item for item in values)
                values = "(" + values + ")"
                insert_script = "INSERT " + schema + " " + col_names + " VALUES " + values
                list_current_table_str.append(insert_script)
                list_current_table_str.append("GO")
            
            # SET ... OFF
            # GO
            else:
                sql_script_final = 'SET IDENTITY_INSERT ' + schema + ' OFF'
                list_current_table_str.append(sql_script_final)
                list_current_table_str.append("GO")
            
            start_row += 1
        
        dict[f'Schema{i+1}'] = list_current_table_str
    
    return dict



            

if __name__ == "__main__":
    xlsx_file_path = 'MultiDF.xlsx'
    export_path = 'test.txt'
    empty_count = 0
    df_excel = pd.read_excel(xlsx_file_path, header=None)
    
    # get number of schema
    num_schema = CalculateNumTables(df_excel)

    # create the list of row numbers of different tables
    list_len_table = CalculateNumRows(num_schema, df_excel)

    # aggregate the data to be wrote
    dict_aggData = AggregateData(num_schema, list_len_table, df_excel)

    # write to txt file
    with open(export_path, 'w') as export_file:
        writer = csv.writer(export_file)
        for schema, script in dict_aggData.items():
            for lines in script:
                writer.writerow([lines])




