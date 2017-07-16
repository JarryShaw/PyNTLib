# -*- coding: utf-8 -*-


# 歐幾里得除法
# 判斷是否整除，即b|a


from .NTLValidations import int_check


__all__  = ['euclideanDivision']
nickname =  'isdivisible'


'''Usage sample:

if isdivisible(13, 24):
    print('The result is b|a.\n')
else:
    print('The result is b∤a.\n')

'''


def euclideanDivision(a, b):
    int_check(a, b)

    if b > a:   a, b = b, a         # 若b > a，則交換其次序

    return bool(not (a % b) or 0)   # 求餘數，判斷整除，1為整除，0為不整除
