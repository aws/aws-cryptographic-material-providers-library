import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import standard_library.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_

# Module: Wrappers

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Need(condition, error):
        if condition:
            return Outcome_Pass()
        elif True:
            return Outcome_Fail(error)


class Option:
    @classmethod
    def default(cls, ):
        return lambda: Option_None()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_None(self) -> bool:
        return isinstance(self, Option_None)
    @property
    def is_Some(self) -> bool:
        return isinstance(self, Option_Some)
    def ToResult(self):
        source0_ = self
        unmatched0 = True
        if unmatched0:
            if source0_.is_Some:
                d_0_v_ = source0_.value
                unmatched0 = False
                return Result_Success(d_0_v_)
        if unmatched0:
            unmatched0 = False
            return Result_Failure(_dafny.Seq("Option is None"))
        raise Exception("unexpected control point")

    def ToResult_k(self, error):
        pat_let_tv0_ = error
        source1_ = self
        unmatched1 = True
        if unmatched1:
            if source1_.is_Some:
                d_1_v_ = source1_.value
                unmatched1 = False
                return Result_Success(d_1_v_)
        if unmatched1:
            unmatched1 = False
            return Result_Failure(pat_let_tv0_)
        raise Exception("unexpected control point")

    def UnwrapOr(self, default):
        pat_let_tv1_ = default
        source2_ = self
        unmatched2 = True
        if unmatched2:
            if source2_.is_Some:
                d_2_v_ = source2_.value
                unmatched2 = False
                return d_2_v_
        if unmatched2:
            unmatched2 = False
            return pat_let_tv1_
        raise Exception("unexpected control point")

    def IsFailure(self):
        return (self).is_None

    def PropagateFailure(self):
        return Option_None()

    def Extract(self):
        return (self).value


class Option_None(Option, NamedTuple('None_', [])):
    def __dafnystr__(self) -> str:
        return f'Wrappers.Option.None'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Option_None)
    def __hash__(self) -> int:
        return super().__hash__()

class Option_Some(Option, NamedTuple('Some', [('value', Any)])):
    def __dafnystr__(self) -> str:
        return f'Wrappers.Option.Some({_dafny.string_of(self.value)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Option_Some) and self.value == __o.value
    def __hash__(self) -> int:
        return super().__hash__()


class Result:
    @classmethod
    def default(cls, default_T):
        return lambda: Result_Success(default_T())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Success(self) -> bool:
        return isinstance(self, Result_Success)
    @property
    def is_Failure(self) -> bool:
        return isinstance(self, Result_Failure)
    def ToOption(self):
        source3_ = self
        unmatched3 = True
        if unmatched3:
            if source3_.is_Success:
                d_3_s_ = source3_.value
                unmatched3 = False
                return Option_Some(d_3_s_)
        if unmatched3:
            d_4_e_ = source3_.error
            unmatched3 = False
            return Option_None()
        raise Exception("unexpected control point")

    def UnwrapOr(self, default):
        pat_let_tv2_ = default
        source4_ = self
        unmatched4 = True
        if unmatched4:
            if source4_.is_Success:
                d_5_s_ = source4_.value
                unmatched4 = False
                return d_5_s_
        if unmatched4:
            d_6_e_ = source4_.error
            unmatched4 = False
            return pat_let_tv2_
        raise Exception("unexpected control point")

    def IsFailure(self):
        return (self).is_Failure

    def PropagateFailure(self):
        return Result_Failure((self).error)

    def MapFailure(self, reWrap):
        pat_let_tv3_ = reWrap
        source5_ = self
        unmatched5 = True
        if unmatched5:
            if source5_.is_Success:
                d_7_s_ = source5_.value
                unmatched5 = False
                return Result_Success(d_7_s_)
        if unmatched5:
            d_8_e_ = source5_.error
            unmatched5 = False
            return Result_Failure(pat_let_tv3_(d_8_e_))
        raise Exception("unexpected control point")

    def Extract(self):
        return (self).value


class Result_Success(Result, NamedTuple('Success', [('value', Any)])):
    def __dafnystr__(self) -> str:
        return f'Wrappers.Result.Success({_dafny.string_of(self.value)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Result_Success) and self.value == __o.value
    def __hash__(self) -> int:
        return super().__hash__()

class Result_Failure(Result, NamedTuple('Failure', [('error', Any)])):
    def __dafnystr__(self) -> str:
        return f'Wrappers.Result.Failure({_dafny.string_of(self.error)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Result_Failure) and self.error == __o.error
    def __hash__(self) -> int:
        return super().__hash__()


class Outcome:
    @classmethod
    def default(cls, ):
        return lambda: Outcome_Pass()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Pass(self) -> bool:
        return isinstance(self, Outcome_Pass)
    @property
    def is_Fail(self) -> bool:
        return isinstance(self, Outcome_Fail)
    def IsFailure(self):
        return (self).is_Fail

    def PropagateFailure(self):
        return Result_Failure((self).error)


class Outcome_Pass(Outcome, NamedTuple('Pass', [])):
    def __dafnystr__(self) -> str:
        return f'Wrappers.Outcome.Pass'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Outcome_Pass)
    def __hash__(self) -> int:
        return super().__hash__()

class Outcome_Fail(Outcome, NamedTuple('Fail', [('error', Any)])):
    def __dafnystr__(self) -> str:
        return f'Wrappers.Outcome.Fail({_dafny.string_of(self.error)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Outcome_Fail) and self.error == __o.error
    def __hash__(self) -> int:
        return super().__hash__()

