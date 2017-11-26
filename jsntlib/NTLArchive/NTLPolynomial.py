# -*- coding: utf-8 -*-


from .__abc__ import __polynomial__


import copy


# 複數域多項式類
# 具備基本運算的複數域多項式實現


from .NTLExceptions           import ComplexError, DefinitionError, ResidueError, PolyError
from .NTLRepetiveSquareModulo import repetiveSquareModulo
from .NTLUtilities            import jsappend, jsint, jsitems, jskeys, \
                                     jsmaxint, jsrange, jsupdate, ispy3
from .NTLValidations          import int_check, number_check, tuple_check


__all__  = ['Polynomial']
nickname =  'Polynomial'


'''Usage sample:

a = complex(1,3)
poly_1 = Polynomial(('a', (1,3), (3,4), (2,2), (34,a)))
poly_2 = Polynomial((1,0), (4,-4), (2,3), (0,1))
poly_3 = Polynomial(((2,-1), (0,1)))
poly_4 = Polynomial(((0,1)))
poly_5 = Polynomial(
    ((20140515,20140515), (201405,201495), (2014,2014), (8,8), (6,1), (3,4), (1,1), (0,1)))
poly_6 = Polynomial(((7,1), (1,-1)))
poly_7 = poly_1 / poly_2

print(poly_1[:])
print(poly_2)
print(poly_7)

'''


# Abstract base class of polynomial.
PolyBase = __polynomial__.ABCPolynomial


