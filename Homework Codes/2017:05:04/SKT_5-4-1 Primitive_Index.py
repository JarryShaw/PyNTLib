#-*- coding: utf-8 -*-

#指數求取
#計算整數a模m的指數

def primitiveIndex(m, a):
    if coprimalityTest(a, m):
        for e in xrange(1, m):
            if a**e % m == 1:
                return e
    else:
        raise ValueError('The arguments must be coprime.')

#互素判斷 | 判斷整數a與正整數m是否互素
def coprimalityTest(a=1, m=1):
    if GCD(a, m) == 1:      #互素定義，即(a,m) = 1
        return 1
    else:m
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
            m = int(raw_input('The modulo is m = '))
            if m < 1:
                print 'm must be greater than 1.'
                continue
        except ValueError:
            print 'Invalid input.'
            continue
        break

    while True:
        try:
            a = int(raw_input('The number is a = '))
            if a < 0:
                print 'a must be positive.'
                continue
        except ValueError:
            print 'Invalid input.'
            continue
        break

    e = primitiveIndex(m, a)
    print 'The index of %d mod %d is\n\tmod_%d(%d) = %d' %(a, m, m, a, e)

