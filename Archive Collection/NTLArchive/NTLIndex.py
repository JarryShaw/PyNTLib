# -*- coding: utf-8 -*-


# 指標類
# 計算整數m的指標，並用於求模計算


from .NTLEulerFunction        import eulerFunction
from .NTLPrimitiveRoot        import primitiveRoot
from .NTLRepetiveSquareModulo import repetiveSquareModulo
from .NTLUtilities            import jsrange
from .NTLValidations          import int_check, pos_check


__all__  = ['Index']
nickname =  'Index'


'''Usage sample:

index = Index(41)
print(index, '\n')
rst = index(4, 8)
print('4 * 8 ≡ %d' % rst)

'''


class Index:

    __all__ = ['_mul', '_mod', '_pmr', '_phi', '_ind', '_tab']

    ##########################################################################
    # Properties.
    ##########################################################################

    @property
    def modulo(a):
        return a._mod

    @property
    def root(a):
        return a._pmr

    @property
    def phi(a):
        return a._phi

    @property
    def index(a):
        return a._ind

    @property
    def table(a):
        return a._tab

    ##########################################################################
    # Data models.
    ##########################################################################

    def __init__(self, modulo):
        int_check(modulo);  pos_check(modulo)

        self._mul = []
        self._mod = modulo
        self._pmr = primitiveRoot(modulo)[0]
        self._phi = eulerFunction(self._mod)
        self._ind = self._make_index()
        self._tab = self._make_table()

    def __call__(self, *args):
        self._mul = []
        for _int in args:
            int_check(_int)
            if _int == 0:   return 0
            self._mul.append(_int)

        if self._mul == []: return None
        _product = self._calc_multi()

        return _product

    def __repr__(self):
        return 'Index(%d)' % self_.mod

    def __str__(self):
        string = '\t0\t1\t2\t3\t4\t5\t6\t7\t8\t9'
        for i in jsrange(len(self._tab)):
            string += '\n%d\t' % i
            for j in self._tab[i]:
                if j == 0:
                    string += '\t'
                else:
                    string += '%d\t' % j
            string = string[:-1]

        return string

    ##########################################################################
    # Utilities.
    ##########################################################################

    def _make_index(self):
        _ind = [0]*self._mod
        for _num in jsrange(1, self._mod):
            ptr = repetiveSquareModulo(self._pmr, _num, self._mod)
            _ind[ptr] = _num

        return _ind

    def _make_table(self):
        _tab = []
        for ctr in jsrange(0, self._phi+1, 10):
            _tab.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        for ptr in jsrange(1, self._mod):
            _tab[ptr//10][ptr%10] = self._ind[ptr]

        return _tab

    def _calc_multi(self):
        _all_index = 0
        for _mul in self._mul:
            _all_index += self._ind[_mul % self._mod]
        _product = (self._pmr ** (_all_index % self._phi)) % self._mod

        return _product
