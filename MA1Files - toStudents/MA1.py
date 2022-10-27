"""
Solutions to module 1
Student: David Hovstadius  
Mail: david@hovstadius.com
Reviewed by: Nandini
Reviewed date: 2/9-2022
"""

import random
import time
import math
import functools
from time import perf_counter as pc
from matplotlib import pyplot as plt



def power(x, n):         # Optional
    if n == 0:
        return 1
    else:
        return x*power(x,n-1)


def multiply(m, n):      # Compulsory
    if n == 0:
        return 0
    else:
        return m+multiply(m,n-1)


def divide(t, n):        # Optional
    if t < n:
        return 0
    else:
        return 1+divide(t-n,n)


def harmonic(n):         # Compulsory
    if n == 1:
        return 1
    else:
        return 1/n + harmonic(n-1)


def digit_sum(x):        # Optional
    pass


def get_binary(x):       # Optional
    pass


def reverse(s):          # Optional
    pass


def largest(a):          # Compulsory
    if len(a) == 1:
        return a[0]
    else:
        b = largest(a[1:])
        if b > a[0]:
            return b 
        else:
            return a[0]


def count(x, s):         # Compulsory
    if len(s) == 0:
        return 0
    else: 
        if s[0] == x:
            return 1 + count(x,s[1:])
        elif type(s[0]) == list:
            return count(x,s[0]) + count(x,s[1:])
        else:
            return 0 + count(x,s[1:])
        
    

def zippa(l1, l2):       # Compulsory
    if len(l1) == 0:
        return l2
    elif len(l2) == 0:
        return l1
    else:
        return [l1[0]] + [l2[0]] + zippa(l1[1:],l2[1:])



def bricklek(f, t, h, n): # Compulsory
    if n == 1:
        return [f+'->'+t]
    else:
        return bricklek(f,h,t,n-1) + [f+'->'+t] + bricklek(h,t,f,n-1)


def fac(n):
        if n == 0:
            return 1
        else: 
            return n*fac(n-1)

@functools.lru_cache(maxsize=None)
def fib_fast(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_fast(n-1) + fib_fast(n-2)

def fib_slow(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_slow(n-1) + fib_slow(n-2)

def compare_fib(n):
    start = pc()
    fib_slow(n)
    end = pc()
    slow = end-start
    start = pc()
    fib_fast(n)
    end = pc()
    fast = end-start
    return [fast,slow]



def main():
    """ Demonstates my implementations """
    # Write your demonstration code here

    # animated plot the time it takes to compute fib_fast and fib_slow from 0 to 30
    x = [n for n in range(0,31)]
    y = [compare_fib(n)[0] for n in x]
    z = [compare_fib(n)[1] for n in x]
    plt.plot(x,y,'r.-',label='fast')
    plt.plot(x,z,'b.-',label='slow')
    plt.xlabel('n')
    plt.ylabel('time')
    plt.legend()
    plt.show()
    


# function that compares the speed of fib_slow and fib_fast


if __name__ == "__main__":
    main()

    
####################################################    
    
"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 16: Time for bricklek with 50 bricks:
  
  
    secounds = 2^n - 1


    n = 50:  1125899906842623 secounds
  
  
  Exercise 17: Time for Fibonacci:
  
  a) 
   c*O(1.618^n)
   solve for c

    fib(20) = 0.00697 secounds
    c = 4.6 * 10**-7

    then fib(30) should be approx 0.85 secounds 
    I got 0.712, so it is verified!

  b)
  For fib(50) I just ran the code for this long
  fib(50) = 9703.1295983 secounds = 2.69 hours
  
  This one i needed to calculate.
  I calculated this one by using the already calculated constant c and applying it to n=100
  fib(100) = 8650182 years
  

  Exercise 20: Comparison sorting methods:
  
  For this metod O(n^2)
  I solve for c by knowing n(1000) is 1 secound.
  c = 10**-6

  I get these values by using c and its n respectively
  Insert(10^6) = 10**6 secounds = 11.57 days
  Insert(10^9) = 31709 years
  
    Here I get a c of 1/3000
    By calculating with this c with both n respectively i get these answers
  Merge(10^6) = 2000s
  Merge(10^9) = 34.73 days
  

  Exercise 21: Comparison Theta(n) and Theta(n log n)
  
  First  I calculate the c for each
  A: c = 1
  B: c = 1/(10*log(10)) = 0.1

  I put these two sorting algoritms equals to eachother

  n = 0.1 * n * log(n)
  10 = log(n)
  n = power(10,10)
  
  
  
  
  





"""