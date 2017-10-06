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



#test if number is prime or not
def isPrime(n):
    #test if n is a known prime
    if n in (2, 3, 5, 7):
        return True
    #test if n = 2^k
    elif n % 2 == 0 or n == 1:
        return False

    #use miller rabin method to test primality
    return millerRabin(n)


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

#miller rabin primality test
def millerRabin(n):
    #for n odd, at least 3/4 of intergers a, 1 < a < n are witnesses
    #so we test k times, with k = ceil(n/4)
    k = ceilDiv(n, 4)
    a = 2
    while k > 0:
        if millerWitness(a, n):
            return False
        k -= 1
        a += 1
    return True

#test if a is a witness for n
def millerWitness(a, n):
    (s, d) = findSD(n)
    x = a**d % n
    if x == 1:
        return False
    while s > 0 :
        x = x**2 % n
        if x == 1:
            return False
        s -= 1
    return True

#return s and d as 2^s * d = n-1
def findSD(n):
    d = n - 1
    s = 0
    while(d % 2 == 0):
        s += 1
        d /= 2
    return (s, d)

#return ceil(a/b)
def ceilDiv(a, b):
    return -(-a // b)
