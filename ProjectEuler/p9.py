# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 14:27:13 2015

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


