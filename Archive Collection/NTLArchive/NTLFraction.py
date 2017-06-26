# -*- coding: utf-8 -*-

__all__  = ['Fraction']
nickname = 'Fraction'

import fractions
import math
import numbers
import operator
import sys

#連分數類
#基于分数類，增加转化、逼近等功能

from .NTLUtilities   import jsfloor, jsceil, jsround
from .NTLValidations import int_check

class Fraction:

    __all__ = ('number', 'fraction', 'convergent')

    def __init__(self, _numerator=0, _denominator=None):
        self.convergent = []

        if _denominator is None and _numerator is list:
            self.extract(cfList)
        else:
            self.number = fractions.Fraction(_numerator, _denominator)
        
        if not self.convergent:     self.expand()

    def __str__(self):
        return str(self.fraction)

    def __repr__(self):
        return repr(self.number)

    # @property
    # def numerator(a):
    #     return a.number.numerator

    # @property
    # def denominator(a):
    #     return a.number.denominator

    # @property
    # def number(a):
    #     return a.number

    # @property
    # def fraction(a):
    #     return a.fraction

    # @property
    # def convergent(a):
    #     return a.convergent

    def extract(self, cfList):
        p_1 = 1;    p_2 = 0
        q_1 = 0;    q_2 = 1
        for a_0 in cfList:
            p_1, p_2 = p_1 * a_0 + p_2, p_1
            q_1, q_2 = q_1 * a_0 + q_2, q_1
            self.convergent.append(fractions.Fraction(p_1, q_1))
        self.number = fractions.Fraction(p_1, q_1)

    def expand(self):
        x = self.number
        a = jsfloor(x)
        x -= a
        self.fraction = [a]

        p_1 = a;    p_2 = 1
        q_1 = 1;    q_2 = 0
        self.convergent.append(fractions.Fraction(a, 1))

        while x != 0:
            x = 1 / x
            a = jsfloor(x)
            x -= a
            self.fraction.append(a)

            p_1, p_2 = p_1 * a + p_2, p_1
            q_1, q_2 = q_1 * a + q_2, q_1
            self.convergent.append(fractions.Fraction(p_1, q_1))

    def convergent(self, level=None):
        if level is None:
            return self.number
        else:
            int_check()
            try:
                return self.convergent[level]
            except IndexError:
                return self.number

    def _operator_fallbacks(monomorphic_operator, fallback_operator):
        def forward(a, b):
            if sys.version_info[0] > 2:
                if isinstance(b, (int, Fraction)):
                    return monomorphic_operator(a, b)
                elif isinstance(b, float):
                    return fallback_operator(float(a), b)
                elif isinstance(b, complex):
                    return fallback_operator(complex(a), b)
                else:
                    return NotImplemented
            else:
                if isinstance(b, (int, long, Fraction)):
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
            if isinstance(a, number.Rational):
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
        return Fraction(a.number + b.number)

    __add__, __radd__ = _operator_fallbacks(_add, operator.add)

    def _sub(a, b):
        return Fraction(a.number - b.number)

    __sub__, __rsub__ = _operator_fallbacks(_sub, operator.sub)

    def _div(a, b):
        return Fraction(a.number / b.number)

    if sys.version_info[0] > 2:
        __truediv__, __rtruediv__ = _operator_fallbacks(_div, operator.truediv)
    else:
        __truediv__, __rtruediv__ = _operator_fallbacks(_div, operator.truediv)
        __div__, __rdiv__ = _operator_fallbacks(_div, operator.div)

    def __floordiv__(a, b):
        return Fraction(a.number // b.number)

    def __rfloordiv__(b, a):
        return Fraction(a.number // b.number)

    def __mod__(a, b):
        return Fraction(a.number % b.number)

    def __rmod__(b, a):
        return Fraction(a.number % b.number)

    def __pow__(a, b):
        return Fraction(a.number ** b.number)

    def __rpow__(b, a):
        return Fraction(a.number ** b.number)

    def __pos__(a):
        return Fraction(a.number)

    def __neg__(a):
        return Fraction(-a.number)

    def __abs__(a):
        return Fraction(abs(a.number))

    def __trunc__(a):
        return Fraction(trunc(a))

    def __hash__(self):
        return Fraction(hash(self.number))

    def __floor__(a):
        return Fraction(jsfloor(a.number))

    def __ceil__(a):
        return Fraction(jsceil(a.number))

    def __round__(a):
        return Fraction(jsround(a.number))

    def __eq__(a, b):
        return (a.number == b.number)

    def __lt__(a, b):
        return (a.number < b.number)

    def __gt__(a, b):
        return (a.number > b.number)

    def __le__(a, b):
        return (a.number <= b.number)

    def __ge__(a, b):
        return (a.number >= b.number)

    def __nonzero__(a):
        return (a.number != 0)

    # support for pickling, copy, and deepcopy

    def __reduce__(self):
        return (self.__class__, (str(self),))

    def __copy__(self):
        if type(self) == Fraction:
            return self     # I'm immutable; therefore I am my own clone
        return self.__class__(self.number)

    def __deepcopy__(self, memo):
        if type(self) == Fraction:
            return self     # My components are also immutable
        return self.__class__(self.number)

# if __name__ == '__mian__':
#     print('7700/2145 = ', end=' ')
#     rst_ = Fraction('7699/2145')
#     dst_ = Fraction(1, 2145)
#     print(rst_ + dst_)
