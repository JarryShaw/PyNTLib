# -*- coding: utf-8 -*-


# Legendre符號
# 計算Legendre符號（定義求解）


from .NTLRepetiveSquareModulo import repetiveSquareModulo
from .NTLValidations          import bool_check, int_check, prime_check


__all__  = ['legendreSymbol']
nickname =  'legendre'


'''Usage sample:

print('(3 | 17) = %d' % legendre(3, 17))

'''


def legendreSymbol(a, p, **kwargs):
    trust = False
    for kw in kwargs:
        if kw != 'trust':
            raise KeywordError('Keyword \'%s\' is not defined.' % kw)
        else:
            trust = kwargs[kw];     bool_check(trust)

    int_check(a);   prime_check(trust, p)

    a %= p

    if a == 1:      return 1
    if a == p - 1:  return (-1)**((p-1)//2)
    if a == 2:      return (-1)**((p**2-1)//8)

    mod = repetiveSquareModulo(a, ((p-1)//2), p)
    return mod if mod != p-1 else -1
