"""
Joshua Stough
DIP

Trying to display the Euclidean and the Haar basis transforms in simple 4x4.
Then, show a 4x4 image, its basis transform, and its reconstruction.
"""

import matplotlib.pyplot as plt
import numpy as np
import skimage
import scipy.ndimage as ndimage



#The 4x4 Euclidean basis. Each row represents an
#orthogonal (independent) direction in 4D space.
E = np.eye(4,4)

#For display
fe, axe = plt.subplots(4,4, figsize=(10,10))

for i in range(4):
    for j in range(4):
        #Taking the outer product of a row with any other
        #creates a 4x4 basis image.
        Bij = np.outer(E[i,:], E[j,:])
        axe[i][j].imshow(Bij, cmap='gray')
        axe[i][j].axes.get_xaxis().set_visible(False)
        axe[i][j].axes.get_yaxis().set_visible(False)

#plt.suptitle('Euclidean Basis') #gets in the way if using tight_layout(),
#see below.
plt.show()

#####################################################################

#The 4x4 Haar basis, see DIP 6.9.
H = .5*np.array([[1,1,1,1], [1,1,-1,-1],
              [np.sqrt(2),-np.sqrt(2),0,0],
              [0,0,np.sqrt(2),-np.sqrt(2)]])

fh, axh = plt.subplots(4,4, figsize=(10,10))

for i in range(4):
    for j in range(4):
        # Construct that Haar basis and display it
        Bij = np.outer(H[i,:], H[j,:])
        axh[i][j].imshow(Bij, cmap='gray', vmin=-1, vmax=1)
        axh[i][j].axes.get_xaxis().set_visible(False)
        axh[i][j].axes.get_yaxis().set_visible(False)

#plt.suptitle('Haar Basis')
plt.show()

fe.tight_layout() #minimize padding for slightly better visual.
fh.tight_layout()

#https://stackoverflow.com/questions/5812960/change-figure-window-title-in-pylab
fe.canvas.set_window_title('Euclidean/Standard Basis')
fh.canvas.set_window_title('Haar Basis')


#####################################################################


#So now, a simple color image. F is "F", CF is a random color version.
F = np.array([[0, 1, 1, 1], [0, 1, 0, 0], [0, 1, 1, 1], [0, 1, 0, 0]])
CF = np.concatenate([np.expand_dims(F*np.random.rand(4,4), axis=2)
                     for x in range(3)], axis=2)

#the transform image: We decompose the image according to
#H by T = H*F*H', where H' is H.transpose(). T is a 4x4
#of the transform coefficients.
T = np.matmul(H, np.matmul(F, H.transpose()))

#The reconstructed image: Properties of the orthonormal
#basis make reversing the transform as easy as applying
#H and H' in a different order: F = H'*T*H
TR = np.matmul(H.transpose(), np.matmul(T, H))

f, ax = plt.subplots(1,3, figsize=(12,3))

ax[0].imshow(F, cmap='gray')
ax[0].set_title('Image')

ax[1].imshow(T, cmap='gray', vmin=T.min(), vmax=T.max())
ax[1].set_title('Transform Coefficients')

ax[2].imshow(TR, cmap='gray')
ax[2].set_title('Reconstruction')

f.tight_layout()
f.canvas.set_window_title('Image, Transform, and Reconstruction')

