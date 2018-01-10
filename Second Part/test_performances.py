import sys
import timeit
import matplotlib.pyplot as plt
from  rings.polynomials.naive import Polynomials
from fields.finite.naive import FiniteField
from support.primes import *
from random import randrange

#List of 100 first primes
firstPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
                61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131,
                137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197,
                199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271,
                277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353,
                359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433,
                439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509,
                521, 523, 541]

x1 = []
first_times = []
GF  = FiniteField( 59 )
GFx = Polynomials( GF )
for deg in range(50, 200, 10):
    sum_times = 0
    for _ in range(10):
        f = GFx.random_monic_poly_degree(deg)
        start = timeit.timeit()
        factors = f.factor()
        stop = timeit.timeit()
        sum_times = sum_times + stop - start
    x1.append(deg)
    first_times.append(sum_times/10)

print("part 1 done ")

x2 = []
second_times = []
for p in firstPrimes:
    sum_times = 0
    for _ in range(10):
        GF  = FiniteField( p )
        GFx = Polynomials( GF )
        f = GFx.random_monic_poly_degree(50)
        start = timeit.timeit()
        factors = f.factor()
        stop = timeit.timeit()
        sum_times = sum_times + stop - start
    x2.append(p)
    second_times.append(sum_times/10)


plt.figure(1)
plt.plot(x1, first_times)
plt.title('Runtimes for polynomials in F17')
plt.xlabel('degree of polynomial')
plt.ylabel('factorization time')
plt.savefig("graph1.png")

plt.figure(2)
plt.plot(x2, second_times)
plt.title('Runtimes for polynomials of degree 20')
plt.xlabel('Finite Field')
plt.ylabel('factorization time')
plt.savefig("graph2.png")
