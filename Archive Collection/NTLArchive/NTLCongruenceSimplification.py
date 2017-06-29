# -*- coding: utf-8 -*-

__all__  = ['congruenceSimplification']
nickname =  'simplify'

#同餘式簡化
#素數模的同餘式的簡化

from .NTLPolynomialEuclideanDivision import polyED
from .NTLValidations                 import int_check, list_check, pos_check, prime_check

def congruenceSimplification(cgcExp, cgcCoe, modulo):
    list_check(cgcExp, cgcCoe);
    int_check(modulo);  pos_check(modulo);  prime_check(modulo)

    dvsExp = [modulo, 1]
    dvsCoe = [1, -1]
    (qttExp, qttCoe, rtoExp, rtoCoe) = polyED(cgcExp, cgcCoe, dvsExp, dvsCoe)

    return rtoExp, rtoCoe

# if __name__ == '__main__':
#     cgcExp = [14, 13, 11,  9,  6,  3,  2,  1]
#     cgcCoe = [ 3,  4,  2,  1,  1,  1, 12,  1]
#     modulo = 5

#     (rtoExp, rtoCoe) = congruenceSimplification(cgcExp, cgcCoe, modulo)

#     print('The original polynomial congruence is\n\t', end=' ')
#     for ptr in range(len(cgcExp)):
#         print('%dx^%d' %(cgcCoe[ptr], cgcExp[ptr]), end=' ')
#         if ptr < len(cgcExp) - 1:
#             print('+', end=' ')
#     print('≡ 0 (mod %d)' %modulo)
#     print()
#     print('The simplified polynomial congruence is\n\t', end=' ')
#     for ptr in range(len(rtoExp)):
#         print('%dx^%d' %(rtoCoe[ptr], rtoExp[ptr]), end=' ')
#         if ptr < len(rtoExp) - 1:
#             print('+', end=' ')
#     print('≡ 0 (mod %d)' %modulo)
