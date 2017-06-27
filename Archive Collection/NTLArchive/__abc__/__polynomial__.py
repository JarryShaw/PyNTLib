#-*- coding: utf-8 -*-

__all__ = ['ABCPolynomial']

import abc
import numbers
import re

#多項式基類
#Abstract Base Class for Polynomials

from NTLArchive.NTLExceptions  import DefinitionError
from NTLArchive.NTLUtilities   import jsstring, jsappend, jsupdate
from NTLArchive.NTLValidations import tuple_check, str_check, complex_check, int_check, basestring_check, notneg_check

ABCMeta = abc.ABCMeta
abstractmethod = abc.abstractmethod
abstractproperty = abc.abstractproperty

'''
POLYNOMIAL_FORMAT
    (+\-) coeficient (*) variable (^\**) exponent
'''

POLYNOMIAL_FORMAT = re.compile(r'''
    \A\s*                           # optional whitespace at the start, then
    (?P<sign>[-+]?)                 # an optional sign, then
    (?=\d)                          # lookahead for digit
    (?P<coe_>\d*)                   # coefficient
    (?:\*)                          # followed by an optional asterisk/multiplier, then
    (?=\D)                          # lookahead for non-digit/letter
    (?P<var_>\D*)                   # variable
    (?:(?:\^)?|(?:\*\*)?)           # followed by an optional caret or double asterisk, then
    (?=\d)                          # lookahead for digit
    (?P<exp_>\d*)                   # exponent
    \s*\Z                           # and optional whitespace to finish
''', re.VERBOSE | re.IGNORECASE)

