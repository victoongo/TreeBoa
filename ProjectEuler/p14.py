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
        else:
            num = 3 * num + 1
        terms += 1
    return terms
print terms_collatz(13)


def collatz(num):
    """
    recursive function to impliment collatz
    """
    if num != 1:
        if num % 2 == 0:
            #print num
            return collatz(num / 2)
        else:
            return collatz(3 * num + 1)
    else:
        return 1
print collatz(1300)


def longest_collatz(ceiling):
    num = 1
    max_num = 1
    max_terms = 0
    while num < ceiling:
        terms = terms_collatz(num)
        #print num, terms
        if terms > max_terms:
            max_num = num
            max_terms = terms
        num += 1
    return max_num
print longest_collatz(1000000)

# use dictionary to speed it up
# look up number in the dictionary in each step
def memoized_terms_collatz(num, memo_dict):
    """
    recursive function to impliment collatz
    """
    terms = 1
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = 3 * num + 1
        terms += 1
    return terms

    #global memo_dict
    terms = 1
    while num != 1:
        if num in memo_dict:
            return memo_dict[num]
        else:
            if num % 2 == 0:
                #print num
                memo_dict[num] = num / 2
                return collatz(num / 2)
            else:
                memo_dict[num] = 3 * num + 1
                return collatz(3 * num + 1)
print memoized_terms_collatz(1300, {1:1, 2:2, 4:3})


def longest_collatz(ceiling):
    memo_dict = {1:1, 2:2, 4:3}
    num = 1
    max_num = 1
    max_terms = 0
    while num < ceiling:
        terms = memoized_terms_collatz(num)
        #print num, terms
        if terms > max_terms:
            max_num = num
            max_terms = terms
        num += 1
    return max_num
print longest_collatz(1000000)