# -*- coding: utf-8 -*-

import jsntlib

print

#Create an instacne of Polynomial.
print 'Create Polynomial.'
poly_1 = jsntlib.Polynomial((1,3), (3,4), (2,2), (34,(1+3j)), var='a')
poly_2 = jsntlib.Polynomial((1,0), (4,-4), (2,3), (0,1))
poly_3 = poly_1 // poly_2
print poly_1[:]
print poly_2
print poly_3

print

#Create an instacne of Congruence.
print 'Create Congruence.'
con_ = jsntlib.Congruence((2,1), (0,-46), mod=105, var='z')
rat_ = con_.solve()

print 'The solution of %s is\n\t' %str(con_),
print rat_

print

#Create an instacne of Quadratic.
print 'Create Quadratic.'
qua_ = jsntlib.Quadratic(8068, vars=('p', 'q'))
rst_ = qua_.solve()

print 'The solution of %s is' %str(qua_)
print rst_

print

#Create an instacne of Index.
print 'Create Index.'
index = jsntlib.Index(41)
print index
print
rst = index(4, 8)
print '4 * 8 ≡ %d' %rst

print

#Print all primes numbers less than 100.
print 'Call primelist.'
print jsntlib.primelist(100, -1)

print

#Check if 13 and 20 are divisible.
print 'Call isdivisible.'
if jsntlib.isdivisible(13, 20):
    print 'The result is 13|20.'
else:
    print 'The result is 13∤20.'

print

#Check if 197 is prime.
print 'Call isprime.'
if jsntlib.isprime(197):
    print '197 is a prime number.'
else:
    print '197 is a composit number.'

print

#Print the GCD of 10 and 24.
print 'Call gcd.'
print '(10,24) = %d' %jsntlib.gcd(10, 24)

print

#Check if 157 and 673 are coprime numbers.
print 'Call coprime.'
if jsntlib.coprime(157, 673):
    print '157 and 673 are coprime.'
else:
    print '157 and 673 are not coprime.'

print

#Print the Bézout Equation with parameters 179 and 367.
print 'Call bezout.'
print '%d*179 + %d*367 = (179,367)' %jsntlib.bezout(179, 367)

print 

#Print the factorisation of -234.
print 'Call factor.'
print '-100 =',
ctr = 0
for prime in jsntlib.factor(-100):
    if ctr > 0:     print '*',
    print prime,
    ctr += 1
print

print

#Print the solutions for N|a^2-b^2 while N∤a+b and N∤a-b.
print 'Call decomposit.'
print 'The solutions for N|a^2-b^2 while N∤a+b and N∤a-b is\n\ta = %d\n\tb = %d' %jsntlib.decomposit(100)

print

#Return the special solutions for indefinite binary equation, 7*x + 24*y = -3.
print 'Call binary.'
print 'The general solutions for \'7*x + 24*y = -3\' is (t∈Z)\n\tx = %d + 24*t\n\ty = %d - 7*t' %jsntlib.binary(7, 24, -3)

print

#Print the result of 235^12235 (mod 9).
print 'Call modulo.'
print '235 ^ 12235 ≡ %d (mod 9)\n' %jsntlib.modulo(235,12235,9)

print

#Return the Euclidean division result of (20140515x^20140515 + 201495x^201405 + 2014x^2014 + 8x^8 + x^6 + 4x^3 + x + 1) / (x^7 - 1).
print 'Call polydiv.'
# dvdExp = [20140515, 201405, 2014, 8, 6, 3, 1, 0]
# dvdCoe = [20140515, 201495, 2014, 8, 1, 4, 1, 1]
dvdExp = [1, 3, 2, 34]
dvdCoe = [-2, 4, 3, 1]
dvsExp = [7,  1]
dvsCoe = [1, -1]

(qttExp, qttCoe, rtoExp, rtoCoe) = jsntlib.polydiv(dvdExp, dvdCoe, dvsExp, dvsCoe)

print '\n\t'
for ptr in range(len(dvdExp)):
    print '%dx^%d' %(dvdCoe[ptr], dvdExp[ptr]),
    if ptr < len(dvdExp) - 1:
        print '+',
print '=\n(',
for ptr in range(len(dvsExp)):
    print '%dx^%d' %(dvsCoe[ptr], dvsExp[ptr]),
    if ptr < len(dvsExp) - 1:
        print '+',
print ') * (',
for ptr in range(len(qttExp)):
    print '%dx^%d' %(qttCoe[ptr], qttExp[ptr]),
    if ptr < len(qttExp) - 1:
        print '+',
