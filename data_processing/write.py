import csv
import pandas as pd

export_file = 'test.txt'
str1 = 'SET IDENTITY_INSERT [collection].[ProductType] ON'
str2 = 'GO'
str3 = "INSERT [collection].[ProductType] ([ProductTypeId], [ProductTypeName]) VALUES (2, N'EPP')"
df = pd.DataFrame({
    'col1': [str1]
})

print([str3])


with open(export_file, 'w') as write_file:
    
    writer = csv.writer(write_file)
    writer.writerow([str1])
    writer.writerow([str2])
    writer.writerow([str3])
    
    df.to_csv(write_file, header=None, index=None)

    





