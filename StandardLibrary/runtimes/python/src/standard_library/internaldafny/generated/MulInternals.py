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
import Unicode
import Functions
import Utf8EncodingForm
import Utf16EncodingForm
import UnicodeStrings
import FileIO
import GeneralInternals
import MulInternalsNonlinear

# Module: MulInternals

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def MulPos(x, y):
        d_182___accumulator_ = 0
        while True:
            with _dafny.label():
                if (x) == (0):
                    return (0) + (d_182___accumulator_)
                elif True:
                    d_182___accumulator_ = (d_182___accumulator_) + (y)
                    in24_ = (x) - (1)
                    in25_ = y
                    x = in24_
                    y = in25_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def MulRecursive(x, y):
        if (x) >= (0):
            return default__.MulPos(x, y)
        elif True:
            return (-1) * (default__.MulPos((-1) * (x), y))

