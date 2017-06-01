#-*- coding: utf-8 -*-

#素性檢驗
#用素性檢驗生成偽素數

import NTLExceptions
import NTLJacobiSymbol
import NTLCarmichealTest
import NTLRepetiveSquareModulo

def pseudoPrime(**kwargs):
    mode = 0
    byte = 12
    para = 100000

    for kw in kwargs:
        if kw == 'mode':
            if not isinstance(kwargs[kw], str):
                raise NTLExceptions.StringError('Mode must be a string.')

            if kwargs[kw] == 'Fermat':                          mode = 0
            elif kwargs[kw] == 'Euler' or 'Solovay-Stassen':    mode = 1
            elif kwargs[kw] == 'Strong' or 'Miller-Rabin':      mode = 2
            else:
                raise NTLExceptions.DefinitionError('Mode \'%s\' is not defined.' %kwargs[kw])
        
        elif kw == 'byte':
            if not isinstance(kwargs[kw], int) and not isinstance(kwargs[kw], long):
                raise NTLExceptions.IntError('The byte of result must be integral.')

            if kwargs[kw] <= 0:
                raise NTLExceptions.PNError('The byte of result must be positive.')

            byte = kwargs[kw]

        elif kw == 'para':
            if not isinstance(kwargs[kw], int) and not isinstance(kwargs[kw], long):
                raise NTLExceptions.IntError('The safety parameter must be integral.')

            if kwargs[kw] <= 0:
                raise NTLExceptions.PNError('The safety parameter must be positive.')

            para = kwargs[kw]

        else:
            raise NTLExceptions.KeywordError('Keyword \'%s\' is not defined.' %kw)

    test = {0: lambda num_: fermatTest(num_, para),
            1: lambda num_: solovay_stassenTest(num_, para),
            2: lambda num_: miller_rabinTest(num_, para)}

    lower = 2 ** (byte-1)
    upper = 2 ** byte

    while True:
        num_ = __import__('random').randrange(lower, upper)
        if num_ % 2 != 1:       continue
        if test[mode](num_):    return num_

#Fermat素性檢驗得到Fermat偽素數
def fermatTest(n, t):
    if NTLCarmichealTest.carmichealTest(n):     return False

    for ctr in range(0, t):
        b = __import__('random').randrange(2, n-1)
        if NTLRepetiveSquareModulo.repetiveSquareModulo(b, (n-1), n) != 1:
            return False
    return True

#Solovay-Stassen素性檢驗得到Euler偽素數
def solovay_stassenTest(n, t):
    exp = (n - 1) / 2
    for ctr in range(0, t):
        b = __import__('random').randrange(2, n-1)
        r = NTLRepetiveSquareModulo.repetiveSquareModulo(b, exp, n)
        if r == n - 1:                                  r = -1
        if r != 1 and r != -1:                          return False
        if r != NTLJacobiSymbol.jacobiSymbol(b, n):     return False
    return True

#Miller-Rabin素性檢驗生成強偽素數
def miller_rabinTest(n, k):
    s = 0;  t = n - 1
    while t % 2 == 0:
        s += 1
        t /= 2

    for ctr_1 in range(0, k):
        b = __import__('random').randrange(2, n-1)
        r = NTLRepetiveSquareModulo.repetiveSquareModulo(b, t, n)
        if r == 1 or r == n-1:  continue

        for ctr_2 in range(0, s):
            r = NTLRepetiveSquareModulo.repetiveSquareModulo(r, 2, n)
            if r == n - 1:      break
        return False
    return True

if __name__ == '__main__':
    print 'A pseudo-prime number with Fermat test (t=100000) is %d.' %pseudoPrime(mode='Fermat')
    print 'An Euler pseudo-prime number with Solovay-Stassen test (t=100000) is %d.' %pseudoPrime(mode='Euler')
    print 'A strong pseudo-prime number with Miller-Rabin test (k=100000) is %d.' %pseudoPrime(mode='Strong')
