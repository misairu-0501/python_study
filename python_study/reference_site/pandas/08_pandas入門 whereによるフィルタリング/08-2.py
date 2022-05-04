import pandas as pd
s = pd.Series([1, 2, 3])

print(s[s > 1])

print(s.where(s > 1))