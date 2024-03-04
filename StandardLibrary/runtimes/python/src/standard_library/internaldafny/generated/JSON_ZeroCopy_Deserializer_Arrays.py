import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_MergeSort
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
import StandardLibraryInterop
import StandardLibrary_UInt
import StandardLibrary_String
import StandardLibrary
import UUID
import UTF8
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import GetOpt
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
import JSON_Utils_Views_Core
import JSON_Utils_Views_Writers
import JSON_Utils_Views
import JSON_Utils_Lexers_Core
import JSON_Utils_Lexers_Strings
import JSON_Utils_Lexers
import JSON_Utils_Cursors
import JSON_Utils_Parsers
import JSON_Utils_Str_CharStrConversion
import JSON_Utils_Str_CharStrEscaping
import JSON_Utils_Str
import JSON_Utils_Seq
import JSON_Utils_Vectors
import JSON_Utils
import JSON_Errors
import JSON_Values
import JSON_Spec
import JSON_Grammar
import JSON_Serializer_ByteStrConversion
import JSON_Serializer
import JSON_Deserializer_Uint16StrConversion
import JSON_Deserializer_ByteStrConversion
import JSON_Deserializer
import JSON_ConcreteSyntax_Spec
import JSON_ConcreteSyntax_SpecProperties
import JSON_ConcreteSyntax
import JSON_ZeroCopy_Serializer
import JSON_ZeroCopy_Deserializer_Core
import JSON_ZeroCopy_Deserializer_Strings
import JSON_ZeroCopy_Deserializer_Numbers
import JSON_ZeroCopy_Deserializer_ObjectParams
import JSON_ZeroCopy_Deserializer_Objects
import JSON_ZeroCopy_Deserializer_ArrayParams

