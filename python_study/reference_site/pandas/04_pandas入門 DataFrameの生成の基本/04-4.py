import pandas as pd
s1 = pd.Series([100, 101, 102], index=['a', 'b', 'c'])
s2 = pd.Series([100, 101, 102], index=['b', 'c', 'd'])
df = pd.DataFrame({'col1': s1, 'col2': s2})
print(df)