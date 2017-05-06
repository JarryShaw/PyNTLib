# -*- coding: utf-8 -*-

#同餘式求解
#任意模的同餘式的求解

import math

def congruenceSolution(cgcExp, cgcCoe, modulo):
    if trivialDivision(modulo):                 #判斷模的素性
        ratio = prmMCS(cgcExp, cgcCoe, modulo)  #如為素數模則調用prmMCS()函數
    else:
        ratio = cpsMCS(cgcExp, cgcCoe, modulo)  #如為合數模則調用cpsMCS()函數

    if len(ratio) == 0:
        raise ValueError("The congruence has no solution.")

    return sorted(ratio)

#素數模的同餘式求解
def prmMCS(cgcExp, cgcCoe, modulo):
    ratio = []

    (rtoExp, rtoCoe) = congruenceSimplification(cgcExp, cgcCoe, modulo) #同餘式簡化
    polyCgc = makePolynomial(rtoExp, rtoCoe)                            #將係數與指數數組生成多項式

    r = lambda x : eval(polyCgc)                                        #用於計算多項式的取值
    for x in xrange(modulo):                                             #逐一驗算，如模為0則加入結果數組
        if r(x) % modulo == 0:
            ratio.append(x)

    return ratio

#同餘式簡化 | 素數模的同餘式的簡化
def congruenceSimplification(cgcExp, cgcCoe, modulo):
    dvsExp = [modulo, 1]
    dvsCoe = [1, -1]
    (qttExp, qttCoe, rtoExp, rtoCoe) = polynomialEuclideanDivision(cgcExp, cgcCoe, dvsExp, dvsCoe)

    return rtoExp, rtoCoe

#多項式歐幾里德除法 | 求解多項式的廣義歐幾里德除法
def polynomialEuclideanDivision(dvdExp, dvdCoe, dvsExp, dvsCoe):
    #將被除式係數與次冪添入被除式字典
    ecDictDivident = {}
    for ptr in xrange(len(dvdExp)):
        ecDictDivident[dvdExp[ptr]] = dvdCoe[ptr]

    #將除式係數與次冪添入除式字典
    ecDictDivisor = {}
    for ptr in xrange(len(dvsExp)):
        ecDictDivisor[dvsExp[ptr]] = dvsCoe[ptr]

    #print ecDictDivident
    #print ecDictDivisor

    #計算商式與餘式的字典結果
    ecDictQuotient = {}
    ecDictRatio = {}
    ecDictQuotient, ecDictRatio = polyEDLoop(ecDictDivident, ecDictDivisor, ecDictQuotient, ecDictRatio)

    #print ecDictQuotient
    #print ecDictRatio

    #將商式字典轉為係數與次冪數組
    qttCoe = []
    qttExp = sorted(ecDictQuotient.keys(), reverse=True)
    for exp in qttExp:
        qttCoe.append(ecDictQuotient[exp])

    #將餘式字典轉為係數與次冪數組
    rtoCoe = []
    rtoExp = sorted(ecDictRatio.keys(), reverse=True)
    for rto in rtoExp:
        rtoCoe.append(ecDictRatio[rto])

    return qttExp, qttCoe, rtoExp, rtoCoe

#歐氏除法的循環求解
def polyEDLoop(ecDictDivident, ecDictDivisor, ecDictQuotient, ecDictRatio):
    ecDDvdExpMax = max(ecDictDivident.keys())               #獲取被除式的最高次數
    #print ecDDvdExpMax
    ecDDvsExp = sorted(ecDictDivisor.keys(), reverse=True)  #獲取除式的指數列（降序）

    #若除式最高次冪的係數不為1，則終止程式
    if ecDictDivisor[ecDDvsExp[0]] != 1:
        raise KeyError('The coefficient of the univariate with greatest degree in divisor must be 1.')

    #若被除式最高次冪小於除式最高次冪則終止迭代
    while ecDDvdExpMax >= ecDDvsExp[0]:
        ecDQttCoe = ecDictDivident[ecDDvdExpMax]    #計算商式的係數，即當前被除式最高次冪項的係數
        ecDQttExp = ecDDvdExpMax - ecDDvsExp[0]     #計算商式的次冪，即當前被除式最高次冪與除式最高次冪的差值
        ecDictQuotient[ecDQttExp] = ecDQttCoe       #將結果添入商式字典
        
        #更新被除式係數及次冪狀態
        for exp in ecDDvsExp:
            if ecDictDivident.has_key(exp+ecDQttExp):
                ecDictDivident[exp+ecDQttExp] -= ecDictDivisor[exp] * ecDQttCoe
                if ecDictDivident[exp+ecDQttExp] == 0:
                    ecDictDivident.pop(exp+ecDQttExp)
            else:
                ecDictDivident[exp+ecDQttExp] = -1 * ecDictDivisor[exp] * ecDQttCoe
                
        #更新被除式的最高次數
        ecDDvdExpMax = max(ecDictDivident.keys())               

    ecDictRatio = ecDictDivident.copy()     #此時，餘式即為被除式所剩餘項
    return ecDictQuotient, ecDictRatio

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
    (p, q, pn) = primeFactorisation(modulo)                     #分解模，以便判斷求解方式

    if len(p) == 1:                                             #若模為單素數的次冪，則調用prmMCSLite()函數求解
        tmpMod = p[0]
        tmpExp = q[0]
        ratio = prmMCSLite(cgcExp, cgcCoe, tmpMod, tmpExp)
    else:                                                       #若模為多素數的次冪，則逐一對其素因數調用prmMCSLite()函數求解，再用中國剩餘定理處理
        tmpRto = []
        tmpMod = []
        for ptr in xrange(len(p)):
            tmpModVar = p[ptr]
            tmpExpVar = q[ptr]
            tmpMod.append(tmpModVar ** tmpExpVar)
            tmpRto.append(prmMCSLite(cgcExp, cgcCoe, tmpModVar, tmpExpVar))
        ratio = CHNRemainderTheorem(tmpRto, tmpMod)      #用中國剩餘定理處理上述結果，得到最終結果

    return ratio

