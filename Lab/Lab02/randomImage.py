"""
Joshua Stough
DIP

Creating a couple of random images.
"""

import matplotlib.pyplot as plt
import numpy as np
import numpy.random as random

f, axarr = plt.subplots(1,2, figsize=(10, 3))

#Uniform first, rand in the range[0,1)
IU = np.concatenate([random.rand(100,100,1) for x in range(3)], axis = 2)
axarr[0].imshow(IU)
axarr[0].set_title('Uniform Random Image')


#Normal random, which is usually mean 0, var 1. We'll normalize intensities to
#between [0,1]
IN = np.concatenate([random.randn(100,100,1) for x in range(3)], axis = 2)
IN = IN - IN.ravel().min() #Make the minimum 0
IN = IN/IN.ravel().max()  #Make max 1
axarr[1].imshow(IN)
axarr[1].set_title('Normal Random Image')

