import numpy as np
import random
import matplotlib.pyplot as plt
import pylab

from random import normalvariate


###############################################################

samples = np.random.normal(size=(4,4))
print(samples)

print('\n')
###############################################################

position = 0
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0,1) else -1
    position += step
    walk.append(position)

plt.plot(walk)
#pylab.show()


###############################################################

nsteps = 1000
draws = np.random.randint(0,2,size=nsteps)
steps = np.where(draws>0,1,-1)
walk = steps.cumsum()

#print(draws)
#print(steps)
#print(walk)

print(walk.min())
print(walk.max())
print((np.abs(walk)>=10).argmax())
print('\n')
###############################################################

nwalks = 5000
nsteps = 1000
draws = np.random.randint(0,2,size=(nwalks,nsteps))
#print(draws)
steps = np.where(draws>0, 1, -1)
#print(steps)
walks = steps.cumsum(1)
print(walks)
print('\n')
print(walks.max())
print(walks.min())

hits30 = (np.abs(walks) >= 30).any(1)
print(hits30)

print(hits30.sum())

###############################################################

crossing_times = (np.abs(walks[hits30]) >= 30).argmax(1)
print(crossing_times.mean())

print('\n')

steps = np.random.normal(loc=0, scale=0.25, size=(nwalks,nsteps))









