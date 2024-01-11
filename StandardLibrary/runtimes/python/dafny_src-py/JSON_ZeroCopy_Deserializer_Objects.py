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
import DafnyLibraries
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
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
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

# Module: JSON_ZeroCopy_Deserializer_Objects

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Object(cs, json):
        d_706_valueOrError0_ = default__.Bracketed(cs, json)
        if (d_706_valueOrError0_).IsFailure():
            return (d_706_valueOrError0_).PropagateFailure()
        elif True:
            d_707_sp_ = (d_706_valueOrError0_).Extract()
            return Wrappers.Result_Success(d_707_sp_)

    @staticmethod
    def Open(cs):
        d_708_valueOrError0_ = (cs).AssertByte(JSON_ZeroCopy_Deserializer_ObjectParams.default__.OPEN)
        if (d_708_valueOrError0_).IsFailure():
            return (d_708_valueOrError0_).PropagateFailure()
        elif True:
            d_709_cs_ = (d_708_valueOrError0_).Extract()
            return Wrappers.Result_Success((d_709_cs_).Split())

    @staticmethod
    def Close(cs):
        d_710_valueOrError0_ = (cs).AssertByte(JSON_ZeroCopy_Deserializer_ObjectParams.default__.CLOSE)
        if (d_710_valueOrError0_).IsFailure():
            return (d_710_valueOrError0_).PropagateFailure()
        elif True:
            d_711_cs_ = (d_710_valueOrError0_).Extract()
            return Wrappers.Result_Success((d_711_cs_).Split())

    @staticmethod
    def BracketedFromParts(open, elems, close):
        d_712_sp_ = JSON_Utils_Cursors.Split_SP(JSON_Grammar.Bracketed_Bracketed((open).t, (elems).t, (close).t), (close).cs)
        return d_712_sp_

    @staticmethod
    def AppendWithSuffix(elems, elem, sep):
        d_713_suffixed_ = JSON_Grammar.Suffixed_Suffixed((elem).t, JSON_Grammar.Maybe_NonEmpty((sep).t))
        d_714_elems_k_ = JSON_Utils_Cursors.Split_SP(((elems).t) + (_dafny.Seq([d_713_suffixed_])), (sep).cs)
        return d_714_elems_k_

    @staticmethod
    def AppendLast(elems, elem, sep):
        d_715_suffixed_ = JSON_Grammar.Suffixed_Suffixed((elem).t, JSON_Grammar.Maybe_Empty())
        d_716_elems_k_ = JSON_Utils_Cursors.Split_SP(((elems).t) + (_dafny.Seq([d_715_suffixed_])), (elem).cs)
        return d_716_elems_k_

    @staticmethod
    def Elements(json, open, elems):
        while True:
            with _dafny.label():
                d_717_valueOrError0_ = JSON_ZeroCopy_Deserializer_ObjectParams.default__.Element((elems).cs, json)
                if (d_717_valueOrError0_).IsFailure():
                    return (d_717_valueOrError0_).PropagateFailure()
                elif True:
                    d_718_elem_ = (d_717_valueOrError0_).Extract()
                    if ((d_718_elem_).cs).EOF_q:
                        return Wrappers.Result_Failure(JSON_Utils_Cursors.CursorError_EOF())
                    elif True:
                        d_719_sep_ = JSON_ZeroCopy_Deserializer_Core.default__.TryStructural((d_718_elem_).cs)
                        d_720_s0_ = (((d_719_sep_).t).t).Peek()
                        if ((d_720_s0_) == (default__.SEPARATOR)) and (((((d_719_sep_).t).t).Length()) == (1)):
                            d_721_sep_ = d_719_sep_
                            d_722_elems_ = default__.AppendWithSuffix(elems, d_718_elem_, d_721_sep_)
                            in123_ = json
                            in124_ = open
                            in125_ = d_722_elems_
                            json = in123_
                            open = in124_
                            elems = in125_
                            raise _dafny.TailCall()
                        elif ((d_720_s0_) == (JSON_ZeroCopy_Deserializer_ObjectParams.default__.CLOSE)) and (((((d_719_sep_).t).t).Length()) == (1)):
                            d_723_sep_ = d_719_sep_
                            d_724_elems_k_ = default__.AppendLast(elems, d_718_elem_, d_723_sep_)
                            d_725_bracketed_ = default__.BracketedFromParts(open, d_724_elems_k_, d_723_sep_)
                            return Wrappers.Result_Success(d_725_bracketed_)
                        elif True:
                            d_726_separator_ = default__.SEPARATOR
                            d_727_pr_ = Wrappers.Result_Failure(JSON_Utils_Cursors.CursorError_ExpectingAnyByte(_dafny.Seq([JSON_ZeroCopy_Deserializer_ObjectParams.default__.CLOSE, d_726_separator_]), d_720_s0_))
                            return d_727_pr_
                break

    @staticmethod
    def Bracketed(cs, json):
        d_728_valueOrError0_ = JSON_ZeroCopy_Deserializer_Core.default__.Structural(cs, JSON_Utils_Parsers.Parser___Parser(default__.Open))
        if (d_728_valueOrError0_).IsFailure():
            return (d_728_valueOrError0_).PropagateFailure()
        elif True:
            d_729_open_ = (d_728_valueOrError0_).Extract()
            d_730_elems_ = JSON_Utils_Cursors.Split_SP(_dafny.Seq([]), (d_729_open_).cs)
            if (((d_729_open_).cs).Peek()) == (JSON_ZeroCopy_Deserializer_ObjectParams.default__.CLOSE):
                d_731_p_ = JSON_Utils_Parsers.Parser___Parser(default__.Close)
                d_732_valueOrError1_ = JSON_ZeroCopy_Deserializer_Core.default__.Structural((d_729_open_).cs, d_731_p_)
                if (d_732_valueOrError1_).IsFailure():
                    return (d_732_valueOrError1_).PropagateFailure()
                elif True:
                    d_733_close_ = (d_732_valueOrError1_).Extract()
                    return Wrappers.Result_Success(default__.BracketedFromParts(d_729_open_, d_730_elems_, d_733_close_))
            elif True:
                return default__.Elements(json, d_729_open_, d_730_elems_)

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
        return JSON_Utils_Views_Core.View__.OfBytes(_dafny.Seq([JSON_ZeroCopy_Deserializer_ObjectParams.default__.OPEN]))

class jclose:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return JSON_Utils_Views_Core.View__.OfBytes(_dafny.Seq([JSON_ZeroCopy_Deserializer_ObjectParams.default__.CLOSE]))
