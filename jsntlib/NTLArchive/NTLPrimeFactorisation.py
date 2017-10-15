# -*- coding: utf-8 -*-


# 素因數分解
# 返回一給定整數的標準（素因數）分解式


from .NTLEratosthenesSieve import eratosthenesSieve
from .NTLExceptions        import KeywordError
from .NTLUtilities         import jsrange
from .NTLValidations       import int_check, bool_check, pos_check


__all__  = ['primeFactorisation', 'EDLoop', 'wrap']
nickname =  'factor'


'''Usage sample:

ctr = 0
p = factor(-100, wrap=False)
print('-100 =', end=' ')
for prime in p:
    if ctr > 0:     print('*', end=' ')
    print(prime, end=' ')
    ctr += 1
print()

'''


def primeFactorisation(N, **kwargs):
    int_check(N)

    p = []
    if N < 0:   p.append(-1);   N = -N  # 將負數轉化為正整數進行計算

    prmList = eratosthenesSieve(N+1)    # 獲取素數表

    for kw in kwargs:
        if kw != 'wrap':
            raise KeywordError('Keyword \'%s\' is not defined.' % kw)
        else:
            bool_check(kwargs[kw])
            if kwargs[kw]:
                q = [1] if p == [-1] else []
                # N為0時的分解
                if N == 0:  p.append(0);    q.append(1);    return p, q
                # N為1時的分解
                if N == 1:  p.append(1);    q.append(1);    return p, q
                # 獲取分解因數表
                return wrap(EDLoop(N, prmList, p))

    # N為0時的分解
    if N == 0:  p.append(0);    return p
    # N為1時的分解
    if N == 1:  p.append(1);    return p
    return EDLoop(N, prmList, p)


# 循環歐幾里得除法
def EDLoop(N, prmList, rst):
    if N == 1:  return rst  # 除盡後返回因數序列

    for prm in prmList:     # 逐個（遞歸）嘗試歐幾里得除法，尋找因數
        if N % prm == 0:    rst.append(prm);    N //= prm;      break
    return EDLoop(N, prmList, rst)


# 整合質因數表得到因數表和指數表
def wrap(table):
    p = [];     q = []

    ctr = 1
    for i in jsrange(1, len(table)):
        # 重複因數，計數器自增
        if table[i] == table[i-1]:
            ctr += 1
        # 互異因數，將前項及其計數器添入因數表與指數表，並重置計數器
        else:
            p.append(table[i-1]); q.append(ctr); ctr = 1

        # 將最後一個因數及其計數器添入因數表與指數表
        if i == len(table)-1:
            p.append(table[i]); q.append(ctr)

    # 因數只有一個的特殊情況
    if len(table) == 1:
        p.append(table[-1]);  q.append(1)

    return p, q
