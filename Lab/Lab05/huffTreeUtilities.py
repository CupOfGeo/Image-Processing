"""
Joshua Stough
DIP

Huffman Tree/Coding utility functions for image processing.
"""

import matplotlib.pyplot as plt
import numpy as np
from heapq import *
from huffnode import huffnode
import random

#Build a huffman tree based on some image I, return the tree
#Assuming a uint8 single channel image
def buildHuffTree(I):

    #Now we know I is uint8, single channel
    
    #hist, bins = np.histogram(I.ravel(), np.append(np.unique(I.ravel()),256))
    hist, bins = np.histogram(I.ravel(), np.arange(257))

    lystOfNodes = [huffnode(freq, intensity) for freq,intensity in zip(hist, bins[:-1])]

    #Now use the heapq functions to build a single tree out of these nodes.
    heapify(lystOfNodes)

    while len(lystOfNodes) > 1:
        first = heappop(lystOfNodes)
        second = heappop(lystOfNodes)
        heappush(lystOfNodes, huffnode(first.getFreq() + second.getFreq(),
                            -1, second, first))
        #Notice making the left side the more frequent.

    #When there is only one node in the lyst, then that node is the
    #root of the Huffman tree.
    tree = heappop(lystOfNodes)
    #tree.printTree()
    return tree

#A function that recursively constructs the bit sequence leading to
#each leaf node, building a dictionary that goes from leaf node
#symbol to that sequence.
def buildHuffEncoder(tree, seq = ''):
    retDict = {}
    if tree.isLeaf():
        retDict[tree.getSymb()] = seq
        return retDict

    #Left is 1, right is 0
    if tree.getLeft():
        retDict.update(buildHuffEncoder(tree.getLeft(), seq + '1'))

    if tree.getRight():
        retDict.update(buildHuffEncoder(tree.getRight(), seq + '0'))

    return retDict


def buildHuffPair(I):
    tree = buildHuffTree(I)
    encoder = buildHuffEncoder(tree)
    #the following should work because encoder[key] should also be unique.
    decoder = dict((encoder[key], key) for key in encoder)
    return encoder, decoder

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

def testTreeMaking():
    lyst = [huffnode(random.randint(0,100), chr(ord('A') + x)) for x in range(10)]
    print('Before heapify...')
    print('\n'.join(str(item) for item in lyst))

    heapify(lyst)

    print('\nAfter heapify...')
    print('\n'.join(str(item) for item in lyst))


    #placing the more likely on the left side
    while len(lyst) > 1:
        first = heappop(lyst)
        second = heappop(lyst)
        heappush(lyst, huffnode(first.getFreq() + second.getFreq(),
                            '*', second, first))

    print('Final Huffman tree:\n')
    myHuff = heappop(lyst)
    myHuff.printTree()


#testTreeMaking()
