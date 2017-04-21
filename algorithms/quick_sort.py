# -*- coding: utf-8 -*-
import random
import time
listen = [7,6,5,3,9,1,8,2,4]

random.seed(time.time() * 1000)

def quick_sort(x):
    if len(x) <= 1:
        return x

    pivot = random.choice(x)

    greater_than = []
    less_than = []

    for i in x:
        if i <= pivot:
            less_than.append(i)
        elif i > pivot:
            greater_than.append(i)

    less_than = quick_sort(less_than)
    greater_than = quick_sort(greater_than)
    print less_than
    print greater_than
    return less_than + greater_than

print quick_sort(listen)
