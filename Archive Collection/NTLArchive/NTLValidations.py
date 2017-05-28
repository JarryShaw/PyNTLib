# -*- coding: utf-8 -*-

#自定義模式化參數檢查
#用於在NTL中進行模式化的參數檢查

'''
TODO:

* Define decorators to do argument validation in library header i.e. jsntlib.py
* Connect this file with NTLExceptions
'''

import NTLExceptions

def int_check(*args, **kwargs):
    func = ''
    for kw in kwargs:
        func = kwargs[kw] if kw == 'func' else ''

    for var in args:
        if not isinstance(var, int):
            raise NTLExceptions.IntError('Function %s expected integers, %s got instead.' %(func,  (var)))

def list_check(*args, **kwargs):
    func = ''
    for kw in kwargs:
        func = kwargs[kw] if kw == 'func' else ''

    for var in args:
        if not isinstance(var, list):
            raise NTLExceptions.IntError('Function %s expected integers, %s got instead.' %(func, (var)))
