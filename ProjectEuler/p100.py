# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 10:20:42 2015

Arranged probability
Problem 100
If a box contains twenty-one coloured discs, composed of fifteen blue discs and
six red discs, and two discs were taken at random, it can be seen that the
probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two
blue discs at random, is a box containing eighty-five blue discs and
thirty-five red discs.

By finding the first arrangement to contain over 10 ** 12 = 1,000,000,000,000
discs in total, determine the number of blue discs that the box would contain.

@author: victor
"""

import math

def sqrt2():
    """
    get a more precise sqrt of 0.5 than the one from math.sqrt()
    """
    pass

def arranged_probability(total):
    """
    blue / total should decrease to sqrt(0.5) as total increase.
    """
    start = math.sqrt(0.5)
    found = False
    while found == False:
        blue = int(total * start) - 25
        e = 0
        while e < 51 and found == False:
            print total, blue, float(blue * (blue - 1)) / (total * (total - 1)) == 0.5
            if float(blue * (blue - 1)) / (total * (total - 1)) == 0.5:
                found = True
            else:
                blue += 1
                e += 1
        total += 1
    total -= 1
    return total, blue, total - blue


def arranged_probability2(total):
    """
    blue / total should decrease to sqrt(0.5) as total increase.
    """
    start = math.sqrt(0.5)
    found = False
    while found == False:
        blue = int(math.ceil(total * start) )
        if float(blue * (blue - 1)) / (total * (total - 1)) == 0.5:
            found = True
        else:
            total += 1
    return total, blue, total - blue


#print arranged_probability(21)
#print arranged_probability(22)
print arranged_probability(120)
print arranged_probability2(121)
print arranged_probability2(10 ** 12)
