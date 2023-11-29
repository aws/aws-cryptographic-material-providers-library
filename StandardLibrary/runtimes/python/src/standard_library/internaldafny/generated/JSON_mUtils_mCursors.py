import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_mMergeSort
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
import StandardLibrary_mUInt
import String
import StandardLibrary
import UUID
import UTF8
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
import JSON_mUtils_mViews_mCore
import JSON_mUtils_mViews_mWriters
import JSON_mUtils_mViews
import JSON_mUtils_mLexers_mCore
import JSON_mUtils_mLexers_mStrings
import JSON_mUtils_mLexers

# assert "JSON_mUtils_mCursors" == __name__
JSON_mUtils_mCursors = sys.modules[__name__]


class Split:
    @classmethod
    def default(cls, default_T):
        return lambda: Split_SP(default_T(), JSON_mUtils_mCursors.FreshCursor.default())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_SP(self) -> bool:
        return isinstance(self, JSON_mUtils_mCursors.Split_SP)

class Split_SP(Split, NamedTuple('SP', [('t', Any), ('cs', Any)])):
    def __dafnystr__(self) -> str:
        return f'Cursors.Split.SP({_dafny.string_of(self.t)}, {_dafny.string_of(self.cs)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, JSON_mUtils_mCursors.Split_SP) and self.t == __o.t and self.cs == __o.cs
    def __hash__(self) -> int:
        return super().__hash__()


class Cursor:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return JSON_mUtils_mCursors.Cursor___Cursor(_dafny.Seq([]), 0, 0, 0)

class FreshCursor:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return JSON_mUtils_mCursors.Cursor___Cursor(_dafny.Seq([]), 0, 0, 0)

class CursorError:
    @classmethod
    def default(cls, ):
        return lambda: CursorError_EOF()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_EOF(self) -> bool:
        return isinstance(self, JSON_mUtils_mCursors.CursorError_EOF)
    @property
    def is_ExpectingByte(self) -> bool:
        return isinstance(self, JSON_mUtils_mCursors.CursorError_ExpectingByte)
    @property
    def is_ExpectingAnyByte(self) -> bool:
        return isinstance(self, JSON_mUtils_mCursors.CursorError_ExpectingAnyByte)
    @property
    def is_OtherError(self) -> bool:
        return isinstance(self, JSON_mUtils_mCursors.CursorError_OtherError)
    def ToString(self, pr):
        source7_ = self
        if source7_.is_EOF:
            return _dafny.Seq("Reached EOF")
        elif source7_.is_ExpectingByte:
            d_337___mcc_h0_ = source7_.expected
            d_338___mcc_h1_ = source7_.b
            d_339_b_ = d_338___mcc_h1_
            d_340_b0_ = d_337___mcc_h0_
            d_341_c_ = (((_dafny.Seq("'")) + (_dafny.Seq([chr(d_339_b_)]))) + (_dafny.Seq("'")) if (d_339_b_) > (0) else _dafny.Seq("EOF"))
            return (((_dafny.Seq("Expecting '")) + (_dafny.Seq([chr(d_340_b0_)]))) + (_dafny.Seq("', read "))) + (d_341_c_)
        elif source7_.is_ExpectingAnyByte:
            d_342___mcc_h2_ = source7_.expected__sq
            d_343___mcc_h3_ = source7_.b
            d_344_b_ = d_343___mcc_h3_
            d_345_bs0_ = d_342___mcc_h2_
            d_346_c_ = (((_dafny.Seq("'")) + (_dafny.Seq([chr(d_344_b_)]))) + (_dafny.Seq("'")) if (d_344_b_) > (0) else _dafny.Seq("EOF"))
            d_347_c0s_ = _dafny.Seq([chr((d_345_bs0_)[d_348_idx_]) for d_348_idx_ in range(len(d_345_bs0_))])
            return (((_dafny.Seq("Expecting one of '")) + (d_347_c0s_)) + (_dafny.Seq("', read "))) + (d_346_c_)
        elif True:
            d_349___mcc_h4_ = source7_.err
            d_350_err_ = d_349___mcc_h4_
            return pr(d_350_err_)


