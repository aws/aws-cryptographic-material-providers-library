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
import standard_library.internaldafny.generated.Sorting as Sorting
import standard_library.internaldafny.generated.SortedSets as SortedSets
import standard_library.internaldafny.generated.HexStrings as HexStrings
import standard_library.internaldafny.generated.GetOpt as GetOpt
import standard_library.internaldafny.generated.FloatCompare as FloatCompare
import standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import standard_library.internaldafny.generated.Base64 as Base64
import standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import standard_library.internaldafny.generated.Actions as Actions
import standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import standard_library.internaldafny.generated.JSON_Utils_Views_Core as JSON_Utils_Views_Core
import standard_library.internaldafny.generated.JSON_Utils_Views_Writers as JSON_Utils_Views_Writers
import standard_library.internaldafny.generated.JSON_Utils_Views as JSON_Utils_Views
import standard_library.internaldafny.generated.JSON_Utils_Lexers_Core as JSON_Utils_Lexers_Core
import standard_library.internaldafny.generated.JSON_Utils_Lexers_Strings as JSON_Utils_Lexers_Strings
import standard_library.internaldafny.generated.JSON_Utils_Lexers as JSON_Utils_Lexers
import standard_library.internaldafny.generated.JSON_Utils_Cursors as JSON_Utils_Cursors
import standard_library.internaldafny.generated.JSON_Utils_Parsers as JSON_Utils_Parsers
import standard_library.internaldafny.generated.JSON_Utils_Str_CharStrConversion as JSON_Utils_Str_CharStrConversion
import standard_library.internaldafny.generated.JSON_Utils_Str_CharStrEscaping as JSON_Utils_Str_CharStrEscaping
import standard_library.internaldafny.generated.JSON_Utils_Str as JSON_Utils_Str
import standard_library.internaldafny.generated.JSON_Utils_Seq as JSON_Utils_Seq
import standard_library.internaldafny.generated.JSON_Utils_Vectors as JSON_Utils_Vectors
import standard_library.internaldafny.generated.JSON_Utils as JSON_Utils
import standard_library.internaldafny.generated.JSON_Errors as JSON_Errors
import standard_library.internaldafny.generated.JSON_Values as JSON_Values
import standard_library.internaldafny.generated.JSON_Spec as JSON_Spec
import standard_library.internaldafny.generated.JSON_Grammar as JSON_Grammar
import standard_library.internaldafny.generated.JSON_Serializer_ByteStrConversion as JSON_Serializer_ByteStrConversion
import standard_library.internaldafny.generated.JSON_Serializer as JSON_Serializer
import standard_library.internaldafny.generated.JSON_Deserializer_Uint16StrConversion as JSON_Deserializer_Uint16StrConversion
import standard_library.internaldafny.generated.JSON_Deserializer_ByteStrConversion as JSON_Deserializer_ByteStrConversion
import standard_library.internaldafny.generated.JSON_Deserializer as JSON_Deserializer
import standard_library.internaldafny.generated.JSON_ConcreteSyntax_Spec as JSON_ConcreteSyntax_Spec
import standard_library.internaldafny.generated.JSON_ConcreteSyntax_SpecProperties as JSON_ConcreteSyntax_SpecProperties
import standard_library.internaldafny.generated.JSON_ConcreteSyntax as JSON_ConcreteSyntax
import standard_library.internaldafny.generated.JSON_ZeroCopy_Serializer as JSON_ZeroCopy_Serializer
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Core as JSON_ZeroCopy_Deserializer_Core
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Strings as JSON_ZeroCopy_Deserializer_Strings
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Numbers as JSON_ZeroCopy_Deserializer_Numbers
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_ObjectParams as JSON_ZeroCopy_Deserializer_ObjectParams
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Objects as JSON_ZeroCopy_Deserializer_Objects
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_ArrayParams as JSON_ZeroCopy_Deserializer_ArrayParams
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Arrays as JSON_ZeroCopy_Deserializer_Arrays
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Constants as JSON_ZeroCopy_Deserializer_Constants

