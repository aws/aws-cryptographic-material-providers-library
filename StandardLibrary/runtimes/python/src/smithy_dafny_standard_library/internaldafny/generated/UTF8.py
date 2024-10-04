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

# Module: UTF8

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
        def lambda0_(forall_var_0_):
            d_0_i_: int = forall_var_0_
            return not (((0) <= (d_0_i_)) and ((d_0_i_) < (len(s)))) or ((ord((s)[d_0_i_])) < (128))

        return _dafny.quantifier(_dafny.IntegerRange(0, len(s)), True, lambda0_)

    @staticmethod
    def EncodeAscii(s):
        d_0___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(s)) == (0):
                    return (d_0___accumulator_) + (_dafny.Seq([]))
                elif True:
                    d_1_x_ = _dafny.Seq([ord((s)[0])])
                    d_0___accumulator_ = (d_0___accumulator_) + (d_1_x_)
                    in0_ = _dafny.Seq((s)[1::])
                    s = in0_
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
                    d_0_r_ = _dafny.Seq((a)[lo:hi:])
                    if default__.Uses1Byte(d_0_r_):
                        in0_ = a
                        in1_ = (lo) + (1)
                        in2_ = hi
                        a = in0_
                        lo = in1_
                        hi = in2_
                        raise _dafny.TailCall()
                    elif ((2) <= (len(d_0_r_))) and (default__.Uses2Bytes(d_0_r_)):
                        in3_ = a
                        in4_ = (lo) + (2)
                        in5_ = hi
                        a = in3_
                        lo = in4_
                        hi = in5_
                        raise _dafny.TailCall()
                    elif ((3) <= (len(d_0_r_))) and (default__.Uses3Bytes(d_0_r_)):
                        in6_ = a
                        in7_ = (lo) + (3)
                        in8_ = hi
                        a = in6_
                        lo = in7_
                        hi = in8_
                        raise _dafny.TailCall()
                    elif ((4) <= (len(d_0_r_))) and (default__.Uses4Bytes(d_0_r_)):
                        in9_ = a
                        in10_ = (lo) + (4)
                        in11_ = hi
                        a = in9_
                        lo = in10_
                        hi = in11_
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
        d_0_i_: _dafny.Seq = source__
        return default__.ValidUTF8Seq(d_0_i_)
