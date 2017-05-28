# -*- coding: utf-8 -*-

#模重複平方法
#求解b^n (mod m)的值

import NTLExceptions

def repetiveSquareModulo(base=1, exponent=1, modulo=1):
    if not isinstance(base, int) or not isinstance(exponent, int) or not isinstance(modulo, int):
        raise NTLExceptions.IntError('The arguments must be integral.')

    if exponent < 0:
        raise NTLExceptions.PNError('The exponent must be possitive.')

    if modulo <= 0:
        raise NTLExceptions.PNError('The modulo must be possitive.')

    if base == 0:
        return 0 if (exponent != 0) else 1

    get_bin = lambda x: format(x, 'b')              #二進制轉化函數

    exp_bin = get_bin(exponent)                     #將指數轉為二進制
    ptr = len(exp_bin) - 1

    a = 1           
    b = base        
    n = exp_bin     
    while ptr >= 0:
        a = a * b**int(n[ptr]) % modulo             #a_i ≡ a_i-1 * b_i ^ n_i (mod modulo)
        b = b**2 % modulo                           #b_i ≡ b_i-1 ^ 2 (mod modulo)
        ptr -= 1

    return a if (base > 0) else (-1 * a)            #base ^ exponent ≡ a_k-1 (mod modulo)

if __name__ == '__main__':
    print '-765 ^ 264 ≡ %d (mod 597)\n' %repetiveSquareModulo(-765, 264, 597)
