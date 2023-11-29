import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_mMergeSort
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
import StandardLibrary_mUInt
import String
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
import DafnyLibraries
import JSON_mUtils_mViews_mCore
import JSON_mUtils_mViews_mWriters
import JSON_mUtils_mViews
import JSON_mUtils_mLexers_mCore
import JSON_mUtils_mLexers_mStrings
import JSON_mUtils_mLexers
import JSON_mUtils_mCursors
import JSON_mUtils_mParsers
import JSON_mUtils_mStr_mCharStrConversion
import JSON_mUtils_mStr_mCharStrEscaping
import JSON_mUtils_mStr
import JSON_mUtils_mSeq
import JSON_mUtils_mVectors
import JSON_mUtils
import JSON_mErrors
import JSON_mValues
import JSON_mSpec
import JSON_mGrammar
import JSON_mSerializer_mByteStrConversion
import JSON_mSerializer
import JSON_mDeserializer_mUint16StrConversion
import JSON_mDeserializer_mByteStrConversion

# Module: JSON_mDeserializer

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Bool(js):
        return ((js).At(0)) == (ord('t'))

    @staticmethod
    def UnsupportedEscape16(code):
        return JSON_mErrors.DeserializationError_UnsupportedEscape((UnicodeStrings.default__.FromUTF16Checked(code)).UnwrapOr(_dafny.Seq("Couldn't decode UTF-16")))

    @staticmethod
    def ToNat16(str):
        d_512_hd_ = JSON_mDeserializer_mUint16StrConversion.default__.ToNat__any(str, 16, default__.HEX__TABLE__16)
        return d_512_hd_

    @staticmethod
    def Unescape(str, start, prefix):
        while True:
            with _dafny.label():
                if (start) >= (len(str)):
                    return Wrappers.Result_Success(prefix)
                elif ((str)[start]) == (ord('\\')):
                    if (len(str)) == ((start) + (1)):
                        return Wrappers.Result_Failure(JSON_mErrors.DeserializationError_EscapeAtEOS())
                    elif True:
                        d_513_c_ = (str)[(start) + (1)]
                        if (d_513_c_) == (ord('u')):
                            if (len(str)) <= ((start) + (6)):
                                return Wrappers.Result_Failure(JSON_mErrors.DeserializationError_EscapeAtEOS())
                            elif True:
                                d_514_code_ = _dafny.Seq((str)[(start) + (2):(start) + (6):])
                                def lambda37_(exists_var_1_):
                                    d_515_c_: int = exists_var_1_
                                    return ((d_515_c_) in (d_514_code_)) and ((d_515_c_) not in (default__.HEX__TABLE__16))

                                if _dafny.quantifier((d_514_code_).UniqueElements, False, lambda37_):
                                    return Wrappers.Result_Failure(default__.UnsupportedEscape16(d_514_code_))
                                elif True:
                                    d_516_hd_ = default__.ToNat16(d_514_code_)
                                    in112_ = str
                                    in113_ = (start) + (6)
                                    in114_ = (prefix) + (_dafny.Seq([d_516_hd_]))
                                    str = in112_
                                    start = in113_
                                    prefix = in114_
                                    raise _dafny.TailCall()
                        elif True:
                            d_517_unescaped_ = (34 if (d_513_c_) == (34) else (92 if (d_513_c_) == (92) else (8 if (d_513_c_) == (98) else (12 if (d_513_c_) == (102) else (10 if (d_513_c_) == (110) else (13 if (d_513_c_) == (114) else (9 if (d_513_c_) == (116) else 0)))))))
                            if (d_517_unescaped_) == (0):
                                return Wrappers.Result_Failure(default__.UnsupportedEscape16(_dafny.Seq((str)[start:(start) + (2):])))
                            elif True:
                                in115_ = str
                                in116_ = (start) + (2)
                                in117_ = (prefix) + (_dafny.Seq([d_517_unescaped_]))
                                str = in115_
                                start = in116_
                                prefix = in117_
                                raise _dafny.TailCall()
                elif True:
                    in118_ = str
                    in119_ = (start) + (1)
                    in120_ = (prefix) + (_dafny.Seq([(str)[start]]))
                    str = in118_
                    start = in119_
                    prefix = in120_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def String(js):
        d_518_valueOrError0_ = (UnicodeStrings.default__.FromUTF8Checked(((js).contents).Bytes())).ToResult_k(JSON_mErrors.DeserializationError_InvalidUnicode())
        if (d_518_valueOrError0_).IsFailure():
            return (d_518_valueOrError0_).PropagateFailure()
        elif True:
            d_519_asUtf32_ = (d_518_valueOrError0_).Extract()
            d_520_valueOrError1_ = (UnicodeStrings.default__.ToUTF16Checked(d_519_asUtf32_)).ToResult_k(JSON_mErrors.DeserializationError_InvalidUnicode())
            if (d_520_valueOrError1_).IsFailure():
                return (d_520_valueOrError1_).PropagateFailure()
            elif True:
                d_521_asUint16_ = (d_520_valueOrError1_).Extract()
                d_522_valueOrError2_ = default__.Unescape(d_521_asUint16_, 0, _dafny.Seq([]))
                if (d_522_valueOrError2_).IsFailure():
                    return (d_522_valueOrError2_).PropagateFailure()
                elif True:
                    d_523_unescaped_ = (d_522_valueOrError2_).Extract()
                    return (UnicodeStrings.default__.FromUTF16Checked(d_523_unescaped_)).ToResult_k(JSON_mErrors.DeserializationError_InvalidUnicode())

    @staticmethod
    def ToInt(sign, n):
        d_524_n_ = JSON_mDeserializer_mByteStrConversion.default__.ToNat__any((n).Bytes(), 10, default__.DIGITS)
        return Wrappers.Result_Success(((0) - (d_524_n_) if (sign).Char_q('-') else d_524_n_))

    @staticmethod
    def Number(js):
        let_tmp_rhs1_ = js
        d_525_minus_ = let_tmp_rhs1_.minus
        d_526_num_ = let_tmp_rhs1_.num
        d_527_frac_ = let_tmp_rhs1_.frac
        d_528_exp_ = let_tmp_rhs1_.exp
        d_529_valueOrError0_ = default__.ToInt(d_525_minus_, d_526_num_)
        if (d_529_valueOrError0_).IsFailure():
            return (d_529_valueOrError0_).PropagateFailure()
        elif True:
            d_530_n_ = (d_529_valueOrError0_).Extract()
            def lambda38_(source13_):
                if source13_.is_Empty:
                    return Wrappers.Result_Success(0)
                elif True:
                    d_532___mcc_h0_ = source13_.t
                    def lambda39_(source14_):
                        d_533___mcc_h1_ = source14_.e
                        d_534___mcc_h2_ = source14_.sign
                        d_535___mcc_h3_ = source14_.num
                        def iife12_(_pat_let6_0):
                            def iife13_(d_536_num_):
                                def iife14_(_pat_let7_0):
                                    def iife15_(d_537_sign_):
                                        return default__.ToInt(d_537_sign_, d_536_num_)
                                    return iife15_(_pat_let7_0)
                                return iife14_(d_534___mcc_h2_)
                            return iife13_(_pat_let6_0)
                        return iife12_(d_535___mcc_h3_)

                    return lambda39_(d_532___mcc_h0_)

            d_531_valueOrError1_ = lambda38_(d_528_exp_)
            if (d_531_valueOrError1_).IsFailure():
                return (d_531_valueOrError1_).PropagateFailure()
            elif True:
                d_538_e10_ = (d_531_valueOrError1_).Extract()
                source15_ = d_527_frac_
                if source15_.is_Empty:
                    return Wrappers.Result_Success(JSON_mValues.Decimal_Decimal(d_530_n_, d_538_e10_))
                elif True:
                    d_539___mcc_h4_ = source15_.t
                    source16_ = d_539___mcc_h4_
                    d_540___mcc_h5_ = source16_.period
                    d_541___mcc_h6_ = source16_.num
                    d_542_num_ = d_541___mcc_h6_
                    d_543_pow10_ = (d_542_num_).Length()
                    d_544_valueOrError2_ = default__.ToInt(d_525_minus_, d_542_num_)
                    if (d_544_valueOrError2_).IsFailure():
                        return (d_544_valueOrError2_).PropagateFailure()
                    elif True:
                        d_545_frac_ = (d_544_valueOrError2_).Extract()
                        return Wrappers.Result_Success(JSON_mValues.Decimal_Decimal(((d_530_n_) * (Power.default__.Pow(10, d_543_pow10_))) + (d_545_frac_), (d_538_e10_) - (d_543_pow10_)))

    @staticmethod
    def KeyValue(js):
        d_546_valueOrError0_ = default__.String((js).k)
        if (d_546_valueOrError0_).IsFailure():
            return (d_546_valueOrError0_).PropagateFailure()
        elif True:
            d_547_k_ = (d_546_valueOrError0_).Extract()
            d_548_valueOrError1_ = default__.Value((js).v)
            if (d_548_valueOrError1_).IsFailure():
                return (d_548_valueOrError1_).PropagateFailure()
            elif True:
                d_549_v_ = (d_548_valueOrError1_).Extract()
                return Wrappers.Result_Success((d_547_k_, d_549_v_))

    @staticmethod
    def Object(js):
        def lambda40_(d_550_js_):
            def lambda41_(d_551_d_):
                return default__.KeyValue((d_551_d_).t)

            return lambda41_

        return Seq.default__.MapWithResult(lambda40_(js), (js).data)

    @staticmethod
    def Array(js):
        def lambda42_(d_552_js_):
            def lambda43_(d_553_d_):
                return default__.Value((d_553_d_).t)

            return lambda43_

        return Seq.default__.MapWithResult(lambda42_(js), (js).data)

    @staticmethod
    def Value(js):
        source17_ = js
        if source17_.is_Null:
            d_554___mcc_h0_ = source17_.n
            return Wrappers.Result_Success(JSON_mValues.JSON_Null())
        elif source17_.is_Bool:
            d_555___mcc_h1_ = source17_.b
            d_556_b_ = d_555___mcc_h1_
            return Wrappers.Result_Success(JSON_mValues.JSON_Bool(default__.Bool(d_556_b_)))
        elif source17_.is_String:
            d_557___mcc_h2_ = source17_.str
            d_558_str_ = d_557___mcc_h2_
            d_559_valueOrError0_ = default__.String(d_558_str_)
            if (d_559_valueOrError0_).IsFailure():
                return (d_559_valueOrError0_).PropagateFailure()
            elif True:
                d_560_s_ = (d_559_valueOrError0_).Extract()
                return Wrappers.Result_Success(JSON_mValues.JSON_String(d_560_s_))
        elif source17_.is_Number:
            d_561___mcc_h3_ = source17_.num
            d_562_dec_ = d_561___mcc_h3_
            d_563_valueOrError1_ = default__.Number(d_562_dec_)
            if (d_563_valueOrError1_).IsFailure():
                return (d_563_valueOrError1_).PropagateFailure()
            elif True:
                d_564_n_ = (d_563_valueOrError1_).Extract()
                return Wrappers.Result_Success(JSON_mValues.JSON_Number(d_564_n_))
        elif source17_.is_Object:
            d_565___mcc_h4_ = source17_.obj
            d_566_obj_ = d_565___mcc_h4_
            d_567_valueOrError2_ = default__.Object(d_566_obj_)
            if (d_567_valueOrError2_).IsFailure():
                return (d_567_valueOrError2_).PropagateFailure()
            elif True:
                d_568_o_ = (d_567_valueOrError2_).Extract()
                return Wrappers.Result_Success(JSON_mValues.JSON_Object(d_568_o_))
        elif True:
            d_569___mcc_h5_ = source17_.arr
            d_570_arr_ = d_569___mcc_h5_
            d_571_valueOrError3_ = default__.Array(d_570_arr_)
            if (d_571_valueOrError3_).IsFailure():
                return (d_571_valueOrError3_).PropagateFailure()
            elif True:
                d_572_a_ = (d_571_valueOrError3_).Extract()
                return Wrappers.Result_Success(JSON_mValues.JSON_Array(d_572_a_))

    @staticmethod
    def JSON(js):
        return default__.Value((js).t)

    @_dafny.classproperty
    def HEX__TABLE__16(instance):
        return _dafny.Map({ord('0'): 0, ord('1'): 1, ord('2'): 2, ord('3'): 3, ord('4'): 4, ord('5'): 5, ord('6'): 6, ord('7'): 7, ord('8'): 8, ord('9'): 9, ord('a'): 10, ord('b'): 11, ord('c'): 12, ord('d'): 13, ord('e'): 14, ord('f'): 15, ord('A'): 10, ord('B'): 11, ord('C'): 12, ord('D'): 13, ord('E'): 14, ord('F'): 15})
    @_dafny.classproperty
    def DIGITS(instance):
        return _dafny.Map({ord('0'): 0, ord('1'): 1, ord('2'): 2, ord('3'): 3, ord('4'): 4, ord('5'): 5, ord('6'): 6, ord('7'): 7, ord('8'): 8, ord('9'): 9})
    @_dafny.classproperty
    def MINUS(instance):
        return ord('-')
