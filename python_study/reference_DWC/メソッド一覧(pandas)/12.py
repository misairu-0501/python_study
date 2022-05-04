#isnull()
import pandas as pd
import numpy as np
df = pd.DataFrame(data = {'name': ['A', 'B', 'C'], '国語': [90, 60, np.nan], '数学': [70, 100, 90]})

print(df)
print(df.isnull())