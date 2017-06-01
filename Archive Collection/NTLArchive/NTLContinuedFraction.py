# -*- coding: utf-8 -*-

#連分數
#任意分數轉化為簡單連分數，並求其漸進分數

import NTLExceptions

def continuedFraction(x):
    if not numbercheck(x) and not isinstance(x, __import__('fractions').Fraction):
        raise NTLExceptions.DigitError('The argument must be a number.')

    if x < 0:
        raise NTLExceptions.PNError('THe argument must be positive.')

    x = __import__('fractions').Fraction(x)
    a = __import__('fractions').Fraction(str(__import__('math').floor(x)))
    x -= a

    cf_ = [int(a)]
    # fp_ = [x]

    while x >= 1e-12:
        x = 1 / x
        a = __import__('fractions').Fraction(str(__import__('math').floor(x)))
        x -= a

        cf_.append(int(a))
        # fp_.append(x)

    # return cf_, fp_
    if cf_[-1] == 2:
        cf_[-1:] = [1, 1]
    return cf_

#數字參數檢查（整型、浮點、長整、複數）
def numbercheck(*args):
    for var in args:
        if not (isinstance(var, int) or isinstance(var, long)\
           or isinstance(var, float) or isinstance(var, complex)):
            return False
    return True

if __name__ == '__main__':
    fct_ = __import__('fractions').Fraction(7700, 2145)
    rst_ = continuedFraction(fct_)
    print fct_, '=', rst_
    # print rst_[0]
    # print rst_[1]
