import pandas as pd
df = pd.DataFrame([[1, 10], [2, 20], [3, 30]], columns=['col1', 'col2'], index=['a', 'b', 'c'])
print(df)

print(df['col1'])
print(df.col2)
print(df.col2['a'])
print(df.col2.a)