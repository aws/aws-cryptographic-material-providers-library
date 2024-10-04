import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import smithy_dafny_standard_library.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import smithy_dafny_standard_library.internaldafny.generated.Relations as Relations
import smithy_dafny_standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import smithy_dafny_standard_library.internaldafny.generated.Math as Math
import smithy_dafny_standard_library.internaldafny.generated.Seq as Seq
import smithy_dafny_standard_library.internaldafny.generated.BoundedInts as BoundedInts
import smithy_dafny_standard_library.internaldafny.generated.Unicode as Unicode
import smithy_dafny_standard_library.internaldafny.generated.Functions as Functions
import smithy_dafny_standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import smithy_dafny_standard_library.internaldafny.generated.FileIO as FileIO
import smithy_dafny_standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import smithy_dafny_standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.MulInternals as MulInternals
import smithy_dafny_standard_library.internaldafny.generated.Mul as Mul
import smithy_dafny_standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.ModInternals as ModInternals
import smithy_dafny_standard_library.internaldafny.generated.DivInternals as DivInternals
import smithy_dafny_standard_library.internaldafny.generated.DivMod as DivMod
import smithy_dafny_standard_library.internaldafny.generated.Power as Power
import smithy_dafny_standard_library.internaldafny.generated.Logarithm as Logarithm
import smithy_dafny_standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import smithy_dafny_standard_library.internaldafny.generated.UUID as UUID
import smithy_dafny_standard_library.internaldafny.generated.UTF8 as UTF8
import smithy_dafny_standard_library.internaldafny.generated.Time as Time
import smithy_dafny_standard_library.internaldafny.generated.Streams as Streams

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
        d_0_m_: int
        d_0_m_ = 0
        while (d_0_m_) < ((a).length(0)):
            d_1_mindex_: int
            d_2_n_: int
            rhs0_ = d_0_m_
            rhs1_ = (d_0_m_) + (1)
            d_1_mindex_ = rhs0_
            d_2_n_ = rhs1_
            while (d_2_n_) < ((a).length(0)):
                if not(below((a)[d_1_mindex_], (a)[d_2_n_])):
                    d_1_mindex_ = d_2_n_
                d_2_n_ = (d_2_n_) + (1)
            rhs2_ = (a)[d_1_mindex_]
            rhs3_ = (a)[d_0_m_]
            lhs0_ = a
            lhs1_ = d_0_m_
            lhs2_ = a
            lhs3_ = d_1_mindex_
            lhs0_[lhs1_] = rhs2_
            lhs2_[lhs3_] = rhs3_
            d_0_m_ = (d_0_m_) + (1)

