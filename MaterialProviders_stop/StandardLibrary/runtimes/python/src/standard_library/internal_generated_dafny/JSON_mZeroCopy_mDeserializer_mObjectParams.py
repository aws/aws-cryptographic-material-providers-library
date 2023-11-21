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

assert "JSON_mZeroCopy_mDeserializer_mObjectParams" == __name__
JSON_mZeroCopy_mDeserializer_mObjectParams = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Colon(cs):
        d_695_valueOrError0_ = (cs).AssertChar(':')
        if (d_695_valueOrError0_).IsFailure():
            return (d_695_valueOrError0_).PropagateFailure()
        elif True:
            d_696_cs_ = (d_695_valueOrError0_).Extract()
            return Wrappers.Result_Success((d_696_cs_).Split())

    @staticmethod
    def KeyValueFromParts(k, colon, v):
        d_697_sp_ = JSON_mUtils_mCursors.Split_SP(JSON_mGrammar.jKeyValue_KeyValue((k).t, (colon).t, (v).t), (v).cs)
        return d_697_sp_

    @staticmethod
    def ElementSpec(t):
        return JSON_mConcreteSyntax_mSpec.default__.KeyValue(t)

    @staticmethod
    def Element(cs, json):
        d_698_valueOrError0_ = JSON_mZeroCopy_mDeserializer_mStrings.default__.String(cs)
        if (d_698_valueOrError0_).IsFailure():
            return (d_698_valueOrError0_).PropagateFailure()
        elif True:
            d_699_k_ = (d_698_valueOrError0_).Extract()
            d_700_p_ = JSON_mUtils_mParsers.Parser___Parser(JSON_mZeroCopy_mDeserializer_mObjectParams.default__.Colon)
            d_701_valueOrError1_ = JSON_mZeroCopy_mDeserializer_mCore.default__.Structural((d_699_k_).cs, d_700_p_)
            if (d_701_valueOrError1_).IsFailure():
                return (d_701_valueOrError1_).PropagateFailure()
            elif True:
                d_702_colon_ = (d_701_valueOrError1_).Extract()
                d_703_valueOrError2_ = (json).fn((d_702_colon_).cs)
                if (d_703_valueOrError2_).IsFailure():
                    return (d_703_valueOrError2_).PropagateFailure()
                elif True:
                    d_704_v_ = (d_703_valueOrError2_).Extract()
                    d_705_kv_ = JSON_mZeroCopy_mDeserializer_mObjectParams.default__.KeyValueFromParts(d_699_k_, d_702_colon_, d_704_v_)
                    return Wrappers.Result_Success(d_705_kv_)

    @_dafny.classproperty
    def OPEN(instance):
        return ord('{')
    @_dafny.classproperty
    def CLOSE(instance):
        return ord('}')
