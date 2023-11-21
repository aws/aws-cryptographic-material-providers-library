import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_mMergeSort
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
import StandardLibrary_mUInt
import String
import StandardLibrary
import UUID
import UTF8
import Time
import Streams
import Sorting
import SortedSets
import HexStrings

assert "FloatCompare" == __name__
FloatCompare = sys.modules[__name__]

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
                    in69_ = _dafny.Seq((s)[1::])
                    in70_ = (((acc) * (10)) + (ord((s)[0]))) - (ord('0'))
                    s = in69_
                    acc = in70_
                    raise _dafny.TailCall()
                elif True:
                    in71_ = _dafny.Seq((s)[1::])
                    in72_ = acc
                    s = in71_
                    acc = in72_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def SkipLeadingSpace(val):
        while True:
            with _dafny.label():
                if ((len(val)) > (0)) and (((val)[0]) <= (' ')):
                    in73_ = _dafny.Seq((val)[1::])
                    val = in73_
                    raise _dafny.TailCall()
                elif True:
                    return val
                break

    @staticmethod
    def StrToInt(s, acc):
        d_256_tmp_ = FloatCompare.default__.SkipLeadingSpace(s)
        if (len(d_256_tmp_)) == (0):
            return 0
        elif ((d_256_tmp_)[0]) == ('-'):
            return (0) - (FloatCompare.default__.StrToIntInner(s, 0))
        elif True:
            return FloatCompare.default__.StrToIntInner(s, 0)

    @staticmethod
    def SplitE(x):
        d_257_parts_ = StandardLibrary.default__.SplitOnce_q(x, 'e')
        if (d_257_parts_).is_Some:
            return d_257_parts_
        elif True:
            return StandardLibrary.default__.SplitOnce_q(x, 'E')

    @staticmethod
    def SplitExp(x):
        d_258_parts_ = FloatCompare.default__.SplitE(x)
        if (d_258_parts_).is_Some:
            return (((d_258_parts_).value)[0], FloatCompare.default__.StrToInt(((d_258_parts_).value)[1], 0))
        elif True:
            return (x, 0)

    @staticmethod
    def SkipLeadingZeros(val):
        while True:
            with _dafny.label():
                if ((len(val)) > (0)) and (((val)[0]) == ('0')):
                    in74_ = _dafny.Seq((val)[1::])
                    val = in74_
                    raise _dafny.TailCall()
                elif True:
                    return val
                break

    @staticmethod
    def SkipTrailingZeros(val):
        while True:
            with _dafny.label():
                if ((len(val)) > (0)) and (((val)[(len(val)) - (1)]) == ('0')):
                    in75_ = _dafny.Seq((val)[:(len(val)) - (1):])
                    val = in75_
                    raise _dafny.TailCall()
                elif True:
                    return val
                break

    @staticmethod
    def SplitDot(x):
        d_259_parts_ = StandardLibrary.default__.SplitOnce_q(x, '.')
        if (d_259_parts_).is_Some:
            return (FloatCompare.default__.SkipLeadingZeros(((d_259_parts_).value)[0]), FloatCompare.default__.SkipTrailingZeros(((d_259_parts_).value)[1]))
        elif True:
            return (FloatCompare.default__.SkipLeadingZeros(x), _dafny.Seq(""))

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
                    in76_ = _dafny.Seq((x)[1::])
                    in77_ = _dafny.Seq((y)[1::])
                    x = in76_
                    y = in77_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def AppendZeros(x, newLength):
        return (x) + (_dafny.Seq(['0' for d_260_i_ in range((newLength) - (len(x)))]))

    @staticmethod
    def CompareFloatInner(x, y):
        d_261_xParts_ = FloatCompare.default__.SplitExp(x)
        d_262_yParts_ = FloatCompare.default__.SplitExp(y)
        d_263_xNum_ = FloatCompare.default__.SplitDot((d_261_xParts_)[0])
        d_264_yNum_ = FloatCompare.default__.SplitDot((d_262_yParts_)[0])
        d_265_xDigits_ = FloatCompare.default__.SkipLeadingZeros(((d_263_xNum_)[0]) + ((d_263_xNum_)[1]))
        d_266_yDigits_ = FloatCompare.default__.SkipLeadingZeros(((d_264_yNum_)[0]) + ((d_264_yNum_)[1]))
        d_267_xExp_ = ((d_261_xParts_)[1]) - (len((d_263_xNum_)[1]))
        d_268_yExp_ = ((d_262_yParts_)[1]) - (len((d_264_yNum_)[1]))
        d_269_logX_ = (d_267_xExp_) + (len(d_265_xDigits_))
        d_270_logY_ = (d_268_yExp_) + (len(d_266_yDigits_))
        if (d_269_logX_) > (d_270_logY_):
            return 1
        elif (d_270_logY_) > (d_269_logX_):
            return -1
        elif (len(d_265_xDigits_)) < (len(d_266_yDigits_)):
            return FloatCompare.default__.StrCmp(FloatCompare.default__.AppendZeros(d_265_xDigits_, len(d_266_yDigits_)), d_266_yDigits_)
        elif (len(d_266_yDigits_)) < (len(d_265_xDigits_)):
            return FloatCompare.default__.StrCmp(d_265_xDigits_, FloatCompare.default__.AppendZeros(d_266_yDigits_, len(d_265_xDigits_)))
        elif True:
            return FloatCompare.default__.StrCmp(d_265_xDigits_, d_266_yDigits_)

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
                    in78_ = _dafny.Seq((x)[1::])
                    x = in78_
                    raise _dafny.TailCall()
                elif (('1') <= ((x)[0])) and (((x)[0]) <= ('9')):
                    return False
                elif True:
                    return True
                break

    @staticmethod
    def RecognizeZero(x):
        if FloatCompare.default__.IsNegative(x):
            if FloatCompare.default__.IsZero(_dafny.Seq((x)[1::])):
                return _dafny.Seq("0")
            elif True:
                return x
        elif FloatCompare.default__.IsZero(x):
            return _dafny.Seq("0")
        elif True:
            return x

    @staticmethod
    def CleanNumber(x):
        return FloatCompare.default__.RecognizeZero(FloatCompare.default__.SkipLeadingPlus(FloatCompare.default__.SkipLeadingSpace(x)))

    @staticmethod
    def CompareFloat(x, y):
        d_271_x_ = FloatCompare.default__.CleanNumber(x)
        d_272_y_ = FloatCompare.default__.CleanNumber(y)
        if (FloatCompare.default__.IsNegative(d_271_x_)) and (FloatCompare.default__.IsNegative(d_272_y_)):
            return FloatCompare.default__.CompareFloatInner(_dafny.Seq((d_272_y_)[1::]), _dafny.Seq((d_271_x_)[1::]))
        elif FloatCompare.default__.IsNegative(d_271_x_):
            return -1
        elif FloatCompare.default__.IsNegative(d_272_y_):
            return 1
        elif True:
            return FloatCompare.default__.CompareFloatInner(d_271_x_, d_272_y_)

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
