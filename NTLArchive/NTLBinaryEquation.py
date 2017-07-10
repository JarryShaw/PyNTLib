# -*- coding: utf-8 -*-


# 求解不定方程
# 求二元一次不定方程的特解


from .NTLBezoutEquation        import bezoutEquation
from .NTLExceptions            import SolutionError
from .NTLGreatestCommonDivisor import greatestCommonDivisor
from .NTLValidations           import int_check


__all__  = ['binaryEquation']
nickname =  'binary'


'''Usage sample:

(x0,y0) = binary(7,24,-3)

print('The general solutions for \'7*x + 24*y = -3\' is (t∈Z)')
print('x = %d + 24*t' % x0)
print('y = %d -  7*t' % y0)

'''


def binaryEquation(a, b, c):
    int_check(a, b, c)

    pn_a = pn_b = pn_c = 1
    if a < 0:   pn_a = -1;   a *= -1
    if b < 0:   pn_b = -1;   b *= -1
    if c < 0:   pn_c = -1;   c *= -1

    gcd = greatestCommonDivisor(a, b)
    if (c % gcd != 0):
        raise SolutionError('The binary equation has no integral solution.')
    else:
        mtp = c // gcd

    (s, t) = bezoutEquation(a, b)
    x0 = s * mtp * pn_a * pn_c
    y0 = t * mtp * pn_b * pn_c

    return x0, y0
