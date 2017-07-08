# -*- coding: utf-8 -*-


# 任意數模原根求取
# 計算任意數m的原根


from .NTLCoprimalityTest       import coprimalityTest
from .NTLEulerFunction         import eulerFunction
from .NTLExceptions            import SolutionError
from .NTLGreatestCommonDivisor import greatestCommonDivisor
from .NTLPrimeFactorisation    import primeFactorisation
from .NTLPrimitiveResidueClass import primitiveResidueClass
from .NTLRepetiveSquareModulo  import repetiveSquareModulo
from .NTLUtilities             import jsrange
from .NTLValidations           import int_check, pos_check


__all__  = ['primitiveRoot',
            'primePR', 'exponentPR', 'binaryPR']
nickname =  'root'


'''Usage sample:

a = root(7)
print('The primtive root(s) of modulo 7 is/are', end=' ')
for root in a:
    print(root, end=' ')
print('.')

'''


def primitiveRoot(m):
    int_check(m);   pos_check(m)

    if m == 2:          # m = 2
        return [1]
    elif m == 4:        # m = 4
        return [3]
    else:               # m = p^⍺ / 2p^⍺
        (p, q) = primeFactorisation(m, wrap=True)
        if len(p) == 1:                             # m = p^⍺
            return primePR(p[0]) if q[0] == 1 else exponentPR(p[0], q[0])
        elif len(p) == 2 and q[0] == 1:             # m = 2p^⍺
            return binaryPR(p[1], q[1])
        else:                                       # No primitive root.
            raise SolutionError('%d has no primitive root.' % m)


# 奇素數模原根求取
def primePR(prime):
    primitiveRoot = []

    # p-1的所有不同質因數表
    q = primeFactorisation(prime - 1, wrap=True)[0]

    for g in jsrange(1, prime):
        for qitem in q:
            exp = (prime - 1) // qitem
            if repetiveSquareModulo(g, exp, prime)  == 1:   break
        else:   break

    prc = primitiveResidueClass(prime-1)
    for num in prc:
        primitiveRoot.append(repetiveSquareModulo(g, num, prime))

    '''Deprecated:

    # 由定義求解
    phi_prime = prime - 1

    for a in jsrange(1, prime):
        if coprimalityTest(a, prime):
            for e in jsrange(1, prime):
                if a**e % m == 1:
                    if e == phi_prime:
                        primitiveRoot.append(a)
                    break
    '''

    return sorted(primitiveRoot)


# 奇素數指數模原根求取
def exponentPR(base, exponent):
    primitiveRoot = []
    prrList = primePR(base)

    for prr in prrList:
        if (prr**(base-1)) % base == 1 \
                and greatestCommonDivisor(base, ((prr**(base-1)) // base)) == 1:
            g = prr;        break
        if ((prr+base)**(base-1)) % base == 1 \
                and greatestCommonDivisor(base, (((prr+base)**(base-1)) // base)) == 1:
            g = prr+base;   break

    prc = primitiveResidueClass(eulerFunction(base**2))
    for num in prc:
        primitiveRoot.append(repetiveSquareModulo(g, num, base**exponent))

    return sorted(primitiveRoot)


# 二倍奇素數指數模原根求取
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
