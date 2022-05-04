import pandas as pd
df = pd.DataFrame([[1, 10], [2, 20], [3, 30], [4, 40]], columns=['col1', 'co2'], index=['a', 'b', 'c', 'd'])
s = pd.Series([1, 1, 1, 1], index=['a', 'b', 'c', 'd'])

df['new_col'] = s
print(df)

df['col1'] = s
print(df)
