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

# assert "JSON_mZeroCopy_mDeserializer_mCore" == __name__
JSON_mZeroCopy_mDeserializer_mCore = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Get(cs, err):
        d_634_valueOrError0_ = (cs).Get(err)
        if (d_634_valueOrError0_).IsFailure():
            return (d_634_valueOrError0_).PropagateFailure()
        elif True:
            d_635_cs_ = (d_634_valueOrError0_).Extract()
            return Wrappers.Result_Success((d_635_cs_).Split())

    @staticmethod
    def WS(cs):
        sp: JSON_mUtils_mCursors.Split = JSON_mUtils_mCursors.Split_SP.default(JSON_mGrammar.jblanks.default)()
        d_636_point_k_: BoundedInts.uint32
        d_636_point_k_ = (cs).point
        d_637_end_: BoundedInts.uint32
        d_637_end_ = (cs).end
        while ((d_636_point_k_) < (d_637_end_)) and (JSON_mGrammar.default__.Blank_q(((cs).s)[d_636_point_k_])):
            d_636_point_k_ = (d_636_point_k_) + (1)
        sp = (JSON_mUtils_mCursors.Cursor___Cursor((cs).s, (cs).beg, d_636_point_k_, (cs).end)).Split()
        return sp
        return sp

    @staticmethod
    def Structural(cs, parser):
        let_tmp_rhs2_ = JSON_mZeroCopy_mDeserializer_mCore.default__.WS(cs)
        d_638_before_ = let_tmp_rhs2_.t
        d_639_cs_ = let_tmp_rhs2_.cs
        d_640_valueOrError0_ = (parser).fn(d_639_cs_)
        if (d_640_valueOrError0_).IsFailure():
            return (d_640_valueOrError0_).PropagateFailure()
        elif True:
            let_tmp_rhs3_ = (d_640_valueOrError0_).Extract()
            d_641_val_ = let_tmp_rhs3_.t
            d_642_cs_ = let_tmp_rhs3_.cs
            let_tmp_rhs4_ = JSON_mZeroCopy_mDeserializer_mCore.default__.WS(d_642_cs_)
            d_643_after_ = let_tmp_rhs4_.t
            d_644_cs_ = let_tmp_rhs4_.cs
            return Wrappers.Result_Success(JSON_mUtils_mCursors.Split_SP(JSON_mGrammar.Structural_Structural(d_638_before_, d_641_val_, d_643_after_), d_644_cs_))

    @staticmethod
    def TryStructural(cs):
        let_tmp_rhs5_ = JSON_mZeroCopy_mDeserializer_mCore.default__.WS(cs)
        d_645_before_ = let_tmp_rhs5_.t
        d_646_cs_ = let_tmp_rhs5_.cs
        let_tmp_rhs6_ = ((d_646_cs_).SkipByte()).Split()
        d_647_val_ = let_tmp_rhs6_.t
        d_648_cs_ = let_tmp_rhs6_.cs
        let_tmp_rhs7_ = JSON_mZeroCopy_mDeserializer_mCore.default__.WS(d_648_cs_)
        d_649_after_ = let_tmp_rhs7_.t
        d_650_cs_ = let_tmp_rhs7_.cs
        return JSON_mUtils_mCursors.Split_SP(JSON_mGrammar.Structural_Structural(d_645_before_, d_647_val_, d_649_after_), d_650_cs_)

    @_dafny.classproperty
    def SpecView(instance):
        def lambda50_(d_651_v_):
            return JSON_mConcreteSyntax_mSpec.default__.View(d_651_v_)

        return lambda50_

class jopt:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return JSON_mUtils_mViews_mCore.View__.OfBytes(_dafny.Seq([]))

class ValueParser:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return JSON_mUtils_mParsers.SubParser.default()
