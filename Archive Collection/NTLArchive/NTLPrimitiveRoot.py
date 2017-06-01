#-*- coding: utf-8 -*-

#任意數模原根求取
#計算任意數m的原根

import NTLExceptions
import NTLEulerFunction
import NTLCoprimalityTest
import NTLTrivialDivision
import NTLPrimeFactorisation
import NTLRepetiveSquareModulo
import NTLGreatestCommonDivisor
import NTLPrimitiveResidueClass

def primitiveRoot(m):
    if not isinstance(m, int):
        raise NTLExceptions.IntError('The argument must be integral.')

    if m <= 0:
        raise NTLExceptions.PNError('The integer must be positive.')

    if m == 2:          #m = 2
        return [1]
    elif m == 4:        #m = 4
        return [3]
    else:               #m = p^⍺ / 2p^⍺
        (p, q) = NTLPrimeFactorisation.primeFactorisation(m, wrap=True)
        if len(p) == 1:                             #m = p^⍺
            return primePR(p[0]) if q[0] == 1 else exponentPR(p[0], q[0])
        elif len(p) == 2 and q[0] == 1:             #m = 2p^⍺
            return binaryPR(p[1], q[1])
        else:           #No primitive root.
            return []

#奇素數模原根求取
def primePR(prime):
    primitiveRoot = []

    #p-1的所有不同質因數表
    q = NTLPrimeFactorisation.primeFactorisation(prime - 1, wrap=True)[0]

    for g in xrange(1, prime):
        modFlag = 1
        for qitem in q:
            exp = (prime - 1) / qitem
            if NTLRepetiveSquareModulo.repetiveSquareModulo(g, exp, prime)  == 1:
                modFlag = 0;    break
        if modFlag == 1:        break

    prc = NTLPrimitiveResidueClass.primitiveResidueClass(prime-1)
    for num in prc:
        primitiveRoot.append(NTLRepetiveSquareModulo.repetiveSquareModulo(g, num, prime))

    # #由定義求解
    # phi_prime = prime - 1

    # for a in xrange(1, prime):
    #     if coprimalityTest(a, prime):
    #         for e in xrange(1, prime):
    #             if a**e % m == 1:
    #                 if e == phi_prime:
    #                     primitiveRoot.append(a)
    #                 break

    return sorted(primitiveRoot)

#奇素數指數模原根求取
def exponentPR(base, exponent):
    primitiveRoot = []
    prrList = primePR(base)

    for prr in prrList:
        if (prr**(base-1)) % base == 1\
            and NTLGreatestCommonDivisor.greatestCommonDivisor(base, ((prr**(base-1)) // base)) == 1:
            g = prr;        break
        if ((prr+base)**(base-1)) % base == 1\
            and NTLGreatestCommonDivisor.greatestCommonDivisor(base, (((prr+base)**(base-1)) // base)) == 1:
            g = prr+base;   break

    prc = NTLPrimitiveResidueClass.primitiveResidueClass(NTLEulerFunction.eulerFunction(base**2))
    for num in prc:
        primitiveRoot.append(NTLRepetiveSquareModulo.repetiveSquareModulo(g, num, int(base**exponent)))

    return sorted(primitiveRoot)

#二倍奇素數指數模原根求取
def binaryPR(base, exponent):
    primitiveRoot = []
    glist = exponentPR(base, exponent)

    for g in glist:
        if g % 2 == 1:
            primitiveRoot.append(g)

        g_ = g + base ** exponent
        if g_ % 2 == 1:
            primitiveRoot.append(g_)

    return sorted(primitiveRoot)

if __name__ == '__main__':
    a = primitiveRoot(3362)
    print 'The primtive root(s) of modulo 7 is/are',
    for root in a:
        print root,
    print '.'

