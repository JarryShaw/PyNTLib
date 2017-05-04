 #-*- coding: utf-8 -*-

'''
def checkVersion(func):
    def funcWrapper(*args, **kwargs):
        if __import__("sys").version_info[0] > 2:
            print "This lib runs on python 2 only"
            raise SystemExit
        return func(*args, **kwargs)
    return funcWrapper
'''

if __import__("sys").version_info[0] > 2:
    print
    raise ImportError("This lib runs on python 2 only.")

#@checkVersion

#Return all prime numbers less then N.
def primelist(N):
    return __import__('NTLEratosthenesSieve').eratosthenesSieve(N)

#Return if a and b are divisible.
def isdivisible(a, b):
	return __import__('NTLEuclideanDivision').euclideanDivision(a, b)

#Return if N is a prime.
def isprime(N):
	return __import__('NTLTrivialDivision').trivialDivision(N)

#Return the greatest common divisor of a and b.
def gcd(a, b):
    return __import__('NTLGreatestCommonDivisor').greatestCommonDivisor(a, b)

#Return if a and b are coprime numbers.
def coprime(a, b):
    return __import__('NTLCoprimalityTest').coprimalityTest(a, b)

#Return the parameters of a and b in Bézout equation.
def bezout(a, b):
    return __import__('NTLBezoutEquation').bezoutEquation(a, b)

#Return the prime factor list of N.
def factor(N):
    return __import__('NTLPrimeFactorisation').primeFactorisation(N)

#Return the solutions for N|a^2-b^2 while N∤a+b and N∤a-b.
def decomposit(N):
    return __import__('NTLQuadraticFactorisation').quadraticFactorisation(N)

#Return the special solutions for indefinite binary equation, a*x + b*y = c.
def binary(a, b, c):
    return __import__('NTLBinaryEquation').binaryEquation(a, b, c)

#Return the result of b^e (mod m).
def modulo(b, e, m):
    return __import__('NTLRepetiveSquareModulo').repetiveSquareModulo(b, e, m)

#Return the coefficients and exponents of quotient and ratio after polynomial Euclidean division.
def polydiv(dvdExp, dvdCoe, dvsExp, dvsCoe):
    return __import__('NTLPolynomialEuclideanDivision').polyED(dvdExp, dvdCoe, dvsExp, dvsCoe)

#Return the coefficients and exponents of quotient and ratio after congruence simplification.
def simplify(cgcExp, cgcCoe, modulo):
    return __import__('NTLCongruenceSimplification').congruenceSimplification(cgcExp, cgcCoe, modulo)

#Return the solutions of a linear congruence.
def linear(cgcExp, cgcCoe, modulo):
    return __import__('NTLLinearCongruence').linearCongruence(cgcExp, cgcCoe, modulo)

#Return the solutions of a quadratic congruence.
def quadratic(p):
    return __import__('NTLQuadraticEquation').quadraticEquation(p)
