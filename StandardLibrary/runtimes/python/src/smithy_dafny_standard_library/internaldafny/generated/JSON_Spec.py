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
import smithy_dafny_standard_library.internaldafny.generated.Sorting as Sorting
import smithy_dafny_standard_library.internaldafny.generated.SortedSets as SortedSets
import smithy_dafny_standard_library.internaldafny.generated.HexStrings as HexStrings
import smithy_dafny_standard_library.internaldafny.generated.GetOpt as GetOpt
import smithy_dafny_standard_library.internaldafny.generated.FloatCompare as FloatCompare
import smithy_dafny_standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import smithy_dafny_standard_library.internaldafny.generated.Base64 as Base64
import smithy_dafny_standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import smithy_dafny_standard_library.internaldafny.generated.Actions as Actions
import smithy_dafny_standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Views_Core as JSON_Utils_Views_Core
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Views_Writers as JSON_Utils_Views_Writers
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Views as JSON_Utils_Views
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Lexers_Core as JSON_Utils_Lexers_Core
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Lexers_Strings as JSON_Utils_Lexers_Strings
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Lexers as JSON_Utils_Lexers
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Cursors as JSON_Utils_Cursors
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Parsers as JSON_Utils_Parsers
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Str_CharStrConversion as JSON_Utils_Str_CharStrConversion
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Str_CharStrEscaping as JSON_Utils_Str_CharStrEscaping
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Str as JSON_Utils_Str
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Seq as JSON_Utils_Seq
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Vectors as JSON_Utils_Vectors
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils as JSON_Utils
import smithy_dafny_standard_library.internaldafny.generated.JSON_Errors as JSON_Errors
import smithy_dafny_standard_library.internaldafny.generated.JSON_Values as JSON_Values

