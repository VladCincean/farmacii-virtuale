'''
Created on 6 ian. 2016

@author: Vlad
'''
from utils.lab10 import *
from random import shuffle
from datetime import datetime, timedelta

def testSorts():
    L = list(range(100, 0, -1))
    cocktailSort(L)
    assert  L == list(range(1, 101))
    
    L.reverse()
    combSort(L)
    assert L == list(range(1, 101))
    
    L.reverse()
    mySort(L)
    assert L == list(range(1, 101))
#run test
testSorts()

print("Sort tests passed!\n")

