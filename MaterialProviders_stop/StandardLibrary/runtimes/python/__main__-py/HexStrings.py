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

assert "HexStrings" == __name__
HexStrings = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def HexChar(x):
        if (x) < (10):
            return _dafny.plus_char('0', chr(x))
        elif True:
            return _dafny.plus_char('a', chr((x) - (10)))

    @staticmethod
    def IsLooseHexChar(ch):
        return (((('0') <= (ch)) and ((ch) <= ('9'))) or ((('a') <= (ch)) and ((ch) <= ('f')))) or ((('A') <= (ch)) and ((ch) <= ('F')))

    @staticmethod
    def IsHexChar(ch):
        return ((('0') <= (ch)) and ((ch) <= ('9'))) or ((('a') <= (ch)) and ((ch) <= ('f')))

    @staticmethod
    def IsHexString(s):
        def lambda8_(forall_var_3_):
            d_134_ch_: str = forall_var_3_
            return not ((d_134_ch_) in (s)) or (HexStrings.default__.IsHexChar(d_134_ch_))

        return _dafny.quantifier((s).UniqueElements, True, lambda8_)

    @staticmethod
    def IsLooseHexString(s):
        def lambda9_(forall_var_4_):
            d_135_ch_: str = forall_var_4_
            return not ((d_135_ch_) in (s)) or (HexStrings.default__.IsLooseHexChar(d_135_ch_))

        return _dafny.quantifier((s).UniqueElements, True, lambda9_)

    @staticmethod
    def HexVal(ch):
        if (('0') <= (ch)) and ((ch) <= ('9')):
            return (ord(ch)) - (ord('0'))
        elif (('a') <= (ch)) and ((ch) <= ('f')):
            return ((ord(ch)) - (ord('a'))) + (10)
        elif True:
            return ((ord(ch)) - (ord('A'))) + (10)

    @staticmethod
    def HexStr(x):
        if (x) < (16):
            d_136_res_ = _dafny.Seq(['0', HexStrings.default__.HexChar(x)])
            return d_136_res_
        elif True:
            d_137_res_ = _dafny.Seq([HexStrings.default__.HexChar(_dafny.euclidian_division(x, 16)), HexStrings.default__.HexChar(_dafny.euclidian_modulus(x, 16))])
            return d_137_res_

    @staticmethod
    def HexValue(x):
        return ((HexStrings.default__.HexVal((x)[0])) * (16)) + (HexStrings.default__.HexVal((x)[1]))

    @staticmethod
    def ToHexString(val):
        d_138___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(val)) == (0):
                    return (d_138___accumulator_) + (_dafny.Seq([]))
                elif True:
                    d_138___accumulator_ = (d_138___accumulator_) + (HexStrings.default__.HexStr((val)[0]))
                    in24_ = _dafny.Seq((val)[1::])
                    val = in24_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def FromHexString(data):
        d_139___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(data)) == (0):
                    return (d_139___accumulator_) + (_dafny.Seq([]))
                elif (_dafny.euclidian_modulus(len(data), 2)) == (1):
                    d_139___accumulator_ = (d_139___accumulator_) + (_dafny.Seq([HexStrings.default__.HexVal((data)[0])]))
                    in25_ = _dafny.Seq((data)[1::])
                    data = in25_
                    raise _dafny.TailCall()
                elif True:
                    d_139___accumulator_ = (d_139___accumulator_) + (_dafny.Seq([HexStrings.default__.HexValue(_dafny.Seq((data)[:2:]))]))
                    in26_ = _dafny.Seq((data)[2::])
                    data = in26_
                    raise _dafny.TailCall()
                break


class HexString:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})

class LooseHexString:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
