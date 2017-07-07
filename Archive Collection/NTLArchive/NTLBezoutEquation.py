# -*- coding: utf-8 -*-


# Bézout等式
# 對兩整數a與b，求出使得s*a+t*b=(a,b)的整數s和t


from .NTLEuclideanAlgorithm import euclideanAlgorithm
from .NTLValidations        import int_check


__all__  = ['bezoutEquation', 'coefficient_s', 'coefficient_t']
nickname =  'bezout'

'''Usage sample:

print('%d*-179 + %d*-367 = (-179,-367)' % bezout(-179,-367))

'''


def bezoutEquation(a, b):
    int_check(a, b)

    exflag = pn_a = pn_b = 0
    if a < 0:   a *= -1;        pn_a = 1
    if b < 0:   b *= -1;        pn_b = 1
    if a < b:   a, b = b, a;    pn_a, pn_b = pn_b, pn_a;    exflag = 1  # 交換a與b的次序，使得a≥b

    q = [0] + euclideanAlgorithm(a, b)      # 廣義歐幾里德除法（輾轉相除法），求不完全商數組q
    s = coefficient_s(q, 1, 0, 0)           # 求係數s
    t = coefficient_t(q, 0, 1, 0)           # 求係數t

    if exflag:
        s *= -1 if pn_b else 1;   t *= -1 if pn_a else 1
    else:
        s *= -1 if pn_a else 1;   t *= -1 if pn_b else 1

    return s, t


def coefficient_s(q_j, s_j1, s_j2, ctr):
    try:
        s = -1 * q_j[ctr] * s_j1 + s_j2     # s_j = (-q_j) * s_j-1 + s_j-2
    except IndexError:
        return s_j1

    s_j2 = s_j1
    s_j1 = s
    ctr += 1
    return coefficient_t(q_j, s_j1, s_j2, ctr)


def coefficient_t(q_j, t_j1, t_j2, ctr):
    try:
        t = -1 * q_j[ctr] * t_j1 + t_j2     # t_j = (-q_j) * t_j-1 + t_j-2
    except IndexError:
        return t_j1

    t_j2 = t_j1
    t_j1 = t
    ctr += 1
    return coefficient_t(q_j, t_j1, t_j2, ctr)
