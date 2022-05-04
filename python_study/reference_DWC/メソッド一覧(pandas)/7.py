#concat()
#reset_index
#drop
import pandas as pd
df1 = pd.DataFrame(data = {'name': ['A', 'B', 'C'], '国語': [90, 60, 30], '数学': [70, 100, 90]})
df2 = pd.DataFrame(data = {'name': ['G', 'H'], '国語': [30, 40], '数学': [65, 45]})

df3 = pd.concat([df1, df2])
print(df3)

df4 = pd.concat([df1, df2], ignore_index=True)
print(df4)

df5 = pd.concat([df1, df2], axis=1)
print(df5)

print(df3.reset_index())
print(df3.reset_index(drop=True))

print(df4.drop([1, 3, 4]))
print(df4.drop(['name', '国語'], axis=1))