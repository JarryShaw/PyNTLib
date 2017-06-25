#-*- coding: utf-8 -*-

__all__  = ['legendreSymbol']
nickname = 'legendre'

#Legendre符號
#計算Legendre符號（定義求解）

'''
TODO:

* Creat a Legendre class to further tasks, like simplification.
'''

from .NTLRepetiveSquareModulo import repetiveSquareModulo
from .NTLValidations          import int_check, prime_check

def legendreSymbol(a, p):
    int_check(a, p);    prime_check(p)

    a %= p

    if a == 1:      return 1
    if a == p - 1:  return (-1)**((p-1)//2)
    if a == 2:      return (-1)**((p**2-1)//8)

    mod = repetiveSquareModulo(a, ((p-1)//2), p)
    return mod if mod != p-1 else -1

# if __name__ == '__main__':
#     print('(3 | 17) = %d' %legendreSymbol(3, 17))
