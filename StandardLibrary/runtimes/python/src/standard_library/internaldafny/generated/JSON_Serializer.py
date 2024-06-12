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
        d_534_valueOrError0_ = JSON_Spec.default__.EscapeToUTF8(str, 0)
        if (d_534_valueOrError0_).IsFailure():
            return (d_534_valueOrError0_).PropagateFailure()
        elif True:
            d_535_bs_ = (d_534_valueOrError0_).Extract()
            d_536_valueOrError1_ = default__.CheckLength(d_535_bs_, JSON_Errors.SerializationError_StringTooLong(str))
            if (d_536_valueOrError1_).IsFailure():
                return (d_536_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success(JSON_Grammar.jstring_JString(JSON_Grammar.default__.DOUBLEQUOTE, JSON_Utils_Views_Core.View__.OfBytes(d_535_bs_), JSON_Grammar.default__.DOUBLEQUOTE))

    @staticmethod
    def Sign(n):
        return JSON_Utils_Views_Core.View__.OfBytes((_dafny.Seq([ord('-')]) if (n) < (0) else _dafny.Seq([])))

    @staticmethod
    def Int_k(n):
        return JSON_Serializer_ByteStrConversion.default__.OfInt__any(n, default__.DIGITS, default__.MINUS)

    @staticmethod
    def Int(n):
        d_537_bs_ = default__.Int_k(n)
        d_538_valueOrError0_ = default__.CheckLength(d_537_bs_, JSON_Errors.SerializationError_IntTooLarge(n))
        if (d_538_valueOrError0_).IsFailure():
            return (d_538_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(JSON_Utils_Views_Core.View__.OfBytes(d_537_bs_))

    @staticmethod
    def Number(dec):
        pat_let_tv14_ = dec
        pat_let_tv15_ = dec
        d_539_minus_ = default__.Sign((dec).n)
        d_540_valueOrError0_ = default__.Int(Math.default__.Abs((dec).n))
        if (d_540_valueOrError0_).IsFailure():
            return (d_540_valueOrError0_).PropagateFailure()
        elif True:
            d_541_num_ = (d_540_valueOrError0_).Extract()
            d_542_frac_ = JSON_Grammar.Maybe_Empty()
            def iife12_(_pat_let6_0):
                def iife13_(d_544_e_):
                    def iife14_(_pat_let7_0):
                        def iife15_(d_545_sign_):
                            def iife16_(_pat_let8_0):
                                def iife17_(d_546_valueOrError2_):
                                    def iife18_(_pat_let9_0):
                                        def iife19_(d_547_num_):
                                            return Wrappers.Result_Success(JSON_Grammar.Maybe_NonEmpty(JSON_Grammar.jexp_JExp(d_544_e_, d_545_sign_, d_547_num_)))
                                        return iife19_(_pat_let9_0)
                                    return ((d_546_valueOrError2_).PropagateFailure() if (d_546_valueOrError2_).IsFailure() else iife18_((d_546_valueOrError2_).Extract()))
                                return iife17_(_pat_let8_0)
                            return iife16_(default__.Int(Math.default__.Abs((pat_let_tv15_).e10)))
                        return iife15_(_pat_let7_0)
                    return iife14_(default__.Sign((pat_let_tv14_).e10))
                return iife13_(_pat_let6_0)
            d_543_valueOrError1_ = (Wrappers.Result_Success(JSON_Grammar.Maybe_Empty()) if ((dec).e10) == (0) else iife12_(JSON_Utils_Views_Core.View__.OfBytes(_dafny.Seq([ord('e')]))))
            if (d_543_valueOrError1_).IsFailure():
                return (d_543_valueOrError1_).PropagateFailure()
            elif True:
                d_548_exp_ = (d_543_valueOrError1_).Extract()
                return Wrappers.Result_Success(JSON_Grammar.jnumber_JNumber(d_539_minus_, d_541_num_, JSON_Grammar.Maybe_Empty(), d_548_exp_))

    @staticmethod
    def MkStructural(v):
        return JSON_Grammar.Structural_Structural(JSON_Grammar.default__.EMPTY, v, JSON_Grammar.default__.EMPTY)

    @staticmethod
    def KeyValue(kv):
        d_549_valueOrError0_ = default__.String((kv)[0])
        if (d_549_valueOrError0_).IsFailure():
            return (d_549_valueOrError0_).PropagateFailure()
        elif True:
            d_550_k_ = (d_549_valueOrError0_).Extract()
            d_551_valueOrError1_ = default__.Value((kv)[1])
            if (d_551_valueOrError1_).IsFailure():
                return (d_551_valueOrError1_).PropagateFailure()
            elif True:
                d_552_v_ = (d_551_valueOrError1_).Extract()
                return Wrappers.Result_Success(JSON_Grammar.jKeyValue_KeyValue(d_550_k_, default__.COLON, d_552_v_))

    @staticmethod
    def MkSuffixedSequence(ds, suffix, start):
        d_553___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (start) >= (len(ds)):
                    return (d_553___accumulator_) + (_dafny.Seq([]))
                elif (start) == ((len(ds)) - (1)):
                    return (d_553___accumulator_) + (_dafny.Seq([JSON_Grammar.Suffixed_Suffixed((ds)[start], JSON_Grammar.Maybe_Empty())]))
                elif True:
                    d_553___accumulator_ = (d_553___accumulator_) + (_dafny.Seq([JSON_Grammar.Suffixed_Suffixed((ds)[start], JSON_Grammar.Maybe_NonEmpty(suffix))]))
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
        def lambda35_(d_555_obj_):
            def lambda36_(d_556_v_):
                return default__.KeyValue(d_556_v_)

            return lambda36_

        d_554_valueOrError0_ = Seq.default__.MapWithResult(lambda35_(obj), obj)
        if (d_554_valueOrError0_).IsFailure():
            return (d_554_valueOrError0_).PropagateFailure()
        elif True:
            d_557_items_ = (d_554_valueOrError0_).Extract()
            return Wrappers.Result_Success(JSON_Grammar.Bracketed_Bracketed(default__.MkStructural(JSON_Grammar.default__.LBRACE), default__.MkSuffixedSequence(d_557_items_, default__.COMMA, 0), default__.MkStructural(JSON_Grammar.default__.RBRACE)))

    @staticmethod
    def Array(arr):
        def lambda37_(d_559_arr_):
            def lambda38_(d_560_v_):
                return default__.Value(d_560_v_)

            return lambda38_

        d_558_valueOrError0_ = Seq.default__.MapWithResult(lambda37_(arr), arr)
        if (d_558_valueOrError0_).IsFailure():
            return (d_558_valueOrError0_).PropagateFailure()
        elif True:
            d_561_items_ = (d_558_valueOrError0_).Extract()
            return Wrappers.Result_Success(JSON_Grammar.Bracketed_Bracketed(default__.MkStructural(JSON_Grammar.default__.LBRACKET), default__.MkSuffixedSequence(d_561_items_, default__.COMMA, 0), default__.MkStructural(JSON_Grammar.default__.RBRACKET)))

    @staticmethod
    def Value(js):
        source13_ = js
        unmatched13 = True
        if unmatched13:
            if source13_.is_Null:
                unmatched13 = False
                return Wrappers.Result_Success(JSON_Grammar.Value_Null(JSON_Utils_Views_Core.View__.OfBytes(JSON_Grammar.default__.NULL)))
        if unmatched13:
            if source13_.is_Bool:
                d_562_b_ = source13_.b
                unmatched13 = False
                return Wrappers.Result_Success(JSON_Grammar.Value_Bool(default__.Bool(d_562_b_)))
        if unmatched13:
            if source13_.is_String:
                d_563_str_ = source13_.str
                unmatched13 = False
                d_564_valueOrError0_ = default__.String(d_563_str_)
                if (d_564_valueOrError0_).IsFailure():
                    return (d_564_valueOrError0_).PropagateFailure()
                elif True:
                    d_565_s_ = (d_564_valueOrError0_).Extract()
                    return Wrappers.Result_Success(JSON_Grammar.Value_String(d_565_s_))
        if unmatched13:
            if source13_.is_Number:
                d_566_dec_ = source13_.num
                unmatched13 = False
                d_567_valueOrError1_ = default__.Number(d_566_dec_)
                if (d_567_valueOrError1_).IsFailure():
                    return (d_567_valueOrError1_).PropagateFailure()
                elif True:
                    d_568_n_ = (d_567_valueOrError1_).Extract()
                    return Wrappers.Result_Success(JSON_Grammar.Value_Number(d_568_n_))
        if unmatched13:
            if source13_.is_Object:
                d_569_obj_ = source13_.obj
                unmatched13 = False
                d_570_valueOrError2_ = default__.Object(d_569_obj_)
                if (d_570_valueOrError2_).IsFailure():
                    return (d_570_valueOrError2_).PropagateFailure()
                elif True:
                    d_571_o_ = (d_570_valueOrError2_).Extract()
                    return Wrappers.Result_Success(JSON_Grammar.Value_Object(d_571_o_))
        if unmatched13:
            d_572_arr_ = source13_.arr
            unmatched13 = False
            d_573_valueOrError3_ = default__.Array(d_572_arr_)
            if (d_573_valueOrError3_).IsFailure():
                return (d_573_valueOrError3_).PropagateFailure()
            elif True:
                d_574_a_ = (d_573_valueOrError3_).Extract()
                return Wrappers.Result_Success(JSON_Grammar.Value_Array(d_574_a_))
        raise Exception("unexpected control point")

    @staticmethod
    def JSON(js):
        d_575_valueOrError0_ = default__.Value(js)
        if (d_575_valueOrError0_).IsFailure():
            return (d_575_valueOrError0_).PropagateFailure()
        elif True:
            d_576_val_ = (d_575_valueOrError0_).Extract()
            return Wrappers.Result_Success(default__.MkStructural(d_576_val_))

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
        d_577_bs_: _dafny.Seq = source__
        return (len(d_577_bs_)) < (BoundedInts.default__.TWO__TO__THE__32)

class string32:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq("")
    def _Is(source__):
        d_578_s_: _dafny.Seq = source__
        return (len(d_578_s_)) < (BoundedInts.default__.TWO__TO__THE__32)
