# -*- coding: utf-8 -*-


import math


# 平凡除法
# 對任意整數素性判斷


from .NTLEratosthenesSieve import eratosthenesSieve
from .NTLExceptions        import DefinitionError
from .NTLUtilities         import jsfloor, jsmaxint, jsrange
from .NTLValidations       import int_check, pos_check

# from .NTLPseudoPrime import miller_rabinTest


__all__  = ['trivialDivision']
nickname =  'isprime'


'''Usage sample:

if isprime(101):
    print('N is a prime number.')
else:
    print('N is a composit number.')

'''


def trivialDivision(N):
    int_check(N);   pos_check(N)

    if N == 1 or N == 0:
        raise DefinitionError('The argument must be a natural number greater than 1.')

    if math.log(N, 10)  <= 7.0:
        # 得出小於等於N的所有素數
        table = eratosthenesSieve(N+1)

        # 素性判斷，True為素數，False為合數
        return True if (N in table) else False

    # 若輸入的常數過大，則採用強偽素數檢驗
    else:
        try:
            byte = math.log(N, 2) - 1
            para = 3**jsfloor(math.log(2**byte, 10) // 3)
        except (OverflowError, MemoryError):
            para = jsmaxint

        # 素性判斷，True為素數，False為合數
        from .NTLPseudoPrime import miller_rabinTest
        return True if miller_rabinTest(N, para) else False
