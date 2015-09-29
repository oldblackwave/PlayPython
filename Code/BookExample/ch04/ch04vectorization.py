import numpy as np

arr = np.array([[1.,2.,3.],[4.,5.,6.]])
print(arr)
print('\n')
###############################################################

print(arr * arr)
print(arr - arr)
print('\n')
print(1/arr)
print(arr ** 0.5)
print('\n')

###############################################################

arr = np.arange(10)
print(arr)
print(arr[5])
print(arr[5:8])
arr[5:8]=12
print(arr)
print('\n')

arr_slice = arr[5:8]
arr_slice[1]=12345
print(arr)
arr_slice[:]=64
print(arr)
print('\n')

arr_slice = arr[5:8].copy()
print(arr_slice)
arr_slice[1] = 88
print(arr)
print(arr_slice)
print('\n')
###############################################################


