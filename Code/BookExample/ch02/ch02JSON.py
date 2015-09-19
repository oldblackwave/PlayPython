import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pylab
import json

from matplotlib.pyplot import plot
from numpy import arange
from gc import get_count
from collections import defaultdict

path = 'usagov_bitly_data2012-03-16-1331923249.txt'

def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts

def get_counts2(sequence):
    counts = defaultdict(int)
    for x in sequence:
        counts[x] += 1
    return counts

records = [json.loads(line) for line in open(path)]

print(records[0])
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

time_zones = [rec['tz'] for rec in records if 'tz' in rec]
print(time_zones)
print(time_zones[:10])
print('\n')

_timezonesCounts = get_counts(time_zones)
print(_timezonesCounts)
print(_timezonesCounts['America/New_York'])

_hRec = [rec['h'] for rec in records if 'h' in rec]
print(_hRec)
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

