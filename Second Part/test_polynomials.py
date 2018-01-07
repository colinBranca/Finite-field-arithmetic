import sys

from  rings.polynomials.naive import Polynomials
from fields.finite.naive import FiniteField
from support.primes import *
from random import randrange

def test(p, n):
    GF7  = FiniteField( p )
    GF7x = Polynomials( GF7 )
    i = 0
    product = 1
    while i < 10 :
        degree = randrange(6)
        times = randrange(5)
        f = GF7x.random_element(n)
        if f.is_irreducible():
            print(f)
            i = i + 1
            product = product * pow(f, times)
    print(i)
    print("-----------")
    factors = product.factor()
    print(len(factors))
    newProduct = 1
    for fac, d in factors:
        print(fac)
        print(fac.is_irreducible())
        for i in range(0, d):
            newProduct = newProduct * fac
    print(product)
    print(newProduct)
    print(newProduct == product)


if __name__ == "__main__":

    p = int(sys.argv[1])
    n = int(sys.argv[2])
    if not isPrime(p):
        sys.exit("p is not prime")
    test(p, n)
