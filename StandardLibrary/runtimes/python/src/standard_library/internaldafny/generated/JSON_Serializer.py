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

# Module: JSON_Serializer

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Bool(b):
        return JSON_Utils_Views_Core.View__.OfBytes((JSON_Grammar.default__.TRUE if b else JSON_Grammar.default__.FALSE))

    @staticmethod
    def CheckLength(s, err):
        return Wrappers.default__.Need((len(s)) < (BoundedInts.default__.TWO__TO__THE__32), err)

    @staticmethod
    def String(str):
        d_454_valueOrError0_ = JSON_Spec.default__.EscapeToUTF8(str, 0)
        if (d_454_valueOrError0_).IsFailure():
            return (d_454_valueOrError0_).PropagateFailure()
        elif True:
            d_455_bs_ = (d_454_valueOrError0_).Extract()
            d_456_valueOrError1_ = default__.CheckLength(d_455_bs_, JSON_Errors.SerializationError_StringTooLong(str))
            if (d_456_valueOrError1_).IsFailure():
                return (d_456_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success(JSON_Grammar.jstring_JString(JSON_Grammar.default__.DOUBLEQUOTE, JSON_Utils_Views_Core.View__.OfBytes(d_455_bs_), JSON_Grammar.default__.DOUBLEQUOTE))

    @staticmethod
    def Sign(n):
        return JSON_Utils_Views_Core.View__.OfBytes((_dafny.Seq([ord('-')]) if (n) < (0) else _dafny.Seq([])))

    @staticmethod
    def Int_k(n):
        return JSON_Serializer_ByteStrConversion.default__.OfInt__any(n, default__.DIGITS, default__.MINUS)

    @staticmethod
    def Int(n):
        d_457_bs_ = default__.Int_k(n)
        d_458_valueOrError0_ = default__.CheckLength(d_457_bs_, JSON_Errors.SerializationError_IntTooLarge(n))
        if (d_458_valueOrError0_).IsFailure():
            return (d_458_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(JSON_Utils_Views_Core.View__.OfBytes(d_457_bs_))

    @staticmethod
    def Number(dec):
        pat_let_tv4_ = dec
        pat_let_tv5_ = dec
        d_459_minus_ = default__.Sign((dec).n)
        d_460_valueOrError0_ = default__.Int(Math.default__.Abs((dec).n))
        if (d_460_valueOrError0_).IsFailure():
            return (d_460_valueOrError0_).PropagateFailure()
        elif True:
            d_461_num_ = (d_460_valueOrError0_).Extract()
            d_462_frac_ = JSON_Grammar.Maybe_Empty()
            def iife4_(_pat_let2_0):
                def iife5_(d_464_e_):
                    def iife6_(_pat_let3_0):
                        def iife7_(d_465_sign_):
                            def iife8_(_pat_let4_0):
                                def iife9_(d_466_valueOrError2_):
                                    def iife10_(_pat_let5_0):
                                        def iife11_(d_467_num_):
                                            return Wrappers.Result_Success(JSON_Grammar.Maybe_NonEmpty(JSON_Grammar.jexp_JExp(d_464_e_, d_465_sign_, d_467_num_)))
                                        return iife11_(_pat_let5_0)
                                    return ((d_466_valueOrError2_).PropagateFailure() if (d_466_valueOrError2_).IsFailure() else iife10_((d_466_valueOrError2_).Extract()))
                                return iife9_(_pat_let4_0)
                            return iife8_(default__.Int(Math.default__.Abs((pat_let_tv5_).e10)))
                        return iife7_(_pat_let3_0)
                    return iife6_(default__.Sign((pat_let_tv4_).e10))
                return iife5_(_pat_let2_0)
            d_463_valueOrError1_ = (Wrappers.Result_Success(JSON_Grammar.Maybe_Empty()) if ((dec).e10) == (0) else iife4_(JSON_Utils_Views_Core.View__.OfBytes(_dafny.Seq([ord('e')]))))
            if (d_463_valueOrError1_).IsFailure():
                return (d_463_valueOrError1_).PropagateFailure()
            elif True:
                d_468_exp_ = (d_463_valueOrError1_).Extract()
                return Wrappers.Result_Success(JSON_Grammar.jnumber_JNumber(d_459_minus_, d_461_num_, JSON_Grammar.Maybe_Empty(), d_468_exp_))

    @staticmethod
    def MkStructural(v):
        return JSON_Grammar.Structural_Structural(JSON_Grammar.default__.EMPTY, v, JSON_Grammar.default__.EMPTY)

    @staticmethod
    def KeyValue(kv):
        d_469_valueOrError0_ = default__.String((kv)[0])
        if (d_469_valueOrError0_).IsFailure():
            return (d_469_valueOrError0_).PropagateFailure()
        elif True:
            d_470_k_ = (d_469_valueOrError0_).Extract()
            d_471_valueOrError1_ = default__.Value((kv)[1])
            if (d_471_valueOrError1_).IsFailure():
                return (d_471_valueOrError1_).PropagateFailure()
            elif True:
                d_472_v_ = (d_471_valueOrError1_).Extract()
                return Wrappers.Result_Success(JSON_Grammar.jKeyValue_KeyValue(d_470_k_, default__.COLON, d_472_v_))

    @staticmethod
    def MkSuffixedSequence(ds, suffix, start):
        d_473___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (start) >= (len(ds)):
                    return (d_473___accumulator_) + (_dafny.Seq([]))
                elif (start) == ((len(ds)) - (1)):
                    return (d_473___accumulator_) + (_dafny.Seq([JSON_Grammar.Suffixed_Suffixed((ds)[start], JSON_Grammar.Maybe_Empty())]))
                elif True:
                    d_473___accumulator_ = (d_473___accumulator_) + (_dafny.Seq([JSON_Grammar.Suffixed_Suffixed((ds)[start], JSON_Grammar.Maybe_NonEmpty(suffix))]))
                    in105_ = ds
                    in106_ = suffix
                    in107_ = (start) + (1)
                    ds = in105_
                    suffix = in106_
                    start = in107_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def Object(obj):
        def lambda31_(d_475_obj_):
            def lambda32_(d_476_v_):
                return default__.KeyValue(d_476_v_)

            return lambda32_

        d_474_valueOrError0_ = Seq.default__.MapWithResult(lambda31_(obj), obj)
        if (d_474_valueOrError0_).IsFailure():
            return (d_474_valueOrError0_).PropagateFailure()
        elif True:
            d_477_items_ = (d_474_valueOrError0_).Extract()
            return Wrappers.Result_Success(JSON_Grammar.Bracketed_Bracketed(default__.MkStructural(JSON_Grammar.default__.LBRACE), default__.MkSuffixedSequence(d_477_items_, default__.COMMA, 0), default__.MkStructural(JSON_Grammar.default__.RBRACE)))

    @staticmethod
    def Array(arr):
        def lambda33_(d_479_arr_):
            def lambda34_(d_480_v_):
                return default__.Value(d_480_v_)

            return lambda34_

        d_478_valueOrError0_ = Seq.default__.MapWithResult(lambda33_(arr), arr)
        if (d_478_valueOrError0_).IsFailure():
            return (d_478_valueOrError0_).PropagateFailure()
        elif True:
            d_481_items_ = (d_478_valueOrError0_).Extract()
            return Wrappers.Result_Success(JSON_Grammar.Bracketed_Bracketed(default__.MkStructural(JSON_Grammar.default__.LBRACKET), default__.MkSuffixedSequence(d_481_items_, default__.COMMA, 0), default__.MkStructural(JSON_Grammar.default__.RBRACKET)))

    @staticmethod
    def Value(js):
        source12_ = js
        if source12_.is_Null:
            return Wrappers.Result_Success(JSON_Grammar.Value_Null(JSON_Utils_Views_Core.View__.OfBytes(JSON_Grammar.default__.NULL)))
        elif source12_.is_Bool:
            d_482___mcc_h0_ = source12_.b
            d_483_b_ = d_482___mcc_h0_
            return Wrappers.Result_Success(JSON_Grammar.Value_Bool(default__.Bool(d_483_b_)))
        elif source12_.is_String:
            d_484___mcc_h1_ = source12_.str
            d_485_str_ = d_484___mcc_h1_
            d_486_valueOrError0_ = default__.String(d_485_str_)
            if (d_486_valueOrError0_).IsFailure():
                return (d_486_valueOrError0_).PropagateFailure()
            elif True:
                d_487_s_ = (d_486_valueOrError0_).Extract()
                return Wrappers.Result_Success(JSON_Grammar.Value_String(d_487_s_))
        elif source12_.is_Number:
            d_488___mcc_h2_ = source12_.num
            d_489_dec_ = d_488___mcc_h2_
            d_490_valueOrError1_ = default__.Number(d_489_dec_)
            if (d_490_valueOrError1_).IsFailure():
                return (d_490_valueOrError1_).PropagateFailure()
            elif True:
                d_491_n_ = (d_490_valueOrError1_).Extract()
                return Wrappers.Result_Success(JSON_Grammar.Value_Number(d_491_n_))
        elif source12_.is_Object:
            d_492___mcc_h3_ = source12_.obj
            d_493_obj_ = d_492___mcc_h3_
            d_494_valueOrError2_ = default__.Object(d_493_obj_)
            if (d_494_valueOrError2_).IsFailure():
                return (d_494_valueOrError2_).PropagateFailure()
            elif True:
                d_495_o_ = (d_494_valueOrError2_).Extract()
                return Wrappers.Result_Success(JSON_Grammar.Value_Object(d_495_o_))
        elif True:
            d_496___mcc_h4_ = source12_.arr
            d_497_arr_ = d_496___mcc_h4_
            d_498_valueOrError3_ = default__.Array(d_497_arr_)
            if (d_498_valueOrError3_).IsFailure():
                return (d_498_valueOrError3_).PropagateFailure()
            elif True:
                d_499_a_ = (d_498_valueOrError3_).Extract()
                return Wrappers.Result_Success(JSON_Grammar.Value_Array(d_499_a_))

    @staticmethod
    def JSON(js):
        d_500_valueOrError0_ = default__.Value(js)
        if (d_500_valueOrError0_).IsFailure():
            return (d_500_valueOrError0_).PropagateFailure()
        elif True:
            d_501_val_ = (d_500_valueOrError0_).Extract()
            return Wrappers.Result_Success(default__.MkStructural(d_501_val_))

    @_dafny.classproperty
    def DIGITS(instance):
        return _dafny.Seq([ord('0'), ord('1'), ord('2'), ord('3'), ord('4'), ord('5'), ord('6'), ord('7'), ord('8'), ord('9')])
    @_dafny.classproperty
    def MINUS(instance):
        return ord('-')
    @_dafny.classproperty
    def COLON(instance):
        return default__.MkStructural(JSON_Grammar.default__.COLON)
    @_dafny.classproperty
    def COMMA(instance):
        return default__.MkStructural(JSON_Grammar.default__.COMMA)

class bytes32:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})

class string32:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
