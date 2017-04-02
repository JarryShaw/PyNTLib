# -*- coding: utf-8 -*-

#素因數分解
#返回一給定整數的標準（素因數）分解式

import math

def primeFactorisation(N, pn=0, p=[], q=[]):
    if N < 0:   pn = 1; N = -1 * N                              #將負數轉化為正整數進行計算
    if N == 0: p.append(0); q.append(1); return p, q, pn        #N為0時的分解
    if N == 1: p.append(1); q.append(1); return p, q, pn        #N為1時的分解
    
    prmList = eratosthenesSieve(N+1)        #獲取素數表
    tmp = euclideanDivision(N, prmList)     #獲取分解因數表
    (p,q) = wrap(tmp, p, q)                 #生成因數表p與指數表q
    
    return p, q, pn

def eratosthenesSieve(N):
    set = [1]*(N+1)                 #用於存儲N個正整數的表格／狀態；其中，0表示篩去，1表示保留
    for index in range(2,int(math.sqrt(N))):  #篩法（平凡除法）
        if set[index] == 1:
            ctr = 2
            while index * ctr <= N:
                set[index*ctr] = 0      #將index的倍數篩去
                ctr += 1

    rst = []
    for ptr in range(2,N):          #獲取結果
        if set[ptr] == 1:
            rst.append(ptr)
            ptr += 1

    return rst

def euclideanDivision(N, prmList, rst=[]):
    if N == 1:  return rst  #除盡後返回因素序列
    
    for prm in prmList:     #逐個（遞歸）嘗試歐幾里得除法，尋找因數
        if N % prm == 0:    rst.append(prm); N = N / prm;    break
    return euclideanDivision(N, prmList, rst)

def wrap(set, p, q):
    ctr = 1
    for i in range(1,len(set)):
        if set[i] == set[i-1]:  ctr += 1        #重複因數，計數器自增
        else:                                   #互異因數，將前項及其計數器添入因數表與指數表，並重置計數器
            p.append(set[i-1]); q.append(ctr); ctr = 1
        
        if i == len(set)-1:                     #將最後一個因數及其計數器添入因數表與指數表
            p.append(set[i]); q.append(ctr)

    if len(set) == 1:                           #因數只有一個的特殊情況
        p.append(set[-1]);  q.append(1)
    
    return p, q

if __name__ == '__main__':
    while True:
        try:
            N = int(raw_input('The number is N = '))
        except ValueError:
            print 'Invalid input.'
            continue
        break
    
    ctr = 0
    (p,q,pn) = primeFactorisation(N)
    print N, '=',
    if pn:  print '-',
    for prime in p:
        if ctr > 0:     print '*',
        if q[ctr] != 1: print '%d^%d' %(prime, q[ctr]),
        else:           print prime,
        ctr += 1
