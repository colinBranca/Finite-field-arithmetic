# Finite Field Arithmetic in Python
This is a semester project done in Autumn 2017
At Laboratory for Cryptologic Algorithms, EPFL


# Introduction
The goal of the project was to implement a simple Python library for finite field arithmetic which only depends on standard Python libraries.

The [Schoof Library](https://github.com/pdinges/python-schoof) was taken as base of the project and algorithms were implemented on top of it.
We first began the project from scratch and implemented some classes but finally chose to work with this library.
The generic type system used in this library and the presence of all the basic algorithms were the main arguments to use it as base of the project.

On top of the *Schoof Library*, the following functions were implemented: exponentiation function, primality testing and polynomial factorization.


# Implementation
## Schoof Library Structure
The Library is composed in three main sections : ```elliptic curves```, ```fields``` and ```rings```. There is also a ```support``` folder where we can find useful functions.
Only the classes that were usefull in the project are presented below.

  * The ```FiniteField``` class is a subclass of the ```Field``` class and it represents a prime finite field. An object of the class is constructed with a given prime ```p```. All basics operations are implemented, such as addition, multiplication, exponentiation, etc.
  * The ```Polynomials``` class is contained in ```rings``` directory. An object of the class is constructed with a given coefficient field (i.e. ```FiniteField``` object). A polynomial can then be constructed by simply passing a list of coefficients. All basics operations are implemented, such as addition, multiplication, exponentiation, etc.
  * The ```primes``` file is located in ```support```, and it is composed of auxiliary functions for computations related to prime numbers.


## Selected Algorithms
### Extended Euclidean Algorithm

As its name suggests, this algorithm is based on the *Euclidean Algorithm*. Given two integers, the *Euclidean Algorithm* finds their *greatest common divisor*.
To find $gcd(a, b)$ , we set $a = q_0 b + r_0$ and then recursively resolve the following equations until we find a null remainder.
$$
a = q_0 b + r_0
$$
$$
b = q_1 r_0 + r_1
$$
$$
r_0 = q_2 r_1 + r_2
$$
$$
...
$$

```c
EUCLIDEAN_ALGORITHM(a, b)
INPUT: two integers a and b
OUTPUT: an integer u such as u = gcd(a,b)
1. IF b = 0, return a
   ELSE return EUCLIDEAN_ALGORITHM(b, a mod b)
```
Given two integers $a$ and $b$, the *Extended Euclidean Algorithm* computes, in addition to their greatest common divisor,
the coeficients of *Bezout Identity* $x$ and $y$ such as
$$
ax + by = gcd(a, b)
$$

```c
EXTENDED_EUCLIDEAN_ALGORITHM(u,v)
INPUT: two integers u and v
OUTPUT: (u1, u2, u3) such as u*u1 + v*u2 = u3 = gcd(u, v)
1. SET (u1, u2, u3) = (1, 0, u), (v1, v2, v3) = (0, 1, v)
2. IF v3 = 3, the algorithm terminates
3. SET q = floor(u3/v3) AND THEN SET
    (t1, t2, t3) = (u1, u2, u3) - (v1, v2, v3) * q
    (u1, u2, u3) = (v1, v2, v3)
    (v1, v2, v3) = (t1, t2, t3)
   RETURN TO STEP 2
```

Knowing that $p$ is prime, ${gcd(p, n) = 1}$. So we have ${xn\ +\ yp = 1}$ and ${xn = 1 \ mod(p)}$. Finally we find the inverse ${x=n^{-1}}$.

### Exponentiation
A naive method to compute $a^n$ is simply to multiply $a$ by itself $n$ times. This obviously works but its complexity, $\mathcal{O}(n)$, can be improved.

The *Square-and-Multiply* methods is implemented for this goal. It works with the bit representation of the input exponent $n$.
Knowing that for a positive $n$, we have
$$
a^n = \begin{cases} a(a^2)^{n-1/2}, \ if \ n \ is \ odd \\ (a^2)^{n/2}, \ \ \ \ \ \ \ if \ n \ is \ even \end{cases}
$$
If we take, for example, $n=5$. We have its binary representation ${n \equiv 101}$ and the following steps.  \
First initialize $result = 1 \ (= a^0)$.  \
Set $result = result^2  \ (= a^0)$.  \
The first bit $b_1=1$ so we set $result = result*a  \ (= a^1)$.  \
Set $result = result^2  \ (= a^2)$. \
The second bit $b_2=0$ so there is nothing more to do.  \
Set $result = result^2  \ (= a^4)$. \
The third bit $b_3=1$ so we set $result = result*a  \ (= a^5)$.  \


```c
POWER(a, n)
INPUT: two numbers a and n, n is a positive integer
OUTPUT: a^n
1. SET result = a, i = most significant bit of n
2. result = result * result
3. IF i = 1, result = result * a
4. IF i is the last bit of n, the algorithm terminates
   ELSE i = next bit, RETURN TO STEP 2
```

### Miller Rabin

Knowing that we are working in finite fields, primes take an essential role in the project.
Primality testing can therefore very useful to unsure the numbers we are working with are prime.

The most naive primality test is *trial division*. Given an integer $n$, we can check whether any prime number in the range $[2, \sqrt n]$ divides $n$.
If we find an $x$ that divides $n$ then $n$ is not prime, else it is.

This method has a far to big complexity: $\mathcal{O}(n^{1/2})$. In order to improve the runtime, we used the *Miller Rabin primality test* which is a probabilistic method that runs in $\mathcal{O}(log^3 n)$.
Our implementation is more deterministic and has complexity of $\mathcal{O}(log^4 n)$.

This test is based on the following claim:
Let's assume a prime ${n > 2 }$. We can write :
$$
n-1 = 2^s  d , \ where \ s,\ d\ <\ 0 \ and\ d\ is\ odd
$$
From Fermat's little theorem, for a prime number $n$:
$$
a^{n-1} \equiv 1 \ (mod\ n)
$$
$$
a^{2^s  d} \equiv 1 \ (mod\ n)
$$
From there, we know that for each $a$ in (Z/nZ)* we have :
$$
a^d \equiv 1 \ (mod\ n)
$$
or
$$
a^{2^r d} \equiv -1 \ (mod\ n) \ for \ some \ r : \ 0\leqslant r \leqslant s-1
$$
So if we can find an $a$, $1<a<n$, such as :
$$
a^d \neq 1 \ (mod\ n)
$$
and
$$
a^{2^r d} \neq -1 \ (mod\ n)
$$
we can prove that $n$ is not prime. Such a number $a$ is called a *Miller Witness*.

To determine the primality of any integer ${n < \psi_t }$, where $\psi_t$ is the smallest positive composite integer
which is a strong pseudoprime (composite number that passes a strong version of a primality test)
to all the bases of the first $t$ primes, it is sufficient to call the *Miller Rabin test* with $a = p$ for all $p$ in the first $t$ primes.  \
\newpage
The following table gives values of $\psi_t$ for ${1 \leqslant t \leqslant 7}$.

<center>

|$t$ |  $\psi_t$        |
|----|------------------|
|  1 |  2047            |
|  2 |  1373653         |
|  3 |  25326001        |
|  4 |  3215031751      |
|  5 |  2152302898747   |
|  6 |  3474749660383   |
|  7 |  341550071728321 |

</center>

### Polynomial Factorization
The main part of the project was polynomial factorization over prime.
We first define $K$ as a field with $q$ elements, where $q=p^n$ and $p$ is prime. By *Euler Theorem* [@ACN], the multiplicative group $K^\times$ has order $q-1$. So we can write:
$$
\forall a \in K^\times, \ a^{q-1}=1
$$
With this, we know that all $a \in K$ are solutions of ${X^q - X}$.
Obviously, we also know that ${0^q=0}$. So we have $q$ roots of ${X^q - X}$.
Since this equation cannot have more than $q$ roots, we can factorize it:
$$
X^q - X = \prod_{a \in K} (X - a)
$$

Given $P \in F_p[X]$ a monic polynomial of degree $n$, one can show that all its factors of degree $d$
are those that are also factors of $X^{p^d} - X$.

So, given a polynomial $P(X)$, if we compute $gcd(P, X^{p^d} - X)$, we obtain a polynomial $G_d$
which is the product of all irreducible polynomials of degree $d$ that are factors of $P$.

We can therefore begin the factorization process by decomposing our polynomial into smaller polynomials $G_i$.
We know that each of these polynomials $G_i$ can be factorized into irreducible polynomials which have all the same degree $i$.
```c
DISTINCT_DEGREE_FACTORIZATION(poly)
INPUT: a monic square free polynomial poly
OUTPUT: The set of all pairs (g, d), such that
             f has an irreducible factor of degree d and
             g is the product of all monic irreducible
               factors of f of degree d
1. SET i = 1, S = {}, poly = f
2. g = gcd(f, x^(p^i) - x)
3. if g != 1
  1. S = S U (f, degree of f)
  2. f = f/g
4. i = i + 1
5. IF degree of f >= 2*i, RETURN TO STEP 2
6. IF degree of f != 1, S = S U (f, degree of f)
7. IF S is empty return {(f, 1)}
   ELSE return S
```

The last step of the process is, given the polynomial $P \in F_p[X]$ and the product of irreducible factors ($G_d$) which are all of degree $d$, find these factors.
To do this, the *Cantor-Zassenhaus* algorithm is used.

This algorithm takes as input $G_d$ which has at least two factors (otherwise it is already irreducible) and the degree of its factors $d$.
Let $T \in F_p[X]$, we have
$$
T^{p^d} - T = T(T^{(p^d - 1)/2} + 1)(T^{(p^d - 1)/2} - 1)
$$
So
$$
G_d = gcd(G_d, T) \times gcd(G_d, T^{(p^d - 1)/2} + 1) \times gcd(G_d, T^{(p^d - 1)/2} - 1)
$$

Knowing that $G_d$ divides $T^{p^d} - T$, the common factors of $G_d$ and $T^{p^d} - T$ are just the factors of $G_d$.
These factors are therefore scattered in $T$, $T^{(p^d - 1)/2} + 1$ and $T^{(p^d - 1)/2} - 1$.

If we consider that the two last polynomials contain approximately half of these factors. Their degree is indeed about half of the one of $T^{p^d} - T$.
Furthermore we can show that, if we choose $T$ at random, the probability that $T^{(p^d - 1)/2} - 1$ contains at least one
of the factors of $G_d$ is $4/9$.

The algorithm takes a random $T$  and try to obtain a non-trivial factor of $G_d$ : $U$.
If it finds such a $U$, it applies the algorithm recursively on $U$ and $G_d / U$. If not it tries again with an other $T$.

```c
CANTOR_ZASSENHAUS(f, d)
INPUT: a monic square free polynomial f of degree n = rd,
       which has r >= 2 irreducible factors each of degree d
OUTPUT: The set of monic irreducible factors of f of degree d
1. SET factors = {f}
2. CHOOSE h in Fq[x] with deg(h) < n at random
3. SET e = (p^d - 1)/2 AND g = h^e - 1 (mod f)
4. FOR EACH u in factors with deg(u) > d do:
  1. IF gcd(g, u) != 1 AND gcd(g, u) != u,
        factors = factors \ {u} U {(gcd_temp, u/gcd_temp)}
5. IF size of factors < r, RETURN TO STEP 2
```



# Conclusion
The exponentiation function is often used, optimizing it is gainful for the total runtime of the program. \
We also implemented some missing functions. All the project was about working with prime numbers, prime testing was indeed
a must have to handle potential errors. \
Finding the inverse of a field element is useful for division, which is an often used operation.  \
Finally, the polynomial factorization was not present at all in the *Schoof Library*. This was the main part of the project.
We first implemented irreducibility testing and then a main algorithm to do the factorization.

One of the possible future implementations for this project would be polynomials over finite fields extensions and over rationals.
