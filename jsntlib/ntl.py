# -*- coding: utf-8 -*-


'''
Alternative declaration:
__import__([folder.]module).[module.]function(*args, **kwargs)
'''


from .NTLArchive import NTLCongruence
from .NTLArchive import NTLFraction
from .NTLArchive import NTLIndex
from .NTLArchive import NTLJacobi
from .NTLArchive import NTLLegendre
from .NTLArchive import NTLPolynomial
from .NTLArchive import NTLQuadratic


__all__  = [
    'Congruence', 'Fraction', 'Index', 'Jacobi', 'Legendre', 'Polynomial', 'Quadratic',
    'bezout', 'binary', 'carmicheal', 'congsolve', 'coprime', 'crt', 'decomposit',
    'eealist', 'euler', 'factor', 'fraction', 'gcd', 'isdivisible', 'isprime',
    'jacobi', 'lcm', 'legendre', 'modulo', 'ord', 'polydiv', 'prc', 'prime', 'primelist',
    'pseudo', 'quadratic', 'root', 'simplify'
]


##############################################################################
# Class session.
##############################################################################


# Derives from Congruence class.
class Congruence(NTLCongruence.Congruence):
    pass


# Derives from Fraction class.
class Fraction(NTLFraction.Fraction):
    pass


# Derives from Index class.
class Index(NTLIndex.Index):
    pass


# Derives from Jacobi class.
class Jacobi(NTLJacobi.Jacobi):
    pass


# Derives from Legendre class.
class Legendre(NTLLegendre.Legendre):
    pass


# Derives from Polynomial class.
class Polynomial(NTLPolynomial.Polynomial):
    pass


# Derives from Quadratic class.
class Quadratic(NTLQuadratic.Quadratic):
    pass


##############################################################################
# Method session.
##############################################################################


# Returns the parameters of a and b in Bézout equation.
def bezout(a, b):
    from .NTLArchive import NTLBezoutEquation
    return NTLBezoutEquation.bezoutEquation(a, b)


# Returns the special solutions for indefinite binary equation, a*x + b*y = c.
def binary(a, b, c):
    from .NTLArchive import NTLBinaryEquation
    return NTLBinaryEquation.binaryEquation(a, b, c)


# Returns if an integer is a Carmicheal number.
def carmicheal(N):
    from .NTLArchive import NTLCarmichealTest
    return NTLCarmichealTest.carmichealTest(N)


# Returns the solutions of a polynomial congruence.
def congsolve(cgcExp, cgcCoe, modulo, **kwargs):
    from .NTLArchive import NTLPolynomialCongruence
    return NTLPolynomialCongruence.polynomialCongruence(cgcExp, cgcCoe, modulo, **kwargs)


# Returns if a and b are coprime numbers.
def coprime(a, b):
    from .NTLArchive import NTLCoprimalityTest
    return NTLCoprimalityTest.coprimalityTest(a, b)


# Returns the solutions of a naïve congruence set.
def crt(*args):
    from .NTLArchive import NTLChineseRemainderTheorem
    return NTLChineseRemainderTheorem.CHNRemainderTheorem(*args)


# Returns the solutions for N|a^2-b^2 while N∤a+b and N∤a-b.
def decomposit(N, **kwargs):
    from .NTLArchive import NTLQuadraticFactorisation
    return NTLQuadraticFactorisation.quadraticFactorisation(N, **kwargs)


# Returns list of the quotients with extended Euclidean Algorithm.
def eealist(a, b):
    from .NTLArchive import NTLEuclideanAlgorithm
    return NTLEuclideanAlgorithm.euclideanAlgorithm(a, b)


# Returns Euler function φ(m).
def euler(m):
    from .NTLArchive import NTLEulerFunction
    return NTLEulerFunction.eulerFunction(m)


# Returns the prime factor list of N.
def factor(N, **kwargs):
    from .NTLArchive import NTLPrimeFactorisation
    return NTLPrimeFactorisation.primeFactorisation(N, **kwargs)


# Returns the continued fraction of a real number.
def fraction(n, d=None):
    from .NTLArchive import NTLContinuedFraction
    return NTLContinuedFraction.continuedFraction(n, d)


# Returns the greatest common divisor of a and b.
def gcd(a, b):
    from .NTLArchive import NTLGreatestCommonDivisor
    return NTLGreatestCommonDivisor.greatestCommonDivisor(a, b)


# Returns if a and b are divisible.
def isdivisible(a, b):
    from .NTLArchive import NTLEuclideanDivision
    return NTLEuclideanDivision.euclideanDivision(a, b)


# Returns if N is a prime.
def isprime(N):
    from .NTLArchive import NTLTrivialDivision
    return NTLTrivialDivision.trivialDivision(N)


# Returns the result of Jacobi symbol for (a | m).
def jacobi(a, m):
    from .NTLArchive import NTLJacobiSymbol
    return NTLJacobiSymbol.jacobiSymbol(a, m)


# Returns the least common multiple of a and b.
def lcm(a, b):
    from .NTLArchive import NTLLeastCommonMultiple
    return NTLLeastCommonMultiple.leastCommonMultiple(a, b)


# Returns the result of Legendre symbol for (a | p).
def legendre(a, p, **kwargs):
    from .NTLArchive import NTLLegendreSymbol
    return NTLLegendreSymbol.legendreSymbol(a, p, **kwargs)


# Returns the result of b^e (mod m).
def modulo(b, e, m):
    from .NTLArchive import NTLRepetiveSquareModulo
    return NTLRepetiveSquareModulo.repetiveSquareModulo(b, e, m)


# Returns the order of an integer (a) for a modulo (m), i.e. ord_m(a).
def ord(m, a):
    from .NTLArchive import NTLOrder
    return NTLOrder.order(m, a)


# Returns quotient and remainder after polynomial Euclidean division.
def polydiv(dvdExp, dvdCoe, dvsExp, dvsCoe):
    from .NTLArchive import NTLPolynomialEuclideanDivision
    return NTLPolynomialEuclideanDivision.polyED(dvdExp, dvdCoe, dvsExp, dvsCoe)


# Returns the primitive residue class of an integer m.
def prc(m):
    from .NTLArchive import NTLPrimitiveResidueClass
    return NTLPrimitiveResidueClass.primitiveResidueClass(m)


# Retern iterator of prime numbers between lower and upper bound with steps.
def prime(upper, lower=None, steps=None):
    from .NTLArchive import NTLEratosthenesSieve
    return NTLEratosthenesSieve.primerange(upper, lower, steps)


# Returns all prime numbers between lower and upper bound with steps.
def primelist(upper, lower=None):
    from .NTLArchive import NTLEratosthenesSieve
    return NTLEratosthenesSieve.eratosthenesSieve(upper, lower)


# Returns a pseudo-prime number with certain paterns.
def pseudo(**kwargs):
    from .NTLArchive import NTLPseudoPrime
    return NTLPseudoPrime.pseudoPrime(**kwargs)


# Returns the solutions of a quadratic equation.
def quadratic(p, **kwargs):
    from .NTLArchive import NTLQuadraticEquation
    return NTLQuadraticEquation.quadraticEquation(p, **kwargs)


# Returns the primitive root(s) of modulo (m).
def root(m):
    from .NTLArchive import NTLPrimitiveRoot
    return NTLPrimitiveRoot.primitiveRoot(m)


# Returns the result after congruence simplification.
def simplify(cgcExp, cgcCoe, modulo, **kwargs):
    from .NTLArchive import NTLCongruenceSimplification
    return NTLCongruenceSimplification.congruenceSimplification(cgcExp, cgcCoe, modulo, **kwargs)
