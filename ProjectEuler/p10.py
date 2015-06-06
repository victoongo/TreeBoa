# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 16:33:47 2015

Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

@author: victor
"""

import math

def prime_list(ceiling):
    p_list = [2, 3]
    for num in range((p_list[-1] + 2), ceiling, 2):
        #print num
        sr = math.sqrt(num)
        prime = 1
        for p in p_list:
            if p < num and num % p == 0:
                prime = 0
                break
        if prime == 1:
            p_list.append(num)
    return p_list
print prime_list(10)
print prime_list(2000)
print sum(prime_list(2000000))