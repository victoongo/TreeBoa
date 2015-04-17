# 10001st prime
# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?


# primes are odds numbers
# if a num can't be evenly divided by n, 
# it can't be evenly divided by a number larger than num / n. 
# only prime numbers smaller than num need to be tested
# grow the prime list by combine the existing prime may work
# if a odd number between 3*3 and 5*5 not divisible by 3, 
# it's not divisible by any larger prime
import math
def nth_prime(n):
    #prime = 11
    #count = 5
    primes = [2, 3, 5, 7, 11]
    if n < 5:
        return primes[n-1]
    else:
        test_prime = primes[-1] + 2
        while len(primes) < n: 
            #test_prime = prime
            not_prime = 0
            sr = math.sqrt(test_prime)
            #count = 1
            #for p in range(3, test_prime // 3):
            for p in primes:
                if p > sr:
                    exit
                elif test_prime % p == 0:
                    not_prime = 1
                    #count += 1
                    
            if not_prime == 0:
                primes.append(test_prime)
                
            test_prime += 2
        return primes[-1]             
    
for i in range(1, 117):
    print nth_prime(i)
    
# the baseline is working
