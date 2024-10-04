import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import smithy_dafny_standard_library.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import smithy_dafny_standard_library.internaldafny.generated.Relations as Relations
import smithy_dafny_standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import smithy_dafny_standard_library.internaldafny.generated.Math as Math
import smithy_dafny_standard_library.internaldafny.generated.Seq as Seq
import smithy_dafny_standard_library.internaldafny.generated.BoundedInts as BoundedInts
import smithy_dafny_standard_library.internaldafny.generated.Unicode as Unicode
import smithy_dafny_standard_library.internaldafny.generated.Functions as Functions
import smithy_dafny_standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import smithy_dafny_standard_library.internaldafny.generated.FileIO as FileIO
import smithy_dafny_standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import smithy_dafny_standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.MulInternals as MulInternals
import smithy_dafny_standard_library.internaldafny.generated.Mul as Mul
import smithy_dafny_standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.ModInternals as ModInternals
import smithy_dafny_standard_library.internaldafny.generated.DivInternals as DivInternals
import smithy_dafny_standard_library.internaldafny.generated.DivMod as DivMod
import smithy_dafny_standard_library.internaldafny.generated.Power as Power
import smithy_dafny_standard_library.internaldafny.generated.Logarithm as Logarithm
import smithy_dafny_standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import smithy_dafny_standard_library.internaldafny.generated.UUID as UUID
import smithy_dafny_standard_library.internaldafny.generated.UTF8 as UTF8
import smithy_dafny_standard_library.internaldafny.generated.Time as Time
import smithy_dafny_standard_library.internaldafny.generated.Streams as Streams
import smithy_dafny_standard_library.internaldafny.generated.Sorting as Sorting
import smithy_dafny_standard_library.internaldafny.generated.SortedSets as SortedSets
import smithy_dafny_standard_library.internaldafny.generated.HexStrings as HexStrings
import smithy_dafny_standard_library.internaldafny.generated.GetOpt as GetOpt
import smithy_dafny_standard_library.internaldafny.generated.FloatCompare as FloatCompare
import smithy_dafny_standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import smithy_dafny_standard_library.internaldafny.generated.Base64 as Base64
import smithy_dafny_standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import smithy_dafny_standard_library.internaldafny.generated.Actions as Actions
import smithy_dafny_standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Views_Core as JSON_Utils_Views_Core
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Views_Writers as JSON_Utils_Views_Writers
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Views as JSON_Utils_Views
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Lexers_Core as JSON_Utils_Lexers_Core
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Lexers_Strings as JSON_Utils_Lexers_Strings
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Lexers as JSON_Utils_Lexers
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Cursors as JSON_Utils_Cursors
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Parsers as JSON_Utils_Parsers
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Str_CharStrConversion as JSON_Utils_Str_CharStrConversion
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Str_CharStrEscaping as JSON_Utils_Str_CharStrEscaping
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Str as JSON_Utils_Str
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Seq as JSON_Utils_Seq
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Vectors as JSON_Utils_Vectors
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils as JSON_Utils
import smithy_dafny_standard_library.internaldafny.generated.JSON_Errors as JSON_Errors
import smithy_dafny_standard_library.internaldafny.generated.JSON_Values as JSON_Values
import smithy_dafny_standard_library.internaldafny.generated.JSON_Spec as JSON_Spec
import smithy_dafny_standard_library.internaldafny.generated.JSON_Grammar as JSON_Grammar
import smithy_dafny_standard_library.internaldafny.generated.JSON_Serializer_ByteStrConversion as JSON_Serializer_ByteStrConversion
import smithy_dafny_standard_library.internaldafny.generated.JSON_Serializer as JSON_Serializer
import smithy_dafny_standard_library.internaldafny.generated.JSON_Deserializer_Uint16StrConversion as JSON_Deserializer_Uint16StrConversion
import smithy_dafny_standard_library.internaldafny.generated.JSON_Deserializer_ByteStrConversion as JSON_Deserializer_ByteStrConversion
import smithy_dafny_standard_library.internaldafny.generated.JSON_Deserializer as JSON_Deserializer
import smithy_dafny_standard_library.internaldafny.generated.JSON_ConcreteSyntax_Spec as JSON_ConcreteSyntax_Spec
import smithy_dafny_standard_library.internaldafny.generated.JSON_ConcreteSyntax_SpecProperties as JSON_ConcreteSyntax_SpecProperties
import smithy_dafny_standard_library.internaldafny.generated.JSON_ConcreteSyntax as JSON_ConcreteSyntax

