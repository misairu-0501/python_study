import pandas as pd
df = pd.DataFrame([[1, 10], [2, 20], [3, 30]], columns=['col1', 'col2'])
print(df)
print(len(df))
print(df.size)
print(df.count())
print(df.mean())
print(df.describe())