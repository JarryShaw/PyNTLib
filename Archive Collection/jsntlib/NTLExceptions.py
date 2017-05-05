# -*- coding: utf-8 -*-

#自定義異常類型
#用於在NTL中給予用戶提示

#整數參數異常
#The argument(s) must be integral.
class IntError:
    def __init__(self, message):
        print
        raise TypeError(message)

#列表參數異常
#The argument(s) must be list type.
class ListError:
    def __init__(self, message):
        print
        raise TypeError(message)

#正／負值參數異常
#The argument(s) must be positive/negative.
class PNError:
    def __init__(self, message):
        print
        raise ValueError(message)

#素／合數參數異常
#The argument(s) must be prime/composit.
class PCError:
    def __init__(self, message):
        print
        raise ValueError(message)

#參數定義異常
#The argument must match a specific patern.
class DefinitionError:
    def __init__(self, message):
        print
        raise ValueError(message)

#方程無解異常
#The polynomial has no integral solution.
class SolutionError:
    def __init__(self, message):
        print
        raise RuntimeError(message)

#係數參數異常
#The coefficient of the univariate with greatest degree in divisor must be 1.
class ExponentError:
    def __init__(self, message):
        print
        raise KeyError(message)