#素因數分解 | 返回一給定整數的標準（素因數）分解式
def primeFactorisation(N, pn=0, p=[], q=[]):
    if N < 0:   pn = 1; N = -1 * N                              #將負數轉化為正整數進行計算
    if N == 0: p.append(0); q.append(1); return p, q, pn        #N為0時的分解
    if N == 1: p.append(1); q.append(1); return p, q, pn        #N為1時的分解
    
    prmList = eratosthenesSieve(N+1)        #獲取素數表
    tmp = euclideanDivision(N, prmList)     #獲取分解因數表
    (p,q) = wrap(tmp, p, q)                 #生成因數表p與指數表q
    
    return p, q, pn

#歐幾里得除法 | 判斷是否整除，即b|a
def euclideanDivision(N, prmList, rst=[]):
    if N == 1:  return rst  #除盡後返回因素序列
    
    for prm in prmList:     #逐個（遞歸）嘗試歐幾里得除法，尋找因數
        if N % prm == 0:    rst.append(prm); N = N / prm;    break
    return euclideanDivision(N, prmList, rst)

def wrap(set, p, q):
    ctr = 1
    for i in xrange(1,len(set)):
        if set[i] == set[i-1]:  ctr += 1        #重複因數，計數器自增
        else:                                   #互異因數，將前項及其計數器添入因數表與指數表，並重置計數器
            p.append(set[i-1]); q.append(ctr); ctr = 1
        
        if i == len(set)-1:                     #將最後一個因數及其計數器添入因數表與指數表
            p.append(set[i]); q.append(ctr)

    if len(set) == 1:                           #因數只有一個的特殊情況
        p.append(set[-1]);  q.append(1)
    
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
        #print 'x1 = ', tmpRto
        #print 'p = ', mod
        #print '(f\'(x1),p) = ', GCD(drv(tmpRto), mod)
        if GCD(drv(tmpRto), mod) == 1:          #尋找滿足(f'(x1),p)=1的x1
            polyDrvMod = 0
            for ptr in xrange(len(drvExp)):     #用模重複平方法計算導式的值f'(x1) (mod p)
                polyDrvMod += repetiveSquareModulo(drvCoe[ptr]*tmpRto, drvExp[ptr], mod)

            x = tmpRto
            polyDrvMod = polyDrvMod % mod - mod
            polyDrvRcp = 1 / polyDrvMod
            #print x
            #print polyDrvMod
            break

    for ctr in xrange(0, exp):
        '''
        t = 0
        for ptr in xrange(len(cgcExp)):                             #用模重複平方法計算t_(i-1)與x_i
            cgcBase = ((-1 * cgcCoe[ptr]) / (mod**ctr)) * polyDrvRcp
            t += repetiveSquareModulo(cgcBase, cgcExp[ptr], mod)    #t_(i-1) ≡ (-f(x_i)/p^i) * (f'(x1) (mod p)) (mod p)
        t %= mod
        '''
        poly = makePolynomial(cgcExp, cgcCoe)
        fx = lambda x : eval(poly)
        t = ((-1 * fx(x) / (mod**ctr)) * polyDrvRcp) % mod          #t_(i-1) ≡ (-f(x_i)/p^i) * (f'(x1) (mod p)) (mod p)
        x += (t * (mod**ctr)) % (mod**(ctr+1))                      #x_i ≡ x_(i-1) + t_(i-1) * p^(i-1) (mod p^i)
        #print x, ' ', t

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

