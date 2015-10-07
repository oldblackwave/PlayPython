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



###############################################################




