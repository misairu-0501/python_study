#unravle_index()
import numpy as np
arr = np.arange(0, 15).reshape((3, 5))
print(arr)

print(np.unravel_index(5, (3, 4, 2)))

print(np.unravel_index(5, arr.shape))

print(np.unravel_index(np.argmax(arr), arr.shape))