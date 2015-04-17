# 10001st prime
# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

# primes are odds numbers
# if a num can't be evenly divided by n, 
# it can't be evenly divided by a number larger than num / n. 
# only prime numbers smaller than num need to be tested
# grow the prime list by combine the existing prime may work
def nth_prime(n):
    prime = 11
    count = 5
    if n == 1:
        return 2
    elif n == 2:
        return 3
    elif n == 3:
        return 5
    elif n == 4:
        return 7
    elif n == 5:
        return 11
    else:
        test_prime = prime + 2
        while count < n: 
            #test_prime = prime
            not_prime = 0
            for p in range(3, test_prime // 3):
                if test_prime % p == 0:
                    not_prime = 1
            if not_prime == 0:
                prime = test_prime
                count += 1
            test_prime += 2
        return prime             
    
for i in range(1, 117):
    print nth_prime(i)
