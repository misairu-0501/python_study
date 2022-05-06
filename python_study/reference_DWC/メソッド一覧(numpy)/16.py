#ndenumerate()
import numpy as np

for i in np.ndenumerate([1, 2, 4]):
  print(i)

for i in np.ndenumerate(np.arange(0, 9).reshape(3, 3)):
  print(i)
