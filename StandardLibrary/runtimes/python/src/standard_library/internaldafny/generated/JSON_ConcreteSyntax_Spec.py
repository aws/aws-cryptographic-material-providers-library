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
        d_684___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(ts)) == (0):
                    return (d_684___accumulator_) + (_dafny.Seq([]))
                elif True:
                    d_684___accumulator_ = (d_684___accumulator_) + (fT((ts)[0]))
                    in224_ = _dafny.Seq((ts)[1::])
                    in225_ = fT
                    ts = in224_
                    fT = in225_
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
        def lambda46_(d_685_obj_):
            def lambda47_(d_686_d_):
                return default__.Member(d_686_d_)

            return lambda47_

        return default__.Bracketed(obj, lambda46_(obj))

    @staticmethod
    def Array(arr):
        def lambda48_(d_687_arr_):
            def lambda49_(d_688_d_):
                return default__.Item(d_688_d_)

            return lambda49_

        return default__.Bracketed(arr, lambda48_(arr))

    @staticmethod
    def Value(self):
        source18_ = self
        if source18_.is_Null:
            d_689___mcc_h0_ = source18_.n
            d_690_n_ = d_689___mcc_h0_
            return default__.View(d_690_n_)
        elif source18_.is_Bool:
            d_691___mcc_h1_ = source18_.b
            d_692_b_ = d_691___mcc_h1_
            return default__.View(d_692_b_)
        elif source18_.is_String:
            d_693___mcc_h2_ = source18_.str
            d_694_str_ = d_693___mcc_h2_
            return default__.String(d_694_str_)
        elif source18_.is_Number:
            d_695___mcc_h3_ = source18_.num
            d_696_num_ = d_695___mcc_h3_
            return default__.Number(d_696_num_)
        elif source18_.is_Object:
            d_697___mcc_h4_ = source18_.obj
            d_698_obj_ = d_697___mcc_h4_
            return default__.Object(d_698_obj_)
        elif True:
            d_699___mcc_h5_ = source18_.arr
            d_700_arr_ = d_699___mcc_h5_
            return default__.Array(d_700_arr_)

    @staticmethod
    def JSON(js):
        return default__.Structural(js, default__.Value)

