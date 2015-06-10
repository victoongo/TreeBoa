# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 14:01:12 2015

Power digit sum
Problem 16
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2 ** 1000?

@author: victor
"""

def sum_of_digits(power, base = 2):
    num = base ** power
    num_str = str(num)
    sum_score = 0
    for i in range(len(num_str)):
        sum_score += int(num_str[i])
    return sum_score
print sum_of_digits(15)
print sum_of_digits(1000)


def sum_of_digits2(power, base = 2):
    num = base ** power
    num_str = str(num)
    #num_list = [int(i) for i in list(num_str)]
    num_list = map(int, num_str)
    sum_score = sum(num_list)
    return sum_score
print sum_of_digits2(15)
print sum_of_digits2(1000)