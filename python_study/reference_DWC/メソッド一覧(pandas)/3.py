#to_csv()
#read_csv()
import pandas as pd
df = pd.DataFrame(data = {'name': ['A', 'B'], '国語': [90, 60], '数学': [70, 100]}, index={'a', 'b'})

df.to_csv('./3.csv', index=False, header=False)
df2 = pd.read_csv('./3.csv')
print(df2)
