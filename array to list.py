'''
Write a Python program to convert an array to an ordinary list with the same items.
'''
from array import *
l=[]
c=array('i',[1,2,3,4,5])
for i in c:
    l.append(i)
print(l)