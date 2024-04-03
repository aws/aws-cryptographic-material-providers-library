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

# Module: JSON_Utils_Cursors


class Split:
    @classmethod
    def default(cls, default_T):
        return lambda: Split_SP(default_T(), FreshCursor.default())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_SP(self) -> bool:
        return isinstance(self, Split_SP)

class Split_SP(Split, NamedTuple('SP', [('t', Any), ('cs', Any)])):
    def __dafnystr__(self) -> str:
        return f'Cursors.Split.SP({_dafny.string_of(self.t)}, {_dafny.string_of(self.cs)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Split_SP) and self.t == __o.t and self.cs == __o.cs
    def __hash__(self) -> int:
        return super().__hash__()


class Cursor:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return Cursor___Cursor(_dafny.Seq([]), 0, 0, 0)

class FreshCursor:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return Cursor___Cursor(_dafny.Seq([]), 0, 0, 0)

class CursorError:
    @classmethod
    def default(cls, ):
        return lambda: CursorError_EOF()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_EOF(self) -> bool:
        return isinstance(self, CursorError_EOF)
    @property
    def is_ExpectingByte(self) -> bool:
        return isinstance(self, CursorError_ExpectingByte)
    @property
    def is_ExpectingAnyByte(self) -> bool:
        return isinstance(self, CursorError_ExpectingAnyByte)
    @property
    def is_OtherError(self) -> bool:
        return isinstance(self, CursorError_OtherError)
    def ToString(self, pr):
        source7_ = self
        if source7_.is_EOF:
            return _dafny.Seq("Reached EOF")
        elif source7_.is_ExpectingByte:
            d_446___mcc_h0_ = source7_.expected
            d_447___mcc_h1_ = source7_.b
            d_448_b_ = d_447___mcc_h1_
            d_449_b0_ = d_446___mcc_h0_
            d_450_c_ = (((_dafny.Seq("'")) + (_dafny.Seq([chr(d_448_b_)]))) + (_dafny.Seq("'")) if (d_448_b_) > (0) else _dafny.Seq("EOF"))
            return (((_dafny.Seq("Expecting '")) + (_dafny.Seq([chr(d_449_b0_)]))) + (_dafny.Seq("', read "))) + (d_450_c_)
        elif source7_.is_ExpectingAnyByte:
            d_451___mcc_h2_ = source7_.expected__sq
            d_452___mcc_h3_ = source7_.b
            d_453_b_ = d_452___mcc_h3_
            d_454_bs0_ = d_451___mcc_h2_
            d_455_c_ = (((_dafny.Seq("'")) + (_dafny.Seq([chr(d_453_b_)]))) + (_dafny.Seq("'")) if (d_453_b_) > (0) else _dafny.Seq("EOF"))
            d_456_c0s_ = _dafny.Seq([chr((d_454_bs0_)[d_457_idx_]) for d_457_idx_ in range(len(d_454_bs0_))])
            return (((_dafny.Seq("Expecting one of '")) + (d_456_c0s_)) + (_dafny.Seq("', read "))) + (d_455_c_)
        elif True:
            d_458___mcc_h4_ = source7_.err
            d_459_err_ = d_458___mcc_h4_
            return pr(d_459_err_)


class CursorError_EOF(CursorError, NamedTuple('EOF', [])):
    def __dafnystr__(self) -> str:
        return f'Cursors.CursorError.EOF'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CursorError_EOF)
    def __hash__(self) -> int:
        return super().__hash__()

class CursorError_ExpectingByte(CursorError, NamedTuple('ExpectingByte', [('expected', Any), ('b', Any)])):
    def __dafnystr__(self) -> str:
        return f'Cursors.CursorError.ExpectingByte({_dafny.string_of(self.expected)}, {_dafny.string_of(self.b)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CursorError_ExpectingByte) and self.expected == __o.expected and self.b == __o.b
    def __hash__(self) -> int:
        return super().__hash__()

