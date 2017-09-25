class FiniteField(p):

    #return x mod p
    def f(x):
        return x % p

    #add two numbers mod p
    def add(self, a, b):
        return f(a + b)

    #return opposite (mod p) of input number
    def opposite(self, a):
        return (p-a) % p

    #substract two numbers mod p
    def substract(self, a, b):
        return f(a + opposite(self, b))

    #multiply two numbers mod p
    def multiply(self, a, b):
        return f(a*b)

    #return inverse (mod p) of input number
    def inverse(self, a):
        return euclide(p, a)

    #divide two numbers (mod p)
    def divide(self, a, b):
        return multiply(a, inverse(self, b))

    #return a^b (mod p)
    def power(self, a, b):
        if b == 0:
            return 1
        elif b == 1:
            return a
        elif b % 2 == 0:
            halfPower = power(self, a, b/2)
            return multiply(halfPower, halfPower)
        else:
            halfPower = power(self, a, (b-1)/2)
            return multiply(multiply(a, halfPower), halfPower)

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
            return null
        x.append(c)
        r.append(r[i-1] - c*r[i])
        s.append(s[i-1] - c*s[i])
        if gamma==1:
            return s[i+1]
        else :
            return helper(x, r, s i++)

    res = helper(x, r, s, 1)
    return res if res > 0 else f(res)
