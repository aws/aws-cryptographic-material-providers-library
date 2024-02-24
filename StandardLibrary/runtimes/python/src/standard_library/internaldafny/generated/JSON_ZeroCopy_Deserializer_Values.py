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
import DafnyLibraries
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
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
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
        d_764_c_ = (cs).Peek()
        if (d_764_c_) == (ord('{')):
            d_765_valueOrError0_ = JSON_ZeroCopy_Deserializer_Objects.default__.Object(cs, default__.ValueParser(cs))
            if (d_765_valueOrError0_).IsFailure():
                return (d_765_valueOrError0_).PropagateFailure()
            elif True:
                let_tmp_rhs16_ = (d_765_valueOrError0_).Extract()
                d_766_obj_ = let_tmp_rhs16_.t
                d_767_cs_k_ = let_tmp_rhs16_.cs
                d_768_v_ = JSON_Grammar.Value_Object(d_766_obj_)
                d_769_sp_ = JSON_Utils_Cursors.Split_SP(d_768_v_, d_767_cs_k_)
                return Wrappers.Result_Success(d_769_sp_)
        elif (d_764_c_) == (ord('[')):
            d_770_valueOrError1_ = JSON_ZeroCopy_Deserializer_Arrays.default__.Array(cs, default__.ValueParser(cs))
            if (d_770_valueOrError1_).IsFailure():
                return (d_770_valueOrError1_).PropagateFailure()
            elif True:
                let_tmp_rhs17_ = (d_770_valueOrError1_).Extract()
                d_771_arr_ = let_tmp_rhs17_.t
                d_772_cs_k_ = let_tmp_rhs17_.cs
                d_773_v_ = JSON_Grammar.Value_Array(d_771_arr_)
                d_774_sp_ = JSON_Utils_Cursors.Split_SP(d_773_v_, d_772_cs_k_)
                return Wrappers.Result_Success(d_774_sp_)
        elif (d_764_c_) == (ord('\"')):
            d_775_valueOrError2_ = JSON_ZeroCopy_Deserializer_Strings.default__.String(cs)
            if (d_775_valueOrError2_).IsFailure():
                return (d_775_valueOrError2_).PropagateFailure()
            elif True:
                let_tmp_rhs18_ = (d_775_valueOrError2_).Extract()
                d_776_str_ = let_tmp_rhs18_.t
                d_777_cs_k_ = let_tmp_rhs18_.cs
                return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.Value_String(d_776_str_), d_777_cs_k_))
        elif (d_764_c_) == (ord('t')):
            d_778_valueOrError3_ = JSON_ZeroCopy_Deserializer_Constants.default__.Constant(cs, JSON_Grammar.default__.TRUE)
            if (d_778_valueOrError3_).IsFailure():
                return (d_778_valueOrError3_).PropagateFailure()
            elif True:
                let_tmp_rhs19_ = (d_778_valueOrError3_).Extract()
                d_779_cst_ = let_tmp_rhs19_.t
                d_780_cs_k_ = let_tmp_rhs19_.cs
                return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.Value_Bool(d_779_cst_), d_780_cs_k_))
        elif (d_764_c_) == (ord('f')):
            d_781_valueOrError4_ = JSON_ZeroCopy_Deserializer_Constants.default__.Constant(cs, JSON_Grammar.default__.FALSE)
            if (d_781_valueOrError4_).IsFailure():
                return (d_781_valueOrError4_).PropagateFailure()
            elif True:
                let_tmp_rhs20_ = (d_781_valueOrError4_).Extract()
                d_782_cst_ = let_tmp_rhs20_.t
                d_783_cs_k_ = let_tmp_rhs20_.cs
                return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.Value_Bool(d_782_cst_), d_783_cs_k_))
        elif (d_764_c_) == (ord('n')):
            d_784_valueOrError5_ = JSON_ZeroCopy_Deserializer_Constants.default__.Constant(cs, JSON_Grammar.default__.NULL)
            if (d_784_valueOrError5_).IsFailure():
                return (d_784_valueOrError5_).PropagateFailure()
            elif True:
                let_tmp_rhs21_ = (d_784_valueOrError5_).Extract()
                d_785_cst_ = let_tmp_rhs21_.t
                d_786_cs_k_ = let_tmp_rhs21_.cs
                return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.Value_Null(d_785_cst_), d_786_cs_k_))
        elif True:
            d_787_valueOrError6_ = JSON_ZeroCopy_Deserializer_Numbers.default__.Number(cs)
            if (d_787_valueOrError6_).IsFailure():
                return (d_787_valueOrError6_).PropagateFailure()
            elif True:
                let_tmp_rhs22_ = (d_787_valueOrError6_).Extract()
                d_788_num_ = let_tmp_rhs22_.t
                d_789_cs_k_ = let_tmp_rhs22_.cs
                d_790_v_ = JSON_Grammar.Value_Number(d_788_num_)
                d_791_sp_ = JSON_Utils_Cursors.Split_SP(d_790_v_, d_789_cs_k_)
                return Wrappers.Result_Success(d_791_sp_)

    @staticmethod
    def ValueParser(cs):
        def lambda55_(d_793_cs_):
            def lambda56_(d_794_ps_k_):
                return ((d_794_ps_k_).Length()) < ((d_793_cs_).Length())

            return lambda56_

        d_792_pre_ = lambda55_(cs)
        def lambda57_(d_796_pre_):
            def lambda58_(d_797_ps_k_):
                return default__.Value(d_797_ps_k_)

            return lambda58_

        d_795_fn_ = lambda57_(d_792_pre_)
        return JSON_Utils_Parsers.SubParser___SubParser(d_795_fn_)

