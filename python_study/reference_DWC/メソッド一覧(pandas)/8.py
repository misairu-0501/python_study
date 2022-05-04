#sum()
#mean()
import pandas as pd
df = pd.DataFrame(data = {'name': ['A', 'B', 'C'], '国語': [90, 60, 30], '数学': [70, 100, 90]})
print(df)

print(df.sum())
print(df.sum(axis=1))

print(df.mean())
print(df.mean(axis=1))