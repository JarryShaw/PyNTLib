# -*- coding: utf-8 -*-


import random


# 素性檢驗
# 用素性檢驗生成偽素數


from .NTLCarmichealTest       import carmichealTest
from .NTLExceptions           import DefinitionError, KeywordError
from .NTLJacobiSymbol         import jacobiSymbol
from .NTLRepetiveSquareModulo import repetiveSquareModulo
from .NTLUtilities            import jsrange
from .NTLValidations          import bool_check, int_check, pos_check, str_check


__all__  = ['pseudoPrime',
            'fermatTest', 'solovay_stassenTest', 'miller_rabinTes']
nickname =  'pseudo'


'''Usage sample:

print('A pseudo-prime number with Fermat test (t=10000) is %d.'
    % pseudoPrime(mode='Fermat'))
print('An Euler pseudo-prime number with Solovay-Stassen test (t=10000) is %d.'
    % pseudoPrime(mode='Euler'))
print('A strong pseudo-prime number with Miller-Rabin test (k=10000) is %d.'
    % pseudoPrime(mode='Strong'))

'''


def pseudoPrime(**kwargs):
    flag = 0        # Fermat檢驗時，是否檢查Carmicheal數
    mode = 0        # 模式選擇（Fermat／Euler／強偽素數）
    byte = 16       # 偽素數二進制位數
    para = 10000    # 安全係數

    for kw in kwargs:
        if kw == 'mode':
            str_check(kwargs[kw])

            if kwargs[kw] == 'Fermat':                          mode = 0
            elif kwargs[kw] == 'Euler' or 'Solovay-Stassen':    mode = 1
            elif kwargs[kw] == 'Strong' or 'Miller-Rabin':      mode = 2
            else:
                raise DefinitionError('Mode \'%s\' is not defined.' % kwargs[kw])

        elif kw == 'byte':
            int_check(kwargs[kw]);  pos_check(kwargs[kw])
            byte = kwargs[kw]

        elif kw == 'para':
            int_check(kwargs[kw]);  pos_check(kwargs[kw])
            para = kwargs[kw]

        elif kw == 'flag':
            bool_check(kwargs[kw])
            flag = kwargs[kw]

        else:
            raise KeywordError('Keyword \'%s\' is not defined.' % kw)

    test = {0: lambda num_: fermatTest(num_, para, flag),
            1: lambda num_: solovay_stassenTest(num_, para),
            2: lambda num_: miller_rabinTest(num_, para)}

    lower = 2 ** (byte-1)
    upper = 2 ** byte

    record = []
    while True:
        num_ = random.randrange(lower, upper)
        if num_ in record:      continue
        if num_ % 2 != 1:       continue
        if test[mode](num_):    return num_
        record.append(num_)


# Fermat素性檢驗得到Fermat偽素數
def fermatTest(n, t, flag):
    if flag and carmichealTest(n):  return False

    for ctr in jsrange(0, t):
        b = random.randrange(2, n-1)
        if repetiveSquareModulo(b, (n-1), n) != 1:
            return False
    return True


# Solovay-Stassen素性檢驗得到Euler偽素數
def solovay_stassenTest(n, t):
    exp = (n - 1) // 2
    for ctr in jsrange(0, t):
        b = random.randrange(2, n-1)
        r = repetiveSquareModulo(b, exp, n)
        if r == n - 1:                  r = -1
        if r != 1 and r != -1:          return False
        if r != jacobiSymbol(b, n):     return False
    return True


# Miller-Rabin素性檢驗生成強偽素數
def miller_rabinTest(n, k):
    s = 0;  t = n - 1
    while t % 2 == 0:
        s += 1
        t //= 2

    for ctr_1 in jsrange(0, k):
        b = random.randrange(2, n-1)
        r = repetiveSquareModulo(b, t, n)
        if r == 1 or r == n-1:  continue

        for ctr_2 in jsrange(0, s):
            r = repetiveSquareModulo(r, 2, n)
            if r == n - 1:      break
        return False
    return True
