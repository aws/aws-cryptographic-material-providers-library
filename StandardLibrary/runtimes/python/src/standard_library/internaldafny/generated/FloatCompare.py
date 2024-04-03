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
        d_362_tmp_ = default__.SkipLeadingSpace(s)
        if (len(d_362_tmp_)) == (0):
            return 0
        elif ((d_362_tmp_)[0]) == ('-'):
            return (0) - (default__.StrToIntInner(s, 0))
        elif True:
            return default__.StrToIntInner(s, 0)

    @staticmethod
    def SplitE(x):
        d_363_parts_ = StandardLibrary.default__.SplitOnce_q(x, 'e')
        if (d_363_parts_).is_Some:
            return d_363_parts_
        elif True:
            return StandardLibrary.default__.SplitOnce_q(x, 'E')

    @staticmethod
    def SplitExp(x):
        d_364_parts_ = default__.SplitE(x)
        if (d_364_parts_).is_Some:
            return (((d_364_parts_).value)[0], default__.StrToInt(((d_364_parts_).value)[1], 0))
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
        d_365_parts_ = StandardLibrary.default__.SplitOnce_q(x, '.')
        if (d_365_parts_).is_Some:
            return (default__.SkipLeadingZeros(((d_365_parts_).value)[0]), default__.SkipTrailingZeros(((d_365_parts_).value)[1]))
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
        return (x) + (_dafny.Seq(['0' for d_366_i_ in range((newLength) - (len(x)))]))

    @staticmethod
    def CompareFloatInner(x, y):
        d_367_xParts_ = default__.SplitExp(x)
        d_368_yParts_ = default__.SplitExp(y)
        d_369_xNum_ = default__.SplitDot((d_367_xParts_)[0])
        d_370_yNum_ = default__.SplitDot((d_368_yParts_)[0])
        d_371_xDigits_ = default__.SkipLeadingZeros(((d_369_xNum_)[0]) + ((d_369_xNum_)[1]))
        d_372_yDigits_ = default__.SkipLeadingZeros(((d_370_yNum_)[0]) + ((d_370_yNum_)[1]))
        d_373_xExp_ = ((d_367_xParts_)[1]) - (len((d_369_xNum_)[1]))
        d_374_yExp_ = ((d_368_yParts_)[1]) - (len((d_370_yNum_)[1]))
        d_375_logX_ = (d_373_xExp_) + (len(d_371_xDigits_))
        d_376_logY_ = (d_374_yExp_) + (len(d_372_yDigits_))
        if (d_375_logX_) > (d_376_logY_):
            return 1
        elif (d_376_logY_) > (d_375_logX_):
            return -1
        elif (len(d_371_xDigits_)) < (len(d_372_yDigits_)):
            return default__.StrCmp(default__.AppendZeros(d_371_xDigits_, len(d_372_yDigits_)), d_372_yDigits_)
        elif (len(d_372_yDigits_)) < (len(d_371_xDigits_)):
            return default__.StrCmp(d_371_xDigits_, default__.AppendZeros(d_372_yDigits_, len(d_371_xDigits_)))
        elif True:
            return default__.StrCmp(d_371_xDigits_, d_372_yDigits_)

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
        d_377_x_ = default__.CleanNumber(x)
        d_378_y_ = default__.CleanNumber(y)
        if (default__.IsNegative(d_377_x_)) and (default__.IsNegative(d_378_y_)):
            return default__.CompareFloatInner(_dafny.Seq((d_378_y_)[1::]), _dafny.Seq((d_377_x_)[1::]))
        elif default__.IsNegative(d_377_x_):
            return -1
        elif default__.IsNegative(d_378_y_):
            return 1
        elif True:
            return default__.CompareFloatInner(d_377_x_, d_378_y_)

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
        d_379_x_: int = source__
        return ((-1) <= (d_379_x_)) and ((d_379_x_) <= (1))
