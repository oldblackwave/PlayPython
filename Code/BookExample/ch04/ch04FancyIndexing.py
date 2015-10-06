import numpy as np
from numpy.matlib import randn

arr = np.empty((8,4))
for i in range(8):
    arr[i] = i
    
print(arr)
print('\n')

###############################################################

print(arr[[4,3,0,6]])
print('\n')

print(arr[[-3,-5,-7]])
print('\n')

###############################################################

arr = np.arange(32).reshape((8,4))
print(arr)
print('\n')

###############################################################

print(arr[[1,5,7,2],[0,3,1,2]])
print('\n')

###############################################################

print(arr[np.ix_([1,5,7,2],[0,3,1,2])])
print('\n')

###############################################################

arr = np.arange(15).reshape((3,5))
print(arr)
print('\n')
print(arr.T)
print('\n')
###############################################################

arr = np.random.randn(6,3)
print(np.dot(arr.T, arr))
print('\n')
###############################################################

arr = np.arange(16).reshape((2,2,4))
print(arr)
print('\n')
print(arr.transpose((0,1,2))) #2,2,4
print('\n')
print(arr.transpose((0,2,1))) #2,4,2
print('\n')
print(arr.transpose((1,0,2))) #2,2,4
print('\n')
print(arr.transpose((1,2,0))) #2,4,2
print('\n')
print(arr.transpose((2,1,0))) #4,2,2
print('\n')
print(arr.transpose((2,0,1))) #4,2,2
print('\n')
###############################################################

print(arr.swapaxes(1,2))
print('\n')
print(arr.swapaxes(2,1))
print('\n')

###############################################################



