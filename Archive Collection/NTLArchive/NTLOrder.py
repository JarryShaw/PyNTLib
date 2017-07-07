# -*- coding: utf-8 -*-


# 指數求取
# 計算整數a模m的指數


from .NTLCoprimalityTest import coprimalityTest
from .NTLExceptions      import DefinitionError
from .NTLUtilities       import jsrange
from .NTLValidations     import int_check


__all__  = ['order']
nickname =  'ord'


'''Usage sample:

print('The order of 2 mod 9 is\n\tord_9(2) = %d' % ord(9, 2))

'''


def order(m, a):
    int_check(m, a)

    if not coprimalityTest(a, m):
        raise DefinitionError('The arguments must be coprime.')

    for e in jsrange(1, m):
        if a**e % m == 1:
            return e
