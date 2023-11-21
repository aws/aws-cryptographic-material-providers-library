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

assert "JSON_mZeroCopy_mDeserializer_mStrings" == __name__
JSON_mZeroCopy_mDeserializer_mStrings = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def StringBody(cs):
        pr: Wrappers.Result = Wrappers.Result_Success.default(JSON_mUtils_mCursors.Cursor.default)()
        d_652_escaped_: bool
        d_652_escaped_ = False
        hi11_: BoundedInts.uint32 = (cs).end
        for d_653_point_k_ in range((cs).point, hi11_):
            d_654_byte_: BoundedInts.uint8
            d_654_byte_ = ((cs).s)[d_653_point_k_]
            if ((d_654_byte_) == (ord('\"'))) and (not(d_652_escaped_)):
                pr = Wrappers.Result_Success(JSON_mUtils_mCursors.Cursor___Cursor((cs).s, (cs).beg, d_653_point_k_, (cs).end))
                return pr
            elif (d_654_byte_) == (ord('\\')):
                d_652_escaped_ = not(d_652_escaped_)
            elif True:
                d_652_escaped_ = False
        pr = Wrappers.Result_Failure(JSON_mUtils_mCursors.CursorError_EOF())
        return pr
        return pr

    @staticmethod
    def Quote(cs):
        d_655_valueOrError0_ = (cs).AssertChar('\"')
        if (d_655_valueOrError0_).IsFailure():
            return (d_655_valueOrError0_).PropagateFailure()
        elif True:
            d_656_cs_ = (d_655_valueOrError0_).Extract()
            return Wrappers.Result_Success((d_656_cs_).Split())

    @staticmethod
    def String(cs):
        d_657_valueOrError0_ = JSON_mZeroCopy_mDeserializer_mStrings.default__.Quote(cs)
        if (d_657_valueOrError0_).IsFailure():
            return (d_657_valueOrError0_).PropagateFailure()
        elif True:
            let_tmp_rhs8_ = (d_657_valueOrError0_).Extract()
            d_658_lq_ = let_tmp_rhs8_.t
            d_659_cs_ = let_tmp_rhs8_.cs
            d_660_valueOrError1_ = JSON_mZeroCopy_mDeserializer_mStrings.default__.StringBody(d_659_cs_)
            if (d_660_valueOrError1_).IsFailure():
                return (d_660_valueOrError1_).PropagateFailure()
            elif True:
                d_661_contents_ = (d_660_valueOrError1_).Extract()
                let_tmp_rhs9_ = (d_661_contents_).Split()
                d_662_contents_ = let_tmp_rhs9_.t
                d_663_cs_ = let_tmp_rhs9_.cs
                d_664_valueOrError2_ = JSON_mZeroCopy_mDeserializer_mStrings.default__.Quote(d_663_cs_)
                if (d_664_valueOrError2_).IsFailure():
                    return (d_664_valueOrError2_).PropagateFailure()
                elif True:
                    let_tmp_rhs10_ = (d_664_valueOrError2_).Extract()
                    d_665_rq_ = let_tmp_rhs10_.t
                    d_666_cs_ = let_tmp_rhs10_.cs
                    return Wrappers.Result_Success(JSON_mUtils_mCursors.Split_SP(JSON_mGrammar.jstring_JString(d_658_lq_, d_662_contents_, d_665_rq_), d_666_cs_))

