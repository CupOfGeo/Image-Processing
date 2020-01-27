"""
Joshua Stough
DIP

Some initial usage of matplotlib, for visualizing images. Read more at:
https://matplotlib.org/tutorials/introductory/images.html
https://matplotlib.org/examples/pylab_examples/subplots_demo.html
"""

"""
matplotlib provides numerous redundant and/or conflicting ways of 
displaying data. google is your friend.
"""

import matplotlib.pyplot as plt

I = plt.imread('sf.jpg') #read an image into a numpy array

print("\n\nI's shape is " + str(I.shape)) #the 3 in the last component are the R,G,B channels.

print("I's type is " + str(type(I)))

#plt.imshow(I) is too easy...

f, axarr = plt.subplots(1,4, figsize=(16, 4))

axarr[0].imshow(I) #https://matplotlib.org/api/_as_gen/matplotlib.pyplot.imshow.html
axarr[0].set_title('Color')

axarr[1].imshow(I[...,0], cmap = 'gray')
axarr[1].set_title('Red Channel')

axarr[2].imshow(I[...,2], cmap = 'gray')
axarr[2].set_title('Blue Channel')

Ih = I.copy()
Ih[:,:,0] = I[:,:,0] // 2 #half the red channel

axarr[3].imshow(Ih)
axarr[3].set_title('Only Half Red')






