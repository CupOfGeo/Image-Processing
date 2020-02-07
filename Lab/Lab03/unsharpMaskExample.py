"""
Joshua Stough
DIP

Using generic filter in scipy.ndimage to blur and other things an input image.
https://docs.scipy.org/doc/scipy-0.16.1/reference/generated/scipy.ndimage.filters.generic_filter.html
"""

import matplotlib.pyplot as plt
import scipy.ndimage as ndimage
import numpy as np

#simple blur
def myfunc(x):
    return x.mean()


I = plt.imread('canyon.jpg').astype(float)
I = I/I.ravel().max()

Ib = np.zeros(I.shape)
Out = np.zeros(I.shape[:2])

for chan in range(3):
    ndimage.generic_filter(I[:, :, chan], function=myfunc, size=5, output=Out, mode='reflect')
    Ib[...,chan] = Out.copy();

f, axarr = plt.subplots(1,2, figsize=(10, 3))
axarr[0].imshow(I)
axarr[0].set_title('Original')

axarr[1].imshow(Ib)
axarr[1].set_title('Blurred')


#Now sharpen
D = I - Ib
Isharp = I + D
Isharp[Isharp < 0] = 0
Isharp[Isharp > 1] = 1

f, axarr = plt.subplots(1,2, figsize=(10, 3))

#normalize to [0,1] the difference image, for display.
D = D - D.ravel().min()
D = D/D.ravel().max()

axarr[0].imshow(D)
axarr[0].set_title('Orginal-Blurred (D)')

axarr[1].imshow(Isharp)
axarr[1].set_title('Sharped (Original + D)')



