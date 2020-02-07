"""
Joshua Stough
DIP

Histogram equalization on a color image, with plotting of the histograms.
"""

import matplotlib.pyplot as plt
import scipy.ndimage as ndimage
import numpy as np


#Load an image and normalize to [0,1]
I = plt.imread('underExposed.jpg').astype(float)
I = I - I.ravel().min()
I = I/I.ravel().max()



#Scaled per channel

IE = np.zeros(I.shape)

for channel in range(3):
    hist, bins = np.histogram(I[...,channel], bins=np.arange(257) / 256)
    CDF = np.cumsum(hist) / sum(hist)

    Ir = np.interp(I[...,channel], xp=bins[:-1], fp=CDF)
    IE[...,channel] = Ir




allbins = np.unique(I.ravel())

f, ax1 = plt.subplots(1,2, figsize=(10,3))
ax1[0].imshow(I) #https://matplotlib.org/api/_as_gen/matplotlib.pyplot.imshow.html
ax1[0].set_title('Original Image')

ax1[1].hist(I[...,0].ravel(), allbins, alpha = .6, label = 'red', color = 'r')
ax1[1].hist(I[...,1].ravel(), allbins, alpha = .6, label = 'green', color = 'g')
ax1[1].hist(I[...,2].ravel(), allbins, alpha = .6, label = 'blue', color = 'b')
ax1[1].legend(loc = 'upper right')
plt.show()




f, ax2 = plt.subplots(1,2, figsize=(10,3))
ax2[0].imshow(IE) #https://matplotlib.org/api/_as_gen/matplotlib.pyplot.imshow.html
ax2[0].set_title('Image Equalized Per Channel')

ax2[1].hist(IE[...,0].ravel(), 250, alpha = .6, label = 'red', color = 'r')
ax2[1].hist(IE[...,1].ravel(), 250, alpha = .6, label = 'green', color = 'g')
ax2[1].hist(IE[...,2].ravel(), 250, alpha = .6, label = 'blue', color = 'b')
ax2[1].legend(loc = 'upper right')
plt.show()
