'''
Write a Python program to remove a specified item using the index from an array.
'''
from array import *
c=array('i',[1,2,3,4,5])
c.remove(c[1])
print(c)