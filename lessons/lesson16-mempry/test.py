import numpy as np
a = np.zeros(1000000)

import random

def f1():
    for i in range(1000000):
        r = random.randint(0, 1000000 - 1)
        # x = a[i]

def f2():
    for i in range(1000000):
        r = random.randint(1, 1000000 - 1)
        # x = a[r]

import timeit

time1 = timeit.timeit('import __main__; __main__.f1()', number=8)
print(time1)

time2 = timeit.timeit('import __main__; __main__.f2()', number=8)
print(time2)