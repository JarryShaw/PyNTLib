# -*- coding: utf-8 -*-

#平凡除法
#對100,000內的整數素性判斷

import math

def eratosthenesSieve(N=10000):
    set = [1]*(N+1)                 #用於存儲10000個正整數的表格／狀態；其中，0表示篩去，1表示保留
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

def trivialDivision(a=1, b=1):
    max = int(math.sqrt(N))
    set = eratosthenesSieve(max)    #得出小於√N的所有素數
    for num in set:                 #素行判斷
        if N % num == 0:
            return 0                #N為合數
    return 1                        #N為素數

if __name__ == '__main__':
    while True:
        try:
            N = int(raw_input('The number is N = '))
            if N > 100000:
                print 'N must be under 100,000.'
                continue
        except ValueError:
            print 'Invalid input.'
            continue
        break
    
    if trivialDivision(N):
        print 'N is a prime number.'
    else:
        print 'N is a composit number.'