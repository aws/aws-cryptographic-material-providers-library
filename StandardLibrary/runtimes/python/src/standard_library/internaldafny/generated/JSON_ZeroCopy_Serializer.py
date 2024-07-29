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

# Module: JSON_ZeroCopy_Serializer

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Serialize(js):
        rbs: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.pointer)()
        d_648_writer_: JSON_Utils_Views_Writers.Writer__
        d_648_writer_ = default__.Text(js)
        d_649_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_649_valueOrError0_ = Wrappers.default__.Need((d_648_writer_).Unsaturated_q, JSON_Errors.SerializationError_OutOfMemory())
        if (d_649_valueOrError0_).IsFailure():
            rbs = (d_649_valueOrError0_).PropagateFailure()
            return rbs
        d_650_bs_: _dafny.Array
        out24_: _dafny.Array
        out24_ = (d_648_writer_).ToArray()
        d_650_bs_ = out24_
        rbs = Wrappers.Result_Success(d_650_bs_)
        return rbs
        return rbs

    @staticmethod
    def SerializeTo(js, dest):
        len: Wrappers.Result = Wrappers.Result.default(BoundedInts.uint32.default)()
        d_651_writer_: JSON_Utils_Views_Writers.Writer__
        d_651_writer_ = default__.Text(js)
        d_652_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_652_valueOrError0_ = Wrappers.default__.Need((d_651_writer_).Unsaturated_q, JSON_Errors.SerializationError_OutOfMemory())
        if (d_652_valueOrError0_).IsFailure():
            len = (d_652_valueOrError0_).PropagateFailure()
            return len
        d_653_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_653_valueOrError1_ = Wrappers.default__.Need(((d_651_writer_).length) <= ((dest).length(0)), JSON_Errors.SerializationError_OutOfMemory())
        if (d_653_valueOrError1_).IsFailure():
            len = (d_653_valueOrError1_).PropagateFailure()
            return len
        (d_651_writer_).CopyTo(dest)
        len = Wrappers.Result_Success((d_651_writer_).length)
        return len
        return len

    @staticmethod
    def Text(js):
        return default__.JSON(js, JSON_Utils_Views_Writers.Writer__.Empty)

    @staticmethod
    def JSON(js, writer):
        def lambda52_(d_654_js_):
            def lambda53_(d_655_wr_):
                return default__.Value((d_654_js_).t, d_655_wr_)

            return lambda53_

        return (((writer).Append((js).before)).Then(lambda52_(js))).Append((js).after)

    @staticmethod
    def Value(v, writer):
        pat_let_tv16_ = writer
        pat_let_tv17_ = writer
        pat_let_tv18_ = writer
        pat_let_tv19_ = writer
        pat_let_tv20_ = writer
        pat_let_tv21_ = writer
        source19_ = v
        unmatched19 = True
        if unmatched19:
            if source19_.is_Null:
                d_656_n_ = source19_.n
                unmatched19 = False
                return (pat_let_tv16_).Append(d_656_n_)
        if unmatched19:
            if source19_.is_Bool:
                d_657_b_ = source19_.b
                unmatched19 = False
                d_658_wr_ = (pat_let_tv17_).Append(d_657_b_)
                return d_658_wr_
        if unmatched19:
            if source19_.is_String:
                d_659_str_ = source19_.str
                unmatched19 = False
                d_660_wr_ = default__.String(d_659_str_, pat_let_tv18_)
                return d_660_wr_
        if unmatched19:
            if source19_.is_Number:
                d_661_num_ = source19_.num
                unmatched19 = False
                d_662_wr_ = default__.Number(d_661_num_, pat_let_tv19_)
                return d_662_wr_
        if unmatched19:
            if source19_.is_Object:
                d_663_obj_ = source19_.obj
                unmatched19 = False
                d_664_wr_ = default__.Object(d_663_obj_, pat_let_tv20_)
                return d_664_wr_
        if unmatched19:
            d_665_arr_ = source19_.arr
            unmatched19 = False
            d_666_wr_ = default__.Array(d_665_arr_, pat_let_tv21_)
            return d_666_wr_
        raise Exception("unexpected control point")

    @staticmethod
    def String(str, writer):
        return (((writer).Append((str).lq)).Append((str).contents)).Append((str).rq)

    @staticmethod
    def Number(num, writer):
        d_667_wr_ = ((writer).Append((num).minus)).Append((num).num)
        d_668_wr_ = (((d_667_wr_).Append((((num).frac).t).period)).Append((((num).frac).t).num) if ((num).frac).is_NonEmpty else d_667_wr_)
        d_669_wr_ = ((((d_668_wr_).Append((((num).exp).t).e)).Append((((num).exp).t).sign)).Append((((num).exp).t).num) if ((num).exp).is_NonEmpty else d_668_wr_)
        return d_669_wr_

    @staticmethod
    def StructuralView(st, writer):
        return (((writer).Append((st).before)).Append((st).t)).Append((st).after)

    @staticmethod
    def Object(obj, writer):
        d_670_wr_ = default__.StructuralView((obj).l, writer)
        d_671_wr_ = default__.Members(obj, d_670_wr_)
        d_672_wr_ = default__.StructuralView((obj).r, d_671_wr_)
        return d_672_wr_

    @staticmethod
    def Array(arr, writer):
        d_673_wr_ = default__.StructuralView((arr).l, writer)
        d_674_wr_ = default__.Items(arr, d_673_wr_)
        d_675_wr_ = default__.StructuralView((arr).r, d_674_wr_)
        return d_675_wr_

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
        d_676_members_: _dafny.Seq
        d_676_members_ = (obj).data
        hi9_ = len(d_676_members_)
        for d_677_i_ in range(0, hi9_):
            wr = default__.Member((d_676_members_)[d_677_i_], wr)
        return wr

    @staticmethod
    def ItemsImpl(arr, writer):
        wr: JSON_Utils_Views_Writers.Writer__ = JSON_Utils_Views_Writers.Writer.default()
        wr = writer
        d_678_items_: _dafny.Seq
        d_678_items_ = (arr).data
        hi10_ = len(d_678_items_)
        for d_679_i_ in range(0, hi10_):
            wr = default__.Item((d_678_items_)[d_679_i_], wr)
        return wr

    @staticmethod
    def Member(m, writer):
        d_680_wr_ = default__.String(((m).t).k, writer)
        d_681_wr_ = default__.StructuralView(((m).t).colon, d_680_wr_)
        d_682_wr_ = default__.Value(((m).t).v, d_681_wr_)
        d_683_wr_ = (d_682_wr_ if ((m).suffix).is_Empty else default__.StructuralView(((m).suffix).t, d_682_wr_))
        return d_683_wr_

    @staticmethod
    def Item(m, writer):
        d_684_wr_ = default__.Value((m).t, writer)
        d_685_wr_ = (d_684_wr_ if ((m).suffix).is_Empty else default__.StructuralView(((m).suffix).t, d_684_wr_))
        return d_685_wr_

