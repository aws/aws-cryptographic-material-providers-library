import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import standard_library.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import standard_library.internaldafny.generated.Wrappers as Wrappers
import standard_library.internaldafny.generated.Relations as Relations
import standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import standard_library.internaldafny.generated.Math as Math
import standard_library.internaldafny.generated.Seq as Seq
import standard_library.internaldafny.generated.BoundedInts as BoundedInts
import standard_library.internaldafny.generated.Unicode as Unicode
import standard_library.internaldafny.generated.Functions as Functions
import standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import standard_library.internaldafny.generated.FileIO as FileIO
import standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import standard_library.internaldafny.generated.MulInternals as MulInternals
import standard_library.internaldafny.generated.Mul as Mul
import standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import standard_library.internaldafny.generated.ModInternals as ModInternals
import standard_library.internaldafny.generated.DivInternals as DivInternals
import standard_library.internaldafny.generated.DivMod as DivMod
import standard_library.internaldafny.generated.Power as Power
import standard_library.internaldafny.generated.Logarithm as Logarithm
import standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import standard_library.internaldafny.generated.UUID as UUID

# Module: standard_library.internaldafny.generated.UTF8

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def CreateEncodeSuccess(bytes):
        return Wrappers.Result_Success(bytes)

    @staticmethod
    def CreateEncodeFailure(error):
        return Wrappers.Result_Failure(error)

    @staticmethod
    def CreateDecodeSuccess(s):
        return Wrappers.Result_Success(s)

    @staticmethod
    def CreateDecodeFailure(error):
        return Wrappers.Result_Failure(error)

    @staticmethod
    def IsASCIIString(s):
        def lambda20_(forall_var_2_):
            d_243_i_: int = forall_var_2_
            return not (((0) <= (d_243_i_)) and ((d_243_i_) < (len(s)))) or ((ord((s)[d_243_i_])) < (128))

        return _dafny.quantifier(_dafny.IntegerRange(0, len(s)), True, lambda20_)

    @staticmethod
    def EncodeAscii(s):
        d_244___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(s)) == (0):
                    return (d_244___accumulator_) + (_dafny.Seq([]))
                elif True:
                    d_245_x_ = _dafny.Seq([ord((s)[0])])
                    d_244___accumulator_ = (d_244___accumulator_) + (d_245_x_)
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
                    d_246_r_ = _dafny.Seq((a)[lo:hi:])
                    if default__.Uses1Byte(d_246_r_):
                        in54_ = a
                        in55_ = (lo) + (1)
                        in56_ = hi
                        a = in54_
                        lo = in55_
                        hi = in56_
                        raise _dafny.TailCall()
                    elif ((2) <= (len(d_246_r_))) and (default__.Uses2Bytes(d_246_r_)):
                        in57_ = a
                        in58_ = (lo) + (2)
                        in59_ = hi
                        a = in57_
                        lo = in58_
                        hi = in59_
                        raise _dafny.TailCall()
                    elif ((3) <= (len(d_246_r_))) and (default__.Uses3Bytes(d_246_r_)):
                        in60_ = a
                        in61_ = (lo) + (3)
                        in62_ = hi
                        a = in60_
                        lo = in61_
                        hi = in62_
                        raise _dafny.TailCall()
                    elif ((4) <= (len(d_246_r_))) and (default__.Uses4Bytes(d_246_r_)):
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
    def _Is(source__):
        d_247_i_: _dafny.Seq = source__
        return default__.ValidUTF8Seq(d_247_i_)
