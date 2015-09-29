import numpy as np

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2d)
print(arr2d[2])
print('\n')
print(arr2d[0][2])
print(arr2d[0,2])

###############################################################

arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3d, '\n' ,arr3d.ndim)
print('\n')
print(arr3d[0])
print('\n')
old_values = arr3d[0].copy()
arr3d[0] = 42
print(arr3d)
print('\n')
arr3d[0] = old_values
print(arr3d)
print('\n')
print(arr3d[1,0])
print('\n')

###############################################################

print(arr2d)
print('\n')
print(arr2d[:2])
print('\n')
print(arr2d[:2,1:])
print('\n')
print(arr2d[1,:2])
print('\n')
print(arr2d[2,:1])
print('\n')
print(arr2d[:, :1])
print('\n')
arr2d[:2, 1:]=0
print(arr2d)
print('\n')

###############################################################

#Page 92

###############################################################



