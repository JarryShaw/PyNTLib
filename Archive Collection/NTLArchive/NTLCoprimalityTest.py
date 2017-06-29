# -*- coding: utf-8 -*-

__all__  = ['coprimalityTest']
nickname =  'coprime'

#互素判斷
#判斷整數a與整數m是否互素

from .NTLGreatestCommonDivisor import greatestCommonDivisor
from .NTLValidations           import int_check

def coprimalityTest(a, b):
    int_check(a, b)

    return 1 if greatestCommonDivisor(a, b) == 1 else 0     #互素定義，即(a,b) = 1

# if __name__ == '__main__':
#     if coprimalityTest(53, 19):
#         print('53 and 19 are coprime.')
#     else:
#         print('53 and 19 are not coprime.')
