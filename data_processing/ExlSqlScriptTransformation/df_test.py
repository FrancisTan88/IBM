import pandas as pd 

df = pd.DataFrame({
    'a': ['x', 'y', 'z'],
    'b': ['h', 'j', 'k']
})
list2 = [1,2,3]
df['a'] = "N" + df['a']
df['a'] = df['a'].replace("N", "Q")
df['b'] = list2

# print('(' + str(list(df.columns)) + ')')
print(tuple(df.iloc[0]))
# print(type(df.iloc[0]))