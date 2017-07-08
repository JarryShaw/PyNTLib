# -*- coding: utf-8 -*-


import sys


# 自定義常用工具
# 用於NTL的代碼簡化和適配


__all__ =  [
    'jsrange', 'jsstring', 'jsint', 'jsmaxint',
    'jsfloor', 'jsceil', 'jsround',
    'jskeys', 'jsvalues', 'jsitems',
    'jssquare', 'jssign', 'jsappend', 'jsupdate'
]


##############################################################################
# Overwritten session.
##############################################################################


# Python 2.7 -- xrange | Python 3.6 -- range
jsrange = range if sys.version_info[0] > 2 else xrange


# Python 2.7 -- basestring | Python 3.6 -- str
jsstring = str if sys.version_info[0] > 2 else basestring


# Python 2.7 -- (int, long) | Python 3.6 -- int
jsint = int if sys.version_info[0] > 2 else (int, long)


# Python 2.7 -- sys.maxint | Python 3.6 -- sys.maxsize
jsmaxint = sys.maxsize if sys.version_info[0] > 2 else sys.maxint


##############################################################################
# Compability session.
##############################################################################


# Python 2.7 -- int(floor(num)) | Python 3.6 -- floor(num)
def jsfloor(*args):
    from math import floor
    return floor(*args) if sys.version_info[0] > 2 else int(floor(*args))


# Python 2.7 -- int(ceil(num)) | Python 3.6 -- ceil(num)
def jsceil(*args):
    from math import ceil
    return ceil(*args) if sys.version_info[0] > 2 else int(ceil(*args))


# Python 2.7 -- int(round(num)) | Python 3.6 -- round(num)
def jsround(*args):
    return round(*args) if sys.version_info[0] > 2 else int(round(*args))


# Python 2.7 -- dict.keys() | Python 3.6 -- list(dict.keys())
def jskeys(_dict):
    return list(_dict.keys()) if sys.version_info[0] > 2 else _dict.keys()


# Python 2.7 -- dict.values() | Python 3.6 -- list(dict.values())
def jsvalues(_dict):
    return list(_dict.values()) if sys.version_info[0] > 2 else _dict.values()


# Python 2.7 -- dict.items() | Python 3.6 -- list(dict.items())
def jsitems(_dict):
    return list(_dict.items()) if sys.version_info[0] > 2 else _dict.items()


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
