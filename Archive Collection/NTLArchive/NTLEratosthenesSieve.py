# -*- coding: utf-8 -*-

#厄拉托塞師篩法
#返回upper以內正整數的所有素數列表

import NTLExceptions

def eratosthenesSieve(upper=2, lower=2):
    if not isinstance(lower, int) or not isinstance(upper, int):
        raise NTLExceptions.IntError('The arguments must be integral.')

    if upper < lower:
        upper, lower = lower, upper

    if upper < 0:
        raise NTLExceptions.PNError('The upper bound must be positive.')

    if lower < 2:   lower = 2

    table = [1]*(upper+1)                   #用於存儲upper個正整數的表格／狀態；其中，0表示篩去，1表示保留

    #篩法（平凡除法）                 
    for index in xrange(2, int(__import__('math').sqrt(upper))+1):   
        tmp = index * 2
        if table[index] == 1:
            while tmp <= upper:
                table[tmp] = 0              #將index的倍數篩去
                tmp += index

    #獲取結果
    rst = []
    for ptr in xrange(lower, upper+1):             
        if table[ptr] == 1:
            rst.append(ptr)

    return rst

if __name__ == '__main__':
    print eratosthenesSieve(101, -1)
