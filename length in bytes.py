'''
 Write a Python program to get the length in bytes of one array item in the internal representation
'''
from array import *
c=array('i',[1,2,3,4,5])
print(c.itemsize)