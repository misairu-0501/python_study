#dtypes
#astype
#nuniqu()
#loc[]
#info()
#iloc[]
import pandas as pd
df = pd.DataFrame(data = {'name':['A', 'B', 'C', 'D', 'E', 'F'], '国語':[90, 60, 30, 40, 10, 45], '数学': [70, 100, 90, 65, 40, 80]})
print(df.dtypes)

df1 = df[['国語', '数学']].astype('float64')
print(df1)

print(df.nunique())
print(df.nunique(axis=1))

print(df.loc[1])
print(df.loc[2:4])
print(df.loc[0:2,'国語'])

print(df.info())

print(df.iloc[0])
print(df.iloc[0:2])
print(df.iloc[1:3, 0:2])