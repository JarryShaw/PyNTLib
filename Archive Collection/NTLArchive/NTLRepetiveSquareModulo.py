# -*- coding: utf-8 -*-


# 模重複平方法
# 求解b^n (mod m)的值


from .NTLValidations import int_check, notneg_check, pos_check


__all__  = ['repetiveSquareModulo']
nickname =  'modulo'


'''Usage sample:

print('-765 ^ 264 ≡ %d (mod 597)\n' % modulo(-765, 264, 597))

'''


def repetiveSquareModulo(base, exponent, modulo):
    int_check(base, exponent, modulo)
    pos_check(modulo)
    notneg_check(exponent)

    if base == 0:       return 0 if (exponent != 0) else 1
    if exponent == 0:   return 1

    get_bin = lambda x: format(x, 'b')      # 二進制轉化函數

    exp_bin = get_bin(exponent)             # 將指數轉為二進制
    ptr = len(exp_bin) - 1

    a = 1
    b = base
    n = exp_bin
    while ptr >= 0:
        a = a * b**int(n[ptr]) % modulo     # a_i ≡ a_i-1 * b_i ^ n_i (mod modulo)
        b = b**2 % modulo                   # b_i ≡ b_i-1 ^ 2 (mod modulo)
        ptr -= 1

    return a if (base > 0) else (-1 * a)    # base ^ exponent ≡ a_k-1 (mod modulo)
