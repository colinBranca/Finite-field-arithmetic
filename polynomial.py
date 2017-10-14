from finiteField import FiniteField

def Polynomials(field):

    class Polynomial:

        def __init__(self, coef):
            if isinstance(coef, Polynomial):
                self.coefficients = c.coefficients
            elif isinstance(coef, field):
                self.coefficients = [coef]
            elif hasattr(coef, '__iter__'):
                self.coefficients = [field(c) for c in coef]
            else:
                self.coefficients = [field(coef)]

            #self.coefficients = srtip(self.coefficients, field(0))

        #add two polynomials
        def __add__(self, other):
            selfCoefLength = len(self)
            otherCoefLength = len(other)
            minLength = min(selfCoefLength, otherCoefLength)

            newCoefficients = []
            newCoefficients.append(self[i] + other[i] for i in range(0, minLength))
            if selfCoefLength > otherCoefLength:
                newCoefficients.append(self[i] for i in range(minLength, selfCoefLength))
            elif selfCoefLength < otherCoefLength:
                newCoefficients.append(other[i] for i in range(minLength, otherCoefLength))

            return Polynomial(newCoefficients)

        #substract two polynomials
        def __sub__(self, other):
            if len(self) < len(other):
                return other + (-self)
            else:
                return self + (-other)

        #return the opposite of polynomial
        def __neg__(self):
            return Polynomial([-c for c in self])

        #return the degree of the Polynomial
        def degree(self):
            return len(self) - 1

        #test equality
        def __eq__(self, other):
            return self.degree() == other.degree() and all(sCoef == oCoef for (sCoef, oCoef) in zip(self, other))

        #test inequality
        def __ne__(self, other):
            return self.degree() != other.degree() or any(sCoef != oCoef for (sCoef, oCoef) in zip(self, other))

        #reprensent polynomial
        def __repr__(self):
            if(self.isNull()):
                return '0'
            tmpStr = 'f(x) = '
            for i in range (self.degree(), -1, -1):
                if self[i] != field(0):
                    if i > 1:
                        tmpStr += '%s*x^%d + ' % (self[i], i-1)
                    elif i == 1:
                        tmpStr += '%s*x + ' % (self[i])
                    else:
                        tmpStr += '%s' % (self[i])
            return tmpStr

        #return length of the polynomial
        def __len__(self):
            return len(self.coefficients)

        def __getitem__(self, i):
            return self.coefficients[i]

        #check if polynomial is equal to 0
        def isNull(self):
            return self.coefficients == []

        #multiply two polynomials
        def __mul__(self, other):
            if self.isNull() or other.isNull():
                return Polynomial([])
            newCoefficients = [0 for _ in range(len(self) + len(other) -1)]
            for i in range(0, len(self)):
                for j in range(0, len(self)):
                    newCoefficients[i+j] += self[i] * other[j]

            return Polynomial(newCoefficients)



    Polynomial.field = field
    return Polynomial
