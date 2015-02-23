import numpy as np
a = 0.5*np.ones((4,3),dtype=float)
a[2][1] = 5
b = sum(sum(np.power(a,2)))
print a
print b