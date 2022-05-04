#head()
#tail()
#colmns()
#index
import pandas as pd
df = pd.DataFrame(data = {'name': ['A', 'B', 'C', 'D', 'E', 'F'], '国語': [90, 60, 30, 40, 10, 45], '数学': [70, 100, 90, 65, 40, 80]}, index=['one', 'two', 'three', 'fow', 'five', 'six'])
print(df.head())
print(df.head(10))

print(df.tail())
print(df.tail(3))

print(df.columns)
print(df.index)