# -*- coding: utf-8 -*-

#求取係數
#求a和b使得N|a^2-b^2但N∤a+b與N∤a-b

def quadraticFactorisation(N):
    if not isinstance(N, int):
        raise __import__('NTLExceptions').IntError

    if N <= 1:
        raise __import__('NTLExceptions').DefinitionError

    if __import__('NTLTrivialDivision').trivialDivision(N):
        raise __import__('NTLExceptions').CompositError

    fct = __import__('NTLPrimeFactorisation').primeFactorisation(N)     #獲取N的素因數分解
    (p, q) = wrap(fct)                                                  #生成因數表p與指數表q

    for ptr0 in range(len(q)):                                          #將指數表中的奇數項化為偶數項
        if (q[ptr0] % 2):    q[ptr0] += 1
    if len(p):                                                          #當因數表只有一個元素的情況
        if p[0] == 2:   p.append(3);    q.append(2)                     #若為2，則增補因數3^2
        else:           p.append(2);    q.append(2)                     #若為其他，則增補因數2^2

    x = y = 1
    slc = len(p) / 2    #分片
    for ptr1 in range(slc):             #前半部求取x
        x *= int(__import__('math').pow(p[ptr1],q[ptr1]))
    for ptr2 in range(slc,len(p)):      #後半部求取y
        y *= int(__import__('math').pow(p[ptr2],q[ptr2]))
    if (x % 2): x *= 4  #若x為奇數，則增補因數4（即2^2）
    if (y % 2): y *= 4  #若y為奇數，則增補因數4（即2^2）

    return solve(x,y)   #求取並返回a與b

def wrap(table):
    p = [];     q = []
    if table[0] == -1:  del p[0]

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

def solve(x, y):
    if x < y:   z = x;  x = y;  y = z   #交換次序，使得x>y

    a = (x + y) / 2     #x = a + b
    b = (x - y) / 2     #y = a - b

    return a, b

if __name__ == '__main__':
    (a,b) = quadraticFactorisation(100)
    print 'The solutions for N|a^2-b^2, N∤a+b and N∤a-b is\n\ta = %d\n\tb = %d' %(a,b)
