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

# Module: JSON_Utils_Views_Core

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Adjacent(lv, rv):
        return (((lv).end) == ((rv).beg)) and (((lv).s) == ((rv).s))

    @staticmethod
    def Merge(lv, rv):
        d_0_dt__update__tmp_h0_ = lv
        d_1_dt__update_hend_h0_ = (rv).end
        return View___View((d_0_dt__update__tmp_h0_).s, (d_0_dt__update__tmp_h0_).beg, d_1_dt__update_hend_h0_)


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
        return _dafny.Seq([ord((s)[d_0_i_]) for d_0_i_ in range(len(s))])

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
        hi0_ = (self).Length()
        for d_0_idx_ in range(0, hi0_):
            index0_ = (start) + (d_0_idx_)
            (dest)[index0_] = ((self).s)[((self).beg) + (d_0_idx_)]

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

