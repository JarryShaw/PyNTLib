# -*- coding: utf-8 -*-


import math


# 求取係數
# 求a和b使得N|a^2-b^2但N∤a+b與N∤a-b


from .NTLExceptions         import DefinitionError
from .NTLPrimeFactorisation import primeFactorisation
from .NTLTrivialDivision    import trivialDivision
from .NTLUtilities          import jsrange
from .NTLValidations        import bool_check, composit_check, int_check


__all__  = ['quadraticFactorisation', 'solve']
nickname =  'decomposit'


'''Usage sample:

(a,b) = decomposit(100)
print('The solutions for N|a^2-b^2, N∤a+b and N∤a-b is\n\ta = %d\n\tb = %d' % (a,b))

'''


def quadraticFactorisation(N, **kwargs):
    int_check(N)
    if N <= 1:
        raise DefinitionError('The argument must be a composit number greater than 1.')

    trust = False
    for kw in kwargs:
        if kw != 'trust':
            raise KeywordError('Keyword \'%s\' is not defined.' % kw)
        else:
            trust = kwargs[kw];     bool_check(trust)
    composit_check(trust, N)

    fct = primeFactorisation(N, wrap=True)                          # 獲取N的素因數分解
    for ptr0 in jsrange(len(fct[1])):                               # 將指數表中的奇數項化為偶數項
        if (fct[1][ptr0] % 2):    fct[1][ptr0] += 1
    if len(fct[0]):                                                 # 當因數表只有一個元素的情況
        if fct[0][0] == 2:  fct[0].append(3);    fct[1].append(2)   # 若為2，則增補因數3^2
        else:               fct[0].append(2);    fct[1].append(2)   # 若為其他，則增補因數2^2

    x = y = 1
    slc = len(fct[0]) // 2                                          # 分片
    for ptr1 in jsrange(slc):                                       # 前半部求取x
        x *= math.pow(fct[0][ptr1], fct[1][ptr1])
    for ptr2 in jsrange(slc, len(fct[0])):                          # 後半部求取y
        y *= math.pow(fct[0][ptr2], fct[1][ptr2])
    if (x % 2): x *= 4                                              # 若x為奇數，則增補因數4（即2^2）
    if (y % 2): y *= 4                                              # 若y為奇數，則增補因數4（即2^2）

    return solve(x, y)                                              # 求取並返回a與b


def solve(x, y):
    if x < y:   x, y = y, x     # 交換次序，使得x>y

    a = (x + y) // 2            # x = a + b
    b = (x - y) // 2            # y = a - b

    return a, b
