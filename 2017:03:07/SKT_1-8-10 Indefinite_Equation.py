# -*- coding: utf-8 -*-

#求解不定方程
#求解二元一次不定方程的通解和特解

def indefiniteEquation(a=1, b=1, c=1, apn=0, bpn=0):
    if a < 0:   a *= -1;    apn = 1
    if b < 0:   b *= -1;    bpn = 1
    if c < 0:   c *= -1

    mcf = maxCommonFactor(a,b)
    if (c % mcf):   raise ValueError
    else:               mtp = c / mcf
    
    (s,t) = bezoutEquation(a,b)
    x0 = s * mtp;   y0 = t * mtp
    
    if apn: x0 *= -1
    if bpn: y0 *= -1
    return x0, y0, a, b

def maxCommonFactor(a, b):
    if a < 0:   a = -1 * a              #將a轉為正整數進行計算
    if b < 0:   b = -1 * b              #將b轉為正整數進行計算
    if a < b:   c = a;  a = b;  b = c   #交換a與b的次序，使得a≥b
    if b == 0:  return a                #(r,0) = r
    
    r = a % b
    return maxCommonFactor(r, b)        #(a,b) = (r_-2,r_-1) = (r_-1,r_0) = … = (r_n,r_n+1) = (r_n,0) = r_n

def bezoutEquation(a, b):
    if a < b:   c = a;  a = b;  b = c   #交換a與b的次序，使得a≥b
    
    q = extendedEucrideanDivision(a,b)  #廣義歐幾里德除法，求不完全商數組q
    s = coefficient_s(q)                #求係數s
    t = coefficient_t(q)                #求係數t
    
    return s, t

def coefficient_s(q_j, s_j1=0, s_j2=1, ctr=0):
    try:
        s = -1 * q_j[ctr] * s_j1 + s_j2 #s_j = (-q_j) * s_j-1 + s_j-2
    except IndexError:
        return s_j1
    
    s_j2 = s_j1
    s_j1 = s
    ctr += 1
    return coefficient_s(q_j, s_j1, s_j2, ctr)

def coefficient_t(q_j, t_j1=1, t_j2=0, ctr=0):
    try:
        t = -1 * q_j[ctr] * t_j1 + t_j2 #t_j = (-q_j) * t_j-1 + t_j-2
    except IndexError:
        return t_j1
    
    t_j2 = t_j1
    t_j1 = t
    ctr += 1
    return coefficient_t(q_j, t_j1, t_j2, ctr)

def extendedEucrideanDivision(a, b, qSet=[]):
    q = a / b
    r = a % b
    
    if r == 0:
        return qSet                                     #(r,0) = r
    else:
        qSet.append(q)
        return extendedEucrideanDivision(b, r, qSet)    #(a,b) = (r_-2,r_-1) = (r_-1,r_0) = … = (r_n,r_n+1) = (r_n,0) = r_n

if __name__ == '__main__':
    while True:
        try:
            a = int(raw_input('The coefficient for x is '))
        except ValueError:
            print 'Invalid input.'
            continue
        break
    
    while True:
        try:
            b = int(raw_input('The coefficient for y is '))
        except ValueError:
            print 'Invalid input.'
            continue
        break

    while True:
        try:
            c = int(raw_input('The constant term is '))
        except ValueError:
            print 'Invalid input.'
            continue
        break

    (x0,y0,a,b) = indefiniteEquation(a,b,c)

    print 'The general solutions for \'%d*x + %d*y = %d\' is (t∈Z)' %(a, b, c)
    print 'x = %d + %d*t' %(x0, b)
    print 'y = %d - %d*t' %(y0, a)
