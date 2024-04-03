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
import MulInternals
import Mul
import ModInternalsNonlinear
import DivInternalsNonlinear
import ModInternals
import DivInternals
import DivMod
import Power

# Module: Logarithm

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Log(base, pow):
        d_185___accumulator_ = 0
        while True:
            with _dafny.label():
                if (pow) < (base):
                    return (0) + (d_185___accumulator_)
                elif True:
                    d_185___accumulator_ = (d_185___accumulator_) + (1)
                    in36_ = base
                    in37_ = _dafny.euclidian_division(pow, base)
                    base = in36_
                    pow = in37_
                    raise _dafny.TailCall()
                break

