"""
Joshua Stough
DIP

Basic histogram example using matplotlib. Read more on histograms:
https://matplotlib.org/1.2.1/examples/pylab_examples/histogram_demo.html
https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.hist
"""

"""
This example computes histograms using the sf image.
"""

import matplotlib.pyplot as plt
import numpy as np


I = plt.imread('sf.jpg')

#I.flatten() turns an ndarray to a one dimensional ndarray
print("I has the values...")
print(str(np.unique(I.ravel()))) #https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.ravel.html


n, allbins, patches = plt.hist(I.ravel(), bins=np.unique(I.ravel()))
plt.title("Overall Histogram")



#https://stackoverflow.com/questions/6871201/plot-two-histograms-at-the-same-time-with-matplotlib
plt.figure()

plt.hist(I[...,0].ravel(), allbins, alpha = .6, label = 'red', color = 'r')
plt.hist(I[...,1].ravel(), allbins, alpha = .6, label = 'green', color = 'g')
plt.hist(I[...,2].ravel(), allbins, alpha = .6, label = 'blue', color = 'b')




f, axarr = plt.subplots(1,2, figsize=(10, 3))

axarr[0].imshow(I) #https://matplotlib.org/api/_as_gen/matplotlib.pyplot.imshow.html
axarr[0].set_title('Image')

axarr[1].hist(I[...,0].ravel(), allbins, alpha = .6, label = 'red', color = 'r')
axarr[1].hist(I[...,1].ravel(), allbins, alpha = .6, label = 'green', color = 'g')
axarr[1].hist(I[...,2].ravel(), allbins, alpha = .6, label = 'blue', color = 'b')
axarr[1].legend(loc = 'upper right')
plt.show()









