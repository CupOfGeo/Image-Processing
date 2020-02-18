"""
Joshua Stough
DIP

LZW compression.

https://www2.cs.duke.edu/csed/curious/compression/lzw.html
http://rosettacode.org/wiki/LZW_compression#Python

"""

import matplotlib.pyplot as plt
import numpy as np
from huffTreeUtilities import *


"""
LZWCompress: given a stream of uint8, outputs a 
generator outstream. parameter bits defines how 
many bits to encode each pattern with, or how 
big the dictionary gets.
"""
class LZWCompress(object):
    def __init__(self, instream, bits = 12):
        self.instream = instream
        self.bits = bits
        self.table = {}

    def __iter__(self):
        #myhash = lambda window: ' '.join(str(x) for x in window)
        myhash = lambda window: ''.join(chr(x) for x in window)

        self.table = dict(zip([myhash([x]) for x in range(256)], range(256)))

        #siter = iter(self.instream)
        curwindow = [] #s = empty

        for x in self.instream: #x is ch
            curwindow.append(x) #s + ch
            if myhash(curwindow) not in self.table: #if s+ch not in table
                yield self.table[myhash(curwindow[:-1])] #yield s

                if len(self.table) < 2**self.bits: #if enough space in dict
                    self.table[myhash(curwindow)] = len(self.table) #add s+ch

                curwindow = [x]  # set s = ch

        yield self.table[myhash(curwindow)]

class LZWDecompress(object):
    def __init__(self, compressedStream, bits = 12):
        self.compressedStream = compressedStream
        self.bits = bits
        self.table = {}

    def __iter__(self):
        #table is the other way around now.
        self.table = dict(zip(range(256), [[x] for x in range(256)]))

        itere = iter(self.compressedStream)
        w = [next(itere)]
        yield w[0]

        for x in itere:
            if x in self.table: #if it's already an entry
                entry = self.table[x]
            elif x == len(self.table): #x isn't yet in the table.
                entry = w + [w[0]]
            else:
                raise ValueError('saw compressed index %d, unknown' % x)

            for i in entry:
                yield i

            if len(self.table) < 2 ** self.bits:
                self.table[len(self.table)] = w + [entry[0]]

            w = entry



def loadHuffableImage(I):
    if type(I) == str:
        I = plt.imread(I)

    if (len(I.shape) > 2):
        print("loadHuffableImage: input is multi-channel, using grayscale.")
        Ig = 0.2989 * I[..., 0] + 0.5870 * I[..., 1] + 0.1140 * I[..., 2]
        I = Ig

    if I.ravel().max() <= 1:
        print('loadHuffableImage: Setting range to [0, 255]')
        I = np.round(256*I)

    I[I > 255] = 255
    I = I.copy().astype('uint8')

    return I

