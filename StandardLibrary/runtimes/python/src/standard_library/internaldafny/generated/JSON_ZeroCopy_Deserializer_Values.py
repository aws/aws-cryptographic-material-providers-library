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
import Sorting
import SortedSets
import HexStrings
import GetOpt
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
import JSON_Utils_Views_Core
import JSON_Utils_Views_Writers
import JSON_Utils_Views
import JSON_Utils_Lexers_Core
import JSON_Utils_Lexers_Strings
import JSON_Utils_Lexers
import JSON_Utils_Cursors
import JSON_Utils_Parsers
import JSON_Utils_Str_CharStrConversion
import JSON_Utils_Str_CharStrEscaping
import JSON_Utils_Str
import JSON_Utils_Seq
import JSON_Utils_Vectors
import JSON_Utils
import JSON_Errors
import JSON_Values
import JSON_Spec
import JSON_Grammar
import JSON_Serializer_ByteStrConversion
import JSON_Serializer
import JSON_Deserializer_Uint16StrConversion
import JSON_Deserializer_ByteStrConversion
import JSON_Deserializer
import JSON_ConcreteSyntax_Spec
import JSON_ConcreteSyntax_SpecProperties
import JSON_ConcreteSyntax
import JSON_ZeroCopy_Serializer
import JSON_ZeroCopy_Deserializer_Core
import JSON_ZeroCopy_Deserializer_Strings
import JSON_ZeroCopy_Deserializer_Numbers
import JSON_ZeroCopy_Deserializer_ObjectParams
import JSON_ZeroCopy_Deserializer_Objects
import JSON_ZeroCopy_Deserializer_ArrayParams
import JSON_ZeroCopy_Deserializer_Arrays
import JSON_ZeroCopy_Deserializer_Constants

# Module: JSON_ZeroCopy_Deserializer_Values

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Value(cs):
        d_849_c_ = (cs).Peek()
        if (d_849_c_) == (ord('{')):
            d_850_valueOrError0_ = JSON_ZeroCopy_Deserializer_Objects.default__.Object(cs, default__.ValueParser(cs))
            if (d_850_valueOrError0_).IsFailure():
                return (d_850_valueOrError0_).PropagateFailure()
            elif True:
                let_tmp_rhs22_ = (d_850_valueOrError0_).Extract()
                d_851_obj_ = let_tmp_rhs22_.t
                d_852_cs_k_ = let_tmp_rhs22_.cs
                d_853_v_ = JSON_Grammar.Value_Object(d_851_obj_)
                d_854_sp_ = JSON_Utils_Cursors.Split_SP(d_853_v_, d_852_cs_k_)
                return Wrappers.Result_Success(d_854_sp_)
        elif (d_849_c_) == (ord('[')):
            d_855_valueOrError1_ = JSON_ZeroCopy_Deserializer_Arrays.default__.Array(cs, default__.ValueParser(cs))
            if (d_855_valueOrError1_).IsFailure():
                return (d_855_valueOrError1_).PropagateFailure()
            elif True:
                let_tmp_rhs23_ = (d_855_valueOrError1_).Extract()
                d_856_arr_ = let_tmp_rhs23_.t
                d_857_cs_k_ = let_tmp_rhs23_.cs
                d_858_v_ = JSON_Grammar.Value_Array(d_856_arr_)
                d_859_sp_ = JSON_Utils_Cursors.Split_SP(d_858_v_, d_857_cs_k_)
                return Wrappers.Result_Success(d_859_sp_)
        elif (d_849_c_) == (ord('\"')):
            d_860_valueOrError2_ = JSON_ZeroCopy_Deserializer_Strings.default__.String(cs)
            if (d_860_valueOrError2_).IsFailure():
                return (d_860_valueOrError2_).PropagateFailure()
            elif True:
                let_tmp_rhs24_ = (d_860_valueOrError2_).Extract()
                d_861_str_ = let_tmp_rhs24_.t
                d_862_cs_k_ = let_tmp_rhs24_.cs
                return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.Value_String(d_861_str_), d_862_cs_k_))
        elif (d_849_c_) == (ord('t')):
            d_863_valueOrError3_ = JSON_ZeroCopy_Deserializer_Constants.default__.Constant(cs, JSON_Grammar.default__.TRUE)
            if (d_863_valueOrError3_).IsFailure():
                return (d_863_valueOrError3_).PropagateFailure()
            elif True:
                let_tmp_rhs25_ = (d_863_valueOrError3_).Extract()
                d_864_cst_ = let_tmp_rhs25_.t
                d_865_cs_k_ = let_tmp_rhs25_.cs
                return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.Value_Bool(d_864_cst_), d_865_cs_k_))
        elif (d_849_c_) == (ord('f')):
            d_866_valueOrError4_ = JSON_ZeroCopy_Deserializer_Constants.default__.Constant(cs, JSON_Grammar.default__.FALSE)
            if (d_866_valueOrError4_).IsFailure():
                return (d_866_valueOrError4_).PropagateFailure()
            elif True:
                let_tmp_rhs26_ = (d_866_valueOrError4_).Extract()
                d_867_cst_ = let_tmp_rhs26_.t
                d_868_cs_k_ = let_tmp_rhs26_.cs
                return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.Value_Bool(d_867_cst_), d_868_cs_k_))
        elif (d_849_c_) == (ord('n')):
            d_869_valueOrError5_ = JSON_ZeroCopy_Deserializer_Constants.default__.Constant(cs, JSON_Grammar.default__.NULL)
            if (d_869_valueOrError5_).IsFailure():
                return (d_869_valueOrError5_).PropagateFailure()
            elif True:
                let_tmp_rhs27_ = (d_869_valueOrError5_).Extract()
                d_870_cst_ = let_tmp_rhs27_.t
                d_871_cs_k_ = let_tmp_rhs27_.cs
                return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.Value_Null(d_870_cst_), d_871_cs_k_))
        elif True:
            d_872_valueOrError6_ = JSON_ZeroCopy_Deserializer_Numbers.default__.Number(cs)
            if (d_872_valueOrError6_).IsFailure():
                return (d_872_valueOrError6_).PropagateFailure()
            elif True:
                let_tmp_rhs28_ = (d_872_valueOrError6_).Extract()
                d_873_num_ = let_tmp_rhs28_.t
                d_874_cs_k_ = let_tmp_rhs28_.cs
                d_875_v_ = JSON_Grammar.Value_Number(d_873_num_)
                d_876_sp_ = JSON_Utils_Cursors.Split_SP(d_875_v_, d_874_cs_k_)
                return Wrappers.Result_Success(d_876_sp_)

    @staticmethod
    def ValueParser(cs):
        def lambda57_(d_878_cs_):
            def lambda58_(d_879_ps_k_):
                return ((d_879_ps_k_).Length()) < ((d_878_cs_).Length())

            return lambda58_

        d_877_pre_ = lambda57_(cs)
        def lambda59_(d_881_pre_):
            def lambda60_(d_882_ps_k_):
                return default__.Value(d_882_ps_k_)

            return lambda60_

        d_880_fn_ = lambda59_(d_877_pre_)
        return JSON_Utils_Parsers.SubParser___SubParser(d_880_fn_)

