# -*- coding: utf-8 -*-

#同餘式簡化
#素數模的同餘式的簡化

def congruenceSimplification(cgcExp, cgcCoe, modulo):
    if not isinstance(modulo, int):
        raise __import__('NTLExceptions').IntError

    if not isinstance(cgcExp, list) or not isinstance(cgcCoe, list):
        raise __import__('NTLExceptions').ListError
    
    if modulo < 1:
        raise __import__('NTLExceptions').PNError

    if not __import__('NTLTrivialDivision').trivialDivision(modulo):
        raise __import__('NTLExceptions').PrimeError

    dvsExp = [modulo, 1]
    dvsCoe = [1, -1]
    (qttExp, qttCoe, rtoExp, rtoCoe) = __import__('NTLPolynomialEuclideanDivision').polyED(cgcExp, cgcCoe, dvsExp, dvsCoe)

    return rtoExp, rtoCoe

if __name__ == '__main__':
    #'''
    cgcExp = [14, 13, 11,  9,  6,  3,  2,  1]
    cgcCoe = [ 3,  4,  2,  1,  1,  1, 12,  1]
    modulo = 5
    #'''

    (rtoExp, rtoCoe) = congruenceSimplification(cgcExp, cgcCoe, modulo)

    print 'The original polynomial congruence is\n\t',
    for ptr in xrange(len(cgcExp)):
        print '%dx^%d' %(cgcCoe[ptr], cgcExp[ptr]),
        if ptr < len(cgcExp) - 1:
            print '+',
    print '≡ 0 (mod %d)' %modulo
    print
    print 'The simplified polynomial congruence is\n\t',
    for ptr in xrange(len(rtoExp)):
        print '%dx^%d' %(rtoCoe[ptr], rtoExp[ptr]),
        if ptr < len(rtoExp) - 1:
            print '+',
    print '≡ 0 (mod %d)' %modulo