class CursorError_EOF(CursorError, NamedTuple('EOF', [])):
    def __dafnystr__(self) -> str:
        return f'Cursors.CursorError.EOF'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, JSON_mUtils_mCursors.CursorError_EOF)
    def __hash__(self) -> int:
        return super().__hash__()

class CursorError_ExpectingByte(CursorError, NamedTuple('ExpectingByte', [('expected', Any), ('b', Any)])):
    def __dafnystr__(self) -> str:
        return f'Cursors.CursorError.ExpectingByte({_dafny.string_of(self.expected)}, {_dafny.string_of(self.b)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, JSON_mUtils_mCursors.CursorError_ExpectingByte) and self.expected == __o.expected and self.b == __o.b
    def __hash__(self) -> int:
        return super().__hash__()

class CursorError_ExpectingAnyByte(CursorError, NamedTuple('ExpectingAnyByte', [('expected__sq', Any), ('b', Any)])):
    def __dafnystr__(self) -> str:
        return f'Cursors.CursorError.ExpectingAnyByte({_dafny.string_of(self.expected__sq)}, {_dafny.string_of(self.b)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, JSON_mUtils_mCursors.CursorError_ExpectingAnyByte) and self.expected__sq == __o.expected__sq and self.b == __o.b
    def __hash__(self) -> int:
        return super().__hash__()