class CursorError_ExpectingAnyByte(CursorError, NamedTuple('ExpectingAnyByte', [('expected__sq', Any), ('b', Any)])):
    def __dafnystr__(self) -> str:
        return f'Cursors.CursorError.ExpectingAnyByte({_dafny.string_of(self.expected__sq)}, {_dafny.string_of(self.b)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CursorError_ExpectingAnyByte) and self.expected__sq == __o.expected__sq and self.b == __o.b
    def __hash__(self) -> int:
        return super().__hash__()

class CursorError_OtherError(CursorError, NamedTuple('OtherError', [('err', Any)])):
    def __dafnystr__(self) -> str:
        return f'Cursors.CursorError.OtherError({_dafny.string_of(self.err)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CursorError_OtherError) and self.err == __o.err
    def __hash__(self) -> int:
        return super().__hash__()


class Cursor__:
    @classmethod
    def default(cls, ):
        return lambda: Cursor___Cursor(_dafny.Seq({}), int(0), int(0), int(0))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Cursor(self) -> bool:
        return isinstance(self, Cursor___Cursor)
    @staticmethod
    def OfView(v):
        return Cursor___Cursor((v).s, (v).beg, (v).beg, (v).end)

    @staticmethod
    def OfBytes(bs):
        return Cursor___Cursor(bs, 0, 0, len(bs))

    def Bytes(self):
        return _dafny.Seq(((self).s)[(self).beg:(self).end:])

    def Prefix(self):
        return JSON_Utils_Views_Core.View___View((self).s, (self).beg, (self).point)

    def Suffix(self):
        d_460_dt__update__tmp_h0_ = self
        d_461_dt__update_hbeg_h0_ = (self).point
        return Cursor___Cursor((d_460_dt__update__tmp_h0_).s, d_461_dt__update_hbeg_h0_, (d_460_dt__update__tmp_h0_).point, (d_460_dt__update__tmp_h0_).end)

    def Split(self):
        return Split_SP((self).Prefix(), (self).Suffix())

    def PrefixLength(self):
        return ((self).point) - ((self).beg)

    def SuffixLength(self):
        return ((self).end) - ((self).point)

    def Length(self):
        return ((self).end) - ((self).beg)

    def At(self, idx):
        return ((self).s)[((self).beg) + (idx)]

    def SuffixAt(self, idx):
        return ((self).s)[((self).point) + (idx)]

    def Peek(self):
        if (self).EOF_q:
            return -1
        elif True:
            return (self).SuffixAt(0)

    def LookingAt(self, c):
        return ((self).Peek()) == (ord(c))

    def Skip(self, n):
        d_462_dt__update__tmp_h0_ = self
        d_463_dt__update_hpoint_h0_ = ((self).point) + (n)
        return Cursor___Cursor((d_462_dt__update__tmp_h0_).s, (d_462_dt__update__tmp_h0_).beg, d_463_dt__update_hpoint_h0_, (d_462_dt__update__tmp_h0_).end)

    def Unskip(self, n):
        d_464_dt__update__tmp_h0_ = self
        d_465_dt__update_hpoint_h0_ = ((self).point) - (n)
        return Cursor___Cursor((d_464_dt__update__tmp_h0_).s, (d_464_dt__update__tmp_h0_).beg, d_465_dt__update_hpoint_h0_, (d_464_dt__update__tmp_h0_).end)

    def Get(self, err):
        if (self).EOF_q:
            return Wrappers.Result_Failure(CursorError_OtherError(err))
        elif True:
            return Wrappers.Result_Success((self).Skip(1))

    def AssertByte(self, b):
        d_466_nxt_ = (self).Peek()
        if (d_466_nxt_) == (b):
            return Wrappers.Result_Success((self).Skip(1))
        elif True:
            return Wrappers.Result_Failure(CursorError_ExpectingByte(b, d_466_nxt_))

    def AssertBytes(self, bs, offset):
        _this = self
        while True:
            with _dafny.label():
                if (offset) == (len(bs)):
                    return Wrappers.Result_Success(_this)
                elif True:
                    d_467_valueOrError0_ = (_this).AssertByte((bs)[offset])
                    if (d_467_valueOrError0_).IsFailure():
                        return (d_467_valueOrError0_).PropagateFailure()
                    elif True:
                        d_468_ps_ = (d_467_valueOrError0_).Extract()
                        in190_ = d_468_ps_
                        in191_ = bs
                        in192_ = (offset) + (1)
                        _this = in190_
                        
                        bs = in191_
                        offset = in192_
                        raise _dafny.TailCall()
                break

    def AssertChar(self, c0):
        return (self).AssertByte(ord(c0))

    def SkipByte(self):
        if (self).EOF_q:
            return self
        elif True:
            return (self).Skip(1)

    def SkipIf(self, p):
        if ((self).EOF_q) or (not(p((self).SuffixAt(0)))):
            return self
        elif True:
            return (self).Skip(1)

    def SkipWhile(self, p):
        ps: Cursor__ = Cursor.default()
        d_469_point_k_: int
        d_469_point_k_ = (self).point
        d_470_end_: int
        d_470_end_ = (self).end
        while ((d_469_point_k_) < (d_470_end_)) and (p(((self).s)[d_469_point_k_])):
            d_469_point_k_ = (d_469_point_k_) + (1)
        ps = Cursor___Cursor((self).s, (self).beg, d_469_point_k_, (self).end)
        return ps
        return ps

    def SkipWhileLexer(self, step, st):
        pr: Wrappers.Result = Wrappers.Result.default(Cursor.default)()
        d_471_point_k_: int
        d_471_point_k_ = (self).point
        d_472_end_: int
        d_472_end_ = (self).end
        d_473_st_k_: TypeVar('A__')
        d_473_st_k_ = st
        while True:
            d_474_eof_: bool
            d_474_eof_ = (d_471_point_k_) == (d_472_end_)
            d_475_minusone_: int
            d_475_minusone_ = -1
            d_476_c_: int
            d_476_c_ = (d_475_minusone_ if d_474_eof_ else ((self).s)[d_471_point_k_])
            source8_ = step(d_473_st_k_, d_476_c_)
            if source8_.is_Accept:
                pr = Wrappers.Result_Success(Cursor___Cursor((self).s, (self).beg, d_471_point_k_, (self).end))
                return pr
            elif source8_.is_Reject:
                d_477___mcc_h0_ = source8_.err
                d_478_err_ = d_477___mcc_h0_
                pr = Wrappers.Result_Failure(CursorError_OtherError(d_478_err_))
                return pr
            elif True:
                d_479___mcc_h1_ = source8_.st
                d_480_st_k_k_ = d_479___mcc_h1_
                if d_474_eof_:
                    pr = Wrappers.Result_Failure(CursorError_EOF())
                    return pr
                elif True:
                    d_473_st_k_ = d_480_st_k_k_
                    d_471_point_k_ = (d_471_point_k_) + (1)
        return pr

    @property
    def BOF_q(self):
        return ((self).point) == ((self).beg)
    @property
    def EOF_q(self):
        return ((self).point) == ((self).end)

class Cursor___Cursor(Cursor__, NamedTuple('Cursor', [('s', Any), ('beg', Any), ('point', Any), ('end', Any)])):
    def __dafnystr__(self) -> str:
        return f'Cursors.Cursor_.Cursor({_dafny.string_of(self.s)}, {_dafny.string_of(self.beg)}, {_dafny.string_of(self.point)}, {_dafny.string_of(self.end)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Cursor___Cursor) and self.s == __o.s and self.beg == __o.beg and self.point == __o.point and self.end == __o.end
    def __hash__(self) -> int:
        return super().__hash__()

