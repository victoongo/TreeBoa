# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 16:25:30 2015

Multiples of 3 and 5
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

@author: victor
"""

def m35(ceiling):
    list_m35 = []
    for num in range(ceiling):
        if num % 3 == 0 or num % 5 == 0:
            #print num
            list_m35.append(num)
    return sum(list_m35)
    
print m35(10)
print m35(1000)

def m35a(ceiling):
    m3 = (ceiling - 1) // 3
    m5 = (ceiling - 1) // 5
    #print m3, m5
    list_m35 = []
    for num3 in range(m3 + 1):
        list_m35.append(num3 * 3)
    for num5 in range(m5 + 1):
        list_m35.append(num5 * 5)
    #print list_m35
    list_m35 = set(list_m35)
    return sum(list_m35)
    
print m35a(10)
print m35a(1000)

