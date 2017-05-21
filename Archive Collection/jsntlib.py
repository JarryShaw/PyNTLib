#-*- coding: utf-8 -*-

'''
Alternative declaration:
__import__([folder.]module).[module.]function(*args, **kwargs)
'''

#Return all prime numbers between lower and upper bound.
def primelist(upper, lower=2):
    from NTLArchive import NTLEratosthenesSieve
    return NTLEratosthenesSieve.eratosthenesSieve(upper, lower)

#Return if a and b are divisible.
def isdivisible(a, b):
    from NTLArchive import NTLEuclideanDivision
    return NTLEuclideanDivision.euclideanDivision(a, b)

#Return if N is a prime.
def isprime(N):
    from NTLArchive import NTLTrivialDivision
    return NTLTrivialDivision.trivialDivision(N)

#Return the greatest common divisor of a and b.
def gcd(a, b):
    from NTLArchive import NTLGreatestCommonDivisor
    return NTLGreatestCommonDivisor.greatestCommonDivisor(a, b)

#Return if a and b are coprime numbers.
def coprime(a, b):
    from NTLArchive import NTLCoprimalityTest
    return NTLCoprimalityTest.coprimalityTest(a, b)

#Return the parameters of a and b in Bézout equation.
def bezout(a, b):
    from NTLArchive import NTLBezoutEquation
    return NTLBezoutEquation.bezoutEquation(a, b)

#Return list of the quotients with extended Euclidean Algorithm.
def eealist(a, b):
    from NTLArchive import NTLEuclideanAlgorithm
    return NTLEuclideanAlgorithm.euclideanAlgorithm(a, b)

#Return the prime factor list of N.
def factor(N, **kwargs):
    from NTLArchive import NTLPrimeFactorisation
    return NTLPrimeFactorisation.primeFactorisation(N, **kwargs)

#Return the solutions for N|a^2-b^2 while N∤a+b and N∤a-b.
def decomposit(N):
    from NTLArchive import NTLQuadraticFactorisation
    return NTLQuadraticFactorisation.quadraticFactorisation(N)

#Return the special solutions for indefinite binary equation, a*x + b*y = c.
def binary(a, b, c):
    from NTLArchive import NTLBinaryEquation
    return NTLBinaryEquation.binaryEquation(a, b, c)

#Return the result of b^e (mod m).
def modulo(b, e, m):
    from NTLArchive import NTLRepetiveSquareModulo
    return NTLRepetiveSquareModulo.repetiveSquareModulo(b, e, m)

#Return the coefficients and exponents of quotient and ratio after polynomial Euclidean division.
def polydiv(dvdExp, dvdCoe, dvsExp, dvsCoe):
    from NTLArchive import NTLPolynomialEuclideanDivision
    return NTLPolynomialEuclideanDivision.polyED(dvdExp, dvdCoe, dvsExp, dvsCoe)

#Return the coefficients and exponents of quotient and ratio after congruence simplification.
def simplify(cgcExp, cgcCoe, modulo):
    from NTLArchive import NTLCongruenceSimplification
    return NTLCongruenceSimplification.congruenceSimplification(cgcExp, cgcCoe, modulo)

#Return the solutions of a polynomial congruence.
def polymod(cgcExp, cgcCoe, modulo):
    from NTLArchive import NTLPolynomialCongruence
    return NTLPolynomialCongruence.polynomialCongruence(cgcExp, cgcCoe, modulo)

#Return the solutions of a quadratic equation.
def quadratic(p):
    from NTLArchive import NTLQuadraticEquation
    return NTLQuadraticEquation.quadraticEquation(p)

#Return the index of an integer (a) for a modulo (m).
def index(m, a):
    from NTLArchive import NTLPrimitiveIndex
    return NTLPrimitiveIndex.primitiveIndex(m, a)

#Return the index of an integer (a) for a prime modulo (p).
def indexPrime(p, a):
    from NTLArchive import NTLPrimeIndex
    return NTLPrimeIndex.primeIndex(p, a)

#Return the primitive root(s) of an odd prime modulo (p).
def root(p):
    from NTLArchive import NTLPrimitiveRoot
    return NTLPrimitiveRoot.primitiveRoot(p)
