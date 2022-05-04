import pandas as pd
s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(s1)

s2 = pd.Series([3, 4, 5, 6,], index=['c', 'd', 'e', 'f'])
print(s2)

print(s1 + s2)

