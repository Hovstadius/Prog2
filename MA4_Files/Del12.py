'''
Student: David Hovstadius
Presented too: Nandini M S
Presentation date: 14/10-2022

'''
import functools
import math
import random
import matplotlib.pyplot as plt
import numpy as np
import functools


vd = lambda d : (math.pi**(d/2))/(math.gamma(d/2+1))
sq = lambda x : x**2

def Dspherevol(n,d):
    Ain = 0
    for i in range(n): 
        cord = [random.uniform(-1,1) for i in range(d)]
        check = sum(map(sq,cord))
        if check <= 1:
            Ain += 1
    return 2**d*(Ain/(n))


'''
Dspherevol(100000,2) = 3.1468
vd(2) = 3.141592653589793

Dspherevol(100000,11) = 1.78176
vd(11) = 1.8841038793898994
'''