

from itertools import takewhile
from math import factorial
import itertools


def primes():
    a = 1
    while True:
        a += 1
        # print(a, end=' ')
        test_fac = factorial(a-1)
        test_123 = test_fac+1
        test = (test_123 % a == 0)
        if test:
            yield a

# print(list(itertools.takewhile(lambda x: x <= 31, [1,2,3,4,10])))

print(list(itertools.takewhile(lambda x: x <= 41, primes())))











