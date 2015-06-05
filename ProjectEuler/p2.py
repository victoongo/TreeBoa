# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 16:42:27 2015

@author: victor
"""

l = [1, 2, 3]
print l[:-1]

def even_fibonacci_numbers(ceiling):
    fibonacci = [1, 2]
    while fibonacci[-1] <= ceiling:
        fibonacci.append(sum(fibonacci[-2:]))
    #fibonacci.pop()
    even_fibonacci = []
    for num in fibonacci[:-1]:
        if num % 2 == 0:
            even_fibonacci.append(num)
    return even_fibonacci
    
print even_fibonacci_numbers(100)
print sum(even_fibonacci_numbers(4000000))
