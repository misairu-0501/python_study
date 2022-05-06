#pad()
import numpy as np

arr = np.arange(1, 5)
print(arr)

arr_2 = np.pad(arr, (1, 4))
print(arr_2)

arr_3 = np.pad(arr, (1, 3), mode = 'edge')
print(arr_3)

arr = np.ones((3, 3))
print(arr)

arr_2 = np.pad(arr, (1, 2))
print(arr_2)
