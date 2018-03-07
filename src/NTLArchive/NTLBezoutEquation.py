# -*- coding: utf-8 -*-


# Bézout等式
# 對兩整數a與b，求出使得s*a+t*b=(a,b)的整數s和t


from .NTLEuclideanAlgorithm import euclideanAlgorithm
from .NTLPolynomial         import Polynomial
from .NTLValidations        import int_check


__all__  = ['bezoutEquation', 'coefficient_s', 'coefficient_t']
nickname =  'bezout'


'''Usage sample:

print('%d*-179 + %d*-367 = (-179,-367)' % bezout(-179, -367))

'''


def bezoutEquation(a, b):
    exflag = pn_a = pn_b = False

    if isinstance(a, Polynomial) or isinstance(b, Polynomial):
        a = Polynomial(a);          b = Polynomial(b)
    else:
        int_check(a, b)
        if a < 0:   a *= -1;        pn_a = True
        if b < 0:   b *= -1;        pn_b = True
        if a < b:   a, b = b, a;    pn_a, pn_b = pn_b, pn_a;    exflag = True   # 交換a與b的次序，使得a≥b

    q = [0] + euclideanAlgorithm(a, b)      # 廣義歐幾里德除法（輾轉相除法），求不完全商數組q
    s, t = coefficients(q)                  # 求係數s和t

    if pn_a ^ pn_b:
        if exflag:
            tmp = s
            s = -t   if pn_b else t
            t = -tmp if pn_a else tmp

        else:
            if pn_b:    s = -s
            if pn_a:    t = -t

    elif pn_a and pn_b:
        if exflag:  s, t = -t, -s
        else:       s, t = -s, -t

    else:
        if exflag:  s, t = t, s

    return s, t


def coefficients(q):
    s_j1 = 1;   s_j2 = 0
    t_j1 = 0;   t_j2 = 1

    for q_j in q:
        s_j = -q_j * s_j1 + s_j2            # s_j = (-q_j) * s_j-1 + s_j-2
        t_j = -q_j * t_j1 + t_j2            # t_j = (-q_j) * t_j-1 + t_j-2

        s_j2 = s_j1;    s_j1 = s_j
        t_j2 = t_j1;    t_j1 = t_j
    else:
        return s_j, t_j

    return (0, 1)
