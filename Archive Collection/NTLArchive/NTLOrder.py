#-*- coding: utf-8 -*-

#指數求取
#計算整數a模m的指數

import NTLExceptions
import NTLCoprimalityTest

def order(m, a):
    if not isinstance(a, int) or not isinstance(m, int):
        raise NTLExceptions.IntError('The arguments must be integral.')

    if not NTLCoprimalityTest.coprimalityTest(a, m):
        raise NTLExceptions.DefinitionError('The arguments must be coprime.')
    
    for e in xrange(1, m):
        if a**e % m == 1:
            return e

if __name__ == '__main__':
    e = order(9, 2)
    print 'The order of 2 mod 9 is\n\tord_9(2) = %d' %e
