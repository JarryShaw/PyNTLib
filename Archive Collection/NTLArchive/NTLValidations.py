# -*- coding: utf-8 -*-

__all__ = [ 'int_check',
            'list_check',
            'pos_check']

import inspect
import sys

#自定義模式化參數檢查
#用於在NTL中進行模式化的參數檢查

'''
TODO:

* Define decorators to do argument validation in library header i.e. jsntlib.py
* Connect this file with NTLExceptions
'''

from .NTLExceptions import IntError, ListError, PNError

def int_check(*args):
    func = inspect.stack()[2][3]
    
    if sys.version_info[0] > 2:
        for var in args:
            if not isinstance(var, int):
                raise IntError('Function %s expected int, %s got instead.' %(func,  type(var).__name__))
    else:
        for var in args:
            if not isinstance(var, int) and not isinstance(var, long):
                raise IntError('Function %s expected int or long, %s got instead.' %(func,  type(var).__name__))

def list_check(*args):
    func = inspect.stack()[2][3]

    for var in args:
        if not isinstance(var, list):
            raise ListError('Function %s expected int, %s got instead.' %(func,  type(var).__name__))

def pos_check(*args):
    func = inspect.stack()[2][3]

    for var in args:
        if var <= 0:
            PNError('Function %s expected positives, negatives got instead.' %func)