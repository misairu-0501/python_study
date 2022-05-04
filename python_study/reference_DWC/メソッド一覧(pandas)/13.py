#merge
#values
import pandas as pd
df1 = pd.DataFrame({'id': [1, 2, 3, 4, 5], 'item_id': ['A', 'B', 'C', None, 'G']})
df2 = pd.DataFrame({'id': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'], 'item': ['シャンプー', 'リンス', '石鹸', '洗顔', '歯磨き', '歯磨き粉', '洗剤', '柔軟剤']})

df3 = df1.merge(df2, left_on='item_id', right_on='id')
print(df3)

df4 = df1.merge(df2, how='left', left_on='item_id', right_on='id')
print(df4)

df5 = df1.merge(df2, how='right', left_on='item_id', right_on='id')
print(df5)

df6 = df2['item'].values
print(df6)
print(list(df6))