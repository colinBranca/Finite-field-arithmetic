import sys

from  rings.polynomials.naive import Polynomials
from fields.finite.naive import FiniteField
from support.primes import *
from random import randrange

def test_single(p):
    GF7  = FiniteField( p )
    GF7x = Polynomials( GF7 )
    i = 0
    product = 1
    factors = []
    while i < 5:
        degree = randrange(1, 10)
        times  = randrange(1, 4)
        f = GF7x.random_monic_poly_degree(degree)
        if f.is_irreducible():
            i = i + 1
            factors.append((f, times))

    product = GF7x.one()
    for fac, mu in factors:
#        print(fac, mu)
        product *= (fac**mu)

#    print(product)
#    print('-------------------------')

    result = product.factor()
    prod_res = GF7x.one()
    for fac, mu in result:
#        print(fac, mu)
        prod_res *= (fac**mu)

#    print(prod_res)
    if product.monic() == prod_res.monic():
        return True
    else:
        return False


#    print(i)
#    print("-----------")
#    factors = product.factor()
#    print(len(factors))
#    newProduct = 1
#    for fac, d in factors:
#        print(fac)
#        print(fac.is_irreducible())
#        for i in range(0, d):
#            newProduct = newProduct * fac
#    print(product)
#    print(newProduct)
#    print(newProduct == product)
#

if __name__ == "__main__":

    p = int(sys.argv[1])
    num_tests = int(sys.argv[2])
    if not isPrime(p):
        sys.exit("p is not prime")
    for _ in range(num_tests):
        if not test_single(p):
            print('Error')
            break