# Module: JSON_Spec

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def EscapeUnicode(c):
        d_0_sStr_ = JSON_Utils_Str.default__.OfNat(c, 16)
        d_1_s_ = UnicodeStrings.default__.ASCIIToUTF16(d_0_sStr_)
        return (d_1_s_) + (_dafny.Seq([ord(' ') for d_2___v0_ in range((4) - (len(d_1_s_)))]))

    @staticmethod
    def Escape(str, start):
        d_0___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                def lambda0_():
                    source0_ = (str)[start]
                    if True:
                        if (source0_) == (34):
                            return UnicodeStrings.default__.ASCIIToUTF16(_dafny.Seq("\\\""))
                    if True:
                        if (source0_) == (92):
                            return UnicodeStrings.default__.ASCIIToUTF16(_dafny.Seq("\\\\"))
                    if True:
                        if (source0_) == (8):
                            return UnicodeStrings.default__.ASCIIToUTF16(_dafny.Seq("\\b"))
                    if True:
                        if (source0_) == (12):
                            return UnicodeStrings.default__.ASCIIToUTF16(_dafny.Seq("\\f"))
                    if True:
                        if (source0_) == (10):
                            return UnicodeStrings.default__.ASCIIToUTF16(_dafny.Seq("\\n"))
                    if True:
                        if (source0_) == (13):
                            return UnicodeStrings.default__.ASCIIToUTF16(_dafny.Seq("\\r"))
                    if True:
                        if (source0_) == (9):
                            return UnicodeStrings.default__.ASCIIToUTF16(_dafny.Seq("\\t"))
                    if True:
                        d_1_c_ = source0_
                        if (d_1_c_) < (31):
                            return (UnicodeStrings.default__.ASCIIToUTF16(_dafny.Seq("\\u"))) + (default__.EscapeUnicode(d_1_c_))
                        elif True:
                            return _dafny.Seq([(str)[start]])

                if (start) >= (len(str)):
                    return (d_0___accumulator_) + (_dafny.Seq([]))
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (lambda0_())
                    in0_ = str
                    in1_ = (start) + (1)
                    str = in0_
                    start = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def EscapeToUTF8(str, start):
        d_0_valueOrError0_ = (UnicodeStrings.default__.ToUTF16Checked(str)).ToResult_k(JSON_Errors.SerializationError_InvalidUnicode())
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_1_utf16_ = (d_0_valueOrError0_).Extract()
            d_2_escaped_ = default__.Escape(d_1_utf16_, 0)
            d_3_valueOrError1_ = (UnicodeStrings.default__.FromUTF16Checked(d_2_escaped_)).ToResult_k(JSON_Errors.SerializationError_InvalidUnicode())
            if (d_3_valueOrError1_).IsFailure():
                return (d_3_valueOrError1_).PropagateFailure()
            elif True:
                d_4_utf32_ = (d_3_valueOrError1_).Extract()
                return (UnicodeStrings.default__.ToUTF8Checked(d_4_utf32_)).ToResult_k(JSON_Errors.SerializationError_InvalidUnicode())

    @staticmethod
    def String(str):
        d_0_valueOrError0_ = default__.EscapeToUTF8(str, 0)
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_1_inBytes_ = (d_0_valueOrError0_).Extract()
            return Wrappers.Result_Success(((UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("\""))) + (d_1_inBytes_)) + (UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("\""))))

    @staticmethod
    def IntToBytes(n):
        d_0_s_ = JSON_Utils_Str.default__.OfInt(n, 10)
        return UnicodeStrings.default__.ASCIIToUTF8(d_0_s_)

    @staticmethod
    def Number(dec):
        return Wrappers.Result_Success((default__.IntToBytes((dec).n)) + ((_dafny.Seq([]) if ((dec).e10) == (0) else (UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("e"))) + (default__.IntToBytes((dec).e10)))))

    @staticmethod
    def KeyValue(kv):
        d_0_valueOrError0_ = default__.String((kv)[0])
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_1_key_ = (d_0_valueOrError0_).Extract()
            d_2_valueOrError1_ = default__.JSON((kv)[1])
            if (d_2_valueOrError1_).IsFailure():
                return (d_2_valueOrError1_).PropagateFailure()
            elif True:
                d_3_value_ = (d_2_valueOrError1_).Extract()
                return Wrappers.Result_Success(((d_1_key_) + (UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq(":")))) + (d_3_value_))

    @staticmethod
    def Join(sep, items):
        if (len(items)) == (0):
            return Wrappers.Result_Success(_dafny.Seq([]))
        elif True:
            d_0_valueOrError0_ = (items)[0]
            if (d_0_valueOrError0_).IsFailure():
                return (d_0_valueOrError0_).PropagateFailure()
            elif True:
                d_1_first_ = (d_0_valueOrError0_).Extract()
                if (len(items)) == (1):
                    return Wrappers.Result_Success(d_1_first_)
                elif True:
                    d_2_valueOrError1_ = default__.Join(sep, _dafny.Seq((items)[1::]))
                    if (d_2_valueOrError1_).IsFailure():
                        return (d_2_valueOrError1_).PropagateFailure()
                    elif True:
                        d_3_rest_ = (d_2_valueOrError1_).Extract()
                        return Wrappers.Result_Success(((d_1_first_) + (sep)) + (d_3_rest_))

    @staticmethod
    def Object(obj):
        d_0_valueOrError0_ = default__.Join(UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq(",")), _dafny.Seq([default__.KeyValue((obj)[d_1_i_]) for d_1_i_ in range(len(obj))]))
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_2_middle_ = (d_0_valueOrError0_).Extract()
            return Wrappers.Result_Success(((UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("{"))) + (d_2_middle_)) + (UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("}"))))

    @staticmethod
    def Array(arr):
        d_0_valueOrError0_ = default__.Join(UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq(",")), _dafny.Seq([default__.JSON((arr)[d_1_i_]) for d_1_i_ in range(len(arr))]))
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_2_middle_ = (d_0_valueOrError0_).Extract()
            return Wrappers.Result_Success(((UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("["))) + (d_2_middle_)) + (UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("]"))))

    @staticmethod
    def JSON(js):
        source0_ = js
        if True:
            if source0_.is_Null:
                return Wrappers.Result_Success(UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("null")))
        if True:
            if source0_.is_Bool:
                d_0_b_ = source0_.b
                return Wrappers.Result_Success((UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("true")) if d_0_b_ else UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("false"))))
        if True:
            if source0_.is_String:
                d_1_str_ = source0_.str
                return default__.String(d_1_str_)
        if True:
            if source0_.is_Number:
                d_2_dec_ = source0_.num
                return default__.Number(d_2_dec_)
        if True:
            if source0_.is_Object:
                d_3_obj_ = source0_.obj
                return default__.Object(d_3_obj_)
        if True:
            d_4_arr_ = source0_.arr
            return default__.Array(d_4_arr_)

