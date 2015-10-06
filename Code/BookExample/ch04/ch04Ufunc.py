import numpy as np
import matplotlib.pyplot as plt
from numpy.matlib import randn
import pylab

###############################################################

arr = np.arange(10)
print(np.sqrt(arr))
print('\n')
print(np.exp(arr))
print('\n')

###############################################################

x = randn(8)
y = randn(8)
print(x)
print(y)
print('\n')
print(np.maximum(x,y))
print('\n')

###############################################################

points = np.arange(-5, 5, 0.01)
xs, ys = np.meshgrid(points, points)
print(ys)
print('\n')

###############################################################

z = np.sqrt(xs ** 2 + ys ** 2)
print(z)
plt.imshow(z, cmap = plt.cm.gray)
plt.colorbar()
#pylab.show()
print('\n')

###############################################################

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])

cond = np.array([True, False, True, True, False])
result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]

print(result)
print('\n')

###############################################################

result = np.where(cond, xarr, yarr)
print(result)
print('\n')




