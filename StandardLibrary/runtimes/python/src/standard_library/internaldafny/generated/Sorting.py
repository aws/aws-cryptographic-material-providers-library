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
import UUID
import UTF8
import Time
import Streams

# Module: Sorting

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def LexicographicByteSeqBelow(x, y):
        return default__.LexicographicByteSeqBelowAux(x, y, 0)

    @staticmethod
    def LexicographicByteSeqBelowAux(x, y, n):
        return (((n) == (len(x))) or (((n) != (len(y))) and (((x)[n]) < ((y)[n])))) or ((((n) != (len(y))) and (((x)[n]) == ((y)[n]))) and (default__.LexicographicByteSeqBelowAux(x, y, (n) + (1))))

    @staticmethod
    def SelectionSort(a, below):
        d_264_m_: int
        d_264_m_ = 0
        while (d_264_m_) < ((a).length(0)):
            d_265_mindex_: int
            d_266_n_: int
            rhs0_ = d_264_m_
            rhs1_ = (d_264_m_) + (1)
            d_265_mindex_ = rhs0_
            d_266_n_ = rhs1_
            while (d_266_n_) < ((a).length(0)):
                if not(below((a)[d_265_mindex_], (a)[d_266_n_])):
                    d_265_mindex_ = d_266_n_
                d_266_n_ = (d_266_n_) + (1)
            rhs2_ = (a)[d_265_mindex_]
            rhs3_ = (a)[d_264_m_]
            lhs0_ = a
            lhs1_ = d_264_m_
            lhs2_ = a
            lhs3_ = d_265_mindex_
            lhs0_[lhs1_] = rhs2_
            lhs2_[lhs3_] = rhs3_
            d_264_m_ = (d_264_m_) + (1)

