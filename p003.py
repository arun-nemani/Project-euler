# Prompt
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Author: Arun Nemani
import time


def primefactors(n):
    # return all prime factors of n
    f = 2
    while f * f <= n:
        while not n % f:
            yield f
            n //= f
        f += 1
    if n > 1:
        yield n


if __name__ == "__main__":
    start = time.time()
    print("--------")
    print(max(primefactors(600851475143)))
    print("--------")
    print("Comp time: {:.5f} seconds".format(time.time() - start))
