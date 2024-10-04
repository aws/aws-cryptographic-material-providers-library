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

# Module: Streams


class SeqReader:
    def  __init__(self):
        self.pos: int = int(0)
        self._data: _dafny.Seq = _dafny.Seq({})
        pass

    def __dafnystr__(self) -> str:
        return "Streams.SeqReader"
    def ctor__(self, s):
        (self)._data = s
        (self).pos = 0

    def ReadElements(self, n):
        elems: _dafny.Seq = _dafny.Seq({})
        elems = _dafny.Seq((_dafny.Seq(((self).data)[self.pos::]))[:n:])
        (self).pos = (self.pos) + (n)
        elems = elems
        return elems
        return elems

    def ReadExact(self, n):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        if (n) > ((len((self).data)) - (self.pos)):
            res = Wrappers.Result_Failure(_dafny.Seq("IO Error: Not enough elements left on stream."))
            return res
        elif True:
            d_0_elements_: _dafny.Seq
            out0_: _dafny.Seq
            out0_ = (self).ReadElements(n)
            d_0_elements_ = out0_
            res = Wrappers.Result_Success(d_0_elements_)
            return res
        return res

    @property
    def data(self):
        return self._data

class ByteReader:
    def  __init__(self):
        self._reader: SeqReader = None
        pass

    def __dafnystr__(self) -> str:
        return "Streams.ByteReader"
    def ctor__(self, s):
        d_0_mr_: SeqReader
        nw0_ = SeqReader()
        nw0_.ctor__(s)
        d_0_mr_ = nw0_
        (self)._reader = d_0_mr_

    def ReadByte(self):
        res: Wrappers.Result = Wrappers.Result.default(BoundedInts.uint8.default)()
        d_0_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out0_: Wrappers.Result
        out0_ = ((self).reader).ReadExact(1)
        d_0_valueOrError0_ = out0_
        if (d_0_valueOrError0_).IsFailure():
            res = (d_0_valueOrError0_).PropagateFailure()
            return res
        d_1_bytes_: _dafny.Seq
        d_1_bytes_ = (d_0_valueOrError0_).Extract()
        res = Wrappers.Result_Success((d_1_bytes_)[0])
        return res
        return res

    def ReadBytes(self, n):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_0_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out0_: Wrappers.Result
        out0_ = ((self).reader).ReadExact(n)
        d_0_valueOrError0_ = out0_
        if (d_0_valueOrError0_).IsFailure():
            res = (d_0_valueOrError0_).PropagateFailure()
            return res
        d_1_bytes_: _dafny.Seq
        d_1_bytes_ = (d_0_valueOrError0_).Extract()
        res = Wrappers.Result_Success(d_1_bytes_)
        return res
        return res

    def ReadUInt16(self):
        res: Wrappers.Result = Wrappers.Result.default(BoundedInts.uint16.default)()
        d_0_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out0_: Wrappers.Result
        out0_ = ((self).reader).ReadExact(2)
        d_0_valueOrError0_ = out0_
        if (d_0_valueOrError0_).IsFailure():
            res = (d_0_valueOrError0_).PropagateFailure()
            return res
        d_1_bytes_: _dafny.Seq
        d_1_bytes_ = (d_0_valueOrError0_).Extract()
        d_2_n_: int
        d_2_n_ = StandardLibrary_UInt.default__.SeqToUInt16(d_1_bytes_)
        res = Wrappers.Result_Success(d_2_n_)
        return res
        return res

    def ReadUInt32(self):
        res: Wrappers.Result = Wrappers.Result.default(BoundedInts.uint32.default)()
        d_0_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out0_: Wrappers.Result
        out0_ = ((self).reader).ReadExact(4)
        d_0_valueOrError0_ = out0_
        if (d_0_valueOrError0_).IsFailure():
            res = (d_0_valueOrError0_).PropagateFailure()
            return res
        d_1_bytes_: _dafny.Seq
        d_1_bytes_ = (d_0_valueOrError0_).Extract()
        d_2_n_: int
        d_2_n_ = StandardLibrary_UInt.default__.SeqToUInt32(d_1_bytes_)
        res = Wrappers.Result_Success(d_2_n_)
        return res
        return res

    def ReadUInt64(self):
        res: Wrappers.Result = Wrappers.Result.default(BoundedInts.uint64.default)()
        d_0_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out0_: Wrappers.Result
        out0_ = ((self).reader).ReadExact(8)
        d_0_valueOrError0_ = out0_
        if (d_0_valueOrError0_).IsFailure():
            res = (d_0_valueOrError0_).PropagateFailure()
            return res
        d_1_bytes_: _dafny.Seq
        d_1_bytes_ = (d_0_valueOrError0_).Extract()
        d_2_n_: int
        d_2_n_ = StandardLibrary_UInt.default__.SeqToUInt64(d_1_bytes_)
        res = Wrappers.Result_Success(d_2_n_)
        return res
        return res

    def IsDoneReading(self):
        b: bool = False
        b = (len(((self).reader).data)) == ((self).reader.pos)
        return b
        return b

    def GetSizeRead(self):
        n: int = int(0)
        n = (self).reader.pos
        return n
        return n

    @property
    def reader(self):
        return self._reader

class SeqWriter:
    def  __init__(self):
        self.data: _dafny.Seq = _dafny.Seq({})
        pass

    def __dafnystr__(self) -> str:
        return "Streams.SeqWriter"
    def ctor__(self):
        (self).data = _dafny.Seq([])

    def WriteElements(self, elems):
        n: int = int(0)
        (self).data = (self.data) + (elems)
        n = len(elems)
        return n
        return n


class ByteWriter:
    def  __init__(self):
        self._writer: SeqWriter = None
        pass

    def __dafnystr__(self) -> str:
        return "Streams.ByteWriter"
    def ctor__(self):
        d_0_mw_: SeqWriter
        nw0_ = SeqWriter()
        nw0_.ctor__()
        d_0_mw_ = nw0_
        (self)._writer = d_0_mw_

    def WriteByte(self, n):
        r: int = int(0)
        out0_: int
        out0_ = ((self).writer).WriteElements(_dafny.Seq([n]))
        r = out0_
        return r

    def WriteBytes(self, s):
        r: int = int(0)
        out0_: int
        out0_ = ((self).writer).WriteElements(s)
        r = out0_
        return r

    def WriteUInt16(self, n):
        r: int = int(0)
        out0_: int
        out0_ = ((self).writer).WriteElements(StandardLibrary_UInt.default__.UInt16ToSeq(n))
        r = out0_
        return r

    def WriteUInt32(self, n):
        r: int = int(0)
        out0_: int
        out0_ = ((self).writer).WriteElements(StandardLibrary_UInt.default__.UInt32ToSeq(n))
        r = out0_
        return r

    def GetDataWritten(self):
        return (self).writer.data

    def GetSizeWritten(self):
        return len((self).writer.data)

    @property
    def writer(self):
        return self._writer
