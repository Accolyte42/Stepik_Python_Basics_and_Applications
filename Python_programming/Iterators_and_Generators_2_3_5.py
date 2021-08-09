

from itertools import takewhile
from math import factorial
import itertools


def primes():
    a = 1
    while True:
        a += 1
        if (factorial(a-1)+1) % a == 0:
            yield a

# print(list(itertools.takewhile(lambda x: x <= 31, [1,2,3,4,10])))

print(list(itertools.takewhile(lambda x: x <= 41, primes())))











