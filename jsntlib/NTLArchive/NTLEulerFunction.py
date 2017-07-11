# -*- coding: utf-8 -*-


# Euler函數
# 計算整數m的Euler函數


from .NTLCoprimalityTest import coprimalityTest
from .NTLUtilities       import jsrange
from .NTLValidations     import int_check, pos_check


__all__  = ['eulerFunction']
nickname =  'euler'


'''Usage sample:

print('φ(40) = %d' % euler(40))

'''


def eulerFunction(m):
    int_check(m);   pos_check(m)

    phi_m = 0
    for num in jsrange(1, m+1):
        if (coprimalityTest(num, m)):
            phi_m += 1

    return phi_m
