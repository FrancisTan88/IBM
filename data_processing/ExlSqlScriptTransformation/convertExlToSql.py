from queue import Empty
import numpy as np 
import pandas as pd
from datetime import datetime

"""
Target: 
(1)add N''
(2)
"""

# # calculate the number of tables
# def CalculateNumTables(df):
#     empty_count = 0
#     for i in range(len(df)):
#         if str(df.iloc[i][0]) == 'nan':
#             empty_count += 1
#     num_schema = empty_count + 1  # number of schema in exl == 24
#     return num_schema



# # calculate the number of rows of different tables
# def CalculateNumRows(num_schema, df):
#     list_len_table = []
#     row = 0
#     first_table = True
#     for num in range(num_schema):
#         while row <= len(df)-1 and str(df.iloc[row][0]) != 'nan':
#             row += 1
#         if first_table:
#             list_len_table.append(row)
#             row += 1
#             first_table = False
#         else:
#             list_len_table.append(row - sum(list_len_table[:num]) - num)
#             row += 1
#     return list_len_table


def CalculateNumSchemas(df):
    count = 0
    for i in range(len(df)):
        if str(df.iloc[i][0]) == "nan":
            count += 1
    return count + 1 


# main script
if __name__ == '__main__':
    # read the file
    exl_path = "MultiDF.xlsx"
    data = pd.read_excel(exl_path)
    # with open(exl_path, 'r', encoding="utf-8") as read_file:
    #     data = read_file.readlines()
    
    # calculate the number of tables that exist in excel file
    num_schema = CalculateNumSchemas(data)  # 24
    # print(data)
    # print(num_schema)







    