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
import JSON_mZeroCopy_mDeserializer_mValues

# assert "JSON_mZeroCopy_mDeserializer_mAPI" == __name__
JSON_mZeroCopy_mDeserializer_mAPI = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def LiftCursorError(err):
        source20_ = err
        if source20_.is_EOF:
            return JSON_mErrors.DeserializationError_ReachedEOF()
        elif source20_.is_ExpectingByte:
            d_792___mcc_h0_ = source20_.expected
            d_793___mcc_h1_ = source20_.b
            d_794_b_ = d_793___mcc_h1_
            d_795_expected_ = d_792___mcc_h0_
            return JSON_mErrors.DeserializationError_ExpectingByte(d_795_expected_, d_794_b_)
        elif source20_.is_ExpectingAnyByte:
            d_796___mcc_h2_ = source20_.expected__sq
            d_797___mcc_h3_ = source20_.b
            d_798_b_ = d_797___mcc_h3_
            d_799_expected__sq_ = d_796___mcc_h2_
            return JSON_mErrors.DeserializationError_ExpectingAnyByte(d_799_expected__sq_, d_798_b_)
        elif True:
            d_800___mcc_h4_ = source20_.err
            d_801_err_ = d_800___mcc_h4_
            return d_801_err_

    @staticmethod
    def JSON(cs):
        return (JSON_mZeroCopy_mDeserializer_mCore.default__.Structural(cs, JSON_mUtils_mParsers.Parser___Parser(JSON_mZeroCopy_mDeserializer_mValues.default__.Value))).MapFailure(JSON_mZeroCopy_mDeserializer_mAPI.default__.LiftCursorError)

    @staticmethod
    def Text(v):
        d_802_valueOrError0_ = JSON_mZeroCopy_mDeserializer_mAPI.default__.JSON(JSON_mUtils_mCursors.Cursor__.OfView(v))
        if (d_802_valueOrError0_).IsFailure():
            return (d_802_valueOrError0_).PropagateFailure()
        elif True:
            let_tmp_rhs23_ = (d_802_valueOrError0_).Extract()
            d_803_text_ = let_tmp_rhs23_.t
            d_804_cs_ = let_tmp_rhs23_.cs
            d_805_valueOrError1_ = Wrappers.default__.Need((d_804_cs_).EOF_q, JSON_mErrors.DeserializationError_ExpectingEOF())
            if (d_805_valueOrError1_).IsFailure():
                return (d_805_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success(d_803_text_)

    @staticmethod
    def OfBytes(bs):
        d_806_valueOrError0_ = Wrappers.default__.Need((len(bs)) < ((BoundedInts.default__).TWO__TO__THE__32), JSON_mErrors.DeserializationError_IntOverflow())
        if (d_806_valueOrError0_).IsFailure():
            return (d_806_valueOrError0_).PropagateFailure()
        elif True:
            return JSON_mZeroCopy_mDeserializer_mAPI.default__.Text(JSON_mUtils_mViews_mCore.View__.OfBytes(bs))

