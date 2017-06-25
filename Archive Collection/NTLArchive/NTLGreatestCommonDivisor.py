# -*- coding: utf-8 -*-

__all__  = ['greatestCommonDivisor']
nickname = 'gcd'

#廣義歐幾里德除法
#返回任意兩整數的最大公因數

from .NTLValidations import int_check

def greatestCommonDivisor(a, b):
    int_check(a, b)

    if a < 0:   a = -1 * a      #將a轉為正整數進行計算
    if b < 0:   b = -1 * b      #將b轉為正整數進行計算
    if a < b:   a, b = b, a     #交換a與b的次序，使得a≥b

    while b:
    	a, b = b, a%b			#(a,b) = (r_-2,r_-1) = (r_-1,r_0) = … = (r_n,r_n+1) = (r_n,0) = r_n
    return a

# if __name__ == '__main__':
#     print('(-179,367) = %d' %greatestCommonDivisor(-179, 367))
