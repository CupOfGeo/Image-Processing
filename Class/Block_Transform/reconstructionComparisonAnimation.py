"""
Joshua Stough
DIP

Demo showing reconstruction with standard vs dct basis over the whole image.
Just like old happyFace demo in matlab that showed the basis vectors and the
reconstruction so far.
"""

import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation

from waveletUtil import *

# parameters for the script
IMAGEFILE = 'happy128.png'
SNAME = 'Standard'



I = plt.imread(IMAGEFILE)


ishape = I.shape

if len(ishape) < 3:
    raise ValueError('reconstructionCompressionAnimation: expecting color image')

if ishape[0] != ishape[1]:
    print('reconstructionCompressionAnimation: squaring the image')
    minn = min(ishape[:2])
    I = I[:minn, :minn, :]
    ishape = I.shape

# Make sure the data is in 0-1, so the floating point imshow is okay
I = I/I.max()

# Now the idea is to reconstruct an image one coefficient at a time
# in different transform spaces, S and H
if SNAME == 'Haar':
    S = makeHaarMatrix(ishape[0])
else:
    S = makeStandardMatrix(ishape[0])

# H = makeHaarMatrix(ishape[0])
H = makeDCTMatrix(ishape[0])

# The transform images in S and H
TI_S = np.zeros(ishape)
TI_H = np.zeros(ishape)

for chan in range(3):
    TI_S[..., chan] = np.matmul(S, np.matmul(I[..., chan], S.transpose()))
    TI_H[..., chan] = np.matmul(H, np.matmul(I[..., chan], H.transpose()))


# The reconstruction will go in different orders for the two basis sets,
# one by english-reading, the other by magnitude of the coefficient.
xs = np.meshgrid(np.arange(ishape[0]), np.arange(ishape[0]), indexing='ij')
coords = np.concatenate([np.expand_dims(c, axis=1) for c in
                         [x.ravel() for x in xs]], axis=1)
# dists = np.sum(coords*coords, axis=1) # to use distance from top-left
# dargS = np.argsort(dists) # sorts in increasing order
dargS = list(range(len(coords)))

# If you're not using the standard basis and you want to order
# the reconstruction by coefficient magnitude, do this:
if SNAME == 'Haar':
    mags = TI_S[...,0].ravel(order='F')
    dargS = np.argsort(np.abs(mags))
    dargS = list(reversed(dargS))


# just pic one of the color channels to use.
mags = TI_H[...,0].ravel(order='F')
dargH = np.argsort(np.abs(mags))
dargH = list(reversed(dargH))

# frame number
fn = 0



# The four images we're going to update are the basis images Sij and Hij,
# and the reconstructions so far SRI and HRI. This is just the initialization.
# aSij, etc. are the artists for the animation.

Sij = np.zeros((ishape[0], ishape[0]))
Hij = np.zeros((ishape[0], ishape[0]))
SRI = np.zeros(ishape)
HRI = np.zeros(ishape)


f, ax = plt.subplots(2, 2, figsize=(8,8), sharex=True, sharey=True)
f.canvas.set_window_title('Image Reconstruction with Cosine Patterns')
plt.tight_layout()

aSij = ax[0][0].imshow(Sij, cmap='gray', animated=True)
ax[0][0].set_title('%s Pattern' % SNAME)

aHij = ax[0][1].imshow(Hij, cmap='gray', animated=True)
ax[0][1].set_title('Cosine Pattern')

aSRI = ax[1][0].imshow(SRI, animated=True)
ax[1][0].set_title('%s Reconstruction' % SNAME)

aHRI = ax[1][1].imshow(HRI, animated=True)
ax[1][1].set_title('Cosine Reconstruction')

# Let's add an animated text field for the frame number.
aFNText = ax[0][0].text(np.round(.7*ishape[0]), np.round(.9*ishape[0]), 'frame %04d' % fn,
                        color='cyan', animated=True, bbox=dict(facecolor='red', alpha=0.5))


# And needed to avoid extra whitespace
# See: https://stackoverflow.com/questions/15077364/matplotlib-pyplot-imshow-removing-white-space-within-plots-when-using-attribute/
# and: https://github.com/matplotlib/matplotlib/pull/10033
for i in range(4):
    ax[i//2][i%2].set_adjustable('box')



#Now time for the animation function

# Needs to update the array data and the texts, then
# return the artists. see:
# https://matplotlib.org/api/_as_gen/matplotlib.animation.FuncAnimation.html
#
def updateFig(*args):
    global Sij, Hij, SRI, HRI, dargS, dargH, fn, TI_S, TI_H

    # update the Sij basis and add into the SRI reconstruction

    # Need j, i for coefficient mag.
    # j, i = coords[dargS[fn]]  # Get the i, j for the frame number.
    i, j = coords[dargS[fn]]
    Sij = np.outer(S[i, :], S[j, :])

    for chan in range(3):
        SRI[..., chan] += TI_S[i, j, chan] * Sij

    # Just to prove the coefficients are sorted in decreasing magnitude.
    # print('%6.3f' % TI_S[i, j, 0])

    # similarly update HRI
    j, i = coords[dargH[fn]]
    Hij = np.outer(H[i, :], H[j, :])

    for chan in range(3):
        HRI[..., chan] += TI_H[i, j, chan] * Hij

    # Just to prove the coefficients are sorted in decreasing magnitude.
    # print('%6.3f' % TI_H[i, j, 0])


    # Update the frame number fn for next time.
    fn += 1
    if (fn >= Sij.size): # just ishape[0]*ishape[0], but why keep typing that...
        fn = 0
        SRI.fill(0)
        HRI.fill(0)

    # Now with all the images updated, update the artists and return them.

    # Not sure why the single-channel basis images don't show without the
    # the clim stuff.
    aSij.set_array(Sij)
    aSij.set_clim(Sij.min(), Sij.max())
    # aSij.set_clip_on(True)

    aHij.set_array(Hij)
    aHij.set_clim(Hij.min(), Hij.max())
    # aHij.set_clip_on(True)

    aSRI.set_array(SRI.clip(0,1))
    aHRI.set_array(HRI.clip(0,1))

    aFNText.set_text('frame %04d' % (fn-1))

    return aSij, aHij, aSRI, aHRI, aFNText,


ani = animation.FuncAnimation(f, updateFig, interval=200, blit=True, repeat=True)


