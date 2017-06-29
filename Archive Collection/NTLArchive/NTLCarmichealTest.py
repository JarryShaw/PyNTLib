#-*- coding: utf-8 -*-

__all__  = ['carmichealTest']
nickname =  'carmicheal'

#Carmicheal數檢驗
#判斷奇整數n是否為Carmicheal數，即使得Fermat素性檢驗無效的數

from .NTLPrimeFactorisation import primeFactorisation
from .NTLValidations        import int_check, pos_check, odd_check

def carmichealTest(n):
    int_check(n);   pos_check(n);   odd_check(n)

    (p, q) = primeFactorisation(n, wrap=True)

    if len(p) < 3:                  return False

    for qitem in q:
        if qitem > 1:               return False

    for pitem in p:
        if (n-1) % (pitem-1) != 0:  return False

    return True

# if __name__ == '__main__':
#     print('3499', end=' ')
#     if carmichealTest(3499):
#         print('is', end=' ')
#     else:
#         print('isn\'t', end=' ')
#     print('a Carmicheal number.')
