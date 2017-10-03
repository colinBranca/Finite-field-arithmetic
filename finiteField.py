from utility import *

def FiniteField(p):

    class Field:

        def __init__(self, n):
            self.n = n % p
            self.field = Field

        #add two numbers mod p
        def __add__(self, other):
            return Field(self.n + other.n)

        #return opposite (mod p) of input number
        def __neg__(self):
            return Field(p - self.n)

        #substract two numbers mod p
        def __sub__(self, other):
            return self + (-other)

        #multiply two numbers mod p
        def __mul__(self, other):
            return Field(self.n * other.n)

        #return inverse (mod p) of input number
        def inverse(self):
            return Field(euclide(p, self.n))

        #divide two numbers (mod p)
        def __div__(self, other):
            return self * other.inverse()

        #return a^b (mod p)
        def __pow__(self, other):
            #if the power is an integer
            if type(other) is int:
                power = other
            #if the power is a FiniteField
            elif isinstance(other, Field):
                power = other.n
            #else we do nothing
            else:
                return Field(0)

            if power == 0:
                return 1
            elif power == 1:
                return self
            elif power % 2 == 0:
                halfPower = self ** Field(power/2)
                return halfPower * halfPower
            else:
                halfPower = self ** Field((power-1)/2)
                return self * halfPower * halfPower

        #return the field as a string
        def __str__(self) :
            return '%d mod(%d)' % (self.n, self.p)

        #return the field as a string
        def __repr__(self) :
            return '%d mod(%d)' % (self.n, self.p)

    if(isPrime(p)):
        Field.p = p
    else:
        print 'p is not prime'
        return
    return Field
