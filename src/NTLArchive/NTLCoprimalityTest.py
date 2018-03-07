# -*- coding: utf-8 -*-


# 互素判斷
# 判斷整數a與整數m是否互素


from .NTLGreatestCommonDivisor import greatestCommonDivisor
from .NTLValidations           import int_check


__all__  = ['coprimalityTest']
nickname =  'coprime'


'''Usage sample:

if coprime(53, 19):
    print('53 and 19 are coprime.')
else:
    print('53 and 19 are not coprime.')

'''


def coprimalityTest(a, b):
    int_check(a, b)

    # 互素定義，即(a,b) = 1
    return True if greatestCommonDivisor(a, b) == 1 else False
