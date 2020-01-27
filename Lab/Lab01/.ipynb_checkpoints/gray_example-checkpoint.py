"""
Joshua Stough
DIP

Converting from rgb to grayscale:
"""

#Convert color to gray in a perceptually accurate way.
def rgb2gray(rgb):
    #r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * rgb[:,:,0] + 0.5870 * rgb[:,:,1] + 0.1140 * rgb[:,:,2]
    return gray


I = plt.imread('sf.jpg')

G = rgb2gray(I.astype('float')) #The grayscale version of the image.

