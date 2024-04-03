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

# Module: JSON_ZeroCopy_Deserializer_ObjectParams

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Colon(cs):
        d_806_valueOrError0_ = (cs).AssertChar(':')
        if (d_806_valueOrError0_).IsFailure():
            return (d_806_valueOrError0_).PropagateFailure()
        elif True:
            d_807_cs_ = (d_806_valueOrError0_).Extract()
            return Wrappers.Result_Success((d_807_cs_).Split())

    @staticmethod
    def KeyValueFromParts(k, colon, v):
        d_808_sp_ = JSON_Utils_Cursors.Split_SP(JSON_Grammar.jKeyValue_KeyValue((k).t, (colon).t, (v).t), (v).cs)
        return d_808_sp_

    @staticmethod
    def ElementSpec(t):
        return JSON_ConcreteSyntax_Spec.default__.KeyValue(t)

    @staticmethod
    def Element(cs, json):
        d_809_valueOrError0_ = JSON_ZeroCopy_Deserializer_Strings.default__.String(cs)
        if (d_809_valueOrError0_).IsFailure():
            return (d_809_valueOrError0_).PropagateFailure()
        elif True:
            d_810_k_ = (d_809_valueOrError0_).Extract()
            d_811_p_ = JSON_Utils_Parsers.Parser___Parser(default__.Colon)
            d_812_valueOrError1_ = JSON_ZeroCopy_Deserializer_Core.default__.Structural((d_810_k_).cs, d_811_p_)
            if (d_812_valueOrError1_).IsFailure():
                return (d_812_valueOrError1_).PropagateFailure()
            elif True:
                d_813_colon_ = (d_812_valueOrError1_).Extract()
                d_814_valueOrError2_ = (json).fn((d_813_colon_).cs)
                if (d_814_valueOrError2_).IsFailure():
                    return (d_814_valueOrError2_).PropagateFailure()
                elif True:
                    d_815_v_ = (d_814_valueOrError2_).Extract()
                    d_816_kv_ = default__.KeyValueFromParts(d_810_k_, d_813_colon_, d_815_v_)
                    return Wrappers.Result_Success(d_816_kv_)

    @_dafny.classproperty
    def OPEN(instance):
        return ord('{')
    @_dafny.classproperty
    def CLOSE(instance):
        return ord('}')
