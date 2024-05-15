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

# Module: standard_library.internaldafny.generated.JSON_Utils_Views_Writers


class Chain:
    @classmethod
    def default(cls, ):
        return lambda: Chain_Empty()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Empty(self) -> bool:
        return isinstance(self, Chain_Empty)
    @property
    def is_Chain(self) -> bool:
        return isinstance(self, Chain_Chain)
    def Length(self):
        d_440___accumulator_ = 0
        _this = self
        while True:
            with _dafny.label():
                if (_this).is_Empty:
                    return (0) + (d_440___accumulator_)
                elif True:
                    d_440___accumulator_ = (((_this).v).Length()) + (d_440___accumulator_)
                    in184_ = (_this).previous
                    _this = in184_
                    
                    raise _dafny.TailCall()
                break

    def Count(self):
        d_441___accumulator_ = 0
        _this = self
        while True:
            with _dafny.label():
                if (_this).is_Empty:
                    return (0) + (d_441___accumulator_)
                elif True:
                    d_441___accumulator_ = (1) + (d_441___accumulator_)
                    in185_ = (_this).previous
                    _this = in185_
                    
                    raise _dafny.TailCall()
                break

    def Bytes(self):
        d_442___accumulator_ = _dafny.Seq([])
        _this = self
        while True:
            with _dafny.label():
                if (_this).is_Empty:
                    return (_dafny.Seq([])) + (d_442___accumulator_)
                elif True:
                    d_442___accumulator_ = (((_this).v).Bytes()) + (d_442___accumulator_)
                    in186_ = (_this).previous
                    _this = in186_
                    
                    raise _dafny.TailCall()
                break

    def Append(self, v_k):
        if ((self).is_Chain) and (JSON_Utils_Views_Core.default__.Adjacent((self).v, v_k)):
            return Chain_Chain((self).previous, JSON_Utils_Views_Core.default__.Merge((self).v, v_k))
        elif True:
            return Chain_Chain(self, v_k)

    def CopyTo(self, dest, end):
        _this = self
        while True:
            with _dafny.label():
                if (_this).is_Chain:
                    d_443_end_: int
                    d_443_end_ = (end) - (((_this).v).Length())
                    ((_this).v).CopyTo(dest, d_443_end_)
                    in187_ = (_this).previous
                    in188_ = dest
                    in189_ = d_443_end_
                    _this = in187_
                    
                    dest = in188_
                    end = in189_
                    raise _dafny.TailCall()
                break


class Chain_Empty(Chain, NamedTuple('Empty', [])):
    def __dafnystr__(self) -> str:
        return f'Writers.Chain.Empty'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Chain_Empty)
    def __hash__(self) -> int:
        return super().__hash__()

class Chain_Chain(Chain, NamedTuple('Chain', [('previous', Any), ('v', Any)])):
    def __dafnystr__(self) -> str:
        return f'Writers.Chain.Chain({_dafny.string_of(self.previous)}, {_dafny.string_of(self.v)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Chain_Chain) and self.previous == __o.previous and self.v == __o.v
    def __hash__(self) -> int:
        return super().__hash__()


class Writer:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return Writer___Writer(0, Chain_Empty())

class Writer__:
    @classmethod
    def default(cls, ):
        return lambda: Writer___Writer(int(0), Chain.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Writer(self) -> bool:
        return isinstance(self, Writer___Writer)
    def Bytes(self):
        return ((self).chain).Bytes()

    @staticmethod
    def SaturatedAddU32(a, b):
        if (a) <= ((BoundedInts.default__.UINT32__MAX) - (b)):
            return (a) + (b)
        elif True:
            return BoundedInts.default__.UINT32__MAX

    def Append(self, v_k):
        return Writer___Writer(Writer__.SaturatedAddU32((self).length, (v_k).Length()), ((self).chain).Append(v_k))

    def Then(self, fn):
        return fn(self)

    def CopyTo(self, dest):
        ((self).chain).CopyTo(dest, (self).length)

    def ToArray(self):
        bs: _dafny.Array = _dafny.Array(None, 0)
        nw4_ = _dafny.Array(int(0), (self).length)
        bs = nw4_
        (self).CopyTo(bs)
        return bs

    @_dafny.classproperty
    def Empty(instance):
        return Writer___Writer(0, Chain_Empty())
    @property
    def Unsaturated_q(self):
        return ((self).length) != (BoundedInts.default__.UINT32__MAX)
    @property
    def Empty_q(self):
        return ((self).chain).is_Empty

class Writer___Writer(Writer__, NamedTuple('Writer', [('length', Any), ('chain', Any)])):
    def __dafnystr__(self) -> str:
        return f'Writers.Writer_.Writer({_dafny.string_of(self.length)}, {_dafny.string_of(self.chain)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Writer___Writer) and self.length == __o.length and self.chain == __o.chain
    def __hash__(self) -> int:
        return super().__hash__()

