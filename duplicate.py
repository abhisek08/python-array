'''
Write a Python program to find whether a given array of integers contains any duplicate element.
Return true if any value appears at least twice in the said array and return false if every element is distinct.
'''
from array import *
c=array('i',[1,1,2,3,4])
d=set(c)
if len(c)!=len(d):
    print(True)
