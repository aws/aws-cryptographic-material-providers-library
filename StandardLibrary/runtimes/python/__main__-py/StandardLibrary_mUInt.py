import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import BoundedInts

# Module: StandardLibrary_mUInt

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
        d_18_b0_ = _dafny.euclidian_division(x, 256)
        d_19_b1_ = _dafny.euclidian_modulus(x, 256)
        return _dafny.Seq([d_18_b0_, d_19_b1_])

    @staticmethod
    def SeqToUInt16(s):
        d_20_x0_ = ((s)[0]) * (256)
        return (d_20_x0_) + ((s)[1])

    @staticmethod
    def UInt32ToSeq(x):
        d_21_b0_ = _dafny.euclidian_division(x, 16777216)
        d_22_x0_ = (x) - ((d_21_b0_) * (16777216))
        d_23_b1_ = _dafny.euclidian_division(d_22_x0_, 65536)
        d_24_x1_ = (d_22_x0_) - ((d_23_b1_) * (65536))
        d_25_b2_ = _dafny.euclidian_division(d_24_x1_, 256)
        d_26_b3_ = _dafny.euclidian_modulus(d_24_x1_, 256)
        return _dafny.Seq([d_21_b0_, d_23_b1_, d_25_b2_, d_26_b3_])

    @staticmethod
    def SeqToUInt32(s):
        d_27_x0_ = ((s)[0]) * (16777216)
        d_28_x1_ = (d_27_x0_) + (((s)[1]) * (65536))
        d_29_x2_ = (d_28_x1_) + (((s)[2]) * (256))
        return (d_29_x2_) + ((s)[3])

    @staticmethod
    def UInt64ToSeq(x):
        d_30_b0_ = _dafny.euclidian_division(x, 72057594037927936)
        d_31_x0_ = (x) - ((d_30_b0_) * (72057594037927936))
        d_32_b1_ = _dafny.euclidian_division(d_31_x0_, 281474976710656)
        d_33_x1_ = (d_31_x0_) - ((d_32_b1_) * (281474976710656))
        d_34_b2_ = _dafny.euclidian_division(d_33_x1_, 1099511627776)
        d_35_x2_ = (d_33_x1_) - ((d_34_b2_) * (1099511627776))
        d_36_b3_ = _dafny.euclidian_division(d_35_x2_, 4294967296)
        d_37_x3_ = (d_35_x2_) - ((d_36_b3_) * (4294967296))
        d_38_b4_ = _dafny.euclidian_division(d_37_x3_, 16777216)
        d_39_x4_ = (d_37_x3_) - ((d_38_b4_) * (16777216))
        d_40_b5_ = _dafny.euclidian_division(d_39_x4_, 65536)
        d_41_x5_ = (d_39_x4_) - ((d_40_b5_) * (65536))
        d_42_b6_ = _dafny.euclidian_division(d_41_x5_, 256)
        d_43_b7_ = _dafny.euclidian_modulus(d_41_x5_, 256)
        return _dafny.Seq([d_30_b0_, d_32_b1_, d_34_b2_, d_36_b3_, d_38_b4_, d_40_b5_, d_42_b6_, d_43_b7_])

    @staticmethod
    def SeqToUInt64(s):
        d_44_x0_ = ((s)[0]) * (72057594037927936)
        d_45_x1_ = (d_44_x0_) + (((s)[1]) * (281474976710656))
        d_46_x2_ = (d_45_x1_) + (((s)[2]) * (1099511627776))
        d_47_x3_ = (d_46_x2_) + (((s)[3]) * (4294967296))
        d_48_x4_ = (d_47_x3_) + (((s)[4]) * (16777216))
        d_49_x5_ = (d_48_x4_) + (((s)[5]) * (65536))
        d_50_x6_ = (d_49_x5_) + (((s)[6]) * (256))
        d_51_x_ = (d_50_x6_) + ((s)[7])
        return d_51_x_

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

class seq32:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})

class seq64:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
