# -*- coding: utf-8 -*-

#Bézout等式
#對兩整數a與b，求出使得s*a+t*b=(a,b)的整數s和t

def bezoutEquation(a=1, b=1):
    if not isinstance(a, int) or not isinstance(b, int):
        raise __import__('NTLExceptions').IntError

    if a < b:   a, b = b, a                     #交換a與b的次序，使得a≥b
    
    q = extendedEucrideanDivision(a, b, [0])    #廣義歐幾里德除法，求不完全商數組q
    s = coefficient_s(q, 0, 1, 0)               #求係數s
    t = coefficient_t(q, 1, 0, 0)               #求係數t

    return s, t

def extendedEucrideanDivision(a, b, qSet=[0]):
    q = a / b
    r = a % b
    
    if r == 0:
        return qSet                                     #(r,0) = r
    else:
        qSet.append(q)
        return extendedEucrideanDivision(b, r, qSet)    #(a,b) = (r_-2,r_-1) = (r_-1,r_0) = … = (r_n,r_n+1) = (r_n,0) = r_n

def coefficient_s(q_j, s_j1=0, s_j2=1, ctr=0):
    try:
        s = -1 * q_j[ctr] * s_j1 + s_j2 #s_j = (-q_j) * s_j-1 + s_j-2
    except IndexError:
        return s_j1
    
    s_j2 = s_j1
    s_j1 = s
    ctr += 1
    return coefficient_t(q_j, s_j1, s_j2, ctr)

def coefficient_t(q_j, t_j1=1, t_j2=0, ctr=0):
    try:
        t = -1 * q_j[ctr] * t_j1 + t_j2 #t_j = (-q_j) * t_j-1 + t_j-2
    except IndexError:
        return t_j1
    
    t_j2 = t_j1
    t_j1 = t
    ctr += 1
    return coefficient_t(q_j, t_j1, t_j2, ctr)

if __name__ == '__main__':     
    print '%d*-179 + %d*367 = (-179,367)' %bezoutEquation(-179,367)
