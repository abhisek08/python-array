'''
Write a Python program to get the current memory address and
the length in elements of the buffer used to hold an array?s
contents and also find the size of the memory buffer in bytes.
'''
from array import *
c=array('i',[1,2,3,4,5])
print(c.buffer_info())
print(c.buffer_info()[1]*len(c))
