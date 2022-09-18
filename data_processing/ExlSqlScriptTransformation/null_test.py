import pandas as pd
import numpy as np



col = ['a', 'b', 'c']
val = [1, np.nan, 2]
empty = pd.DataFrame(columns=col)
empty.loc[len(empty)] = val
# rowdata = empty.iloc[0]
# isNull = rowdata.isnull()
# rowdata[isNull] = "NULL"
# print(empty)

dict = {}
dict['tmp'] = empty
print(dict)
k = list(dict.values())
print(k)
print(k[0])
# print(v)

# print(isNull)
# print(rowdata[isNull])

# print(empty)