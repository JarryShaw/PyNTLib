#-*- coding: utf-8 -*-

__all__ = ['jsrange', 'jsfloor', 'jssquare', 'jssign']

import sys

#自定義常用工具
#用於NTL的代碼簡化和適配

#Python 2.7 -- xrange | Python 3.6 -- range
jsrange = range if sys.version_info[0] > 2 else xrange

#Python 2.7 -- int(floor) | Python 3.6 -- floor
def jsfloor(*args):
    from math import floor
    return floor(*args) if sys.version_info[0] > 2 else int(floor(*args))

#Python 2.7 -- int(ceil) | Python 3.6 -- ceil
def jsceil(*args):
    from math import ceil
    return ceil(*args) if sys.version_info[0] > 2 else int(ceil(*args))

#Python 2.7 -- int(round) | Python 3.6 -- round
def jsround(*args):
    return round(*args) if sys.version_info[0] > 2 else int(round(*args))

#判斷整數是否為平方數
def jssquare(*args):
    from math import sqrt

    for var in args:
        if int(sqrt(var))**2 != var:    return False
    return True

#獲取整數的符號
def jssign(num):
    return 1 if num >= 0 else -1
