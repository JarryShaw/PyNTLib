# -*- coding: utf-8 -*-

#模重複平方法
#求解b^n (mod m)的值

import NTLExceptions

def repetiveSquareModulo(base, exponent, divisor):
    if not isinstance(base, int) or not isinstance(exponent, int) or not isinstance(divisor, int):
        raise NTLExceptions.IntError('The arguments must be integral.')

    get_bin = lambda x: format(x, 'b')  #二進制轉化函數

    exp_bin = get_bin(exponent)         #將指數轉為二進制
    ptr = len(exp_bin) - 1

    a = 1           
    b = base        
    n = exp_bin     
    while ptr >= 0:
        a = a * b**int(n[ptr]) % divisor    #a_i ≡ a_i-1 * b_i ^ n_i (mod divisor)
        b = b**2 % divisor                  #b_i ≡ b_i-1 ^ 2 (mod divisor)
        ptr -= 1

    return a                                #base ^ exponent ≡ a_k-1 (mod divisor)

if __name__ == '__main__':
    while True:
        try:
            b = int(raw_input('The base is '))
        except ValueError:
            print 'Invalid input.'
            continue
        break
    
    while True:
        try:
            e = int(raw_input('The exponent is '))
        except ValueError:
            print 'Invalid input.'
            continue
        break

    while True:
        try:
            d = int(raw_input('The divisor is '))
        except ValueError:
            print 'Invalid input.'
            continue
        break

    r = repetiveSquareModulo(b,e,d)

    print '\n%d ^ %d ≡ %d (mod %d)\n' %(b, e, r, d)
