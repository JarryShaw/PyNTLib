# -*- coding: utf-8 -*-

#中國剩餘定理
#求基本同餘式組的通解

import NTLExceptions
import NTLPolynomialCongruence

def CHNRemainderTheorem(*args):
    rto = []
    mod = []

    for tpl in args:
        if not isinstance(tpl, tuple) or len(tpl) != 2:
            raise NTLExceptions.TupleError('The arguments must be tuples of modulos and corresponding solutions (in a list).')

        if not isinstance(tpl[0], int) and not isinstance(tpl[0], long):
            raise NTLExceptions.IntError('The modulo must be integral.')

        if not isinstance(tpl[1], list):
            raise NTLExceptions.TupleError('The solutions must contained in a list.')

        for num in tpl[1]:
            if not isinstance(num, int) and not isinstance(num, long):
                raise NTLExceptions.IntError('The solutions must be integral.')

        mod.append(tpl[0])
        rto.append(tpl[1])

    modulo = 1
    for tmpMod1 in mod:
        modulo *= tmpMod1                                               #M(original modulo) = ∏m_i

    bList = []
    for tmpMod2 in mod:
        M = modulo / tmpMod2                                            #M_i = M / m_i
        t = NTLPolynomialCongruence.prmMCS([1,0], [M,-1], tmpMod2)[0]   #t_i * M_i ≡ 1 (mod m_i)
        bList.append(t * M)                                             #b_i = t_i * M_i
    
    ratio = iterCalc(rto, bList, modulo)                                #x_j = Σ(b_i * r_i) (mod M)                          
    return sorted(ratio)

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
    ratio = CHNRemainderTheorem((3, [1,-1]), (5, [1,-1]), (7, [2,-2]))

    print
    print 'x ≡ ±1 (mod 3)'
    print 'x ≡ ±1 (mod 5)'
    print 'x ≡ ±2 (mod 7)'
    print 'The solutions of the above equation set is\n\tx ≡',
    for rst in ratio:
        print rst,
    print '(mod 105)'
