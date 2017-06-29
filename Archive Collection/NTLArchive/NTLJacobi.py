#-*- coding: utf-8 -*-

from .__abc__ import __symbol__

__all__  = ['Jacobi',
            'default_numerator', 'default_denominator',
            'jacobi_eval', 'jacobi_simplify', 'jacobi_reciprocate']
nickname =  'Jacobi'

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

    a = _ret._numerator
    p = _ret._denominator

    if a == 1:      return 1
    if a == - 1:    return (-1)**((p-1)//2)
    if a == 2:      return (-1)**((p**2-1)//8)

    r = jssign(a)
    for _a in primeFactorisation(abs(a)):
        r *= Jacobi(_a, p).eval()

    return r if r != p-1 else -1

def jacobi_simplify(jacobi):
    _ret = jacobi

    while abs(_ret._numerator) not in [0, 1, 2]\
            and trivialDivision(abs(_ret._numerator)):
        _num = _ret._numerator
        _den = _ret._denominator

        if _den > abs(_num):
            _ret = jacobi_reciprocate(_ret)

    return _ret

def jacobi_reciprocate(jacobi):
    _den = jacobi._numerator
    _num = jacobi._denominator * (-1)**((_den-1)//2) % _den

    if _num == _den - 1:    _num = -1
    _ret = Jacobi(_num, _den)

    return _ret

class Jacobi(Symbol):

    @property
    def nickname(a):
        return a._nickname

    @property
    def numerator(a):
        return a._numerator

    @property
    def denominator(a):
        return a._denominator

    def convert(self, kind):
        str_check(kind)

        if kind == 'Jacobi':
            return self
        elif kind == 'Legendre':
            from .NTLLegendre import Legendre
            _ret = Legendre(self._numerator, self._denominator)
            return _ret
        else:
            raise KeywordError('%s is an unknown type of symbol.' %kind)

    # Virtual properties.
    _nickname    = 'Jacobi'
    _numerator   = default_numerator
    _denominator = default_denominator

    # Virtual functions.
    eval = jacobi_eval
    simplify = jacobi_simplify
    reciprocate = jacobi_reciprocate

# if __name__ == '__main__':
#     j1 = Jacobi(2, 3)
#     j2 = Jacobi('2|3')
#     j3 = Jacobi(l1)

#     print(j1, j1.eval())
#     print(j2, j2.simplify())
#     print(j3, j3.reciprocate())
