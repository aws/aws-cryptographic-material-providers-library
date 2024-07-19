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

# Module: JSON_Spec

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def EscapeUnicode(c):
        d_497_sStr_ = JSON_Utils_Str.default__.OfNat(c, 16)
        d_498_s_ = UnicodeStrings.default__.ASCIIToUTF16(d_497_sStr_)
        return (d_498_s_) + (_dafny.Seq([ord(' ') for d_499___v0_ in range((4) - (len(d_498_s_)))]))

    @staticmethod
    def Escape(str, start):
        d_500___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                def lambda33_():
                    source11_ = (str)[start]
                    if True:
                        if (source11_) == (34):
                            return UnicodeStrings.default__.ASCIIToUTF16(_dafny.Seq("\\\""))
                    if True:
                        if (source11_) == (92):
                            return UnicodeStrings.default__.ASCIIToUTF16(_dafny.Seq("\\\\"))
                    if True:
                        if (source11_) == (8):
                            return UnicodeStrings.default__.ASCIIToUTF16(_dafny.Seq("\\b"))
                    if True:
                        if (source11_) == (12):
                            return UnicodeStrings.default__.ASCIIToUTF16(_dafny.Seq("\\f"))
                    if True:
                        if (source11_) == (10):
                            return UnicodeStrings.default__.ASCIIToUTF16(_dafny.Seq("\\n"))
                    if True:
                        if (source11_) == (13):
                            return UnicodeStrings.default__.ASCIIToUTF16(_dafny.Seq("\\r"))
                    if True:
                        if (source11_) == (9):
                            return UnicodeStrings.default__.ASCIIToUTF16(_dafny.Seq("\\t"))
                    if True:
                        d_501_c_ = source11_
                        if (d_501_c_) < (31):
                            return (UnicodeStrings.default__.ASCIIToUTF16(_dafny.Seq("\\u"))) + (default__.EscapeUnicode(d_501_c_))
                        elif True:
                            return _dafny.Seq([(str)[start]])

                if (start) >= (len(str)):
                    return (d_500___accumulator_) + (_dafny.Seq([]))
                elif True:
                    d_500___accumulator_ = (d_500___accumulator_) + (lambda33_())
                    in204_ = str
                    in205_ = (start) + (1)
                    str = in204_
                    start = in205_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def EscapeToUTF8(str, start):
        d_502_valueOrError0_ = (UnicodeStrings.default__.ToUTF16Checked(str)).ToResult_k(JSON_Errors.SerializationError_InvalidUnicode())
        if (d_502_valueOrError0_).IsFailure():
            return (d_502_valueOrError0_).PropagateFailure()
        elif True:
            d_503_utf16_ = (d_502_valueOrError0_).Extract()
            d_504_escaped_ = default__.Escape(d_503_utf16_, 0)
            d_505_valueOrError1_ = (UnicodeStrings.default__.FromUTF16Checked(d_504_escaped_)).ToResult_k(JSON_Errors.SerializationError_InvalidUnicode())
            if (d_505_valueOrError1_).IsFailure():
                return (d_505_valueOrError1_).PropagateFailure()
            elif True:
                d_506_utf32_ = (d_505_valueOrError1_).Extract()
                return (UnicodeStrings.default__.ToUTF8Checked(d_506_utf32_)).ToResult_k(JSON_Errors.SerializationError_InvalidUnicode())

    @staticmethod
    def String(str):
        d_507_valueOrError0_ = default__.EscapeToUTF8(str, 0)
        if (d_507_valueOrError0_).IsFailure():
            return (d_507_valueOrError0_).PropagateFailure()
        elif True:
            d_508_inBytes_ = (d_507_valueOrError0_).Extract()
            return Wrappers.Result_Success(((UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("\""))) + (d_508_inBytes_)) + (UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("\""))))

    @staticmethod
    def IntToBytes(n):
        d_509_s_ = JSON_Utils_Str.default__.OfInt(n, 10)
        return UnicodeStrings.default__.ASCIIToUTF8(d_509_s_)

    @staticmethod
    def Number(dec):
        return Wrappers.Result_Success((default__.IntToBytes((dec).n)) + ((_dafny.Seq([]) if ((dec).e10) == (0) else (UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("e"))) + (default__.IntToBytes((dec).e10)))))

    @staticmethod
    def KeyValue(kv):
        d_510_valueOrError0_ = default__.String((kv)[0])
        if (d_510_valueOrError0_).IsFailure():
            return (d_510_valueOrError0_).PropagateFailure()
        elif True:
            d_511_key_ = (d_510_valueOrError0_).Extract()
            d_512_valueOrError1_ = default__.JSON((kv)[1])
            if (d_512_valueOrError1_).IsFailure():
                return (d_512_valueOrError1_).PropagateFailure()
            elif True:
                d_513_value_ = (d_512_valueOrError1_).Extract()
                return Wrappers.Result_Success(((d_511_key_) + (UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq(":")))) + (d_513_value_))

    @staticmethod
    def Join(sep, items):
        if (len(items)) == (0):
            return Wrappers.Result_Success(_dafny.Seq([]))
        elif True:
            d_514_valueOrError0_ = (items)[0]
            if (d_514_valueOrError0_).IsFailure():
                return (d_514_valueOrError0_).PropagateFailure()
            elif True:
                d_515_first_ = (d_514_valueOrError0_).Extract()
                if (len(items)) == (1):
                    return Wrappers.Result_Success(d_515_first_)
                elif True:
                    d_516_valueOrError1_ = default__.Join(sep, _dafny.Seq((items)[1::]))
                    if (d_516_valueOrError1_).IsFailure():
                        return (d_516_valueOrError1_).PropagateFailure()
                    elif True:
                        d_517_rest_ = (d_516_valueOrError1_).Extract()
                        return Wrappers.Result_Success(((d_515_first_) + (sep)) + (d_517_rest_))

    @staticmethod
    def Object(obj):
        d_518_valueOrError0_ = default__.Join(UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq(",")), _dafny.Seq([default__.KeyValue((obj)[d_519_i_]) for d_519_i_ in range(len(obj))]))
        if (d_518_valueOrError0_).IsFailure():
            return (d_518_valueOrError0_).PropagateFailure()
        elif True:
            d_520_middle_ = (d_518_valueOrError0_).Extract()
            return Wrappers.Result_Success(((UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("{"))) + (d_520_middle_)) + (UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("}"))))

    @staticmethod
    def Array(arr):
        d_521_valueOrError0_ = default__.Join(UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq(",")), _dafny.Seq([default__.JSON((arr)[d_522_i_]) for d_522_i_ in range(len(arr))]))
        if (d_521_valueOrError0_).IsFailure():
            return (d_521_valueOrError0_).PropagateFailure()
        elif True:
            d_523_middle_ = (d_521_valueOrError0_).Extract()
            return Wrappers.Result_Success(((UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("["))) + (d_523_middle_)) + (UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("]"))))

    @staticmethod
    def JSON(js):
        source12_ = js
        if True:
            if source12_.is_Null:
                return Wrappers.Result_Success(UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("null")))
        if True:
            if source12_.is_Bool:
                d_524_b_ = source12_.b
                return Wrappers.Result_Success((UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("true")) if d_524_b_ else UnicodeStrings.default__.ASCIIToUTF8(_dafny.Seq("false"))))
        if True:
            if source12_.is_String:
                d_525_str_ = source12_.str
                return default__.String(d_525_str_)
        if True:
            if source12_.is_Number:
                d_526_dec_ = source12_.num
                return default__.Number(d_526_dec_)
        if True:
            if source12_.is_Object:
                d_527_obj_ = source12_.obj
                return default__.Object(d_527_obj_)
        if True:
            d_528_arr_ = source12_.arr
            return default__.Array(d_528_arr_)

