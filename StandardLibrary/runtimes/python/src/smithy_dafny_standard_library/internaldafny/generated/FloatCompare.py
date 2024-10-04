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

# Module: FloatCompare

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def StrToIntInner(s, acc):
        while True:
            with _dafny.label():
                if (len(s)) == (0):
                    return acc
                elif (('0') <= ((s)[0])) and (((s)[0]) <= ('9')):
                    in0_ = _dafny.Seq((s)[1::])
                    in1_ = (((acc) * (10)) + (ord((s)[0]))) - (ord('0'))
                    s = in0_
                    acc = in1_
                    raise _dafny.TailCall()
                elif True:
                    in2_ = _dafny.Seq((s)[1::])
                    in3_ = acc
                    s = in2_
                    acc = in3_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def SkipLeadingSpace(val):
        while True:
            with _dafny.label():
                if ((len(val)) > (0)) and (((val)[0]) <= (' ')):
                    in0_ = _dafny.Seq((val)[1::])
                    val = in0_
                    raise _dafny.TailCall()
                elif True:
                    return val
                break

    @staticmethod
    def StrToInt(s, acc):
        d_0_tmp_ = default__.SkipLeadingSpace(s)
        if (len(d_0_tmp_)) == (0):
            return 0
        elif ((d_0_tmp_)[0]) == ('-'):
            return (0) - (default__.StrToIntInner(s, 0))
        elif True:
            return default__.StrToIntInner(s, 0)

    @staticmethod
    def SplitE(x):
        d_0_parts_ = StandardLibrary.default__.SplitOnce_q(x, 'e')
        if (d_0_parts_).is_Some:
            return d_0_parts_
        elif True:
            return StandardLibrary.default__.SplitOnce_q(x, 'E')

    @staticmethod
    def SplitExp(x):
        d_0_parts_ = default__.SplitE(x)
        if (d_0_parts_).is_Some:
            return (((d_0_parts_).value)[0], default__.StrToInt(((d_0_parts_).value)[1], 0))
        elif True:
            return (x, 0)

    @staticmethod
    def SkipLeadingZeros(val):
        while True:
            with _dafny.label():
                if ((len(val)) > (0)) and (((val)[0]) == ('0')):
                    in0_ = _dafny.Seq((val)[1::])
                    val = in0_
                    raise _dafny.TailCall()
                elif True:
                    return val
                break

    @staticmethod
    def SkipTrailingZeros(val):
        while True:
            with _dafny.label():
                if ((len(val)) > (0)) and (((val)[(len(val)) - (1)]) == ('0')):
                    in0_ = _dafny.Seq((val)[:(len(val)) - (1):])
                    val = in0_
                    raise _dafny.TailCall()
                elif True:
                    return val
                break

    @staticmethod
    def SplitDot(x):
        d_0_parts_ = StandardLibrary.default__.SplitOnce_q(x, '.')
        if (d_0_parts_).is_Some:
            return (default__.SkipLeadingZeros(((d_0_parts_).value)[0]), default__.SkipTrailingZeros(((d_0_parts_).value)[1]))
        elif True:
            return (default__.SkipLeadingZeros(x), _dafny.Seq(""))

    @staticmethod
    def StrCmp(x, y):
        while True:
            with _dafny.label():
                if ((len(x)) == (0)) and ((len(y)) == (0)):
                    return 0
                elif (len(x)) == (0):
                    return -1
                elif (len(y)) == (0):
                    return 1
                elif ((x)[0]) < ((y)[0]):
                    return -1
                elif ((x)[0]) > ((y)[0]):
                    return 1
                elif True:
                    in0_ = _dafny.Seq((x)[1::])
                    in1_ = _dafny.Seq((y)[1::])
                    x = in0_
                    y = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def AppendZeros(x, newLength):
        return (x) + (_dafny.Seq(['0' for d_0_i_ in range((newLength) - (len(x)))]))

    @staticmethod
    def CompareFloatInner(x, y):
        d_0_xParts_ = default__.SplitExp(x)
        d_1_yParts_ = default__.SplitExp(y)
        d_2_xNum_ = default__.SplitDot((d_0_xParts_)[0])
        d_3_yNum_ = default__.SplitDot((d_1_yParts_)[0])
        d_4_xDigits_ = default__.SkipLeadingZeros(((d_2_xNum_)[0]) + ((d_2_xNum_)[1]))
        d_5_yDigits_ = default__.SkipLeadingZeros(((d_3_yNum_)[0]) + ((d_3_yNum_)[1]))
        d_6_xExp_ = ((d_0_xParts_)[1]) - (len((d_2_xNum_)[1]))
        d_7_yExp_ = ((d_1_yParts_)[1]) - (len((d_3_yNum_)[1]))
        d_8_logX_ = (d_6_xExp_) + (len(d_4_xDigits_))
        d_9_logY_ = (d_7_yExp_) + (len(d_5_yDigits_))
        if (d_8_logX_) > (d_9_logY_):
            return 1
        elif (d_9_logY_) > (d_8_logX_):
            return -1
        elif (len(d_4_xDigits_)) < (len(d_5_yDigits_)):
            return default__.StrCmp(default__.AppendZeros(d_4_xDigits_, len(d_5_yDigits_)), d_5_yDigits_)
        elif (len(d_5_yDigits_)) < (len(d_4_xDigits_)):
            return default__.StrCmp(d_4_xDigits_, default__.AppendZeros(d_5_yDigits_, len(d_4_xDigits_)))
        elif True:
            return default__.StrCmp(d_4_xDigits_, d_5_yDigits_)

    @staticmethod
    def IsNegative(x):
        return ((len(x)) > (0)) and (((x)[0]) == ('-'))

    @staticmethod
    def SkipLeadingPlus(x):
        if ((0) < (len(x))) and (((x)[0]) == ('+')):
            return _dafny.Seq((x)[1::])
        elif True:
            return x

    @staticmethod
    def IsZero(x):
        while True:
            with _dafny.label():
                if (len(x)) == (0):
                    return True
                elif (((x)[0]) == ('0')) or (((x)[0]) == ('.')):
                    in0_ = _dafny.Seq((x)[1::])
                    x = in0_
                    raise _dafny.TailCall()
                elif (('1') <= ((x)[0])) and (((x)[0]) <= ('9')):
                    return False
                elif True:
                    return True
                break

    @staticmethod
    def RecognizeZero(x):
        if default__.IsNegative(x):
            if default__.IsZero(_dafny.Seq((x)[1::])):
                return _dafny.Seq("0")
            elif True:
                return x
        elif default__.IsZero(x):
            return _dafny.Seq("0")
        elif True:
            return x

    @staticmethod
    def CleanNumber(x):
        return default__.RecognizeZero(default__.SkipLeadingPlus(default__.SkipLeadingSpace(x)))

    @staticmethod
    def CompareFloat(x, y):
        d_0_x_ = default__.CleanNumber(x)
        d_1_y_ = default__.CleanNumber(y)
        if (default__.IsNegative(d_0_x_)) and (default__.IsNegative(d_1_y_)):
            return default__.CompareFloatInner(_dafny.Seq((d_1_y_)[1::]), _dafny.Seq((d_0_x_)[1::]))
        elif default__.IsNegative(d_0_x_):
            return -1
        elif default__.IsNegative(d_1_y_):
            return 1
        elif True:
            return default__.CompareFloatInner(d_0_x_, d_1_y_)

    @_dafny.classproperty
    def Less(instance):
        return -1
    @_dafny.classproperty
    def Equal(instance):
        return 0
    @_dafny.classproperty
    def Greater(instance):
        return 1

class CompareType:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_0_x_: int = source__
        return ((-1) <= (d_0_x_)) and ((d_0_x_) <= (1))
