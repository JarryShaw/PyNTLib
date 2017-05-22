# -*- coding: utf-8 -*-

#多項式歐幾里德除法
#求解多項式的廣義歐幾里德除法

import NTLExceptions
import NTLGreatestCommonDivisor

def polyED(dvdExp, dvdCoe, dvsExp, dvsCoe):
    if not isinstance(dvdExp, list) or not isinstance(dvdCoe, list)\
    or not isinstance(dvsExp, list) or not isinstance(dvsCoe, list):
        raise NTLExceptions.ListError('The argument(s) must be list type.')

    #將被除式係數與次冪添入被除式字典
    ecDictDividend = {}
    for ptr in range(len(dvdExp)):
        ecDictDividend[dvdExp[ptr]] = dvdCoe[ptr]

    #將除式係數與次冪添入除式字典
    ecDictDivisor = {}
    for ptr in range(len(dvsExp)):
        ecDictDivisor[dvsExp[ptr]] = dvsCoe[ptr]

    #計算商式與餘式的字典結果
    ecDictQuotient = {}
    ecDictRatio = {}
    ecDictQuotient, ecDictRatio = polyEDLoop(ecDictDividend, ecDictDivisor, ecDictQuotient, ecDictRatio)

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
def polyEDLoop(ecDictDividend, ecDictDivisor, ecDictQuotient, ecDictRatio):
    #當除式為一常數時，直接判斷係數是否能被整除
    if ecDictDivisor.keys() == [0]:
        num = ecDictDivisor[0]
        ecDDvdCopy = __import__('copy').deepcopy(ecDictDividend)

        for key in ecDictDividend.keys():
            if ecDictDividend[key] % num != 0:
                return {}, ecDictDividend
            else:
                ecDDvdCopy[key] = ecDictDividend[key] / num

        return ecDictDividend, {}
    
    ecDDvdExpMax = max(ecDictDividend.keys())               #獲取被除式的最高次數
    ecDDvsExp = sorted(ecDictDivisor.keys(), reverse=True)  #獲取除式的指數列（降序）

    #若除式最高次冪的係數不為1，則中止程式
    if ecDictDivisor[ecDDvsExp[0]] != 1:
        raise NTLExceptions.ExponentError('The coefficient of the univariate with greatest degree in divisor must be 1.')

        '''
        ecDDvdCoe = ecDictDividend.values()
        ecDDvsCoe = ecDictDivisor.values()

        dvdGCD = ecDDvdCoe[0]
        for dvdCoe in ecDDvdCoe:
            dvdGCD = NTLGreatestCommonDivisor.greatestCommonDivisor(dvdCoe, dvdGCD)

        dvsGCD = ecDDvsCoe[0]
        for dvsCoe in ecDDvsCoe:
            dvsGCD = NTLGreatestCommonDivisor.greatestCommonDivisor(dvsCoe, dvsGCD)

        GCD = NTLGreatestCommonDivisor.greatestCommonDivisor(dvdGCD, dvsGCD)
        if GCD == 1 or ecDictDivisor[ecDDvsExp[0]] != GCD:
            return {}, ecDictDividend
        '''
        '''
        coe = ecDictDivisor[ecDDvsExp[0]]
        ecDDvdCopy = __import__('copy').deepcopy(ecDictDividend)

        #判斷除式是否可化簡
        for exp in ecDDvsExp:
            if ecDictDivisor[exp] % coe != 0:
                return {}, ecDictDividend
            else:
                ecDictDivisor[exp] /= coe

        #判斷被除式是否可化簡
        for key in ecDictDividend.keys():
            if ecDictDividend[key] % coe != 0:
                return {}, ecDictDividend
            else:
                ecDDvdCopy[key] = ecDictDividend[key] / coe

        ecDictDividend = __import__('copy').deepcopy(ecDDvdCopy)

        '''

    #若被除式最高次冪小於除式最高次冪則終止迭代
    while ecDDvdExpMax >= ecDDvsExp[0]:
        ecDQttCoe = ecDictDividend[ecDDvdExpMax]    #計算商式的係數，即當前被除式最高次冪項的係數
        ecDQttExp = ecDDvdExpMax - ecDDvsExp[0]     #計算商式的次冪，即當前被除式最高次冪與除式最高次冪的差值
        ecDictQuotient[ecDQttExp] = ecDQttCoe       #將結果添入商式字典
        
        #更新被除式係數及次冪狀態
        for exp in ecDDvsExp:
            if ecDictDividend.has_key(exp+ecDQttExp):
                ecDictDividend[exp+ecDQttExp] -= ecDictDivisor[exp] * ecDQttCoe
                if ecDictDividend[exp+ecDQttExp] == 0:
                    ecDictDividend.pop(exp+ecDQttExp)
            else:
                ecDictDividend[exp+ecDQttExp] = -1 * ecDictDivisor[exp] * ecDQttCoe
                
        #更新被除式的最高次數
        try:
            ecDDvdExpMax = max(ecDictDividend.keys())
        except ValueError:
            return ecDictQuotient, {}

    ecDictRatio = ecDictDividend.copy()             #此時，餘式即為被除式所剩餘項
    return ecDictQuotient, ecDictRatio

if __name__ == '__main__':
    #'''
    dvdExp = [20140515, 201405, 2014, 8, 6, 3, 1, 0]
    dvdCoe = [20140515, 201495, 2014, 8, 1, 4, 1, 1]
    # (1,-2), (3,4), (2,3), (34,1)
    # dvdExp = [1, 3, 2, 34]
    # dvdCoe = [-2, 4, 3, 1]
    dvsExp = [7,  1]
    dvsCoe = [1, -1]
    #'''
    (qttExp, qttCoe, rtoExp, rtoCoe) = polyED(dvdExp, dvdCoe, dvsExp, dvsCoe)

    print '\n\t'
    for ptr in range(len(dvdExp)):
        print '%dx^%d' %(dvdCoe[ptr], dvdExp[ptr]),
        if ptr < len(dvdExp) - 1:
            print '+',
    print '=\n(',
    for ptr in range(len(dvsExp)):
        print '%dx^%d' %(dvsCoe[ptr], dvsExp[ptr]),
        if ptr < len(dvsExp) - 1:
            print '+',
    print ') * (',
    for ptr in range(len(qttExp)):
        print '%dx^%d' %(qttCoe[ptr], qttExp[ptr]),
        if ptr < len(qttExp) - 1:
            print '+',
    print ') +',
    for ptr in range(len(rtoExp)):
        print '%dx^%d' %(rtoCoe[ptr], rtoExp[ptr]),
        if ptr < len(rtoExp) - 1:
            print '+',
    print
