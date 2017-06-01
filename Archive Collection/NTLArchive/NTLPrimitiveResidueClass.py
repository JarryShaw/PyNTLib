#-*- coding: utf-8 -*-

#簡化剩餘係
#求整數m的簡化剩餘係

import NTLExceptions
import NTLCoprimalityTest

def primitiveResidueClass(n):
    if not isinstance(n, int) and not isinstance(n, long):
        raise NTLExceptions.IntError('THe argument must be integral.')

    if n <= 0:
        raise NTLExceptions.PNError('The integer must be positive.')

    #當(d,n)=1時，d遍歷n的簡化剩餘係
    rst = []
    for d in xrange(1, n):
        if NTLCoprimalityTest.coprimalityTest(d, n) == 1:
            rst.append(d)

    return rst

if __name__ == '__mian__':
    prc = primitiveResidueClass(40)

    print 'The primitive residue class of 40 is'
    for num in prc:
        print num,