class CursorError_OtherError(CursorError, NamedTuple('OtherError', [('err', Any)])):
    def __dafnystr__(self) -> str:
        return f'Cursors.CursorError.OtherError({_dafny.string_of(self.err)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, JSON_mUtils_mCursors.CursorError_OtherError) and self.err == __o.err
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
        return isinstance(self, JSON_mUtils_mCursors.Cursor___Cursor)
    @staticmethod
    def OfView(v):
        return JSON_mUtils_mCursors.Cursor___Cursor((v).s, (v).beg, (v).beg, (v).end)

    @staticmethod
    def OfBytes(bs):
        return JSON_mUtils_mCursors.Cursor___Cursor(bs, 0, 0, len(bs))

    def Bytes(self):
        return _dafny.Seq(((self).s)[(self).beg:(self).end:])

    def Prefix(self):
        return JSON_mUtils_mViews_mCore.View___View((self).s, (self).beg, (self).point)

    def Suffix(self):
        d_351_dt__update__tmp_h0_ = self
        d_352_dt__update_hbeg_h0_ = (self).point
        return JSON_mUtils_mCursors.Cursor___Cursor((d_351_dt__update__tmp_h0_).s, d_352_dt__update_hbeg_h0_, (d_351_dt__update__tmp_h0_).point, (d_351_dt__update__tmp_h0_).end)

    def Split(self):
        return JSON_mUtils_mCursors.Split_SP((self).Prefix(), (self).Suffix())

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
        d_353_dt__update__tmp_h0_ = self
        d_354_dt__update_hpoint_h0_ = ((self).point) + (n)
        return JSON_mUtils_mCursors.Cursor___Cursor((d_353_dt__update__tmp_h0_).s, (d_353_dt__update__tmp_h0_).beg, d_354_dt__update_hpoint_h0_, (d_353_dt__update__tmp_h0_).end)

    def Unskip(self, n):
        d_355_dt__update__tmp_h0_ = self
        d_356_dt__update_hpoint_h0_ = ((self).point) - (n)
        return JSON_mUtils_mCursors.Cursor___Cursor((d_355_dt__update__tmp_h0_).s, (d_355_dt__update__tmp_h0_).beg, d_356_dt__update_hpoint_h0_, (d_355_dt__update__tmp_h0_).end)

    def Get(self, err):
        if (self).EOF_q:
            return Wrappers.Result_Failure(JSON_mUtils_mCursors.CursorError_OtherError(err))
        elif True:
            return Wrappers.Result_Success((self).Skip(1))

    def assertByte(self, b):
        d_357_nxt_ = (self).Peek()
        if (d_357_nxt_) == (b):
            return Wrappers.Result_Success((self).Skip(1))
        elif True:
            return Wrappers.Result_Failure(JSON_mUtils_mCursors.CursorError_ExpectingByte(b, d_357_nxt_))

    def assertBytes(self, bs, offset):
        _this = self
        while True:
            with _dafny.label():
                if (offset) == (len(bs)):
                    return Wrappers.Result_Success(_this)
                elif True:
                    d_358_valueOrError0_ = (_this).assertByte((bs)[offset])
                    if (d_358_valueOrError0_).IsFailure():
                        return (d_358_valueOrError0_).PropagateFailure()
                    elif True:
                        d_359_ps_ = (d_358_valueOrError0_).Extract()
                        in87_ = d_359_ps_
                        in88_ = bs
                        in89_ = (offset) + (1)
                        _this = in87_
                        bs = in88_
                        offset = in89_
                        raise _dafny.TailCall()
                break

    def assertChar(self, c0):
        return (self).assertByte(ord(c0))

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
        ps: JSON_mUtils_mCursors.Cursor__ = JSON_mUtils_mCursors.Cursor.default()
        d_360_point_k_: BoundedInts.uint32
        d_360_point_k_ = (self).point
        d_361_end_: BoundedInts.uint32
        d_361_end_ = (self).end
        while ((d_360_point_k_) < (d_361_end_)) and (p(((self).s)[d_360_point_k_])):
            d_360_point_k_ = (d_360_point_k_) + (1)
        ps = JSON_mUtils_mCursors.Cursor___Cursor((self).s, (self).beg, d_360_point_k_, (self).end)
        return ps
        return ps

    def SkipWhileLexer(self, step, st):
        pr: Wrappers.Result = Wrappers.Result_Success.default(JSON_mUtils_mCursors.Cursor.default)()
        d_362_point_k_: BoundedInts.uint32
        d_362_point_k_ = (self).point
        d_363_end_: BoundedInts.uint32
        d_363_end_ = (self).end
        d_364_st_k_: TypeVar('A__')
        d_364_st_k_ = st
        while True:
            d_365_eof_: bool
            d_365_eof_ = (d_362_point_k_) == (d_363_end_)
            d_366_minusone_: BoundedInts.opt__byte
            d_366_minusone_ = -1
            d_367_c_: BoundedInts.opt__byte
            d_367_c_ = (d_366_minusone_ if d_365_eof_ else ((self).s)[d_362_point_k_])
            source8_ = step(d_364_st_k_, d_367_c_)
            if source8_.is_Accept:
                pr = Wrappers.Result_Success(JSON_mUtils_mCursors.Cursor___Cursor((self).s, (self).beg, d_362_point_k_, (self).end))
                return pr
            elif source8_.is_Reject:
                d_368___mcc_h0_ = source8_.err
                d_369_err_ = d_368___mcc_h0_
                pr = Wrappers.Result_Failure(JSON_mUtils_mCursors.CursorError_OtherError(d_369_err_))
                return pr
            elif True:
                d_370___mcc_h1_ = source8_.st
                d_371_st_k_k_ = d_370___mcc_h1_
                if d_365_eof_:
                    pr = Wrappers.Result_Failure(JSON_mUtils_mCursors.CursorError_EOF())
                    return pr
                elif True:
                    d_364_st_k_ = d_371_st_k_k_
                    d_362_point_k_ = (d_362_point_k_) + (1)
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
        return isinstance(__o, JSON_mUtils_mCursors.Cursor___Cursor) and self.s == __o.s and self.beg == __o.beg and self.point == __o.point and self.end == __o.end
    def __hash__(self) -> int:
        return super().__hash__()

