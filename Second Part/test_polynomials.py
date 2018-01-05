import sys

from  rings.polynomials.naive import Polynomials
from fields.finite.naive import FiniteField
from support.primes import *

def test(p, n):
    GF7  = FiniteField( p )
    GF7x = Polynomials( GF7 )
    f = GF7x.random_element(n)

    print(f)

    factors = f.factor()

    for fac, d in factors:
        print (fac, d)


if __name__ == "__main__":
    
    p = int(sys.argv[1])
    n = int(sys.argv[2])
    if not isPrime(p):
        sys.exit("p is not prime")
    test(p, n)