import numpy as np
from numpy.core.multiarray import dtype

arr1 = np.array([1,2,3], dtype=np.float64)
arr2 = np.array([1,2,3], dtype=np.int32)
print(arr1.dtype)
print(arr2.dtype)
print('\n')
###############################################################

arr = np.array([1,2,3,4,5])
print(arr.dtype)
float_arr = arr.astype(np.float64)
print(float_arr.dtype)
print('\n')
###############################################################

arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
print(arr)
print(arr.astype(np.int32))
print('\n')
###############################################################

numeric_strings = np.array(['1.25','-9.6','42'], dtype=np.string_)
print(numeric_strings.astype(float))
print('\n')
###############################################################

int_array = np.arange(10)
calibers = np.array([.22,.270,.357,.380,.44,.50], dtype=np.float64)
print(int_array.astype(calibers.dtype))
print('\n')
###############################################################

empty_uint32 = np.empty(8, dtype='u4')
print(empty_uint32)
print('\n')
###############################################################

