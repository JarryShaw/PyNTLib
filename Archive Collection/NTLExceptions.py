# -*- coding: utf-8 -*-

#自定義異常類型
#用於在NTL中給予用戶提示

#整數參數異常
class IntError:
    def __init__(self):
        print
        raise TypeError('The argument(s) must be integral.')

#列表參數異常
class ListError:
    def __init__(self):
        print
        raise TypeError('The argument(s) must be list type.')

#負值參數異常
class PNError:
    def __init__(self):
        print
        raise ValueError('The argument(s) must be positive.')

#素數參數異常
class PrimeError:
    def __init__(self):
        print
        raise ValueError('The argument must be prime.')

#合數參數異常
class CompositError:
    def __init__(self):
        print
        raise ValueError('The argument must be composit.')

#參數定義異常
class DefinitionError:
    def __init__(self):
        print
        raise ValueError('The argument must be a natural number greater than 1.')

#方程無解異常
class SolutionError:
    def __init__(self):
        print
        raise RuntimeError('The polynomial has no integral solution.')

#係數參數異常
class ExponentError:
    def __init__(self):
        print
        raise KeyError('The coefficient of the univariate with greatest degree in divisor must be 1.')
