#-*- coding: utf-8 -*-

__all__  = ['jacobiSymbol']
nickname = 'jacobi'

import math

#Jacobi符號
#計算Jacobi符號（定義求解）

'''
TODO:

* Creat a Jacobi class to further tasks, like simplification.
'''

from .NTLCoprimalityTest    import coprimalityTest
from .NTLLegendreSymbol     import legendreSymbol
from .NTLPrimeFactorisation import primeFactorisation
from .NTLUtilities          import jsrange, jssquare
from .NTLValidations        import int_check, pos_check

def jacobiSymbol(a, m):
    int_check(a, m);    pos_check(m)

    a %= m

    if a == 1:      return 1
    if a == m - 1:  return (-1)**((m-1)//2)
    if a == 2:      return (-1)**((m**2-1)//8)
    if coprimalityTest(a, m) and jssquare(a):   return 1

    (p, q) = primeFactorisation(m, wrap=True)

    rst = 1
    for ptr in jsrange(len(p)):
        rst *= legendreSymbol(a, p[ptr]) ** q[ptr]

    return rst

# if __name__ == '__main__':
#     print('(286 | 563) = %d' %jacobiSymbol(286, 563))
