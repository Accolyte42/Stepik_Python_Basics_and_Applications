

from itertools import takewhile
import itertools


def primes():
    a = 1
    while True:
        a += 1
        # print(a, end=' ')
        # if fac(a-1)+1 % a == 0:
        # for i in
        yield a


# print(list(itertools.takewhile(lambda x: x <= 31, [1,2,3,4,10])))

print(list(itertools.takewhile(lambda x: x <= 10, primes())))











