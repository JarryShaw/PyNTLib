# -*- coding: utf-8 -*-


# 同餘式求解
# 任意模的同餘式的求解


from .NTLChineseRemainderTheorem  import CHNRemainderTheorem
from .NTLCongruenceSimplification import congruenceSimplification
from .NTLExceptions               import SolutionError
from .NTLGreatestCommonDivisor    import greatestCommonDivisor
from .NTLPrimeFactorisation       import primeFactorisation
from .NTLRepetiveSquareModulo     import repetiveSquareModulo
from .NTLTrivialDivision          import trivialDivision
from .NTLUtilities                import jsrange
from .NTLValidations              import int_check, list_check, pos_check


__all__  = ['polynomialCongruence',
            'prmMCS', 'cpsMCS',
            'prmMCSLite', 'prmMCSPro',
            'makePolynomial', 'polyDerivative']
nickname =  'congsolve'


'''Usage sample:

# 1st set:
cgcExp = [20140515, 201405, 2014, 8, 6, 3, 1, 0]
cgcCoe = [20140515, 201495, 2014, 8, 1, 4, 1, 1]
modulo = 343

# 2nd set:
cgcExp = [2, 0]
cgcCoe = [1, -46]
modulo = 105

# 3rd set:
cgcExp = [2, 0]
cgcCoe = [1, -1219]
modulo = 2310

for ptr in range(len(cgcExp)):
    print('%dx^%d' % (cgcCoe[ptr], cgcExp[ptr]), end=' ')
    if ptr < len(cgcExp) - 1:
        print('+', end=' ')
print('≡ 0 (mod %d)' % modulo)

remainder = congsolve(cgcExp, cgcCoe, modulo)

print('The solution of the above polynomial congruence is\n\tx ≡', end=' ')
for rst in remainder:
    print('%d' % rst, end=' ')
print('(mod %d)' % modulo)

'''


def polynomialCongruence(cgcExp, cgcCoe, modulo, **kwargs):
    list_check(cgcExp, cgcCoe)
    int_check(modulo);  pos_check(modulo)

    trust = False
    for kw in kwargs:
        if kw != 'trust':
            raise KeywordError('Keyword \'%s\' is not defined.' % kw)
        else:
            trust = kwargs[kw];     bool_check(trust)

    if trust or trivialDivision(modulo):            # 判斷模的素性
        remainder = prmMCS(cgcExp, cgcCoe, modulo)  # 如為素數模則調用prmMCS()函數
    else:
        remainder = cpsMCS(cgcExp, cgcCoe, modulo)  # 如為合數模則調用cpsMCS()函數

    if len(remainder) == 0:
        raise SolutionError('The polynomial congruence has no integral solution.')

    return sorted(remainder)


# 素數模的同餘式求解
def prmMCS(cgcExp, cgcCoe, modulo):
    remainder = []

    # 同餘式簡化
    (rmdExp, rmdCoe) = congruenceSimplification(cgcExp, cgcCoe, modulo)
    polyCgc = makePolynomial(rmdExp, rmdCoe)    # 將係數與指數數組生成多項式

    r = lambda x: eval(polyCgc)                 # 用於計算多項式的取值
    for x in jsrange(modulo):                   # 逐一驗算，如模為0則加入結果數組
        if r(x) % modulo == 0:
            remainder.append(x)

    return remainder


# 生成多項式
def makePolynomial(expList, coeList):
    polynomial = ''
    for ptr in jsrange(len(expList)):
        polynomial += str(coeList[ptr]) + '*x**' + str(expList[ptr])
        if ptr < len(expList) - 1:
            polynomial += ' + '

    return polynomial


# 合數模的同餘式求解
def cpsMCS(cgcExp, cgcCoe, modulo):
    # 分解模，以便判斷求解方式, 並生成因數表p與指數表q
    (p, q) = primeFactorisation(modulo, wrap=True)

    if len(p) == 1:     # 若模為單素數的次冪，則調用prmMCSLite()函數求解
        tmpMod = p[0]
        tmpExp = q[0]
        remainder = prmMCSLite(cgcExp, cgcCoe, tmpMod, tmpExp)
    else:               # 若模為多素數的次冪，則逐一對其素因數調用prmMCSLite()函數求解，再用中國剩餘定理處理
        tmpRmd = []
        tmpMod = []
        for ptr in jsrange(len(p)):
            tmpModVar = p[ptr]
            tmpExpVar = q[ptr]
            tmpMod.append(tmpModVar ** tmpExpVar)
            tmpRmd.append(prmMCSLite(cgcExp, cgcCoe, tmpModVar, tmpExpVar))

        # 用中國剩餘定理處理上述結果，得到最終結果
        remainder = CHNRemainderTheorem(*zip(tmpMod, tmpRmd))

    return remainder


# 單素數的次冪模同餘式求解
def prmMCSLite(cgcExp, cgcCoe, mod, exp):
    # 獲取源素數模的同餘式的解
    tmpRmd = prmMCS(cgcExp, cgcCoe, mod)
    if exp == 1:    return tmpRmd

    # 作高次同餘式的提升，求出源素數次冪模的同餘式的解
    remainder = prmMCSPro(cgcExp, cgcCoe, tmpRmd, mod, exp)
    return remainder


# 高次同餘式的提升
def prmMCSPro(cgcExp, cgcCoe, rmd, mod, exp):
    # 求取原同餘式的導式
    (drvExp, drvCoe) = polyDerivative(cgcExp, cgcCoe)
    polyDrv = makePolynomial(drvExp, drvCoe)

    drv = lambda x: eval(polyDrv)
    for tmpRmd in rmd:
        # 尋找滿足(f'(x1),p)=1的x1
        if greatestCommonDivisor(drv(tmpRmd), mod) == 1:
            polyDrvMod = 0
            # 用模重複平方法計算導式的值f'(x1) (mod p)
            for ptr in jsrange(len(drvExp)):
                polyDrvMod += repetiveSquareModulo(drvCoe[ptr]*tmpRmd, drvExp[ptr], mod)

            x = tmpRmd
            polyDrvMod = polyDrvMod % mod - mod
            polyDrvRcp = 1 / polyDrvMod
            break

    for ctr in jsrange(0, exp):
        poly = makePolynomial(cgcExp, cgcCoe)
        fx = lambda x: eval(poly)
        # t_(i-1) ≡ (-f(x_i)/p^i) * (f'(x1) (mod p)) (mod p)
        t = ((-1 * fx(x) / (mod**ctr)) * polyDrvRcp) % mod
        # x_i ≡ x_(i-1) + t_(i-1) * p^(i-1) (mod p^i)
        x += (t * (mod**ctr)) % (mod**(ctr+1))

    return [x]    # remainder = x


# 求取多項式的導式
def polyDerivative(cgcExp, cgcCoe):
    drvExp = []
    drvCoe = []

    for ptr in jsrange(len(cgcExp)):
        if cgcExp[ptr] != 0:                            # 若該項次數不為0，即不為常數項，則需添加至導式中
            drvExp.append(cgcExp[ptr] - 1)              # 該項次數減一
            drvCoe.append(cgcCoe[ptr] * cgcExp[ptr])    # 該項係數為原係數乘原次數

    return drvExp, drvCoe
