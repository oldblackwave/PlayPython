import numpy as np



###############################################################
data1 = [6,7.5,8,0,1]
arr1 = np.array(data1)
print(arr1)
print('\n')

###############################################################

data2 = [
        [1,2,3,4],[5,6,7,8]
        ]
arr2 = np.array(data2)
print(arr2)
print('\n')
print(arr2.ndim)##matrix of array
print('\n')
print(arr2.shape)
print('\n')
###############################################################
print(arr1.dtype)
print(arr2.dtype)
print('\n')
###############################################################

print(np.zeros(10))
print('\n')
print(np.zeros((3,6)))
print('\n')
print(np.empty((2,3,2)))
print('\n')
###############################################################
print(np.arange(15))
print('\n')

###############################################################


