#-*- coding: utf-8 -*-

from .__abc__ import __symbol__

__all__  = ['Jacobi',
            'default_numerator', 'default_denominator',
            'jacobi_eval', 'jacobi_simplify', 'jacobi_reciprocate']
nickname = 'Jacobi'

#Jacobi符號類
#具備化簡、求值等基本功能

from .NTLExceptions           import DefinitionError, KeywordError
from .NTLPrimeFactorisation   import primeFactorisation
from .NTLTrivialDivision      import trivialDivision
from .NTLUtilities            import jssign
from .NTLValidations          import prime_check, str_check

# from .NTLLegendre import Legendre

Symbol = __symbol__.ABCSymbol

# Jacobi default form.
default_numerator   = 1
default_denominator = 2

def jacobi_eval(jacobi):
    _ret = jacobi_simplify(jacobi)

    a = _ret.numerator
    p = _ret.denominator

    if a == 1:      return 1
    if a == - 1:    return (-1)**((p-1)//2)
    if a == 2:      return (-1)**((p**2-1)//8)

    r = jssign(a)
    for _a in primeFactorisation(abs(a)):
        r *= Jacobi(_a, p).eval()

    return r if r != p-1 else -1

def jacobi_simplify(jacobi):
    _ret = jacobi

    while abs(_ret.numerator) not in [0, 1, 2]\
            and trivialDivision(abs(_ret.numerator)):
        _num = _ret.numerator
        _den = _ret.denominator

        if _den > abs(_num):
            _ret = jacobi_reciprocate(_ret)

    return _ret

def jacobi_reciprocate(jacobi):
    _den = jacobi.numerator
    _num = jacobi.denominator * (-1)**((_den-1)//2) % _den

    if _num == _den - 1:    _num = -1
    _ret = Jacobi(_num, _den)

    return _ret

class Jacobi(Symbol):

    def convert(self, kind):
        str_check(kind)

        if kind == 'Jacobi':
            return self
        elif kind == 'Legendre':
            from .NTLLegendre import Legendre
            _ret = Legendre(self.numerator, self.denominator)
            return _ret
        else:
            raise KeywordError('%s is an unknown type of symbol.' %kind)

    # Virtual properties.
    nickname    = 'Jacobi'
    numerator   = default_numerator
    denominator = default_denominator

    # Virtual functions.
    eval = jacobi_eval
    simplify = jacobi_simplify
    reciprocate = jacobi_reciprocate

# if __name__ == '__main__':
#     l1 = Jacobi(1, 2)
#     l2 = Jacobi('2|3')
#     l3 = Jacobi(l1)

#     print(l1, l1.eval())
#     print(l2, l2.eval())
#     print(l3, l3.eval())
