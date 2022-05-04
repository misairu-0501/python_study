#drop_duplicates()
import pandas as pd
df = pd.DataFrame(data = {'name': ['A', 'B', 'C', 'C'], '国語': [90, 60, 30, 30], '数学': [70, 100, 90, 90]})

print(df)
print(df.drop_duplicates())
print(df.drop_duplicates(keep='last'))
print(df.drop_duplicates(keep=False))