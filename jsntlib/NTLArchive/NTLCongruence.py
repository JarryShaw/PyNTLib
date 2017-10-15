# -*- coding: utf-8 -*-


import copy


# 同餘式類
# 由多項式衍生的同餘式


from .NTLBezoutEquation        import bezoutEquation
from .NTLExceptions            import DefinitionError, PCError, PolyError, SolutionError
from .NTLGreatestCommonDivisor import greatestCommonDivisor
from .NTLPolynomial            import Polynomial
from .NTLPrimeFactorisation    import primeFactorisation
from .NTLRepetiveSquareModulo  import repetiveSquareModulo
from .NTLTrivialDivision       import trivialDivision
from .NTLUtilities             import jsmaxint, jsrange
from .NTLValidations           import int_check, number_check


__all__  = ['Congruence', 'Solution']
nickname =  'Congruence'


'''Usage smaple:

_con = Congruence(('z', (2, 1), (0, -46)), mod=105)
print('The solution of %s is' % str(_con))

_ret = _con.solution
print('\t', _ret)

'''


class Congruence(Polynomial):

    __all__   = ['modulo', 'isprime', 'solution', 'iscomplex', 'isinteger',
        'ismultivar', 'var', 'vector', 'dfvar', 'nickname']
    __slots__ = ('_modulo', '_pflag', '_solution', '_cflag', '_iflag', '_vflag',
        '_var', '_vec', '_dfvar', '_nickname')

    ##########################################################################
    # Properties.
    ##########################################################################

    @property
    def modulo(a):
        return a._modulo

    @property
    def isprime(a):
        return a._pflag

    @property
    def solution(a):
        if a._solution is None:
            return a._solve()
        else:
            return a._solution

    ##########################################################################
    # Data models.
    ##########################################################################

    def __new__(cls, other=None, *items, **mods):
        try:
            trust = mods.pop('trust')
        except KeyError:
            trust = False

        if isinstance(other, Congruence):
            self = copy.deepcopy(other)

        elif isinstance(other, Polynomial):
            self = copy.deepcopy(other)
            self._modulo = None
            self._pflag = True if trust else None
            self._solution = None

        else:
            self = super(Congruence, cls).__new__(cls, other, *items, **mods)
            self._modulo = None
            self._pflag = True if trust else None
            self._solution = None

        return self

    def __init__(self, other=None, *items, **mods):
        self._update_state()
        self._nickname = 'cong'

        if self._modulo is None:
            self._modulo = self._read_mods(**mods)
            if self._modulo is None:
                raise DefinitionError('The modulo of congruence is missing.')
        if self._pflag is None:
            self._pflag = trivialDivision(self._modulo)

    def __call__(self, *vars):
        var = self._read_vars(*vars)
        if var is None:
            return self.solution
        else:
            _mod = self._modulo
            return self._eval(var, mod=_mod)

    # 返回同餘式對象的從屬
    def __repr__(self):
        _ret = '%s(%s, mod=%d)'
        name = self.__class__.__name__
        _var = ', '.join(self._var)
        _mod = self._modulo
        return _ret % (name, _var, _mod)

    # 返回同餘式的算術形式
    def __str__(self):
        _str = super(Congruence, self).__str__()
        _str += ' ≡ 0 (mod %d)' % self._modulo
        return _str

    ##########################################################################
    # Utilities.
    ##########################################################################

    # 用模重複平方法求self在x=_num時的值
    def _eval(self, *vars):
        _mod = self._modulo
        return self.mod(*vars, mod=_mod)

    # 求取self在x=_num時（不取模）的值
    def _calc(self, *vars):
        _ret = super(Congruence, self).eval(*vars)
        return _ret

    # 素數模同餘式的簡化
    def _simplify(self):
        if self._vflag:
            raise PolyError('Multi-variable congruence dose not support simplification.')
        if not self._iflag:
            raise PolyError('Non-integral congruence does not support simplification.')
        if not self._pflag:
            raise PCError('Composit-modulo congruence does not support simplification.')

        _mod = self._modulo;    _var = self._var[0]
        dvs_cong = Congruence((_var, (_mod, 1), (1, -1)), mod=_mod)
        rst_cong = self % dvs_cong
        return rst_cong

    # 任意模同餘式的求解
    def _solve(self):
        if self._vflag:
            raise PolyError('Multi-variable congruence dose not support solution.')
        if not self._iflag:
            raise PolyError('Non-integral congruence does not support solution.')

        if self._pflag:
            return self._prime()
        else:
            return self._composit()

    # 素數模的同餘式求解
    def _prime(self):
        _rem = []

        # 同餘式簡化
        rem = self._simplify()

        # 逐一驗算，如模為0則加入結果數組
        for x in jsrange(rem._modulo):
            if rem._eval(x) == 0:
                _rem.append(x)

        _var = self._var;   _mod = self._modulo
        _ret = Solution(_var, _mod, _rem)
        return _ret

    # 合數模的同餘式求解
    def _composit(self):
        # 分解模，以便判斷求解方式
        (p, q) = primeFactorisation(self._modulo, wrap=True)

        if len(p) == 1:     # 若模為單素數的次冪，則調用primeLite()函數求解
            tmpMod = p[0]
            tmpExp = q[0]
            _rem = self._primeLite(tmpMod, tmpExp)

        else:               # 若模為多素數的次冪，則逐一對其素因數調用primeLite()函數求解，再用中國剩餘定理處理
            tmpRem = []
            tmpMod = []
            for ptr in jsrange(len(p)):
                tmpModVar = p[ptr]
                tmpExpVar = q[ptr]
                tmpMod.append(tmpModVar ** tmpExpVar)
                tmpRem.append(self._primeLite(tmpModVar, tmpExpVar))

            # 用中國剩餘定理處理上述結果，得到最終結果
            _rem = self._CTR(tmpRem, tmpMod)

        _var = self._var;   _mod = self._modulo
        _ret = Solution(_var, _mod, _rem)
        return _ret

    # 單素數的次冪模同餘式求解
    def _primeLite(self, mod, exp):
        tmpCgc = copy.deepcopy(self)
        tmpCgc._modulo = mod
        tmpCgc._pflag = True

        tmpRem = tmpCgc._prime()[:]             # 獲取源素數模的同餘式的解
        if exp == 1:    return tmpRem

        _rem = tmpCgc._primePro(tmpRem, exp)    # 作高次同餘式的提升，求出源素數次冪模的同餘式的解
        return _rem

    # 高次同餘式的提升
    def _primePro(self, rem, exp):
        mod = self._modulo
        drv = self._der()   # 求取原同餘式的導式

        for tmpRem in rem:
            # 尋找滿足(f'(x1),p)=1的x1
            if greatestCommonDivisor(drv.mod(tmpRem), mod) == 1:
                x = tmpRem

                # 計算導式的值f'(x1) (mod p)，取其負值
                drvMod = drv.mod(x, mod=mod) - mod
                drvRcp = 1 // drvMod
                break

        for ctr in jsrange(0, exp):
            # t_(i-1) ≡ (-f(x_i)/p^i) * (f'(x1)^-1 (mod p)) (mod p)
            t = ((-self._calc(x) // (mod**ctr)) * drvRcp) % mod

            # x_i ≡ x_(i-1) + t_(i-1) * p^(i-1) (mod p^i)
            x += (t * (mod**ctr)) % (mod**(ctr+1))

        return [x]      # remainder = x

    # 中國剩餘定理
    def _CTR(self, rem, mod):
        modulo = self._modulo                           # M(original modulo) = ∏m_i

        bList = []
        for tmpMod in mod:
            M = modulo // tmpMod                        # M_i = M / m_i
            t = bezoutEquation(M, tmpMod)[0]            # t_i * M_i ≡ 1 (mod m_i)
            bList.append(t * M)                         # b_i = t_i * M_i

        _rem = self._iterCalc(rem, bList)               # x_j = Σ(b_i * r_i) (mod M)
        return _rem

    # 對rto多維數組（層，號）中的數進行全排列並計算結果
    def _iterCalc(self, ognList, coeList):
        ptrList = []                            # 寄存指向每一數組層的號
        lvlList = []                            # 寄存每一數組層的最大號
        for tmpList in ognList:
            ptrList.append(len(tmpList)-1)
            lvlList.append(len(tmpList)-1)

        flag = True
        rstList = []
        modulo = self._modulo

        while flag:
            ptrNum = 0
            rstNum = 0
            for ptr in ptrList:
                rstNum += ognList[ptrNum][ptr] * coeList[ptrNum]    # 計算結果
                ptrNum += 1

            x = rstNum % modulo
            rstList.append(x)
            (ptrList, flag) = self._updateState(ptrList, lvlList)   # 更新ptrList的寄存值，並返回是否結束循環

        return rstList

    # 更新ptrList的寄存值，並返回是否已遍歷所有組合
    def _updateState(self, ptrList, lvlList):
        ptr = 0
        flag = True
        glbFlag = True

        while flag:                                 # 未更新寄存數值前，保持循環（類似同步計數器）
            if ptrList[ptr] > 0:                    # 該層未遍歷，更新該層，終止循環
                ptrList[ptr] -= 1
                flag = False
            else:                                   # 該層已遍歷
                if ptr < len(lvlList) - 1:          # 更新指針至下一層並接著循環
                    ptrList[ptr] = lvlList[ptr]
                    ptr += 1
                else:                               # 所有情況均已遍歷，終止循環
                    flag = False
                    glbFlag = False

        return ptrList, glbFlag

    ##########################################################################
    # Methods.
    ##########################################################################

    calc     = _calc
    eval     = _eval
    simplify = _simplify
    solve    = _solve

    # support for pickling, copy, and deepcopy

    def __reduce__(self):
        return (self.__class__, (str(self),))

    def __copy__(self):
        if type(self) == Congruence:
            return self     # I'm immutable; therefore I am my own clone
        return self.__class__(self._vec, mod=self._modulo, dfvar=self._dfvar)

    def __deepcopy__(self, memo):
        if type(self) == Congruence:
            return self     # My components are also immutable
        return self.__class__(self._vec, mod=self._modulo, dfvar=self._dfvar)


class Solution(object):

    __all__   = ['var', 'mod', 'rem', 'qflag']
    __slots__ = ('_var', '_mod', '_rem', '_qflag')

    @property
    def variables(a):
        return a._var

    @property
    def modulo(a):
        return a._mod

    @property
    def solutions(a):
        return a._rem

    def __new__(cls, var, mod, rem, qflag=None):
        self = super(Solution, cls).__new__(cls)

        self._var = var
        self._mod = mod
        self._rem = sorted(rem)

        if qflag is None:
            self._qflag = False
        else:
            self._qflag = qflag

        return self

    def __call__(self):
        return self._rem

    def __repr__(self):
        _ret = 'Solution(%s, %d)' % (self._var, self._mod)
        return _ret

    def __str__(self):
        def _make_str(_list):
            _ret = []
            for item in _list:
                _ret.append(str(item))
            return _ret

        if self._qflag:
            x = self._var[0];   y = self._var[1]
            a = self._rem[0];   b = self._rem[1]
            _str = '%s = ±%d\t%s = ±%d' % (x, a, y, b)

        else:
            if len(self._rem) == 0:
                return 'No solution for %s modulo %d' % (self._var, self._mod)
            _rem = _make_str(self._rem)

            _str  = '%s ≡ ' % self._var[0]
            _str += ', '.join(_rem)
            _str += ' (mod %d)' % self._mod

        return _str

    def __len__(self):
        return len(self._rem)

    def __getitem__(self, _key):
        if isinstance(_key, str):
            if self._qflag:
                try:
                    return self._rem[self._var.find(_key)]
                except IndexError:
                    return None

            else:
                if _key in self._var:   return self._rem
                else:                   return []

        elif isinstance(_key, slice):
            return self.__getslice__(_key.start, _key.stop, _key.step)

        else:
            int_check(_key)
            try:
                return self._rem[_key]
            except IndexError:
                raise SolutionError('Only %d solutions found.' % len(self._rem))

    def __getslice__(self, i, j, k=None):
        if i is None:   i = 0
        if j is None:   j = len(self)
        if k is None:   k = 1

        int_check(i, j, k)

        if j == jsmaxint:   j = len(self)

        _list = []
        for ptr in jsrange(i, j, k):
            try:
                _list.append(self._rem[ptr])
            except IndexError:
                pass
        return _list

    # support for pickling, copy, and deepcopy

    def __reduce__(self):
        return (self.__class__, (str(self),))

    def __copy__(self):
        if type(self) == Congruence:
            return self     # I'm immutable; therefore I am my own clone
        return self.__class__(self._vec, self._mod, self._rem)

    def __deepcopy__(self, memo):
        if type(self) == Congruence:
            return self     # My components are also immutable
        return self.__class__(self._vec, self._mod, self._rem)
