#-*- coding: utf-8 -*-

'''
Alternative declaration:
__import__(folder.module).module.function(*args, **kwargs)
'''

#Return all prime numbers less then N.
def primelist(N):
    import NTLEratosthenesSieve
    return NTLEratosthenesSieve.eratosthenesSieve(N)    

#Return if a and b are divisible.
def isdivisible(a, b):
    import NTLEuclideanDivision
    return NTLEuclideanDivision.euclideanDivision(a, b)

#Return if N is a prime.
def isprime(N):
    import NTLTrivialDivision
    return NTLTrivialDivision.trivialDivision(N)

#Return the greatest common divisor of a and b.
def gcd(a, b):
    import NTLGreatestCommonDivisor
    return NTLGreatestCommonDivisor.greatestCommonDivisor(a, b)

#Return if a and b are coprime numbers.
def coprime(a, b):
    import NTLCoprimalityTest
    return NTLCoprimalityTest.coprimalityTest(a, b)

#Return the parameters of a and b in Bézout equation.
def bezout(a, b):
    import NTLBezoutEquation
    return NTLBezoutEquation.bezoutEquation(a, b)

#Return the prime factor list of N.
def factor(N):
    import NTLPrimeFactorisation
    return NTLPrimeFactorisation.primeFactorisation(N)

#Return the solutions for N|a^2-b^2 while N∤a+b and N∤a-b.
def decomposit(N):
    import NTLQuadraticFactorisation
    return NTLQuadraticFactorisation.quadraticFactorisation(N)

#Return the special solutions for indefinite binary equation, a*x + b*y = c.
def binary(a, b, c):
    import NTLBinaryEquation
    return NTLBinaryEquation.binaryEquation(a, b, c)

#Return the result of b^e (mod m).
def modulo(b, e, m):
    import NTLRepetiveSquareModulo
    return NTLRepetiveSquareModulo.repetiveSquareModulo(b, e, m)

#Return the coefficients and exponents of quotient and ratio after polynomial Euclidean division.
def polydiv(dvdExp, dvdCoe, dvsExp, dvsCoe):
    import NTLPolynomialEuclideanDivision
    return NTLPolynomialEuclideanDivision.polyED(dvdExp, dvdCoe, dvsExp, dvsCoe)

#Return the coefficients and exponents of quotient and ratio after congruence simplification.
def simplify(cgcExp, cgcCoe, modulo):
    import NTLCongruenceSimplification
    return NTLCongruenceSimplification.congruenceSimplification(cgcExp, cgcCoe, modulo)

#Return the solutions of a polynomial congruence.
def polymod(cgcExp, cgcCoe, modulo):
    import NTLPolynomialCongruence
    return NTLPolynomialCongruence.polynomialCongruence(cgcExp, cgcCoe, modulo)

#Return the solutions of a quadratic equation.
def quadratic(p):
    import NTLQuadraticEquation
    return NTLQuadraticEquation.quadraticEquation(p)

#Return the index of an integer (a) for a modulo (m).
def index(m, a):
    import NTLPrimitiveIndex
    return NTLPrimitiveIndex.primitiveIndex(m, a)

#Return the index of an integer (a) for a prime modulo (p).
def indexPrime(p, a):
    import NTLPrimeIndex
    return NTLPrimeIndex.primeIndex(p, a)

#Return the primitive root(s) of an odd prime modulo (p).
def root(p):
    import NTLPrimitiveRoot
    return NTLPrimitiveRoot.primitiveRoot(p)
