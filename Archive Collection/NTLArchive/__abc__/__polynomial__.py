#-*- coding: utf-8 -*-

__all__ = ['ABCPolynomial']

import abc
import numbers
import operator
import re
import sys

#多項式基類
#Abstract Base Class for Polynomials

from NTLArchive.NTLExceptions  import DefinitionError, KeywordError
from NTLArchive.NTLUtilities   import jsstring, jsappend, jsupdate, jsint
from NTLArchive.NTLValidations import tuple_check, str_check, number_check, int_check, basestring_check, notneg_check, pos_check, dict_check

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
    (?=[a-z_]?)                     # lookahead for non-digit/letter
    (?P<var_>[a-z_]?+)              # variable
    (?:\^)                          # followed by an optional caret, then
    (?=\d)                          # lookahead for digit
    (?P<exp_>\d*)                   # exponent
    \s*\Z                           # and optional whitespace to finish
''', re.VERBOSE | re.IGNORECASE)

class ABCPolynomial(object):

    __all__ = ['var', 'vec', 'dfvar', 'nickname']
    __metaclass__ = ABCMeta

    # Not hashable
    __hash__ = None

    @abstractproperty
    def var(a):
        pass

    @abstractproperty
    def vec(a):
        pass

    @abstractproperty
    def dfvar(a):
        pass

    @abstractproperty
    def nickname(a):
        pass

    @abstractmethod
    def eval(self, *vars):
        pass

    @abstractmethod
    def mod(self, *vars, **mods):
        pass

    @abstractmethod
    def convert(self, kind):
        pass

    def _none_check(self, _dict):
        if _dict == {}:
            return True

        for _key in _dict:
            if _dict[_key] != 0:    return False
        return True

    def _read_item(self, item):
        m = POLYNOMIAL_FORMAT.match(item)
        if m is None:
            raise DefinitionError('Invalid literal for symbols: %r' %item)

        var = m.group('var_')
        coe = int(m.group('coe_'))
        exp = int(m.group('exp_'))

        if m.group('sign') == '-':
            coe = -coe

        return var, exp, coe

    def _read_poly(self, poly):
        # TUPLE_FORMAT
        #     (['variable',] (expnonet, coefficient), ...)

        tuple_check(poly)
        var = [];   ec = {};    vec = {}
        if isinstance(poly[0], str):
            _vec = list(poly);  _vec.reverse()
            _var = _vec.pop();  var.append(_var)
        else:
            _var = self._dfvar
            _vec = list(poly);  var.append(_var)

        for _ec in _vec:
            tuple_check(_ec)
            if len(_ec) != 2:
                raise DefinitionError('Tuple of coeffients and corresponding exponents in need.')
            
            _exp = _ec[0];  int_check(_exp);    notneg_check(_exp)
            _coe = _ec[1];  number_check(_coe)
            jsupdate(ec, {_exp: _coe})

        if _var in vec:
            vec[_var] = jsupdate(vec[_var], ec)
        else:
            vec[_var] = ec
        return var, vec

    def _read_dict(self, vec):
        # DICT_FORMAT
        #     {'variable': {exponent: coefficient, ...}, ...}

        _var = [];      _vec = {}
        for var in vec:
            str_check(var);             dict_check(vec[var])
            for exp in vec[var]:
                int_check(exp);         number_check(vec[var][exp])
            _var.append(var)
        _vec.update(vec)
        return _var, _vec

    def _read_vars(self, *vars):
        _var = {}
        for var in vars:
            if isinstance(var, numbers.Number):
                if len(self._var) == 0:
                    _var[self._dfvar] = var
                elif len(self._var) == 1:
                    _var[self._var[0]] = var
                else:
                    raise DefinitionError('Tuple of variable name and corresponding value in need.')
            else:
                tuple_check(var)
                if len(var) != 2:
                    raise DefinitionError('Tuple of variable name and corresponding value in need.')
                
                str_check(var[0]);  number_check(var[1])
                if var[0] in _var:
                    raise DefinitionError('Only one set of variable name and corresponding value taken.')
                elif var[0] not in self._var:
                    raise KeywordError('Variable \'%s\' is not found.' %var[0])
                else:
                    _var[var[0]] = var[1]
        
        if len(_var) != len(self._var):
            for var in _var:
                self._var.remove(var)
            var = '\', \''.join(self._var)
            raise KeywordError('Variable \'%s\' should be assigned.' %var)
        
        return _var

    def _read_mods(self, **mods):
        _mod = None
        set_flag = False
        for mod in mods:
            if mod == 'mod':
                if set_flag:
                    raise DefinitionError('Only one modulo taken.')
                else:
                    int_check(mod);     pos_check(mod)
                    _mod = mod;         set_flag = True;    break
            else:
                raise KeywordError('Keyword \'%s\' is not defined.' %mod)
        return _mod

    # Check is types match.
    def has_sametype(self, other):
        return isinstance(other, self.__class__)

    # Set default variable.
    def default(self, var=None):
        if var is None:
            self._dfvar = _dfvar
        else:
            str_check(var)
            self._dfvar = var

    def __new__(cls, other=None, *items):
        self = super(ABCPolynomial, cls).__new__(cls)

        # Default variable
        self._dfvar = 'x'

        if other is None:
            self._var = []
            self._vec = {}
            return self

        else:
            if isinstance(other, ABCPolynomial):
                self = other
                return self

            elif isinstance(other, numbers.Number):
                # Handle construction from numbers.
                self._var = [self._dfvar]
                self._vec = {self._dfvar: {0: other}}
                return self

            elif isinstance(other, jsstring):
                # Handle construction from strings.

                # Slice polynomial into items.
                other = other.replace('-', '+ -')
                items = other.split('+')

                var = [];   ec = {};    vec = {}
                for item in items:
                    _var, _exp, _coe = self._read_item(item)
                    var = jsappend(var, _var)
                    ec = jsupdate(ec, {_exp: _coe})
                    vec[_var] = jsupdate(vec[_var], ec)

            elif isinstance(other, dict):
                # Handle construction from dictionaries.
                var, vec = self._read_dict(other)

            else:
                # Handle construction from tuples.
                var, vec = self._read_poly(other)

                for _vec in items:
                    _var, _vec = self._read_poly(_vec)
                    var = jsappend(var, _var);  vec = jsupdate(vec, _vec)

        for key in vec:
            if self._none_check(vec[key]):  var.remove(key);    del vec[key]
        
        self._var = sorted(var)
        self._vec = vec
        return self

    def __call__(self, *vars, **mods):
        _mod = self._read_mods(**mods)
        _var = self._read_vars(*vars)

        if _mod is None:
            return self._eval(_var)
        else:
            return self._mod(_var, _mod)

    def __repr__(self):
        _ret = '%s(%s)'
        name = self.__class__.__name__
        _var = ', '.join(self._var)
        return _ret %(name, _var)

    def __str__(self):
        def str_ec(_ec, _var):
            if _ec == {}:   return ''

            _str = ''
            _exp = sorted(list(_ec), reverse=True)

            for exp in _exp:
                _coe = _ec[exp]
                if _coe == 0:   continue

                if isinstance(_coe, complex):
                    _str += ' + '
                else:
                    _str += ' - ' if _coe < 0 else ' + '
                    _coe = abs(_coe)

                if exp == 0:
                    _str += str(_coe)
                else:
                    _str += '' if _coe == 1 else (str(_coe))
                    _str += _var
                    _str += '' if exp == 1 else ('^' + str(exp))

            if _str[1] == '-':  _str = '-' + _str[3:]
            if _str[1] == '+':  _str = _str[3:]
            return _str

        if self._var == []:
            _str = ''
        else:
            _str = []
            for _var in self._var:
                _str.append(str_ec(self._vec[_var], _var))
            _str = ' + '.join(_str)
        return _str if _str != '' else '0'

    @abstractmethod
    def _add(a, b):
        pass

    @abstractmethod
    def radd(a, b):
        pass

    @abstractmethod
    def _sub(a, b):
        pass

    @abstractmethod
    def rsub(a, b):
        pass

    @abstractmethod
    def _mul(a, b):
        pass

    @abstractmethod
    def rmul(a, b):
        pass

    @abstractmethod
    def _div(a, b):
        pass

    @abstractmethod
    def rdiv(a, b):
        pass

    @abstractmethod
    def _divmod(a, b):
        pass

    @abstractmethod
    def rdivmod(a, b):
        pass

    @abstractmethod
    def _floordiv(a, b):
        pass

    @abstractmethod
    def rfloordiv(a, b):
        pass

    @abstractmethod
    def _mod(a, b):
        pass

    @abstractmethod
    def rmod(a, b):
        pass

    @abstractmethod
    def _pow(a, exp, mod=None):
        pass

    @abstractmethod
    def _neg(a):
        pass

    @abstractmethod
    def _pos(a):
        pass

    @abstractmethod
    def _abs(a):
        pass

    @abstractmethod
    def _int(self):
        pass

    @abstractmethod
    def _der(self):
        pass

    polyder = _der
    polyint = _int
