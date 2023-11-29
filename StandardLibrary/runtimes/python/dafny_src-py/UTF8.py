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

# Module: UTF8

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def IsASCIIString(s):
        def lambda20_(forall_var_2_):
            d_227_i_: int = forall_var_2_
            return not (((0) <= (d_227_i_)) and ((d_227_i_) < (len(s)))) or ((ord((s)[d_227_i_])) < (128))

        return _dafny.quantifier(_dafny.IntegerRange(0, len(s)), True, lambda20_)

    @staticmethod
    def EncodeAscii(s):
        d_228___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(s)) == (0):
                    return (d_228___accumulator_) + (_dafny.Seq([]))
                elif True:
                    d_229_x_ = _dafny.Seq([ord((s)[0])])
                    d_228___accumulator_ = (d_228___accumulator_) + (d_229_x_)
                    in53_ = _dafny.Seq((s)[1::])
                    s = in53_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def Uses1Byte(s):
        return ((0) <= ((s)[0])) and (((s)[0]) <= (127))

    @staticmethod
    def Uses2Bytes(s):
        return (((194) <= ((s)[0])) and (((s)[0]) <= (223))) and (((128) <= ((s)[1])) and (((s)[1]) <= (191)))

    @staticmethod
    def Uses3Bytes(s):
        return (((((((s)[0]) == (224)) and (((160) <= ((s)[1])) and (((s)[1]) <= (191)))) and (((128) <= ((s)[2])) and (((s)[2]) <= (191)))) or (((((225) <= ((s)[0])) and (((s)[0]) <= (236))) and (((128) <= ((s)[1])) and (((s)[1]) <= (191)))) and (((128) <= ((s)[2])) and (((s)[2]) <= (191))))) or (((((s)[0]) == (237)) and (((128) <= ((s)[1])) and (((s)[1]) <= (159)))) and (((128) <= ((s)[2])) and (((s)[2]) <= (191))))) or (((((238) <= ((s)[0])) and (((s)[0]) <= (239))) and (((128) <= ((s)[1])) and (((s)[1]) <= (191)))) and (((128) <= ((s)[2])) and (((s)[2]) <= (191))))

    @staticmethod
    def Uses4Bytes(s):
        return (((((((s)[0]) == (240)) and (((144) <= ((s)[1])) and (((s)[1]) <= (191)))) and (((128) <= ((s)[2])) and (((s)[2]) <= (191)))) and (((128) <= ((s)[3])) and (((s)[3]) <= (191)))) or ((((((241) <= ((s)[0])) and (((s)[0]) <= (243))) and (((128) <= ((s)[1])) and (((s)[1]) <= (191)))) and (((128) <= ((s)[2])) and (((s)[2]) <= (191)))) and (((128) <= ((s)[3])) and (((s)[3]) <= (191))))) or ((((((s)[0]) == (244)) and (((128) <= ((s)[1])) and (((s)[1]) <= (143)))) and (((128) <= ((s)[2])) and (((s)[2]) <= (191)))) and (((128) <= ((s)[3])) and (((s)[3]) <= (191))))

    @staticmethod
    def ValidUTF8Range(a, lo, hi):
        while True:
            with _dafny.label():
                if (lo) == (hi):
                    return True
                elif True:
                    d_230_r_ = _dafny.Seq((a)[lo:hi:])
                    if default__.Uses1Byte(d_230_r_):
                        in54_ = a
                        in55_ = (lo) + (1)
                        in56_ = hi
                        a = in54_
                        lo = in55_
                        hi = in56_
                        raise _dafny.TailCall()
                    elif ((2) <= (len(d_230_r_))) and (default__.Uses2Bytes(d_230_r_)):
                        in57_ = a
                        in58_ = (lo) + (2)
                        in59_ = hi
                        a = in57_
                        lo = in58_
                        hi = in59_
                        raise _dafny.TailCall()
                    elif ((3) <= (len(d_230_r_))) and (default__.Uses3Bytes(d_230_r_)):
                        in60_ = a
                        in61_ = (lo) + (3)
                        in62_ = hi
                        a = in60_
                        lo = in61_
                        hi = in62_
                        raise _dafny.TailCall()
                    elif ((4) <= (len(d_230_r_))) and (default__.Uses4Bytes(d_230_r_)):
                        in63_ = a
                        in64_ = (lo) + (4)
                        in65_ = hi
                        a = in63_
                        lo = in64_
                        hi = in65_
                        raise _dafny.TailCall()
                    elif True:
                        return False
                break

    @staticmethod
    def ValidUTF8Seq(s):
        return default__.ValidUTF8Range(s, 0, len(s))


class ValidUTF8Bytes:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq([])
