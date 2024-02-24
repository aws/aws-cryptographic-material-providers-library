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

# Module: DafnyLibraries


class MutableMapTrait:
    pass
    def Put(self, k, v):
        pass

    def Remove(self, k):
        pass


class MutableMap(MutableMapTrait):
    def  __init__(self):
        pass

    def __dafnystr__(self) -> str:
        return "DafnyLibraries.MutableMap"
    def SelectOpt(self, k):
        if (self).HasKey(k):
            return Wrappers.Option_Some((self).Select(k))
        elif True:
            return Wrappers.Option_None()

