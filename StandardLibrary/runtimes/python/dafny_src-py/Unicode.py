import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_mMergeSort
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

class HighSurrogateCodePoint:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return default__.HIGH__SURROGATE__MIN

class LowSurrogateCodePoint:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return default__.LOW__SURROGATE__MIN

class ScalarValue:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)

class AssignedCodePoint:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
