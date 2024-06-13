import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import standard_library.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import standard_library.internaldafny.generated.Wrappers as Wrappers
import standard_library.internaldafny.generated.Relations as Relations
import standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import standard_library.internaldafny.generated.Math as Math
import standard_library.internaldafny.generated.Seq as Seq
import standard_library.internaldafny.generated.BoundedInts as BoundedInts
import standard_library.internaldafny.generated.Unicode as Unicode
import standard_library.internaldafny.generated.Functions as Functions
import standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import standard_library.internaldafny.generated.FileIO as FileIO
import standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import standard_library.internaldafny.generated.MulInternals as MulInternals
import standard_library.internaldafny.generated.Mul as Mul
import standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import standard_library.internaldafny.generated.ModInternals as ModInternals
import standard_library.internaldafny.generated.DivInternals as DivInternals
import standard_library.internaldafny.generated.DivMod as DivMod
import standard_library.internaldafny.generated.Power as Power
import standard_library.internaldafny.generated.Logarithm as Logarithm
import standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import standard_library.internaldafny.generated.UUID as UUID
import standard_library.internaldafny.generated.UTF8 as UTF8
import standard_library.internaldafny.generated.Time as Time
import standard_library.internaldafny.generated.Streams as Streams
import standard_library.internaldafny.generated.Sorting as Sorting
import standard_library.internaldafny.generated.SortedSets as SortedSets
import standard_library.internaldafny.generated.HexStrings as HexStrings
import standard_library.internaldafny.generated.GetOpt as GetOpt
import standard_library.internaldafny.generated.FloatCompare as FloatCompare
import standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import standard_library.internaldafny.generated.Base64 as Base64
import standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import standard_library.internaldafny.generated.Actions as Actions
import standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import standard_library.internaldafny.generated.JSON_Utils_Views_Core as JSON_Utils_Views_Core
import standard_library.internaldafny.generated.JSON_Utils_Views_Writers as JSON_Utils_Views_Writers
import standard_library.internaldafny.generated.JSON_Utils_Views as JSON_Utils_Views
import standard_library.internaldafny.generated.JSON_Utils_Lexers_Core as JSON_Utils_Lexers_Core
import standard_library.internaldafny.generated.JSON_Utils_Lexers_Strings as JSON_Utils_Lexers_Strings
import standard_library.internaldafny.generated.JSON_Utils_Lexers as JSON_Utils_Lexers
import standard_library.internaldafny.generated.JSON_Utils_Cursors as JSON_Utils_Cursors
import standard_library.internaldafny.generated.JSON_Utils_Parsers as JSON_Utils_Parsers
import standard_library.internaldafny.generated.JSON_Utils_Str_CharStrConversion as JSON_Utils_Str_CharStrConversion
import standard_library.internaldafny.generated.JSON_Utils_Str_CharStrEscaping as JSON_Utils_Str_CharStrEscaping
import standard_library.internaldafny.generated.JSON_Utils_Str as JSON_Utils_Str
import standard_library.internaldafny.generated.JSON_Utils_Seq as JSON_Utils_Seq
import standard_library.internaldafny.generated.JSON_Utils_Vectors as JSON_Utils_Vectors
import standard_library.internaldafny.generated.JSON_Utils as JSON_Utils
import standard_library.internaldafny.generated.JSON_Errors as JSON_Errors
import standard_library.internaldafny.generated.JSON_Values as JSON_Values
import standard_library.internaldafny.generated.JSON_Spec as JSON_Spec
import standard_library.internaldafny.generated.JSON_Grammar as JSON_Grammar
import standard_library.internaldafny.generated.JSON_Serializer_ByteStrConversion as JSON_Serializer_ByteStrConversion
import standard_library.internaldafny.generated.JSON_Serializer as JSON_Serializer
import standard_library.internaldafny.generated.JSON_Deserializer_Uint16StrConversion as JSON_Deserializer_Uint16StrConversion
import standard_library.internaldafny.generated.JSON_Deserializer_ByteStrConversion as JSON_Deserializer_ByteStrConversion
import standard_library.internaldafny.generated.JSON_Deserializer as JSON_Deserializer

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
        d_641___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(ts)) == (0):
                    return (d_641___accumulator_) + (_dafny.Seq([]))
                elif True:
                    d_641___accumulator_ = (d_641___accumulator_) + (fT((ts)[0]))
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
        def lambda48_(d_642_obj_):
            def lambda49_(d_643_d_):
                return default__.Member(d_643_d_)

            return lambda49_

        return default__.Bracketed(obj, lambda48_(obj))

    @staticmethod
    def Array(arr):
        def lambda50_(d_644_arr_):
            def lambda51_(d_645_d_):
                return default__.Item(d_645_d_)

            return lambda51_

        return default__.Bracketed(arr, lambda50_(arr))

    @staticmethod
    def Value(self):
        source18_ = self
        unmatched18 = True
        if unmatched18:
            if source18_.is_Null:
                d_646_n_ = source18_.n
                unmatched18 = False
                return default__.View(d_646_n_)
        if unmatched18:
            if source18_.is_Bool:
                d_647_b_ = source18_.b
                unmatched18 = False
                return default__.View(d_647_b_)
        if unmatched18:
            if source18_.is_String:
                d_648_str_ = source18_.str
                unmatched18 = False
                return default__.String(d_648_str_)
        if unmatched18:
            if source18_.is_Number:
                d_649_num_ = source18_.num
                unmatched18 = False
                return default__.Number(d_649_num_)
        if unmatched18:
            if source18_.is_Object:
                d_650_obj_ = source18_.obj
                unmatched18 = False
                return default__.Object(d_650_obj_)
        if unmatched18:
            d_651_arr_ = source18_.arr
            unmatched18 = False
            return default__.Array(d_651_arr_)
        raise Exception("unexpected control point")

    @staticmethod
    def JSON(js):
        return default__.Structural(js, default__.Value)

