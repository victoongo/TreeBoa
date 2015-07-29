# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 16:42:27 2015

Even Fibonacci numbers
Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous
two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.

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
print sum(even_fibonacci_numbers(100))
print sum(even_fibonacci_numbers(4000000))


def even_fibonacci_numbers2(ceiling):
    a = 1
    b = 2
    sum = 0
    while b < ceiling:
        if b % 2 == 0:
            sum += b
        h = a + b
        a = b
        b = h
    return sum
print even_fibonacci_numbers2(100)
print even_fibonacci_numbers2(4000000)


def even_fibonacci_numbers3(ceiling):
    a = 1
    b = 1
    c = a + b
    sum = 0
    while c < ceiling:
        sum += c
        a = b + c
        b = a + c
        c = a + b
    return sum
print even_fibonacci_numbers3(100)
print even_fibonacci_numbers3(4000000)


def fib(num):
    """
    recursive fibonacci
    """
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)
for i in range(15):
    print fib(i)