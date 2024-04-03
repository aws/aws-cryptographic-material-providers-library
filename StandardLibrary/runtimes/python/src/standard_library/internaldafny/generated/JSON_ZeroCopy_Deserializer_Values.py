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
        d_875_c_ = (cs).Peek()
        if (d_875_c_) == (ord('{')):
            d_876_valueOrError0_ = JSON_ZeroCopy_Deserializer_Objects.default__.Object(cs, default__.ValueParser(cs))
            if (d_876_valueOrError0_).IsFailure():
                return (d_876_valueOrError0_).PropagateFailure()
            elif True:
                let_tmp_rhs22_ = (d_876_valueOrError0_).Extract()
                d_877_obj_ = let_tmp_rhs22_.t
                d_878_cs_k_ = let_tmp_rhs22_.cs
                d_879_v_ = JSON_Grammar.Value_Object(d_877_obj_)
                d_880_sp_ = JSON_Utils_Cursors.Split_SP(d_879_v_, d_878_cs_k_)
                return Wrappers.Result_Success(d_880_sp_)
        elif (d_875_c_) == (ord('[')):
            d_881_valueOrError1_ = JSON_ZeroCopy_Deserializer_Arrays.default__.Array(cs, default__.ValueParser(cs))
            if (d_881_valueOrError1_).IsFailure():
                return (d_881_valueOrError1_).PropagateFailure()
            elif True:
                let_tmp_rhs23_ = (d_881_valueOrError1_).Extract()
                d_882_arr_ = let_tmp_rhs23_.t
                d_883_cs_k_ = let_tmp_rhs23_.cs
                d_884_v_ = JSON_Grammar.Value_Array(d_882_arr_)
                d_885_sp_ = JSON_Utils_Cursors.Split_SP(d_884_v_, d_883_cs_k_)
                return Wrappers.Result_Success(d_885_sp_)
        elif (d_875_c_) == (ord('\"')):
            d_886_valueOrError2_ = JSON_ZeroCopy_Deserializer_Strings.default__.String(cs)
            if (d_886_valueOrError2_).IsFailure():
                return (d_886_valueOrError2_).PropagateFailure()
            elif True:
                let_tmp_rhs24_ = (d_886_valueOrError2_).Extract()
                d_887_str_ = let_tmp_rhs24_.t
                d_888_cs_k_ = let_tmp_rhs24_.cs
                return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.Value_String(d_887_str_), d_888_cs_k_))
        elif (d_875_c_) == (ord('t')):
            d_889_valueOrError3_ = JSON_ZeroCopy_Deserializer_Constants.default__.Constant(cs, JSON_Grammar.default__.TRUE)
            if (d_889_valueOrError3_).IsFailure():
                return (d_889_valueOrError3_).PropagateFailure()
            elif True:
                let_tmp_rhs25_ = (d_889_valueOrError3_).Extract()
                d_890_cst_ = let_tmp_rhs25_.t
                d_891_cs_k_ = let_tmp_rhs25_.cs
                return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.Value_Bool(d_890_cst_), d_891_cs_k_))
        elif (d_875_c_) == (ord('f')):
            d_892_valueOrError4_ = JSON_ZeroCopy_Deserializer_Constants.default__.Constant(cs, JSON_Grammar.default__.FALSE)
            if (d_892_valueOrError4_).IsFailure():
                return (d_892_valueOrError4_).PropagateFailure()
            elif True:
                let_tmp_rhs26_ = (d_892_valueOrError4_).Extract()
                d_893_cst_ = let_tmp_rhs26_.t
                d_894_cs_k_ = let_tmp_rhs26_.cs
                return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.Value_Bool(d_893_cst_), d_894_cs_k_))
        elif (d_875_c_) == (ord('n')):
            d_895_valueOrError5_ = JSON_ZeroCopy_Deserializer_Constants.default__.Constant(cs, JSON_Grammar.default__.NULL)
            if (d_895_valueOrError5_).IsFailure():
                return (d_895_valueOrError5_).PropagateFailure()
            elif True:
                let_tmp_rhs27_ = (d_895_valueOrError5_).Extract()
                d_896_cst_ = let_tmp_rhs27_.t
                d_897_cs_k_ = let_tmp_rhs27_.cs
                return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.Value_Null(d_896_cst_), d_897_cs_k_))
        elif True:
            d_898_valueOrError6_ = JSON_ZeroCopy_Deserializer_Numbers.default__.Number(cs)
            if (d_898_valueOrError6_).IsFailure():
                return (d_898_valueOrError6_).PropagateFailure()
            elif True:
                let_tmp_rhs28_ = (d_898_valueOrError6_).Extract()
                d_899_num_ = let_tmp_rhs28_.t
                d_900_cs_k_ = let_tmp_rhs28_.cs
                d_901_v_ = JSON_Grammar.Value_Number(d_899_num_)
                d_902_sp_ = JSON_Utils_Cursors.Split_SP(d_901_v_, d_900_cs_k_)
                return Wrappers.Result_Success(d_902_sp_)

    @staticmethod
    def ValueParser(cs):
        def lambda58_(d_904_cs_):
            def lambda59_(d_905_ps_k_):
                return ((d_905_ps_k_).Length()) < ((d_904_cs_).Length())

            return lambda59_

        d_903_pre_ = lambda58_(cs)
        def lambda60_(d_907_pre_):
            def lambda61_(d_908_ps_k_):
                return default__.Value(d_908_ps_k_)

            return lambda61_

        d_906_fn_ = lambda60_(d_903_pre_)
        return JSON_Utils_Parsers.SubParser___SubParser(d_906_fn_)

