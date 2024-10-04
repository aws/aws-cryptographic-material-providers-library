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

# Module: Actions

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DeterministicMap(action, s):
        res: _dafny.Seq = _dafny.Seq({})
        d_0_rs_: _dafny.Seq
        d_0_rs_ = _dafny.Seq([])
        hi0_ = len(s)
        for d_1_i_ in range(0, hi0_):
            d_2_r_: TypeVar('R__')
            out0_: TypeVar('R__')
            out0_ = (action).Invoke((s)[d_1_i_])
            d_2_r_ = out0_
            d_0_rs_ = (d_0_rs_) + (_dafny.Seq([d_2_r_]))
        res = d_0_rs_
        return res
        return res

    @staticmethod
    def DeterministicMapWithResult(action, s):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_0_rs_: _dafny.Seq
        d_0_rs_ = _dafny.Seq([])
        hi0_ = len(s)
        for d_1_i_ in range(0, hi0_):
            d_2_valueOrError0_: Wrappers.Result = None
            out0_: Wrappers.Result
            out0_ = (action).Invoke((s)[d_1_i_])
            d_2_valueOrError0_ = out0_
            if (d_2_valueOrError0_).IsFailure():
                res = (d_2_valueOrError0_).PropagateFailure()
                return res
            d_3_r_: TypeVar('R__')
            d_3_r_ = (d_2_valueOrError0_).Extract()
            d_0_rs_ = (d_0_rs_) + (_dafny.Seq([d_3_r_]))
        res = Wrappers.Result_Success(d_0_rs_)
        return res
        return res

    @staticmethod
    def DeterministicFlatMap(action, s):
        res: _dafny.Seq = _dafny.Seq({})
        d_0_rs_: _dafny.Seq
        d_0_rs_ = _dafny.Seq([])
        hi0_ = len(s)
        for d_1_i_ in range(0, hi0_):
            d_2_r_: _dafny.Seq
            out0_: _dafny.Seq
            out0_ = (action).Invoke((s)[d_1_i_])
            d_2_r_ = out0_
            d_0_rs_ = (d_0_rs_) + (d_2_r_)
        res = d_0_rs_
        return res
        return res

    @staticmethod
    def DeterministicFlatMapWithResult(action, s):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_0_rs_: _dafny.Seq
        d_0_rs_ = _dafny.Seq([])
        hi0_ = len(s)
        for d_1_i_ in range(0, hi0_):
            d_2_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            out0_: Wrappers.Result
            out0_ = (action).Invoke((s)[d_1_i_])
            d_2_valueOrError0_ = out0_
            if (d_2_valueOrError0_).IsFailure():
                res = (d_2_valueOrError0_).PropagateFailure()
                return res
            d_3_r_: _dafny.Seq
            d_3_r_ = (d_2_valueOrError0_).Extract()
            d_0_rs_ = (d_0_rs_) + (d_3_r_)
        rhs0_ = Wrappers.Result_Success(d_0_rs_)
        res = rhs0_
        return res
        return res

    @staticmethod
    def Filter(action, s):
        res: _dafny.Seq = _dafny.Seq({})
        d_0_rs_: _dafny.Seq
        d_0_rs_ = _dafny.Seq([])
        hi0_ = len(s)
        for d_1_i_ in range(0, hi0_):
            d_2_r_: bool
            out0_: bool
            out0_ = (action).Invoke((s)[d_1_i_])
            d_2_r_ = out0_
            if d_2_r_:
                d_0_rs_ = (d_0_rs_) + (_dafny.Seq([(s)[d_1_i_]]))
        res = d_0_rs_
        return res
        return res

    @staticmethod
    def FilterWithResult(action, s):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_0_rs_: _dafny.Seq
        d_0_rs_ = _dafny.Seq([])
        hi0_ = len(s)
        for d_1_i_ in range(0, hi0_):
            d_2_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
            out0_: Wrappers.Result
            out0_ = (action).Invoke((s)[d_1_i_])
            d_2_valueOrError0_ = out0_
            if (d_2_valueOrError0_).IsFailure():
                res = (d_2_valueOrError0_).PropagateFailure()
                return res
            d_3_r_: bool
            d_3_r_ = (d_2_valueOrError0_).Extract()
            if d_3_r_:
                d_0_rs_ = (d_0_rs_) + (_dafny.Seq([(s)[d_1_i_]]))
        res = Wrappers.Result_Success(d_0_rs_)
        return res
        return res

    @staticmethod
    def ReduceToSuccess(action, s):
        res: Wrappers.Result = None
        d_0_attemptedResults_: _dafny.Seq
        d_0_attemptedResults_ = _dafny.Seq([])
        hi0_ = len(s)
        for d_1_i_ in range(0, hi0_):
            d_2_attempt_: Wrappers.Result
            out0_: Wrappers.Result
            out0_ = (action).Invoke((s)[d_1_i_])
            d_2_attempt_ = out0_
            d_0_attemptedResults_ = (d_0_attemptedResults_) + (_dafny.Seq([d_2_attempt_]))
            if (d_2_attempt_).is_Success:
                rhs0_ = Wrappers.Result_Success((d_2_attempt_).value)
                res = rhs0_
                return res
        res = Wrappers.Result_Failure(Seq.default__.Map(lambda eta0_: default__.pluckErrors(eta0_), d_0_attemptedResults_))
        return res

    @staticmethod
    def pluckErrors(r):
        return (r).error


class ActionInvoke:
    @classmethod
    def default(cls, default_A, default_R):
        return lambda: ActionInvoke_ActionInvoke(default_A(), default_R())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ActionInvoke(self) -> bool:
        return isinstance(self, ActionInvoke_ActionInvoke)

class ActionInvoke_ActionInvoke(ActionInvoke, NamedTuple('ActionInvoke', [('input', Any), ('output', Any)])):
    def __dafnystr__(self) -> str:
        return f'Actions.ActionInvoke.ActionInvoke({_dafny.string_of(self.input)}, {_dafny.string_of(self.output)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ActionInvoke_ActionInvoke) and self.input == __o.input and self.output == __o.output
    def __hash__(self) -> int:
        return super().__hash__()


class Action:
    pass
    def Invoke(self, a):
        pass


class ActionWithResult:
    pass

class DeterministicAction:
    pass
    def Invoke(self, a):
        pass


class DeterministicActionWithResult:
    pass
