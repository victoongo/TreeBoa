# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 09:44:28 2015

Longest Collatz sequence
Problem 14
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

@author: victor
"""

def terms_collatz(num):
    terms = 1
    while num != 1:
        if num % 2 == 0:
            num /= 2
            terms += 1
        else:
            num = 3 * num + 1
            terms += 1
    return terms
print terms_collatz(13)

def longest_collatz(ceiling):
    start_num = 1
    max_num = 1
    max_terms = 0
    while start_num < ceiling:
        num = start_num
        terms = terms_collatz(num)
        #print num, terms
        if terms > max_terms:
            max_num = num
            max_terms = terms
        start_num += 1
    return max_num
print longest_collatz(1000000)

# use dictionary to speed it up
# look up number in the dictionary in each step