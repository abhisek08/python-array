'''
Write a Python program to append items from a specified list
'''
from array import *
c=array('i',[1,2,3,4,5])
l=[6,7,8,9]
for j in l:
    c.append(j)
for i in c:
    print(i,end=' ')