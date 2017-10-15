# -*- coding: utf-8 -*-


# 同餘式簡化
# 素數模的同餘式的簡化


from .NTLExceptions                  import KeywordError
from .NTLPolynomialEuclideanDivision import polyED
from .NTLValidations                 import bool_check, list_check, prime_check


__all__  = ['congruenceSimplification']
nickname =  'simplify'


'''Usage sample:

cgcExp = [14, 13, 11,  9,  6,  3,  2,  1]
cgcCoe = [ 3,  4,  2,  1,  1,  1, 12,  1]
modulo = 5

(remExp, remCoe) = simplify(cgcExp, cgcCoe, modulo)

print('The original polynomial congruence is\n\t', end=' ')
for ptr in range(len(cgcExp)):
    print('%dx^%d' % (cgcCoe[ptr], cgcExp[ptr]), end=' ')
    if ptr < len(cgcExp) - 1:
        print('+', end=' ')
print('≡ 0 (mod %d)' % modulo)
print()
print('The simplified polynomial congruence is\n\t', end=' ')
for ptr in range(len(remExp)):
    print('%dx^%d' % (remCoe[ptr], remExp[ptr]), end=' ')
    if ptr < len(remExp) - 1:
        print('+', end=' ')
print('≡ 0 (mod %d)' % modulo)

'''


def congruenceSimplification(cgcExp, cgcCoe, modulo, **kwargs):
    trust = False
    for kw in kwargs:
        if kw != 'trust':
            raise KeywordError('Keyword \'%s\' is not defined.' % kw)
        else:
            trust = kwargs[kw];     bool_check(trust)
            
    list_check(cgcExp, cgcCoe);     prime_check(trust, modulo)

    dvsExp = [modulo, 1]
    dvsCoe = [1, -1]
    (qttExp, qttCoe, rtoExp, rtoCoe) = polyED(cgcExp, cgcCoe, dvsExp, dvsCoe)

    return rtoExp, rtoCoe
