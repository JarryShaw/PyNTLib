#-*- coding: utf-8 -*-

__all__  = ['Index']
nickname = 'Index'

#指標類
#計算整數m的指標，並用於求模計算

from .NTLEulerFunction        import eulerFunction
from .NTLPrimitiveRoot        import primitiveRoot
from .NTLRepetiveSquareModulo import repetiveSquareModulo
from .NTLUtilities            import jsrange
from .NTLValidations          import int_check

class Index:

    __all__ = ['mul_', 'mod_', 'pmr_', 'phi_', 'ind_', 'tab_']

    def __init__(self, modulo):
        self.mul_ = []
        self.mod_ = modulo
        self.pmr_ = primitiveRoot(modulo)[0]
        self.phi_ = eulerFunction(self.mod_)
        self.ind_ = self.index()
        self.tab_ = self.table()

    def __call__(self, *args):
        for int_ in args:
            int_check(int_)
            self.mul_.append(int_)

        return self.multiply()

    def __repr__(self):
        return 'Index(%d)' %self.mod_

    def __str__(self):
        string = '\t0\t1\t2\t3\t4\t5\t6\t7\t8\t9'
        for i in jsrange(len(self.tab_)):
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
        for num_ in jsrange(1, self.mod_):
            index = repetiveSquareModulo(self.pmr_, num_, self.mod_)
            ind_[index] = num_

        return ind_

    def table(self):
        tab_ = []
        for ctr in jsrange(0, self.phi_+1, 10):
            tab_.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        for ptr in jsrange(1, self.mod_):
            tab_[ptr//10][ptr%10] = self.ind_[ptr]

        return tab_

    def multiply(self):
        index_a = self.ind_[self.mul_[0] % self.mod_]
        index_b = self.ind_[self.mul_[1] % self.mod_]

        return (self.pmr_ ** ((index_a + index_b) % self.phi_)) % self.mod_

# if __name__ == '__main__':
#     index = Index(41)
#     print(index)
#     print()
#     rst = index(4, 8)
#     print('4 * 8 ≡ %d' %rst)
