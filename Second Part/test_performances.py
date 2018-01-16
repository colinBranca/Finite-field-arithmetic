import sys
import time
import matplotlib.pyplot as plt
from  rings.polynomials.naive import Polynomials
from fields.finite.naive import FiniteField
from support.primes import *
from random import randrange

#List of primes (51 to 100 th)
primes = [3, 7, 13, 31, 61, 127, 251, 509, 1021, 2039,
        4093, 8191, 16381, 32749, 65521, 131071, 262139, 524287, 999983]

x1 = []
first_times = []
GF  = FiniteField( 449 )
GFx = Polynomials( GF )
for deg in range(5, 201, 5):
    print(deg)
    sum_times = 0
    for _ in range(5):
        f = GFx.random_monic_poly_degree(deg)
        start = time.clock()
        factors = f.factor()
        stop = time.clock()
        sum_times = sum_times + stop - start
    x1.append(deg)
    first_times.append(sum_times/5)


plt.figure(1)
plt.plot(x1, first_times)
plt.xlabel('degree of polynomial')
plt.ylabel('factorization time (in seconds)')
plt.savefig("graph1.png")

print("part 1 done ")

x2 = []
second_times = []
i = 1
for p in primes:
    print(p)
    sum_times = 0
    i = i + 1
    for _ in range(5):
        GF  = FiniteField( p )
        GFx = Polynomials( GF )
        f = GFx.random_monic_poly_degree(50)
        start = time.clock()
        factors = f.factor()
        stop = time.clock()
        sum_times = sum_times + stop - start
    x2.append(i)
    second_times.append(sum_times/5)


plt.figure(2)
plt.plot(x2, second_times)
plt.xlabel('Prime length (in bits)')
plt.ylabel('factorization time (in seconds)')
plt.savefig("graph2.png")
