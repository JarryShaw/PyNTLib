# -*- coding: utf-8 -*-

#平凡除法
#對任意整數素性判斷

import NTLExceptions
import NTLEratosthenesSieve

def trivialDivision(N=2):
    if not isinstance(N, int):
        raise NTLExceptions.IntError('The argument must be integral.')

    if N < 0:
        raise NTLExceptions.PNError('The argument must be positive.')

    if N == 1 or N == 0:
        raise NTLExceptions.DefinitionError('The argument must be a natural number greater than 1.')
    
    #得出小於等於N的所有素數
    table = NTLEratosthenesSieve.eratosthenesSieve(N)    

    #素性判斷，1為素數，0為合數
    return 1 if (N in table) else 0

if __name__ == '__main__':
    if trivialDivision(101):
        print 'N is a prime number.'
    else:
        print 'N is a composit number.'
