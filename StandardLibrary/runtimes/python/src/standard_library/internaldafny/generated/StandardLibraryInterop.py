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

# Module: StandardLibraryInterop


class WrappersInterop:
    def  __init__(self):
        pass

    def __dafnystr__(self) -> str:
        return "StandardLibraryInterop.WrappersInterop"
    @staticmethod
    def CreateStringSome(s):
        return Wrappers.Option_Some(s)

    @staticmethod
    def CreateStringNone():
        return Wrappers.Option_None()

    @staticmethod
    def CreateBooleanSome(b):
        return Wrappers.Option_Some(b)

    @staticmethod
    def CreateBooleanNone():
        return Wrappers.Option_None()

