# -*- coding: utf-8 -*-

#同餘式類
#由多項式衍生的同餘式

import NTLExceptions
import NTLPolynomial
import NTLTrivialDivision
import NTLPrimeFactorisation
import NTLRepetiveSquareModulo
import NTLGreatestCommonDivisor

'''
TODO:

* Fix the bugs with self.solve()
'''

class Congruence(NTLPolynomial.Polynomial):

    __slots__ = ('modulo', 'pcflag')

    def __init__(self, *args, **kwargs):
        self.var = 'x'
        self.ecDict = {}
        self.modulo = None
        self.rcflag = False
        self.pcflag = False

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
            if kw == 'mod':
                if not isinstance(kwargs[kw], int) and not isinstance(kwargs[kw], long):
                    raise IntError('The modulo must be integral.')

                if kwargs[kw] <= 0:
                    raise PNError('The modulo must be positive')

                self.modulo = kwargs[kw]
                self.pcflag = NTLTrivialDivision.trivialDivision(self.modulo)

            elif kw == 'var':
                if not isinstance(kwargs[kw], str):
                    raise NTLExceptions.StringError('The argument must be a string.')

                self.var = kwargs[kw]

            else:
                raise NTLExceptions.KeywordError('Keyword \'%s\' is not defined.' %kw)

        if self.modulo == None:
            raise NTLExceptions.DefinitionError('The modulo of congruence must be assigned in advance.')

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

    #返回同餘式對象的從屬
    def __repr__(self):
        return 'Congruence(%s, mod=%d)' %(self.congeq.var, self.modulo)

    #返回同餘式的算術形式
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

        string += ' ≡ 0 (mod %d)' %self.modulo

        return string

    #用模重複平方法求self在x=num_時的值
    def eval(self, num_):
        rst_ = 0
        for key in self.ecDict:
            coe_ = self.ecDict[key] % self.modulo
            var_ = NTLRepetiveSquareModulo.repetiveSquareModulo(num_, key, self.modulo)
            rst_ += (coe_ * var_) % self.modulo

        return rst_

    #求取self在x=num_時的值
    def calc(self, num_):
        if not numbercheck:
            raise NTLExceptions.NTLIntError('The argument must be a number.')

        poly = self.make_eval()
        rst_ = lambda x: eval(poly)

        return rst_(num_)
        # return (lambda x: eval(self.make_eval()))(num_)

    #素數模同餘式的簡化
    def simplify(self):
        if not self.pcflag:
            raise NTLExceptions.PCError('The modulo must be prime for simplification.')

        dvs_cong = Congruence((self.modulo,1), (1,-1), mod=self.modulo)
        rst_cong = self % dvs_cong

        return rst_cong

    #任意模同餘式的求解
    def solve(self):
        if self.pcflag:
            return self.prime()
        else:
            return self.composit()

    #素數模的同餘式求解
    def prime(self):
        ratio = []

        #同餘式簡化
        rat_ = self.simplify() 
        
        for x in xrange(modulo):        #逐一驗算，如模為0則加入結果數組
            if self.calc_mod(x) == 0:
                ratio.append(x)

        return ratio

    #合數模的同餘式求解
    def composit(self):
        (p, q) = NTLPrimeFactorisation.primeFactorisation(self.modulo, wrap=True)      #分解模，以便判斷求解方式

        if len(p) == 1:     #若模為單素數的次冪，則調用primeLite()函數求解
            tmpMod = p[0]
            tmpExp = q[0]
            ratio = self.primeLite(tmpMod, tmpExp)
        else:               #若模為多素數的次冪，則逐一對其素因數調用primeLite()函數求解，再用中國剩餘定理處理
            tmpRto = []
            tmpMod = []
            for ptr in xrange(len(p)):
                tmpModVar = p[ptr]
                tmpExpVar = q[ptr]
                tmpMod.append(tmpModVar ** tmpExpVar)
                tmpRto.append(self.primeLite(tmpModVar, tmpExpVar))
            ratio = self.CTR(tmpRto, tmpMod)        #用中國剩餘定理處理上述結果，得到最終結果

        return ratio

    #單素數的次冪模同餘式求解
    def primeLite(self, mod, exp):
        tmpRto = self.prime(cgcExp, cgcCoe, mod)         #獲取源素數模的同餘式的解
        if exp == 1:
            return tmpRto
        
        ratio = self.primePro(tmpRto, mod, exp)     #作高次同餘式的提升，求出源素數次冪模的同餘式的解
        return ratio

    #高次同餘式的提升
    def primePro(self, rto, mod, exp):
        drv = self.diff()   #求取原同餘式的導式
        
        for tmpRto in rto:
            #尋找滿足(f'(x1),p)=1的x1
            if NTLGreatestCommonDivisor.greatestCommonDivisor(drv.eval(tmpRto), mod) == 1:
                x = tmpRto
                drvMod = drv.mod(tmpRto, mod) - mod #計算導式的值f'(x1) (mod p)，取其負值
                drvRcp = 1 / polyDrvMod
                break

        for ctr in xrange(0, exp):
            t = ((-1 * self.calc(x) / (mod**ctr)) * drvRcp) % mod          #t_(i-1) ≡ (-f(x_i)/p^i) * (f'(x1)^-1 (mod p)) (mod p)
            x += (t * (mod**ctr)) % (mod**(ctr+1))                      #x_i ≡ x_(i-1) + t_(i-1) * p^(i-1) (mod p^i)

        return x    #ratio = x

    #中國剩餘定理
    def CTR(self, rto, mod):
        print rto
        print mod
        modulo = 1
        for tmpMod1 in mod:
            modulo *= tmpMod1                                   #M(original modulo) = ∏m_i

        bList = []
        for tmpMod2 in mod:
            M = modulo / tmpMod2                                #M_i = M / m_i
            t = prmMCS([1,0], [M,-1], tmpMod2)[0]               #t_i * M_i ≡ 1 (mod m_i)
            bList.append(t * M)                                 #b_i = t_i * M_i

        ratio = self.iterCalc(rto, bList, modulo)                    #x_j = Σ(b_i * r_i) (mod M)                          
        return ratio

    #對rto多維數組（層，號）中的數進行全排列並計算結果
    def iterCalc(self, ognList, coeList, modulo):
        ptrList = []                            #寄存指向每一數組層的號
        lvlList = []                            #寄存每一數組層的最大號
        for tmpList in ognList:
            ptrList.append(len(tmpList)-1)
            lvlList.append(len(tmpList)-1)
     
        flag = 1
        rstList = []

        while flag:
            ptrNum = 0
            rstNum = 0
            for ptr in ptrList:
                rstNum += ognList[ptrNum][ptr] * coeList[ptrNum]    #計算結果
                ptrNum += 1

            rstList.append(rstNum % modulo)
            (ptrList, flag) = self.updateState(ptrList, lvlList)         #更新ptrList的寄存值，並返回是否結束循環

        return rstList

    #更新ptrList的寄存值，並返回是否已遍歷所有組合
    def updateState(self, ptrList, lvlList):
        ptr = 0
        flag = 1
        glbFlag = 1

        while flag:                                 #未更新寄存數值前，保持循環（類似同步計數器）
            if ptrList[ptr] > 0:                    #該層未遍歷，更新該層，終止循環
                ptrList[ptr] -= 1                   
                flag = 0
            else:                                   #該層已遍歷
                if ptr < len(lvlList) - 1:          #更新指針至下一層並接著循環
                    ptrList[ptr] = lvlList[ptr]
                    ptr += 1
                else:                               #所有情況均已遍歷，終止循環
                    flag = 0
                    glbFlag = 0

        return ptrList, glbFlag

#數字參數檢查（整型、浮點、長整、複數）
def numbercheck(*args):
    for var in args:
        if not (isinstance(var, int) or isinstance(var, long)\
           or isinstance(var, float) or isinstance(var, complex)):
            return False
    return True

if __name__ == '__main__':
    con_ = Congruence((2,1), (1,-46), mod=105, var='z')
    ratio = con_.solve()
    
    print 'The solution of x^2 ≡ 46 (mod 105) is\n\tx ≡',
    for rst in ratio:
        print '%d' %rst,
    print '(mod %d)' %105

