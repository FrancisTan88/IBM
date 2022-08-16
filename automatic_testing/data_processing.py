import pandas as pd
import numpy as np 
import xlsxwriter

df1 = pd.DataFrame({
    'col1': ['aaa', 'bbb', 'ccc'],
    'col2': ['ddd', 'eee', 'fff']
})

df2 = pd.DataFrame({
    'col1': ['aaa', 'bbb', 'ccc', 'kkk'],
    'col2': ['ddd', 'eee', 'fff', 'ppp'],
    'col3': ['ddd', 'eee', 'fff', 'ppp']
})

writer = pd.ExcelWriter('MultiDF.xlsx', engine='xlsxwriter')   
workbook=writer.book
worksheet=workbook.add_worksheet('sheet1')
writer.sheets['sheet1'] = worksheet
df1.to_excel(writer,sheet_name='sheet1',startrow=0 , startcol=0)   
df2.to_excel(writer,sheet_name='sheet1',startrow=10, startcol=0) 







