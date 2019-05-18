# Prompt
# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
#    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

# Author: Arun Nemani
import time


def fibonacci(n):
    # Use iterative approach since Python sucks at handling recursion for high n
    out = 0
    a, b = 0, 1
    while a <= n:
        if a % 2 == 0:
            out += a
        a, b = b, a + b
    return out


if __name__ == "__main__":
    start = time.time()
    print("--------")
    print(fibonacci(4000000))
    print("--------")
    print("Comp time: {:.5f} seconds".format(time.time() - start))
