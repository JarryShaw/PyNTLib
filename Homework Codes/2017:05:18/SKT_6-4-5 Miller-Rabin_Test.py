#-*- coding: utf-8 -*-

#Miller-Rabin素性檢驗
#用Miller-Rabin素性檢驗生成強偽素數

import math
import random

def pseudoPrime(i=12, k=100000):
    lower = 2 ** (i-1)
    upper = 2 ** i

    while True:
        n = random.randrange(lower, upper)
        if n % 2 != 1:                  continue
        if miller_rabinTest(n, k):      return n

def miller_rabinTest(n, k):
    s = 0;  t = n - 1
    while t % 2 == 0:
        s += 1
        t /= 2

    for ctr_1 in range(0, k):
        b = random.randrange(2, n-1)
        r = repetiveSquareModulo(b, t, n)
        if r == 1 or r == n-1:  continue

        for ctr_2 in range(0, s):
            r = repetiveSquareModulo(r, 2, n)
            if r == n - 1:      break
        return False
    return True

#模重複平方法 | 求解b^n (mod m)的值
def repetiveSquareModulo(base, exponent, divisor):
    get_bin = lambda x: format(x, 'b')  #二進制轉化函數

    exp_bin = get_bin(exponent)         #將指數轉為二進制
    ptr = len(exp_bin) - 1

    a = 1           
    b = base        
    n = exp_bin     
    while ptr >= 0:
        a = a * b**int(n[ptr]) % divisor    #a_i ≡ a_i-1 * b_i ^ n_i (mod divisor)
        b = b**2 % divisor                  #b_i ≡ b_i-1 ^ 2 (mod divisor)
        ptr -= 1

    return a                                #base ^ exponent ≡ a_k-1 (mod divisor)

if __name__ == '__main__':
    print 'A strong pseudo-prime number with Miller-Rabin test (k=100000) is %d.' %pseudoPrime()
