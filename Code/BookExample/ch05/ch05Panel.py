import numpy as np
import pandas as pd
import pandas.io.data as web

import pandas.io.data as web

from pandas import Series, DataFrame
from numpy import NaN as NA

###############################################################

pdata = pd.Panel(dict((stk, web.get_data_yahoo(stk, '9/1/2015', '10/1/2015'))
                      for stk in ['AAPL','GOOGL','MSFT','IBM']))

print(pdata)
print('\n')

###############################################################

pdata = pdata.swapaxes('items', 'minor')
print(pdata['Adj Close'])
print('\n')
print(pdata.ix[:,'9/1/2015',:])
print('\n')
print(pdata.ix['Close',:'9/5/2015',:])
print('\n')

###############################################################

stacked = pdata.ix[:,'9/25/2015':,:].to_frame()
print(stacked)
print('\n')

print('Back TO Panel \n')
print(stacked.to_panel())









