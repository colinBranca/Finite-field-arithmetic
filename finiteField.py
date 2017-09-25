class FiniteField:

    def __init__(self, p):
        self.p = p

    #return x mod p
    def f(self, x):
        return x % self.p

    #add two numbers mod p
    def add(self, a, b):
        return self.f(a + b)

    #return opposite (mod p) of input number
    def opposite(self, a):
        return self.f(self.p - a)

    #substract two numbers mod p
    def substract(self, a, b):
        return self.f(a + self.opposite(b))

    #multiply two numbers mod p
    def multiply(self, a, b):
        return self.f(a*b)

    #return inverse (mod p) of input number
    def inverse(self, a):
        return self.f(euclide(self.p, a))

    #divide two numbers (mod p)
    def divide(self, a, b):
        return self.multiply(a, self.inverse(b))

    #return a^b (mod p)
    def power(self, a, b):
        if b == 0:
            return 1
        elif b == 1:
            return self.f(a)
        elif b % 2 == 0:
            halfPower = self.power(a, b/2)
            return self.multiply(halfPower, halfPower)
        else:
            halfPower = self.power(a, (b-1)/2)
            return self.multiply(self.multiply(a, halfPower), halfPower)

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
