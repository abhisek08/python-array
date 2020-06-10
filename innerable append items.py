'''
Write a Python program to append items from inerrable to the end of the array.
'''
from array import *
c=array('i',[1,2,3,4,5])
c.extend(c)
for i in c:
    print(i,end=',')