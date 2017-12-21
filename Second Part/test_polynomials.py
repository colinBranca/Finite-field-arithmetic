import sys
import rings.polynomials.naive
import fields.finite.naive
import support.primes

def test(p, n):
    GF7 = fields.finite.naive.FiniteField( p )
    GF7x = rings.polynomials.naive.Polynomials( GF7 )
    f = GF7x.random_element(n)
    factors = f.factorize()
    for x in factors:
         test = x.is_irreducible()
         print(repr(test))

if __name__ == "__main__":
    p = int(sys.argv[1])
    n = int(sys.argv[2])
    if not support.primes.isPrime(p):
        sys.exit("p is not prime")
    test(p, n)