class ABCPolynomial(object):

    __all__ = ['var', 'vec', 'df_var', 'nickname']
    __metaclass__ = ABCMeta

    # Not hashable
    __hash__ = None

    @abstractproperty
    def var(self):
        pass

    @abstractproperty
    def vec(self):
        pass

    @abstractproperty
    def df_var(self):
        pass

    @abstractproperty
    def nickname(self):
        pass

    @abstractmethod
    def eval(self, _var):
        pass

    @abstractmethod
    def mod(self, _var, _mod):
        pass

    @abstractmethod
    def _int(self):
        pass

    @abstractmethod
    def _der(self):
        pass

    @abstractmethod
    def _add(self):
        pass

    @abstractmethod
    def _sub(self):
        pass

    @abstractmethod
    def _mul(self):
        pass

    @abstractmethod
    def _div(self):
        pass

    @abstractmethod
    def _mod(self):
        pass

    @abstractmethod
    def convert(self, kind):
        pass

    # Check is types match.
    def has_sametype(self, other):
        return isinstance(other, self.__class__)

    # Set default variable.
    def default(self, _var):
        str_check(_var)
        self.df_var = _var

    def __new__(cls, other=None, *items):
        self = super(ABCPolynomial, cls).__new__(cls)

        if other is None:
            self.var = []
            self.vec = {}
            return self

        else:
            if isinstance(other, ABCPolynomial):
                self = other
                return self

            elif isinstance(other, numbers.Number):
                # Handle construction from numbers.
                self.var = ['x']
                self.vec = {'x': {0: other}}
                return self

            elif isinstance(other, jsstring):
                # Handle construction from strings.
                def read_item(item):
                    m = POLYNOMIAL_FORMAT.match(item)
                    if m is None:
                        raise DefinitionError('Invalid literal for symbols: %r' %other)

                    var = m.group('var_')
                    coe = int(m.group('coe_'))
                    exp = int(m.group('exp_'))

                    if m.group('sign') == '-':
                        coe = -coe

                    return var, exp, coe

                # Slice polynomial into items.
                other = other.replace('-', '+ -')
                items = other.split('+')

                var = [];   ec = {};    vec = {}
                for item in items:
                    _var, _exp, _coe = read_item(item)
                    var = jsappend(var, _var)
                    ec = jsupdate(ec, {_exp: _coe})
                    vec[_var] = jsupdate(vec[_var], ec)

            else:
                def read_poly(poly):
                    tuple_check(poly)
                    var = [];   ec = {};    vec = {}
                    _vec = list(poly); _vec.reverse()
                    _var = _vec.pop();  str_check(_var)
                    var.append(_var)

                    for _ec in _vec:
                        if len(_ec) != 2:
                            raise DefinitionError('Tuple of coeffients and corresponding exponents in need.')
                        
                        _exp = _ec[0];  complex_check(_exp)
                        _coe = _ec[1];  int_check(_coe);    notneg_check(_coe)
                        jsupdate(ec, {_exp: _coe})

                    vec[_var] = jsupdate(vec[_var], ec)
                    return var, vec

                var, vec = read_poly(other)

                for _vec in items:
                    _var, _vec = read_poly(_vec)
                    var = jsappend(var, _var);  vec = jsupdate(vec, _vec)

        self.var = var.sort()
        self.vec = vec
        return self

    def __call__(self, other=None, *items):
        if other is None:
            pass

        else:
            if isinstance(other, ABCPolynomial):
                self.var = jsappend(self.var, other.var)
                self.vec = jsupdate(self.vec, other.vec)

            elif isinstance(other, numbers.Number):
                # Handle construction from numbers.
                self.var = jsappend(self.var, [self.df_var])
                self.vec = jsupdate(self.vec, {self.df_var: {0: other}})

            elif isinstance(other, jsstring):
                # Handle construction from strings.
                def read_item(item):
                    m = POLYNOMIAL_FORMAT.match(item)
                    if m is None:
                        raise DefinitionError('Invalid literal for symbols: %r' %other)

                    var = m.group('var_')
                    coe = int(m.group('coe_'))
                    exp = int(m.group('exp_'))

                    if m.group('sign') == '-':
                        coe = -coe

                    return var, exp, coe

                # Slice polynomial into items.
                other = other.replace('-', '+ -')
                items = other.split('+')

                var = [];   ec = {};    vec = {}
                for item in items:
                    _var, _exp, _coe = read_item(item)
                    var = jsappend(var, _var)
                    ec = jsupdate(ec, {_exp: _coe})
                    vec[_var] = jsupdate(vec[_var], ec)

            else:
                def read_poly(poly):
                    tuple_check(poly)
                    var = [];   ec = {};    vec = {}
                    _vec = list(poly); _vec.reverse()
                    _var = _vec.pop();  str_check(_var)
                    var.append(_var)

                    for _ec in _vec:
                        if len(_ec) != 2:
                            raise DefinitionError('Tuple of coeffients and corresponding exponents in need.')
                        
                        _exp = _ec[0];  complex_check(_exp)
                        _coe = _ec[1];  int_check(_coe);    notneg_check(_coe)
                        jsupdate(ec, {_exp: _coe})

                    jsupdate(vec[_var], ec)
                    return var, vec

                var, vec = read_poly(other)

                for _vec in items:
                    _var, _vec = read_poly(_vec)
                    var = jsappend(var, _var);  vec = jsupdate(vec, _vec)

        self.var = jsappend(self.var, var).sort()
        self.vec = jsupdate(self.vec, vec)

    def __repr__(self):
        _ret = '%s(%s)'
        name = self.__class__.__name__
        _var = ', '.join(self.var)
        return _ret %(name, _var)

    def __str__(self):
        def str_ec(_ec, _var):
            if _ec == {}:   return '0'

            _str = ''
            _exp = sorted(list(_ec), reverse=True)

            for exp in _exp:
                _coe = _ec[exp]
                if _coe == 0:   continue

                if isinstance(_coe, complex):
                    _str += ' + '
                else:
                    _coe = abs(_coe)
                    _str += ' - ' if _coe < 0 else ' + '

                if exp == 0:
                    _str += str(_coe)
                else:
                    _str += '' if _coe == 1 else (str(_coe))
                    _str += _var
                    _str += '' if exp == 1 else ('^' + str(exp))

            if _str[1] == '+':  _str = _str[3:]
            if _str[1] == '-':  _str = '-' + _str[3:]
            return _str

        _str = ''
        for _var in self.var:
            _str += str_ec(self.vec[_var], _var)
        return _str

    # support for pickling, copy, and deepcopy

    def __reduce__(self):
        return (self.__class__, (str(self),))

    def __copy__(self):
        if type(self) == ABCPolynomial:
            return self     # I'm immutable; therefore I am my own clone
        return self.__class__(self.var, self.vec, self.nickname)

    def __deepcopy__(self, memo):
        if type(self) == ABCPolynomial:
            return self     # My components are also immutable
        return self.__class__(self.var, self.vec, self.nickname)
