# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 22:33:06 2015

@author: victor
"""

def prime_list(ceiling):
    p_list = [2, 3]
    for num in range(4, ceiling + 1):
        prime = 1
        for p in p_list:
            if num % p == 0:
                prime = 0
                break
        if prime == 1:
            p_list.append(num)
    return p_list
#print prime_list(10)

def prime_list_higher_order(ceiling):
    p_list = prime_list(ceiling)
    p_list_multiple = p_list
    power = 2
    end_power = 0
    while end_power == 0:
        for p in p_list:
            p_power = p ** power
            if p_power <= ceiling:
                p_list.append(p)
            elif p == 2:
                end_power = 1
                break
            else:
                power += 1
                break
    return p_list_multiple
#print prime_list_higher_order(10)

def smallest_multiple(ceiling):
    #p_list = prime_list(ceiling)
    #print p_list
    p_list_multiple = prime_list_higher_order(ceiling)
    #nn_list_r = list(range(ceiling, 3, -1))
    #print nn_list_r
    #multiple = 1
    p_multiple = 1
    for p in p_list_multiple:
        p_multiple *= p
    #for p in p_list:
    #    multiple *= p
    #for p in p_list:
    #    multiple *= p
    #    print p, multiple
    #    divisible = 1
    #    for num in nn_list_r:
    #        print num
    #        if multiple % num != 0:
    #            #for p in p_list:
    #            divisible = 0                
    #            break
    #    if divisible == 1:
    #        break
    return p_multiple
print smallest_multiple(10) # = 2520
print smallest_multiple(20)