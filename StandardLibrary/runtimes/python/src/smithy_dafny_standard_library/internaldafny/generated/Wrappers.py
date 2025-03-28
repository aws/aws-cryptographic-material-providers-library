import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import smithy_dafny_standard_library.internaldafny.generated.module_ as module_
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
        if True:
            if source0_.is_Some:
                d_0_v_ = source0_.value
                return Result_Success(d_0_v_)
        if True:
            return Result_Failure(_dafny.Seq("Option is None"))

    def ToResult_k(self, error):
        source0_ = self
        if True:
            if source0_.is_Some:
                d_0_v_ = source0_.value
                return Result_Success(d_0_v_)
        if True:
            return Result_Failure(error)

    def UnwrapOr(self, default):
        source0_ = self
        if True:
            if source0_.is_Some:
                d_0_v_ = source0_.value
                return d_0_v_
        if True:
            return default

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
        source0_ = self
        if True:
            if source0_.is_Success:
                d_0_s_ = source0_.value
                return Option_Some(d_0_s_)
        if True:
            d_1_e_ = source0_.error
            return Option_None()

    def UnwrapOr(self, default):
        source0_ = self
        if True:
            if source0_.is_Success:
                d_0_s_ = source0_.value
                return d_0_s_
        if True:
            d_1_e_ = source0_.error
            return default

    def IsFailure(self):
        return (self).is_Failure

    def PropagateFailure(self):
        return Result_Failure((self).error)

    def MapFailure(self, reWrap):
        source0_ = self
        if True:
            if source0_.is_Success:
                d_0_s_ = source0_.value
                return Result_Success(d_0_s_)
        if True:
            d_1_e_ = source0_.error
            return Result_Failure(reWrap(d_1_e_))

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