print ') +',
for ptr in range(len(rtoExp)):
    print '%dx^%d' %(rtoCoe[ptr], rtoExp[ptr]),
    if ptr < len(rtoExp) - 1:
        print '+',
print

print

#Return the coefficients and exponents of quotient and ratio after congruence simplification of 3x^14 + 4x^13 + 2x^11 + x^9 + x^6 + x^3 + 12x^2 + x ≡ 0 (mod 5).
print 'Call simplify.'
cgcExp = [14, 13, 11,  9,  6,  3,  2,  1]
cgcCoe = [ 3,  4,  2,  1,  1,  1, 12,  1]
modulo = 5

(rtoExp, rtoCoe) = jsntlib.simplify(cgcExp, cgcCoe, modulo)

print 'The original polynomial congruence is\n\t',
for ptr in xrange(len(cgcExp)):
    print '%dx^%d' %(cgcCoe[ptr], cgcExp[ptr]),
    if ptr < len(cgcExp) - 1:
        print '+',
print '≡ 0 (mod %d)' %modulo
print
print 'The simplified polynomial congruence is\n\t',
for ptr in xrange(len(rtoExp)):
    print '%dx^%d' %(rtoCoe[ptr], rtoExp[ptr]),
    if ptr < len(rtoExp) - 1:
        print '+',
print '≡ 0 (mod %d)' %modulo

print

#Return the solutions of a naïve congruence set.
print 'Call crt'

ratio = jsntlib.crt((3, [1,-1]), (5, [1,-1]), (7, [2,-2]))

print 'x ≡ ±1 (mod 3)'
print 'x ≡ ±1 (mod 5)'
print 'x ≡ ±2 (mod 7)'
print 'The solutions of the above equation set is\n\tx ≡',
for rst in ratio:
    print rst,
print '(mod 105)'

print

#Return the solutions of congruence equation x^2 ≡ 46 (mod 105).
print 'Call congsolve'
cgcExp = [2, 0]
cgcCoe = [1, -46]
modulo = 105

for ptr in xrange(len(cgcExp)):
    print '%dx^%d' %(cgcCoe[ptr], cgcExp[ptr]),
    if ptr < len(cgcExp) - 1:
        print '+',
print '≡ 0 (mod %d)' %modulo

ratio = jsntlib.congsolve(cgcExp, cgcCoe, modulo)

print 'The solution of the above polynomial congruence is\n\tx ≡',
for rst in ratio:
    print '%d' %rst,
print '(mod %d)' %modulo

print

#Return the solutions of quadratic equation x^2 + y^2 = 2017.
print 'Call quadratic.'
print 'The solution of the equation x^2 + y^2 = 2017 is\n\tx=±%d, y=±%d' %jsntlib.quadratic(2017)

print

#Return the order of 2 for modulo 9.
print 'Call ord.'
print 'The order of 2 mod 9 is\n\tord_9(2) = %d' %jsntlib.ord(9, 2)

print

#Return the primitive root(s) of modulo 7.
print 'Call root.'
print 'The primtive root(s) of modulo 7 is/are',
for root in jsntlib.root(7):
    print root,
print '.'

print

#Return the primitive residue class of integer 40.
print 'Call prc'
print 'The primitive residue class of 40 is'
for num in jsntlib.prc(40):
    print num,
print '.'

print

#Return Euler function φ(40)
print 'Call euler.'
print 'φ(40) = %d' %jsntlib.euler(40)

print

#Return the result of Legendre symbol for (a | p).
print 'Call legendre.'
print '(3 | 17) = %d' %jsntlib.legendre(3, 17)

print

#Return the result of jocabi symbol for (a | m).
print 'Call jacobi.'
print '(286 | 563) = %d' %jsntlib.jacobi(286, 563)

print

#Return if an integer is a Carmicheal number.
print 'Call carmicheal.'
print '3499',
if jsntlib.carmicheal(3499):
    print 'is',
else:
    print 'isn\'t',
print 'a Carmicheal number'

print

#Return a pseudo-prime number with certain paterns.
print 'Call pseudo.'
print 'A pseudo-prime number with Fermat test (t=100000) is %d.' %pseudoPrime(byte=12, para=100000, mode='Fermat')
print 'An Euler pseudo-prime number with Solovay-Stassen test (t=100000) is %d.' %pseudoPrime(byte=12, para=100000, mode='Euler')
print 'A strong pseudo-prime number with Miller-Rabin test (k=100000) is %d.' %pseudoPrime(byte=12, para=100000, mode='Strong')

print 
