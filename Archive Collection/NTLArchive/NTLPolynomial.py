# -*- coding: utf-8 -*-

#多項式類
#具備加減乘除運算的多項式實現

import NTLExceptions
import NTLPolynomialEuclideanDivision

class Polynomial:
    def __init__(self, *args):
        self.ecDict = {}

        for tpl in args:
            if not isinstance(tpl, tuple) or len(tpl) != 2:
                raise NTLExceptions.TupleError('The arguments must be tuples of exponents and coefficients.')

            if not isinstance(tpl[0], int) or not isinstance(tpl[1], int):
                raise NTLExceptions.IntError('The exponent and coefficient must be integral.')

            if tpl[0] < 0:      raise NTLExceptions.PNError('The exponent must be possitive.')

            if tpl[1] == 0:     continue

            try:
                self.ecDict[tpl[0]] += tpl[1]
            except KeyError:
                self.ecDict[tpl[0]] = tpl[1]

            if self.ecDict[tpl[0]] == 0:
                del self.ecDict[tpl[0]]

    def __call__(self, *args):
        for tpl in args:
            if not isinstance(tpl, tuple) or len(tpl) != 2:
                raise NTLExceptions.TupleError('The arguments must be tuples of exponents and coefficients.')

            if not isinstance(tpl[0], int) or not isinstance(tpl[1], int):
                raise NTLExceptions.IntError('The exponent and coefficients must be integral.')

            if tpl[0] < 0:      raise NTLExceptions.PNError('The exponent must be possitive.')

            if tpl[1] == 0:     continue

            try:
                self.ecDict[tpl[0]] += tpl[1]
            except KeyError:
                self.ecDict[tpl[0]] = tpl[1]

            if self.ecDict[tpl[0]] == 0:
                del self.ecDict[tpl[0]]

    #返回多項式對象的從屬
    def __repr__(self):
        return 'Polynomial()'

    #返回多項式的算術形式
    def __str__(self):
        if self.ecDict == {}:   return '0'

        string = ''
        (exp, coe) = self.dicttolist()

        if coe[0] < 0:
            string += '-'
        for ptr in xrange(len(exp)):
            if ptr > 0:
                if coe[ptr] < 0:
                    string += ' - '
                else:
                    string += ' + '

            if exp[ptr] == 0:
                if coe[ptr] == 0:
                    pass
                else:
                    string += '%d' %abs(coe[ptr])
            elif exp[ptr] == 1:
                if coe[ptr] == 0:
                    pass
                elif abs(coe[ptr]) == 1:
                    string += 'x'
                else:
                    string += '%dx' %abs(coe[ptr])
            else:
                if coe[ptr] == 0:
                    pass
                elif abs(coe[ptr]) == 1:
                    string += 'x^%d' %exp[ptr]
                else:
                    string += '%dx^%d' %(abs(coe[ptr]), exp[ptr])

        return string

    #返回self<poly的布爾值
    def __lt__(self, poly):
        if isinstance(poly, int):   poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The comparison is between two instances of Polynomial.')

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
        if isinstance(poly, int):   poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The comparison is between two instances of Polynomial.')

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
        if isinstance(poly, int):   poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = make_poly(poly)

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
        if isinstance(poly, int):   poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The comparison is between two instances of Polynomial.')

        if len(self) != len(poly):       return True
        
        a_coe = self.dicttolist()[1]
        b_coe = poly.dicttolist()[1]
        for ptr in range(len(a_coe)):
            if a_coe[ptr] != b_coe[ptr]:
                return True

        return False

    #返回self>poly的布爾值
    def __gt__(self, poly):
        if isinstance(poly, int):   poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The comparison is between two instances of Polynomial.')

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
        if isinstance(poly, int):   poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The comparison is between two instances of Polynomial.')

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
        return max(self.ecDict.keys())

    #返回key次項的係數
    def __getitem__(self, key):
        return self.ecDict[key]

    #修改key次項的係數為value
    def __setitem__(self, key, value):
        self.ecDict[key] = value

    #刪去key次項
    def __delitem__(self, key):
        del self.ecDict[key]

    #判斷一多項式是否含於多項式中
    def __contains__(self, poly):
        if isinstance(poly, int):   poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = make_poly(poly)

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

    #返回i至j-1次項的多項式
    def __getslice__(self, i, j):
        if not isinstance(i, int) or not isinstance(j, int):
            raise NTLExceptions.IntError('The arguments must be integral.')

        # if i < 0:   tmp_i = len(self) + i + 1;  i = 0 if tmp_i < 0 else tmp_i
        # if j < 0:   tmp_j = len(self) + j + 1;  j = 0 if tmp_j < 0 else tmp_j
        if j == 9223372036854775807:    j = len(self) + 1
        
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
        
        # if i < 0:   tmp_i = len(self) + i + 1;  i = 0 if tmp_i < 0 else tmp_i
        # if j < 0:   tmp_j = len(self) + j + 1;  j = 0 if tmp_j < 0 else tmp_j

        j = i + len(coe)
        for ptr in range(i, j):
            self.ecDict[ptr] = coe[ptr - i]
           
    #刪除i至j次項的多項式       
    def __delslice__(self, i, j):
        if not isinstance(i, int) or not isinstance(j, int):
            raise NTLExceptions.IntError('The arguments must be integral.')

        # if i < 0:   tmp_i = len(self) + i + 1;  i = 0 if tmp_i < 0 else tmp_i
        # if j < 0:   tmp_j = len(self) + j + 1;  j = 0 if tmp_j < 0 else tmp_j

        for ptr in range(i, j):
            try:
                del self.ecDict[ptr]
            except KeyError:
                pass

    #求取sum_ = self + poly
    def __add__(self, poly):
        if isinstance(poly, int):   poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = make_poly(poly)

        if not isinstance(poly, Polynomial): 
            raise NTLExceptions.PolyError('The addent must be an instance of Polynomial.')

        sum_ = __import__('copy').deepcopy(self)
        (b_exp, b_coe) = poly.dicttolist()
        for ptr in range(len(b_exp)):
            exp = b_exp[ptr]
            coe = b_coe[ptr]
            sum_((exp, coe))

        return sum_

    #求取rsum = poly + self
    def __radd__(self, poly):
        if isinstance(poly, int):   poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The augend must be an instance of Polynomial.')

        rsum = __import__('copy').deepcopy(poly)
        (b_exp, b_coe) = self.dicttolist()
        for ptr in range(len(b_exp)):
            exp = b_exp[ptr]
            coe = b_coe[ptr]
            rsum((exp, coe))

        return rsum

    #求取self += poly
    def __iadd__(self, poly):
        if isinstance(poly, int):   poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = make_poly(poly)

        if not isinstance(poly, Polynomial): 
            raise NTLExceptions.PolyError('The addent must be an instance of Polynomial.')

        sum_ = __import__('copy').deepcopy(self)
        (b_exp, b_coe) = poly.dicttolist()
        for ptr in range(len(b_exp)):
            exp = b_exp[ptr]
            coe = b_coe[ptr]
            sum_((exp, coe))

        return sum_

    #求取dif_ = self - poly
    def __sub__(self, poly):
        if isinstance(poly, int):   poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The subtrahend must be an instance of Polynomial.')

        dif_ = __import__('copy').deepcopy(self)
        (b_exp, b_coe) = poly.dicttolist()
        for ptr in range(len(b_exp)):
            exp = b_exp[ptr]
            coe = b_coe[ptr] * -1
            dif_((exp, coe))

        return dif_

    #求取rdif = poly - self
    def __rsub__(self, poly):
        if isinstance(poly, int):   poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The minuend must be an instance of Polynomial.')

        rdif = __import__('copy').deepcopy(poly)
        (b_exp, b_coe) = self.dicttolist()
        for ptr in range(len(b_exp)):
            exp = b_exp[ptr]
            coe = b_coe[ptr] * -1
            rdif((exp, coe))

        return rdif

    #求取self -= poly
    def __isub__(self, poly):
        if isinstance(poly, int):   poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The minuend must be an instance of Polynomial.')

        dif_ = __import__('copy').deepcopy(self)
        (b_exp, b_coe) = poly.dicttolist()
        for ptr in range(len(b_exp)):
            exp = b_exp[ptr]
            coe = b_coe[ptr] * -1
            dif_((exp, coe))

        return dif_

    #求取pro_ = self * poly
    def __mul__(self, poly):
        if isinstance(poly, int):   poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = make_poly(poly)

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
        if isinstance(poly, int):   poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = make_poly(poly)

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
        if isinstance(poly, int):   poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = make_poly(poly)

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
        if isinstance(poly, int):   poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The divisor must be an instance of Polynomial.')

        quo_ = Polynomial()
        quo_.ecDict = \
            NTLPolynomialEuclideanDivision.polyEDLoop(self.ecDict, poly.ecDict, {}, {})[0]

        return quo_

    #求取rquo = poly / self
    def __rdiv__(self, poly):
        if isinstance(poly, int):   poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The dividend must be an instance of Polynomial.')

        rquo = Polynomial()
        rquo.ecDict = \
            NTLPolynomialEuclideanDivision.polyEDLoop(poly.ecDict, self.ecDict, {}, {})[0]

        return rquo

    #求取self /= poly
    def __idiv__(self, poly):
        if isinstance(poly, int):   poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The divisor must be an instance of Polynomial.')

        quo_ = Polynomial()
        quo_.ecDict = \
            NTLPolynomialEuclideanDivision.polyEDLoop(self.ecDict, poly.ecDict, {}, {})[0]

        return quo_

    #求取quo_ = self // poly
    def __floordiv__(self, poly):
        if isinstance(poly, int):   poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The divisor must be an instance of Polynomial.')

        quo_ = Polynomial()
        quo_.ecDict = \
            NTLPolynomialEuclideanDivision.polyEDLoop(self.ecDict, poly.ecDict, {}, {})[0]

        return quo_

    #求取rquo = poly // self
    def __rfloordiv__(self, poly):
        if isinstance(poly, int):   poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The dividend must be an instance of Polynomial.')

        rquo = Polynomial()
        rquo.ecDict = \
            NTLPolynomialEuclideanDivision.polyEDLoop(poly.ecDict, self.ecDict, {}, {})[0]

        return rquo

    #求取self //= poly
    def __ifloordiv__(self, poly):
        if isinstance(poly, int):   poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The divisor must be an instance of Polynomial.')

        quo_ = Polynomial()
        quo_.ecDict = \
            NTLPolynomialEuclideanDivision.polyEDLoop(self.ecDict, poly.ecDict, {}, {})[0]

        return quo_

    #求取rat_ = self % poly
    def __mod__(self, poly):
        if isinstance(poly, int):   poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The divisor must be an instance of Polynomial.')

        rat_ = Polynomial()
        rat_.ecDict = \
            NTLPolynomialEuclideanDivision.polyEDLoop(self.ecDict, poly.ecDict, {}, {})[1]

        return rat_

    #求取rrat = poly % self
    def __rmod__(self, poly):
        if isinstance(poly, int):   poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The dividend must be an instance of Polynomial.')

        rrat = Polynomial()
        rrat.ecDict = \
            NTLPolynomialEuclideanDivision.polyEDLoop(poly.ecDict, self.ecDict, {}, {})[1]

        return rrat

    #求取self %= poly
    def __imod__(self, poly):
        if isinstance(poly, int):   poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The divisor must be an instance of Polynomial.')

        rat_ = Polynomial()
        rat_.ecDict = \
            NTLPolynomialEuclideanDivision.polyEDLoop(self.ecDict, poly.ecDict, {}, {})[1]

        return rat_

    #求取(quo_, rat_) = divmod(self, poly)
    def __divmod__(self, poly):
        if isinstance(poly, int):   poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The divisor must be an instance of Polynomial.')

        quo_ = Polynomial()
        rat_ = Polynomial()
        (quo_.ecDict, rat_.ecDict) = \
            NTLPolynomialEuclideanDivision.polyEDLoop(self.ecDict, poly.ecDict, {}, {})

        return quo_, rat_

    #求取(rquo, rrat) = rdivmod(poly, self)
    def __rdivmod__(self, poly):
        if isinstance(poly, int):   poly = Polynomial((0, poly))

        if isinstance(poly, str):   poly = make_poly(poly)

        if not isinstance(poly, Polynomial):
            raise NTLExceptions.PolyError('The dividend must be an instance of Polynomial.')

        rquo = Polynomial()
        rrat = Polynomial()
        (rquo.ecDict, rrat.ecDict) = \
            NTLPolynomialEuclideanDivision.polyEDLoop(poly.ecDict, self.ecDict, {}, {})

        return rquo, rrat

    #求取pow_ = pow(self, exp_[, mod_])
    def __pow__(self, exp_, *args):
        if len(args) > 1:
            raise NTLExceptions.ArgumentError('Function \'pow\' expected at most 3 arguments, got %d.' %len(args))

        if not isinstance(exp_, int):
            raise NTLExceptions.IntError('The exponent must be integral.')

        pow_ = __import__('copy').deepcopy(self)
        for ctr in range(1, exp_):
            pow_ *= pow_

        for arg in args:
            mod_ = arg
            pow_ %= mod_

        return pow_

    #求取self **= exp_
    def __ipow__(self, exp_):
        if not isinstance(exp_, int):
            raise NTLExceptions.IntError('The exponent must be integral.')

        pow_ = __import__('copy').deepcopy(self)
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

if __name__ == '__main__':
    poly_1 = Polynomial((1,-2), (3,4), (2,3), (34,1))
    poly_2 = Polynomial((1,0), (4,-4), (2,3))
    poly_3 = Polynomial((2,-1), (0,1))
    poly_4 = Polynomial((0,0))
    poly_5 = Polynomial((20140515,20140515), (201405,201495), (2014,2014), (8,8), (6,1), (3,4), (1,1), (0,1))
    poly_6 = Polynomial((7,1), (1,-1))
    poly_7 = abs(poly_1)

    print poly_1
    print poly_2
    print poly_7
