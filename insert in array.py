'''
 Write a Python program to insert a new item before the second element in an existing array.
'''
from array import *
c=array('i',[1,2,3,4,5])
c.insert(1,100)
for i in c:
    print(i)