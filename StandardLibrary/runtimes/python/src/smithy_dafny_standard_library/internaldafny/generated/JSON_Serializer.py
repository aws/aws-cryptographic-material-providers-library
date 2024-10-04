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
import smithy_dafny_standard_library.internaldafny.generated.JSON_Spec as JSON_Spec
import smithy_dafny_standard_library.internaldafny.generated.JSON_Grammar as JSON_Grammar
import smithy_dafny_standard_library.internaldafny.generated.JSON_Serializer_ByteStrConversion as JSON_Serializer_ByteStrConversion

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
        d_0_valueOrError0_ = JSON_Spec.default__.EscapeToUTF8(str, 0)
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_1_bs_ = (d_0_valueOrError0_).Extract()
            d_2_valueOrError1_ = default__.CheckLength(d_1_bs_, JSON_Errors.SerializationError_StringTooLong(str))
            if (d_2_valueOrError1_).IsFailure():
                return (d_2_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success(JSON_Grammar.jstring_JString(JSON_Grammar.default__.DOUBLEQUOTE, JSON_Utils_Views_Core.View__.OfBytes(d_1_bs_), JSON_Grammar.default__.DOUBLEQUOTE))

    @staticmethod
    def Sign(n):
        return JSON_Utils_Views_Core.View__.OfBytes((_dafny.Seq([ord('-')]) if (n) < (0) else _dafny.Seq([])))

    @staticmethod
    def Int_k(n):
        return JSON_Serializer_ByteStrConversion.default__.OfInt__any(n, default__.DIGITS, default__.MINUS)

    @staticmethod
    def Int(n):
        d_0_bs_ = default__.Int_k(n)
        d_1_valueOrError0_ = default__.CheckLength(d_0_bs_, JSON_Errors.SerializationError_IntTooLarge(n))
        if (d_1_valueOrError0_).IsFailure():
            return (d_1_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(JSON_Utils_Views_Core.View__.OfBytes(d_0_bs_))

    @staticmethod
    def Number(dec):
        pat_let_tv0_ = dec
        pat_let_tv1_ = dec
        d_0_minus_ = default__.Sign((dec).n)
        d_1_valueOrError0_ = default__.Int(Math.default__.Abs((dec).n))
        if (d_1_valueOrError0_).IsFailure():
            return (d_1_valueOrError0_).PropagateFailure()
        elif True:
            d_2_num_ = (d_1_valueOrError0_).Extract()
            d_3_frac_ = JSON_Grammar.Maybe_Empty()
            def iife0_(_pat_let6_0):
                def iife1_(d_5_e_):
                    def iife2_(_pat_let7_0):
                        def iife3_(d_6_sign_):
                            def iife4_(_pat_let8_0):
                                def iife5_(d_7_valueOrError2_):
                                    def iife6_(_pat_let9_0):
                                        def iife7_(d_8_num_):
                                            return Wrappers.Result_Success(JSON_Grammar.Maybe_NonEmpty(JSON_Grammar.jexp_JExp(d_5_e_, d_6_sign_, d_8_num_)))
                                        return iife7_(_pat_let9_0)
                                    return ((d_7_valueOrError2_).PropagateFailure() if (d_7_valueOrError2_).IsFailure() else iife6_((d_7_valueOrError2_).Extract()))
                                return iife5_(_pat_let8_0)
                            return iife4_(default__.Int(Math.default__.Abs((pat_let_tv1_).e10)))
                        return iife3_(_pat_let7_0)
                    return iife2_(default__.Sign((pat_let_tv0_).e10))
                return iife1_(_pat_let6_0)
            d_4_valueOrError1_ = (Wrappers.Result_Success(JSON_Grammar.Maybe_Empty()) if ((dec).e10) == (0) else iife0_(JSON_Utils_Views_Core.View__.OfBytes(_dafny.Seq([ord('e')]))))
            if (d_4_valueOrError1_).IsFailure():
                return (d_4_valueOrError1_).PropagateFailure()
            elif True:
                d_9_exp_ = (d_4_valueOrError1_).Extract()
                return Wrappers.Result_Success(JSON_Grammar.jnumber_JNumber(d_0_minus_, d_2_num_, JSON_Grammar.Maybe_Empty(), d_9_exp_))

    @staticmethod
    def MkStructural(v):
        return JSON_Grammar.Structural_Structural(JSON_Grammar.default__.EMPTY, v, JSON_Grammar.default__.EMPTY)

    @staticmethod
    def KeyValue(kv):
        d_0_valueOrError0_ = default__.String((kv)[0])
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_1_k_ = (d_0_valueOrError0_).Extract()
            d_2_valueOrError1_ = default__.Value((kv)[1])
            if (d_2_valueOrError1_).IsFailure():
                return (d_2_valueOrError1_).PropagateFailure()
            elif True:
                d_3_v_ = (d_2_valueOrError1_).Extract()
                return Wrappers.Result_Success(JSON_Grammar.jKeyValue_KeyValue(d_1_k_, default__.COLON, d_3_v_))

    @staticmethod
    def MkSuffixedSequence(ds, suffix, start):
        d_0___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (start) >= (len(ds)):
                    return (d_0___accumulator_) + (_dafny.Seq([]))
                elif (start) == ((len(ds)) - (1)):
                    return (d_0___accumulator_) + (_dafny.Seq([JSON_Grammar.Suffixed_Suffixed((ds)[start], JSON_Grammar.Maybe_Empty())]))
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + (_dafny.Seq([JSON_Grammar.Suffixed_Suffixed((ds)[start], JSON_Grammar.Maybe_NonEmpty(suffix))]))
                    in0_ = ds
                    in1_ = suffix
                    in2_ = (start) + (1)
                    ds = in0_
                    suffix = in1_
                    start = in2_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def Object(obj):
        def lambda0_(d_1_obj_):
            def lambda1_(d_2_v_):
                return default__.KeyValue(d_2_v_)

            return lambda1_

        d_0_valueOrError0_ = Seq.default__.MapWithResult(lambda0_(obj), obj)
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_3_items_ = (d_0_valueOrError0_).Extract()
            return Wrappers.Result_Success(JSON_Grammar.Bracketed_Bracketed(default__.MkStructural(JSON_Grammar.default__.LBRACE), default__.MkSuffixedSequence(d_3_items_, default__.COMMA, 0), default__.MkStructural(JSON_Grammar.default__.RBRACE)))

    @staticmethod
    def Array(arr):
        def lambda0_(d_1_arr_):
            def lambda1_(d_2_v_):
                return default__.Value(d_2_v_)

            return lambda1_

        d_0_valueOrError0_ = Seq.default__.MapWithResult(lambda0_(arr), arr)
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_3_items_ = (d_0_valueOrError0_).Extract()
            return Wrappers.Result_Success(JSON_Grammar.Bracketed_Bracketed(default__.MkStructural(JSON_Grammar.default__.LBRACKET), default__.MkSuffixedSequence(d_3_items_, default__.COMMA, 0), default__.MkStructural(JSON_Grammar.default__.RBRACKET)))

    @staticmethod
    def Value(js):
        source0_ = js
        if True:
            if source0_.is_Null:
                return Wrappers.Result_Success(JSON_Grammar.Value_Null(JSON_Utils_Views_Core.View__.OfBytes(JSON_Grammar.default__.NULL)))
        if True:
            if source0_.is_Bool:
                d_0_b_ = source0_.b
                return Wrappers.Result_Success(JSON_Grammar.Value_Bool(default__.Bool(d_0_b_)))
        if True:
            if source0_.is_String:
                d_1_str_ = source0_.str
                d_2_valueOrError0_ = default__.String(d_1_str_)
                if (d_2_valueOrError0_).IsFailure():
                    return (d_2_valueOrError0_).PropagateFailure()
                elif True:
                    d_3_s_ = (d_2_valueOrError0_).Extract()
                    return Wrappers.Result_Success(JSON_Grammar.Value_String(d_3_s_))
        if True:
            if source0_.is_Number:
                d_4_dec_ = source0_.num
                d_5_valueOrError1_ = default__.Number(d_4_dec_)
                if (d_5_valueOrError1_).IsFailure():
                    return (d_5_valueOrError1_).PropagateFailure()
                elif True:
                    d_6_n_ = (d_5_valueOrError1_).Extract()
                    return Wrappers.Result_Success(JSON_Grammar.Value_Number(d_6_n_))
        if True:
            if source0_.is_Object:
                d_7_obj_ = source0_.obj
                d_8_valueOrError2_ = default__.Object(d_7_obj_)
                if (d_8_valueOrError2_).IsFailure():
                    return (d_8_valueOrError2_).PropagateFailure()
                elif True:
                    d_9_o_ = (d_8_valueOrError2_).Extract()
                    return Wrappers.Result_Success(JSON_Grammar.Value_Object(d_9_o_))
        if True:
            d_10_arr_ = source0_.arr
            d_11_valueOrError3_ = default__.Array(d_10_arr_)
            if (d_11_valueOrError3_).IsFailure():
                return (d_11_valueOrError3_).PropagateFailure()
            elif True:
                d_12_a_ = (d_11_valueOrError3_).Extract()
                return Wrappers.Result_Success(JSON_Grammar.Value_Array(d_12_a_))

    @staticmethod
    def JSON(js):
        d_0_valueOrError0_ = default__.Value(js)
        if (d_0_valueOrError0_).IsFailure():
            return (d_0_valueOrError0_).PropagateFailure()
        elif True:
            d_1_val_ = (d_0_valueOrError0_).Extract()
            return Wrappers.Result_Success(default__.MkStructural(d_1_val_))

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
        d_0_bs_: _dafny.Seq = source__
        return (len(d_0_bs_)) < (BoundedInts.default__.TWO__TO__THE__32)

class string32:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_1_s_: _dafny.Seq = source__
        return (len(d_1_s_)) < (BoundedInts.default__.TWO__TO__THE__32)
