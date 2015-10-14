import numpy as np
import pandas as pd

import pandas.io.data as web

from pandas import Series, DataFrame
from numpy import NaN as NA

###############################################################

frame = DataFrame({'a':range(7),'b':range(7,0,-1),
                   'c':['one','one','one','two','two','two','two'],
                   'd':[0,1,2,0,1,2,3]})

print(frame)
print('\n')

###############################################################

frame2 = frame.set_index(['c','d'])
print(frame2)
print('\n')

print(frame.set_index(['c','d'], drop=False))
print('\n')

print(frame2.reset_index())
print('\n')

###############################################################

ser = Series(np.arange(3.))
print(ser)
print('\n')

ser2 = Series(np.arange(3.), index=['a','b','c'])
print(ser2)
print('\n')
print(ser2[-1])
print('\n')
print(ser.ix[:1])
print('\n')

ser3 = Series(range(3), index=[-5,1,3])
print(ser3.iget_value(2))
print('\n')

###############################################################

frame = DataFrame(np.arange(6).reshape(3,2), index=[2,0,1])
print(frame.irow(0))

















