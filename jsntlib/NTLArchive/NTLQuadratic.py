# -*- coding: utf-8 -*-

import copy
import numbers


# 二次同餘式類
# 由多項式式類衍生，型如x^2+y^2=p


from .NTLCongruence         import Congruence, Solution
from .NTLExceptions         import DefinitionError, PCError, PolyError
from .NTLPolynomial         import Polynomial
from .NTLPrimeFactorisation import primeFactorisation
from .NTLTrivialDivision    import trivialDivision
from .NTLUtilities          import jskeys, jssquare
from .NTLValidations        import str_check, tuple_check


__all__  = ['Quadratic']
nickname =  'Quadratic'


'''Usage sample:

_qua = Quadratic(8068, vars=('p', 'q'))
_rst = _qua.solution

print('The solution of %s is\n\t' % str(_qua))
print(_rst)

'''


class Quadratic(Polynomial):

    __all__   = ['constant', 'isprime', 'solution', 'iscomplex', 'isinteger', 'ismultivar',
        'var', 'vector', 'dfvar', 'nickname']
    __slots__ = ('_constant', '_pflag', '_solution', '_cflag', '_iflag', '_vflag',
        '_var', '_vec', '_dfvar', '_nickname')

    ##########################################################################
    # Properties.
    ##########################################################################

    @property
    def constant(a):
        return a._constant

    @property
    def isprime(a):
        return a._pflag

    @property
    def solution(a):
        if a._solution is None:
            return a.solve()
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

        if isinstance(other, Quadratic):
            # Handle construction from another Quadratic.
            self = copy.deepcopy(other)
            return self

        elif isinstance(other, numbers.Number):
            # Handle construction from numbers.
            def _read_name(**mods):
                for name in mods:
                    if name == 'vars':
                        tuple_check(mods[name])
                        if len(mods[name]) != 2:
                            raise DefinitionError('Only takes two variable names.')

                        v_1 = mods[name][0];    v_2 = mods[name][1]
                        str_check(v_1, v_2);    _var = (v_1, v_2);  break
                    else:
                        raise KeywordError('Keyword \'%s\' is not defined.' % kw)
                else:
                    _var = ('x', 'y')
                return _var

            v_1, v_2 = _read_name(**mods)
            vec = {v_1: {2: 1}, v_2: {2: 1}}
            self = super(Quadratic, cls).__new__(cls, vec, **mods)
            self._pflag = True if trust else trivialDivision(other)
            self._constant = other
            self._solution = None
            return self

        else:
            self = super(Quadratic, cls).__new__(cls, other, *items, **mods)
            self._pflag = True if trust else None
            self._constant = None
            return self

    def __init__(self, other=None, *items, **mods):
        self._update_state()
        self._nickname = 'quad'

        if len(self._var) != 2:
            raise PolyError('Quadratic must take two variables.')

        # Extract name of variables and common number item.
        def _extract(_dict):
            ctr = 0
            for var in _dict:
                for exp in jskeys(_dict[var]):
                    if exp == 0:
                        self._constant = -_dict[var][exp]
                        ctr += 1;   del _dict[exp]
                    if ctr > 1:
                        raise DefinitionError('Invalid literal for Quadratic.')

        _extract(self._vec)
        v_1 = self._var[0]; v_2 = self._var[1]
        vec = {v_1: {2: 1}, v_2: {2: 1}}
        if self._vec != vec:
            raise DefinitionError('Invalid literal for Quadratic.')

        if self._constant is None:
            raise DefinitionError('Invalid literal for Quadratic.')
        if self._pflag is None:
            self._pflag = trivialDivision(self._constant)

    def __str__(self):
        return '%s^2 + %s^2 = %d' % (self._var[0], self._var[1], self._constant)

    ##########################################################################
    # Methods.
    ##########################################################################

    def solve(self):
        _mul = 1
        if not self._pflag:
            (_p, _q) = primeFactorisation(self._constant, wrap=True)
            for item in zip(_p, _q):
                if item[1] % 2 == 1:
                    p = item[0]
                    q = self._constant // p
                    if jssquare(q):     break
            else:
                _var = self._var;   _mod = self._modulo;    _rem = []
                _ret = Solution(_var, _mod, _rem, True)
                return _ret
        else:
            p = self._constant

        if p % 4 != 1:
            _var = self._var;   _mod = None;    _rem = []
            _ret = Solution(_var, _mod, _rem)
            return _ret

        # 若p=8k+5為素數，有2為模p平方非剩餘，則同餘式x^2≡-1(mod p)的解為x=±2^((p-1)/4)(mod p)
        if p % 8 == 5:
            # 令x_0 = 2^((p-1)/4)(mod p)
            x = (2**((p-1)//4)) % p

        # 反之，用同餘式求解函數求出結果
        else:
            # 令x_0為x^2≡-1(mod p)的正解
            x = Congruence(((2, 1), (0, 1)), mod=p).solution[0]

        y = 1                               # 令y_0 = 1
        m = (x**2 + y**2) // p              # 由x_0^2 + y_0^2 = m_0 * p得m_0

        while m != 1:                       # 在x_i^2 + y_i^2 = p即m_0 = 1之後，退出循環
            tmp_x = x                       # 寄存當前的x_i-1
            u = x % m                       # 令u_i-1 ≡ x_i-1 (mod m_i-1)
            if u - m == -1:     u = -1
            v = y % m                       # 令v_i-1 ≡ y_i-1 (mod m_i-1)
            if v - m == -1:     v = -1
            x = (u*x + v*y) // m            # 則x_i = (u_i-1 * x_i-1 + v_i-1 * y_i-1) / m_i-1
            y = (u*y - v*tmp_x) // m        # 則y_i = (u_i-1 * y_i-1 - v_i-1 * x_i-1) / m_i-1
            m = (x**2 + y**2) // p          # 由x_i^2 + y_i^2 = m_i * p-1，得m_i

        x *= _mul;  y *= _mul
        _var = self._var;   _mod = None;    _rem = [abs(x), abs(y)]
        _ret = Solution(_var, _mod, _rem, True)
        return _ret
