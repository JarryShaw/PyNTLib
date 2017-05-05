# -*- coding: utf-8 -*-

#素因數分解
#返回一給定整數的標準（素因數）分解式

import NTLExceptions
import NTLEratosthenesSieve

def primeFactorisation(N):
    if not isinstance(N, int):
        raise NTLExceptions.IntError('The argument must be integral.')

    p = []
        
    if N < 0:   p.append(-1);   N = -1 * N      #將負數轉化為正整數進行計算
    if N == 0:  p.append(0);    return p        #N為0時的分解
    if N == 1:  p.append(1);    return p        #N為1時的分解
    
    prmList = NTLEratosthenesSieve.eratosthenesSieve(N+1) #獲取素數表
    return euclideanDivisionLoop(N, prmList, p)                            #獲取分解因數表

#循環歐幾里得除法
def euclideanDivisionLoop(N, prmList, rst=[]):
    if N == 1:  return rst  #除盡後返回因數序列
    
    for prm in prmList:     #逐個（遞歸）嘗試歐幾里得除法，尋找因數
        if N % prm == 0:    rst.append(prm);    N /= prm;    break
    return euclideanDivisionLoop(N, prmList, rst)

if __name__ == '__main__':
    ctr = 0
    p = primeFactorisation(-100)
    print
    print '-100 =',
    for prime in p:
        if ctr > 0:     print '*',
        print prime,
        ctr += 1
    print
