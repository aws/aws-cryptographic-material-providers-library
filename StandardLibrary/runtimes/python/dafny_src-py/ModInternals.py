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

# Module: ModInternals

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def ModRecursive(x, d):
        while True:
            with _dafny.label():
                if (x) < (0):
                    in26_ = (d) + (x)
                    in27_ = d
                    x = in26_
                    d = in27_
                    raise _dafny.TailCall()
                elif (x) < (d):
                    return x
                elif True:
                    in28_ = (x) - (d)
                    in29_ = d
                    x = in28_
                    d = in29_
                    raise _dafny.TailCall()
                break

