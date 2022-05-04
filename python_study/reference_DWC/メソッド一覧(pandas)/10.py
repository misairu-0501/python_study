#duplicated()
import pandas as pd
df = pd.DataFrame(data = {'name': ['A', 'B', 'C', 'C'], '国語': [90, 60, 30, 30], '数学': [70, 100, 90, 90]})

print(df.duplicated())
print(df[df.duplicated()])

print(df.duplicated(subset=['name']))

print(df.duplicated(keep='last'))

print(df.duplicated(keep='first'))

print(df.duplicated(keep=False))

