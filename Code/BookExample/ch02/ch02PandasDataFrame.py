from pandas import DataFrame, Series
from matplotlib.pyplot import plot
from numpy import arange
from gc import get_count

import pandas as pd 
import numpy as np
import json
import matplotlib.pyplot as plt
import pylab



path = 'usagov_bitly_data2012-03-16-1331923249.txt'

records = []
for line in open(path):
    records.append(json.loads(line))
    
###############################################################

frame = DataFrame(records)
#print(frame)
print(frame['tz'][:10])
print('\n')

tz_counts = frame['tz'].value_counts()
print(tz_counts[:10])
print('\n')

###############################################################

clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
print(tz_counts[:10])
print('\n')

###############################################################
#tz_counts[:10].plot(kind='barh', rot=0)
#pylab.show()

###############################################################
print(frame['a'][1])
print(frame['a'][50])
print(frame['a'][51])
print('\n')

###############################################################

result = Series([x.split()[0] for x in frame.a.dropna()])
print(result[:5])
print('\n')
###############################################################
print(result.value_counts()[:8])
print('\n')

###############################################################
cframe = frame[frame.a.notnull()]
operating_system = np.where(cframe['a'].str.contains('Windows'),'Windows','Not Windows')
print(operating_system[:5])
for line in operating_system[:5]:
    print(line)
print('\n')
    
###############################################################
by_tz_os = cframe.groupby(['tz', operating_system])
agg_counts = by_tz_os.size().unstack().fillna(0)
print(agg_counts[:10])
#agg_counts[:10].plot(kind='barh',rot=0)
#pylab.show()
 
###############################################################
indexer = agg_counts.sum(1).argsort()
print(indexer[:10])
   
    
