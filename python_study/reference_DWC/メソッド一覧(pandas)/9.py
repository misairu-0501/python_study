#count()
#describe()
#corr()
import pandas as pd
import numpy as np
df = pd.DataFrame(data = {'name': ['A', 'B', 'C'], '国語': [90, np.nan, 30], '数学': [70, 100, 90]})
print(df)
print(df.count())
print(df.count(axis=1))

df = pd.DataFrame(data = {'name': ['A', 'B', 'C'], '国語': [90, 60, 30], '数学': [70, 100, 90]})
print(df)
print(df.describe())
print(df.describe(include=['int64']))

print(df.corr())
