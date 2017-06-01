#-*- coding: utf-8 -*-

#Euler函數
#計算整數m的Euler函數

import NTLExceptions
import NTLCoprimalityTest

def eulerFunction(m):
    if not isinstance(m, int) and not isinstance(m, long):
        raise NTLExceptions.IntError('THe argument must be integral.')

    if m <= 0:
        raise NTLExceptions.PNError('The integer must be positive.')

    phi_m = 0
    for num in xrange(1, m+1):
        if (NTLCoprimalityTest.coprimalityTest(num, m)):  phi_m += 1

    return phi_m

if __name__ == '__mian__':
    euler = eulerFunction(40)

    print 'φ(40) = %d' %euler
