# -*- coding: utf-8 -*-

__all__  = ['euclideanAlgorithm', 'EEALoop']
nickname = 'eealist'

#廣義歐幾里德除法
#用輾轉相除法求出商數列

from .NTLExceptions  import DefinitionError
from .NTLValidations import int_check

def euclideanAlgorithm(dividend, divisor):
    int_check(dividend, divisor)

    if divisor == 0:
        raise DefinitionError('The divisor should never be zero.')

    return EEALoop(dividend, divisor, [])

def EEALoop(a, b, qSet):
    q = a // b
    r = a %  b
    
    if r == 0:
        return qSet                 #(r,0) = r
    else:
        qSet.append(q)
        return EEALoop(b, r, qSet)  #(a,b) = (r_-2,r_-1) = (r_-1,r_0) = … = (r_n,r_n+1) = (r_n,0) = r_n

# if __name__ == '__main__':
#     print(euclideanAlgorithm(3424, 13))
