#-*- coding: utf-8 -*-

#Jacobi符號
#計算Jacobi符號（定義求解）

'''
TODO:

* Creat a Jacobi class to further tasks, like simplification.
'''

import NTLExceptions
import NTLLegendreSymbol
import NTLCoprimalityTest
import NTLPrimeFactorisation

def jacobiSymbol(a, m):
    if (not isinstance(a, int) and not isinstance(a, long))\
    or (not isinstance(m, int) and not isinstance(m, long)):
        raise NTLExceptions.IntError('The arguments must be integral.')

    if m <= 0:
        raise NTLExceptions.PNError('The denominator argument must be positive.')

    a %= m

    if a == 1:      return 1
    if a == -1:     return (-1)**((m-1)/2)
    if a == 2:      return (-1)**((m**2-1)/8)
    if NTLCoprimalityTest.coprimalityTest(a, m) and issquare(a):   return 1

    (p, q) = NTLPrimeFactorisation.primeFactorisation(m, wrap=True)

    rst = 1
    for ptr in range(len(p)):
        rst *= NTLLegendreSymbol.legendreSymbol(a, p[ptr]) ** q[ptr]

    return rst

#判斷整數是否為平方數
def issquare(a):
    return True if int(__import__('math').sqrt(a))**2 == a else False

if __name__ == '__main__':
    print '(286 | 563) = %d' %jacobiSymbol(286, 563)
