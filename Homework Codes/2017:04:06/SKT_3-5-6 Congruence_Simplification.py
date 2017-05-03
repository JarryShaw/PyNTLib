# -*- coding: utf-8 -*-

#同餘式簡化
#素數模的同餘式的簡化

import math

def congruenceSimplification(cgcExp, cgcCoe, modulo):
    if not trivialDivision(modulo):
        print 'The modulo is composit. Only prime modulo accepted.'
        raise KeyError

    dvsExp = [modulo, 1]
    dvsCoe = [1, -1]
    (qttExp, qttCoe, rtoExp, rtoCoe) = polynomialEuclideanDivision(cgcExp, cgcCoe, dvsExp, dvsCoe)

    return rtoExp, rtoCoe

#平凡除法 | 對100,000內的整數素性判斷
def trivialDivision(N=2):
    if N < 0:   N = -1 * N
    if N == 1 or N == 0:    raise ValueError
    
    set = eratosthenesSieve(N+1)      #得出小於N的所有素數
    if N in set:                    #素性判斷
        return 1                    #N為素數
    return 0                        #N為合數

def eratosthenesSieve(N):
    set = [1]*(N+1)                 #用於存儲N個正整數的表格／狀態；其中，0表示篩去，1表示保留
    for index in range(2,int(math.sqrt(N))):  #篩法（平凡除法）
        if set[index] == 1:
            ctr = 2
            while index * ctr <= N:
                set[index*ctr] = 0      #將index的倍數篩去
                ctr += 1

    rst = []
    for ptr in range(2,N):          #獲取結果
        if set[ptr] == 1:
            rst.append(ptr)
            ptr += 1

    return rst

#多項式歐幾里德除法 | 求解多項式的廣義歐幾里德除法
def polynomialEuclideanDivision(dvdExp, dvdCoe, dvsExp, dvsCoe):
    #將被除式係數與次冪添入被除式字典
    ecDictDivident = {}
    for ptr in range(len(dvdExp)):
        ecDictDivident[dvdExp[ptr]] = dvdCoe[ptr]

    #將除式係數與次冪添入除式字典
    ecDictDivisor = {}
    for ptr in range(len(dvsExp)):
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
        print 'The coefficient of the univariate with greatest degree in divisor must be 1.'
        raise KeyError

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
    '''
    cgcExp = [14, 13, 11,  9,  6,  3,  2,  1]
    cgcCoe = [ 3,  4,  2,  1,  1,  1, 12,  1]
    '''
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
    (rtoExp, rtoCoe) = congruenceSimplification(cgcExp, cgcCoe, modulo)

    print 'The original polynomial congruence is'
    for ptr in range(len(cgcExp)):
        print '%dx^%d' %(cgcCoe[ptr], cgcExp[ptr]),
        if ptr < len(cgcExp) - 1:
            print '+',
    print '≡ 0 (mod %d)' %modulo
    print
    print 'The simplified polynomial congruence is'
    for ptr in range(len(rtoExp)):
        print '%dx^%d' %(rtoCoe[ptr], rtoExp[ptr]),
        if ptr < len(rtoExp) - 1:
            print '+',
    print '≡ 0 (mod %d)\n' %modulo
