#diag
import numpy as np

arr = [1, 2, 3, 4]
print(arr)
print(np.diag(arr))

arr_2 = np.arange(0, 9).reshape((3, 3))
print(arr_2)
print(np.diag(arr_2))
print(np.diag(arr_2, k=1))
print(np.diag(arr_2, k=-1))
