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
import JSON_mZeroCopy_mDeserializer_mAPI
import JSON_mZeroCopy_mDeserializer
import JSON_mZeroCopy_mAPI
import JSON_mZeroCopy

# assert "JSON_mAPI" == __name__
JSON_mAPI = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Serialize(js):
        d_807_valueOrError0_ = JSON_mSerializer.default__.JSON(js)
        if (d_807_valueOrError0_).IsFailure():
            return (d_807_valueOrError0_).PropagateFailure()
        elif True:
            d_808_js_ = (d_807_valueOrError0_).Extract()
            return JSON_mZeroCopy_mAPI.default__.Serialize(d_808_js_)

    @staticmethod
    def SerializeAlloc(js):
        bs: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.pointer)()
        d_809_js_: JSON_mGrammar.Structural
        d_810_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(JSON_mGrammar.Structural.default(JSON_mGrammar.Value.default()))()
        d_810_valueOrError0_ = JSON_mSerializer.default__.JSON(js)
        if (d_810_valueOrError0_).IsFailure():
            bs = (d_810_valueOrError0_).PropagateFailure()
            return bs
        d_809_js_ = (d_810_valueOrError0_).Extract()
        out29_: Wrappers.Result
        out29_ = JSON_mZeroCopy_mAPI.default__.SerializeAlloc(d_809_js_)
        bs = out29_
        return bs

    @staticmethod
    def SerializeInto(js, bs):
        len: Wrappers.Result = Wrappers.Result_Success.default(BoundedInts.uint32.default)()
        d_811_js_: JSON_mGrammar.Structural
        d_812_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(JSON_mGrammar.Structural.default(JSON_mGrammar.Value.default()))()
        d_812_valueOrError0_ = JSON_mSerializer.default__.JSON(js)
        if (d_812_valueOrError0_).IsFailure():
            len = (d_812_valueOrError0_).PropagateFailure()
            return len
        d_811_js_ = (d_812_valueOrError0_).Extract()
        out30_: Wrappers.Result
        out30_ = JSON_mZeroCopy_mAPI.default__.SerializeInto(d_811_js_, bs)
        len = out30_
        return len

    @staticmethod
    def Deserialize(bs):
        d_813_valueOrError0_ = JSON_mZeroCopy_mAPI.default__.Deserialize(bs)
        if (d_813_valueOrError0_).IsFailure():
            return (d_813_valueOrError0_).PropagateFailure()
        elif True:
            d_814_js_ = (d_813_valueOrError0_).Extract()
            return JSON_mDeserializer.default__.JSON(d_814_js_)

