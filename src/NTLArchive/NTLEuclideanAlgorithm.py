# -*- coding: utf-8 -*-


# 廣義歐幾里德除法
# 用輾轉相除法求出商數列


from .NTLExceptions  import DefinitionError
from .NTLPolynomial  import Polynomial
from .NTLValidations import int_check


__all__  = ['euclideanAlgorithm', 'EEALoop']
nickname =  'eealist'


'''Usage sample:

print(eealist(3424, 13))

'''


def euclideanAlgorithm(dividend, divisor):
    if isinstance(dividend, Polynomial) or isinstance(divisor, Polynomial):
        dividend = Polynomial(dividend);    divisor = Polynomial(divisor)
    else:
        int_check(dividend, divisor)

        if divisor == 0:
            raise DefinitionError('The divisor should never be zero.')

    return EEALoop(dividend, divisor, [])


def EEALoop(a, b, qSet):
    q, r = divmod(a, b)

    if r == 0:  # (r,0) = r
        return qSet
    else:       # (a,b) = (r_-2,r_-1) = (r_-1,r_0) = … = (r_n,r_n+1) = (r_n,0) = r_n
        qSet.append(q)
        return EEALoop(b, r, qSet)
