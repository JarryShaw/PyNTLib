# -*- coding: utf-8 -*-

__all__  = ['eratosthenesSieve']
nickname = 'primelist'

import math

#厄拉托塞師篩法
#返回upper以內正整數的所有素數列表

from .NTLUtilities   import jsrange
from .NTLValidations import int_check, pos_check

def eratosthenesSieve(upper, lower=None):
    if lower is None:   lower = 2
    int_check(upper, lower)
    
    if upper < lower:
        upper, lower = lower, upper

    if lower < 2:   lower = 2
    pos_check(upper)

    table = [1]*(upper+1)                   #用於存儲upper個正整數的表格／狀態；其中，0表示篩去，1表示保留

    #篩法（平凡除法）
    for index in jsrange(2, int(math.sqrt(upper))+1):
        tmp = index * 2
        if table[index] == 1:
            while tmp <= upper:
                table[tmp] = 0              #將index的倍數篩去
                tmp += index

    #獲取結果
    rst = []
    for ptr in jsrange(lower, upper+1):             
        if table[ptr] == 1:
            rst.append(ptr)

    return rst

# if __name__ == '__main__':
#     print(eratosthenesSieve(-1, -2))
