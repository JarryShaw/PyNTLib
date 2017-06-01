#-*- coding: utf-8 -*-

#Carmicheal數檢驗
#判斷奇整數n是否為Carmicheal數，即使得Fermat素性檢驗無效的數

import NTLExceptions
import NTLPrimeFactorisation

def carmichealTest(n):
    if not isinstance(n, int) and not isinstance(n, long):
        raise NTLExceptions.IntError('The argument must be integral.')

    if n <= 0:
        raise NTLExceptions.PNError('The argument must be positive.')

    if n % 2 != 1:
        raise NTLExceptions.OEError('THe argument must be odd.')

    (p, q) = NTLPrimeFactorisation.primeFactorisation(n, wrap=True)[:2]

    if len(p) < 3:                  return False

    for qitem in q:
        if qitem > 1:               return False

    for pitem in p:
        if (n-1) % (pitem-1) != 0:  return False

    return True

if __name__ == '__main__':
    print '3499',
    if carmichealTest(3499):
        print 'is',
    else:
        print 'isn\'t',
    print 'a Carmicheal number'
