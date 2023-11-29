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

# Module: Math

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Min(a, b):
        if (a) < (b):
            return a
        elif True:
            return b

    @staticmethod
    def Max(a, b):
        if (a) < (b):
            return b
        elif True:
            return a

    @staticmethod
    def Abs(a):
        if (a) >= (0):
            return a
        elif True:
            return (0) - (a)

