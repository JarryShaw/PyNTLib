#-*- coding: utf-8 -*-

#奇素數模指數求取
#計算整數a模奇素數m的指數

import math

def primeOrdinary(m, a):
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

#平凡除法 | 對100,000內的整數素性判斷
def trivialDivision(N=2):
    if N < 0:   N = -1 * N
    if N == 1 or N == 0:
        raise ValueError('The argument must be a natural number greater than 1.')
    
    set = eratosthenesSieve(N+1)      #得出小於N的所有素數
    if N in set:                    #素性判斷
        return 1                    #N為素數
    return 0                        #N為合數

#厄拉托塞師篩法 | 返回10,000以內正整數的所有素數（默認情況）
def eratosthenesSieve(N):
    set = [1]*(N+1)                 #用於存儲N個正整數的表格／狀態；其中，0表示篩去，1表示保留
    for index in range(2,int(math.sqrt(N))):  #篩法（平凡除法）
        if set[index] == 1:
            ctr = 2
            while index * ctr <= N:
                set[index*ctr] = 0      #將index的倍數篩去
                ctr += 1

    rst = []
    for ptr in range(2,N):          #獲取結果
        if set[ptr] == 1:
            rst.append(ptr)
            ptr += 1

    return rst

if __name__ == '__main__':
    while True:
        try:
            m = int(raw_input('The modulo is m = '))
            if m == 2 or not trivialDivision(m):
                print 'm must be an odd prime number.'
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

    e = primeOrdinary(m, a)
    print 'The ordinary of %d mod %d is\n\tmod_%d(%d) = %d' %e

