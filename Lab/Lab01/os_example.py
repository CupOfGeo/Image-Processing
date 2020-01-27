"""
Joshua Stough
DIP

Simple usage example of os module. Read more at:
https://www.tutorialspoint.com/python/os_file_methods.htm
"""

"""
The os module provides a vast range of capabilities for manipulating file systems.
I mostly find os useful to navigate within the python console.
"""

import os

print(os.path.abspath('.')) #print the current path.

print('changing dir to ..')
os.chdir('..') #change directory
print(os.path.abspath('.'))

os.listdir('.') #list directory contents
