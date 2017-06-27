#-*- coding: utf-8 -*-

__all__ = ['ABCSymbol']

import abc
import re

#Legendre及Jacobi符號基類
#Abstract Base Class for Legendre & Jacobi Symbols

from NTLArchive.NTLExceptions  import DefinitionError, ResidueError
from NTLArchive.NTLValidations import basestring_check, int_check

'''
SYMBOL_FORMAT
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

    @abstractproperty
    def numerator(self):
        pass

    @abstractproperty
    def denominator(self):
        pass

    @abstractproperty
    def nickname(self):
        pass

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

    def __new__(cls, _numerator, _denominator=None):
        self = super(ABCSymbol, cls).__new__(cls)

        if _denominator is None:
            if isinstance(_numerator, ABCSymbol):
                self = _numerator
                return self

            else:
                # Handle construction from strings.
                basestring_check(_numerator)
                    
                m = SYMBOL_FORMAT.match(_numerator)
                if m is None:
                    raise DefinitionError('Invalid literal for symbols: %r' %_numerator)
                
                numerator   = int(m.group('num'))
                denominator = int(m.group('den'))

                if m.group('sign') == '-':
                    numerator = -numerator

        else:
            int_check(_numerator, _denominator)
            if _denominator < 0:
                numerator = -_numerator;    denominator = -_denominator
            else:
                numerator = _numerator;     denominator = _denominator

        if denominator == 0:
            raise ResidueError('Symbol(%s, 0)' % numerator)

        self.numerator   = numerator
        self.denominator = denominator
        return self

    def __repr__(self):
        _ret = '%s(%d, %d)'
        name = self.__class__.__name__
        _num = self.numerator
        _den = self.denominator
        return _ret %(name, _num, _den)

    def __str__(self):
        return '%d | %d' %(self.numerator, self.denominator)

    def __eq__(self, other):
        _ret = (self.numerator == other.numerator) and \
               (self.denominator == other.denominator)
        return _ret

    def __ne__(self, other):
        return not self.__eq__(other)

    # support for pickling, copy, and deepcopy

    def __reduce__(self):
        return (self.__class__, (str(self),))

    def __copy__(self):
        if type(self) == ABCSymbol:
            return self     # I'm immutable; therefore I am my own clone
        return self.__class__(self.numerator, self.denominator, self.nickname)

    def __deepcopy__(self, memo):
        if type(self) == ABCSymbol:
            return self     # My components are also immutable
        return self.__class__(self.numerator, self.denominator, self.nickname)