# Module: JSON_ZeroCopy_Deserializer_Arrays

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Array(cs, json):
        d_819_valueOrError0_ = default__.Bracketed(cs, json)
        if (d_819_valueOrError0_).IsFailure():
            return (d_819_valueOrError0_).PropagateFailure()
        elif True:
            d_820_sp_ = (d_819_valueOrError0_).Extract()
            return Wrappers.Result_Success(d_820_sp_)

    @staticmethod
    def Open(cs):
        d_821_valueOrError0_ = (cs).AssertByte(JSON_ZeroCopy_Deserializer_ArrayParams.default__.OPEN)
        if (d_821_valueOrError0_).IsFailure():
            return (d_821_valueOrError0_).PropagateFailure()
        elif True:
            d_822_cs_ = (d_821_valueOrError0_).Extract()
            return Wrappers.Result_Success((d_822_cs_).Split())

    @staticmethod
    def Close(cs):
        d_823_valueOrError0_ = (cs).AssertByte(JSON_ZeroCopy_Deserializer_ArrayParams.default__.CLOSE)
        if (d_823_valueOrError0_).IsFailure():
            return (d_823_valueOrError0_).PropagateFailure()
        elif True:
            d_824_cs_ = (d_823_valueOrError0_).Extract()
            return Wrappers.Result_Success((d_824_cs_).Split())

    @staticmethod
    def BracketedFromParts(open, elems, close):
        d_825_sp_ = JSON_Utils_Cursors.Split_SP(JSON_Grammar.Bracketed_Bracketed((open).t, (elems).t, (close).t), (close).cs)
        return d_825_sp_

    @staticmethod
    def AppendWithSuffix(elems, elem, sep):
        d_826_suffixed_ = JSON_Grammar.Suffixed_Suffixed((elem).t, JSON_Grammar.Maybe_NonEmpty((sep).t))
        d_827_elems_k_ = JSON_Utils_Cursors.Split_SP(((elems).t) + (_dafny.Seq([d_826_suffixed_])), (sep).cs)
        return d_827_elems_k_

    @staticmethod
    def AppendLast(elems, elem, sep):
        d_828_suffixed_ = JSON_Grammar.Suffixed_Suffixed((elem).t, JSON_Grammar.Maybe_Empty())
        d_829_elems_k_ = JSON_Utils_Cursors.Split_SP(((elems).t) + (_dafny.Seq([d_828_suffixed_])), (elem).cs)
        return d_829_elems_k_

    @staticmethod
    def Elements(json, open, elems):
        while True:
            with _dafny.label():
                d_830_valueOrError0_ = JSON_ZeroCopy_Deserializer_ArrayParams.default__.Element((elems).cs, json)
                if (d_830_valueOrError0_).IsFailure():
                    return (d_830_valueOrError0_).PropagateFailure()
                elif True:
                    d_831_elem_ = (d_830_valueOrError0_).Extract()
                    if ((d_831_elem_).cs).EOF_q:
                        return Wrappers.Result_Failure(JSON_Utils_Cursors.CursorError_EOF())
                    elif True:
                        d_832_sep_ = JSON_ZeroCopy_Deserializer_Core.default__.TryStructural((d_831_elem_).cs)
                        d_833_s0_ = (((d_832_sep_).t).t).Peek()
                        if ((d_833_s0_) == (default__.SEPARATOR)) and (((((d_832_sep_).t).t).Length()) == (1)):
                            d_834_sep_ = d_832_sep_
                            d_835_elems_ = default__.AppendWithSuffix(elems, d_831_elem_, d_834_sep_)
                            in229_ = json
                            in230_ = open
                            in231_ = d_835_elems_
                            json = in229_
                            open = in230_
                            elems = in231_
                            raise _dafny.TailCall()
                        elif ((d_833_s0_) == (JSON_ZeroCopy_Deserializer_ArrayParams.default__.CLOSE)) and (((((d_832_sep_).t).t).Length()) == (1)):
                            d_836_sep_ = d_832_sep_
                            d_837_elems_k_ = default__.AppendLast(elems, d_831_elem_, d_836_sep_)
                            d_838_bracketed_ = default__.BracketedFromParts(open, d_837_elems_k_, d_836_sep_)
                            return Wrappers.Result_Success(d_838_bracketed_)
                        elif True:
                            d_839_separator_ = default__.SEPARATOR
                            d_840_pr_ = Wrappers.Result_Failure(JSON_Utils_Cursors.CursorError_ExpectingAnyByte(_dafny.Seq([JSON_ZeroCopy_Deserializer_ArrayParams.default__.CLOSE, d_839_separator_]), d_833_s0_))
                            return d_840_pr_
                break

    @staticmethod
    def Bracketed(cs, json):
        d_841_valueOrError0_ = JSON_ZeroCopy_Deserializer_Core.default__.Structural(cs, JSON_Utils_Parsers.Parser___Parser(default__.Open))
        if (d_841_valueOrError0_).IsFailure():
            return (d_841_valueOrError0_).PropagateFailure()
        elif True:
            d_842_open_ = (d_841_valueOrError0_).Extract()
            d_843_elems_ = JSON_Utils_Cursors.Split_SP(_dafny.Seq([]), (d_842_open_).cs)
            if (((d_842_open_).cs).Peek()) == (JSON_ZeroCopy_Deserializer_ArrayParams.default__.CLOSE):
                d_844_p_ = JSON_Utils_Parsers.Parser___Parser(default__.Close)
                d_845_valueOrError1_ = JSON_ZeroCopy_Deserializer_Core.default__.Structural((d_842_open_).cs, d_844_p_)
                if (d_845_valueOrError1_).IsFailure():
                    return (d_845_valueOrError1_).PropagateFailure()
                elif True:
                    d_846_close_ = (d_845_valueOrError1_).Extract()
                    return Wrappers.Result_Success(default__.BracketedFromParts(d_842_open_, d_843_elems_, d_846_close_))
            elif True:
                return default__.Elements(json, d_842_open_, d_843_elems_)

    @_dafny.classproperty
    def SpecViewOpen(instance):
        return JSON_ZeroCopy_Deserializer_Core.default__.SpecView
    @_dafny.classproperty
    def SpecViewClose(instance):
        return JSON_ZeroCopy_Deserializer_Core.default__.SpecView
    @_dafny.classproperty
    def SEPARATOR(instance):
        return ord(',')

class jopen:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return JSON_Utils_Views_Core.View__.OfBytes(_dafny.Seq([JSON_ZeroCopy_Deserializer_ArrayParams.default__.OPEN]))

class jclose:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return JSON_Utils_Views_Core.View__.OfBytes(_dafny.Seq([JSON_ZeroCopy_Deserializer_ArrayParams.default__.CLOSE]))
