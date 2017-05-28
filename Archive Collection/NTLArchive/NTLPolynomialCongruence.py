# -*- coding: utf-8 -*-

#同餘式求解
#任意模的同餘式的求解

import NTLExceptions
import NTLTrivialDivision
import NTLPrimeFactorisation
import NTLRepetiveSquareModulo
import NTLGreatestCommonDivisor
import NTLCongruenceSimplification

def polynomialCongruence(cgcExp, cgcCoe, modulo):
    if not isinstance(modulo, int):
        raise NTLExceptions.IntError('The modulo must be integral.')

    if not isinstance(cgcExp, list) or not isinstance(cgcCoe, list):
        raise NTLExceptions.ListError('The arguments must be list type.')

    if modulo < 1:
        raise NTLExceptions.PNError('The modulo must be positive.')

    if NTLTrivialDivision.trivialDivision(modulo):                 #判斷模的素性
        ratio = prmMCS(cgcExp, cgcCoe, modulo)  #如為素數模則調用prmMCS()函數
    else:
        ratio = cpsMCS(cgcExp, cgcCoe, modulo)  #如為合數模則調用cpsMCS()函數

    if len(ratio) == 0:
        raise NTLExceptions.SolutionError('The polynomial congruence has no integral solution.')

    return sorted(ratio)

#素數模的同餘式求解
def prmMCS(cgcExp, cgcCoe, modulo):
    ratio = []

    #同餘式簡化
    (rtoExp, rtoCoe) = NTLCongruenceSimplification.congruenceSimplification(cgcExp, cgcCoe, modulo) 
    polyCgc = makePolynomial(rtoExp, rtoCoe)    #將係數與指數數組生成多項式

    r = lambda x : eval(polyCgc)                #用於計算多項式的取值
    for x in xrange(modulo):                    #逐一驗算，如模為0則加入結果數組
        if r(x) % modulo == 0:
            ratio.append(x)

    return ratio

#生成多項式
def makePolynomial(expList, coeList):
    polynomial = ''
    for ptr in xrange(len(expList)):
        polynomial += str(coeList[ptr]) + '*x**' + str(expList[ptr])
        if ptr < len(expList) - 1:
            polynomial += ' + '

    return polynomial

#合數模的同餘式求解
def cpsMCS(cgcExp, cgcCoe, modulo):
    fct = NTLPrimeFactorisation.primeFactorisation(modulo)      #分解模，以便判斷求解方式
    (p, q) = wrap(fct)                                          #生成因數表p與指數表q

    if len(p) == 1:     #若模為單素數的次冪，則調用prmMCSLite()函數求解
        tmpMod = p[0]
        tmpExp = q[0]
        ratio = prmMCSLite(cgcExp, cgcCoe, tmpMod, tmpExp)
    else:               #若模為多素數的次冪，則逐一對其素因數調用prmMCSLite()函數求解，再用中國剩餘定理處理
        tmpRto = []
        tmpMod = []
        for ptr in xrange(len(p)):
            tmpModVar = p[ptr]
            tmpExpVar = q[ptr]
            tmpMod.append(tmpModVar ** tmpExpVar)
            tmpRto.append(prmMCSLite(cgcExp, cgcCoe, tmpModVar, tmpExpVar))
        ratio = CHNRemainderTheorem(tmpRto, tmpMod)              #用中國剩餘定理處理上述結果，得到最終結果

    return ratio

def wrap(table):
    p = [];     q = []
    if table[0] == -1:  del p[0]

    ctr = 1
    for i in range(1,len(table)):
        if table[i] == table[i-1]:  ctr += 1        #重複因數，計數器自增
        else:                                       #互異因數，將前項及其計數器添入因數表與指數表，並重置計數器
            p.append(table[i-1]); q.append(ctr); ctr = 1
        
        if i == len(table)-1:                       #將最後一個因數及其計數器添入因數表與指數表
            p.append(table[i]); q.append(ctr)

    if len(table) == 1:                             #因數只有一個的特殊情況
            p.append(table[-1]);  q.append(1)

    return p, q

#單素數的次冪模同餘式求解
def prmMCSLite(cgcExp, cgcCoe, mod, exp):
    tmpRto = prmMCS(cgcExp, cgcCoe, mod)                    #獲取源素數模的同餘式的解
    if exp == 1:
        return tmpRto
    
    ratio = prmMCSPro(cgcExp, cgcCoe, tmpRto, mod, exp)     #作高次同餘式的提升，求出源素數次冪模的同餘式的解
    return ratio

