# -*- coding: utf-8 -*-

#歐幾里得除法
#判斷是否整除，即b|a

def euclideanDivision(a=1, b=1):
    if not isinstance(a, int) or not isinstance(b, int):
        raise __import__('NTLExceptions').IntError

    if (b > a):                 #若b > a，則交換其次序
        a, b = b, a

    return not (a % b) or 0     #求餘數，判斷整除，1為整除，0為不整除

if __name__ == '__main__':
    if euclideanDivision():
        print 'The result is b|a.\n'
    else:
        print 'The result is b∤a.\n'