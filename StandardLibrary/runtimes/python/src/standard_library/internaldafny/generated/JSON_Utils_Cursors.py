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
        if True:
            if source7_.is_EOF:
                return _dafny.Seq("Reached EOF")
        if True:
            if source7_.is_ExpectingByte:
                d_436_b0_ = source7_.expected
                d_437_b_ = source7_.b
                d_438_c_ = (((_dafny.Seq("'")) + (_dafny.Seq([chr(d_437_b_)]))) + (_dafny.Seq("'")) if (d_437_b_) > (0) else _dafny.Seq("EOF"))
                return (((_dafny.Seq("Expecting '")) + (_dafny.Seq([chr(d_436_b0_)]))) + (_dafny.Seq("', read "))) + (d_438_c_)
        if True:
            if source7_.is_ExpectingAnyByte:
                d_439_bs0_ = source7_.expected__sq
                d_440_b_ = source7_.b
                d_441_c_ = (((_dafny.Seq("'")) + (_dafny.Seq([chr(d_440_b_)]))) + (_dafny.Seq("'")) if (d_440_b_) > (0) else _dafny.Seq("EOF"))
                d_442_c0s_ = _dafny.Seq([chr((d_439_bs0_)[d_443_idx_]) for d_443_idx_ in range(len(d_439_bs0_))])
                return (((_dafny.Seq("Expecting one of '")) + (d_442_c0s_)) + (_dafny.Seq("', read "))) + (d_441_c_)
        if True:
            d_444_err_ = source7_.err
            return pr(d_444_err_)


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
        d_445_dt__update__tmp_h0_ = self
        d_446_dt__update_hbeg_h0_ = (self).point
        return Cursor___Cursor((d_445_dt__update__tmp_h0_).s, d_446_dt__update_hbeg_h0_, (d_445_dt__update__tmp_h0_).point, (d_445_dt__update__tmp_h0_).end)

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
        d_447_dt__update__tmp_h0_ = self
        d_448_dt__update_hpoint_h0_ = ((self).point) + (n)
        return Cursor___Cursor((d_447_dt__update__tmp_h0_).s, (d_447_dt__update__tmp_h0_).beg, d_448_dt__update_hpoint_h0_, (d_447_dt__update__tmp_h0_).end)

    def Unskip(self, n):
        d_449_dt__update__tmp_h0_ = self
        d_450_dt__update_hpoint_h0_ = ((self).point) - (n)
        return Cursor___Cursor((d_449_dt__update__tmp_h0_).s, (d_449_dt__update__tmp_h0_).beg, d_450_dt__update_hpoint_h0_, (d_449_dt__update__tmp_h0_).end)

    def Get(self, err):
        if (self).EOF_q:
            return Wrappers.Result_Failure(CursorError_OtherError(err))
        elif True:
            return Wrappers.Result_Success((self).Skip(1))

    def AssertByte(self, b):
        d_451_nxt_ = (self).Peek()
        if (d_451_nxt_) == (b):
            return Wrappers.Result_Success((self).Skip(1))
        elif True:
            return Wrappers.Result_Failure(CursorError_ExpectingByte(b, d_451_nxt_))

    def AssertBytes(self, bs, offset):
        _this = self
        while True:
            with _dafny.label():
                if (offset) == (len(bs)):
                    return Wrappers.Result_Success(_this)
                elif True:
                    d_452_valueOrError0_ = (_this).AssertByte((bs)[offset])
                    if (d_452_valueOrError0_).IsFailure():
                        return (d_452_valueOrError0_).PropagateFailure()
                    elif True:
                        d_453_ps_ = (d_452_valueOrError0_).Extract()
                        in190_ = d_453_ps_
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
        d_454_point_k_: int
        d_454_point_k_ = (self).point
        d_455_end_: int
        d_455_end_ = (self).end
        while ((d_454_point_k_) < (d_455_end_)) and (p(((self).s)[d_454_point_k_])):
            d_454_point_k_ = (d_454_point_k_) + (1)
        ps = Cursor___Cursor((self).s, (self).beg, d_454_point_k_, (self).end)
        return ps
        return ps

    def SkipWhileLexer(self, step, st):
        pr: Wrappers.Result = Wrappers.Result.default(Cursor.default)()
        d_456_point_k_: int
        d_456_point_k_ = (self).point
        d_457_end_: int
        d_457_end_ = (self).end
        d_458_st_k_: TypeVar('A__')
        d_458_st_k_ = st
        while True:
            d_459_eof_: bool
            d_459_eof_ = (d_456_point_k_) == (d_457_end_)
            d_460_minusone_: int
            d_460_minusone_ = -1
            d_461_c_: int
            if d_459_eof_:
                d_461_c_ = d_460_minusone_
            elif True:
                d_461_c_ = ((self).s)[d_456_point_k_]
            source8_ = step(d_458_st_k_, d_461_c_)
            with _dafny.label("match0"):
                if True:
                    if source8_.is_Accept:
                        pr = Wrappers.Result_Success(Cursor___Cursor((self).s, (self).beg, d_456_point_k_, (self).end))
                        return pr
                        raise _dafny.Break("match0")
                if True:
                    if source8_.is_Reject:
                        d_462_err_ = source8_.err
                        pr = Wrappers.Result_Failure(CursorError_OtherError(d_462_err_))
                        return pr
                        raise _dafny.Break("match0")
                if True:
                    d_463_st_k_k_ = source8_.st
                    if d_459_eof_:
                        pr = Wrappers.Result_Failure(CursorError_EOF())
                        return pr
                    elif True:
                        d_458_st_k_ = d_463_st_k_k_
                        d_456_point_k_ = (d_456_point_k_) + (1)
                pass
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

