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

#Find inverse of a number (mod p) using extented Euclide algorithm
def euclide(a, b):
    x = [a, b]
    r = [1, 0]
    s = [0 ,1]

    def helper(x, r, s, i):
        alpha = x[i-1]
        beta = x[i]

        c = (alpha//beta)
        gamma = alpha - beta*c
        if gamma < 1:
            return s[i]
        x.append(x[i-1] - c*x[i])
        r.append(r[i-1] - c*r[i])
        s.append(s[i-1] - c*s[i])
        if gamma==1:
            return s[i+1]
        else :
            return helper(x, r, s, i+1)

    res = helper(x, r, s, 1)
    return res if res > 0 else res

def isPrime(x):
    if x == 2:
        return True
    elif x % 2 == 0 or x == 1:
        return False

    for i in range(3, x, 2):
        if x % i == 0:
            return False
    return True
