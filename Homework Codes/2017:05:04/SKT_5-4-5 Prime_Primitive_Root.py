#-*- coding: utf-8 -*-

#奇素數模原根求取
#計算奇素數m的原根

import math

def primePrimitiveRoot(m):
    primtiveRoot = []

    #p-1的所有不同質因數表
    q = primeFactorisation(m - 1)[0]

    for g in xrange(1, m):
        modFlag = 1
        for qitem in q:
            exp = (m - 1) / qitem
            if repetiveSquareModulo(g, exp, m)  == 1:
                modFlag = 0;    break
        if modFlag == 1:        break

    prc = primitiveResidueClass(m-1)
    for num in prc:
        primtiveRoot.append(repetiveSquareModulo(g, num, m))

    # #由定義求解
    # phi_m = m - 1

    # for a in xrange(1, m):
    #     if coprimalityTest(a, m):
    #         for e in xrange(1, m):
    #             if a**e % m == 1:
    #                 if e == phi_m:
    #                     primtiveRoot.append(a)
    #                 break

    return sorted(primtiveRoot)

#簡化剩餘係
def primitiveResidueClass(n):
    rst = []

    for d in xrange(1, n):
        if coprimalityTest(d, n) == 1:
            rst.append(d)

    return rst

#素因數分解 | 返回一給定整數的標準（素因數）分解式
def primeFactorisation(N, pn=0, p=[], q=[]):
    if N < 0:   pn = 1; N = -1 * N                              #將負數轉化為正整數進行計算
    if N == 0: p.append(0); q.append(1); return p, q, pn        #N為0時的分解
    if N == 1: p.append(1); q.append(1); return p, q, pn        #N為1時的分解
    
    prmList = eratosthenesSieve(N+1)        #獲取素數表
    tmp = euclideanDivisionLoop(N, prmList)     #獲取分解因數表
    (p,q) = wrap(tmp, p, q)                 #生成因數表p與指數表q
    
    return p, q, pn

#循環歐幾里得除法
def euclideanDivisionLoop(N, prmList, rst=[]):
    if N == 1:  return rst  #除盡後返回因素序列
    
    for prm in prmList:     #逐個（遞歸）嘗試歐幾里得除法，尋找因數
        if N % prm == 0:    rst.append(prm);    N /= prm;    break
    return euclideanDivisionLoop(N, prmList, rst)

def wrap(set, p, q):
    ctr = 1
    for i in xrange(1,len(set)):
        if set[i] == set[i-1]:  ctr += 1        #重複因數，計數器自增
        else:                                   #互異因數，將前項及其計數器添入因數表與指數表，並重置計數器
            p.append(set[i-1]); q.append(ctr); ctr = 1
        
        if i == len(set)-1:                     #將最後一個因數及其計數器添入因數表與指數表
            p.append(set[i]); q.append(ctr)

    if len(set) == 1:                           #因數只有一個的特殊情況
        p.append(set[-1]);  q.append(1)
    
    return p, q

#模重複平方法 | 求解b^n (mod m)的值
def repetiveSquareModulo(base, exponent, divisor):
    get_bin = lambda x: format(x, 'b')  #二進制轉化函數

    exp_bin = get_bin(exponent)         #將指數轉為二進制
    ptr = len(exp_bin) - 1

    a = 1           
    b = base        
    n = exp_bin     
    while ptr >= 0:
        a = a * b**int(n[ptr]) % divisor    #a_i ≡ a_i-1 * b_i ^ n_i (mod divisor)
        b = b**2 % divisor                  #b_i ≡ b_i-1 ^ 2 (mod divisor)
        ptr -= 1

    return a                                #base ^ exponent ≡ a_k-1 (mod divisor)

#互素判斷 | 判斷整數a與正整數m是否互素
def coprimalityTest(a=1, m=1):
    if GCD(a, m) == 1:      #互素定義，即(a,m) = 1
        return 1
    else:
        return 0

#廣義歐幾里德除法 | 返回100,000內任意兩整數的最大公因數
def GCD(a=1, b=1):
    if a < 0:   a = -1 * a              #將a轉為正整數進行計算
    if b < 0:   b = -1 * b              #將b轉為正整數進行計算
    if a < b:   c = a;  a = b;  b = c   #交換a與b的次序，使得a≥b
    if b == 0:  return a                #(r,0) = r
    
    r = a % b
    return GCD(r, b)        #(a,b) = (r_-2,r_-1) = (r_-1,r_0) = … = (r_n,r_n+1) = (r_n,0) = r_n

#平凡除法 | 對100,000內的整數素性判斷
def trivialDivision(N=2):
    if N < 0:   N = -1 * N
    if N == 1 or N == 0:
        raise ValueError('The argument must be a natural number greater than 1.')
    
    set = eratosthenesSieve(N+1)      #得出小於N的所有素數
    if N in set:                    #素性判斷
        return 1                    #N為素數
    return 0                        #N為合數

#厄拉托塞師篩法 | 返回10,000以內正整數的所有素數（默認情況）
def eratosthenesSieve(N):
    set = [1]*(N+1)                 #用於存儲N個正整數的表格／狀態；其中，0表示篩去，1表示保留
    for index in xrange(2,int(math.sqrt(N))):  #篩法（平凡除法）
        if set[index] == 1:
            ctr = 2
            while index * ctr <= N:
                set[index*ctr] = 0      #將index的倍數篩去
                ctr += 1

    rst = []
    for ptr in xrange(2,N):          #獲取結果
        if set[ptr] == 1:
            rst.append(ptr)
            ptr += 1

    return rst

if __name__ == '__main__':
    while True:
        try:
            m = int(raw_input('The modulo is m = '))
            if m == 2 or not trivialDivision(m):
                print 'm must be an odd prime number.'
                continue
        except ValueError:
            print('Invalid input.')
            continue
        break

    a = primePrimitiveRoot(m)
    print 'The primtive root(s) of modulo %d is/are' %m,
    for root in a:
        print root,
    print '.'