# Module: JSON_ZeroCopy_Serializer

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Serialize(js):
        rbs: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.pointer)()
        d_0_writer_: JSON_Utils_Views_Writers.Writer__
        d_0_writer_ = default__.Text(js)
        d_1_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1_valueOrError0_ = Wrappers.default__.Need((d_0_writer_).Unsaturated_q, JSON_Errors.SerializationError_OutOfMemory())
        if (d_1_valueOrError0_).IsFailure():
            rbs = (d_1_valueOrError0_).PropagateFailure()
            return rbs
        d_2_bs_: _dafny.Array
        out0_: _dafny.Array
        out0_ = (d_0_writer_).ToArray()
        d_2_bs_ = out0_
        rbs = Wrappers.Result_Success(d_2_bs_)
        return rbs
        return rbs

    @staticmethod
    def SerializeTo(js, dest):
        len: Wrappers.Result = Wrappers.Result.default(BoundedInts.uint32.default)()
        d_0_writer_: JSON_Utils_Views_Writers.Writer__
        d_0_writer_ = default__.Text(js)
        d_1_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1_valueOrError0_ = Wrappers.default__.Need((d_0_writer_).Unsaturated_q, JSON_Errors.SerializationError_OutOfMemory())
        if (d_1_valueOrError0_).IsFailure():
            len = (d_1_valueOrError0_).PropagateFailure()
            return len
        d_2_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_2_valueOrError1_ = Wrappers.default__.Need(((d_0_writer_).length) <= ((dest).length(0)), JSON_Errors.SerializationError_OutOfMemory())
        if (d_2_valueOrError1_).IsFailure():
            len = (d_2_valueOrError1_).PropagateFailure()
            return len
        (d_0_writer_).CopyTo(dest)
        len = Wrappers.Result_Success((d_0_writer_).length)
        return len
        return len

    @staticmethod
    def Text(js):
        return default__.JSON(js, JSON_Utils_Views_Writers.Writer__.Empty)

    @staticmethod
    def JSON(js, writer):
        def lambda0_(d_0_js_):
            def lambda1_(d_1_wr_):
                return default__.Value((d_0_js_).t, d_1_wr_)

            return lambda1_

        return (((writer).Append((js).before)).Then(lambda0_(js))).Append((js).after)

    @staticmethod
    def Value(v, writer):
        source0_ = v
        if True:
            if source0_.is_Null:
                d_0_n_ = source0_.n
                return (writer).Append(d_0_n_)
        if True:
            if source0_.is_Bool:
                d_1_b_ = source0_.b
                d_2_wr_ = (writer).Append(d_1_b_)
                return d_2_wr_
        if True:
            if source0_.is_String:
                d_3_str_ = source0_.str
                d_4_wr_ = default__.String(d_3_str_, writer)
                return d_4_wr_
        if True:
            if source0_.is_Number:
                d_5_num_ = source0_.num
                d_6_wr_ = default__.Number(d_5_num_, writer)
                return d_6_wr_
        if True:
            if source0_.is_Object:
                d_7_obj_ = source0_.obj
                d_8_wr_ = default__.Object(d_7_obj_, writer)
                return d_8_wr_
        if True:
            d_9_arr_ = source0_.arr
            d_10_wr_ = default__.Array(d_9_arr_, writer)
            return d_10_wr_

    @staticmethod
    def String(str, writer):
        return (((writer).Append((str).lq)).Append((str).contents)).Append((str).rq)

    @staticmethod
    def Number(num, writer):
        d_0_wr_ = ((writer).Append((num).minus)).Append((num).num)
        d_1_wr_ = (((d_0_wr_).Append((((num).frac).t).period)).Append((((num).frac).t).num) if ((num).frac).is_NonEmpty else d_0_wr_)
        d_2_wr_ = ((((d_1_wr_).Append((((num).exp).t).e)).Append((((num).exp).t).sign)).Append((((num).exp).t).num) if ((num).exp).is_NonEmpty else d_1_wr_)
        return d_2_wr_

    @staticmethod
    def StructuralView(st, writer):
        return (((writer).Append((st).before)).Append((st).t)).Append((st).after)

    @staticmethod
    def Object(obj, writer):
        d_0_wr_ = default__.StructuralView((obj).l, writer)
        d_1_wr_ = default__.Members(obj, d_0_wr_)
        d_2_wr_ = default__.StructuralView((obj).r, d_1_wr_)
        return d_2_wr_

    @staticmethod
    def Array(arr, writer):
        d_0_wr_ = default__.StructuralView((arr).l, writer)
        d_1_wr_ = default__.Items(arr, d_0_wr_)
        d_2_wr_ = default__.StructuralView((arr).r, d_1_wr_)
        return d_2_wr_

    @staticmethod
    def Members(obj, writer):
        wr: JSON_Utils_Views_Writers.Writer__ = JSON_Utils_Views_Writers.Writer.default()
        out0_: JSON_Utils_Views_Writers.Writer__
        out0_ = default__.MembersImpl(obj, writer)
        wr = out0_
        return wr

    @staticmethod
    def Items(arr, writer):
        wr: JSON_Utils_Views_Writers.Writer__ = JSON_Utils_Views_Writers.Writer.default()
        out0_: JSON_Utils_Views_Writers.Writer__
        out0_ = default__.ItemsImpl(arr, writer)
        wr = out0_
        return wr

    @staticmethod
    def MembersImpl(obj, writer):
        wr: JSON_Utils_Views_Writers.Writer__ = JSON_Utils_Views_Writers.Writer.default()
        wr = writer
        d_0_members_: _dafny.Seq
        d_0_members_ = (obj).data
        hi0_ = len(d_0_members_)
        for d_1_i_ in range(0, hi0_):
            wr = default__.Member((d_0_members_)[d_1_i_], wr)
        return wr

    @staticmethod
    def ItemsImpl(arr, writer):
        wr: JSON_Utils_Views_Writers.Writer__ = JSON_Utils_Views_Writers.Writer.default()
        wr = writer
        d_0_items_: _dafny.Seq
        d_0_items_ = (arr).data
        hi0_ = len(d_0_items_)
        for d_1_i_ in range(0, hi0_):
            wr = default__.Item((d_0_items_)[d_1_i_], wr)
        return wr

    @staticmethod
    def Member(m, writer):
        d_0_wr_ = default__.String(((m).t).k, writer)
        d_1_wr_ = default__.StructuralView(((m).t).colon, d_0_wr_)
        d_2_wr_ = default__.Value(((m).t).v, d_1_wr_)
        d_3_wr_ = (d_2_wr_ if ((m).suffix).is_Empty else default__.StructuralView(((m).suffix).t, d_2_wr_))
        return d_3_wr_

    @staticmethod
    def Item(m, writer):
        d_0_wr_ = default__.Value((m).t, writer)
        d_1_wr_ = (d_0_wr_ if ((m).suffix).is_Empty else default__.StructuralView(((m).suffix).t, d_0_wr_))
        return d_1_wr_

