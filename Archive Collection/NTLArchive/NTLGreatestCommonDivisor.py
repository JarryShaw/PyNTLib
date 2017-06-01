# -*- coding: utf-8 -*-

#廣義歐幾里德除法
#返回任意兩整數的最大公因數

import NTLExceptions

def greatestCommonDivisor(a=1, b=1):
    if (not isinstance(a, int) and not isinstance(a, long))\
    or (not isinstance(b, int) and not isinstance(b, long)):
        raise NTLExceptions.IntError('The arguments must be integral.')

    if a < 0:   a = -1 * a      #將a轉為正整數進行計算
    if b < 0:   b = -1 * b      #將b轉為正整數進行計算

    return GCDLoop(a, b)

def GCDLoop(a, b):
    if a < b:   a, b = b, a             #交換a與b的次序，使得a≥b
    if b == 0:  return a                #(r,0) = r
    
    r = a % b
    return GCDLoop(r, b)                #(a,b) = (r_-2,r_-1) = (r_-1,r_0) = … = (r_n,r_n+1) = (r_n,0) = r_n

if __name__ == '__main__':
    print '(-179,367) = %d' %greatestCommonDivisor(-179, 367)