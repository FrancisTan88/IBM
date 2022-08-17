from cmath import nan
from ntpath import join
import pandas as pd
import numpy as np
from openpyxl import load_workbook
import csv

xlsx_file_path = 'MultiDF2.xlsx'
export_path = 'XlsToSqlQuery.xlsx'
# writer = pd.ExcelWriter(export_path, engine='openpyxl')  
empty_count = 0
df = pd.read_excel(xlsx_file_path, header=None)
col = df.iloc[3]
name = col.dropna().values
name = ", ".join(item for item in name)
# list = [1,2,3]
# sum = sum(list[0:3])

print(df)
# print(col[0])
# print(col[1])