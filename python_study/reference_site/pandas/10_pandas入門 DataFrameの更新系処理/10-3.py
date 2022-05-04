import pandas as pd
df = pd.DataFrame([[1, 10], [2, 20], [3, 30], [4, 40]], columns=['col1', 'col2'], index=['a', 'b', 'c', 'd'])

#行の削除
print(df.drop('a'))
print(df.drop(['a', 'b']))

#列の削除
print(df.drop('col1', axis=1))

#要素の更新
df2 = df.at['a', 'col1'] = 999
print(df2)