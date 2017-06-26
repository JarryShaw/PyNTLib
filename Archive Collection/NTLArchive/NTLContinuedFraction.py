# -*- coding: utf-8 -*-

__all__  = ['continuedFraction']
nickname = 'fraction'

import fractions
import math

#連分數
#任意分數轉化為簡單連分數

from .NTLUtilities   import jsfloor
from .NTLValidations import real_check, notneg_check

def continuedFraction(numerator, denominator=None):
    if denominator == None:     denominator = 1

    real_check(numerator, denominator); notneg_check(numerator, denominator)

    x = fractions.Fraction(numerator, denominator)
    a = jsfloor(x)
    x -= a
    cf_ = [a]

    while x != 0:
        x = 1 / x
        a = jsfloor(x)
        x -= a
        cf_.append(a)

    if cf_[-1] == 2:    cf_[-1:] = [1, 1]
    return cf_

# if __name__ == '__main__':
#     print('7700/2145 = ', end=' ')
#     rst_ = continuedFraction(7700, 2145)
#     print(rst_)
