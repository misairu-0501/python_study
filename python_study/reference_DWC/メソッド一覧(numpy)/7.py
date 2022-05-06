#random()
#randint()
#uniform()
import numpy as np
print(np.random.random((3, 3, 3)))
print(np.random.random_sample((3, 3, 3)))

print(np.random.randint(4))
print(np.random.randint(4, 12))
print(np.random.randint(4, 12, (3, 2)))

print(np.random.uniform())
print(np.random.uniform(0))
print(np.random.uniform(0, 10))
print(np.random.uniform(0, 10, (2,3)))
