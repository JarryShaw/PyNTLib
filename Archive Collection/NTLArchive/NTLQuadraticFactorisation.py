# -*- coding: utf-8 -*-

#求取係數
#求a和b使得N|a^2-b^2但N∤a+b與N∤a-b

import NTLExceptions
import NTLTrivialDivision
import NTLPrimeFactorisation

def quadraticFactorisation(N):
    if not isinstance(N, int):
        raise NTLExceptions.IntError('The argument must be integral.')

    if N <= 1:
        raise NTLExceptions.DefinitionError('The argument must be a composit number greater than 1.')

    if NTLTrivialDivision.trivialDivision(N):
        raise NTLExceptions.PCError('The argument must be composit.')

    fct = NTLPrimeFactorisation.primeFactorisation(N, wrap=True)        #獲取N的素因數分解

    for ptr0 in range(len(fct[1])):                                     #將指數表中的奇數項化為偶數項
        if (fct[1][ptr0] % 2):    fct[1][ptr0] += 1
    if len(fct[0]):                                                     #當因數表只有一個元素的情況
        if fct[0][0] == 2:   fct[0].append(3);    fct[1].append(2)      #若為2，則增補因數3^2
        else:           fct[0].append(2);    fct[1].append(2)           #若為其他，則增補因數2^2

    x = y = 1
    slc = len(fct[0]) / 2                                               #分片
    for ptr1 in range(slc):                                             #前半部求取x
        x *= int(__import__('math').pow(fct[0][ptr1],fct[1][ptr1]))
    for ptr2 in range(slc,len(fct[0])):                                 #後半部求取y
        y *= int(__import__('math').pow(fct[0][ptr2],fct[1][ptr2]))
    if (x % 2): x *= 4                                                  #若x為奇數，則增補因數4（即2^2）
    if (y % 2): y *= 4                                                  #若y為奇數，則增補因數4（即2^2）

    return solve(x,y)                                                   #求取並返回a與b

def solve(x, y):
    if x < y:   z = x;  x = y;  y = z   #交換次序，使得x>y

    a = (x + y) / 2     #x = a + b
    b = (x - y) / 2     #y = a - b

    return a, b

if __name__ == '__main__':
    (a,b) = quadraticFactorisation(100)
    print 'The solutions for N|a^2-b^2, N∤a+b and N∤a-b is\n\ta = %d\n\tb = %d' %(a,b)
