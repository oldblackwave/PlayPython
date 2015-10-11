import numpy as np
import pandas as pd

from pandas import Series, DataFrame

###############################################################

frame = DataFrame(np.random.rand(4,3),
                  columns=list('bde'),
                  index=['Utah','Ohio','Texas','Oregon']
                  )

print(frame)
print('\n')
print(np.abs(frame))
print('\n')

###############################################################

f = lambda x:x.max() - x.min()
print(frame.apply(f))
print('\n')
print(frame.apply(f, axis=1))
print('\n')

###############################################################

def f(x):
    return Series([x.min(), x.max()], index=['min','max'])

print(frame.apply(f))
print('\n')

format = lambda x:'%.2f'%x
print(frame.applymap(format))

print('\n')
print(frame['e'].map(format))


    









