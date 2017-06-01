# -*- coding: utf-8 -*-

#二次同餘式類
#由同餘式類衍生，型如x^2+y^2=p

import NTLExceptions
import NTLCongruence
import NTLTrivialDivision
import NTLPrimeFactorisation

class Quadratic(NTLCongruence.Congruence):

    __slots__ = ('prime', 'pcflag', 'vars')

    def __init__(self, *args, **kwargs):
        self.ctr_ = 0
        self.vars = ('x', 'y')
        self.prime = 0
        self.pcflag = False
        self.solution = None

        for prime in args:
            self.ctr_ += 1
            if self.ctr_ > 1:
                raise NTLExceptions.ArgumentError('Quadratic expected at most 1 arguments.')

            if not isinstance(prime, int) and isinstance(prime, long):
                raise NTLExceptions.IntError('The argument must be an integral.')

            if NTLTrivialDivision.trivialDivision(prime):
                self.pcflag = True
            self.prime = prime

        for kw in kwargs:
            if kw == 'vars':
                if not isinstance(kwargs[kw], tuple) or len(kwargs[kw]) != 2:
                    raise NTLExceptions.TupleError('The argument must be a tuple of two variables.')

                if not isinstance(kwargs[kw][0], str) or not isinstance(kwargs[kw][1], str):
                    raise NTLExceptions.StringError('The name of varibales must be string type.')

                self.vars = (kwargs[kw][0], kwargs[kw][1])

            else:
                raise NTLExceptions.KeywordError('Keyword \'%s\' is not defined.' %kw)

        self.solution = Solution(self)

    def __call__(self, *args):
        for prime in args:
            self.ctr_ += 1
            if self.ctr_ > 1:
                raise NTLExceptions.ArgumentError('Quadratic expected at most 1 arguments.')

            if not isinstance(prime, int) and isinstance(prime, long):
                raise NTLExceptions.IntError('The argument must be an integral.')

            if NTLTrivialDivision.trivialDivision(prime):
                self.pcflag = True
            self.prime = prime

    def __str__(self):
        return '%s^2 + %s^2 = %d' %(self.vars[0], self.vars[1], self.prime)

    def __repr__(self):
        return 'Quodratic(%d, vars=%s)' %(self.prime, str(self.vars))

    def solve(self):
        mul_ = 1
        if not self.pcflag:
            (p_, q_) = NTLPrimeFactorisation.primeFactorisation(self.prime, wrap=True)

            ctr_ = 0
            for ptr_ in xrange(len(p_)):
                if q_[ptr_] % 2 == 1:
                    ctr_ += 1
                    if ctr_ > 2:
                        return self.solution
                    if q_[ptr_] == 1:
                        p = p_[ptr_]
                    else:
                        mul_ *= p_[ptr_] ** ((q_[ptr_]-1) / 2)
                else:
                    mul_ *= p_[ptr_] ** (q_[ptr_] / 2)
        else:
            p = self.prime

        if p % 4 != 1:
            return self.solution

        if p % 8 == 5:      #若p=8k+5為素數，有2為模p平方非剩餘，則同餘式x^2≡-1(mod p)的解為x=±2^((p-1)/4)(mod p)
            #令x_0 = 2^((p-1)/4)(mod p)
            x = (2**((p-1)/4)) % p                          
        else:               #反之，用同餘式求解函數求出結果
            #令x_0為x^2≡-1(mod p)的正解
            x = NTLCongruence.Congruence((2,1), (0,1), mod=p).solve()[0]
        
        y = 1                                               #令y_0 = 1
        m = (x**2 + y**2) / p                               #由x_0^2 + y_0^2 = m_0 * p得m_0

        while m != 1:                                       #在x_i^2 + y_i^2 = p即m_0 = 1之後，退出循環
            tmp_x = x                                       #寄存當前的x_i-1
            u = x % m if (x%m - m != -1) else -1            #令u_i-1 ≡ x_i-1 (mod m_i-1)
            v = y % m if (y%m - m != -1) else -1            #令v_i-1 ≡ y_i-1 (mod m_i-1)
            x = (u*x + v*y) / m                             #則x_i = (u_i-1 * x_i-1 + v_i-1 * y_i-1) / m_i-1
            y = (u*y - v*tmp_x) / m                         #則y_i = (u_i-1 * y_i-1 - v_i-1 * x_i-1) / m_i-1
            m = (x**2 + y**2) / p                           #由x_i^2 + y_i^2 = m_i * p得m_i

        x *= mul_
        y *= mul_
        self.solution(x, y)
        return self.solution

class Solution:
    def __init__(self, qua_):
        self.x = 0
        self.y = 0
        self.var_x = qua_.vars[0]
        self.var_y = qua_.vars[1]

    def __call__(self, x, y):
        self.x = x if x > 0 else -1 * x
        self.y = y if y > 0 else -1 * y

    def __str__(self):
        if self.x != 0 or self.y != 0:
            return '%s = ±%d\t%s = ±%d' %(self.var_x, self.x, self.var_y, self.y) 
        else:
            return 'No solution'

    def __getitem__(self, key_):
        if key_ == 0:
            return self.x
        elif key_ == 1:
            return self.y
        else:
            raise IndexError

if __name__ == '__main__':
    qua_ = Quadratic(8068, vars=('p', 'q'))
    rst_ = qua_.solve()

    print 'The solution of %s is' %str(qua_)
    print rst_
