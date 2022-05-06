#reshape()
#shape
#ndim
import numpy as np
print(np.arange(15))
print(np.arange(15).reshape(3, 5))
print(np.arange(15).reshape(5, 3))

print(np.arange(15).shape)
print(np.arange(15).reshape(3, 5).shape)
print(np.arange(15).reshape(5, 3).shape)

print(np.arange(15).ndim)
print(np.arange(15).reshape(3, 5).ndim)
print(np.arange(15).reshape(5, 3).ndim)