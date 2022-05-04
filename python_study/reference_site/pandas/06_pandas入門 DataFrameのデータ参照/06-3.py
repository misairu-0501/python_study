import pandas as pd
df = pd.DataFrame([[1, 10], [2, 20], [3, 30]], index=['a', 'b', 'c'], columns=['col1', 'col2'])
print(df.at['a', 'col1'])
print(df.iat[1, 1])