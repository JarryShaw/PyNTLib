# -*- coding: utf-8 -*-

#複數域多項式類
#具備基本運算的複數域多項式實現

'''
TODO:

* Rewrite this file to an ABC (abstract base class)
* Inherit Polynomial class into integral/float/complex field (of coefficients)
* Consider using C++ to write a Polynomial extension type

Refernece: https://github.com/numpy/numpy/blob/v1.12.0/numpy/polynomial/_polybase.py
'''

import NTLExceptions
import NTLRepetiveSquareModulo

# class Polynomial(__import__('numbers').Number):
#     __name__  = 'Polynomial()'
#     __bases__ = '(Number)'
#     __slots__ = ('var', 'ecDict', 'rcflag')

__all__     = ['']
__version__ = '1.0'
__auther__  = 'jsNBZH'

class Polynomial:

    def __init__(self, *args, **kwargs):
        self.var = 'x'
        self.ecDict = {}
        self.rcflag = False

        for tpl in args:
            if not isinstance(tpl, tuple) or len(tpl) != 2:
                raise NTLExceptions.TupleError('The arguments must be tuples of exponents and coefficients.')

            if not numbercheck(tpl[1]):
                raise NTLExceptions.DigitError('The coefficient must be a number.')

            if tpl[1] == 0:     continue

            if not isinstance(tpl[0], int):
                raise NTLExceptions.IntError('The exponent must be integral.')

            if tpl[0] < 0:      raise NTLExceptions.PNError('The exponent must be positive.')

            if isinstance(tpl[1], complex):     self.rcflag = True

            try:
                self.ecDict[tpl[0]] += tpl[1]
                if self.ecDict[tpl[0]] == 0:
                    del self.ecDict[tpl[0]]
            except KeyError:
                self.ecDict[tpl[0]] = tpl[1]

        for kw in kwargs:
            if kw != 'var':
                raise NTLExceptions.KeywordError('Keyword \'%s\' is not defined.' %kw)
            else:
                if not isinstance(kwargs[kw], str):
                    raise NTLExceptions.StringError('The argument must be a string.')

                self.var = kwargs[kw]

    def __call__(self, *args):
        for tpl in args:
            if not isinstance(tpl, tuple) or len(tpl) != 2:
                raise NTLExceptions.TupleError('The arguments must be tuples of exponents and coefficients.')

            if not numbercheck(tpl[1]):
                raise NTLExceptions.DigitError('The coefficient must be a number.')

            if tpl[1] == 0:     continue

            if not isinstance(tpl[0], int):
                raise NTLExceptions.IntError('The exponent must be integral.')

            if tpl[0] < 0:      raise NTLExceptions.PNError('The exponent must be positive.')

            if isinstance(tpl[1], complex):     self.rcflag = True

            try:
                self.ecDict[tpl[0]] += tpl[1]
                if self.ecDict[tpl[0]] == 0:
                    del self.ecDict[tpl[0]]
            except KeyError:
                self.ecDict[tpl[0]] = tpl[1]

    #返回多項式對象的從屬
    def __repr__(self):
        return 'Polynomial(%s)' %self.var

    #返回多項式的算術形式
    def __str__(self):
        if self.ecDict == {}:   return '0'

        string = ''
        (exp, coe) = self.dicttolist()

        for ptr in xrange(len(exp)):
            exp_ = exp[ptr]

            if isinstance(coe[ptr], complex):
                coe_ = coe[ptr]
                if coe_ == 0:   continue
                if ptr > 0:     string += ' + '
            else:
                coe_ = abs(coe[ptr]) 
                if coe_ == 0:   continue
                if ptr == 0:  string += '-' if coe[0] < 0 else ''
                if ptr > 0:     string += ' - ' if coe[ptr] < 0 else ' + '

            if exp_ == 0:
                string += str(coe_)
            else:
                string += '' if coe_ == 1 else (str(coe_))
                string += self.var
                string += ''  if exp_ == 1 else ('^' + str(exp_))

        return string

    #返回self<poly的布爾值
    def __lt__(self, poly):
        if numbercheck(poly):       poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = self.make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The comparison is between two instances of Polynomial.')

        if self.rcflag or poly.rcflag:
            raise NTLExceptions.ComplexError('No ordering relation is defined for complex polynomials.')

        if len(self) > len(poly):       return False
        if len(self) < len(poly):       return True
        
        a_coe = self.dicttolist()[1]
        b_coe = poly.dicttolist()[1]
        for ptr in range(len(a_coe)):
            if a_coe[ptr] >= b_coe[ptr]:
                return False

        return True

    #返回self≤poly的布爾值
    def __le__(self, poly):
        if numbercheck(poly):       poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = self.make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The comparison is between two instances of Polynomial.')

        if self.rcflag or poly.rcflag:
            raise NTLExceptions.ComplexError('No ordering relation is defined for complex polynomials.')

        if len(self) >  len(poly):      return False
        if len(self) <= len(poly):      return True
        
        a_coe = self.dicttolist()[1]
        b_coe = poly.dicttolist()[1]
        for ptr in range(len(a_coe)):
            if a_coe[ptr] > b_coe[ptr]:
                return False

        return True

    #返回self=poly的布爾值
    def __eq__(self, poly):
        if numbercheck(poly):       poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = self.make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The comparison is between two instances of Polynomial.')

        if len(self) != len(poly):       return False
        
        a_coe = self.dicttolist()[1]
        b_coe = poly.dicttolist()[1]
        for ptr in range(len(a_coe)):
            if a_coe[ptr] != b_coe[ptr]:
                return False

        return True

    #返回self≠poly的布爾值
    def __ne__(self, poly):
        if numbercheck(poly):       poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = self.make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The comparison is between two instances of Polynomial.')

        if self.rcflag or poly.rcflag:
            raise NTLExceptions.ComplexError('No ordering relation is defined for complex polynomials.')

        if len(self) != len(poly):       return True
        
        a_coe = self.dicttolist()[1]
        b_coe = poly.dicttolist()[1]
        for ptr in range(len(a_coe)):
            if a_coe[ptr] != b_coe[ptr]:
                return True

        return False

    #返回self>poly的布爾值
    def __gt__(self, poly):
        if numbercheck(poly):       poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = self.make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The comparison is between two instances of Polynomial.')

        if self.rcflag or poly.rcflag:
            raise NTLExceptions.ComplexError('No ordering relation is defined for complex polynomials.')

        if len(self) >  len(poly):      return True
        if len(self) <= len(poly):      return False
        
        a_coe = self.dicttolist()[1]
        b_coe = poly.dicttolist()[1]
        for ptr in range(len(a_coe)):
            if a_coe[ptr] <= b_coe[ptr]:
                return False

        return True

    #返回self≥poly的布爾值
    def __ge__(self, poly):
        if numbercheck(poly):       poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = self.make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The comparison is between two instances of Polynomial.')

        if self.rcflag or poly.rcflag:
            raise NTLExceptions.ComplexError('No ordering relation is defined for complex polynomials.')

        if len(self) > len(poly):       return True
        if len(self) < len(poly):       return False
        
        a_coe = self.dicttolist()[1]
        b_coe = poly.dicttolist()[1]
        for ptr in range(len(a_coe)):
            if a_coe[ptr] < b_coe[ptr]:
                return False

        return True

    #返回最高次項的次冪
    def __len__(self):
        return (max(self.ecDict) + 1)

    #返回key次項的係數
    def __getitem__(self, key):
        if not isinstance(key, int):
            raise NTLExceptions.IntError('The index must be integral.')

        try:
            return self.ecDict[key]
        except KeyError:
            return 0

    #修改key次項的係數為value
    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise NTLExceptions.IntError('The index must be integral.')

        if not numbercheck(value):
            raise NTLExceptions.DigitError('The value must be a number.') 

        self.ecDict[key] = value

    #刪去key次項
    def __delitem__(self, key):
        if not isinstance(key, int):
            raise NTLExceptions.IntError('The index must be integral.')

        try:    
            del self.ecDict[key]
        except KeyError:
            pass

    #判斷一多項式是否含於多項式中
    def __contains__(self, poly):
        if numbercheck(poly):       poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = self.make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The argument must be an instance of Polynomial.')

        poly_exp = poly.dicttolist()[0]
        for exp in poly_exp:
            try:
                if self[exp] != poly[exp]:
                    return False
            except KeyError:
                return False

        return True

    '''
    特別注意：
    1. 當下標值（key／i&j）小於零時，系統自動調用__len__()函數，並自增轉化為正數下標，即 key += len；
    2. 若下標缺省，起始地址模認為0，而終止地址將被模認為最大整型數，即9223372036854775807。
    '''

    #返回i至j-1次項的多項式
    def __getslice__(self, i, j):
        if not isinstance(i, int) or not isinstance(j, int):
            raise NTLExceptions.IntError('The arguments must be integral.')

        # if i < 0:   tmp_i = len(self) + i + 1;  i = 0 if tmp_i < 0 else tmp_i
        # if j < 0:   tmp_j = len(self) + j + 1;  j = 0 if tmp_j < 0 else tmp_j
        if j == 9223372036854775807:    j = len(self)
        
        poly = Polynomial()
        for ptr in range(i, j):
            try:
                poly((ptr, self.ecDict[ptr]))
            except KeyError:
                pass

        return poly

    #修改i至j-1次項的多項式
    def __setslice__(self, i, j, coe):
        if not isinstance(i, int) or not isinstance(j, int):
            raise NTLExceptions.IntError('The arguments must be integral.')

        if not isinstance(coe, list):
            raise NTLExceptions.ListError('The sequence must be list type.')

        for coe_ in coe:
            if not numbercheck(coe_):
                raise NTLExceptions.DigitError('The values must be numbers.')
        
        # if i < 0:   tmp_i = len(self) + i + 1;  i = 0 if tmp_i < 0 else tmp_i
        # if j < 0:   tmp_j = len(self) + j + 1;  j = 0 if tmp_j < 0 else tmp_j
        if j == 9223372036854775807:    j = len(self)

        j = i + len(coe)
        for ptr in range(i, j):
            self.ecDict[ptr] = coe[ptr - i]
           
    #刪除i至j-1次項的多項式       
    def __delslice__(self, i, j):
        if not isinstance(i, int) or not isinstance(j, int):
            raise NTLExceptions.IntError('The arguments must be integral.')

        # if i < 0:   tmp_i = len(self) + i + 1;  i = 0 if tmp_i < 0 else tmp_i
        # if j < 0:   tmp_j = len(self) + j + 1;  j = 0 if tmp_j < 0 else tmp_j
        if j == 9223372036854775807:    j = len(self)

        for ptr in range(i, j):
            try:
                del self.ecDict[ptr]
            except KeyError:
                pass

    #求取sum_ = self + poly
    def __add__(self, poly):
        if numbercheck(poly):       poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = self.make_poly(poly)

        if not isinstance(poly, Polynomial): 
            raise NTLExceptions.PolyError('The addent must be an instance of Polynomial.')

        sum_ = __import__('copy').deepcopy(self)
        sum_.var = 'x'

        (b_exp, b_coe) = poly.dicttolist()
        for ptr in range(len(b_exp)):
            exp = b_exp[ptr]
            coe = b_coe[ptr]
            sum_((exp, coe))

        return sum_

    #求取rsum = poly + self
    def __radd__(self, poly):
        if numbercheck(poly):       poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = self.make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The augend must be an instance of Polynomial.')

        rsum = __import__('copy').deepcopy(poly)
        rsum.var = 'x'

        (b_exp, b_coe) = self.dicttolist()
        for ptr in range(len(b_exp)):
            exp = b_exp[ptr]
            coe = b_coe[ptr]
            rsum((exp, coe))

        return rsum

    #求取self += poly
    def __iadd__(self, poly):
        if numbercheck(poly):       poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = self.make_poly(poly)

        if not isinstance(poly, Polynomial): 
            raise NTLExceptions.PolyError('The addent must be an instance of Polynomial.')

        sum_ = __import__('copy').deepcopy(self)
        sum_.var = 'x'

        (b_exp, b_coe) = poly.dicttolist()
        for ptr in range(len(b_exp)):
            exp = b_exp[ptr]
            coe = b_coe[ptr]
            sum_((exp, coe))

        return sum_

    #求取dif_ = self - poly
    def __sub__(self, poly):
        if numbercheck(poly):       poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = self.make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The subtrahend must be an instance of Polynomial.')

        dif_ = __import__('copy').deepcopy(self)
        dif_.var = 'x'

        (b_exp, b_coe) = poly.dicttolist()
        for ptr in range(len(b_exp)):
            exp = b_exp[ptr]
            coe = b_coe[ptr] * -1
            dif_((exp, coe))

        return dif_

    #求取rdif = poly - self
    def __rsub__(self, poly):
        if numbercheck(poly):       poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = self.make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The minuend must be an instance of Polynomial.')

        rdif = __import__('copy').deepcopy(poly)
        rdif.var = 'x'

        (b_exp, b_coe) = self.dicttolist()
        for ptr in range(len(b_exp)):
            exp = b_exp[ptr]
            coe = b_coe[ptr] * -1
            rdif((exp, coe))

        return rdif

    #求取self -= poly
    def __isub__(self, poly):
        if numbercheck(poly):       poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = self.make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The minuend must be an instance of Polynomial.')

        dif_ = __import__('copy').deepcopy(self)
        dif_.var = 'x'

        (b_exp, b_coe) = poly.dicttolist()
        for ptr in range(len(b_exp)):
            exp = b_exp[ptr]
            coe = b_coe[ptr] * -1
            dif_((exp, coe))

        return dif_

    #求取pro_ = self * poly
    def __mul__(self, poly):
        if numbercheck(poly):       poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = self.make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The multiplier must be an instance of Polynomial.')

        pro_ = Polynomial()
        (a_exp, a_coe) = self.dicttolist()
        (b_exp, b_coe) = poly.dicttolist()
        for ptr_1 in range(len(a_exp)):
            for ptr_2 in range(len(b_exp)):
                exp = a_exp[ptr_1] + b_exp[ptr_2]
                coe = a_coe[ptr_1] * b_coe[ptr_2]
                pro_((exp, coe))

        return pro_

    #求取rpro = poly * self
    def __rmul__(self, poly):
        if numbercheck(poly):       poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = self.make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The multiplicand must be an instance of Polynomial.')

        rpro = Polynomial()
        (a_exp, a_coe) = poly.dicttolist()
        (b_exp, b_coe) = self.dicttolist()
        for ptr_1 in range(len(a_exp)):
            for ptr_2 in range(len(b_exp)):
                exp = a_exp[ptr_1] + b_exp[ptr_2]
                coe = a_coe[ptr_1] * b_coe[ptr_2]
                rpro((exp, coe))

        return rpro

    #求取self *= poly
    def __imul__(self, poly):
        if numbercheck(poly):       poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = self.make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The multiplier must be an instance of Polynomial.')

        pro_ = Polynomial()
        (a_exp, a_coe) = self.dicttolist()
        (b_exp, b_coe) = poly.dicttolist()
        for ptr_1 in range(len(a_exp)):
            for ptr_2 in range(len(b_exp)):
                exp = a_exp[ptr_1] + b_exp[ptr_2]
                coe = a_coe[ptr_1] * b_coe[ptr_2]
                pro_((exp, coe))

        return pro_

    #求取quo_ = self / poly
    def __div__(self, poly):
        if numbercheck(poly):       poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = self.make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The divisor must be an instance of Polynomial.')

        quo_ = Polynomial()
        rem_ = __import__('copy').deepcopy(self)
        rem_.var = 'x'

        a_expmax = max(self.ecDict)                         #獲取被除式的最高次數
        b_exp = sorted(poly.ecDict.keys(), reverse=True)    #獲取除式的指數列（降序）

        #若被除式最高次冪小於除式最高次冪則終止迭代
        while a_expmax >= b_exp[0]:
            quo_coe = 1.0 * rem_.ecDict[a_expmax] / poly.ecDict[b_exp[0]]   #計算商式的係數，即當前被除式最高次冪項係數與除式最高次冪的項係數的商值
            quo_exp = a_expmax - b_exp[0]                                   #計算商式的次冪，即當前被除式最高次冪與除式最高次冪的差值
            quo_((quo_exp, quo_coe))                                        #將結果添入商式多項式

            #更新被除式係數及次冪狀態
            for exp in b_exp:
                rem_exp = exp + quo_exp
                rem_coe = -1.0 * poly.ecDict[exp] * quo_coe
                rem_((rem_exp, rem_coe))
                    
            #更新被除式的最高次數
            try:
                a_expmax = max(rem_.ecDict)
            except ValueError:
                return quo_

        return quo_

    #求取rquo = poly / self
    def __rdiv__(self, poly):
        if numbercheck(poly):       poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = self.make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The dividend must be an instance of Polynomial.')

        rquo = Polynomial()
        rrem = __import__('copy').deepcopy(self)
        rrem.var = 'x'

        a_expmax = max(poly.ecDict)                         #獲取被除式的最高次數
        b_exp = sorted(self.ecDict.keys(), reverse=True)    #獲取除式的指數列（降序）

        #若被除式最高次冪小於除式最高次冪則終止迭代
        while a_expmax >= b_exp[0]:
            quo_coe = 1.0 * rem_.ecDict[a_expmax] / self.ecDict[b_exp[0]]   #計算商式的係數，即當前被除式最高次冪項係數與除式最高次冪的項係數的商值
            quo_exp = a_expmax - b_exp[0]                                   #計算商式的次冪，即當前被除式最高次冪與除式最高次冪的差值
            rquo((quo_exp, quo_coe))            #將結果添入商式字典

            #更新被除式係數及次冪狀態
            for exp in b_exp:
                rem_exp = exp + quo_exp
                rem_coe = -1 * self.ecDict[exp] * quo_coe
                rrem((rem_exp, rem_coe))
                    
            #更新被除式的最高次數
            try:
                a_expmax = max(rrem.ecDict)
            except ValueError:
                return rquo

        return rquo

    #求取self /= poly
    def __idiv__(self, poly):
        if numbercheck(poly):       poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = self.make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The divisor must be an instance of Polynomial.')

        quo_ = Polynomial()
        rem_ = __import__('copy').deepcopy(self)
        rem_.var = 'x'

        a_expmax = max(self.ecDict)                         #獲取被除式的最高次數
        b_exp = sorted(poly.ecDict.keys(), reverse=True)    #獲取除式的指數列（降序）

        #若被除式最高次冪小於除式最高次冪則終止迭代
        while a_expmax >= b_exp[0]:
            quo_coe = 1.0 * rem_.ecDict[a_expmax] / poly.ecDict[b_exp[0]]   #計算商式的係數，即當前被除式最高次冪項係數與除式最高次冪的項係數的商值
            quo_exp = a_expmax - b_exp[0]                                   #計算商式的次冪，即當前被除式最高次冪與除式最高次冪的差值
            quo_((quo_exp, quo_coe))                                        #將結果添入商式多項式

            #更新被除式係數及次冪狀態
            for exp in b_exp:
                rem_exp = exp + quo_exp
                rem_coe = -1.0 * poly.ecDict[exp] * quo_coe
                rem_((rem_exp, rem_coe))
                    
            #更新被除式的最高次數
            try:
                a_expmax = max(rem_.ecDict)
            except ValueError:
                return quo_

        return quo_

    #求取quo_ = self // poly
    def __floordiv__(self, poly):
        if numbercheck(poly):       poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = self.make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The divisor must be an instance of Polynomial.')

        quo_ = Polynomial()
        did_ = __import__('copy').deepcopy(poly)
        rem_ = __import__('copy').deepcopy(self)
        rem_.var = 'x'

        a_expmax = max(self.ecDict.keys())                  #獲取被除式的最高次數
        b_exp = sorted(poly.ecDict.keys(), reverse=True)    #獲取除式的指數列（降序）

        #若除式最高次冪的係數不為1，則需化簡
        if poly.ecDict[b_exp[0]] != 1:
            coe_ = poly.ecDict[b_exp[0]]

            if self.ecDict[a_expmax] % coe_ == 0:
                mul_ = self.ecDict[a_expmax] / coe_
                if self == poly * mul_:
                    quo_ = Polynomial((0, mul_))
                    return quo_

            #判斷除式是否可化簡
            for exp in b_exp:
                if poly.ecDict[exp] % coe_ != 0:
                    return quo_
                else:
                    did_.ecDict[exp] /= coe_

            #判斷被除式是否可化簡
            for key in self.ecDict.keys():
                if self.ecDict[key] % coe_ != 0:
                    return quo_
                else:
                    rem_.ecDict[key] /= coe_

        #若被除式最高次冪小於除式最高次冪則終止迭代
        while a_expmax >= b_exp[0]:
            quo_coe = rem_.ecDict[a_expmax]     #計算商式的係數，即當前被除式最高次冪項的係數
            quo_exp = a_expmax - b_exp[0]       #計算商式的次冪，即當前被除式最高次冪與除式最高次冪的差值
            quo_((quo_exp, quo_coe))            #將結果添入商式字典

            #更新被除式係數及次冪狀態
            for exp in b_exp:
                rem_exp = exp + quo_exp
                rem_coe = -1 * did_.ecDict[exp] * quo_coe
                rem_((rem_exp, rem_coe))
                    
            #更新被除式的最高次數
            try:
                a_expmax = max(rem_.ecDict.keys())
            except ValueError:
                return quo_

        return quo_

    #求取rquo = poly // self
    def __rfloordiv__(self, poly):
        if numbercheck(poly):       poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = self.make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The dividend must be an instance of Polynomial.')

        rquo = Polynomial()
        rdid = __import__('copy').deepcopy(self)
        rrem = __import__('copy').deepcopy(poly)
        rrem.var = 'x'

        a_expmax = max(poly.ecDict.keys())                  #獲取被除式的最高次數
        b_exp = sorted(self.ecDict.keys(), reverse=True)    #獲取除式的指數列（降序）

        #若除式最高次冪的係數不為1，則需化簡
        if self.ecDict[b_exp[0]] != 1:
            rcoe = self.ecDict[b_exp[0]]

            if poly.ecDict[a_expmax] % rcoe == 0:
                rmul = poly.ecDict[a_expmax] / rcoe
                if poly == self * rmul:
                    rquo = Polynomial((0, rmul))
                    return rquo

            #判斷除式是否可化簡
            for exp in b_exp:
                if self.ecDict[exp] % rcoe != 0:
                    return rquo
                else:
                    rdid.ecDict[exp] /= rcoe

            #判斷被除式是否可化簡
            for key in poly.ecDict.keys():
                if poly.ecDict[key] % rcoe != 0:
                    return rquo
                else:
                    rrem.ecDict[key] /= rcoe

        #若被除式最高次冪小於除式最高次冪則終止迭代
        while a_expmax >= b_exp[0]:
            quo_coe = rrem.ecDict[a_expmax]     #計算商式的係數，即當前被除式最高次冪項的係數
            quo_exp = a_expmax - b_exp[0]       #計算商式的次冪，即當前被除式最高次冪與除式最高次冪的差值
            rquo((quo_exp, quo_coe))            #將結果添入商式字典

            #更新被除式係數及次冪狀態
            for exp in b_exp:
                rem_exp = exp + quo_exp
                rem_coe = -1 * rdid.ecDict[exp] * quo_coe
                rrem((rem_exp, rem_coe))
                    
            #更新被除式的最高次數
            try:
                a_expmax = max(rrem.ecDict.keys())
            except ValueError:
                return rquo

        return rquo

    #求取self //= poly
    def __ifloordiv__(self, poly):
        if numbercheck(poly):       poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = self.make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The divisor must be an instance of Polynomial.')

        if isinstance(poly, int):   poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = self.make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The divisor must be an instance of Polynomial.')

        quo_ = Polynomial()
        did_ = __import__('copy').deepcopy(poly)
        rem_ = __import__('copy').deepcopy(self)
        rem_.var = 'x'

        a_expmax = max(self.ecDict.keys())                  #獲取被除式的最高次數
        b_exp = sorted(poly.ecDict.keys(), reverse=True)    #獲取除式的指數列（降序）

        #若除式最高次冪的係數不為1，則需化簡
        if poly.ecDict[b_exp[0]] != 1:
            coe_ = poly.ecDict[b_exp[0]]

            if self.ecDict[a_expmax] % coe_ == 0:
                mul_ = self.ecDict[a_expmax] / coe_
                if self == poly * mul_:
                    quo_ = Polynomial((0, mul_))
                    return quo_

            #判斷除式是否可化簡
            for exp in b_exp:
                if poly.ecDict[exp] % coe_ != 0:
                    return quo_
                else:
                    did_.ecDict[exp] /= coe_

            #判斷被除式是否可化簡
            for key in self.ecDict.keys():
                if self.ecDict[key] % coe_ != 0:
                    return quo_
                else:
                    rem_.ecDict[key] /= coe_

        #若被除式最高次冪小於除式最高次冪則終止迭代
        while a_expmax >= b_exp[0]:
            quo_coe = rem_.ecDict[a_expmax]     #計算商式的係數，即當前被除式最高次冪項的係數
            quo_exp = a_expmax - b_exp[0]       #計算商式的次冪，即當前被除式最高次冪與除式最高次冪的差值
            quo_((quo_exp, quo_coe))            #將結果添入商式字典

            #更新被除式係數及次冪狀態
            for exp in b_exp:
                rem_exp = exp + quo_exp
                rem_coe = -1 * did_.ecDict[exp] * quo_coe
                rem_((rem_exp, rem_coe))
                    
            #更新被除式的最高次數
            try:
                a_expmax = max(rem_.ecDict.keys())
            except ValueError:
                return quo_

        return quo_

    #求取rem_ = self % poly
    def __mod__(self, poly):
        if numbercheck(poly):       poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = self.make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The divisor must be an instance of Polynomial.')

        # quo_ = Polynomial()
        did_ = __import__('copy').deepcopy(poly)
        rem_ = __import__('copy').deepcopy(self)
        rem_.var = 'x'

        a_expmax = max(self.ecDict.keys())                  #獲取被除式的最高次數
        b_exp = sorted(poly.ecDict.keys(), reverse=True)    #獲取除式的指數列（降序）

        #若除式最高次冪的係數不為1，則需化簡
        if poly.ecDict[b_exp[0]] != 1:
            coe_ = poly.ecDict[b_exp[0]]

            if self.ecDict[a_expmax] % coe_ == 0:
                mul_ = self.ecDict[a_expmax] / coe_
                if self == poly * mul_:
                    rem_ = Polynomial()
                    return rem_

            #判斷除式是否可化簡
            for exp in b_exp:
                if poly.ecDict[exp] % coe_ != 0:
                    return rem_
                else:
                    did_.ecDict[exp] /= coe_

            #判斷被除式是否可化簡
            for key in self.ecDict.keys():
                if self.ecDict[key] % coe_ != 0:
                    return rem_
                else:
                    rem_.ecDict[key] /= coe_

        #若被除式最高次冪小於除式最高次冪則終止迭代
        while a_expmax >= b_exp[0]:
            quo_coe = rem_.ecDict[a_expmax]     #計算商式的係數，即當前被除式最高次冪項的係數
            quo_exp = a_expmax - b_exp[0]       #計算商式的次冪，即當前被除式最高次冪與除式最高次冪的差值
            # quo_((quo_exp, quo_coe))          #將結果添入商式字典

            #更新被除式係數及次冪狀態
            for exp in b_exp:
                rem_exp = exp + quo_exp
                rem_coe = -1 * did_.ecDict[exp] * quo_coe
                rem_((rem_exp, rem_coe))
                    
            #更新被除式的最高次數
            try:
                a_expmax = max(rem_.ecDict.keys())
            except ValueError:
                # rem_ = Polynomial()
                return rem_

        return rem_

    #求取rrem = poly % self
    def __rmod__(self, poly):
        if numbercheck(poly):       poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = self.make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The dividend must be an instance of Polynomial.')

        # rquo = Polynomial()
        rdid = __import__('copy').deepcopy(self)
        rrem = __import__('copy').deepcopy(poly)
        rrem.var = 'x'

        a_expmax = max(poly.ecDict.keys())                  #獲取被除式的最高次數
        b_exp = sorted(self.ecDict.keys(), reverse=True)    #獲取除式的指數列（降序）

        #若除式最高次冪的係數不為1，則需化簡
        if self.ecDict[b_exp[0]] != 1:
            rcoe = self.ecDict[b_exp[0]]

            if poly.ecDict[a_expmax] % rcoe == 0:
                rmul = poly.ecDict[a_expmax] / rcoe
                if poly == poly * rmul:
                    rrem = Polynomial()
                    return rrem

            #判斷除式是否可化簡
            for exp in b_exp:
                if self.ecDict[exp] % rcoe != 0:
                    return rrem
                else:
                    rdid.ecDict[exp] /= rcoe

            #判斷被除式是否可化簡
            for key in poly.ecDict.keys():
                if poly.ecDict[key] % rcoe != 0:
                    return rrem
                else:
                    rrem.ecDict[key] /= rcoe

        #若被除式最高次冪小於除式最高次冪則終止迭代
        while a_expmax >= b_exp[0]:
            quo_coe = rem_.ecDict[a_expmax]     #計算商式的係數，即當前被除式最高次冪項的係數
            quo_exp = a_expmax - b_exp[0]       #計算商式的次冪，即當前被除式最高次冪與除式最高次冪的差值
            # quo_((quo_exp, quo_coe))          #將結果添入商式字典

            #更新被除式係數及次冪狀態
            for exp in b_exp:
                rem_exp = exp + quo_exp
                rem_coe = -1 * rdid.ecDict[exp] * quo_coe
                rrem((rem_exp, rem_coe))
                    
            #更新被除式的最高次數
            try:
                a_expmax = max(rrem.ecDict.keys())
            except ValueError:
                # rrem = Polynomial()
                return rrem

        return rrem

    #求取self %= poly
    def __imod__(self, poly):
        if numbercheck(poly):       poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = self.make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The divisor must be an instance of Polynomial.')

        # quo_ = Polynomial()
        did_ = __import__('copy').deepcopy(poly)
        rem_ = __import__('copy').deepcopy(self)
        rem_.var = 'x'

        a_expmax = max(self.ecDict.keys())                  #獲取被除式的最高次數
        b_exp = sorted(poly.ecDict.keys(), reverse=True)    #獲取除式的指數列（降序）

        #若除式最高次冪的係數不為1，則需化簡
        if poly.ecDict[b_exp[0]] != 1:
            coe_ = poly.ecDict[b_exp[0]]

            if self.ecDict[a_expmax] % coe_ == 0:
                mul_ = self.ecDict[a_expmax] / coe_
                if self == poly * mul_:
                    rem_ = Polynomial()
                    return rem_

            #判斷除式是否可化簡
            for exp in b_exp:
                if poly.ecDict[exp] % coe_ != 0:
                    return rem_
                else:
                    did_.ecDict[exp] /= coe_

            #判斷被除式是否可化簡
            for key in self.ecDict.keys():
                if self.ecDict[key] % coe_ != 0:
                    return rem_
                else:
                    rem_.ecDict[key] /= coe_

        #若被除式最高次冪小於除式最高次冪則終止迭代
        while a_expmax >= b_exp[0]:
            quo_coe = rem_.ecDict[a_expmax]     #計算商式的係數，即當前被除式最高次冪項的係數
            quo_exp = a_expmax - b_exp[0]       #計算商式的次冪，即當前被除式最高次冪與除式最高次冪的差值
            # quo_((quo_exp, quo_coe))          #將結果添入商式字典

            #更新被除式係數及次冪狀態
            for exp in b_exp:
                rem_exp = exp + quo_exp
                rem_coe = -1 * did_.ecDict[exp] * quo_coe
                rem_((rem_exp, rem_coe))
                    
            #更新被除式的最高次數
            try:
                a_expmax = max(rem_.ecDict.keys())
            except ValueError:
                # rem_ = Polynomial()
                return rem_

        return rem_

    #求取(quo_, rem_) = divmod(self, poly)
    def __divmod__(self, poly):
        if numbercheck(poly):       poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = self.make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The divisor must be an instance of Polynomial.')

        quo_ = Polynomial()
        did_ = __import__('copy').deepcopy(poly)
        rem_ = __import__('copy').deepcopy(self)
        rem_.var = 'x'

        a_expmax = max(self.ecDict.keys())                  #獲取被除式的最高次數
        b_exp = sorted(poly.ecDict.keys(), reverse=True)    #獲取除式的指數列（降序）

        #若除式最高次冪的係數不為1，則需化簡
        if poly.ecDict[b_exp[0]] != 1:
            coe_ = poly.ecDict[b_exp[0]]

            if self.ecDict[a_expmax] % coe_ == 0:
                mul_ = self.ecDict[a_expmax] / coe_
                if self == poly * mul_:
                    quo_ = Polynomial((0, mul_))
                    rem_ = Polynomial()
                    return quo_, rem_

            #判斷除式是否可化簡
            for exp in b_exp:
                if poly.ecDict[exp] % coe_ != 0:
                    return quo_, rem_
                else:
                    did_.ecDict[exp] /= coe_

            #判斷被除式是否可化簡
            for key in self.ecDict.keys():
                if self.ecDict[key] % coe_ != 0:
                    return quo_, rem_
                else:
                    rem_.ecDict[key] /= coe_

        #若被除式最高次冪小於除式最高次冪則終止迭代
        while a_expmax >= b_exp[0]:
            quo_coe = rem_.ecDict[a_expmax]     #計算商式的係數，即當前被除式最高次冪項的係數
            quo_exp = a_expmax - b_exp[0]       #計算商式的次冪，即當前被除式最高次冪與除式最高次冪的差值
            quo_((quo_exp, quo_coe))            #將結果添入商式字典

            #更新被除式係數及次冪狀態
            for exp in b_exp:
                rem_exp = exp + quo_exp
                rem_coe = -1 * did_.ecDict[exp] * quo_coe
                rem_((rem_exp, rem_coe))
                    
            #更新被除式的最高次數
            try:
                a_expmax = max(rem_.ecDict.keys())
            except ValueError:
                # rem_ = Polynomial()
                return quo_, rem_

        return quo_, rem_

    #求取(rquo, rrem) = rdivmod(poly, self)
    def __rdivmod__(self, poly):
        if numbercheck(poly):       poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = self.make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The dividend must be an instance of Polynomial.')

        rquo = Polynomial()
        rdid = __import__('copy').deepcopy(self)
        rrem = __import__('copy').deepcopy(poly)
        rrem.var = 'x'

        a_expmax = max(poly.ecDict.keys())                  #獲取被除式的最高次數
        b_exp = sorted(self.ecDict.keys(), reverse=True)    #獲取除式的指數列（降序）

        #若除式最高次冪的係數不為1，則需化簡
        if self.ecDict[b_exp[0]] != 1:
            rcoe = self.ecDict[b_exp[0]]

            if poly.ecDict[a_expmax] % rcoe == 0:
                rmul = poly.ecDict[a_expmax] / rcoe
                if poly == poly * rmul:
                    rquo = Polynomial((0, rmul))
                    rrem = Polynomial()
                    return rquo, rrem

            #判斷除式是否可化簡
            for exp in b_exp:
                if self.ecDict[exp] % rcoe != 0:
                    return rquo, rrem
                else:
                    rdid.ecDict[exp] /= rcoe

            #判斷被除式是否可化簡
            for key in poly.ecDict.keys():
                if poly.ecDict[key] % rcoe != 0:
                    return rquo, rrem
                else:
                    rrem.ecDict[key] /= rcoe

        #若被除式最高次冪小於除式最高次冪則終止迭代
        while a_expmax >= b_exp[0]:
            quo_coe = rem_.ecDict[a_expmax]     #計算商式的係數，即當前被除式最高次冪項的係數
            quo_exp = a_expmax - b_exp[0]       #計算商式的次冪，即當前被除式最高次冪與除式最高次冪的差值
            # quo_((quo_exp, quo_coe))          #將結果添入商式字典

            #更新被除式係數及次冪狀態
            for exp in b_exp:
                rem_exp = exp + quo_exp
                rem_coe = -1 * rdid.ecDict[exp] * quo_coe
                rrem((rem_exp, rem_coe))
                    
            #更新被除式的最高次數
            try:
                a_expmax = max(rrem.ecDict.keys())
            except ValueError:
                # rrem = Polynomial()
                return rquo, rrem

        return rquo, rrem

    #求取pow_ = pow(self, exp_[, mod_])
    def __pow__(self, exp_, *args):
        if len(args) > 1:
            raise NTLExceptions.ArgumentError('Function \'pow\' expected at most 3 arguments, got %f.' %len(args))

        if not isinstance(exp_, int):
            raise NTLExceptions.IntError('The exponent must be integral.')

        pow_ = __import__('copy').deepcopy(self)
        pow_.var = 'x'

        for ctr in range(1, exp_):      pow_ *= pow_
        for mod_ in args:               pow_ %= mod_

        return pow_

    #求取self **= exp_
    def __ipow__(self, exp_):
        if not isinstance(exp_, int):
            raise NTLExceptions.IntError('The exponent must be integral.')

        pow_ = __import__('copy').deepcopy(self)
        pow_.var = 'x'

        for ctr in range(1, exp_):
            pow_ *= pow_

        return pow_

    #求取neg_ = -self
    def __neg__(self):
        neg_ = __import__('copy').deepcopy(self)
        for key in neg_.ecDict.keys():
            neg_.ecDict[key] *= -1
        return neg_

    #求取pos_ = +self
    def __pos__(self):
        pos_ = __import__('copy').deepcopy(self)
        return pos_

    #求取abs_ = abs(self)
    def __abs__(self):
        abs_ = __import__('copy').deepcopy(self)
        for key in abs_.ecDict.keys():
            abs_.ecDict[key] *= -1 if abs_.ecDict[key] < 0 else 1
        return abs_

    #求取self的導式
    def diff(self):
        de_ = Polynomial()

        for key in self.ecDict.keys():
            exp = key - 1 if key > 0 else 0
            coe = self.ecDict[key] * key if key > 0 else 0
            de_((exp, coe))

        return de_

    #求取self的積分
    def intg(self):
        ie_ = Polynomial()

        for key in self.ecDict.keys():
            exp = key + 1
            coe = 1.0 * self.ecDict[key] / key if key > 0 else self.ecDict[key]
            ie_((exp, coe))

        return ie_

    #求取self在x=num_時的值
    def eval(self, num_):
        if not numbercheck:
            raise NTLExceptions.NTLIntError('The argument must be a number.')

        poly = self.make_eval()
        rst_ = lambda x: eval(poly)

        return rst_(num_)
        # return (lambda x: eval(self.make_eval()))(num_)

    #用模重複平方法求self在x=num_時求模mod後的值
    def mod(self, num_, mod_):
        rst_ = 0
        for key_ in self.ecDict:
            coe_ = self.ecDict[key_] % mod_
            var_ = NTLRepetiveSquareModulo.repetiveSquareModulo(num_, key_, mod_)
            rst_ += (coe_ * var_) % mod_
        return rst_

    #將多項式字典轉化為其係數與次冪數組
    def dicttolist(self):
        coe = []
        exp = sorted(self.ecDict.keys(), reverse=True)
        for expitem in exp:
            coe.append(self.ecDict[expitem])

        return exp, coe

    #將字符串轉化為多項式
    def make_poly(self, poly_str):
        pass

    #生成可計算的多項式
    def make_eval(self):
        (expList, coeList) = self.dicttolist()

        polynomial = ''
        for ptr in xrange(len(expList)):
            polynomial += str(coeList[ptr]) + '*x**' + str(expList[ptr])
            if ptr < len(expList) - 1:
                polynomial += ' + '

        return polynomial

    #生成可計算的多項式的項
    def make_item(self):
        (expList, coeList) = self.dicttolist()

        items = []
        for ptr in xrange(len(expList)):
            item = ''
            item += str(coeList[ptr]) + '*x**' + str(expList[ptr])
            items.append(item)

        return items

# Polynomial.register(__import__('types').ClassType)

#數字參數檢查（整型、浮點、長整、複數）
def numbercheck(*args):
    for var in args:
        if not (isinstance(var, int) or isinstance(var, long)\
           or isinstance(var, float) or isinstance(var, complex)):
            return False
    return True

def poly(poly):
    if numbercheck(poly):       poly = Polynomial((0, poly))

    if isinstance(poly, str):   poly = self.make_poly(poly)

    if not isinstance(poly, Polynomial):
        raise NTLExceptions.PolyError('The argument cannot be tranfered into a polynomial.')

    return poly

if __name__ == '__main__':
    a = complex(1,3)
    poly_1 = Polynomial((1,3), (3,4), (2,2), (34,a), var='a')
    poly_2 = Polynomial((1,0), (4,-4), (2,3), (0,1))
    poly_3 = Polynomial((2,-1), (0,1))
    poly_4 = Polynomial((0,1))
    poly_5 = Polynomial((20140515,20140515), (201405,201495), (2014,2014), (8,8), (6,1), (3,4), (1,1), (0,1))
    poly_6 = Polynomial((7,1), (1,-1))
    poly_7 = poly_1 / poly_2
    
    print poly_1[:]
    print poly_2
    print poly_7
