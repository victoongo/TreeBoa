# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 22:30:42 2015

Sum square difference
Problem 6
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

@author: victor
"""

def sum_square_difference(ceiling):
    nn_list = list(range(ceiling + 1))
    #nns_list = []
    nns = 0
    for num in nn_list:    
        #nns_list.append(num ** 2)
        nns += num ** 2
    #print sum(nns_list)
    return sum(nn_list) ** 2 - nns
    
print sum_square_difference(10) # = 2640
print sum_square_difference(100)
