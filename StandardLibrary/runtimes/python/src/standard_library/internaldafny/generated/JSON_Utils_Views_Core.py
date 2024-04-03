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

# Module: JSON_Utils_Views_Core

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Adjacent(lv, rv):
        return (((lv).end) == ((rv).beg)) and (((lv).s) == ((rv).s))

    @staticmethod
    def Merge(lv, rv):
        d_436_dt__update__tmp_h0_ = lv
        d_437_dt__update_hend_h0_ = (rv).end
        return View___View((d_436_dt__update__tmp_h0_).s, (d_436_dt__update__tmp_h0_).beg, d_437_dt__update_hend_h0_)


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
        return _dafny.Seq([ord((s)[d_438_i_]) for d_438_i_ in range(len(s))])

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
        for d_439_idx_ in range(0, hi7_):
            index0_ = (start) + (d_439_idx_)
            (dest)[index0_] = ((self).s)[((self).beg) + (d_439_idx_)]

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

