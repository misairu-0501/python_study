import pandas as pd
s = pd.Series([10, 20, 30, 40])
s[0] = 100
print(s)

s[0:2] = pd.Series([100, 200])
print(s)

print(type(list(s)))