#高次同餘式的提升
def prmMCSPro(cgcExp, cgcCoe, rto, mod, exp):
    (drvExp, drvCoe) = polyDerivative(cgcExp, cgcCoe)   #求取原同餘式的導式
    polyDrv = makePolynomial(drvExp, drvCoe)
    #print polyDrv
    
    drv = lambda x : eval(polyDrv)
    for tmpRto in rto:
        #尋找滿足(f'(x1),p)=1的x1
        if NTLGreatestCommonDivisor.greatestCommonDivisor(drv(tmpRto), mod) == 1:
            polyDrvMod = 0
            #用模重複平方法計算導式的值f'(x1) (mod p)
            for ptr in xrange(len(drvExp)):     
                polyDrvMod += NTLRepetiveSquareModulo.repetiveSquareModulo(drvCoe[ptr]*tmpRto, drvExp[ptr], mod)

            x = tmpRto
            polyDrvMod = polyDrvMod % mod - mod
            polyDrvRcp = 1 / polyDrvMod
            #print x
            #print polyDrvMod
            break

    for ctr in xrange(0, exp):
        poly = makePolynomial(cgcExp, cgcCoe)
        fx = lambda x : eval(poly)
        t = ((-1 * fx(x) / (mod**ctr)) * polyDrvRcp) % mod          #t_(i-1) ≡ (-f(x_i)/p^i) * (f'(x1) (mod p)) (mod p)
        x += (t * (mod**ctr)) % (mod**(ctr+1))                      #x_i ≡ x_(i-1) + t_(i-1) * p^(i-1) (mod p^i)

    return x    #ratio = x

#求取多項式的導式
def polyDerivative(cgcExp, cgcCoe):
    drvExp = []
    drvCoe = []

    for ptr in xrange(len(cgcExp)):
        if cgcExp[ptr] != 0:                            #若該項次數不為0，即不為常數項，則需添加至導式中
            drvExp.append(cgcExp[ptr] - 1)              #該項次數減一
            drvCoe.append(cgcCoe[ptr] * cgcExp[ptr])    #該項係數為原係數乘原次數

    return drvExp, drvCoe

#中國剩餘定理
def CHNRemainderTheorem(rto, mod):
    modulo = 1
    for tmpMod1 in mod:
        modulo *= tmpMod1                                   #M(original modulo) = ∏m_i

    bList = []
    for tmpMod2 in mod:
        M = modulo / tmpMod2                                #M_i = M / m_i
        t = prmMCS([1,0], [M,-1], tmpMod2)[0]               #t_i * M_i ≡ 1 (mod m_i)
        bList.append(t * M)                                 #b_i = t_i * M_i

    ratio = iterCalc(rto, bList, modulo)                    #x_j = Σ(b_i * r_i) (mod M)                          
    return ratio

#對rto多維數組（層，號）中的數進行全排列並計算結果
def iterCalc(ognList, coeList, modulo):
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
        (ptrList, flag) = updateState(ptrList, lvlList)         #更新ptrList的寄存值，並返回是否結束循環

    return rstList

#更新ptrList的寄存值，並返回是否已遍歷所有組合
def updateState(ptrList, lvlList):
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

if __name__ == '__main__':
    '''
    cgcExp = [20140515, 201405, 2014, 8, 6, 3, 1, 0]
    cgcCoe = [20140515, 201495, 2014, 8, 1, 4, 1, 1]
    modulo = 343
    '''
    #'''
    cgcExp = [2, 0]
    cgcCoe = [1, -46]
    modulo = 105
    #'''
    '''
    cgcExp = [2, 0]
    cgcCoe = [1, -1219]
    modulo = 2310
    '''

    print 
    for ptr in xrange(len(cgcExp)):
        print '%dx^%d' %(cgcCoe[ptr], cgcExp[ptr]),
        if ptr < len(cgcExp) - 1:
            print '+',
    print '≡ 0 (mod %d)' %modulo

    ratio = polynomialCongruence(cgcExp, cgcCoe, modulo)

    print 'The solution of the above polynomial congruence is\n\tx ≡',
    for rst in ratio:
        print '%d' %rst,
    print '(mod %d)' %modulo
