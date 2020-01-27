"""
Joshua Stough
DIP

Viewing a washed-out image and its histogram.
"""

import matplotlib.pyplot as plt
import numpy as np
import numpy.random as random

#We're going to normalize the image and deal with floating point.
I = plt.imread('washed.jpeg').astype('float')
I = I/I.ravel().max()

#The histogram bins are just let's say 256 bins in [0,1]
bins = np.arange(256)/256

f, axarr = plt.subplots(1,2, figsize=(10, 3))

axarr[0].imshow(I) #https://matplotlib.org/api/_as_gen/matplotlib.pyplot.imshow.html
axarr[0].set_title('Washed Out Image')

axarr[1].hist(I[...,0].ravel(), bins, alpha = .6, label = 'red', color = 'r')
axarr[1].hist(I[...,1].ravel(), bins, alpha = .6, label = 'green', color = 'g')
axarr[1].hist(I[...,2].ravel(), bins, alpha = .6, label = 'blue', color = 'b')
axarr[1].legend(loc = 'upper right')
plt.show()