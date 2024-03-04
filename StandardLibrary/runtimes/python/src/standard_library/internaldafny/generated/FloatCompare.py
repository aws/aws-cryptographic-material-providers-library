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
                    in172_ = _dafny.Seq((s)[1::])
                    in173_ = (((acc) * (10)) + (ord((s)[0]))) - (ord('0'))
                    s = in172_
                    acc = in173_
                    raise _dafny.TailCall()
                elif True:
                    in174_ = _dafny.Seq((s)[1::])
                    in175_ = acc
                    s = in174_
                    acc = in175_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def SkipLeadingSpace(val):
        while True:
            with _dafny.label():
                if ((len(val)) > (0)) and (((val)[0]) <= (' ')):
                    in176_ = _dafny.Seq((val)[1::])
                    val = in176_
                    raise _dafny.TailCall()
                elif True:
                    return val
                break

    @staticmethod
    def StrToInt(s, acc):
        d_341_tmp_ = default__.SkipLeadingSpace(s)
        if (len(d_341_tmp_)) == (0):
            return 0
        elif ((d_341_tmp_)[0]) == ('-'):
            return (0) - (default__.StrToIntInner(s, 0))
        elif True:
            return default__.StrToIntInner(s, 0)

    @staticmethod
    def SplitE(x):
        d_342_parts_ = StandardLibrary.default__.SplitOnce_q(x, 'e')
        if (d_342_parts_).is_Some:
            return d_342_parts_
        elif True:
            return StandardLibrary.default__.SplitOnce_q(x, 'E')

    @staticmethod
    def SplitExp(x):
        d_343_parts_ = default__.SplitE(x)
        if (d_343_parts_).is_Some:
            return (((d_343_parts_).value)[0], default__.StrToInt(((d_343_parts_).value)[1], 0))
        elif True:
            return (x, 0)

    @staticmethod
    def SkipLeadingZeros(val):
        while True:
            with _dafny.label():
                if ((len(val)) > (0)) and (((val)[0]) == ('0')):
                    in177_ = _dafny.Seq((val)[1::])
                    val = in177_
                    raise _dafny.TailCall()
                elif True:
                    return val
                break

    @staticmethod
    def SkipTrailingZeros(val):
        while True:
            with _dafny.label():
                if ((len(val)) > (0)) and (((val)[(len(val)) - (1)]) == ('0')):
                    in178_ = _dafny.Seq((val)[:(len(val)) - (1):])
                    val = in178_
                    raise _dafny.TailCall()
                elif True:
                    return val
                break

    @staticmethod
    def SplitDot(x):
        d_344_parts_ = StandardLibrary.default__.SplitOnce_q(x, '.')
        if (d_344_parts_).is_Some:
            return (default__.SkipLeadingZeros(((d_344_parts_).value)[0]), default__.SkipTrailingZeros(((d_344_parts_).value)[1]))
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
                    in179_ = _dafny.Seq((x)[1::])
                    in180_ = _dafny.Seq((y)[1::])
                    x = in179_
                    y = in180_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def AppendZeros(x, newLength):
        return (x) + (_dafny.Seq(['0' for d_345_i_ in range((newLength) - (len(x)))]))

    @staticmethod
    def CompareFloatInner(x, y):
        d_346_xParts_ = default__.SplitExp(x)
        d_347_yParts_ = default__.SplitExp(y)
        d_348_xNum_ = default__.SplitDot((d_346_xParts_)[0])
        d_349_yNum_ = default__.SplitDot((d_347_yParts_)[0])
        d_350_xDigits_ = default__.SkipLeadingZeros(((d_348_xNum_)[0]) + ((d_348_xNum_)[1]))
        d_351_yDigits_ = default__.SkipLeadingZeros(((d_349_yNum_)[0]) + ((d_349_yNum_)[1]))
        d_352_xExp_ = ((d_346_xParts_)[1]) - (len((d_348_xNum_)[1]))
        d_353_yExp_ = ((d_347_yParts_)[1]) - (len((d_349_yNum_)[1]))
        d_354_logX_ = (d_352_xExp_) + (len(d_350_xDigits_))
        d_355_logY_ = (d_353_yExp_) + (len(d_351_yDigits_))
        if (d_354_logX_) > (d_355_logY_):
            return 1
        elif (d_355_logY_) > (d_354_logX_):
            return -1
        elif (len(d_350_xDigits_)) < (len(d_351_yDigits_)):
            return default__.StrCmp(default__.AppendZeros(d_350_xDigits_, len(d_351_yDigits_)), d_351_yDigits_)
        elif (len(d_351_yDigits_)) < (len(d_350_xDigits_)):
            return default__.StrCmp(d_350_xDigits_, default__.AppendZeros(d_351_yDigits_, len(d_350_xDigits_)))
        elif True:
            return default__.StrCmp(d_350_xDigits_, d_351_yDigits_)

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
                    in181_ = _dafny.Seq((x)[1::])
                    x = in181_
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
        d_356_x_ = default__.CleanNumber(x)
        d_357_y_ = default__.CleanNumber(y)
        if (default__.IsNegative(d_356_x_)) and (default__.IsNegative(d_357_y_)):
            return default__.CompareFloatInner(_dafny.Seq((d_357_y_)[1::]), _dafny.Seq((d_356_x_)[1::]))
        elif default__.IsNegative(d_356_x_):
            return -1
        elif default__.IsNegative(d_357_y_):
            return 1
        elif True:
            return default__.CompareFloatInner(d_356_x_, d_357_y_)

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
