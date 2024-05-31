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
        d_563_valueOrError0_ = JSON_Spec.default__.EscapeToUTF8(str, 0)
        if (d_563_valueOrError0_).IsFailure():
            return (d_563_valueOrError0_).PropagateFailure()
        elif True:
            d_564_bs_ = (d_563_valueOrError0_).Extract()
            d_565_valueOrError1_ = default__.CheckLength(d_564_bs_, JSON_Errors.SerializationError_StringTooLong(str))
            if (d_565_valueOrError1_).IsFailure():
                return (d_565_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success(JSON_Grammar.jstring_JString(JSON_Grammar.default__.DOUBLEQUOTE, JSON_Utils_Views_Core.View__.OfBytes(d_564_bs_), JSON_Grammar.default__.DOUBLEQUOTE))

    @staticmethod
    def Sign(n):
        return JSON_Utils_Views_Core.View__.OfBytes((_dafny.Seq([ord('-')]) if (n) < (0) else _dafny.Seq([])))

    @staticmethod
    def Int_k(n):
        return JSON_Serializer_ByteStrConversion.default__.OfInt__any(n, default__.DIGITS, default__.MINUS)

    @staticmethod
    def Int(n):
        d_566_bs_ = default__.Int_k(n)
        d_567_valueOrError0_ = default__.CheckLength(d_566_bs_, JSON_Errors.SerializationError_IntTooLarge(n))
        if (d_567_valueOrError0_).IsFailure():
            return (d_567_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(JSON_Utils_Views_Core.View__.OfBytes(d_566_bs_))

    @staticmethod
    def Number(dec):
        pat_let_tv6_ = dec
        pat_let_tv7_ = dec
        d_568_minus_ = default__.Sign((dec).n)
        d_569_valueOrError0_ = default__.Int(Math.default__.Abs((dec).n))
        if (d_569_valueOrError0_).IsFailure():
            return (d_569_valueOrError0_).PropagateFailure()
        elif True:
            d_570_num_ = (d_569_valueOrError0_).Extract()
            d_571_frac_ = JSON_Grammar.Maybe_Empty()
            def iife14_(_pat_let7_0):
                def iife15_(d_573_e_):
                    def iife16_(_pat_let8_0):
                        def iife17_(d_574_sign_):
                            def iife18_(_pat_let9_0):
                                def iife19_(d_575_valueOrError2_):
                                    def iife20_(_pat_let10_0):
                                        def iife21_(d_576_num_):
                                            return Wrappers.Result_Success(JSON_Grammar.Maybe_NonEmpty(JSON_Grammar.jexp_JExp(d_573_e_, d_574_sign_, d_576_num_)))
                                        return iife21_(_pat_let10_0)
                                    return ((d_575_valueOrError2_).PropagateFailure() if (d_575_valueOrError2_).IsFailure() else iife20_((d_575_valueOrError2_).Extract()))
                                return iife19_(_pat_let9_0)
                            return iife18_(default__.Int(Math.default__.Abs((pat_let_tv7_).e10)))
                        return iife17_(_pat_let8_0)
                    return iife16_(default__.Sign((pat_let_tv6_).e10))
                return iife15_(_pat_let7_0)
            d_572_valueOrError1_ = (Wrappers.Result_Success(JSON_Grammar.Maybe_Empty()) if ((dec).e10) == (0) else iife14_(JSON_Utils_Views_Core.View__.OfBytes(_dafny.Seq([ord('e')]))))
            if (d_572_valueOrError1_).IsFailure():
                return (d_572_valueOrError1_).PropagateFailure()
            elif True:
                d_577_exp_ = (d_572_valueOrError1_).Extract()
                return Wrappers.Result_Success(JSON_Grammar.jnumber_JNumber(d_568_minus_, d_570_num_, JSON_Grammar.Maybe_Empty(), d_577_exp_))

    @staticmethod
    def MkStructural(v):
        return JSON_Grammar.Structural_Structural(JSON_Grammar.default__.EMPTY, v, JSON_Grammar.default__.EMPTY)

    @staticmethod
    def KeyValue(kv):
        d_578_valueOrError0_ = default__.String((kv)[0])
        if (d_578_valueOrError0_).IsFailure():
            return (d_578_valueOrError0_).PropagateFailure()
        elif True:
            d_579_k_ = (d_578_valueOrError0_).Extract()
            d_580_valueOrError1_ = default__.Value((kv)[1])
            if (d_580_valueOrError1_).IsFailure():
                return (d_580_valueOrError1_).PropagateFailure()
            elif True:
                d_581_v_ = (d_580_valueOrError1_).Extract()
                return Wrappers.Result_Success(JSON_Grammar.jKeyValue_KeyValue(d_579_k_, default__.COLON, d_581_v_))

    @staticmethod
    def MkSuffixedSequence(ds, suffix, start):
        d_582___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (start) >= (len(ds)):
                    return (d_582___accumulator_) + (_dafny.Seq([]))
                elif (start) == ((len(ds)) - (1)):
                    return (d_582___accumulator_) + (_dafny.Seq([JSON_Grammar.Suffixed_Suffixed((ds)[start], JSON_Grammar.Maybe_Empty())]))
                elif True:
                    d_582___accumulator_ = (d_582___accumulator_) + (_dafny.Seq([JSON_Grammar.Suffixed_Suffixed((ds)[start], JSON_Grammar.Maybe_NonEmpty(suffix))]))
                    in208_ = ds
                    in209_ = suffix
                    in210_ = (start) + (1)
                    ds = in208_
                    suffix = in209_
                    start = in210_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def Object(obj):
        def lambda34_(d_584_obj_):
            def lambda35_(d_585_v_):
                return default__.KeyValue(d_585_v_)

            return lambda35_

        d_583_valueOrError0_ = Seq.default__.MapWithResult(lambda34_(obj), obj)
        if (d_583_valueOrError0_).IsFailure():
            return (d_583_valueOrError0_).PropagateFailure()
        elif True:
            d_586_items_ = (d_583_valueOrError0_).Extract()
            return Wrappers.Result_Success(JSON_Grammar.Bracketed_Bracketed(default__.MkStructural(JSON_Grammar.default__.LBRACE), default__.MkSuffixedSequence(d_586_items_, default__.COMMA, 0), default__.MkStructural(JSON_Grammar.default__.RBRACE)))

    @staticmethod
    def Array(arr):
        def lambda36_(d_588_arr_):
            def lambda37_(d_589_v_):
                return default__.Value(d_589_v_)

            return lambda37_

        d_587_valueOrError0_ = Seq.default__.MapWithResult(lambda36_(arr), arr)
        if (d_587_valueOrError0_).IsFailure():
            return (d_587_valueOrError0_).PropagateFailure()
        elif True:
            d_590_items_ = (d_587_valueOrError0_).Extract()
            return Wrappers.Result_Success(JSON_Grammar.Bracketed_Bracketed(default__.MkStructural(JSON_Grammar.default__.LBRACKET), default__.MkSuffixedSequence(d_590_items_, default__.COMMA, 0), default__.MkStructural(JSON_Grammar.default__.RBRACKET)))

    @staticmethod
    def Value(js):
        source12_ = js
        if source12_.is_Null:
            return Wrappers.Result_Success(JSON_Grammar.Value_Null(JSON_Utils_Views_Core.View__.OfBytes(JSON_Grammar.default__.NULL)))
        elif source12_.is_Bool:
            d_591___mcc_h0_ = source12_.b
            d_592_b_ = d_591___mcc_h0_
            return Wrappers.Result_Success(JSON_Grammar.Value_Bool(default__.Bool(d_592_b_)))
        elif source12_.is_String:
            d_593___mcc_h1_ = source12_.str
            d_594_str_ = d_593___mcc_h1_
            d_595_valueOrError0_ = default__.String(d_594_str_)
            if (d_595_valueOrError0_).IsFailure():
                return (d_595_valueOrError0_).PropagateFailure()
            elif True:
                d_596_s_ = (d_595_valueOrError0_).Extract()
                return Wrappers.Result_Success(JSON_Grammar.Value_String(d_596_s_))
        elif source12_.is_Number:
            d_597___mcc_h2_ = source12_.num
            d_598_dec_ = d_597___mcc_h2_
            d_599_valueOrError1_ = default__.Number(d_598_dec_)
            if (d_599_valueOrError1_).IsFailure():
                return (d_599_valueOrError1_).PropagateFailure()
            elif True:
                d_600_n_ = (d_599_valueOrError1_).Extract()
                return Wrappers.Result_Success(JSON_Grammar.Value_Number(d_600_n_))
        elif source12_.is_Object:
            d_601___mcc_h3_ = source12_.obj
            d_602_obj_ = d_601___mcc_h3_
            d_603_valueOrError2_ = default__.Object(d_602_obj_)
            if (d_603_valueOrError2_).IsFailure():
                return (d_603_valueOrError2_).PropagateFailure()
            elif True:
                d_604_o_ = (d_603_valueOrError2_).Extract()
                return Wrappers.Result_Success(JSON_Grammar.Value_Object(d_604_o_))
        elif True:
            d_605___mcc_h4_ = source12_.arr
            d_606_arr_ = d_605___mcc_h4_
            d_607_valueOrError3_ = default__.Array(d_606_arr_)
            if (d_607_valueOrError3_).IsFailure():
                return (d_607_valueOrError3_).PropagateFailure()
            elif True:
                d_608_a_ = (d_607_valueOrError3_).Extract()
                return Wrappers.Result_Success(JSON_Grammar.Value_Array(d_608_a_))

    @staticmethod
    def JSON(js):
        d_609_valueOrError0_ = default__.Value(js)
        if (d_609_valueOrError0_).IsFailure():
            return (d_609_valueOrError0_).PropagateFailure()
        elif True:
            d_610_val_ = (d_609_valueOrError0_).Extract()
            return Wrappers.Result_Success(default__.MkStructural(d_610_val_))

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
    def _Is(source__):
        d_611_bs_: _dafny.Seq = source__
        return (len(d_611_bs_)) < (BoundedInts.default__.TWO__TO__THE__32)

class string32:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_612_s_: _dafny.Seq = source__
        return (len(d_612_s_)) < (BoundedInts.default__.TWO__TO__THE__32)
