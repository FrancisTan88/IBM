import csv
import pandas as pd
import numpy as np

# INSERT INTO common.SystemDropDownList(Code, Type, Name, LanguageEnglish, LanguageLocal, Description,  ParentCode, SortNo, IsEnable, IsSystemGen, CreateUserNo, CreateTime) Values
# (‘${Post Code}’, ‘AddressPostCode’, ‘${Post Code}‘, ‘${Post Code}‘, ‘${Post Code}‘, ‘${Post Code}’,  (SELECT [Code] FROM common.SystemDropDownList
# where Type=‘AddressLevel2’ and Name=${City} and ParentCode=${State code}), ${Post Code}, True, true, ‘00000’, GETDATE())

data = pd.read_excel('Book1.xlsx')
export_path = '/Users/kian199887/Downloads/Bernie_github_repo/chailease-log-analyzer/sql.txt'
list = []
for i in range(len(data)):
    post_code = data['Post Code'].iloc[i]
    city = data['City'].iloc[i]
    state_code = data['State code'].iloc[i]
    string = "INSERT INTO common.SystemDropDownList(Code, Type, Name, LanguageEnglish, LanguageLocal, Description,  ParentCode, SortNo, IsEnable, IsSystemGen, CreateUserNo, CreateTime) Values" + f"('{post_code}', 'AddressPostCode', '{post_code}', '{post_code}', '{post_code}', 'AddressLevel2',  (SELECT [Code] FROM common.SystemDropDownList where Type='AddressLevel2' and Name='{city}' and ParentCode='{state_code}'), {post_code}, True, true, '00000', GETDATE())"
    list.append(string)

df = pd.DataFrame(list, columns=['SQL query'])
df.to_csv(export_path, header=False, index=False)



