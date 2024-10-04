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
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Views_Core as JSON_Utils_Views_Core
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Views_Writers as JSON_Utils_Views_Writers
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Views as JSON_Utils_Views
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Lexers_Core as JSON_Utils_Lexers_Core
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Lexers_Strings as JSON_Utils_Lexers_Strings
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Lexers as JSON_Utils_Lexers
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Cursors as JSON_Utils_Cursors
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Parsers as JSON_Utils_Parsers
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Str_CharStrConversion as JSON_Utils_Str_CharStrConversion
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Str_CharStrEscaping as JSON_Utils_Str_CharStrEscaping
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Str as JSON_Utils_Str
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Seq as JSON_Utils_Seq

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
        def lambda0_(d_0_a0_):
            def lambda1_(d_1___v0_):
                return d_0_a0_

            return lambda1_

        init0_ = lambda0_(a0)
        nw0_ = _dafny.Array(None, initial__capacity)
        for i0_0_ in range(nw0_.length(0)):
            nw0_[i0_0_] = init0_(i0_0_)
        (self).data = nw0_

    def At(self, idx):
        return (self.data)[idx]

    def Top(self):
        return (self.data)[(self.size) - (1)]

    def Put(self, idx, a):
        arr0_ = self.data
        arr0_[(idx)] = a

    def CopyFrom(self, new__data, count):
        hi0_ = count
        for d_0_idx_ in range(0, hi0_):
            arr0_ = self.data
            arr0_[(d_0_idx_)] = (new__data)[d_0_idx_]

    def Realloc(self, new__capacity):
        d_0_old__data_: _dafny.Array
        d_1_old__capacity_: int
        rhs0_ = self.data
        rhs1_ = self.capacity
        d_0_old__data_ = rhs0_
        d_1_old__capacity_ = rhs1_
        def lambda0_(d_2___v1_):
            return (self).a

        init0_ = lambda0_
        nw0_ = _dafny.Array(None, new__capacity)
        for i0_0_ in range(nw0_.length(0)):
            nw0_[i0_0_] = init0_(i0_0_)
        rhs2_ = nw0_
        rhs3_ = new__capacity
        lhs0_ = self
        lhs1_ = self
        lhs0_.data = rhs2_
        lhs1_.capacity = rhs3_
        (self).CopyFrom(d_0_old__data_, d_1_old__capacity_)

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
        d_0_new__capacity_: int
        d_0_new__capacity_ = self.capacity
        while (reserved) > ((d_0_new__capacity_) - (self.size)):
            d_0_new__capacity_ = (self).DefaultNewCapacity(d_0_new__capacity_)
        (self).Realloc(d_0_new__capacity_)
        o = Wrappers.Outcome_Pass()
        return o
        return o

    def PopFast(self):
        (self).size = (self.size) - (1)

    def PushFast(self, a):
        arr0_ = self.data
        index0_ = self.size
        arr0_[index0_] = a
        (self).size = (self.size) + (1)

    def Push(self, a):
        o: Wrappers.Outcome = Wrappers.Outcome.default()()
        if (self.size) == (self.capacity):
            d_0_d_: Wrappers.Outcome
            out0_: Wrappers.Outcome
            out0_ = (self).ReallocDefault()
            d_0_d_ = out0_
            if (d_0_d_).is_Fail:
                o = d_0_d_
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
