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

# Module: JSON_mZeroCopy_mDeserializer_mArrays

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Array(cs, json):
        d_731_valueOrError0_ = default__.Bracketed(cs, json)
        if (d_731_valueOrError0_).IsFailure():
            return (d_731_valueOrError0_).PropagateFailure()
        elif True:
            d_732_sp_ = (d_731_valueOrError0_).Extract()
            return Wrappers.Result_Success(d_732_sp_)

    @staticmethod
    def Open(cs):
        d_733_valueOrError0_ = (cs).AssertByte(JSON_mZeroCopy_mDeserializer_mArrayParams.default__.OPEN)
        if (d_733_valueOrError0_).IsFailure():
            return (d_733_valueOrError0_).PropagateFailure()
        elif True:
            d_734_cs_ = (d_733_valueOrError0_).Extract()
            return Wrappers.Result_Success((d_734_cs_).Split())

    @staticmethod
    def Close(cs):
        d_735_valueOrError0_ = (cs).AssertByte(JSON_mZeroCopy_mDeserializer_mArrayParams.default__.CLOSE)
        if (d_735_valueOrError0_).IsFailure():
            return (d_735_valueOrError0_).PropagateFailure()
        elif True:
            d_736_cs_ = (d_735_valueOrError0_).Extract()
            return Wrappers.Result_Success((d_736_cs_).Split())

    @staticmethod
    def BracketedFromParts(open, elems, close):
        d_737_sp_ = JSON_mUtils_mCursors.Split_SP(JSON_mGrammar.Bracketed_Bracketed((open).t, (elems).t, (close).t), (close).cs)
        return d_737_sp_

    @staticmethod
    def AppendWithSuffix(elems, elem, sep):
        d_738_suffixed_ = JSON_mGrammar.Suffixed_Suffixed((elem).t, JSON_mGrammar.Maybe_NonEmpty((sep).t))
        d_739_elems_k_ = JSON_mUtils_mCursors.Split_SP(((elems).t) + (_dafny.Seq([d_738_suffixed_])), (sep).cs)
        return d_739_elems_k_

    @staticmethod
    def AppendLast(elems, elem, sep):
        d_740_suffixed_ = JSON_mGrammar.Suffixed_Suffixed((elem).t, JSON_mGrammar.Maybe_Empty())
        d_741_elems_k_ = JSON_mUtils_mCursors.Split_SP(((elems).t) + (_dafny.Seq([d_740_suffixed_])), (elem).cs)
        return d_741_elems_k_

    @staticmethod
    def Elements(json, open, elems):
        while True:
            with _dafny.label():
                d_742_valueOrError0_ = JSON_mZeroCopy_mDeserializer_mArrayParams.default__.Element((elems).cs, json)
                if (d_742_valueOrError0_).IsFailure():
                    return (d_742_valueOrError0_).PropagateFailure()
                elif True:
                    d_743_elem_ = (d_742_valueOrError0_).Extract()
                    d_744_sep_ = JSON_mZeroCopy_mDeserializer_mCore.default__.TryStructural((d_743_elem_).cs)
                    d_745_s0_ = (((d_744_sep_).t).t).Peek()
                    if (d_745_s0_) == (default__.SEPARATOR):
                        d_746_elems_ = default__.AppendWithSuffix(elems, d_743_elem_, d_744_sep_)
                        in126_ = json
                        in127_ = open
                        in128_ = d_746_elems_
                        json = in126_
                        open = in127_
                        elems = in128_
                        raise _dafny.TailCall()
                    elif (d_745_s0_) == (JSON_mZeroCopy_mDeserializer_mArrayParams.default__.CLOSE):
                        d_747_elems_k_ = default__.AppendLast(elems, d_743_elem_, d_744_sep_)
                        d_748_bracketed_ = default__.BracketedFromParts(open, d_747_elems_k_, d_744_sep_)
                        return Wrappers.Result_Success(d_748_bracketed_)
                    elif True:
                        d_749_separator_ = default__.SEPARATOR
                        d_750_pr_ = Wrappers.Result_Failure(JSON_mUtils_mCursors.CursorError_ExpectingAnyByte(_dafny.Seq([JSON_mZeroCopy_mDeserializer_mArrayParams.default__.CLOSE, d_749_separator_]), d_745_s0_))
                        return d_750_pr_
                break

    @staticmethod
    def Bracketed(cs, json):
        d_751_valueOrError0_ = JSON_mZeroCopy_mDeserializer_mCore.default__.Structural(cs, JSON_mUtils_mParsers.Parser___Parser(default__.Open))
        if (d_751_valueOrError0_).IsFailure():
            return (d_751_valueOrError0_).PropagateFailure()
        elif True:
            d_752_open_ = (d_751_valueOrError0_).Extract()
            d_753_elems_ = JSON_mUtils_mCursors.Split_SP(_dafny.Seq([]), (d_752_open_).cs)
            if (((d_752_open_).cs).Peek()) == (JSON_mZeroCopy_mDeserializer_mArrayParams.default__.CLOSE):
                d_754_valueOrError1_ = JSON_mZeroCopy_mDeserializer_mCore.default__.Structural((d_752_open_).cs, JSON_mUtils_mParsers.Parser___Parser(default__.Close))
                if (d_754_valueOrError1_).IsFailure():
                    return (d_754_valueOrError1_).PropagateFailure()
                elif True:
                    d_755_close_ = (d_754_valueOrError1_).Extract()
                    return Wrappers.Result_Success(default__.BracketedFromParts(d_752_open_, d_753_elems_, d_755_close_))
            elif True:
                return default__.Elements(json, d_752_open_, d_753_elems_)

    @_dafny.classproperty
    def SEPARATOR(instance):
        return ord(',')

class jopen:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return JSON_mUtils_mViews_mCore.View__.OfBytes(_dafny.Seq([JSON_mZeroCopy_mDeserializer_mArrayParams.default__.OPEN]))

class jclose:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return JSON_mUtils_mViews_mCore.View__.OfBytes(_dafny.Seq([JSON_mZeroCopy_mDeserializer_mArrayParams.default__.CLOSE]))
