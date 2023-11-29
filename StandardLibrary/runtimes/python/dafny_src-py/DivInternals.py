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
import Unicode
import Functions
import Utf8EncodingForm
import Utf16EncodingForm
import UnicodeStrings
import FileIO
import GeneralInternals
import MulInternalsNonlinear
import MulInternals
import Mul
import ModInternalsNonlinear
import DivInternalsNonlinear
import ModInternals

# Module: DivInternals

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DivPos(x, d):
        d_170___accumulator_ = 0
        while True:
            with _dafny.label():
                if (x) < (0):
                    d_170___accumulator_ = (d_170___accumulator_) + (-1)
                    in30_ = (x) + (d)
                    in31_ = d
                    x = in30_
                    d = in31_
                    raise _dafny.TailCall()
                elif (x) < (d):
                    return (0) + (d_170___accumulator_)
                elif True:
                    d_170___accumulator_ = (d_170___accumulator_) + (1)
                    in32_ = (x) - (d)
                    in33_ = d
                    x = in32_
                    d = in33_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def DivRecursive(x, d):
        if (d) > (0):
            return default__.DivPos(x, d)
        elif True:
            return (-1) * (default__.DivPos(x, (-1) * (d)))

