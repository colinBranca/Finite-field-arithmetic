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

    limit = sqrt(x)

    for i in range(3, limit+1, 2):
        if x % i == 0:
            return False
    return True


#return the square root of a number rounded to lower value
#using Newton's method
def sqrt(a):
    x1 = float(a)
    dif = 1
    while dif > 0.1:
        x2 = 0.5 * (x1 + a/x1)
        dif = abs(x1 - x2)
        x1 = x2
    return int(x1)
