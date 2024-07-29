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
            d_239_elements_: _dafny.Seq
            out6_: _dafny.Seq
            out6_ = (self).ReadElements(n)
            d_239_elements_ = out6_
            res = Wrappers.Result_Success(d_239_elements_)
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
        d_240_mr_: SeqReader
        nw2_ = SeqReader()
        nw2_.ctor__(s)
        d_240_mr_ = nw2_
        (self)._reader = d_240_mr_

    def ReadByte(self):
        res: Wrappers.Result = Wrappers.Result.default(BoundedInts.uint8.default)()
        d_241_bytes_: _dafny.Seq
        d_242_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out7_: Wrappers.Result
        out7_ = ((self).reader).ReadExact(1)
        d_242_valueOrError0_ = out7_
        if (d_242_valueOrError0_).IsFailure():
            res = (d_242_valueOrError0_).PropagateFailure()
            return res
        d_241_bytes_ = (d_242_valueOrError0_).Extract()
        res = Wrappers.Result_Success((d_241_bytes_)[0])
        return res
        return res

    def ReadBytes(self, n):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_243_bytes_: _dafny.Seq
        d_244_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out8_: Wrappers.Result
        out8_ = ((self).reader).ReadExact(n)
        d_244_valueOrError0_ = out8_
        if (d_244_valueOrError0_).IsFailure():
            res = (d_244_valueOrError0_).PropagateFailure()
            return res
        d_243_bytes_ = (d_244_valueOrError0_).Extract()
        res = Wrappers.Result_Success(d_243_bytes_)
        return res
        return res

    def ReadUInt16(self):
        res: Wrappers.Result = Wrappers.Result.default(BoundedInts.uint16.default)()
        d_245_bytes_: _dafny.Seq
        d_246_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out9_: Wrappers.Result
        out9_ = ((self).reader).ReadExact(2)
        d_246_valueOrError0_ = out9_
        if (d_246_valueOrError0_).IsFailure():
            res = (d_246_valueOrError0_).PropagateFailure()
            return res
        d_245_bytes_ = (d_246_valueOrError0_).Extract()
        d_247_n_: int
        d_247_n_ = StandardLibrary_UInt.default__.SeqToUInt16(d_245_bytes_)
        res = Wrappers.Result_Success(d_247_n_)
        return res
        return res

    def ReadUInt32(self):
        res: Wrappers.Result = Wrappers.Result.default(BoundedInts.uint32.default)()
        d_248_bytes_: _dafny.Seq
        d_249_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out10_: Wrappers.Result
        out10_ = ((self).reader).ReadExact(4)
        d_249_valueOrError0_ = out10_
        if (d_249_valueOrError0_).IsFailure():
            res = (d_249_valueOrError0_).PropagateFailure()
            return res
        d_248_bytes_ = (d_249_valueOrError0_).Extract()
        d_250_n_: int
        d_250_n_ = StandardLibrary_UInt.default__.SeqToUInt32(d_248_bytes_)
        res = Wrappers.Result_Success(d_250_n_)
        return res
        return res

    def ReadUInt64(self):
        res: Wrappers.Result = Wrappers.Result.default(BoundedInts.uint64.default)()
        d_251_bytes_: _dafny.Seq
        d_252_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out11_: Wrappers.Result
        out11_ = ((self).reader).ReadExact(8)
        d_252_valueOrError0_ = out11_
        if (d_252_valueOrError0_).IsFailure():
            res = (d_252_valueOrError0_).PropagateFailure()
            return res
        d_251_bytes_ = (d_252_valueOrError0_).Extract()
        d_253_n_: int
        d_253_n_ = StandardLibrary_UInt.default__.SeqToUInt64(d_251_bytes_)
        res = Wrappers.Result_Success(d_253_n_)
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
        d_254_mw_: SeqWriter
        nw3_ = SeqWriter()
        nw3_.ctor__()
        d_254_mw_ = nw3_
        (self)._writer = d_254_mw_

    def WriteByte(self, n):
        r: int = int(0)
        out12_: int
        out12_ = ((self).writer).WriteElements(_dafny.Seq([n]))
        r = out12_
        return r

    def WriteBytes(self, s):
        r: int = int(0)
        out13_: int
        out13_ = ((self).writer).WriteElements(s)
        r = out13_
        return r

    def WriteUInt16(self, n):
        r: int = int(0)
        out14_: int
        out14_ = ((self).writer).WriteElements(StandardLibrary_UInt.default__.UInt16ToSeq(n))
        r = out14_
        return r

    def WriteUInt32(self, n):
        r: int = int(0)
        out15_: int
        out15_ = ((self).writer).WriteElements(StandardLibrary_UInt.default__.UInt32ToSeq(n))
        r = out15_
        return r

    def GetDataWritten(self):
        return (self).writer.data

    def GetSizeWritten(self):
        return len((self).writer.data)

    @property
    def writer(self):
        return self._writer
