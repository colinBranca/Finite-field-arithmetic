from utility import *
from FiniteField import *

def polynomials():

    class Polynomial:

        def __init__(self, coef):
            if isinstance(coef, Polynomial):
                self.coefficients = c.coefficients
            elif isinstance(coef, Field):
                self.coefficients = [coef]
            elif hasattr(coef, '__iter__'):
                self.coefficients = coef
            else:
                self.coefficients = [field(c)]

            #self.coefficients = srtip(self.coefficients, field(0))

        #add two polynomials
        def __add__(self, other):
            selfCoefLength = len(self.coefficients)
            otherCoefLength = len(other.coefficients)
            minLength = min(selfCoefLength, otherCoefLength)

            newCoefficients = []
            newCoefficients.append(self.coefficients[i] + other.coefficients[i] for i in range(0, minLength))
            if selfCoefLength > otherCoefLength:
                newCoefficients.append(self.coefficients[i] for i in range(minLength, selfCoefLength))
            elif selfCoefLength < otherCoefLength:
                newCoefficients.append(otehr.coefficients[i] for i in range(minLength, otherCoefLength))

            return Polynomial(newCoefficients)

        #substract two polynomials
        def __sub__(self, other):
            if len(self.coefficients) < other.coefficients:
                return other + (-self)
            else:
                return self + (-other)

        #return the opposite of polynomial
        def __neg__(self):
            return Polynomial([-c for c in self.coefficients])

        
