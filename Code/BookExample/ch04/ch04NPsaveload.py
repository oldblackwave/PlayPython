import numpy as np


###############################################################
arr = np.arange(10)
np.save('some_array',arr)

arr = np.load('some_array.npy')
print(arr)
###############################################################