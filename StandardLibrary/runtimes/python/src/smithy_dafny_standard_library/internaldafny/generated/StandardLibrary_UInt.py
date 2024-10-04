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

# Module: StandardLibrary_UInt

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def UInt8Less(a, b):
        return (a) < (b)

    @staticmethod
    def HasUint16Len(s):
        return (len(s)) < (default__.UINT16__LIMIT)

    @staticmethod
    def HasUint32Len(s):
        return (len(s)) < (default__.UINT32__LIMIT)

    @staticmethod
    def HasUint64Len(s):
        return (len(s)) < (default__.UINT64__LIMIT)

    @staticmethod
    def UInt16ToSeq(x):
        d_0_b0_ = _dafny.euclidian_division(x, 256)
        d_1_b1_ = _dafny.euclidian_modulus(x, 256)
        return _dafny.Seq([d_0_b0_, d_1_b1_])

    @staticmethod
    def SeqToUInt16(s):
        d_0_x0_ = ((s)[0]) * (256)
        return (d_0_x0_) + ((s)[1])

    @staticmethod
    def UInt32ToSeq(x):
        d_0_b0_ = _dafny.euclidian_division(x, 16777216)
        d_1_x0_ = (x) - ((d_0_b0_) * (16777216))
        d_2_b1_ = _dafny.euclidian_division(d_1_x0_, 65536)
        d_3_x1_ = (d_1_x0_) - ((d_2_b1_) * (65536))
        d_4_b2_ = _dafny.euclidian_division(d_3_x1_, 256)
        d_5_b3_ = _dafny.euclidian_modulus(d_3_x1_, 256)
        return _dafny.Seq([d_0_b0_, d_2_b1_, d_4_b2_, d_5_b3_])

    @staticmethod
    def SeqToUInt32(s):
        d_0_x0_ = ((s)[0]) * (16777216)
        d_1_x1_ = (d_0_x0_) + (((s)[1]) * (65536))
        d_2_x2_ = (d_1_x1_) + (((s)[2]) * (256))
        return (d_2_x2_) + ((s)[3])

    @staticmethod
    def UInt64ToSeq(x):
        d_0_b0_ = _dafny.euclidian_division(x, 72057594037927936)
        d_1_x0_ = (x) - ((d_0_b0_) * (72057594037927936))
        d_2_b1_ = _dafny.euclidian_division(d_1_x0_, 281474976710656)
        d_3_x1_ = (d_1_x0_) - ((d_2_b1_) * (281474976710656))
        d_4_b2_ = _dafny.euclidian_division(d_3_x1_, 1099511627776)
        d_5_x2_ = (d_3_x1_) - ((d_4_b2_) * (1099511627776))
        d_6_b3_ = _dafny.euclidian_division(d_5_x2_, 4294967296)
        d_7_x3_ = (d_5_x2_) - ((d_6_b3_) * (4294967296))
        d_8_b4_ = _dafny.euclidian_division(d_7_x3_, 16777216)
        d_9_x4_ = (d_7_x3_) - ((d_8_b4_) * (16777216))
        d_10_b5_ = _dafny.euclidian_division(d_9_x4_, 65536)
        d_11_x5_ = (d_9_x4_) - ((d_10_b5_) * (65536))
        d_12_b6_ = _dafny.euclidian_division(d_11_x5_, 256)
        d_13_b7_ = _dafny.euclidian_modulus(d_11_x5_, 256)
        return _dafny.Seq([d_0_b0_, d_2_b1_, d_4_b2_, d_6_b3_, d_8_b4_, d_10_b5_, d_12_b6_, d_13_b7_])

    @staticmethod
    def SeqToUInt64(s):
        d_0_x0_ = ((s)[0]) * (72057594037927936)
        d_1_x1_ = (d_0_x0_) + (((s)[1]) * (281474976710656))
        d_2_x2_ = (d_1_x1_) + (((s)[2]) * (1099511627776))
        d_3_x3_ = (d_2_x2_) + (((s)[3]) * (4294967296))
        d_4_x4_ = (d_3_x3_) + (((s)[4]) * (16777216))
        d_5_x5_ = (d_4_x4_) + (((s)[5]) * (65536))
        d_6_x6_ = (d_5_x5_) + (((s)[6]) * (256))
        d_7_x_ = (d_6_x6_) + ((s)[7])
        return d_7_x_

    @_dafny.classproperty
    def UINT16__LIMIT(instance):
        return (BoundedInts.default__.UINT16__MAX) + (1)
    @_dafny.classproperty
    def UINT32__LIMIT(instance):
        return (BoundedInts.default__.UINT32__MAX) + (1)
    @_dafny.classproperty
    def UINT64__LIMIT(instance):
        return (BoundedInts.default__.UINT64__MAX) + (1)
    @_dafny.classproperty
    def INT32__MAX__LIMIT(instance):
        return BoundedInts.default__.INT32__MAX
    @_dafny.classproperty
    def INT64__MAX__LIMIT(instance):
        return BoundedInts.default__.INT64__MAX

class seq16:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_0_s_: _dafny.Seq = source__
        return default__.HasUint16Len(d_0_s_)

class seq32:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_1_s_: _dafny.Seq = source__
        return default__.HasUint32Len(d_1_s_)

class seq64:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_2_s_: _dafny.Seq = source__
        return default__.HasUint64Len(d_2_s_)
