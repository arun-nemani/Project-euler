# A palindromic number reads the same both ways. The largest palindrome
# made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.
# Author: Arun Nemani
import time


def palindrome(digs=2):
    out = max(i * j
              for i in range(10**(digs - 1), 10**digs)
              for j in range(10**(digs - 1), 10**digs)
              if str(i * j) == str(i * j)[:: -1])

    return out

if __name__ == "__main__":
    start = time.time()
    print("--------")
    print(palindrome(3))
    print("--------")
    print("Comp time: {:.5f} seconds".format(time.time() - start))
