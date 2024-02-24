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
import DafnyLibraries
import FileIO
import GeneralInternals
import MulInternalsNonlinear
import MulInternals
import Mul
import ModInternalsNonlinear
import DivInternalsNonlinear
import ModInternals
import DivInternals
import DivMod

# Module: Power

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Pow(b, e):
        d_171___accumulator_ = 1
        while True:
            with _dafny.label():
                if (e) == (0):
                    return (1) * (d_171___accumulator_)
                elif True:
                    d_171___accumulator_ = (d_171___accumulator_) * (b)
                    in34_ = b
                    in35_ = (e) - (1)
                    b = in34_
                    e = in35_
                    raise _dafny.TailCall()
                break

