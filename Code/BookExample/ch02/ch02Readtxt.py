import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pylab
import json

from matplotlib.pyplot import plot
from numpy import arange

path = 'usagov_bitly_data2012-03-16-1331923249.txt'
print(open(path).readline())

_allLine = open(path).read()
print(_allLine)

