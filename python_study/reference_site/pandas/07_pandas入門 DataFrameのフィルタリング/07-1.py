import pandas as pd
df = pd.DataFrame([['A', 10], ['B', 20], ['C', 30], ['D', 40]], columns=['col1', 'col2'])
l = [True, False, True, False]
print(df[l])

print(df.index % 2 == 0)
print(df[df.index % 2 == 0])

print(df[df.col1 == "C"])

print(df[df.col2 > 10])

cond = df.col1.str.contains('.*A')
print(df[cond])