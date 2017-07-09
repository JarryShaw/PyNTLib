# -*- coding: utf-8 -*-


from .NTLExceptions  import DefinitionError
from .NTLValidations import int_check


# 廣義歐幾里德除法
# 用輾轉相除法求出商數列


__all__  = ['euclideanAlgorithm', 'EEALoop']
nickname =  'eealist'


'''Usage sample:

print(eealist(3424, 13))

'''


def euclideanAlgorithm(dividend, divisor):
    int_check(dividend, divisor)

    if divisor == 0:
        raise DefinitionError('The divisor should never be zero.')

    return EEALoop(dividend, divisor, [])


def EEALoop(a, b, qSet):
    q = a // b
    r = a %  b

    if r == 0:  # (r,0) = r
        return qSet
    else:       # (a,b) = (r_-2,r_-1) = (r_-1,r_0) = … = (r_n,r_n+1) = (r_n,0) = r_n
        qSet.append(q)
        return EEALoop(b, r, qSet)
