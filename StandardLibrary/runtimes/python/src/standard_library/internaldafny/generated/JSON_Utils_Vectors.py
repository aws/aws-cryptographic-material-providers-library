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
import standard_library.internaldafny.generated.JSON_Utils_Cursors as JSON_Utils_Cursors
import standard_library.internaldafny.generated.JSON_Utils_Parsers as JSON_Utils_Parsers
import standard_library.internaldafny.generated.JSON_Utils_Str_CharStrConversion as JSON_Utils_Str_CharStrConversion
import standard_library.internaldafny.generated.JSON_Utils_Str_CharStrEscaping as JSON_Utils_Str_CharStrEscaping
import standard_library.internaldafny.generated.JSON_Utils_Str as JSON_Utils_Str
import standard_library.internaldafny.generated.JSON_Utils_Seq as JSON_Utils_Seq

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
        self._i_a: TypeVar('A') = None
        pass

    def __dafnystr__(self) -> str:
        return "JSON.Utils.Vectors.Vector"
    def ctor__(self, a0, initial__capacity):
        (self)._i_a = a0
        (self).size = 0
        (self).capacity = initial__capacity
        def lambda30_(d_478_a0_):
            def lambda31_(d_479___v0_):
                return d_478_a0_

            return lambda31_

        init2_ = lambda30_(a0)
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
        for d_480_idx_ in range(0, hi8_):
            arr1_ = self.data
            arr1_[(d_480_idx_)] = (new__data)[d_480_idx_]

    def Realloc(self, new__capacity):
        d_481_old__data_: _dafny.Array
        d_482_old__capacity_: int
        rhs6_ = self.data
        rhs7_ = self.capacity
        d_481_old__data_ = rhs6_
        d_482_old__capacity_ = rhs7_
        def lambda32_(d_483___v1_):
            return (self).a

        init3_ = lambda32_
        nw6_ = _dafny.Array(None, new__capacity)
        for i0_3_ in range(nw6_.length(0)):
            nw6_[i0_3_] = init3_(i0_3_)
        rhs8_ = nw6_
        rhs9_ = new__capacity
        lhs4_ = self
        lhs5_ = self
        lhs4_.data = rhs8_
        lhs5_.capacity = rhs9_
        (self).CopyFrom(d_481_old__data_, d_482_old__capacity_)

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
        d_484_new__capacity_: int
        d_484_new__capacity_ = self.capacity
        while (reserved) > ((d_484_new__capacity_) - (self.size)):
            d_484_new__capacity_ = (self).DefaultNewCapacity(d_484_new__capacity_)
        (self).Realloc(d_484_new__capacity_)
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
            d_485_d_: Wrappers.Outcome
            out23_: Wrappers.Outcome
            out23_ = (self).ReallocDefault()
            d_485_d_ = out23_
            if (d_485_d_).is_Fail:
                o = d_485_d_
                return o
        (self).PushFast(a)
        o = Wrappers.Outcome_Pass()
        return o
        return o

    @property
    def a(self):
        return self._i_a
    @property
    def MAX__CAPACITY__BEFORE__DOUBLING(self):
        return _dafny.euclidian_division(BoundedInts.default__.UINT32__MAX, 2)
    @property
    def MAX__CAPACITY(self):
        return BoundedInts.default__.UINT32__MAX
