#Find inverse of a n mod p using extented Euclide algorithm
def euclide(n, p):
    x = [p, n]
    s = [0 ,1]

    def helper(x, s, i):
        alpha = x[i-1]
        beta = x[i]

        c = (alpha//beta)
        gamma = alpha - beta*c
        if gamma < 1:
            return s[i]
        x.append(gamma)
        s.append(s[i-1] - c*s[i])
        if gamma==1:
            return s[i+1]
        else :
            return helper(x, s, i+1)

    res = helper(x, s, 1)
    return res



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
    primesToTest = selectPrimesToTest(n)
    for k in primesToTest:
        if millerWitness(k, n):
            return False
    return True

#test if a is a witness for n
def millerWitness(a, n):
    (s, d) = findSD(n)
    x = pow(a, d, n)
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

#return the primes to test in millerRabin
#numbers are taken from: Handbook of Applied Cryptography (chapter 4)
#by A. Menezes, P. van Oorschot, and S. Vanstone, CRC Press, 1996.
def selectPrimesToTest(n):
    primes = [2, 3]
    if n < 1373653:
        return primes
    primes += [5]
    if n < 25326001:
        return primes
    primes += [7]
    if n < 3215031751:
        return primes
    primes += [11]
    if n < 2152302898747:
        return primes
    primes += [13]
    if n < 3474749660383:
        return primes
    primes += [17]
    if n < 341550071728321:
        return primes

    #otherwise return all primes smaller than 100
    primes += [x for x in range(19, 100, 2) if isPrime(x)]
    return primes
