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
import standard_library.internaldafny.generated.MulInternals as MulInternals
import standard_library.internaldafny.generated.Mul as Mul
import standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import standard_library.internaldafny.generated.ModInternals as ModInternals
import standard_library.internaldafny.generated.DivInternals as DivInternals
import standard_library.internaldafny.generated.DivMod as DivMod
import standard_library.internaldafny.generated.Power as Power
import standard_library.internaldafny.generated.Logarithm as Logarithm
import standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import standard_library.internaldafny.generated.UUID as UUID
import standard_library.internaldafny.generated.UTF8 as UTF8
import standard_library.internaldafny.generated.Time as Time
import standard_library.internaldafny.generated.Streams as Streams

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
        d_255_m_: int
        d_255_m_ = 0
        while (d_255_m_) < ((a).length(0)):
            d_256_mindex_: int
            d_257_n_: int
            rhs0_ = d_255_m_
            rhs1_ = (d_255_m_) + (1)
            d_256_mindex_ = rhs0_
            d_257_n_ = rhs1_
            while (d_257_n_) < ((a).length(0)):
                if not(below((a)[d_256_mindex_], (a)[d_257_n_])):
                    d_256_mindex_ = d_257_n_
                d_257_n_ = (d_257_n_) + (1)
            rhs2_ = (a)[d_256_mindex_]
            rhs3_ = (a)[d_255_m_]
            lhs0_ = a
            lhs1_ = d_255_m_
            lhs2_ = a
            lhs3_ = d_256_mindex_
            lhs0_[lhs1_] = rhs2_
            lhs2_[lhs3_] = rhs3_
            d_255_m_ = (d_255_m_) + (1)

