# -*- coding: utf-8 -*-


import fractions
import math
import numbers
import operator


# 連分數類
# 基于分数類，增加转化、逼近等功能


from .NTLGreatestCommonDivisor import greatestCommonDivisor
from .NTLUtilities             import jsceil, jsint, jsfloor, jsround, jsstring, ispy3
from .NTLValidations           import int_check


__all__  = ['Fraction']
nickname =  'Fraction'


'''Usage sample:

print('7700/2145 = ', end=' ')
rst_ = Fraction('7699/2145')
dst_ = Fraction(1, 2145)
print(rst_ + dst_)

'''


if ispy3:
    _PyHASH_MODULUS = fractions._PyHASH_MODULUS
    _PyHASH_INF     = fractions._PyHASH_INF


FractionBase = fractions.Fraction


class Fraction(FractionBase):

    __all__   = ['numerator', 'denominator', 'fraction', 'convergent', 'number']
    __slots__ = ('_numerator', '_denominator', '_fraction', '_convergent', '_number')

    ##########################################################################
    # Properties.
    ##########################################################################

    @property
    def number(a):
        return a._number

    @property
    def fraction(a):
        return a._fraction

    @property
    def convergent(a):
        return a._convergent

    ##########################################################################
    # Data models.
    ##########################################################################

    def __new__(cls, numerator=0, denominator=None):

        # Expand into continued fraction.
        def expand(fraction):
            x = fraction
            a = jsfloor(x)
            x -= a
            _fraction = [a]

            p_1 = a;    p_2 = 1
            q_1 = 1;    q_2 = 0
            _convergent = [FractionBase(a, 1)]

            while x != 0:
                x = 1 / x
                a = jsfloor(x)
                x -= a
                _fraction.append(a)

                p_1, p_2 = p_1 * a + p_2, p_1
                q_1, q_2 = q_1 * a + q_2, q_1
                _convergent.append(FractionBase(p_1, q_1))
            return _fraction, _convergent

        if denominator is None:
            if isinstance(numerator, Fraction):
                # Construct with Fraction instance.
                self = super(Fraction, cls).__new__(cls)
                self._fraction    = numerator._fraction
                self._convergent  = numerator._convergent
                self._number      = numerator._number
                self._numerator   = numerator._numerator
                self._denominator = numerator._denominator
                return self

            elif isinstance(numerator, list):
                # Contrcut with continued fraction.
                self = super(Fraction, cls).__new__(cls)

                # Extract original fraction.
                def extract(cfList):
                    _convergent = []
                    p_1 = 1;    p_2 = 0
                    q_1 = 0;    q_2 = 1
                    for a_0 in cfList:
                        p_1, p_2 = p_1 * a_0 + p_2, p_1
                        q_1, q_2 = q_1 * a_0 + q_2, q_1
                        _convergent.append(FractionBase(p_1, q_1))
                    _numerator = p_1;   _denominator = q_1
                    return _convergent, _numerator, _denominator

                self._fraction = numerator
                self._convergent, self._numerator, self._denominator = extract(self._fraction)
                self._number = FractionBase(self._numerator, self._denominator)
                return self

            else:
                self = super(Fraction, cls).__new__(cls, numerator, denominator)
                self._number = FractionBase(self._numerator, self._denominator)
                self._fraction, self._convergent = expand(self._number)
                return self

        else:
            self = super(Fraction, cls).__new__(cls, numerator, denominator)
            self._number = FractionBase(self._numerator, self._denominator)
            self._fraction, self._convergent = expand(self._number)
            return self

    # Get certain level of convergents.
    def __getitem__(self, level=None):
        int_check(level)

        if level is None:
            return self._number
        else:
            int_check()
            try:
                return self.convergent[level]
            except IndexError:
                return self._number

    ##########################################################################
    # Algebra.
    ##########################################################################

    def _operator_fallbacks(monomorphic_operator, fallback_operator):
        def forward(a, b):
            if isinstance(b, (jsint, Fraction)):
                return monomorphic_operator(a, b)
            elif isinstance(b, float):
                return fallback_operator(float(a), b)
            elif isinstance(b, complex):
                return fallback_operator(complex(a), b)
            else:
                return NotImplemented
        forward.__name__ = '__' + fallback_operator.__name__ + '__'
        forward.__doc__ = monomorphic_operator.__doc__

        def reverse(b, a):
            if isinstance(a, numbers.Rational):
                # Includes ints.
                return monomorphic_operator(a, b)
            elif isinstance(a, numbers.Real):
                return fallback_operator(float(a), float(b))
            elif isinstance(a, numbers.Complex):
                return fallback_operator(complex(a), complex(b))
            else:
                return NotImplemented
        reverse.__name__ = '__r' + fallback_operator.__name__ + '__'
        reverse.__doc__ = monomorphic_operator.__doc__

        return forward, reverse

    def _add(a, b):
        return Fraction(a._number + b._number)

    __add__, __radd__ = _operator_fallbacks(_add, operator.add)

    def _sub(a, b):
        return Fraction(a._number - b._number)

    __sub__, __rsub__ = _operator_fallbacks(_sub, operator.sub)

    def _mul(a, b):
        return Fraction(a._number * b._number)

    __mul__, __rmul__ = _operator_fallbacks(_mul, operator.mul)

    def _div(a, b):
        return Fraction(a._number / b._number)

    if ispy3:
        __truediv__, __rtruediv__ = _operator_fallbacks(_div, operator.truediv)
    else:
        __truediv__, __rtruediv__ = _operator_fallbacks(_div, operator.truediv)
        __div__, __rdiv__ = _operator_fallbacks(_div, operator.div)

    def __floordiv__(a, b):
        return Fraction(a._number // b._number)

    def __rfloordiv__(b, a):
        return Fraction(a._number // b._number)

    def __mod__(a, b):
        return Fraction(a._number % b._number)

    def __rmod__(b, a):
        return Fraction(a._number % b._number)

    def __pow__(a, b):
        return Fraction(a._number ** b._number)

    def __rpow__(b, a):
        return Fraction(a._number ** b._number)

    def __pos__(a):
        return Fraction(a._number)

    def __neg__(a):
        return Fraction(-a._number)

    def __abs__(a):
        return Fraction(abs(a._number))

    def __trunc__(a):
        return Fraction(trunc(a))

    def __hash__(self):
        return Fraction(hash(self._number))

    def __floor__(a):
        return Fraction(jsfloor(a._number))

    def __ceil__(a):
        return Fraction(jsceil(a._number))

    def __round__(a):
        return Fraction(jsround(a._number))

    def __eq__(a, b):
        return (a._number == b._number)

    def __lt__(a, b):
        return (a._number < b._number)

    def __gt__(a, b):
        return (a._number > b._number)

    def __le__(a, b):
        return (a._number <= b._number)

    def __ge__(a, b):
        return (a._number >= b._number)

    def __nonzero__(a):
        return (a._number != 0)
