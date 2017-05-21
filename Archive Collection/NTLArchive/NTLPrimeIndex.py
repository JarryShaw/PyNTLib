#-*- coding: utf-8 -*-

#奇素數模指數求取
#計算整數a模奇素數m的指數

import NTLExceptions
import NTLCoprimalityTest
import NTLTrivialDivision

def primeIndex(m, a):
    if not isinstance(a, int) or not isinstance(m, int):
        raise NTLExceptions.IntError('The arguments must be integral.')

    if not NTLTrivialDivision.trivialDivision(m):
        raise NTLExceptions.PCError('The argument must be prime.')

    if not NTLCoprimalityTest.coprimalityTest(a, m):
        raise NTLExceptions.DefinitionError('The arguments must be coprime.')

    for e in xrange(1, m):
        if a**e % m == 1:
            return e
            
if __name__ == '__main__':
    e = primeIndex(17, 5)
    print 'The index of 5 mod 17 is\n\tmod_17(5) = %d' %e