#模重複平方法 | 求解b^n (mod m)的值
def repetiveSquareModulo(base, exponent, divisor):
    get_bin = lambda x: format(x, 'b')  #二進制轉化函數

    exp_bin = get_bin(exponent)         #將指數轉為二進制
    ptr = len(exp_bin) - 1

    a = 1           
    b = base        
    n = exp_bin     
    while ptr >= 0:
        a = a * b**int(n[ptr]) % divisor    #a_i ≡ a_i-1 * b_i ^ n_i (mod divisor)
        b = b**2 % divisor                  #b_i ≡ b_i-1 ^ 2 (mod divisor)
        ptr -= 1

    return a                                #base ^ exponent ≡ a_k-1 (mod divisor)

#廣義歐幾里德除法 | 返回100,000內任意兩整數的最大公因數
def GCD(a=1, b=1):
    if a < 0:   a = -1 * a              #將a轉為正整數進行計算
    if b < 0:   b = -1 * b              #將b轉為正整數進行計算
    if a < b:   c = a;  a = b;  b = c   #交換a與b的次序，使得a≥b
    if b == 0:  return a                #(r,0) = r
    
    r = a % b
    return GCD(r, b)                    #(a,b) = (r_-2,r_-1) = (r_-1,r_0) = … = (r_n,r_n+1) = (r_n,0) = r_n

#中國剩餘定理
def CHNRemainderTheorem(rto, mod):
    modulo = 1
    for tmpMod1 in mod:
        modulo *= tmpMod1                                   #M(original modulo) = ∏m_i

    bList = []
    for tmpMod2 in mod:
        M = modulo / tmpMod2                                #M_i = M / m_i
        t = int(prmMCS([1,0], [M,-1], tmpMod2)[0])          #t_i * M_i ≡ 1 (mod m_i)
        bList.append(t * M)                                 #b_i = t_i * M_i
    
    #print 'b = ', bList
    #print 'r = ', rto

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
    #print 'p = ', ptrList
    while flag:
        ptrNum = 0
        rstNum = 0
        for ptr in ptrList:
            rstNum += ognList[ptrNum][ptr] * coeList[ptrNum]    #計算結果
            ptrNum += 1

        #print 'p = ', ptrList
        rstList.append(rstNum % modulo)
        (ptrList, flag) = updateState(ptrList, lvlList)         #更新ptrList的寄存值，並返回是否結束循環

    return rstList

'''
def checkState(objList):
    tmpString = ''
    for obj in objList:
        tmpString += str(obj)

    if int(tmpString) != 0:
        return 1
    else:
        return 0
'''

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

    #print 'p = ', ptrList
    return ptrList, glbFlag

if __name__ == '__main__':
    #'''
    cgcFlg = True
    cgcExp = []
    cgcCoe = []
    print 'Please type as the instruction.\n-1 for exponent means stop the input process.\n'
    while cgcFlg:
        if cgcFlg == False:
            break
        try:
            a = int(raw_input('The exponent of the univariate in polynomial is '))
            if a < -1:
                print 'Possitve number for exponent. -1 for abortion.\n'
                continue
            if a == -1:
                cgcFlg = False
                break
            b = int(raw_input('The coefficient of the above univariate is '))
        except ValueError:
            print 'Invalid input, please redo.\n'
            continue
        cgcExp.append(a)
        cgcCoe.append(b)
        print
    print
    #'''
    '''
    cgcExp = [20140515, 201405, 2014, 8, 6, 3, 1, 0]
    cgcCoe = [20140515, 201495, 2014, 8, 1, 4, 1, 1]
    modulo = 343
    '''
    '''
    cgcExp = [2, 0]
    cgcCoe = [1, -46]
    modulo = 105
    '''
    '''
    cgcExp = [2, 0]
    cgcCoe = [1, -1219]
    modulo = 2310
    '''
    #'''
    while True:
        try:
            modulo = int(raw_input('The modulo is '))
            if modulo < 1:
                print 'The modulo must be greater than 0.'
                continue
        except ValueError:
            print 'Invalid input.'
            continue
        break
    #'''

    print 
    for ptr in xrange(len(cgcExp)):
        print '%dx^%d' %(cgcCoe[ptr], cgcExp[ptr]),
        if ptr < len(cgcExp) - 1:
            print '+',
    print '≡ 0 (mod %d)' %modulo

    ratio = congruenceSolution(cgcExp, cgcCoe, modulo)

    print 'The solution of the above polynomial congruence is\nx ≡',
    for rst in ratio:
        print '%d' %rst,
    print '(mod %d)\n' %modulo
