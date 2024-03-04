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

# Module: JSON_ZeroCopy_Serializer

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Serialize(js):
        rbs: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.pointer)()
        d_675_writer_: JSON_Utils_Views_Writers.Writer__
        d_675_writer_ = default__.Text(js)
        d_676_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_676_valueOrError0_ = Wrappers.default__.Need((d_675_writer_).Unsaturated_q, JSON_Errors.SerializationError_OutOfMemory())
        if (d_676_valueOrError0_).IsFailure():
            rbs = (d_676_valueOrError0_).PropagateFailure()
            return rbs
        d_677_bs_: _dafny.Array
        out24_: _dafny.Array
        out24_ = (d_675_writer_).ToArray()
        d_677_bs_ = out24_
        rbs = Wrappers.Result_Success(d_677_bs_)
        return rbs
        return rbs

    @staticmethod
    def SerializeTo(js, dest):
        len: Wrappers.Result = Wrappers.Result.default(BoundedInts.uint32.default)()
        d_678_writer_: JSON_Utils_Views_Writers.Writer__
        d_678_writer_ = default__.Text(js)
        d_679_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_679_valueOrError0_ = Wrappers.default__.Need((d_678_writer_).Unsaturated_q, JSON_Errors.SerializationError_OutOfMemory())
        if (d_679_valueOrError0_).IsFailure():
            len = (d_679_valueOrError0_).PropagateFailure()
            return len
        d_680_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_680_valueOrError1_ = Wrappers.default__.Need(((d_678_writer_).length) <= ((dest).length(0)), JSON_Errors.SerializationError_OutOfMemory())
        if (d_680_valueOrError1_).IsFailure():
            len = (d_680_valueOrError1_).PropagateFailure()
            return len
        (d_678_writer_).CopyTo(dest)
        len = Wrappers.Result_Success((d_678_writer_).length)
        return len
        return len

    @staticmethod
    def Text(js):
        return default__.JSON(js, JSON_Utils_Views_Writers.Writer__.Empty)

    @staticmethod
    def JSON(js, writer):
        def lambda49_(d_681_js_):
            def lambda50_(d_682_wr_):
                return default__.Value((d_681_js_).t, d_682_wr_)

            return lambda50_

        return (((writer).Append((js).before)).Then(lambda49_(js))).Append((js).after)

    @staticmethod
    def Value(v, writer):
        source19_ = v
        if source19_.is_Null:
            d_683___mcc_h0_ = source19_.n
            d_684_n_ = d_683___mcc_h0_
            return (writer).Append(d_684_n_)
        elif source19_.is_Bool:
            d_685___mcc_h1_ = source19_.b
            d_686_b_ = d_685___mcc_h1_
            d_687_wr_ = (writer).Append(d_686_b_)
            return d_687_wr_
        elif source19_.is_String:
            d_688___mcc_h2_ = source19_.str
            d_689_str_ = d_688___mcc_h2_
            d_690_wr_ = default__.String(d_689_str_, writer)
            return d_690_wr_
        elif source19_.is_Number:
            d_691___mcc_h3_ = source19_.num
            d_692_num_ = d_691___mcc_h3_
            d_693_wr_ = default__.Number(d_692_num_, writer)
            return d_693_wr_
        elif source19_.is_Object:
            d_694___mcc_h4_ = source19_.obj
            d_695_obj_ = d_694___mcc_h4_
            d_696_wr_ = default__.Object(d_695_obj_, writer)
            return d_696_wr_
        elif True:
            d_697___mcc_h5_ = source19_.arr
            d_698_arr_ = d_697___mcc_h5_
            d_699_wr_ = default__.Array(d_698_arr_, writer)
            return d_699_wr_

    @staticmethod
    def String(str, writer):
        return (((writer).Append((str).lq)).Append((str).contents)).Append((str).rq)

    @staticmethod
    def Number(num, writer):
        d_700_wr_ = ((writer).Append((num).minus)).Append((num).num)
        d_701_wr_ = (((d_700_wr_).Append((((num).frac).t).period)).Append((((num).frac).t).num) if ((num).frac).is_NonEmpty else d_700_wr_)
        d_702_wr_ = ((((d_701_wr_).Append((((num).exp).t).e)).Append((((num).exp).t).sign)).Append((((num).exp).t).num) if ((num).exp).is_NonEmpty else d_701_wr_)
        return d_702_wr_

    @staticmethod
    def StructuralView(st, writer):
        return (((writer).Append((st).before)).Append((st).t)).Append((st).after)

    @staticmethod
    def Object(obj, writer):
        d_703_wr_ = default__.StructuralView((obj).l, writer)
        d_704_wr_ = default__.Members(obj, d_703_wr_)
        d_705_wr_ = default__.StructuralView((obj).r, d_704_wr_)
        return d_705_wr_

    @staticmethod
    def Array(arr, writer):
        d_706_wr_ = default__.StructuralView((arr).l, writer)
        d_707_wr_ = default__.Items(arr, d_706_wr_)
        d_708_wr_ = default__.StructuralView((arr).r, d_707_wr_)
        return d_708_wr_

    @staticmethod
    def Members(obj, writer):
        wr: JSON_Utils_Views_Writers.Writer__ = JSON_Utils_Views_Writers.Writer.default()
        out25_: JSON_Utils_Views_Writers.Writer__
        out25_ = default__.MembersImpl(obj, writer)
        wr = out25_
        return wr

    @staticmethod
    def Items(arr, writer):
        wr: JSON_Utils_Views_Writers.Writer__ = JSON_Utils_Views_Writers.Writer.default()
        out26_: JSON_Utils_Views_Writers.Writer__
        out26_ = default__.ItemsImpl(arr, writer)
        wr = out26_
        return wr

    @staticmethod
    def MembersImpl(obj, writer):
        wr: JSON_Utils_Views_Writers.Writer__ = JSON_Utils_Views_Writers.Writer.default()
        wr = writer
        d_709_members_: _dafny.Seq
        d_709_members_ = (obj).data
        hi9_ = len(d_709_members_)
        for d_710_i_ in range(0, hi9_):
            wr = default__.Member((d_709_members_)[d_710_i_], wr)
        return wr

    @staticmethod
    def ItemsImpl(arr, writer):
        wr: JSON_Utils_Views_Writers.Writer__ = JSON_Utils_Views_Writers.Writer.default()
        wr = writer
        d_711_items_: _dafny.Seq
        d_711_items_ = (arr).data
        hi10_ = len(d_711_items_)
        for d_712_i_ in range(0, hi10_):
            wr = default__.Item((d_711_items_)[d_712_i_], wr)
        return wr

    @staticmethod
    def Member(m, writer):
        d_713_wr_ = default__.String(((m).t).k, writer)
        d_714_wr_ = default__.StructuralView(((m).t).colon, d_713_wr_)
        d_715_wr_ = default__.Value(((m).t).v, d_714_wr_)
        d_716_wr_ = (d_715_wr_ if ((m).suffix).is_Empty else default__.StructuralView(((m).suffix).t, d_715_wr_))
        return d_716_wr_

    @staticmethod
    def Item(m, writer):
        d_717_wr_ = default__.Value((m).t, writer)
        d_718_wr_ = (d_717_wr_ if ((m).suffix).is_Empty else default__.StructuralView(((m).suffix).t, d_717_wr_))
        return d_718_wr_

