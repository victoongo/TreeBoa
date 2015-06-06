# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 14:27:13 2015

Special Pythagorean triplet
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

@author: victor
"""

def is_pythagorean_triplet(a, b, c):
    return a ** 2 + b ** 2 == c ** 2
print is_pythagorean_triplet(3, 4, 5)
print is_pythagorean_triplet(3, 4, 6)

def find_pythagorean_triplet(number):
    a = 1
    b = a + 1
    c = number - a - b
    found = 0
    while found == 0:
        while b < c:
            print a, b, c
            if a ** 2 + b ** 2 == c ** 2:
                found = 1            
                break
            else:
                b += 1
                c = number - a- b
                
        if found == 0:
            a += 1
            b = a + 1
            c = number - a - b
    return a, b, c
print find_pythagorean_triplet(12)
print find_pythagorean_triplet(1000)

print is_pythagorean_triplet(200, 375, 425)
print 200 * 375 * 425