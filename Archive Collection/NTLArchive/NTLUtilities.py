#-*- coding: utf-8 -*-

__all__ =  ['jsrange', 'jsstring',
            'jsfloor', 'jsceil', 'jsround'
            'jslist', 'jssquare', 'jssign',
            'jsappend', 'jsupdate']

import sys

#自定義常用工具
#用於NTL的代碼簡化和適配

#Python 2.7 -- xrange | Python 3.6 -- range
jsrange = range if sys.version_info[0] > 2 else xrange

jsstring = str if sys.version_info[0] > 2 else basestring

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

#合併列表（去重）
def jsappend(rst, dst):
    if dst is list:
        return list(set(rst + dst))
    else:
        return list(set(rst + [dst]))

#合併字典（增補）
def jsupdate(rst, dst):
    for key in list(dst):
        if key in rst:
            if rst[key] is dict:
                jsupdate(rst[key], dst[key])
            else:
                rst[key] += dst[key]
        else:
            rst[key] = dst[key]
    return rst
