#-*- coding: utf-8 -*-

__all__  = ['order']
nickname = 'ord'

#指數求取
#計算整數a模m的指數

from .NTLCoprimalityTest import coprimalityTest
from .NTLUtilities   	 import jsrange
from .NTLValidations 	 import int_check

def order(m, a):
    int_check(m, a)

    if not coprimalityTest(a, m):
        raise NTLExceptions.DefinitionError('The arguments must be coprime.')
    
    for e in jsrange(1, m):
        if a**e % m == 1:
            return e

# if __name__ == '__main__':
#     e = order(9, 2)
#     print('The order of 2 mod 9 is\n\tord_9(2) = %d' %e)
