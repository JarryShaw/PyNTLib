# -*- coding: utf-8 -*-


import math
import sys


# 自定義常用工具
# 用於NTL的代碼簡化和適配


__all__ =  [
    'jsrange', 'jsstring', 'jsint', 'jsmaxint', 'jsbytes', 'jsstr'
    'jsfloor', 'jsceil', 'jsround',
    'jskeys', 'jsvalues', 'jsitems',
    'jssquare', 'jssign', 'jsappend', 'jsupdate'
]


ispy3 = sys.version_info[0] > 2


##############################################################################
# Overwritten session.
##############################################################################


# Python 2.7 -- xrange | Python 3.6 -- range
jsrange = range if ispy3 else xrange


# Python 2.7 -- basestring | Python 3.6 -- str
jsstring = str if ispy3 else basestring


# Python 2.7 -- (int, long) | Python 3.6 -- int
jsint = int if ispy3 else (int, long)


# Python 2.7 -- sys.maxint | Python 3.6 -- sys.maxsize
jsmaxint = sys.maxsize if ispy3 else sys.maxint


# Python 2.7 -- unicode | Python 3.6 -- str
jsstr = str if ispy3 else unicode


# Python 2.7 -- str | Python 3.6 -- bytes
jsbytes = bytes if ispy3 else str


##############################################################################
# Compability session.
##############################################################################


# Python 2.7 -- int(floor(num)) | Python 3.6 -- floor(num)
jsfloor = math.floor if ispy3 else lambda x: int(math.floor(x))


# Python 2.7 -- int(ceil(num)) | Python 3.6 -- ceil(num)
jsceil = math.ceil if ispy3 else lambda x: int(math.ceil(x))


# Python 2.7 -- int(round(num)) | Python 3.6 -- round(num)
jsround = round if ispy3 else lambda x: int(round(x))


# Python 2.7 -- dict.keys() | Python 3.6 -- list(dict.keys())
jskeys = lambda x: list(x.keys()) if ispy3 else x.keys()


# Python 2.7 -- dict.values() | Python 3.6 -- list(dict.values())
jsvalues = lambda x: list(x.values()) if ispy3 else x.values()


# Python 2.7 -- dict.items() | Python 3.6 -- list(dict.items())
jsitems = lambda x: list(x.items()) if ispy3 else x.items()


##############################################################################
# Utility session.
##############################################################################


# 判斷整數是否為平方數
def jssquare(*args):
    from math import sqrt

    for var in args:
        if int(sqrt(var))**2 != var:    return False
    return True


# 獲取整數的符號
def jssign(num):
    return 1 if num >= 0 else -1


# 合併列表（去重）
def jsappend(rst, dst):
    if isinstance(dst, list):
        return list(set(rst + dst))
    else:
        return list(set(rst + [dst]))


# 合併字典（增補）
def jsupdate(rst, dst):
    for key in dst:
        if key in rst:
            if isinstance(dst[key], dict):
                jsupdate(rst[key], dst[key])
            else:
                rst[key] += dst[key]
        else:
            rst[key] = dst[key]
    return rst
