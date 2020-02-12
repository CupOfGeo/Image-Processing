"""
Joshua Stough
DIP

Some color clustering using k-means...
https://en.wikipedia.org/wiki/K-means_clustering
https://www.datascience.com/blog/k-means-clustering
https://sites.google.com/site/dataclusteringalgorithms/k-means-clustering-algorithm

Added an error image to the output.
"""

#from scipy.cluster.vq import kmeans2
import scipy.cluster.vq as vq
import matplotlib.pyplot as plt
import numpy as np

COLORS = 256

I = plt.imread('skyandsea.jpg')
#I is NxMx3

X = np.concatenate([np.expand_dims(IC, axis = 1) for IC in
                    [I[...,0].ravel(), I[...,1].ravel(), I[...,2].ravel()]], axis = 1)
#X is N*Mx3

#Needs floating point data to work with, we'll translate back.
Xf = X.copy().astype('float')

# Xf = vq.whiten(Xf)
# The kmeans documentation asks for this, but results seem easier to deal with
# if I don't use it.


#Ask kmeans to get us 256 colors.
[centers, labels] = vq.kmeans2(Xf, COLORS)
centersUint = centers.copy().astype('uint8')
#uint8 versions of the centers will clip to 0-255 for us, just in case.

# Why do some centers end up outside of [0, 255]? I tried to include all the centers,
# but then the colors associated with labels warp toward gray, kind of washing out
# the image...
# centerscopy = centers.copy()
# centerscopy = centerscopy - centerscopy.min()
# centerscopy = centerscopy/centerscopy.max()
# centersUint = np.array(255*centerscopy).astype('uint8')



#centers is 256x3 representative colors from the image, while
#labels is I.size indexes that tells which row of centers best
#represents (is closest to) each and every pixel of the image.

#Now, make an image consisting of the colors that each pixel got mapped to.
Ir = np.zeros(I.shape)
Ir[...,0] = np.reshape(centersUint[labels, 0], I.shape[:2])
Ir[...,1] = np.reshape(centersUint[labels, 1], I.shape[:2])
Ir[...,2] = np.reshape(centersUint[labels, 2], I.shape[:2])

#Somehow, Ir is still floating point, so the imshow colormap will be weird.
#We'll just cast it to uint8
Ir = Ir.astype('uint8')


#Visualize
f, ax = plt.subplots(1,3, figsize=(15,3))
ax[0].imshow(I)
ax[0].set_title('Original')

ax[1].imshow(Ir)
ax[1].set_title('Reconstructed with %d Colors' % COLORS)


#Get and display an error image. We'll use scipy.cluster.vq
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.vq.vq.html
color_codes, dist = vq.vq(Xf, centersUint)

#color_codes should be equal to labels.
pic = ax[2].imshow(np.reshape(dist, I.shape[:2]))
f.colorbar(pic, ax=ax[2])
ax[2].set_title('Reconstruction Error')




#And just to prove it, look at unique.
#with numpy 1.13, you can send an axis to unique.
#https://stackoverflow.com/questions/16970982/find-unique-rows-in-numpy-array
#But I'll write it more generally.
origvals = I[...,0].ravel() + 256*I[...,1].ravel() + 256**2*I[...,2].ravel()
newvals = Ir[...,0].ravel() + 256*Ir[...,1].ravel() + 256**2*Ir[...,2].ravel()

print('Original image has %d unique colors, versus %d in the cluster colored image.' %
      (len(np.unique(origvals)), len(np.unique(newvals))))







