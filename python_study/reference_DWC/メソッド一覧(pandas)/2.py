#DataFrame()
import pandas as pd
df = pd.DataFrame(data = [['A', 90, 70], ['B', 60, 100]], index=['a', 'b'], columns=['名前', '国語', '数学'])
print(df)