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
import Logarithm
import StandardLibraryInterop
import StandardLibrary_UInt
import StandardLibrary_String
import StandardLibrary

# Module: UUID

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def CreateBytesSuccess(bytes):
        return Wrappers.Result_Success(bytes)

    @staticmethod
    def CreateBytesFailure(error):
        return Wrappers.Result_Failure(error)

    @staticmethod
    def CreateStringSuccess(s):
        return Wrappers.Result_Success(s)

    @staticmethod
    def CreateStringFailure(error):
        return Wrappers.Result_Failure(error)

