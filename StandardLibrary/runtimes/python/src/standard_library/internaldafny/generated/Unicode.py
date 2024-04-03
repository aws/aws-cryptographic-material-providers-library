import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_MergeSort
import Math
import Seq
import BoundedInts

# Module: Unicode

class default__:
    def  __init__(self):
        pass

    @_dafny.classproperty
    def HIGH__SURROGATE__MIN(instance):
        return 55296
    @_dafny.classproperty
    def HIGH__SURROGATE__MAX(instance):
        return 56319
    @_dafny.classproperty
    def LOW__SURROGATE__MIN(instance):
        return 56320
    @_dafny.classproperty
    def LOW__SURROGATE__MAX(instance):
        return 57343
    @_dafny.classproperty
    def ASSIGNED__PLANES(instance):
        return _dafny.Set({0, 1, 2, 3, 14, 15, 16})

class CodePoint:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_52_i_: int = source__
        return ((0) <= (d_52_i_)) and ((d_52_i_) <= (1114111))

class HighSurrogateCodePoint:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return default__.HIGH__SURROGATE__MIN
    def _Is(source__):
        d_53_p_: int = source__
        if CodePoint._Is(d_53_p_):
            return ((default__.HIGH__SURROGATE__MIN) <= (d_53_p_)) and ((d_53_p_) <= (default__.HIGH__SURROGATE__MAX))
        return False

class LowSurrogateCodePoint:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return default__.LOW__SURROGATE__MIN
    def _Is(source__):
        d_54_p_: int = source__
        if CodePoint._Is(d_54_p_):
            return ((default__.LOW__SURROGATE__MIN) <= (d_54_p_)) and ((d_54_p_) <= (default__.LOW__SURROGATE__MAX))
        return False

class ScalarValue:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_55_p_: int = source__
        if CodePoint._Is(d_55_p_):
            return (((d_55_p_) < (default__.HIGH__SURROGATE__MIN)) or ((d_55_p_) > (default__.HIGH__SURROGATE__MAX))) and (((d_55_p_) < (default__.LOW__SURROGATE__MIN)) or ((d_55_p_) > (default__.LOW__SURROGATE__MAX)))
        return False

class AssignedCodePoint:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
