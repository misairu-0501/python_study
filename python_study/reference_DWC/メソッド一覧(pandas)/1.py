#DataFrame()
import pandas as pd
df = pd.DataFrame(data = {'name': ['A', 'B'], '国語':[90, 60], '数学':[70, 100]}, index=['a', 'b'])

print(df)