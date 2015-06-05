# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 22:30:42 2015

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
