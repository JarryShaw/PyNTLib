# -*- coding: utf-8 -*-

#廣義歐幾里德除法
#返回100,000內任意兩整數的最大公因數

def maxCommonFactor(a=1, b=1):
    if a < 0:   a = -1 * a              #將a轉為正整數進行計算
    if b < 0:   b = -1 * b              #將b轉為正整數進行計算
    if a < b:   c = a;  a = b;  b = c   #交換a與b的次序，使得a≥b
    if b == 0:  return a                #(r,0) = r
    
    r = a % b
    return maxCommonFactor(r, b)        #(a,b) = (r_-2,r_-1) = (r_-1,r_0) = … = (r_n,r_n+1) = (r_n,0) = r_n

if __name__ == '__main__':
    while True:
        try:
            a = int(raw_input('The first number is '))
            if a > 100000:
                print 'The number must be under 100,000.'
                continue
        except ValueError:
            print 'Invalid input.'
            continue
        break

    while True:
        try:
            b = int(raw_input('The second number is '))
            if b > 100000:
                print 'The number must be under 100,000.'
                continue
        except ValueError:
            print 'Invalid input.'
            continue
        break

    print '(%d,%d) = %d' %(a, b, maxCommonFactor(a, b))
