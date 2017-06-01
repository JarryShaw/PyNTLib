#-*- coding: utf-8 -*-

#指標類
#計算整數m的指標，並用於求模計算

import NTLExceptions
import NTLEulerFunction
import NTLPrimitiveRoot
import NTLRepetiveSquareModulo

class Index:
    def __init__(self, modulo):
        self.mul_ = []
        self.mod_ = modulo
        self.pmr_ = NTLPrimitiveRoot.primitiveRoot(modulo)[0]
        self.phi_ = NTLEulerFunction.eulerFunction(self.mod_)
        self.ind_ = self.index()
        self.tab_ = self.table()

    def __call__(self, *args):
        for int_ in args:
            if not isinstance(int_, int) and not isinstance(int_, long):
                raise NTLExceptions.Tuple('Call Index instance to calculate mod-product of integers.')
            self.mul_.append(int_)

        return self.multiply()

    def __repr__(self):
        return 'Index(%d)' %self.mod_

    def __str__(self):
        string = '\t0\t1\t2\t3\t4\t5\t6\t7\t8\t9'
        for i in range(len(self.tab_)):
            string += '\n%d\t' %i
            for j in self.tab_[i]:
                if j == 0:
                    string += '\t'
                else:
                    string += '%d\t' %j
            string = string[:-1]

        return string

    def index(self):
        ind_ = [0]*self.mod_
        for num_ in xrange(1, self.mod_):
            index = NTLRepetiveSquareModulo.repetiveSquareModulo(self.pmr_, num_, self.mod_)
            ind_[index] = num_

        return ind_

    def table(self):
        tab_ = []
        for ctr in range(0, self.phi_+1, 10):
            tab_.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        for ptr in range(1, self.mod_):
            tab_[ptr/10][ptr%10] = self.ind_[ptr]

        return tab_

    def multiply(self):
        index_a = self.ind_[self.mul_[0] % self.mod_]
        index_b = self.ind_[self.mul_[1] % self.mod_]

        return (self.pmr_ ** ((index_a + index_b) % self.phi_)) % self.mod_

if __name__ == '__main__':
    index = Index(41)
    print index
    print
    rst = index(4, 8)
    print '4 * 8 ≡ %d' %rst
