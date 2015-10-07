import numpy as np
from numpy.matlib import randn
from numpy.linalg import inv, qr


###############################################################
arr = np.arange(10)
np.save('some_array',arr)

arr = np.load('some_array.npy')
print(arr)
###############################################################

np.savez('array_archive.npz', a=arr, b=arr)

arch = np.load('array_archive.npz')
print(arch['b'])


print('\n')
###############################################################

arr = randn(100)
np.savetxt('array_ex.txt',arr, delimiter=',')

arrtxt = np.loadtxt('array_ex.txt',delimiter=',')
print(arrtxt)

print('\n')
###############################################################

x = np.array([[1.,2.,3.],[4.,5.,6.]])
y = np.array([[6.,23.],[-1,7],[8,9]])

print(x)
print(y)
print('\n')

print(np.dot(x,y))

print(np.dot(x, np.ones(3)))

print('\n')
###############################################################

X = randn(5,5)
print(X)
mat = X.T.dot(X)

print(inv(mat))
print(mat.dot(inv(mat)))

q,r = qr(mat)
print(r)

