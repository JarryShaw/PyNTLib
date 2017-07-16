# -*- coding: utf-8 -*-


# 中國剩餘定理
# 求基本同餘式組的通解


from .NTLBezoutEquation       import bezoutEquation
from .NTLExceptions           import DefinitionError
from .NTLUtilities            import jsrange
from .NTLValidations          import int_check, list_check, tuple_check


__all__  = ['CHNRemainderTheorem', 'solve', 'iterCalc', 'updateState']
nickname =  'crt'


'''Usage sample:

remainder = crt((3, [1,-1]), (5, [1,-1]), (7, [2,-2]))

print('x ≡ ±1 (mod 3)')
print('x ≡ ±1 (mod 5)')
print('x ≡ ±2 (mod 7)')
print('The solutions of the above equation set is\n\tx ≡', end=' ')
for rst in remainder:
    print(rst, end=' ')
print('(mod 105)')

'''


def CHNRemainderTheorem(*args):
    rmd = []
    mod = []

    for tpl in args:
        tuple_check(tpl)

        if len(tpl) != 2:
            raise DefinitionError(
                'The arguments must be tuples of modulos and corresponding solutions (in a list).')

        int_check(tpl[0]);  list_check(tpl[1])
        for num in tpl[1]:  int_check(num)

        mod.append(tpl[0]); rmd.append(tpl[1])

    modulo = 1
    for tmpMod1 in mod:
        modulo *= tmpMod1                       # M(original modulo) = ∏m_i

    bList = []
    for tmpMod in mod:
        M = modulo // tmpMod                    # M_i = M / m_i
        t = bezoutEquation(M, tmpMod)[0]        # t_i * M_i ≡ 1 (mod m_i)
        bList.append(t * M)                     # b_i = t_i * M_i

    remainder = iterCalc(rmd, bList, modulo)    # x_j = Σ(b_i * r_i) (mod M)
    return sorted(remainder)


# 對rmd多維數組（層，號）中的數進行全排列並計算結果
def iterCalc(ognList, coeList, modulo):
    ptrList = []                            # 寄存指向每一數組層的號
    lvlList = []                            # 寄存每一數組層的最大號
    for tmpList in ognList:
        ptrList.append(len(tmpList)-1)
        lvlList.append(len(tmpList)-1)

    flag = 1
    rstList = []

    while flag:
        ptrNum = 0
        rstNum = 0
        for ptr in ptrList:
            rstNum += ognList[ptrNum][ptr] * coeList[ptrNum]    # 計算結果
            ptrNum += 1

        rstList.append(rstNum % modulo)
        (ptrList, flag) = updateState(ptrList, lvlList)         # 更新ptrList的寄存值，並返回是否結束循環

    return rstList


# 更新ptrList的寄存值，並返回是否已遍歷所有組合
def updateState(ptrList, lvlList):
    ptr = 0
    flag = 1
    glbFlag = 1

    while flag:                                 # 未更新寄存數值前，保持循環（類似同步計數器）
        if ptrList[ptr] > 0:                    # 該層未遍歷，更新該層，終止循環
            ptrList[ptr] -= 1
            flag = 0
        else:                                   # 該層已遍歷
            if ptr < len(lvlList) - 1:          # 更新指針至下一層並接著循環
                ptrList[ptr] = lvlList[ptr]
                ptr += 1
            else:                               # 所有情況均已遍歷，終止循環
                flag = 0
                glbFlag = 0

    return ptrList, glbFlag
