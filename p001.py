# Prompt: If we list all the natural numbers below 10
# that are multiples of 3 or 5, we get 3, 5, 6P and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


# Author: Arun Nemani
import time


def solution1(n):
    count = 0
    for i in range(0, n):
        if i % 3 == 0 or i % 5 == 0:
            count += i

    return count


def solution2(n):

    return sum(i for i in range(0, n) if (i % 3 == 0 or i % 5 == 0))

if __name__ == "__main__":
    start = time.time()
    print("--------")
    print(solution1(1000))
    print("--------")
    print("Comp time: {:.5f} seconds".format(time.time() - start))
