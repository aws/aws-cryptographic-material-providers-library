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

# Module: JSON_ConcreteSyntax_Spec

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def View(v):
        return (v).Bytes()

    @staticmethod
    def Structural(self, fT):
        return ((default__.View((self).before)) + (fT((self).t))) + (default__.View((self).after))

    @staticmethod
    def StructuralView(self):
        return default__.Structural(self, default__.View)

    @staticmethod
    def Maybe(self, fT):
        if (self).is_Empty:
            return _dafny.Seq([])
        elif True:
            return fT((self).t)

    @staticmethod
    def ConcatBytes(ts, fT):
        d_573___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(ts)) == (0):
                    return (d_573___accumulator_) + (_dafny.Seq([]))
                elif True:
                    d_573___accumulator_ = (d_573___accumulator_) + (fT((ts)[0]))
                    in121_ = _dafny.Seq((ts)[1::])
                    in122_ = fT
                    ts = in121_
                    fT = in122_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def Bracketed(self, fDatum):
        return ((default__.StructuralView((self).l)) + (default__.ConcatBytes((self).data, fDatum))) + (default__.StructuralView((self).r))

    @staticmethod
    def KeyValue(self):
        return ((default__.String((self).k)) + (default__.StructuralView((self).colon))) + (default__.Value((self).v))

    @staticmethod
    def Frac(self):
        return (default__.View((self).period)) + (default__.View((self).num))

    @staticmethod
    def Exp(self):
        return ((default__.View((self).e)) + (default__.View((self).sign))) + (default__.View((self).num))

    @staticmethod
    def Number(self):
        return (((default__.View((self).minus)) + (default__.View((self).num))) + (default__.Maybe((self).frac, default__.Frac))) + (default__.Maybe((self).exp, default__.Exp))

    @staticmethod
    def String(self):
        return ((default__.View((self).lq)) + (default__.View((self).contents))) + (default__.View((self).rq))

    @staticmethod
    def CommaSuffix(c):
        return default__.Maybe(c, default__.StructuralView)

    @staticmethod
    def Member(self):
        return (default__.KeyValue((self).t)) + (default__.CommaSuffix((self).suffix))

    @staticmethod
    def Item(self):
        return (default__.Value((self).t)) + (default__.CommaSuffix((self).suffix))

    @staticmethod
    def Object(obj):
        def lambda43_(d_574_obj_):
            def lambda44_(d_575_d_):
                return default__.Member(d_575_d_)

            return lambda44_

        return default__.Bracketed(obj, lambda43_(obj))

    @staticmethod
    def Array(arr):
        def lambda45_(d_576_arr_):
            def lambda46_(d_577_d_):
                return default__.Item(d_577_d_)

            return lambda46_

        return default__.Bracketed(arr, lambda45_(arr))

    @staticmethod
    def Value(self):
        source18_ = self
        if source18_.is_Null:
            d_578___mcc_h0_ = source18_.n
            d_579_n_ = d_578___mcc_h0_
            return default__.View(d_579_n_)
        elif source18_.is_Bool:
            d_580___mcc_h1_ = source18_.b
            d_581_b_ = d_580___mcc_h1_
            return default__.View(d_581_b_)
        elif source18_.is_String:
            d_582___mcc_h2_ = source18_.str
            d_583_str_ = d_582___mcc_h2_
            return default__.String(d_583_str_)
        elif source18_.is_Number:
            d_584___mcc_h3_ = source18_.num
            d_585_num_ = d_584___mcc_h3_
            return default__.Number(d_585_num_)
        elif source18_.is_Object:
            d_586___mcc_h4_ = source18_.obj
            d_587_obj_ = d_586___mcc_h4_
            return default__.Object(d_587_obj_)
        elif True:
            d_588___mcc_h5_ = source18_.arr
            d_589_arr_ = d_588___mcc_h5_
            return default__.Array(d_589_arr_)

    @staticmethod
    def JSON(js):
        return default__.Structural(js, default__.Value)

