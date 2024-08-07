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

# Module: JSON_ZeroCopy_Deserializer_Numbers

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Digits(cs):
        return ((cs).SkipWhile(JSON_Grammar.default__.Digit_q)).Split()

    @staticmethod
    def NonEmptyDigits(cs):
        d_719_sp_ = default__.Digits(cs)
        d_720_valueOrError0_ = Wrappers.default__.Need(not(((d_719_sp_).t).Empty_q), JSON_Utils_Cursors.CursorError_OtherError(JSON_Errors.DeserializationError_EmptyNumber()))
        if (d_720_valueOrError0_).IsFailure():
            return (d_720_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(d_719_sp_)

    @staticmethod
    def NonZeroInt(cs):
        return default__.NonEmptyDigits(cs)

    @staticmethod
    def OptionalMinus(cs):
        def lambda55_(d_721_c_):
            return (d_721_c_) == (ord('-'))

        return ((cs).SkipIf(lambda55_)).Split()

    @staticmethod
    def OptionalSign(cs):
        def lambda56_(d_722_c_):
            return ((d_722_c_) == (ord('-'))) or ((d_722_c_) == (ord('+')))

        return ((cs).SkipIf(lambda56_)).Split()

    @staticmethod
    def TrimmedInt(cs):
        def lambda57_(d_724_c_):
            return (d_724_c_) == (ord('0'))

        d_723_sp_ = ((cs).SkipIf(lambda57_)).Split()
        if ((d_723_sp_).t).Empty_q:
            return default__.NonZeroInt((d_723_sp_).cs)
        elif True:
            return Wrappers.Result_Success(d_723_sp_)

    @staticmethod
    def Exp(cs):
        def lambda58_(d_725_c_):
            return ((d_725_c_) == (ord('e'))) or ((d_725_c_) == (ord('E')))

        let_tmp_rhs17_ = ((cs).SkipIf(lambda58_)).Split()
        d_726_e_ = let_tmp_rhs17_.t
        d_727_cs_ = let_tmp_rhs17_.cs
        if (d_726_e_).Empty_q:
            return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.Maybe_Empty(), d_727_cs_))
        elif True:
            let_tmp_rhs18_ = default__.OptionalSign(d_727_cs_)
            d_728_sign_ = let_tmp_rhs18_.t
            d_729_cs_ = let_tmp_rhs18_.cs
            d_730_valueOrError0_ = default__.NonEmptyDigits(d_729_cs_)
            if (d_730_valueOrError0_).IsFailure():
                return (d_730_valueOrError0_).PropagateFailure()
            elif True:
                let_tmp_rhs19_ = (d_730_valueOrError0_).Extract()
                d_731_num_ = let_tmp_rhs19_.t
                d_732_cs_ = let_tmp_rhs19_.cs
                return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.Maybe_NonEmpty(JSON_Grammar.jexp_JExp(d_726_e_, d_728_sign_, d_731_num_)), d_732_cs_))

    @staticmethod
    def Frac(cs):
        def lambda59_(d_733_c_):
            return (d_733_c_) == (ord('.'))

        let_tmp_rhs20_ = ((cs).SkipIf(lambda59_)).Split()
        d_734_period_ = let_tmp_rhs20_.t
        d_735_cs_ = let_tmp_rhs20_.cs
        if (d_734_period_).Empty_q:
            return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.Maybe_Empty(), d_735_cs_))
        elif True:
            d_736_valueOrError0_ = default__.NonEmptyDigits(d_735_cs_)
            if (d_736_valueOrError0_).IsFailure():
                return (d_736_valueOrError0_).PropagateFailure()
            elif True:
                let_tmp_rhs21_ = (d_736_valueOrError0_).Extract()
                d_737_num_ = let_tmp_rhs21_.t
                d_738_cs_ = let_tmp_rhs21_.cs
                return Wrappers.Result_Success(JSON_Utils_Cursors.Split_SP(JSON_Grammar.Maybe_NonEmpty(JSON_Grammar.jfrac_JFrac(d_734_period_, d_737_num_)), d_738_cs_))

    @staticmethod
    def NumberFromParts(minus, num, frac, exp):
        d_739_sp_ = JSON_Utils_Cursors.Split_SP(JSON_Grammar.jnumber_JNumber((minus).t, (num).t, (frac).t, (exp).t), (exp).cs)
        return d_739_sp_

    @staticmethod
    def Number(cs):
        d_740_minus_ = default__.OptionalMinus(cs)
        d_741_valueOrError0_ = default__.TrimmedInt((d_740_minus_).cs)
        if (d_741_valueOrError0_).IsFailure():
            return (d_741_valueOrError0_).PropagateFailure()
        elif True:
            d_742_num_ = (d_741_valueOrError0_).Extract()
            d_743_valueOrError1_ = default__.Frac((d_742_num_).cs)
            if (d_743_valueOrError1_).IsFailure():
                return (d_743_valueOrError1_).PropagateFailure()
            elif True:
                d_744_frac_ = (d_743_valueOrError1_).Extract()
                d_745_valueOrError2_ = default__.Exp((d_744_frac_).cs)
                if (d_745_valueOrError2_).IsFailure():
                    return (d_745_valueOrError2_).PropagateFailure()
                elif True:
                    d_746_exp_ = (d_745_valueOrError2_).Extract()
                    return Wrappers.Result_Success(default__.NumberFromParts(d_740_minus_, d_742_num_, d_744_frac_, d_746_exp_))

