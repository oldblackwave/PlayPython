import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pylab
import json

from matplotlib.pyplot import plot
from numpy import arange

plt.plot(arange(20))

pylab.show()


path = 'usagov_bitly_data2012-03-16-1331923249.txt'
print(open(path).readline())

#_allLine = open(path).read()
#print(_allLine)

records = [json.loads(line) for line in open(path)]
print(records[0])
print(records[0]['tz'])


