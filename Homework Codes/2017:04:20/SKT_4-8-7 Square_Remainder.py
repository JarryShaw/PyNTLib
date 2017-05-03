# -*- coding: utf-8 -*-

#二次同餘式與平方剩餘
#求解方程x^2+y^2=p，其中p為素數

import math

def squareRemainder(p):
    if p == 2 or trivialDivision(p) == 0:           #p為奇素數
        print "The number p must be prime."
        raise ValueError

    if p % 8 != 5:                                  #p = 8k + 5
        print "This equation has no solution."
        raise ValueError

    #若p=8k+5為素數，有2為模p平方非剩餘，則同餘式x^2≡-1(mod p)的解為x=±2^((p-1)/4)(mod p)
    x = (2**((p-1)/4)) % p                          #令x_0 = 2^((p-1)/4)(mod p)
    y = 1                                           #令y_0 = 1
    m = (x**2 + y**2) / p                           #由x_0^2 + y_0^2 = m_0 * p得m_0
    '''
    print 'x0 = ', x
    print 'y0 = ', y
    print 'm0 = ', m
    print
    '''
    while m != 1:                                   #在x_i^2 + y_i^2 = p即m_0 = 1之後，退出循環
        tmp_x = x                                   #寄存當前的x_i-1
        u = x % m if (x%m - m != -1) else -1        #令u_i-1 ≡ x_i-1 (mod m_i-1)
        v = y % m if (y%m - m != -1) else -1        #令v_i-1 ≡ y_i-1 (mod m_i-1)
        x = (u*x + v*y) / m                         #則x_i = (u_i-1 * x_i-1 + v_i-1 * y_i-1) / m_i-1
        y = (u*y - v*tmp_x) / m                     #則y_i = (u_i-1 * y_i-1 - v_i-1 * x_i-1) / m_i-1
        m = (x**2 + y**2) / p                       #由x_i^2 + y_i^2 = m_i * p得m_i
        '''
        print 'u = ', u
        print 'v = ', v
        print 'x = ', x
        print 'y = ', y
        print 'm = ', m
        print
        '''
    make_positive = lambda x : (-1 * x) if (x < 0) else x
    return sorted([make_positive(x), make_positive(y)])
    #return x, y

#平凡除法 | 對100,000內的整數素性判斷
def trivialDivision(N=2):
    if N < 0:   N = -1 * N
    if N == 1 or N == 0:    raise ValueError
    
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
    #'''
    while True:
        try:
            p = int(raw_input('The coefficient is p = '))
        except ValueError:
            print 'Invalid input.'
            continue
        break
    #'''
    #p = 1069
    print
    print 'x^2 + y^2 = %d' %p

    (x,y) = squareRemainder(p)

    print 'The solution of the above equation is x=±%d, y=±%d' %(x, y)
