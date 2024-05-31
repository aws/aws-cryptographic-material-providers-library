import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import standard_library.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import standard_library.internaldafny.generated.Wrappers as Wrappers
import standard_library.internaldafny.generated.Relations as Relations
import standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import standard_library.internaldafny.generated.Math as Math
import standard_library.internaldafny.generated.Seq as Seq
import standard_library.internaldafny.generated.BoundedInts as BoundedInts
import standard_library.internaldafny.generated.Unicode as Unicode
import standard_library.internaldafny.generated.Functions as Functions
import standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import standard_library.internaldafny.generated.FileIO as FileIO
import standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear

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