# Module: JSON_ZeroCopy_Deserializer_Values

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Value(cs):
        d_820_c_ = (cs).Peek()
        if (d_820_c_) == (ord('{')):
            d_821_valueOrError0_ = JSON_ZeroCopy_Deserializer_Objects.default__.Object(cs, default__.ValueParser(cs))
            if (d_821_valueOrError0_).IsFailure():
                return (d_821_valueOrError0_).PropagateFailure()
            elif True:
                let_tmp_rhs22_ = (d_821_valueOrError0_).Extract()
                d_822_obj_ = let_tmp_rhs22_.t
                d_823_cs_k_ = let_tmp_rhs22_.cs
                d_824_v_ = JSON_Grammar.Value_Object(d_822_obj_)
                d_825_sp_ = JSON_Utils_Cursors.Split_SP(d_824_v_, d_823_cs_k_)
                return Wrappers.Result_Success(d_825_sp_)
        elif (d_820_c_) == (ord('[')):
            d_826_valueOrError1_ = JSON_ZeroCopy_Deserializer_Arrays.default__.Array(cs, default__.ValueParser(cs))
            if (d_826_valueOrError1_).IsFailure():
                return (d_826_valueOrError1_).PropagateFailure()
            elif True:
                let_tmp_rhs23_ = (d_826_valueOrError1_).Extract()
                d_827_arr_ = let_tmp_rhs23_.t
                d_828_cs_k_ = let_tmp_rhs23_.cs
                d_829_v_ = JSON_Grammar.Value_Array(d_827_arr_)
                d_830_sp_ = JSON_Utils_Cursors.Split_SP(d_829_v_, d_828_cs_k_)
                return Wrappers.Result_Success(d_830_sp_)
        elif (d_820_c_) == (ord('\"')):
            d_831_valueOrError2_ = JSON_ZeroCopy_Deserializer_Strings.default__.String(cs)
            if (d_831_valueOrError2_).IsFailure():
                return (d_831_valueOrError2_).PropagateFailure()
            elif True:
                let_tmp_rhs24_ = (d_831_valueOrError2_).Extract()
                d_832_str_ = let_tmp_rhs24_.t
                d_833_cs_k_ = let_tmp_rhs24_.cs
                return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.Value_String(d_832_str_), d_833_cs_k_))
        elif (d_820_c_) == (ord('t')):
            d_834_valueOrError3_ = JSON_ZeroCopy_Deserializer_Constants.default__.Constant(cs, JSON_Grammar.default__.TRUE)
            if (d_834_valueOrError3_).IsFailure():
                return (d_834_valueOrError3_).PropagateFailure()
            elif True:
                let_tmp_rhs25_ = (d_834_valueOrError3_).Extract()
                d_835_cst_ = let_tmp_rhs25_.t
                d_836_cs_k_ = let_tmp_rhs25_.cs
                return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.Value_Bool(d_835_cst_), d_836_cs_k_))
        elif (d_820_c_) == (ord('f')):
            d_837_valueOrError4_ = JSON_ZeroCopy_Deserializer_Constants.default__.Constant(cs, JSON_Grammar.default__.FALSE)
            if (d_837_valueOrError4_).IsFailure():
                return (d_837_valueOrError4_).PropagateFailure()
            elif True:
                let_tmp_rhs26_ = (d_837_valueOrError4_).Extract()
                d_838_cst_ = let_tmp_rhs26_.t
                d_839_cs_k_ = let_tmp_rhs26_.cs
                return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.Value_Bool(d_838_cst_), d_839_cs_k_))
        elif (d_820_c_) == (ord('n')):
            d_840_valueOrError5_ = JSON_ZeroCopy_Deserializer_Constants.default__.Constant(cs, JSON_Grammar.default__.NULL)
            if (d_840_valueOrError5_).IsFailure():
                return (d_840_valueOrError5_).PropagateFailure()
            elif True:
                let_tmp_rhs27_ = (d_840_valueOrError5_).Extract()
                d_841_cst_ = let_tmp_rhs27_.t
                d_842_cs_k_ = let_tmp_rhs27_.cs
                return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.Value_Null(d_841_cst_), d_842_cs_k_))
        elif True:
            d_843_valueOrError6_ = JSON_ZeroCopy_Deserializer_Numbers.default__.Number(cs)
            if (d_843_valueOrError6_).IsFailure():
                return (d_843_valueOrError6_).PropagateFailure()
            elif True:
                let_tmp_rhs28_ = (d_843_valueOrError6_).Extract()
                d_844_num_ = let_tmp_rhs28_.t
                d_845_cs_k_ = let_tmp_rhs28_.cs
                d_846_v_ = JSON_Grammar.Value_Number(d_844_num_)
                d_847_sp_ = JSON_Utils_Cursors.Split_SP(d_846_v_, d_845_cs_k_)
                return Wrappers.Result_Success(d_847_sp_)

    @staticmethod
    def ValueParser(cs):
        def lambda60_(d_849_cs_):
            def lambda61_(d_850_ps_k_):
                return ((d_850_ps_k_).Length()) < ((d_849_cs_).Length())

            return lambda61_

        d_848_pre_ = lambda60_(cs)
        def lambda62_(d_852_pre_):
            def lambda63_(d_853_ps_k_):
                return default__.Value(d_853_ps_k_)

            return lambda63_

        d_851_fn_ = lambda62_(d_848_pre_)
        return JSON_Utils_Parsers.SubParser___SubParser(d_851_fn_)

