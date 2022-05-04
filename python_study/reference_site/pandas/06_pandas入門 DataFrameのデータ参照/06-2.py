import pandas as pd
df = pd.DataFrame([[1, 10], [2, 20], [3, 30]], columns=['col1', 'col2'])
print(df)
print(df[1:2])

print(df.loc[0])
print(df.loc[1:2])
print(df.loc[0]['col1'])
print(df.iloc[1])
