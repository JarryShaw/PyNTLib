# -*- coding: utf-8 -*-

#互素判斷
#判斷整數a與正整數m是否互素

def coprimalityTest(a=1, m=1):
    if GCD(a, m) == 1:      #互素定義，即(a,m) = 1
        return 1
    else:
        return 0

#廣義歐幾里德除法 | 返回100,000內任意兩整數的最大公因數
def GCD(a=1, b=1):
    if a < 0:   a = -1 * a              #將a轉為正整數進行計算
    if b < 0:   b = -1 * b              #將b轉為正整數進行計算
    if a < b:   c = a;  a = b;  b = c   #交換a與b的次序，使得a≥b
    if b == 0:  return a                #(r,0) = r
    
    r = a % b
    return GCD(r, b)        #(a,b) = (r_-2,r_-1) = (r_-1,r_0) = … = (r_n,r_n+1) = (r_n,0) = r_n

if __name__ == '__main__':
    while True:
        try:
            a = int(raw_input('The integer is '))
        except ValueError:
            print 'Invalid input.'
            continue
        break
    
    while True:
        try:
            m = int(raw_input('The positive integer is '))
            if m <= 0:
                print 'The number must be positive.'
                continue
        except ValueError:
            print 'Invalid input.'
            continue
        break

    if coprimalityTest(a, m):
        print '%d and %d are coprime.' %(a, m)
    else:
        print '%d and %d are not coprime.' %(a, m)
