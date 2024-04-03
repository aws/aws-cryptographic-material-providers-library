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
import JSON_ZeroCopy_Deserializer_Arrays
import JSON_ZeroCopy_Deserializer_Constants
import JSON_ZeroCopy_Deserializer_Values
import JSON_ZeroCopy_Deserializer_API
import JSON_ZeroCopy_Deserializer
import JSON_ZeroCopy_API
import JSON_ZeroCopy

# Module: JSON_API

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Serialize(js):
        d_924_valueOrError0_ = JSON_Serializer.default__.JSON(js)
        if (d_924_valueOrError0_).IsFailure():
            return (d_924_valueOrError0_).PropagateFailure()
        elif True:
            d_925_js_ = (d_924_valueOrError0_).Extract()
            return JSON_ZeroCopy_API.default__.Serialize(d_925_js_)

    @staticmethod
    def SerializeAlloc(js):
        bs: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.pointer)()
        d_926_js_: JSON_Grammar.Structural
        d_927_valueOrError0_: Wrappers.Result = Wrappers.Result.default(JSON_Grammar.Structural.default(JSON_Grammar.Value.default()))()
        d_927_valueOrError0_ = JSON_Serializer.default__.JSON(js)
        if (d_927_valueOrError0_).IsFailure():
            bs = (d_927_valueOrError0_).PropagateFailure()
            return bs
        d_926_js_ = (d_927_valueOrError0_).Extract()
        out29_: Wrappers.Result
        out29_ = JSON_ZeroCopy_API.default__.SerializeAlloc(d_926_js_)
        bs = out29_
        return bs

    @staticmethod
    def SerializeInto(js, bs):
        len: Wrappers.Result = Wrappers.Result.default(BoundedInts.uint32.default)()
        d_928_js_: JSON_Grammar.Structural
        d_929_valueOrError0_: Wrappers.Result = Wrappers.Result.default(JSON_Grammar.Structural.default(JSON_Grammar.Value.default()))()
        d_929_valueOrError0_ = JSON_Serializer.default__.JSON(js)
        if (d_929_valueOrError0_).IsFailure():
            len = (d_929_valueOrError0_).PropagateFailure()
            return len
        d_928_js_ = (d_929_valueOrError0_).Extract()
        out30_: Wrappers.Result
        out30_ = JSON_ZeroCopy_API.default__.SerializeInto(d_928_js_, bs)
        len = out30_
        return len

    @staticmethod
    def Deserialize(bs):
        d_930_valueOrError0_ = JSON_ZeroCopy_API.default__.Deserialize(bs)
        if (d_930_valueOrError0_).IsFailure():
            return (d_930_valueOrError0_).PropagateFailure()
        elif True:
            d_931_js_ = (d_930_valueOrError0_).Extract()
            return JSON_Deserializer.default__.JSON(d_931_js_)

