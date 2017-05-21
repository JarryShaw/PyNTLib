# -*- coding: utf-8 -*-

#素因數分解
#返回一給定整數的標準（素因數）分解式

import NTLExceptions
import NTLEratosthenesSieve

def primeFactorisation(N=1, **kwargs):
    if not isinstance(N, int):
        raise NTLExceptions.IntError('The argument must be integral.')

    p = [] 
    if N < 0:   p.append(-1);   N = -1 * N                  #將負數轉化為正整數進行計算
    
    prmList = NTLEratosthenesSieve.eratosthenesSieve(N)     #獲取素數表

    for kw in kwargs:
        if kw != 'wrap':
            raise NTLExceptions.KeywordError('Keyword \'%s\' is not defined.' %kw)
        else:
            if not isinstance(kwargs[kw], bool):
                raise NTLExceptions.BoolError('The argument must be bool type.')
            if kwargs[kw]:
                if p != []:
                    raise NTLExceptions.PNError('The argument must be possitive under \'wrap\' mode.')
                if N == 0:  p.append(0);    return p, [1]   #N為0時的分解
                if N == 1:  p.append(1);    return p, [1]   #N為1時的分解
                return wrap(EDLoop(N, prmList, p))          #獲取分解因數表

    if N == 0:  p.append(0);    return p                    #N為0時的分解
    if N == 1:  p.append(1);    return p                    #N為1時的分解
    return EDLoop(N, prmList, p)

#循環歐幾里得除法
def EDLoop(N, prmList, rst):
    if N == 1:  return rst  #除盡後返回因數序列
    
    for prm in prmList:     #逐個（遞歸）嘗試歐幾里得除法，尋找因數
        if N % prm == 0:    rst.append(prm);    N /= prm;    break
    return EDLoop(N, prmList, rst)

#整合質因數表得到因數表和指數表
def wrap(table):
    p = [];     q = []

    ctr = 1
    for i in range(1,len(table)):
        if table[i] == table[i-1]:  ctr += 1        #重複因數，計數器自增
        else:                                       #互異因數，將前項及其計數器添入因數表與指數表，並重置計數器
            p.append(table[i-1]); q.append(ctr); ctr = 1
        
        if i == len(table)-1:                       #將最後一個因數及其計數器添入因數表與指數表
            p.append(table[i]); q.append(ctr)

    if len(table) == 1:                             #因數只有一個的特殊情況
            p.append(table[-1]);  q.append(1)

    return p, q

if __name__ == '__main__':
    ctr = 0
    p = primeFactorisation(-100, wrap=False)
    print '-100 =',
    for prime in p:
        if ctr > 0:     print '*',
        print prime,
        ctr += 1
    print
