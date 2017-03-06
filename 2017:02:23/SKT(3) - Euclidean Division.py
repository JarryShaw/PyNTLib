# -*- coding: utf-8 -*-

#歐幾里得除法
#判斷是否整除，即b|a

def euclideanDivision(a=1, b=1):
    q = a / b 		#求（不完全）商
    r = a % b 		#求餘數
    if r == 0:		#判斷整除
        print 'The result is b|a.'
    else:
    	print 'The result is b∤a.'


if __name__ == '__main__':
    while True:
        try:
            a = int(raw_input('DEVIDE a = '))
        except ValueError:
            continue
        break
    while True:
        try:
            b = int(raw_input('DIVISIOR b = '))
            if b == 0:
                print 'The divisor cannot be zero.'
                continue
        except ValueError:
            print 'Invalid input.'
            continue
        break

    euclideanDivision(a,b)
