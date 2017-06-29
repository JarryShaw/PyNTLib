# -*- coding: utf-8 -*-

__all__  = ['leastCommonMultiple']
nickname =  'lcm'

#最小公倍數
#返回任意兩整數的最小公倍數

from .NTLGreatestCommonDivisor import greatestCommonDivisor
from .NTLValidations           import int_check

def leastCommonMultiple(a, b):
    int_check(a, b)

    if a < 0:   a = -1 * a      #將a轉為正整數進行計算
    if b < 0:   b = -1 * b      #將b轉為正整數進行計算

    return (a * b) // greatestCommonDivisor(a, b)   #[a,b] = a*b / (a,b)

# if __name__ == '__main__':
#     print('(-179,367) = %d' %leastCommonMultiple(-179, 367))
