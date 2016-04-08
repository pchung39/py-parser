import os
import sys

lister = [1,2,3,4,5,6,7,8,9,10]
target = 2

def max_min(list, num):
    min = 0
    max = len(lister)
    binary_search(lister, min, max, target)


def binary_search(list, small, big, num):
    min = small # 0
    max = big # 10
    middle = (max + min/2) - 1 # 5 
    
 
    if list[middle] == num:
        print "You found it! %r " % target
    elif list[middle] != target:        
        if num > list[middle]:
            print "Target is bigger"
            min = middle
            binary_search(lister, min, max, target)
        else:
            print "Target is smaller"
            max = middle
            binary_search(lister, min, max, target)

max_min(lister, target)
