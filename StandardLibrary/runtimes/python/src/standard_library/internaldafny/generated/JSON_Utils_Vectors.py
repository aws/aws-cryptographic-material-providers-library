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
import JSON_Utils_Cursors
import JSON_Utils_Parsers
import JSON_Utils_Str_CharStrConversion
import JSON_Utils_Str_CharStrEscaping
import JSON_Utils_Str
import JSON_Utils_Seq

# Module: JSON_Utils_Vectors

class default__:
    def  __init__(self):
        pass

    @_dafny.classproperty
    def OOM__FAILURE(instance):
        return Wrappers.Outcome_Fail(VectorError_OutOfMemory())

class VectorError:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [VectorError_OutOfMemory()]
    @classmethod
    def default(cls, ):
        return lambda: VectorError_OutOfMemory()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_OutOfMemory(self) -> bool:
        return isinstance(self, VectorError_OutOfMemory)

class VectorError_OutOfMemory(VectorError, NamedTuple('OutOfMemory', [])):
    def __dafnystr__(self) -> str:
        return f'Vectors.VectorError.OutOfMemory'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, VectorError_OutOfMemory)
    def __hash__(self) -> int:
        return super().__hash__()


class Vector:
    def  __init__(self):
        self.size: int = int(0)
        self.capacity: int = int(0)
        self.data: _dafny.Array = _dafny.Array(None, 0)
        self._a: TypeVar('A') = None
        pass

    def __dafnystr__(self) -> str:
        return "JSON.Utils.Vectors.Vector"
    def ctor__(self, a0, initial__capacity):
        (self)._a = a0
        (self).size = 0
        (self).capacity = initial__capacity
        def lambda29_(d_471_a0_):
            def lambda30_(d_472___v0_):
                return d_471_a0_

            return lambda30_

        init2_ = lambda29_(a0)
        nw5_ = _dafny.Array(None, initial__capacity)
        for i0_2_ in range(nw5_.length(0)):
            nw5_[i0_2_] = init2_(i0_2_)
        (self).data = nw5_

    def At(self, idx):
        return (self.data)[idx]

    def Top(self):
        return (self.data)[(self.size) - (1)]

    def Put(self, idx, a):
        arr0_ = self.data
        arr0_[(idx)] = a

    def CopyFrom(self, new__data, count):
        hi8_ = count
        for d_473_idx_ in range(0, hi8_):
            arr1_ = self.data
            arr1_[(d_473_idx_)] = (new__data)[d_473_idx_]

    def Realloc(self, new__capacity):
        d_474_old__data_: _dafny.Array
        d_475_old__capacity_: int
        rhs6_ = self.data
        rhs7_ = self.capacity
        d_474_old__data_ = rhs6_
        d_475_old__capacity_ = rhs7_
        def lambda31_(d_476___v1_):
            return (self).a

        init3_ = lambda31_
        nw6_ = _dafny.Array(None, new__capacity)
        for i0_3_ in range(nw6_.length(0)):
            nw6_[i0_3_] = init3_(i0_3_)
        rhs8_ = nw6_
        rhs9_ = new__capacity
        lhs4_ = self
        lhs5_ = self
        lhs4_.data = rhs8_
        lhs5_.capacity = rhs9_
        (self).CopyFrom(d_474_old__data_, d_475_old__capacity_)

    def DefaultNewCapacity(self, capacity):
        if (capacity) < ((self).MAX__CAPACITY__BEFORE__DOUBLING):
            return (2) * (capacity)
        elif True:
            return (self).MAX__CAPACITY

    def ReallocDefault(self):
        o: Wrappers.Outcome = Wrappers.Outcome.default()()
        if (self.capacity) == ((self).MAX__CAPACITY):
            o = Wrappers.Outcome_Fail(VectorError_OutOfMemory())
            return o
        (self).Realloc((self).DefaultNewCapacity(self.capacity))
        o = Wrappers.Outcome_Pass()
        return o
        return o

    def Ensure(self, reserved):
        o: Wrappers.Outcome = Wrappers.Outcome.default()()
        if (reserved) > (((self).MAX__CAPACITY) - (self.size)):
            o = Wrappers.Outcome_Fail(VectorError_OutOfMemory())
            return o
        if (reserved) <= ((self.capacity) - (self.size)):
            o = Wrappers.Outcome_Pass()
            return o
        d_477_new__capacity_: int
        d_477_new__capacity_ = self.capacity
        while (reserved) > ((d_477_new__capacity_) - (self.size)):
            d_477_new__capacity_ = (self).DefaultNewCapacity(d_477_new__capacity_)
        (self).Realloc(d_477_new__capacity_)
        o = Wrappers.Outcome_Pass()
        return o
        return o

    def PopFast(self):
        (self).size = (self.size) - (1)

    def PushFast(self, a):
        arr2_ = self.data
        index1_ = self.size
        arr2_[index1_] = a
        (self).size = (self.size) + (1)

    def Push(self, a):
        o: Wrappers.Outcome = Wrappers.Outcome.default()()
        if (self.size) == (self.capacity):
            d_478_d_: Wrappers.Outcome
            out23_: Wrappers.Outcome
            out23_ = (self).ReallocDefault()
            d_478_d_ = out23_
            if (d_478_d_).is_Fail:
                o = d_478_d_
                return o
        (self).PushFast(a)
        o = Wrappers.Outcome_Pass()
        return o
        return o

    @property
    def a(self):
        return self._a
    @property
    def MAX__CAPACITY__BEFORE__DOUBLING(self):
        return _dafny.euclidian_division(BoundedInts.default__.UINT32__MAX, 2)
    @property
    def MAX__CAPACITY(self):
        return BoundedInts.default__.UINT32__MAX
