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
import standard_library.internaldafny.generated.JSON_ConcreteSyntax_Spec as JSON_ConcreteSyntax_Spec
import standard_library.internaldafny.generated.JSON_ConcreteSyntax_SpecProperties as JSON_ConcreteSyntax_SpecProperties
import standard_library.internaldafny.generated.JSON_ConcreteSyntax as JSON_ConcreteSyntax

# Module: standard_library.internaldafny.generated.JSON_ZeroCopy_Serializer

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Serialize(js):
        rbs: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.pointer)()
        d_701_writer_: JSON_Utils_Views_Writers.Writer__
        d_701_writer_ = default__.Text(js)
        d_702_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_702_valueOrError0_ = Wrappers.default__.Need((d_701_writer_).Unsaturated_q, JSON_Errors.SerializationError_OutOfMemory())
        if (d_702_valueOrError0_).IsFailure():
            rbs = (d_702_valueOrError0_).PropagateFailure()
            return rbs
        d_703_bs_: _dafny.Array
        out24_: _dafny.Array
        out24_ = (d_701_writer_).ToArray()
        d_703_bs_ = out24_
        rbs = Wrappers.Result_Success(d_703_bs_)
        return rbs
        return rbs

    @staticmethod
    def SerializeTo(js, dest):
        len: Wrappers.Result = Wrappers.Result.default(BoundedInts.uint32.default)()
        d_704_writer_: JSON_Utils_Views_Writers.Writer__
        d_704_writer_ = default__.Text(js)
        d_705_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_705_valueOrError0_ = Wrappers.default__.Need((d_704_writer_).Unsaturated_q, JSON_Errors.SerializationError_OutOfMemory())
        if (d_705_valueOrError0_).IsFailure():
            len = (d_705_valueOrError0_).PropagateFailure()
            return len
        d_706_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_706_valueOrError1_ = Wrappers.default__.Need(((d_704_writer_).length) <= ((dest).length(0)), JSON_Errors.SerializationError_OutOfMemory())
        if (d_706_valueOrError1_).IsFailure():
            len = (d_706_valueOrError1_).PropagateFailure()
            return len
        (d_704_writer_).CopyTo(dest)
        len = Wrappers.Result_Success((d_704_writer_).length)
        return len
        return len

    @staticmethod
    def Text(js):
        return default__.JSON(js, JSON_Utils_Views_Writers.Writer__.Empty)

    @staticmethod
    def JSON(js, writer):
        def lambda50_(d_707_js_):
            def lambda51_(d_708_wr_):
                return default__.Value((d_707_js_).t, d_708_wr_)

            return lambda51_

        return (((writer).Append((js).before)).Then(lambda50_(js))).Append((js).after)

    @staticmethod
    def Value(v, writer):
        source19_ = v
        if source19_.is_Null:
            d_709___mcc_h0_ = source19_.n
            d_710_n_ = d_709___mcc_h0_
            return (writer).Append(d_710_n_)
        elif source19_.is_Bool:
            d_711___mcc_h1_ = source19_.b
            d_712_b_ = d_711___mcc_h1_
            d_713_wr_ = (writer).Append(d_712_b_)
            return d_713_wr_
        elif source19_.is_String:
            d_714___mcc_h2_ = source19_.str
            d_715_str_ = d_714___mcc_h2_
            d_716_wr_ = default__.String(d_715_str_, writer)
            return d_716_wr_
        elif source19_.is_Number:
            d_717___mcc_h3_ = source19_.num
            d_718_num_ = d_717___mcc_h3_
            d_719_wr_ = default__.Number(d_718_num_, writer)
            return d_719_wr_
        elif source19_.is_Object:
            d_720___mcc_h4_ = source19_.obj
            d_721_obj_ = d_720___mcc_h4_
            d_722_wr_ = default__.Object(d_721_obj_, writer)
            return d_722_wr_
        elif True:
            d_723___mcc_h5_ = source19_.arr
            d_724_arr_ = d_723___mcc_h5_
            d_725_wr_ = default__.Array(d_724_arr_, writer)
            return d_725_wr_

    @staticmethod
    def String(str, writer):
        return (((writer).Append((str).lq)).Append((str).contents)).Append((str).rq)

    @staticmethod
    def Number(num, writer):
        d_726_wr_ = ((writer).Append((num).minus)).Append((num).num)
        d_727_wr_ = (((d_726_wr_).Append((((num).frac).t).period)).Append((((num).frac).t).num) if ((num).frac).is_NonEmpty else d_726_wr_)
        d_728_wr_ = ((((d_727_wr_).Append((((num).exp).t).e)).Append((((num).exp).t).sign)).Append((((num).exp).t).num) if ((num).exp).is_NonEmpty else d_727_wr_)
        return d_728_wr_

    @staticmethod
    def StructuralView(st, writer):
        return (((writer).Append((st).before)).Append((st).t)).Append((st).after)

    @staticmethod
    def Object(obj, writer):
        d_729_wr_ = default__.StructuralView((obj).l, writer)
        d_730_wr_ = default__.Members(obj, d_729_wr_)
        d_731_wr_ = default__.StructuralView((obj).r, d_730_wr_)
        return d_731_wr_

    @staticmethod
    def Array(arr, writer):
        d_732_wr_ = default__.StructuralView((arr).l, writer)
        d_733_wr_ = default__.Items(arr, d_732_wr_)
        d_734_wr_ = default__.StructuralView((arr).r, d_733_wr_)
        return d_734_wr_

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
        d_735_members_: _dafny.Seq
        d_735_members_ = (obj).data
        hi9_ = len(d_735_members_)
        for d_736_i_ in range(0, hi9_):
            wr = default__.Member((d_735_members_)[d_736_i_], wr)
        return wr

    @staticmethod
    def ItemsImpl(arr, writer):
        wr: JSON_Utils_Views_Writers.Writer__ = JSON_Utils_Views_Writers.Writer.default()
        wr = writer
        d_737_items_: _dafny.Seq
        d_737_items_ = (arr).data
        hi10_ = len(d_737_items_)
        for d_738_i_ in range(0, hi10_):
            wr = default__.Item((d_737_items_)[d_738_i_], wr)
        return wr

    @staticmethod
    def Member(m, writer):
        d_739_wr_ = default__.String(((m).t).k, writer)
        d_740_wr_ = default__.StructuralView(((m).t).colon, d_739_wr_)
        d_741_wr_ = default__.Value(((m).t).v, d_740_wr_)
        d_742_wr_ = (d_741_wr_ if ((m).suffix).is_Empty else default__.StructuralView(((m).suffix).t, d_741_wr_))
        return d_742_wr_

    @staticmethod
    def Item(m, writer):
        d_743_wr_ = default__.Value((m).t, writer)
        d_744_wr_ = (d_743_wr_ if ((m).suffix).is_Empty else default__.StructuralView(((m).suffix).t, d_743_wr_))
        return d_744_wr_

