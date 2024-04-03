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
            d_248_elements_: _dafny.Seq
            out6_: _dafny.Seq
            out6_ = (self).ReadElements(n)
            d_248_elements_ = out6_
            res = Wrappers.Result_Success(d_248_elements_)
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
        d_249_mr_: SeqReader
        nw2_ = SeqReader()
        nw2_.ctor__(s)
        d_249_mr_ = nw2_
        (self)._reader = d_249_mr_

    def ReadByte(self):
        res: Wrappers.Result = Wrappers.Result.default(BoundedInts.uint8.default)()
        d_250_bytes_: _dafny.Seq
        d_251_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out7_: Wrappers.Result
        out7_ = ((self).reader).ReadExact(1)
        d_251_valueOrError0_ = out7_
        if (d_251_valueOrError0_).IsFailure():
            res = (d_251_valueOrError0_).PropagateFailure()
            return res
        d_250_bytes_ = (d_251_valueOrError0_).Extract()
        res = Wrappers.Result_Success((d_250_bytes_)[0])
        return res
        return res

    def ReadBytes(self, n):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_252_bytes_: _dafny.Seq
        d_253_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out8_: Wrappers.Result
        out8_ = ((self).reader).ReadExact(n)
        d_253_valueOrError0_ = out8_
        if (d_253_valueOrError0_).IsFailure():
            res = (d_253_valueOrError0_).PropagateFailure()
            return res
        d_252_bytes_ = (d_253_valueOrError0_).Extract()
        res = Wrappers.Result_Success(d_252_bytes_)
        return res
        return res

    def ReadUInt16(self):
        res: Wrappers.Result = Wrappers.Result.default(BoundedInts.uint16.default)()
        d_254_bytes_: _dafny.Seq
        d_255_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out9_: Wrappers.Result
        out9_ = ((self).reader).ReadExact(2)
        d_255_valueOrError0_ = out9_
        if (d_255_valueOrError0_).IsFailure():
            res = (d_255_valueOrError0_).PropagateFailure()
            return res
        d_254_bytes_ = (d_255_valueOrError0_).Extract()
        d_256_n_: int
        d_256_n_ = StandardLibrary_UInt.default__.SeqToUInt16(d_254_bytes_)
        res = Wrappers.Result_Success(d_256_n_)
        return res
        return res

    def ReadUInt32(self):
        res: Wrappers.Result = Wrappers.Result.default(BoundedInts.uint32.default)()
        d_257_bytes_: _dafny.Seq
        d_258_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out10_: Wrappers.Result
        out10_ = ((self).reader).ReadExact(4)
        d_258_valueOrError0_ = out10_
        if (d_258_valueOrError0_).IsFailure():
            res = (d_258_valueOrError0_).PropagateFailure()
            return res
        d_257_bytes_ = (d_258_valueOrError0_).Extract()
        d_259_n_: int
        d_259_n_ = StandardLibrary_UInt.default__.SeqToUInt32(d_257_bytes_)
        res = Wrappers.Result_Success(d_259_n_)
        return res
        return res

    def ReadUInt64(self):
        res: Wrappers.Result = Wrappers.Result.default(BoundedInts.uint64.default)()
        d_260_bytes_: _dafny.Seq
        d_261_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out11_: Wrappers.Result
        out11_ = ((self).reader).ReadExact(8)
        d_261_valueOrError0_ = out11_
        if (d_261_valueOrError0_).IsFailure():
            res = (d_261_valueOrError0_).PropagateFailure()
            return res
        d_260_bytes_ = (d_261_valueOrError0_).Extract()
        d_262_n_: int
        d_262_n_ = StandardLibrary_UInt.default__.SeqToUInt64(d_260_bytes_)
        res = Wrappers.Result_Success(d_262_n_)
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
        d_263_mw_: SeqWriter
        nw3_ = SeqWriter()
        nw3_.ctor__()
        d_263_mw_ = nw3_
        (self)._writer = d_263_mw_

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
