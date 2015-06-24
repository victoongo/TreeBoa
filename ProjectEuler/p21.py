# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 21:33:36 2015

Amicable numbers
Problem 21
Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

@author: victor
"""

import math

def sum_divisors(num):
    divisors = []
    n = 1
    sqrt = math.sqrt(num)
    while n < sqrt:
        if num % n == 0:
            if n == 1:
                divisors.append(1)
            else:
                divisors.extend([n, num / n])
        n += 1
    # eturn num, sum(divisors), divisors
    return sum(divisors)

#print sum_divisors(220)[1]
print sum_divisors(284)
print sum_divisors(1)

def amicable(ceiling):
    amicables = []
    n = 2
    while n < ceiling:
        sum_of_divisors = sum_divisors(n)
        if sum_of_divisors != n:
            reverse_sum = sum_divisors(sum_of_divisors)
            if sum_of_divisors < ceiling and reverse_sum == n:
                amicables.extend([n, sum_of_divisors])
        n += 1
    print amicables
    amicables = set(amicables)
    return sum(amicables), amicables

print amicable(10000)#[0]

