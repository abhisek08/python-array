'''
Write a Python program to convert an array to an array of machine values and return the bytes representation.
'''
from array import *
c=array('i',[1,2,3,4,5])
print(c.tobytes())