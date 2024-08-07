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

# Module: JSON_Utils_Views_Core

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Adjacent(lv, rv):
        return (((lv).end) == ((rv).beg)) and (((lv).s) == ((rv).s))

    @staticmethod
    def Merge(lv, rv):
        d_427_dt__update__tmp_h0_ = lv
        d_428_dt__update_hend_h0_ = (rv).end
        return View___View((d_427_dt__update__tmp_h0_).s, (d_427_dt__update__tmp_h0_).beg, d_428_dt__update_hend_h0_)


class View:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return View___View(_dafny.Seq([]), 0, 0)

class View__:
    @classmethod
    def default(cls, ):
        return lambda: View___View(_dafny.Seq({}), int(0), int(0))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_View(self) -> bool:
        return isinstance(self, View___View)
    def Length(self):
        return ((self).end) - ((self).beg)

    def Bytes(self):
        return _dafny.Seq(((self).s)[(self).beg:(self).end:])

    @staticmethod
    def OfBytes(bs):
        return View___View(bs, 0, len(bs))

    @staticmethod
    def OfString(s):
        return _dafny.Seq([ord((s)[d_429_i_]) for d_429_i_ in range(len(s))])

    def Byte_q(self, c):
        hresult_: bool = False
        hresult_ = (((self).Length()) == (1)) and (((self).At(0)) == (c))
        return hresult_
        return hresult_

    def Char_q(self, c):
        return (self).Byte_q(ord(c))

    def At(self, idx):
        return ((self).s)[((self).beg) + (idx)]

    def Peek(self):
        if (self).Empty_q:
            return -1
        elif True:
            return (self).At(0)

    def CopyTo(self, dest, start):
        hi7_ = (self).Length()
        for d_430_idx_ in range(0, hi7_):
            index0_ = (start) + (d_430_idx_)
            (dest)[index0_] = ((self).s)[((self).beg) + (d_430_idx_)]

    @_dafny.classproperty
    def Empty(instance):
        return View___View(_dafny.Seq([]), 0, 0)
    @property
    def Empty_q(self):
        return ((self).beg) == ((self).end)

class View___View(View__, NamedTuple('View', [('s', Any), ('beg', Any), ('end', Any)])):
    def __dafnystr__(self) -> str:
        return f'Core.View_.View({_dafny.string_of(self.s)}, {_dafny.string_of(self.beg)}, {_dafny.string_of(self.end)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, View___View) and self.s == __o.s and self.beg == __o.beg and self.end == __o.end
    def __hash__(self) -> int:
        return super().__hash__()

