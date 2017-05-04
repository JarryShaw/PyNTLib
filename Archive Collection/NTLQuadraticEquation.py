# -*- coding: utf-8 -*-

#二次同餘式與平方剩餘
#求解方程x^2+y^2=p，其中p為素數

def quadraticEquation(p):
    if p == 2 or __import__('NTLTrivialDivision').trivialDivision(p) == 0:
        raise __import__('NTLExceptions').PrimeError

    if p % 4 != 1:
        raise __import__('NTLExceptions').SolutionError

    if p % 8 == 5:      #若p=8k+5為素數，有2為模p平方非剩餘，則同餘式x^2≡-1(mod p)的解為x=±2^((p-1)/4)(mod p)
        #令x_0 = 2^((p-1)/4)(mod p)
        x = (2**((p-1)/4)) % p                          
    else:               #反之，用同餘式求解函數求出結果
        #令x_0為x^2≡-1(mod p)的正解
        x = __import__('NTLLinearCongruence').linearCongruence([2,0], [1,1], 2017)[0]   
    
    y = 1                                               #令y_0 = 1
    m = (x**2 + y**2) / p                               #由x_0^2 + y_0^2 = m_0 * p得m_0

    while m != 1:                                       #在x_i^2 + y_i^2 = p即m_0 = 1之後，退出循環
        tmp_x = x                                       #寄存當前的x_i-1
        u = x % m if (x%m - m != -1) else -1            #令u_i-1 ≡ x_i-1 (mod m_i-1)
        v = y % m if (y%m - m != -1) else -1            #令v_i-1 ≡ y_i-1 (mod m_i-1)
        x = (u*x + v*y) / m                             #則x_i = (u_i-1 * x_i-1 + v_i-1 * y_i-1) / m_i-1
        y = (u*y - v*tmp_x) / m                         #則y_i = (u_i-1 * y_i-1 - v_i-1 * x_i-1) / m_i-1
        m = (x**2 + y**2) / p                           #由x_i^2 + y_i^2 = m_i * p得m_i

    make_positive = lambda x : (-1 * x) if (x < 0) else x
    return tuple(sorted([make_positive(x), make_positive(y)]))

if __name__ == '__main__':
    (x,y) = quadraticEquation(2017)

    print 'The solution of the equation x^2 + y^2 = 2017 is\n\tx=±%d, y=±%d' %(x, y)
