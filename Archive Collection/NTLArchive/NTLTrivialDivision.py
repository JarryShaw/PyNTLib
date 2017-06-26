# -*- coding: utf-8 -*-

__all__  = ['trivialDivision']
nickname = 'isprime'

import math

#平凡除法
#對任意整數素性判斷

from .NTLEratosthenesSieve import eratosthenesSieve
from .NTLExceptions        import DefinitionError
from .NTLPseudoPrime       import fermatTest, solovay_stassenTest, miller_rabinTest
from .NTLUtilities         import jsfloor, jsrange
from .NTLValidations       import int_check, pos_check

def trivialDivision(N):
    int_check(N);   pos_check(N)
    
    if N == 1 or N == 0:
        raise DefinitionError('The argument must be a natural number greater than 1.')
    
    try:
        #得出小於等於N的所有素數
        table = eratosthenesSieve(N)

        #素性判斷，1為素數，0為合數
        return 1 if (N in table) else 0

    except OverflowError:
        byte = math.log(N, 2) - 1
        para = 3**jsfloor(math.log(2**byte, 10) // 3)

        if miller_rabinTest(N, para) and fermatTest(N, para, False):
            return 1
        else:
            return 0

# if __name__ == '__main__':
#     if trivialDivision(101):
#         print('N is a prime number.')
#     else:
#         print('N is a composit number.')
