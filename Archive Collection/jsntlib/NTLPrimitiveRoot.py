#-*- coding: utf-8 -*-

#奇素數模原根求取
#計算奇素數m的原根

import NTLExceptions
import NTLCoprimalityTest
import NTLTrivialDivision

def primitiveRoot(m):
    if not isinstance(m, int):
        raise NTLExceptions.IntError('The argument must be integral.')

    if not NTLTrivialDivision.trivialDivision(m):
        raise NTLExceptions.PCError('The argument must be prime.')

    phi_m = m - 1
    primtiveRoot = []

    for a in xrange(1, m):
        if NTLCoprimalityTest.coprimalityTest(a, m):
            for e in xrange(1, m):
                if a**e % m == 1:
                    if e == phi_m:
                        primtiveRoot.append(a)
                    break

    return primtiveRoot

if __name__ == '__main__':
    a = primitiveRoot(7)
    print 'The primtive root(s) of modulo 7 is/are',
    for root in a:
        print root,
    print '.'

