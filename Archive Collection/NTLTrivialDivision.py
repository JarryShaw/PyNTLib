# -*- coding: utf-8 -*-

#平凡除法
#對任意整數素性判斷

def trivialDivision(N=2):
    if not isinstance(N, int):
        raise __import__('NTLExceptions').IntError

    if N < 0:
        raise __import__('NTLExceptions').PNError

    if N == 1 or N == 0:
        raise __import__('NTLExceptions').DefinitionError
    
    #得出小於等於N的所有素數
    table = __import__('NTLEratosthenesSieve').eratosthenesSieve(N + 1)    

    #素性判斷，1為素數，0為合數
    return 1 if (N in table) else 0

if __name__ == '__main__':
    if trivialDivision(100):
        print 'N is a prime number.'
    else:
        print 'N is a composit number.'
