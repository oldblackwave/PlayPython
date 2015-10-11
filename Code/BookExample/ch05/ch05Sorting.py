import numpy as np
import pandas as pd

from pandas import Series, DataFrame

###############################################################

obj = Series(range(4), index=['d','a','b','c'])
print(obj.sort_index())

print('\n')

frame = DataFrame(np.arange(8).reshape((2,4)),
                  index=['three','one'],
                  columns=['d','a','b','c']
                  )

print(frame)
print('\n')
print(frame.sort_index())
print('\n')
print(frame.sort_index(axis=1))
print('\n')
print(frame.sort_index(axis=1,ascending=False))
print('\n')

###############################################################

obj = Series([4,7,-3,2])
print(obj.order())
print('\n')

obj = Series([4, np.nan, 7, np.nan, -3, 2])
print(obj.order())
print('\n')

###############################################################

frame = DataFrame({'b':[4,7,-3,2],
                   'a':[0,1,0,1]
                   })
print(frame)
print(frame.sort_index(by='b'))
print(frame.sort_index(by=['a','b']))





















print('\n')

