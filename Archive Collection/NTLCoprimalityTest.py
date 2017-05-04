# -*- coding: utf-8 -*-

#互素判斷
#判斷整數a與整數m是否互素

def coprimalityTest(a=1, b=1):
    if not isinstance(a, int) or not isinstance(b, int):
        raise __import__('NTLExceptions').IntError

    if __import__('NTLGreatestCommonDivisor').greatestCommonDivisor(a, b) == 1:      #互素定義，即(a,b) = 1
        return 1
    else:
        return 0

if __name__ == '__main__':
    if coprimalityTest(53, 19):
        print '53 and 19 are coprime.'
    else:
        print '53 and 19 are not coprime.'
