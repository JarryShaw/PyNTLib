# -*- coding: utf-8 -*-

#RSA 密鑰生成器
#通過大素數生成公／私密鑰對

import math
import random

class RSAGenerator:
    def __init__(self, lenBit=2**14):
        self.primeSet = self.eratosthenesSieve(lenBit)  #求取2^14以內的所有素數，生成素數表
        self.primeSetLen = len(self.primeSet)
        
        (self.publicKey, self.privateKey, self.divisorKey, self.blockSize) = self.keyGeneration()

        #print self.publicKey, self.privateKey, self.divisorKey, self.blockSize
        '''
        print 'The public key is %d' %self.publicKey
        print 'The private key is %d' %self.privateKey
        print 'The divisor key is %d' %self.divisorKey
        print 'The block size is %d' %self.blockSize
        '''

    #獲取公鑰對(e,n)及分區長度
    def getPublicKey(self):
        return self.publicKey, self.divisorKey, self.blockSize

    #獲取私鑰對(d,n)
    def getPrivateKey(self):
        return self.privateKey, self.divisorKey

    #厄拉托塞師篩法
    def eratosthenesSieve(self, N=10000):
        set = [1]*(N+1)                 #用於存儲N(默认为10000）個正整數的表格／狀態；其中，0表示篩去，1表示保留
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

    #生成公／私鑰對及分區長度
    def keyGeneration(self):
        p = self.cookPrimeNum()
        q = self.cookPrimeNum()

        n = p * q
        phi_n = (p-1) * (q-1)       #歐拉函數φ(n) = (p-1)*(q-1)

        e = self.cookPublicKey(phi_n)
        d = self.cookPrivateKey(phi_n, e)
        bs = self.cookBlockSize(n)

        return e, d, n, bs

    #獲取隨機大素數p及q
    def cookPrimeNum(self):
        ptr = random.randrange(0, self.primeSetLen)
        return self.primeSet[ptr]   #從素數表中隨機選取大素數

    #獲取公鑰e
    def cookPublicKey(self, phi_n):
        flag = 1                            #紀錄e與φ(n)是否互素，1為“否”，0為“是”
        eSet = []                           #紀錄曾嘗試過的無效的e
        tmp_e = random.randrange(1, phi_n)  #隨機生成e，並進行合理性判斷

        while flag:
            while tmp_e in eSet:            #若e紀錄與eSet中，重新生成之
                tmp_e = random.randrange(1, phi_n)
            if self.GCD(tmp_e, phi_n) == 1: #e與φ(n)互素性質判斷
                flag = 0
            else:
                eSet.append(tmp_e)          #若不互素，則加入eSet紀錄

        return tmp_e

    #求取最大公因數
    def GCD(self, a, b):
        if a < 0:   a = -1 * a              #將a轉為正整數進行計算
        if b < 0:   b = -1 * b              #將b轉為正整數進行計算
        if a < b:   c = a;  a = b;  b = c   #交換a與b的次序，使得a≥b
        if b == 0:  return a                #(r,0) = r
    
        r = a % b
        return self.GCD(r, b)        #(a,b) = (r_-2,r_-1) = (r_-1,r_0) = … = (r_n,r_n+1) = (r_n,0) = r_n

    #獲取私鑰d
    def cookPrivateKey(self, phi_n, e):
        (s,t) = self.bezoutEquation(e,phi_n)    #e * d ≡ 1 (mod φ(n))，等效於Bézout等式

        while s < 0:
            s += e

        return s

    #求取Bézout等式係數
    def bezoutEquation(self, a=1, b=1):
        if a < b:   c = a;  a = b;  b = c   #交換a與b的次序，使得a≥b
    
        q = self.extendedEucrideanDivision(a,b)  #廣義歐幾里德除法，求不完全商數組q
        s = self.coefficient_s(q)                #求係數s
        t = self.coefficient_t(q)                #求係數t

        return s, t

    #廣義歐幾里德除法
    def extendedEucrideanDivision(self, a, b, qSet=[0]):
        q = a / b
        r = a % b
    
        if r == 0:
            return qSet                                     #(r,0) = r
        else:
            qSet.append(q)
            return self.extendedEucrideanDivision(b, r, qSet)    #(a,b) = (r_-2,r_-1) = (r_-1,r_0) = … = (r_n,r_n+1) = (r_n,0) = r_n

    #計算Bézout等式係數s
    def coefficient_s(self, q_j, s_j1=0, s_j2=1, ctr=0):
        try:
            s = -1 * q_j[ctr] * s_j1 + s_j2 #s_j = (-q_j) * s_j-1 + s_j-2
        except IndexError:
            return s_j1
    
        s_j2 = s_j1
        s_j1 = s
        ctr += 1
        return self.coefficient_s(q_j, s_j1, s_j2, ctr)

    #計算Bézout等式係數t
    def coefficient_t(self, q_j, t_j1=1, t_j2=0, ctr=0):
        try:
            t = -1 * q_j[ctr] * t_j1 + t_j2 #t_j = (-q_j) * t_j-1 + t_j-2
        except IndexError:
            return t_j1
    
        t_j2 = t_j1
        t_j1 = t
        ctr += 1
        return self.coefficient_t(q_j, t_j1, t_j2, ctr)

    #獲取分區長度
    def cookBlockSize(self, n):
        size = 0
        series = 0

        while n - series > 0 :
            size = size + 1
            series = series + pow(95,size)

        return size-1

if __name__ == '__main__':
    rsaModule = RSAGenerator()
    (e,n,bs) = rsaModule.getPublicKey()
    (d,n)    = rsaModule.getPrivateKey()

    print 'The public key is %d' %e
    print 'The private key is %d' %d
    print 'The divisor key is %d' %n
    print 'The block size is %d' %bs
