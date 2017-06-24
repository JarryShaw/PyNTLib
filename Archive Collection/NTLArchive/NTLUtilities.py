#-*- coding: utf-8 -*-

__all__ = ['jsrange', 'jsfloor']

import sys

#自定義常用工具
#用於NTL的代碼簡化和適配

#Python 2.7 -- xrange | Python 3.6 -- range
jsrange = range if sys.version_info[0] > 2 else xrange

#Python 2.7 -- floor | Python 3.6 -- int(floor)
def jsfloor(*args):
    from math import floor
    return floor(*args) if sys.version_info[0] > 2 else int(floor(*args))
