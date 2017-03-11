# -*- coding: utf-8 -*-

#求取係數
#求a和b使得N|a^2-b^2但N∤a+b與N∤a-b

import math

def decomposition(N=4):
    (p,q,pn) = primeFactorisation(N)        #獲取N的素因數分解
    for ptr0 in range(len(q)):              #將指數表中的奇數項化為偶數項
        if (q[ptr0] % 2):    q[ptr0] += 1
    if len(p):                              #當因數表只有一個元素的情況
        if p[0] == 2:   p.append(3);    q.append(2)     #若為2，則增補因數3^2
        else:           p.append(2);    q.append(2)     #若為其他，則增補因數2^2

    x = y = 1
    slc = len(p) / 2    #分片
    for ptr1 in range(slc):             #前半部求取x
        x *= int(math.pow(p[ptr1],q[ptr1]))
    for ptr2 in range(slc,len(p)):      #後半部求取y
        y *= int(math.pow(p[ptr2],q[ptr2]))
    if (x % 2): x *= 4  #若x為奇數，則增補因數4（即2^2）
    if (y % 2): y *= 4  #若y為奇數，則增補因數4（即2^2）

    return solve(x,y)   #求取並返回a與b

def solve(x, y):
    if x < y:   z = x;  x = y;  y = z   #交換次序，使得x>y

    a = (x + y) / 2     #x = a + b
    b = (x - y) / 2     #y = a - b

    return a, b

def primeFactorisation(N, pn=0, p=[], q=[]):
    if N < 0:   pn = 1; N = -1 * N; primeFactorisation(N, pn)   #將負數轉化為正整數進行計算
    if N == 0: p.append(0); q.append(1); return p, q, pn        #N為0時的分解
    if N == 1: p.append(1); q.append(1); return p, q, pn        #N為1時的分解

    prmList = eratosthenesSieve(N+1)        #獲取素數表
    tmp = euclideanDivision(N, prmList)     #獲取分解因數表
    (p,q) = wrap(tmp, p, q)                 #生成因數表p與指數表q
    
    return p, q, pn

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

def euclideanDivision(N, prmList, rst=[]):
    if N == 1:  return rst  #除盡後返回因素序列
    
    for prm in prmList:     #逐個（遞歸）嘗試歐幾里得除法，尋找因數
        if N % prm == 0:    rst.append(prm); N = N / prm;    break
    return euclideanDivision(N, prmList, rst)

def trivialDivision(N):
    if N < 0:   N = -1 * N
    if N == 1 or N == 0:    raise ValueError
    
    set = eratosthenesSieve(N)    #得出小於N的所有素數
    for num in set:                 #素性判斷
        if N % num == 0:
            return 0                #N為合數
    return 1                        #N為素數

def eratosthenesSieve(N=10000):
    set = [1]*(N+1)                 #用於存儲N個正整數的表格／狀態；其中，0表示篩去，1表示保留
    for index in range(2,int(math.sqrt(N))):  #篩法（平凡除法）
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

if __name__ == '__main__':
    while True:
        try:
            N = int(raw_input('The number is N = '))
        except ValueError:
            print 'Invalid input.'
            continue
        if N <= 1:
            print 'Must be a positive number.'
            continue
        if trivialDivision(N):
            print 'Must be a composit number.'
            continue
        break
    
    (a,b) = decomposition(N)
    print 'a and b for N|a^2-b^2, N∤a+b and N∤a-b is\na = %d\nb = %d' %(a,b)
