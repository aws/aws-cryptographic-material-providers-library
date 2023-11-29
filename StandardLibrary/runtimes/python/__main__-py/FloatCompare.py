import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import BoundedInts
import StandardLibrary_mUInt
import StandardLibrary
import UTF8
import TestUTF8
import Time
import TestTime
import HexStrings
import TestHexStrings
import Relations
import Seq_mMergeSort
import Math
import Seq
import SortedSets
import TestSeqReaderReadElements
import Functions
import Sets

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
                    in53_ = _dafny.Seq((s)[1::])
                    in54_ = (((acc) * (10)) + (ord((s)[0]))) - (ord('0'))
                    s = in53_
                    acc = in54_
                    raise _dafny.TailCall()
                elif True:
                    in55_ = _dafny.Seq((s)[1::])
                    in56_ = acc
                    s = in55_
                    acc = in56_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def SkipLeadingSpace(val):
        while True:
            with _dafny.label():
                if ((len(val)) > (0)) and (((val)[0]) <= (' ')):
                    in57_ = _dafny.Seq((val)[1::])
                    val = in57_
                    raise _dafny.TailCall()
                elif True:
                    return val
                break

    @staticmethod
    def StrToInt(s, acc):
        d_199_tmp_ = default__.SkipLeadingSpace(s)
        if (len(d_199_tmp_)) == (0):
            return 0
        elif ((d_199_tmp_)[0]) == ('-'):
            return (0) - (default__.StrToIntInner(s, 0))
        elif True:
            return default__.StrToIntInner(s, 0)

    @staticmethod
    def SplitE(x):
        d_200_parts_ = StandardLibrary.default__.SplitOnce_q(x, 'e')
        if (d_200_parts_).is_Some:
            return d_200_parts_
        elif True:
            return StandardLibrary.default__.SplitOnce_q(x, 'E')

    @staticmethod
    def SplitExp(x):
        d_201_parts_ = default__.SplitE(x)
        if (d_201_parts_).is_Some:
            return (((d_201_parts_).value)[0], default__.StrToInt(((d_201_parts_).value)[1], 0))
        elif True:
            return (x, 0)

    @staticmethod
    def SkipLeadingZeros(val):
        while True:
            with _dafny.label():
                if ((len(val)) > (0)) and (((val)[0]) == ('0')):
                    in58_ = _dafny.Seq((val)[1::])
                    val = in58_
                    raise _dafny.TailCall()
                elif True:
                    return val
                break

    @staticmethod
    def SkipTrailingZeros(val):
        while True:
            with _dafny.label():
                if ((len(val)) > (0)) and (((val)[(len(val)) - (1)]) == ('0')):
                    in59_ = _dafny.Seq((val)[:(len(val)) - (1):])
                    val = in59_
                    raise _dafny.TailCall()
                elif True:
                    return val
                break

    @staticmethod
    def SplitDot(x):
        d_202_parts_ = StandardLibrary.default__.SplitOnce_q(x, '.')
        if (d_202_parts_).is_Some:
            return (default__.SkipLeadingZeros(((d_202_parts_).value)[0]), default__.SkipTrailingZeros(((d_202_parts_).value)[1]))
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
                    in60_ = _dafny.Seq((x)[1::])
                    in61_ = _dafny.Seq((y)[1::])
                    x = in60_
                    y = in61_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def AppendZeros(x, newLength):
        return (x) + (_dafny.Seq(['0' for d_203_i_ in range((newLength) - (len(x)))]))

    @staticmethod
    def CompareFloatInner(x, y):
        d_204_xParts_ = default__.SplitExp(x)
        d_205_yParts_ = default__.SplitExp(y)
        d_206_xNum_ = default__.SplitDot((d_204_xParts_)[0])
        d_207_yNum_ = default__.SplitDot((d_205_yParts_)[0])
        d_208_xDigits_ = default__.SkipLeadingZeros(((d_206_xNum_)[0]) + ((d_206_xNum_)[1]))
        d_209_yDigits_ = default__.SkipLeadingZeros(((d_207_yNum_)[0]) + ((d_207_yNum_)[1]))
        d_210_xExp_ = ((d_204_xParts_)[1]) - (len((d_206_xNum_)[1]))
        d_211_yExp_ = ((d_205_yParts_)[1]) - (len((d_207_yNum_)[1]))
        d_212_logX_ = (d_210_xExp_) + (len(d_208_xDigits_))
        d_213_logY_ = (d_211_yExp_) + (len(d_209_yDigits_))
        if (d_212_logX_) > (d_213_logY_):
            return 1
        elif (d_213_logY_) > (d_212_logX_):
            return -1
        elif (len(d_208_xDigits_)) < (len(d_209_yDigits_)):
            return default__.StrCmp(default__.AppendZeros(d_208_xDigits_, len(d_209_yDigits_)), d_209_yDigits_)
        elif (len(d_209_yDigits_)) < (len(d_208_xDigits_)):
            return default__.StrCmp(d_208_xDigits_, default__.AppendZeros(d_209_yDigits_, len(d_208_xDigits_)))
        elif True:
            return default__.StrCmp(d_208_xDigits_, d_209_yDigits_)

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
                    in62_ = _dafny.Seq((x)[1::])
                    x = in62_
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
        d_214_x_ = default__.CleanNumber(x)
        d_215_y_ = default__.CleanNumber(y)
        if (default__.IsNegative(d_214_x_)) and (default__.IsNegative(d_215_y_)):
            return default__.CompareFloatInner(_dafny.Seq((d_215_y_)[1::]), _dafny.Seq((d_214_x_)[1::]))
        elif default__.IsNegative(d_214_x_):
            return -1
        elif default__.IsNegative(d_215_y_):
            return 1
        elif True:
            return default__.CompareFloatInner(d_214_x_, d_215_y_)

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
