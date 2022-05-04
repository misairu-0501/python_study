import pandas as pd
df = pd.DataFrame([[1, 10], [2, 20], [3, 30], [4, 40]], columns=['col1', 'col2'])

print(df[df['col1'] > 2])

print(df.where(df['col1'] > 2))

print(df.where(df['col1'] > 2, 0))

pad = pd.DataFrame([[0, '-']] * len(df), columns=df.columns, index=df.index)

print(pad)

print(df.where(df['col1'] > 2, pad))