class Polynomial(PolyBase):

    __all__   = ['iscomplex', 'isinteger', 'ismultivar', 'var', 'vector', 'dfvar', 'nickname']
    __slots__ = ('_cflag', '_iflag', '_vflag', '_var', '_vec', '_dfvar', '_nickname')

    ##########################################################################
    # Properties.
    ##########################################################################

    @property
    def iscomplex(a):
        return a._cflag

    @property
    def isinteger(a):
        return a._iflag

    @property
    def ismultivar(a):
        return a._vflag

    @property
    def var(a):
        return a._var

    @property
    def vector(a):
        return a._vec

    @property
    def dfvar(a):
        return a._dfvar

    @property
    def nickname(a):
        return a._nickname

    ##########################################################################
    # Methods.
    ##########################################################################

    # 求取self的值
    def eval(self, *vars):
        # 生成可計算的多項式
        def make_eval(_dict):
            poly = []
            for exp in _dict:
                item = str(_dict[exp]) + '*x**' + str(exp)
                poly.append(item)
            _eval = ' + '.join(poly)
            return _eval

        _rst = 0;   _var = self._read_vars(*vars)
        if _var is None:        return 0
        if self._var == []:     return 0
        for var in _var:
            poly = make_eval(self._vec[var])
            _rst += (lambda x: eval(poly))(_var[var])
        return _rst

    # 用模重複平方法求self取模後的值
    def mod(self, *vars, **mods):
        _rst = 0
        _mod = self._read_mods(**mods)
        if _mod is None:        return self.eval(*vars)
        _var = self._read_vars(*vars)
        if _var is None:        return 0
        if self._var == []:     return 0
        for var in _var:
            for exp in self._vec[var]:
                _coe = self._vec[var][exp] % _mod
                base = _var[var]
                _tmp = repetiveSquareModulo(base, exp, _mod)
                _rst += (_coe * _tmp) % _mod
        _rst %= _mod
        return _rst

    ##########################################################################
    # Utilities.
    ##########################################################################

    def _update_state(self):
        for var in self._var:
            for exp in jskeys(self._vec[var]):
                if self._vec[var][exp] == 0:    del self._vec[var][exp]
            if self._none_check(self._vec[var]):
                self._var.remove(var);          del self._vec[var]

        self._var.sort()
        self._vflag = True if len(self._var) > 1 else False

        for var in self._var:
            if self._complex_check(self._vec[var]):
                self._cflag = True;         break
        else:
            self._cflag = False

        if self._cflag:
            self._iflag = False
        else:
            for var in self._var:
                if not self._int_check(self._vec[var]):
                    self._iflag = False;    break
            else:
                self._iflag = True

        self._var = self._var or [self._dfvar]
        self._vec = self._vec or {self._dfvar: {0: 0}}

    ##########################################################################
    # Data models.
    ##########################################################################

    def __init__(self, other=None, *items, **kwargs):
        self._nickname = 'poly'
        self._update_state()

    # 返回最高次項的次冪加一
    def __len__(self):
        if self._vflag:
            raise PolyError('Multi-variable polynomial has no len().')
        else:
            return (max(self._vec[self._var[0]]) + 1)

    # 返回key次項的係數或關於key變量的多項式
    def __getitem__(self, key):
        if isinstance(key, str):
            if key in self._var:
                vec = {key: self._vec[key]}
                item = Polynomial(vec)
                item._dfvar = self._dfvar
            else:
                item = Polynomial()
            return item

        elif isinstance(key, slice):
            return self.__getslice__(key.start, key.stop, key.step)

        else:
            int_check(key)
            if ispy3:
                if key < 0:     key += len(self)

            if self._vflag:
                raise PolyError('Multi-variable polynomial has no attribute \'__getitem__\'.')
            else:
                try:
                    return self._vec[self._var[0]][key]
                except KeyError:
                    return 0

    # 修改key次項的係數或關於key變量的項為value
    def __setitem__(self, key, value):
        if isinstance(key, str):
            tuple_check(value);     _ec = {}
            for item in value:
                tuple_check()
                if len(item) != 2:
                    raise DefinitionError(
                        'Tuple of coeffients and corresponding exponents in need.')
                _ec[item[0]] = item[1]

            jsappend(self._var, key)
            self._vec[key] = _ec

        elif isinstance(key, slice):
            self.__setslice__(key.start, key.stop, key.step, value)

        else:
            int_check(key);         number_check(value)
            if ispy3:
                    if key < 0:     key += len(self)

            if self._vflag:
                raise PolyError('Multi-variable polynomial does not support item assignment.')

            if key in self._vec[self._var[0]] and value == 0:
                del self._vec[self._var[0]][key]
            else:
                self._vec[self._var[0]][key] = value

        self._update_state()

    # 刪去key次項
    def __delitem__(self, key):
        if isinstance(key, str):
            if key in self._var:
                self._var.remove(key)
                del self._vec[key]

        elif isinstance(key, slice):
            self.__delslice__(key.start, key.stop, key.step)

        else:
            int_check(key)

            if self._vflag:
                raise PolyError('Multi-variable polynomial does not support item deletion.')

            try:
                del self._vec[self._var[0]][key]
            except KeyError:
                pass

        self._update_state()

    # 判斷一多項式是否含於多項式中
    def __contains__(self, poly):
        if isinstance(poly, Polynomial):
            if (poly._var in self._var):
                for var in poly._var:
                    for key in poly._vec[var]:
                        try:
                            if poly._vec[var][key] == self._vec[var][key]:
                                continue
                            else:
                                return False
                        except KeyError:
                            return False
            else:
                return False
        else:
            return (Polynomial(poly) in self)

    '''
    特別注意：
    1. 當下標值（key\i&j）小於零時，系統自動調用__len__()函數，並自增轉化為正數下標，即 key += len；
    2. 若下標缺省，起始地址模認為0，而終止地址將被模認為最大整型數，即sys.maxint=9223372036854775807。
    '''

    # 返回i至j-1次項的多項式
    def __getslice__(self, i, j, k=None):
        if i is None:   i = 0
        if j is None:   j = len(self)
        if k is None:   k = 1

        int_check(i, j, k)

        if self._vflag:
            raise PolyError('Multi-variable polynomial has no attribute \'__getitem__\'.')

        if j == jsmaxint:   j = len(self)

        _list = [self._var[0]]
        for ptr in jsrange(i, j, k):
            try:
                _list.append((ptr, self._vec[self._var[0]][ptr]))
            except KeyError:
                pass

        poly = Polynomial(tuple(_list))
        return poly

    # 修改i至j-1次項的多項式
    def __setslice__(self, i, j, k, coe=None):
        if coe is None:
            if i is None:   i = 0
            if j is None:   j = len(self)

            int_check(i, j);     tuple_check(k)

            if self._vflag:
                raise PolyError('Multi-variable polynomial does not support item assignment.')

            coe = k;    j = i + len(coe)
            for ptr in jsrange(i, j):
                if ptr in self._vec[self._var[0]] and coe[ptr-i] == 0:
                    del self._vec[self._var[0]][ptr]
                else:
                    self._vec[self._var[0]][ptr] = coe[ptr-i]

            self._update_state()
        else:
            if i is None:   i = 0
            if j is None:   j = len(self)
            if k is None:   k = 1

            int_check(i, j, k);     tuple_check(coe)

            if self._vflag:
                raise PolyError('Multi-variable polynomial does not support item assignment.')

            j = i + len(coe) * k;   ctr = -1
            for ptr in jsrange(i, j, k):
                ctr += 1
                if ptr in self._vec[self._var[0]] and coe[ctr] == 0:
                    del self._vec[self._var[0]][ptr]
                else:
                    self._vec[self._var[0]][ptr] = coe[ctr]

            self._update_state()

    # 刪除i至j-1次項的多項式
    def __delslice__(self, i, j, k=None):
        if i is None:   i = 0
        if j is None:   j = len(self)
        if k is None:   k = 1

        int_check(i, j, k)

        if self._vflag:
            raise PolyError('Multi-variable polynomial does not support item deletion.')

        if j == jsmaxint:   j = len(self)

        for ptr in range(i, j, k):
            try:
                del self._vec[self._var[0]][ptr]
            except KeyError:
                pass

        self._update_state()

    ##########################################################################
    # Algebra.
    ##########################################################################

    # 求取_sum = self + poly
    def _add(self, poly):
        if isinstance(poly, Polynomial):
            _sum = copy.deepcopy(self)
            _sum._var = jsappend(_sum._var, poly._var)
            _sum._vec = jsupdate(self._vec, poly._vec)
            _sum._update_state()
        else:
            _sum = self + Polynomial(poly)
        return _sum

    # 求取rsum = poly + self
    def radd(self, poly):
        rsum = poly + self
        return rsum

    __add__  = _add
    __radd__ = radd

    # 求取_dif = self - poly
    def _sub(self, poly):
        if isinstance(poly, Polynomial):
            _dif = copy.deepcopy(self);     _poly = -poly
            _dif._var = jsappend(_dif._var, poly._var)
            _dif._vec = jsupdate(self._vec, _poly._vec)
            _dif._update_state()
        else:
            _dif = self - Polynomial(poly)

        return _dif

    # 求取rdif = poly - self
    def rsub(self, poly):
        rdif = poly - self
        return rdif

    __sub__  = _sub
    __rsub__ = rsub

    # 求取_pro = self * poly
    def _mul(self, poly):
        if isinstance(poly, Polynomial):
            if self._vflag:
                raise PolyError('Multi-variable polynomial does not support multiplication.')
            else:
                if self._var == poly._var:
                    _pro = copy.deepcopy(self)
                    vec = {};   _ec = {}
                    for exp_a in self._vec[self._var[0]]:
                        for exp_b in poly._vec[poly._var[0]]:
                            exp = exp_a + exp_b
                            coe = self._vec[self._var[0]][exp_a] * poly._vec[poly._var[0]][exp_b]
                            _ec[exp] = coe
                    vec[self._var[0]] = _ec
                    _pro = Polynomial(vec)
                else:
                    raise PolyError('No support for multi-variable multiplication.')
        else:
            _pro = self * Polynomial(poly)
        return _pro

    # 求取rpro = poly * self
    def rmul(self, poly):
        rpro = poly * self
        return rpro

    __mul__  = _mul
    __rmul__ = rmul

    # 求取_quo = self / poly
    def _div(self, poly):
        if poly == 1:
            return self
        if poly == 0:
            raise ResidueError('integer division or modulo by zero')
        
        if ispy3 and self._iflag and poly._iflag:
            _quo = self // poly
            return _quo

        if isinstance(poly, Polynomial):
            if self._vflag:
                raise PolyError('Multi-variable polynomial does not support division.')
            else:
                if self._var == poly._var:
                    _var = self._var[0];    _vec = {_var: {}}
                    _did = copy.deepcopy(poly)
                    _rem = copy.deepcopy(self)

                    # 獲取被除式的最高次數
                    a_expmax = max(self._vec[_var])
                    # 獲取除式的指數列（降序）
                    b_exp = sorted(jskeys(_did._vec[_var]), reverse=True)

                    # 若被除式最高次冪小於除式最高次冪則終止迭代
                    while a_expmax >= b_exp[0]:
                        # 計算商式的係數，即當前被除式最高次冪項係數與除式最高次冪的項係數的商值
                        quo_coe = _rem._vec[_var][a_expmax] / _did._vec[_var][b_exp[0]]
                        # 計算商式的次冪，即當前被除式最高次冪與除式最高次冪的差值
                        quo_exp = a_expmax - b_exp[0]
                        # 將結果添入商式多項式
                        _vec[_var][quo_exp] = quo_coe

                        # 更新被除式係數及次冪狀態
                        for exp in b_exp:
                            rem_exp = exp + quo_exp
                            rem_coe = _did._vec[_var][exp] * quo_coe
                            try:
                                _rem._vec[_var][rem_exp] -= rem_coe
                            except KeyError:
                                _rem._vec[_var][rem_exp] = -rem_coe
                        _rem._update_state()

                        # 更新被除式的最高次數
                        try:
                            a_expmax = max(_rem._vec[_var])
                        except ValueError:
                            break

                    _quo = Polynomial(_vec)
                    return _quo
                else:
                    raise PolyError('No support for multi-variable division.')
        else:
            _quo = self / Polynomial(poly)
            return _quo

    # 求取rquo = poly / self
    def rdiv(self, poly):
        rquo = poly / self
        return rquo

    __truediv__  = _div
    __rtruediv__ = rdiv

    if not ispy3:
        __div__  = _div
        __rdiv__ = rdiv

    # 求取(_quo, _rem) = divmod(self, poly)
    def _divmod(self, poly):
        if isinstance(poly, Polynomial):
            if self._vflag:
                raise PolyError('Multi-variable polynomial does not support division & modulo.')
            else:
                if poly == 1:
                    return self, 0
                if poly == 0:
                    raise ResidueError('integer division or modulo by zero')
                
                if self._var == poly._var:
                    _var = self._var[0];    _vec = {_var: {}}
                    _did = copy.deepcopy(poly)
                    _rem = copy.deepcopy(self)

                    # 獲取被除式的最高次數
                    a_expmax = max(self._vec[_var])
                    # 獲取除式的指數列（降序）
                    b_exp = sorted(jskeys(_did._vec[_var]), reverse=True)

                    # 若除式最高次冪的係數不為1，則需化簡
                    if _did._vec[_var][b_exp[0]] != 1:
                        _coe = _did._vec[_var][b_exp[0]]

                        if self._vec[_var][a_expmax] % _coe == 0:
                            _mul = self._vec[_var][a_expmax] // _coe
                            if self == _did * _mul:
                                _quo = Polynomial(_mul)
                                _rem = Polynomial()
                                return _quo, _rem

                        # 判斷除式是否可化簡
                        for exp in b_exp:
                            if _did._vec[_var][exp] % _coe != 0:
                                _quo = Polynomial()
                                _rem = copy.deepcopy(self)
                                return _quo, _rem
                            else:
                                _did._vec[_var][exp] //= _coe

                        # 判斷被除式是否可化簡
                        for key in self._vec[_var]:
                            if self._vec[_var][key] % _coe != 0:
                                _quo = Polynomial()
                                _rem = copy.deepcopy(self)
                                return _quo, _rem
                            else:
                                _rem._vec[_var][key] //= _coe

                    # 若被除式最高次冪小於除式最高次冪則終止迭代
                    while a_expmax >= b_exp[0]:
                        # 計算商式的係數，即當前被除式最高次冪項係數
                        quo_coe = _rem._vec[_var][a_expmax]
                        # 計算商式的次冪，即當前被除式最高次冪與除式最高次冪的差值
                        quo_exp = a_expmax - b_exp[0]
                        # 將結果添入商式多項式
                        _vec[_var][quo_exp] = quo_coe

                        # 更新被除式係數及次冪狀態
                        for exp in b_exp:
                            rem_exp = exp + quo_exp
                            rem_coe = _did._vec[_var][exp] * quo_coe
                            try:
                                _rem._vec[_var][rem_exp] -= rem_coe
                            except KeyError:
                                _rem._vec[_var][rem_exp] = -rem_coe
                        _rem._update_state()

                        # 更新被除式的最高次數
                        try:
                            a_expmax = max(_rem._vec[_var])
                        except (ValueError, KeyError):
                            break
                    _quo = Polynomial(_vec)
                    return _quo, _rem
                else:
                    raise PolyError('No support for multi-variable division & modulo.')
        else:
            _quo, _rem = self._divmod(Polynomial(poly))
            return _quo, _rem

    # 求取(_quo, _rem) = divmod(poly, self)
    def rdivmod(self, poly):
        (_quo, _rem) = divmod(poly, self)
        return _quo, _rem

    __divmod__  = _divmod
    __rdivmod__ = rdivmod

    # 求取_quo = self // poly
    def _floordiv(self, poly):
        _quo = self._divmod(poly)[0]
        return _quo

    # 求取rquo = poly // self
    def rfloordiv(self, poly):
        rquo = poly // self
        return rquo

    __floordiv__  = _floordiv
    __rfloordiv__ = rfloordiv

    # 求取_rem = self % poly
    def _mod(self, poly):
        _rem = self._divmod(poly)[1]
        return _rem

    # 求取rrem = poly % self
    def rmod(self, poly):
        rrem = poly % self
        return rrem

    __mod__  = _mod
    __rmod__ = rmod

    # 求取_pow = pow(self, exp[, mod])
    def _pow(self, exp, mod=None):
        int_check(exp);     _pow = copy.deepcopy(self)
        for ctr in jsrange(1, exp):        _pow *= _pow
        if mod is not None: int_check(mod); _pow %= _mod
        return _pow

    __pow__  = _pow

    # 求取_neg = -self
    def _neg(self):
        _neg = copy.deepcopy(self)
        for var in _neg._vec:
            for exp in _neg._vec[var]:
                _neg._vec[var][exp] = -_neg._vec[var][exp]
        return _neg

    # 求取_pos = +self
    def _pos(self):
        _pos = copy.deepcopy(self)
        return _pos

    # 求取_abs = abs(self)
    def _abs(self):
        _abs = copy.deepcopy(self)
        for var in _abs._vec:
            for exp in _abs._vec[var]:
                _neg._vec[var][exp] = abs(_neg._vec[var][exp])
        return _abs

    __neg__ = _neg
    __pos__ = _pos
    __abs__ = _abs

    # 求取self的導式
    def _der(self):
        vec = {};   _ec = {}
        for var in self._vec:
            for exp in self._vec[var]:
                if exp:
                    _exp = exp - 1
                    _coe = self._vec[var][exp] * exp
                else:
                    _exp = 0;   _coe = 0
                _ec[_exp] = _coe
            vec[var] = _ec
        _der = Polynomial(vec)
        return _der

    # 求取self的積分
    def _int(self):
        vec = {};   _ec = {}
        for var in self._vec:
            for exp in self._vec[var]:
                _exp = exp + 1
                if exp:
                    if ispy3:
                        _coe = self._vec[var][exp] / key
                    else:
                        _coe = 1.0 * self._vec[var][exp] / key
                else:
                    _coe = self._vec[var][exp]
                _ec[_exp] = [_coe]
            vec[var] = _ec
        _int = Polynomial(vec)
        return _int

    polyder = _der
    polyint = _int

    # 返回self=poly的布爾值
    def __eq__(self, other):
        if isinstance(other, Polynomial):
            return (self._var == other._var and self._vec == other._vec)
        else:
            return (self == Polynomial(other))

    # 返回self≠poly的布爾值
    def __ne__(self, poly):
        return (not (self == poly))

    # 返回self<poly的布爾值
    def __lt__(self, poly):
        if self.has_sametype(poly):
            if self._cflag or poly._cflag:
                raise ComplexError('No ordering relation is defined for complex polynomial.')

            if self._vflag or poly._vflag:
                raise PolyError('No ordering relation is defined for multi-variable polynomial.')

            if len(self) > len(poly):       return False
            if len(self) < len(poly):       return True

            a_ec = self._vec[self._var[0]]
            b_ec = poly._vec[poly._var[0]]

            for ptr in jsrange(len(self), -1, -1):
                try:
                    if ptr in a_ec and ptr not in b_ec:     return False
                    if a_ec[ptr] > b_ec[ptr]:               return False
                except KeyError:
                    continue
            return True
        else:
            return (self < Polynomial(poly))

    # 返回self≤poly的布爾值
    def __le__(self, poly):
        return ((self == poly) or (self < poly))

    # 返回self>poly的布爾值
    def __gt__(self, poly):
        return (not (self <= poly))

    # 返回self≥poly的布爾值
    def __ge__(self, poly):
        return (not (self < poly))

    # support for pickling, copy, and deepcopy

    def __reduce__(self):
        return (self.__class__, (str(self),))

    def __copy__(self):
        if type(self) == Polynomial:
            return self     # I'm immutable; therefore I am my own clone
        return self.__class__(self._vec, dfvar=self._dfvar)

    def __deepcopy__(self, memo):
        if type(self) == Polynomial:
            return self     # My components are also immutable
        return self.__class__(self._vec, dfvar=self._dfvar)
