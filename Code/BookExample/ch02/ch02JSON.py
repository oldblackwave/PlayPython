import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pylab
import json

from matplotlib.pyplot import plot
from numpy import arange
from gc import get_count
from collections import defaultdict

from collections import Counter

path = 'usagov_bitly_data2012-03-16-1331923249.txt'




#records = [json.loads(line) for line in open(path)] #return List
records = []
for line in open(path):
    #print(type(line),line)
    records.append(json.loads(line))

#print(type(records).records)
'''
print(type(records),records[0])
print('\n')
print(records[0]['a'])
print(records[0]['tz'])
print(records[0]['nk'])
print(records[0]['c'])
print(records[0]['g'])
print(records[0]['h'])
print(records[0]['l'])
print(records[0]['hh'])
print(records[0]['r'])
print('\n')
'''
###############################################################

time_zones = [rec['tz'] for rec in records if 'tz' in rec]#Get all items with 'tz'
print(time_zones)
#print(time_zones[:10])
print(len(time_zones))
print('\n')


###############################################################


def get_counts(sequence):#Return Number
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts

def get_counts2(sequence):#Return Number
    counts = defaultdict(int)
    for x in sequence:
        counts[x] += 1
    return counts

_timezonesCounts = get_counts(time_zones)
#print(_timezonesCounts)
print(_timezonesCounts['America/New_York'])
print(len(_timezonesCounts))
print('\n')

_timezonesCounts2 = get_counts2(time_zones)
print(_timezonesCounts2['America/New_York'])
print(len(_timezonesCounts2))
print('\n')
###############################################################
'''
_hRec = [rec['h'] for rec in records if 'h' in rec]
print(type(_hRec),_hRec)
_hRecCount = get_counts(_hRec)
print(_hRecCount)
print(_hRecCount['xaOGZY'])
print('\n')

_hRec.append('hahahaah')
print(_hRec)
_hRecCount2 = get_counts2(_hRec)
print(_hRecCount2)
print(_hRecCount2['xaOGZY'])

print('\n')
'''
###############################################################

def top_counts(count_dict, n=10):
    value_key_pairs = [(count,tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    print(type(value_key_pairs),type(value_key_pairs[0]))
    return value_key_pairs

def top_counts2(count_dict, n = 10):
    value_key_pairs = []
    for tz, count in count_dict.items():
        value_key_pairs.append([count,tz])
    value_key_pairs.sort()
    return value_key_pairs

print(top_counts(_timezonesCounts))
print(top_counts2(_timezonesCounts))

###############################################################

_timeZoneCollectionCounts = Counter(time_zones)
print(_timeZoneCollectionCounts.most_common(10))

###############################################################

