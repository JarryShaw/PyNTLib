# -*- coding: utf-8 -*-

#厄拉托塞師篩法
#返回N以內正整數的所有素數列表

def eratosthenesSieve(N=100):
    if not isinstance(N, int):
        raise __import__('NTLExceptions').IntError

    if N < 0:
        raise __import__('NTLExceptions').PNError

    table = [1]*(N+1)                   #用於存儲N個正整數的表格／狀態；其中，0表示篩去，1表示保留

    #篩法（平凡除法）                 
    for index in xrange(2, int(__import__('math').sqrt(N))+1):   
        if table[index] == 1:
            ctr = 2
            while index * ctr <= N:
                table[index*ctr] = 0    #將index的倍數篩去
                ctr += 1

    #獲取結果
    rst = []
    for ptr in xrange(2,N):             
        if table[ptr] == 1:
            rst.append(ptr)
            ptr += 1

    return rst

if __name__ == '__main__':
    print eratosthenesSieve(101)
