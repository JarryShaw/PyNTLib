# -*- coding: utf-8 -*-


import abc
import re


# Legendre及Jacobi符號基類
# Abstract Base Class for Legendre & Jacobi Symbols


from ..NTLExceptions  import DefinitionError, ResidueError
from ..NTLValidations import basestring_check, int_check


__all__ = ['ABCSymbol']


'''SYMBOL_FORMAT:

(+\-) numerator (/\|) denominator
'''

SYMBOL_FORMAT = re.compile(r'''
    \A\s*                       # optional whitespace at the start, then
    (?P<sign>[-+]?)             # an optional sign, then
    (?=\d)                      # lookahead for digit
    (?P<num>\d*)                # numerator
    (?:[/|]?)                   # followed by a solidus or vertical line, then
    (?=\d)                      # lookahead for digit
    (?P<den>\d*)                # denominator
    \s*\Z                       # and optional whitespace to finish
''', re.VERBOSE | re.IGNORECASE)


ABCMeta = abc.ABCMeta
abstractmethod = abc.abstractmethod
abstractproperty = abc.abstractproperty


class ABCSymbol(object):

    __all__ = ['numerator', 'denominator', 'nickname']
    __metaclass__ = ABCMeta

    # Not hashable
    __hash__ = None

    ##########################################################################
    # Properties.
    ##########################################################################

    @abstractproperty
    def numerator(self):
        pass

    @abstractproperty
    def denominator(self):
        pass

    @abstractproperty
    def nickname(self):
        pass

    ##########################################################################
    # Methods.
    ##########################################################################

    @abstractmethod
    def eval(self):
        pass

    @abstractmethod
    def simplify(self):
        pass

    @abstractmethod
    def reciprocate(self):
        pass

    @abstractmethod
    def convert(self, kind):
        pass

    # Check is types match.
    def has_sametype(self, other):
        return isinstance(other, self.__class__)

    ##########################################################################
    # Data models.
    ##########################################################################

    def __new__(cls, numerator, denominator=None, **kwargs):
        self = super(ABCSymbol, cls).__new__(cls)

        if denominator is None:
            if isinstance(numerator, ABCSymbol):
                self = numerator
                return self

            else:
                # Handle construction from strings.
                basestring_check(numerator)

                m = SYMBOL_FORMAT.match(numerator)
                if m is None:
                    raise DefinitionError('Invalid literal for symbols: %r' % numerator)

                _numerator   = int(m.group('num'))
                _denominator = int(m.group('den'))

                if m.group('sign') == '-':
                    _numerator = -_numerator

        else:
            int_check(numerator, denominator)
            if denominator < 0:
                _numerator = -numerator;    _denominator = -denominator
            else:
                _numerator = numerator;     _denominator = denominator

        if _denominator == 0:
            raise ResidueError('Symbol(%s, 0)' % _numerator)

        self._numerator   = _numerator
        self._denominator = _denominator
        return self

    def __repr__(self):
        _ret = '%s(%d, %d)'
        name = self.__class__.__name__
        _num = self._numerator
        _den = self._denominator
        return _ret % (name, _num, _den)

    def __str__(self):
        return '%d | %d' % (self._numerator, self._denominator)

    ##########################################################################
    # Utilities.
    ##########################################################################

    def __eq__(self, other):
        _ret = (self._numerator == other._numerator) and \
               (self._denominator == other._denominator)
        return _ret

    def __ne__(self, other):
        return not self.__eq__(other)

    # support for pickling, copy, and deepcopy

    def __reduce__(self):
        return (self.__class__, (str(self),))

    def __copy__(self):
        if type(self) == ABCSymbol:
            return self     # I'm immutable; therefore I am my own clone
        return self.__class__(self._numerator, self._denominator, self._nickname)

    def __deepcopy__(self, memo):
        if type(self) == ABCSymbol:
            return self     # My components are also immutable
        return self.__class__(self._numerator, self._denominator, self._nickname)
