"""
Joshua Stough
DIP

Using mplot3d to show the colors of an image in RGB space.
https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

NUMPOINTS = 5000

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

I = plt.imread('bellagio.jpg')

#X is the N*M x 3 version of the image.
X = np.concatenate([np.expand_dims(IC, axis = 1) for IC in
                    [I[...,0].ravel(), I[...,1].ravel(), I[...,2].ravel()]], axis = 1)

#https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.choice.html
randomInds = np.random.choice(np.arange(X.shape[0]), NUMPOINTS, replace=False)

#Now plot those pixels in the 3d space.
ax.scatter(X[randomInds,0], X[randomInds,1], X[randomInds,2], c=X[randomInds, :]/255)

#Label the axes.
ax.set_xlabel('Red')
ax.set_ylabel('Green')
ax.set_zlabel('Blue')
