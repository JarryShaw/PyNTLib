# -*- coding: utf-8 -*-


# 指數求取
# 計算整數a模m的指數


from .NTLCoprimalityTest import coprimalityTest
from .NTLExceptions      import DefinitionError
from .NTLPolynomial      import Polynomial
from .NTLUtilities       import jsrange
from .NTLValidations     import int_check, prime_check


__all__  = ['order']
nickname =  'ord'


'''Usage sample:

print('The order of 2 mod 9 is\n\tord_9(2) = %d' % ord(9, 2))

'''


def order(m, a):
    if isinstance(m, Polynomial) or isinstance(a, Polynomial):
        m = Polynomial(m);      prime_check(a)

        deg = a**len(m);        a = Polynomial('x')

    else:
        int_check(m, a)

        if not coprimalityTest(a, m):
            raise DefinitionError('The arguments must be coprime.')

        deg = m

    for e in jsrange(deg, 1, -1):
        if a**e % m == 1:
            return e
