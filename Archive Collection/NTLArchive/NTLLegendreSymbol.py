#-*- coding: utf-8 -*-

#Legendre符號
#計算Legendre符號（定義求解）

'''
TODO:

* Creat a Legendre class to further tasks, like simplification.
'''

import NTLExceptions
import NTLTrivialDivision
import NTLRepetiveSquareModulo

def legendreSymbol(a, p):
    if (not isinstance(a, int) and not isinstance(a, long))\
    or (not isinstance(p, int) and not isinstance(p, long)):
        raise NTLExceptions.IntError('The arguments must be integral.')

    if not NTLTrivialDivision.trivialDivision(p):
        raise NTLExceptions.PNError('The denominator argument must be a prime number.')

    a %= p

    if a == 1:      return 1
    if a == -1:     return (-1)**((p-1)/2)
    if a == 2:      return (-1)**((p**2-1)/8)

    mod = NTLRepetiveSquareModulo.repetiveSquareModulo(a, ((p-1)/2), p)
    return mod if mod != p-1 else -1

if __name__ == '__main__':
    print '(3 | 17) = %d' %legendreSymbol(3, 17)
