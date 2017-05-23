# -*- coding: utf-8 -*-

#自定義異常類型
#用於在NTL中給予用戶提示

#數字參數異常
#The argument(s) must be (a) number(s).
class DigitError:
    def __init__(self, message):
        print
        raise TypeError(message)

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

#元組參數異常
#The argument(s) must be tuple type.
class TupleError:
    def __init__(self, message):
        print
        raise TypeError(message)

#多項式參數異常
#The argument(s) must be Polynomial type.
class PolyError:
    def __init__(self, message):
        print
        raise TypeError(message)

#參數異常
#Function expected at most / least n arguments, got m.
class ArgumentError:
    def __init__(self, message):
        print
        raise TypeError(message)

#複數功能異常
#The function is not defined for complex instance.
class ComplexError:
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

#布爾參數異常
#The argument(s) must be bool type.
class BoolError:
    def __init__(self, message):
        print 
        raise ValueError(message)

#字符串參數異常
#The argument(s) must be (a) string(s).
class StringError:
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

#關鍵詞參數異常
#Unknow attribute(s).
class KeywordError:
    def __init__(self, message):
        print
        raise AttributeError(message)
