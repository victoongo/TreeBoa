# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 13:00:28 2015

Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

@author: victor
"""

def next_prime(p_list):
    new_p = p_list[-1]
    prime = 0
    while prime == 0:
        new_p += 2
        prime = 1
        for p in p_list:
            #print p, new_p
            if new_p % p == 0:
                prime = 0
                break
    p_list.append(new_p)
    return p_list
print next_prime([2, 3])

# test next_prime function
p_list = [2, 3]
while p_list[-1] < 100:
    p_list = next_prime(p_list)
#print p_list

def largest_prime_factor(num):
    p_list = [2, 3]
    while num != p_list[-1]:
        #print num, p_list[-1]
        if num % p_list[-1] == 0:
            num /= p_list[-1]
        else:
            p_list = next_prime(p_list)
    return p_list[-1]
print largest_prime_factor(13195)
print largest_prime_factor(600851475143)