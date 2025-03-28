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
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_Sequence as StandardLibrary_Sequence
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import smithy_dafny_standard_library.internaldafny.generated.UUID as UUID
import smithy_dafny_standard_library.internaldafny.generated.UTF8 as UTF8
import smithy_dafny_standard_library.internaldafny.generated.OsLang as OsLang

# Module: Time

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def FormatMilli(diff):
        d_0_whole_ = StandardLibrary_String.default__.Base10Int2String(_dafny.euclidian_division(diff, 1000))
        d_1_frac_ = StandardLibrary_String.default__.Base10Int2String(_dafny.euclidian_modulus(diff, 1000))
        if (len(d_1_frac_)) == (1):
            return ((d_0_whole_) + (_dafny.Seq(".00"))) + (d_1_frac_)
        elif (len(d_1_frac_)) == (2):
            return ((d_0_whole_) + (_dafny.Seq(".0"))) + (d_1_frac_)
        elif True:
            return ((d_0_whole_) + (_dafny.Seq("."))) + (d_1_frac_)

    @staticmethod
    def FormatMilliDiff(start, end):
        if (start) <= (end):
            return default__.FormatMilli((end) - (start))
        elif True:
            return (_dafny.Seq("-")) + (default__.FormatMilli((start) - (end)))

    @staticmethod
    def GetAbsoluteTime():
        output: AbsoluteTime = AbsoluteTime.default()()
        d_0_ClockTime_: int
        out0_: int
        out0_ = default__.CurrentRelativeTimeMilli()
        d_0_ClockTime_ = out0_
        d_1_CpuTime_: int
        out1_: int
        out1_ = default__.GetProcessCpuTimeMillis()
        d_1_CpuTime_ = out1_
        output = AbsoluteTime_AbsoluteTime(d_0_ClockTime_, d_1_CpuTime_)
        return output
        return output

    @staticmethod
    def PrintTimeSince(start):
        d_0_t_: RelativeTime
        out0_: RelativeTime
        out0_ = default__.TimeSince(start)
        d_0_t_ = out0_
        default__.PrintTime(d_0_t_)

    @staticmethod
    def PrintTimeSinceShort(start):
        d_0_t_: RelativeTime
        out0_: RelativeTime
        out0_ = default__.TimeSince(start)
        d_0_t_ = out0_
        default__.PrintTimeShort(d_0_t_)

    @staticmethod
    def PrintTimeSinceShortChained(start):
        x: AbsoluteTime = AbsoluteTime.default()()
        d_0_end_: AbsoluteTime
        out0_: AbsoluteTime
        out0_ = default__.GetAbsoluteTime()
        d_0_end_ = out0_
        default__.PrintTimeShort(default__.TimeDiff(start, d_0_end_))
        x = d_0_end_
        return x
        return x

    @staticmethod
    def TimeDiff(start, end):
        if (((start).ClockTime) <= ((end).ClockTime)) and (((start).CpuTime) <= ((end).CpuTime)):
            return RelativeTime_RelativeTime(((end).ClockTime) - ((start).ClockTime), ((end).CpuTime) - ((start).CpuTime))
        elif True:
            return RelativeTime_RelativeTime(0, 0)

    @staticmethod
    def TimeSince(start):
        output: RelativeTime = RelativeTime.default()()
        d_0_end_: AbsoluteTime
        out0_: AbsoluteTime
        out0_ = default__.GetAbsoluteTime()
        d_0_end_ = out0_
        output = default__.TimeDiff(start, d_0_end_)
        return output

    @staticmethod
    def PrintTime(time):
        _dafny.print(_dafny.string_of(_dafny.Seq("Clock Time : ")))
        _dafny.print(_dafny.string_of(default__.FormatMilli((time).ClockTime)))
        _dafny.print(_dafny.string_of(_dafny.Seq(" CPU Time : ")))
        _dafny.print(_dafny.string_of(default__.FormatMilli((time).CpuTime)))
        _dafny.print(_dafny.string_of(_dafny.Seq("\n")))

    @staticmethod
    def PrintTimeLong(time, tag):
        _dafny.print(_dafny.string_of(tag))
        _dafny.print(_dafny.string_of(_dafny.Seq(" ")))
        _dafny.print(_dafny.string_of(OsLang.default__.GetOsLong()))
        _dafny.print(_dafny.string_of(_dafny.Seq(" ")))
        _dafny.print(_dafny.string_of(OsLang.default__.GetLanguageLong()))
        _dafny.print(_dafny.string_of(_dafny.Seq(" Clock Time : ")))
        _dafny.print(_dafny.string_of(default__.FormatMilli((time).ClockTime)))
        _dafny.print(_dafny.string_of(_dafny.Seq(" CPU Time : ")))
        _dafny.print(_dafny.string_of(default__.FormatMilli((time).CpuTime)))
        _dafny.print(_dafny.string_of(_dafny.Seq("\n")))

    @staticmethod
    def PrintTimeShort(time):
        _dafny.print(_dafny.string_of(_dafny.Seq("CPU:")))
        _dafny.print(_dafny.string_of(default__.FormatMilli((time).CpuTime)))
        _dafny.print(_dafny.string_of(_dafny.Seq(" ")))

    @staticmethod
    def CreateGetCurrentTimeStampSuccess(value):
        return Wrappers.Result_Success(value)

    @staticmethod
    def CreateGetCurrentTimeStampFailure(error):
        return Wrappers.Result_Failure(error)


class AbsoluteTime:
    @classmethod
    def default(cls, ):
        return lambda: AbsoluteTime_AbsoluteTime(int(0), int(0))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AbsoluteTime(self) -> bool:
        return isinstance(self, AbsoluteTime_AbsoluteTime)

class AbsoluteTime_AbsoluteTime(AbsoluteTime, NamedTuple('AbsoluteTime', [('ClockTime', Any), ('CpuTime', Any)])):
    def __dafnystr__(self) -> str:
        return f'Time.AbsoluteTime.AbsoluteTime({_dafny.string_of(self.ClockTime)}, {_dafny.string_of(self.CpuTime)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AbsoluteTime_AbsoluteTime) and self.ClockTime == __o.ClockTime and self.CpuTime == __o.CpuTime
    def __hash__(self) -> int:
        return super().__hash__()


class RelativeTime:
    @classmethod
    def default(cls, ):
        return lambda: RelativeTime_RelativeTime(int(0), int(0))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_RelativeTime(self) -> bool:
        return isinstance(self, RelativeTime_RelativeTime)

class RelativeTime_RelativeTime(RelativeTime, NamedTuple('RelativeTime', [('ClockTime', Any), ('CpuTime', Any)])):
    def __dafnystr__(self) -> str:
        return f'Time.RelativeTime.RelativeTime({_dafny.string_of(self.ClockTime)}, {_dafny.string_of(self.CpuTime)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RelativeTime_RelativeTime) and self.ClockTime == __o.ClockTime and self.CpuTime == __o.CpuTime
    def __hash__(self) -> int:
        return super().__hash__()

