import pandas as pd
df = pd.DataFrame([[3, 10, 200], [2, 30, 100], [4, 40, 300], [1, 20, 200]], columns=['col1', 'col2', 'col3'])

print(df)

print(df.sort_values(['col1', 'col2'], ascending=[True, False]))