# -*- coding: utf-8 -*-
# Copyright (c) 2010--2012  Peter Dinges <pdinges@acm.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


"""
Auxiliary functions for computations related to prime numbers.

The algorithms and implementations are kept as simple as possible. They are
not meant for high performance computing, but for instructive purposes.

@package   support.primes
@author    Peter Dinges <pdinges@acm.org>
@author    Colin Branca <colin.branca@epfl.ch>
"""

from math import ceil, sqrt

#List of 100 first primes
firstPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
                61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131,
                137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197,
                199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271,
                277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353,
                359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433,
                439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509,
                521, 523, 541]

def primes_range(lower_bound, upper_bound):
    """
    Return a list of all primes in the range [@p lower_bound, @p upper_bound).

    @note      The function returns an actual list, not a proper range object.
               Furthermore, it computes the complete list of primes up to
               @p upper_bound on each call. These characteristics make it badly
               suited for anything involving large ranges or large primes.

    @param     lower_bound     The minimum size for returned primes; typically
                               this is an integer, but any number object with
                               an integer interpretation works.
    @param     upper_bound     The strict upper bound for returned primes: all
                               returned primes are strictly less than this
                               number.
    """
    # The sieve of Eratosthenes
    primes = set( range(2, upper_bound) )
    sieve_bound = ceil( sqrt(upper_bound) )
    for i in range(2, sieve_bound):
        if i in primes:
            multiples = [ i*j for j in range(2, ceil(upper_bound / i)) ]
            primes -= set(multiples)
    return sorted(list( primes - set(range(2, lower_bound)) ))


def inverse_primorial(n, shunned = 0):
    """
    Return the smallest prime @c p such that the product of all primes
    up to @c p (inclusive) is at least @p n. For example,
    @c inverse_primorial(30) is 5, and @c inverse_primorial(31) is 7.

    @note      This function uses primes_range() to obtain a list of primes.
               See the notes there for use case limitations.

    @param     n   The number object that the product must exceed in size.
                   The object must have an integer interpretation.

    @return    The prime @c p such that the product of all primes up to @c p
               (inclusive) is at least @p n; if @p n is too small (less than 2)
               the result is 2.
    """
    product = 1
    # A much smaller upper bound should suffice; however, we play it safe.
    for prime in primes_range(2, int(n)+1):
        if prime != shunned:
            product *= prime
            if product >= n:
                return prime
    # Return the smallest prime if n is too small
    return 2

def isPrime(n):
    """
    Return whether or not @c n is prime

    @note      This function first check if @c n is even or is one
               of the first 100 primes
               Then use Miller Rabin method to check its primality.

    @param     n   The number to test primality

    @return    True if @c n is prime, False otherwise
    """
    #test if n is a known prime
    if n in firstPrimes:
        return True

    #test if n = 2^k
    if n % 2 == 0 or n == 1:
        return False

    #use miller rabin method to test primality
    return millerRabin(n)

#miller rabin primality test
def millerRabin(n):
    """
    Return whether or not @c n is prime

    @param     n   The number to test primality

    @return    True if @c n is prime, False otherwise
    """
    primesToTest = selectPrimesToTest(n)
    for k in primesToTest:
        if millerWitness(k, n):
            return False
    return True

#test if a is a witness for n
def millerWitness(a, n):
    """
    Return whether or not @c a is a witness for @c n

    @param     a   The potential witness
    @param     n   The number to test primality

    @return    True if @c a is a witness for @c n
    """
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
    """
    Return @c s and @c d as 2^@c s * @c d = @c n-1

    @note      This function is usefull for millerWitness function

    @param     n   The number to decompose

    @return    @c s and @c d as 2^@c s * @c d = @c n-1
    """
    d = n - 1
    s = 0
    while(d % 2 == 0):
        s += 1
        d /= 2
    return (s, int(d))


def selectPrimesToTest(n):
    """
    Return list of primes to test for Miller Rabin

    @note      This function is usefull for millerRabin function

    @note      numbers are taken from: Handbook of Applied Cryptography (chapter 4)
               by A. Menezes, P. van Oorschot, and S. Vanstone, CRC Press, 1996.

    @param     n   selecter for list of primes

    @return    list of primes to test for Miller Rabin
    """
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
