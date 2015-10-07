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

###############################################################

arr = randn(4,4)
print(arr)
print('\n')

print(np.where(arr > 0,2,-2))
print('\n')

print(np.where(arr>0,2,arr))
print('\n')

###############################################################

arr = np.random.randn(5,4)
print(arr.mean())
print(np.mean(arr))
print(arr.sum())
print('\n')

print(arr.mean(axis = 1))
print(arr.sum(0))

###############################################################

arr = np.array([[0,1,2],[3,4,5],[6,7,8]])
print(arr)
print(arr.cumsum(0))
print(arr.cumprod(1))
print('\n')

###############################################################

arr = randn(100)
print((arr>0).sum())
print('\n')

###############################################################

bools = np.array([False, False, True, False])
print(bools.any())
print(bools.all())
print('\n')

###############################################################

arr = randn(8)
print(arr)
arr.sort()
print(arr)

print('\n')

arr = randn(5,3)
print(arr)
arr.sort(1)
print(arr)

print('\n')

large_arr = randn(100)
large_arr.sort()
print(large_arr[int(0.05 * len(large_arr))])

print('\n')


###############################################################

names = np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])
print(np.unique(names))

ints = np.array([3,3,3,2,2,1,1,4,4])
print(np.unique(ints))


print(sorted(set(names)))
print('\n')

values = np.array([6,0,0,3,2,5,6])
print(np.in1d(values, [2,3,6]))
print('\n')


###############################################################









###############################################################









