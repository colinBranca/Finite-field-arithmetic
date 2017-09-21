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
        (x, y) = euclide(p, a)
        return bezout(x, y)
    def divide(slef, a, b):
        return f(a/b)

def euclide(a, b):
    x = [a]
    y = [b]

    def helper(x, y, i):
        c = x[i]//y[i]
        if c < 1:
            return (0, 0)
        x.append(y[i])
        y.append(c)
        if c==1:
            return (x, y)
        else :
            return helper(x, y, i++)

    return helper(x, y, 0)


def bezout(a, b, c):
