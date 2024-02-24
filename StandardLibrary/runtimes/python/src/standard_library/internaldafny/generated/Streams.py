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
            d_231_elements_: _dafny.Seq
            out6_: _dafny.Seq
            out6_ = (self).ReadElements(n)
            d_231_elements_ = out6_
            res = Wrappers.Result_Success(d_231_elements_)
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
        d_232_mr_: SeqReader
        nw2_ = SeqReader()
        nw2_.ctor__(s)
        d_232_mr_ = nw2_
        (self)._reader = d_232_mr_

    def ReadByte(self):
        res: Wrappers.Result = Wrappers.Result.default(BoundedInts.uint8.default)()
        d_233_bytes_: _dafny.Seq
        d_234_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out7_: Wrappers.Result
        out7_ = ((self).reader).ReadExact(1)
        d_234_valueOrError0_ = out7_
        if (d_234_valueOrError0_).IsFailure():
            res = (d_234_valueOrError0_).PropagateFailure()
            return res
        d_233_bytes_ = (d_234_valueOrError0_).Extract()
        res = Wrappers.Result_Success((d_233_bytes_)[0])
        return res
        return res

    def ReadBytes(self, n):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_235_bytes_: _dafny.Seq
        d_236_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out8_: Wrappers.Result
        out8_ = ((self).reader).ReadExact(n)
        d_236_valueOrError0_ = out8_
        if (d_236_valueOrError0_).IsFailure():
            res = (d_236_valueOrError0_).PropagateFailure()
            return res
        d_235_bytes_ = (d_236_valueOrError0_).Extract()
        res = Wrappers.Result_Success(d_235_bytes_)
        return res
        return res

    def ReadUInt16(self):
        res: Wrappers.Result = Wrappers.Result.default(BoundedInts.uint16.default)()
        d_237_bytes_: _dafny.Seq
        d_238_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out9_: Wrappers.Result
        out9_ = ((self).reader).ReadExact(2)
        d_238_valueOrError0_ = out9_
        if (d_238_valueOrError0_).IsFailure():
            res = (d_238_valueOrError0_).PropagateFailure()
            return res
        d_237_bytes_ = (d_238_valueOrError0_).Extract()
        d_239_n_: int
        d_239_n_ = StandardLibrary_UInt.default__.SeqToUInt16(d_237_bytes_)
        res = Wrappers.Result_Success(d_239_n_)
        return res
        return res

    def ReadUInt32(self):
        res: Wrappers.Result = Wrappers.Result.default(BoundedInts.uint32.default)()
        d_240_bytes_: _dafny.Seq
        d_241_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out10_: Wrappers.Result
        out10_ = ((self).reader).ReadExact(4)
        d_241_valueOrError0_ = out10_
        if (d_241_valueOrError0_).IsFailure():
            res = (d_241_valueOrError0_).PropagateFailure()
            return res
        d_240_bytes_ = (d_241_valueOrError0_).Extract()
        d_242_n_: int
        d_242_n_ = StandardLibrary_UInt.default__.SeqToUInt32(d_240_bytes_)
        res = Wrappers.Result_Success(d_242_n_)
        return res
        return res

    def ReadUInt64(self):
        res: Wrappers.Result = Wrappers.Result.default(BoundedInts.uint64.default)()
        d_243_bytes_: _dafny.Seq
        d_244_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out11_: Wrappers.Result
        out11_ = ((self).reader).ReadExact(8)
        d_244_valueOrError0_ = out11_
        if (d_244_valueOrError0_).IsFailure():
            res = (d_244_valueOrError0_).PropagateFailure()
            return res
        d_243_bytes_ = (d_244_valueOrError0_).Extract()
        d_245_n_: int
        d_245_n_ = StandardLibrary_UInt.default__.SeqToUInt64(d_243_bytes_)
        res = Wrappers.Result_Success(d_245_n_)
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
        d_246_mw_: SeqWriter
        nw3_ = SeqWriter()
        nw3_.ctor__()
        d_246_mw_ = nw3_
        (self)._writer = d_246_mw_

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
