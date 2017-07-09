# -*- coding: utf-8 -*-


# 簡化剩餘係
# 求整數m的簡化剩餘係


from .NTLCoprimalityTest import coprimalityTest
from .NTLUtilities       import jsrange
from .NTLValidations     import int_check, pos_check


__all__  = ['primitiveResidueClass']
nickname =  'prc'


'''Usage sample:

prc = prc(40)

print('The primitive residue class of 40 is')
for num in prc:
    print(num, end=' ')
print()

'''


def primitiveResidueClass(n):
    int_check(n);   pos_check(n)

    # 當(d,n)=1時，d遍歷n的簡化剩餘係
    rst = []
    for d in jsrange(1, n):
        if coprimalityTest(d, n) == 1:
            rst.append(d)

    return rst
