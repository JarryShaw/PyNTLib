# -*- coding: utf-8 -*-


from .__abc__ import __symbol__


# Legendre符號類
# 具備化簡、求值等基本功能


from .NTLExceptions           import DefinitionError, KeywordError
from .NTLPrimeFactorisation   import primeFactorisation
from .NTLRepetiveSquareModulo import repetiveSquareModulo
from .NTLTrivialDivision      import trivialDivision
from .NTLUtilities            import jssign
from .NTLValidations          import bool_check, prime_check, str_check

# from .NTLJacobi import Jacobi


__all__  = ['Legendre',
            '_default_numerator', '_default_denominator',
            '_legendre_eval', '_legendre_simplify', '_legendre_reciprocate']
nickname =  'Legendre'


'''Usage sample:

l1 = Legendre(2, 3)
l2 = Legendre('2|3')
l3 = Legendre(l1)

print(l1, l1.eval())
print(l2, l2.simplify())
print(l3, l3.reciprocate())

'''


# Abstract base class of symbol.
Symbol = __symbol__.ABCSymbol


# Legendre default form.
_default_numerator   = 1
_default_denominator = 2


# 計算Legendre符號的值
def _legendre_eval(legendre):
    _ret = _legendre_simplify(legendre)

    a = _ret._numerator
    p = _ret._denominator

    if a == 1:      return 1
    if a == - 1:    return (-1)**((p-1)//2)
    if a == 2:      return (-1)**((p**2-1)//8)

    r = jssign(a)
    for _a in primeFactorisation(abs(a)):
        r *= Legendre(_a, p).eval()

    return r if r != p-1 else -1


#化簡Legendre符號
def _legendre_simplify(legendre):
    _ret = legendre
    _ret._numerator %= _ret._denominator

    while abs(_ret._numerator) not in [0, 1, 2]\
            and trivialDivision(abs(_ret._numerator)):
        _num = _ret._numerator
        _den = _ret._denominator

        if _den > abs(_num):
            _ret = _legendre_reciprocate(_ret)

    return _ret


# 二次互反律
def _legendre_reciprocate(legendre):
    _den = legendre._numerator
    _num = legendre._denominator * (-1)**((_den-1)//2) % _den

    if _num == _den - 1:    _num = -1
    _ret = Legendre(_num, _den)

    return _ret


class Legendre(Symbol):

    ##########################################################################
    # Properties.
    ##########################################################################

    @property
    def nickname(a):
        return a._nickname

    @property
    def numerator(a):
        return a._numerator

    @property
    def denominator(a):
        return a._denominator

    ##########################################################################
    # Data models.
    ##########################################################################

    def __init__(self, numerator, denominator=None, **kwargs):
        trust = False
        for kw in kwargs:
            if kw != 'trust':
                raise KeywordError('Keyword \'%s\' is not defined.' % kw)
            else:
                trust = kwargs[kw];     bool_check(trust)

        prime_check(trust, self._denominator)

    def __call__(self):
        a = self._numerator
        p = self._denominator
        a %= p

        if a == 1:      return 1
        if a == p - 1:  return (-1)**((p-1)//2)
        if a == 2:      return (-1)**((p**2-1)//8)

        mod = repetiveSquareModulo(a, ((p-1)//2), p)
        return mod if mod != p-1 else -1

    ##########################################################################
    # Methods.
    ##########################################################################

    def convert(self, kind=None):
        if kind is None:
            return self

        else:
            str_check(kind)

            if kind == 'Legendre':
                return self
            elif kind == 'Jacobi':
                from .NTLJacobi import Jacobi
                _ret = Jacobi(self._numerator, self._denominator)
                return _ret
            else:
                raise KeywordError('%s is an unknown type of symbol.' % kind)

    # Virtual properties.
    _nickname    = 'Legendre'
    _numerator   = _default_numerator
    _denominator = _default_denominator

    # Virtual functions.
    eval = _legendre_eval
    simplify = _legendre_simplify
    reciprocate = _legendre_reciprocate
