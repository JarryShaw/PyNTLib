#-*- coding: utf-8 -*-

'''
Alternative declaration:
__import__([folder.]module).[module.]function(*args, **kwargs)
'''

from NTLArchive.NTLValidations import *

#Inherit Polynomial class.
from NTLArchive import NTLPolynomial
class Polynomial(NTLPolynomial.Polynomial):
    pass

#Inherit Congruence class.
from NTLArchive import NTLCongruence
class Congruence(NTLCongruence.Congruence):
    pass

#Inherit Quadratic class.
from NTLArchive import NTLQuadratic
class Quadratic(NTLQuadratic.Quadratic):
    pass

#Inherit Index class.
from NTLArchive import NTLIndex
class Index(NTLIndex.Index):
    pass

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

#Return the solutions of a naïve congruence set.
def crt(*args):
    from NTLArchive import NTLChineseRemainderTheorem
    return NTLChineseRemainderTheorem.CHNRemainderTheorem(*args)

#Return the solutions of a polynomial congruence.
def congsolve(cgcExp, cgcCoe, modulo):
    from NTLArchive import NTLPolynomialCongruence
    return NTLPolynomialCongruence.polynomialCongruence(cgcExp, cgcCoe, modulo)

#Return the solutions of a quadratic equation.
def quadratic(p):
    from NTLArchive import NTLQuadraticEquation
    return NTLQuadraticEquation.quadraticEquation(p)

#Return the order of an integer (a) for a modulo (m), i.e. ord_m(a).
def ord(m, a):
    from NTLArchive import NTLOrder
    return NTLOrder.order(m, a)

#Return the primitive root(s) of modulo (m).
def root(m):
    from NTLArchive import NTLPrimitiveRoot
    return NTLPrimitiveRoot.primitiveRoot(m)

#Return the primitive residue class of an integer m.
def prc(m):
    from NTLArchive import NTLPrimitiveResidueClass
    return NTLPrimitiveResidueClass.primitiveResidueClass(m)

#Return Euler function φ(m).
def euler(m):
    from NTLArchive import NTLEulerFunction
    return NTLEulerFunction.eulerFunction(m)

#Return the result of Legendre symbol for (a | p).
def legendre(a, p):
    from NTLArchive import NTLLegendreSymbol
    return NTLLegendreSymbol.legendreSymbol(a, p)

#Return the result of Jacobi symbol for (a | m).
def jacobi(a, m):
    from NTLArchive import NTLJacobiSymbol
    return NTLJacobiSymbol.jacobiSymbol(a, m)

#Return if an integer is a Carmicheal number.
def carmicheal(n):
    from NTLArchive import NTLCarmichealTest
    return NTLCarmichealTest.carmichealTest(n)

#Return a pseudo-prime number with certain paterns.
def pseudo(**kwargs):
    from NTLArchive import NTLPseudoPrime
    return NTLPseudoPrime.pseudoPrime(**kwargs)
