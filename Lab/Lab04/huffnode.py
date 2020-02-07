"""
Joshua Stough
DIP

Simple binary tree class for huffman coding demo.
"""

class huffnode(object):
    def __init__(self):
        self.l = self.r = None
        self.f = -1 #frequency
        self.s = 'a' #symbol, or intensity

    def __init__(self, freq, symbol ='a', left = None, right = None):
        self.f = freq
        self.s = symbol
        self.l = left
        self.r = right

    def getFreq(self):
        return self.f

    def getSymb(self):
        return self.s

    def getLeft(self):
        return self.l

    def getRight(self):
        return self.r

    def isLeaf(self):
        return (self.l is None) and (self.r is None)

    def __str__(self):
        return '[node: freq %d: %s]' % \
                (self.f, ['', str(self.s)][self.isLeaf()])

    def __cmp__(self, other):
        return self.f - other.f

    def __eq__(self, other):
        return self.f == other.f

    def __ne__(self, other):
        return self.f != other.f

    def __lt__(self, other):
        return self.f < other.f

    def printTree(self, level = 0):
        thisnodestr = '  ' * level + '--'+ str(self)
        if self.isLeaf():
            print(thisnodestr)
        else:
            #backwards in-order traversal
            #so left and right is still
            #left and right when you twist your head.
            if self.r is not None:
                self.r.printTree(level + 1)
            print(thisnodestr)
            if self.l is not None:
                self.l.printTree(level + 1)
                
                
    def treeFreqs(self, level = 0):
        thisnodestr = '  ' * level + '--'+ str(self)
        if self.isLeaf():
            print(self.getFreq())
        else:
            #backwards in-order traversal
            #so left and right is still
            #left and right when you twist your head.
            if self.r is not None:
                self.r.printTree(level + 1)
            print(thisnodestr)
            if self.l is not None:
                self.l.printTree(level + 1)
        
