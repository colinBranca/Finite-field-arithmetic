class FiniteField(p):
    def f(x):
        return x % p

    def add(self, a, b):
        return f(a + b)
    def opposite(self, a):
        return (p-a) % p
    def substract(self, a, b):
        return f(a + opposite(self, b))
    def multiply(self, a, b):
        return f(a*b)
    def inverse(self, a):
        return euclide(p, a)
    def divide(slef, a, b):
        return multiply(a, inverse(self, b))

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
