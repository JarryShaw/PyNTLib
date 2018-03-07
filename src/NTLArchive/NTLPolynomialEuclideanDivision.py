# -*- coding: utf-8 -*-


import copy


# 多項式歐幾里德除法
# 求解多項式的廣義歐幾里德除法


from .NTLUtilities   import jsrange
from .NTLValidations import int_check, list_check


__all__  = ['polyED', 'polyEDLoop']
nickname =  'polydiv'


'''Usage sample:

# 1st set:
dvdExp = [20140515, 201405, 2014, 8, 6, 3, 1, 0]
dvdCoe = [20140515, 201495, 2014, 8, 1, 4, 1, 1]

# 2nd set:
dvdExp = [1, 3, 2, 34]
dvdCoe = [-2, 4, 3, 1]

# 3rd set:
dvsExp = [7,  1]
dvsCoe = [1, -1]

(qttExp, qttCoe, rmdExp, rmdCoe) = polydiv(dvdExp, dvdCoe, dvsExp, dvsCoe)

for ptr in range(len(dvdExp)):
    print('%dx^%d' % (dvdCoe[ptr], dvdExp[ptr]), end=' ')
    if ptr < len(dvdExp) - 1:
        print('+', end=' ')
print('=\n(', end=' ')
for ptr in range(len(dvsExp)):
    print('%dx^%d' % (dvsCoe[ptr], dvsExp[ptr]), end=' ')
    if ptr < len(dvsExp) - 1:
        print('+', end=' ')
print(') * (', end=' ')
for ptr in range(len(qttExp)):
    print('%dx^%d' % (qttCoe[ptr], qttExp[ptr]), end=' ')
    if ptr < len(qttExp) - 1:
        print('+', end=' ')
print(') +', end=' ')
for ptr in range(len(rmdExp)):
    print('%dx^%d' % (rmdCoe[ptr], rmdExp[ptr]), end=' ')
    if ptr < len(rmdExp) - 1:
        print('+', end=' ')
print()

'''


def polyED(dvdExp, dvdCoe, dvsExp, dvsCoe):
    list_check(dvdExp, dvdCoe, dvsExp, dvsCoe)

    # 將被除式係數與次冪添入被除式字典
    ecDictDividend = {}
    for ptr in jsrange(len(dvdExp)):
        exp_ = dvdExp[ptr]
        coe_ = dvdCoe[ptr]
        int_check(exp_, coe_)
        ecDictDividend[exp_] = coe_

    # 將除式係數與次冪添入除式字典
    ecDictDivisor = {}
    for ptr in jsrange(len(dvsExp)):
        exp_ = dvsExp[ptr]
        coe_ = dvsCoe[ptr]
        int_check(exp_, coe_)
        ecDictDivisor[exp_] = coe_

    # 計算商式與餘式的字典結果
    ecDictQuotient = {}
    ecDictRemainder = {}
    ecDictQuotient, ecDictRemainder = polyEDLoop(
        ecDictDividend, ecDictDivisor, ecDictQuotient, ecDictRemainder)

    # 將商式字典轉為係數與次冪數組
    qttCoe = []
    qttExp = sorted(ecDictQuotient.keys(), reverse=True)
    for exp in qttExp:
        qttCoe.append(ecDictQuotient[exp])

    # 將餘式字典轉為係數與次冪數組
    rmdCoe = []
    rmdExp = sorted(ecDictRemainder.keys(), reverse=True)
    for rmd in rmdExp:
        rmdCoe.append(ecDictRemainder[rmd])

    return qttExp, qttCoe, rmdExp, rmdCoe


# 歐氏除法的循環求解
def polyEDLoop(ecDictDividend, ecDictDivisor, ecDictQuotient, ecDictRemainder):
    ecDDvdCopy = copy.deepcopy(ecDictDividend)

    ecDDvdExpMax = max(ecDictDividend.keys())               # 獲取被除式的最高次數
    ecDDvsExp = sorted(ecDictDivisor.keys(), reverse=True)  # 獲取除式的指數列（降序）

    # 若除式最高次冪的係數不為1，則需化簡
    if ecDictDivisor[ecDDvsExp[0]] != 1:

        '''Deprecated:

        raise ExponentError(
            'The coefficient of the univariate with greatest degree in divisor must be 1.')
        '''

        flag = True
        ecDDvsCoeMax = ecDictDivisor[ecDDvsExp[0]]

        if ecDictDividend[ecDDvdExpMax] % ecDDvsCoeMax == 0:
            mul_ = ecDictDividend[ecDDvdExpMax] // ecDDvsCoeMax
            for key in ecDictDivisor.keys():
                if ecDictDivisor[key] * mul_ != ecDictDividend[key]:    break
            else:
                ecDictQuotient = copy.deepcopy(ecDictDivisor)
                return ecDictQuotient, ecDictRemainder

        # 判斷除式是否可化簡
        for exp in ecDDvsExp:
            if ecDictDivisor[exp] % ecDDvsCoeMax != 0:
                ecDictRemainder = copy.deepcopy(ecDictDividend)
                return ecDictQuotient, ecDictRemainder
            else:
                ecDictDivisor[exp] //= ecDDvsCoeMax

        # 判斷被除式是否可化簡
        for key in ecDictDividend.keys():
            if ecDictDividend[key] % ecDDvsCoeMax != 0:
                ecDictRemainder = copy.deepcopy(ecDictDividend)
                return ecDictQuotient, ecDictRemainder
            else:
                ecDDvdCopy[key] //= ecDDvsCoeMax

    ecDictDividend = copy.deepcopy(ecDDvdCopy)

    # 若被除式最高次冪小於除式最高次冪則終止迭代
    while ecDDvdExpMax >= ecDDvsExp[0]:
        # 計算商式的係數，即當前被除式最高次冪項的係數
        ecDQttCoe = ecDictDividend[ecDDvdExpMax]
        # 計算商式的次冪，即當前被除式最高次冪與除式最高次冪的差值
        ecDQttExp = ecDDvdExpMax - ecDDvsExp[0]
        # 將結果添入商式字典
        ecDictQuotient[ecDQttExp] = ecDQttCoe

        # 更新被除式係數及次冪狀態
        for exp in ecDDvsExp:
            tmpexp = exp + ecDQttExp
            if (tmpexp) in ecDictDividend:
                ecDictDividend[tmpexp] -= ecDictDivisor[exp] * ecDQttCoe
                if ecDictDividend[tmpexp] == 0:
                    ecDictDividend.pop(tmpexp)
            else:
                ecDictDividend[tmpexp] = -1 * ecDictDivisor[exp] * ecDQttCoe

        # 更新被除式的最高次數
        try:
            ecDDvdExpMax = max(ecDictDividend.keys())
        except ValueError:
            ecDictRemainder = {}
            return ecDictQuotient, ecDictRemainder

    # 此時，餘式即為被除式所剩餘項
    ecDictRemainder = ecDictDividend.copy()
    return ecDictQuotient, ecDictRemainder
