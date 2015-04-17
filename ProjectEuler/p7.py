# 10001st prime
# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?


def nth_prime(n):
    prime = 2
    count = 1
    if n == 1:
            return prime
    else:
        test_prime = prime
        while count < n: 
            test_prime = prime
            not_prime = 0
            for p in 2:test_prime:
                if test_prime % p == 0:
                    not_prime = 1
            if not_prime = 0:
                prime = test_prime + 1
                count += 1
            else:
                test_prime += 1 
        return prime             
    
print nth_prime(12)
