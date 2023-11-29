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
import JSON_mDeserializer
import JSON_mConcreteSyntax_mSpec
import JSON_mConcreteSyntax_mSpecProperties
import JSON_mConcreteSyntax
import JSON_mZeroCopy_mSerializer
import JSON_mZeroCopy_mDeserializer_mCore
import JSON_mZeroCopy_mDeserializer_mStrings
import JSON_mZeroCopy_mDeserializer_mNumbers
import JSON_mZeroCopy_mDeserializer_mObjectParams
import JSON_mZeroCopy_mDeserializer_mObjects
import JSON_mZeroCopy_mDeserializer_mArrayParams
import JSON_mZeroCopy_mDeserializer_mArrays
import JSON_mZeroCopy_mDeserializer_mConstants

# assert "JSON_mZeroCopy_mDeserializer_mValues" == __name__
JSON_mZeroCopy_mDeserializer_mValues = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Value(cs):
        d_758_c_ = (cs).Peek()
        if (d_758_c_) == (ord('{')):
            d_759_valueOrError0_ = JSON_mZeroCopy_mDeserializer_mObjects.default__.Object(cs, JSON_mZeroCopy_mDeserializer_mValues.default__.ValueParser(cs))
            if (d_759_valueOrError0_).IsFailure():
                return (d_759_valueOrError0_).PropagateFailure()
            elif True:
                let_tmp_rhs16_ = (d_759_valueOrError0_).Extract()
                d_760_obj_ = let_tmp_rhs16_.t
                d_761_cs_k_ = let_tmp_rhs16_.cs
                d_762_v_ = JSON_mGrammar.Value_Object(d_760_obj_)
                d_763_sp_ = JSON_mUtils_mCursors.Split_SP(d_762_v_, d_761_cs_k_)
                return Wrappers.Result_Success(d_763_sp_)
        elif (d_758_c_) == (ord('[')):
            d_764_valueOrError1_ = JSON_mZeroCopy_mDeserializer_mArrays.default__.Array(cs, JSON_mZeroCopy_mDeserializer_mValues.default__.ValueParser(cs))
            if (d_764_valueOrError1_).IsFailure():
                return (d_764_valueOrError1_).PropagateFailure()
            elif True:
                let_tmp_rhs17_ = (d_764_valueOrError1_).Extract()
                d_765_arr_ = let_tmp_rhs17_.t
                d_766_cs_k_ = let_tmp_rhs17_.cs
                d_767_v_ = JSON_mGrammar.Value_Array(d_765_arr_)
                d_768_sp_ = JSON_mUtils_mCursors.Split_SP(d_767_v_, d_766_cs_k_)
                return Wrappers.Result_Success(d_768_sp_)
        elif (d_758_c_) == (ord('\"')):
            d_769_valueOrError2_ = JSON_mZeroCopy_mDeserializer_mStrings.default__.String(cs)
            if (d_769_valueOrError2_).IsFailure():
                return (d_769_valueOrError2_).PropagateFailure()
            elif True:
                let_tmp_rhs18_ = (d_769_valueOrError2_).Extract()
                d_770_str_ = let_tmp_rhs18_.t
                d_771_cs_ = let_tmp_rhs18_.cs
                return Wrappers.Result_Success(JSON_mUtils_mCursors.Split_SP(JSON_mGrammar.Value_String(d_770_str_), d_771_cs_))
        elif (d_758_c_) == (ord('t')):
            d_772_valueOrError3_ = JSON_mZeroCopy_mDeserializer_mConstants.default__.Constant(cs, (JSON_mGrammar.default__).TRUE)
            if (d_772_valueOrError3_).IsFailure():
                return (d_772_valueOrError3_).PropagateFailure()
            elif True:
                let_tmp_rhs19_ = (d_772_valueOrError3_).Extract()
                d_773_cst_ = let_tmp_rhs19_.t
                d_774_cs_ = let_tmp_rhs19_.cs
                return Wrappers.Result_Success(JSON_mUtils_mCursors.Split_SP(JSON_mGrammar.Value_Bool(d_773_cst_), d_774_cs_))
        elif (d_758_c_) == (ord('f')):
            d_775_valueOrError4_ = JSON_mZeroCopy_mDeserializer_mConstants.default__.Constant(cs, (JSON_mGrammar.default__).FALSE)
            if (d_775_valueOrError4_).IsFailure():
                return (d_775_valueOrError4_).PropagateFailure()
            elif True:
                let_tmp_rhs20_ = (d_775_valueOrError4_).Extract()
                d_776_cst_ = let_tmp_rhs20_.t
                d_777_cs_ = let_tmp_rhs20_.cs
                return Wrappers.Result_Success(JSON_mUtils_mCursors.Split_SP(JSON_mGrammar.Value_Bool(d_776_cst_), d_777_cs_))
        elif (d_758_c_) == (ord('n')):
            d_778_valueOrError5_ = JSON_mZeroCopy_mDeserializer_mConstants.default__.Constant(cs, (JSON_mGrammar.default__).NULL)
            if (d_778_valueOrError5_).IsFailure():
                return (d_778_valueOrError5_).PropagateFailure()
            elif True:
                let_tmp_rhs21_ = (d_778_valueOrError5_).Extract()
                d_779_cst_ = let_tmp_rhs21_.t
                d_780_cs_ = let_tmp_rhs21_.cs
                return Wrappers.Result_Success(JSON_mUtils_mCursors.Split_SP(JSON_mGrammar.Value_Null(d_779_cst_), d_780_cs_))
        elif True:
            d_781_valueOrError6_ = JSON_mZeroCopy_mDeserializer_mNumbers.default__.Number(cs)
            if (d_781_valueOrError6_).IsFailure():
                return (d_781_valueOrError6_).PropagateFailure()
            elif True:
                let_tmp_rhs22_ = (d_781_valueOrError6_).Extract()
                d_782_num_ = let_tmp_rhs22_.t
                d_783_cs_k_ = let_tmp_rhs22_.cs
                d_784_v_ = JSON_mGrammar.Value_Number(d_782_num_)
                d_785_sp_ = JSON_mUtils_mCursors.Split_SP(d_784_v_, d_783_cs_k_)
                return Wrappers.Result_Success(d_785_sp_)

    @staticmethod
    def ValueParser(cs):
        def lambda56_(d_787_cs_):
            def lambda57_(d_788_ps_k_):
                return ((d_788_ps_k_).Length()) < ((d_787_cs_).Length())

            return lambda57_

        d_786_pre_ = lambda56_(cs)
        def lambda58_(d_790_pre_):
            def lambda59_(d_791_ps_k_):
                return JSON_mZeroCopy_mDeserializer_mValues.default__.Value(d_791_ps_k_)

            return lambda59_

        d_789_fn_ = lambda58_(d_786_pre_)
        return JSON_mUtils_mParsers.SubParser___SubParser(d_789_fn_)

