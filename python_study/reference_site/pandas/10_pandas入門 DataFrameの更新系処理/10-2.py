import pandas as pd
df = pd.DataFrame([[1, 10], [2, 20], [3, 30], [4, 40]], columns=['col1', 'col2'], index=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame([[9, 99]], columns=['col1', 'col2'], index=['x'])
df3 = df.append(df2)

print(df3)