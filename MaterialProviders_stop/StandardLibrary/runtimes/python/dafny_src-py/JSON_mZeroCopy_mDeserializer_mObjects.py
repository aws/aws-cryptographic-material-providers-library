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

assert "JSON_mZeroCopy_mDeserializer_mObjects" == __name__
JSON_mZeroCopy_mDeserializer_mObjects = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Object(cs, json):
        d_706_valueOrError0_ = JSON_mZeroCopy_mDeserializer_mObjects.default__.Bracketed(cs, json)
        if (d_706_valueOrError0_).IsFailure():
            return (d_706_valueOrError0_).PropagateFailure()
        elif True:
            d_707_sp_ = (d_706_valueOrError0_).Extract()
            return Wrappers.Result_Success(d_707_sp_)

    @staticmethod
    def Open(cs):
        d_708_valueOrError0_ = (cs).AssertByte((JSON_mZeroCopy_mDeserializer_mObjectParams.default__).OPEN)
        if (d_708_valueOrError0_).IsFailure():
            return (d_708_valueOrError0_).PropagateFailure()
        elif True:
            d_709_cs_ = (d_708_valueOrError0_).Extract()
            return Wrappers.Result_Success((d_709_cs_).Split())

    @staticmethod
    def Close(cs):
        d_710_valueOrError0_ = (cs).AssertByte((JSON_mZeroCopy_mDeserializer_mObjectParams.default__).CLOSE)
        if (d_710_valueOrError0_).IsFailure():
            return (d_710_valueOrError0_).PropagateFailure()
        elif True:
            d_711_cs_ = (d_710_valueOrError0_).Extract()
            return Wrappers.Result_Success((d_711_cs_).Split())

    @staticmethod
    def BracketedFromParts(open, elems, close):
        d_712_sp_ = JSON_mUtils_mCursors.Split_SP(JSON_mGrammar.Bracketed_Bracketed((open).t, (elems).t, (close).t), (close).cs)
        return d_712_sp_

    @staticmethod
    def AppendWithSuffix(elems, elem, sep):
        d_713_suffixed_ = JSON_mGrammar.Suffixed_Suffixed((elem).t, JSON_mGrammar.Maybe_NonEmpty((sep).t))
        d_714_elems_k_ = JSON_mUtils_mCursors.Split_SP(((elems).t) + (_dafny.Seq([d_713_suffixed_])), (sep).cs)
        return d_714_elems_k_

    @staticmethod
    def AppendLast(elems, elem, sep):
        d_715_suffixed_ = JSON_mGrammar.Suffixed_Suffixed((elem).t, JSON_mGrammar.Maybe_Empty())
        d_716_elems_k_ = JSON_mUtils_mCursors.Split_SP(((elems).t) + (_dafny.Seq([d_715_suffixed_])), (elem).cs)
        return d_716_elems_k_

    @staticmethod
    def Elements(json, open, elems):
        while True:
            with _dafny.label():
                d_717_valueOrError0_ = JSON_mZeroCopy_mDeserializer_mObjectParams.default__.Element((elems).cs, json)
                if (d_717_valueOrError0_).IsFailure():
                    return (d_717_valueOrError0_).PropagateFailure()
                elif True:
                    d_718_elem_ = (d_717_valueOrError0_).Extract()
                    d_719_sep_ = JSON_mZeroCopy_mDeserializer_mCore.default__.TryStructural((d_718_elem_).cs)
                    d_720_s0_ = (((d_719_sep_).t).t).Peek()
                    if (d_720_s0_) == ((JSON_mZeroCopy_mDeserializer_mObjects.default__).SEPARATOR):
                        d_721_elems_ = JSON_mZeroCopy_mDeserializer_mObjects.default__.AppendWithSuffix(elems, d_718_elem_, d_719_sep_)
                        in123_ = json
                        in124_ = open
                        in125_ = d_721_elems_
                        json = in123_
                        open = in124_
                        elems = in125_
                        raise _dafny.TailCall()
                    elif (d_720_s0_) == ((JSON_mZeroCopy_mDeserializer_mObjectParams.default__).CLOSE):
                        d_722_elems_k_ = JSON_mZeroCopy_mDeserializer_mObjects.default__.AppendLast(elems, d_718_elem_, d_719_sep_)
                        d_723_bracketed_ = JSON_mZeroCopy_mDeserializer_mObjects.default__.BracketedFromParts(open, d_722_elems_k_, d_719_sep_)
                        return Wrappers.Result_Success(d_723_bracketed_)
                    elif True:
                        d_724_separator_ = (JSON_mZeroCopy_mDeserializer_mObjects.default__).SEPARATOR
                        d_725_pr_ = Wrappers.Result_Failure(JSON_mUtils_mCursors.CursorError_ExpectingAnyByte(_dafny.Seq([(JSON_mZeroCopy_mDeserializer_mObjectParams.default__).CLOSE, d_724_separator_]), d_720_s0_))
                        return d_725_pr_
                break

    @staticmethod
    def Bracketed(cs, json):
        d_726_valueOrError0_ = JSON_mZeroCopy_mDeserializer_mCore.default__.Structural(cs, JSON_mUtils_mParsers.Parser___Parser(JSON_mZeroCopy_mDeserializer_mObjects.default__.Open))
        if (d_726_valueOrError0_).IsFailure():
            return (d_726_valueOrError0_).PropagateFailure()
        elif True:
            d_727_open_ = (d_726_valueOrError0_).Extract()
            d_728_elems_ = JSON_mUtils_mCursors.Split_SP(_dafny.Seq([]), (d_727_open_).cs)
            if (((d_727_open_).cs).Peek()) == ((JSON_mZeroCopy_mDeserializer_mObjectParams.default__).CLOSE):
                d_729_valueOrError1_ = JSON_mZeroCopy_mDeserializer_mCore.default__.Structural((d_727_open_).cs, JSON_mUtils_mParsers.Parser___Parser(JSON_mZeroCopy_mDeserializer_mObjects.default__.Close))
                if (d_729_valueOrError1_).IsFailure():
                    return (d_729_valueOrError1_).PropagateFailure()
                elif True:
                    d_730_close_ = (d_729_valueOrError1_).Extract()
                    return Wrappers.Result_Success(JSON_mZeroCopy_mDeserializer_mObjects.default__.BracketedFromParts(d_727_open_, d_728_elems_, d_730_close_))
            elif True:
                return JSON_mZeroCopy_mDeserializer_mObjects.default__.Elements(json, d_727_open_, d_728_elems_)

    @_dafny.classproperty
    def SEPARATOR(instance):
        return ord(',')

class jopen:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return JSON_mUtils_mViews_mCore.View__.OfBytes(_dafny.Seq([(JSON_mZeroCopy_mDeserializer_mObjectParams.default__).OPEN]))

class jclose:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return JSON_mUtils_mViews_mCore.View__.OfBytes(_dafny.Seq([(JSON_mZeroCopy_mDeserializer_mObjectParams.default__).CLOSE]))
