# -*- coding: utf-8 -*-


#二次同餘式與平方剩餘
#求解方程x^2+y^2=p，其中p為素數


from .NTLExceptions           import SolutionError
from .NTLPolynomialCongruence import polynomialCongruence
from .NTLValidations          import bool_check, prime_check


__all__  = ['quadraticEquation(']
nickname =  'quadratic'


'''Usage sample:

(x,y) = quadratic(2017)
print('The solution of the equation x^2 + y^2 = 2017 is\n\tx=±%d, y=±%d' % (x, y))

'''


def quadraticEquation(p, **kwargs):
    trust = False
    for kw in kwargs:
        if kw != 'trust':
            raise KeywordError('Keyword \'%s\' is not defined.' % kw)
        else:
            trust = kwargs[kw];     bool_check(trust)

    prime_check(trust, p)

    if p % 4 != 1:
        raise SolutionError('The quadratic equation has no integral solution.')

    # 若p=8k+5為素數，有2為模p平方非剩餘，則同餘式x^2≡-1(mod p)的解為x=±2^((p-1)/4)(mod p)
    if p % 8 == 5:
        # 令x_0 = 2^((p-1)/4)(mod p)
        x = (2**((p-1)/4)) % p

    # 反之，用同餘式求解函數求出結果
    else:
        # 令x_0為x^2≡-1(mod p)的正解
        x = polynomialCongruence([2,0], [1,1], p)[0]   
    
    y = 1                                       # 令y_0 = 1
    m = (x**2 + y**2) // p                      # 由x_0^2 + y_0^2 = m_0 * p得m_0

    while m != 1:                               # 在x_i^2 + y_i^2 = p即m_0 = 1之後，退出循環
        tmp_x = x                               # 寄存當前的x_i-1
        u = x % m if (x%m - m != -1) else -1    # 令u_i-1 ≡ x_i-1 (mod m_i-1)
        v = y % m if (y%m - m != -1) else -1    # 令v_i-1 ≡ y_i-1 (mod m_i-1)
        x = (u*x + v*y) // m                    # 則x_i = (u_i-1 * x_i-1 + v_i-1 * y_i-1) / m_i-1
        y = (u*y - v*tmp_x) // m                # 則y_i = (u_i-1 * y_i-1 - v_i-1 * x_i-1) / m_i-1
        m = (x**2 + y**2) // p                  # 由x_i^2 + y_i^2 = m_i * p，得m_i

    x *= -1 if x < 0 else 1
    y *= -1 if y < 0 else 1
    if x > y:   x, y = y, x
    return x, y
