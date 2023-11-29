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

# assert "StandardLibrary_mUInt" == __name__
StandardLibrary_mUInt = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def UInt8Less(a, b):
        return (a) < (b)

    @staticmethod
    def HasUint16Len(s):
        return (len(s)) < ((StandardLibrary_mUInt.default__).UINT16__LIMIT)

    @staticmethod
    def HasUint32Len(s):
        return (len(s)) < ((StandardLibrary_mUInt.default__).UINT32__LIMIT)

    @staticmethod
    def HasUint64Len(s):
        return (len(s)) < ((StandardLibrary_mUInt.default__).UINT64__LIMIT)

    @staticmethod
    def UInt16ToSeq(x):
        d_173_b0_ = _dafny.euclidian_division(x, 256)
        d_174_b1_ = _dafny.euclidian_modulus(x, 256)
        return _dafny.Seq([d_173_b0_, d_174_b1_])

    @staticmethod
    def SeqToUInt16(s):
        d_175_x0_ = ((s)[0]) * (256)
        return (d_175_x0_) + ((s)[1])

    @staticmethod
    def UInt32ToSeq(x):
        d_176_b0_ = _dafny.euclidian_division(x, 16777216)
        d_177_x0_ = (x) - ((d_176_b0_) * (16777216))
        d_178_b1_ = _dafny.euclidian_division(d_177_x0_, 65536)
        d_179_x1_ = (d_177_x0_) - ((d_178_b1_) * (65536))
        d_180_b2_ = _dafny.euclidian_division(d_179_x1_, 256)
        d_181_b3_ = _dafny.euclidian_modulus(d_179_x1_, 256)
        return _dafny.Seq([d_176_b0_, d_178_b1_, d_180_b2_, d_181_b3_])

    @staticmethod
    def SeqToUInt32(s):
        d_182_x0_ = ((s)[0]) * (16777216)
        d_183_x1_ = (d_182_x0_) + (((s)[1]) * (65536))
        d_184_x2_ = (d_183_x1_) + (((s)[2]) * (256))
        return (d_184_x2_) + ((s)[3])

    @staticmethod
    def UInt64ToSeq(x):
        d_185_b0_ = _dafny.euclidian_division(x, 72057594037927936)
        d_186_x0_ = (x) - ((d_185_b0_) * (72057594037927936))
        d_187_b1_ = _dafny.euclidian_division(d_186_x0_, 281474976710656)
        d_188_x1_ = (d_186_x0_) - ((d_187_b1_) * (281474976710656))
        d_189_b2_ = _dafny.euclidian_division(d_188_x1_, 1099511627776)
        d_190_x2_ = (d_188_x1_) - ((d_189_b2_) * (1099511627776))
        d_191_b3_ = _dafny.euclidian_division(d_190_x2_, 4294967296)
        d_192_x3_ = (d_190_x2_) - ((d_191_b3_) * (4294967296))
        d_193_b4_ = _dafny.euclidian_division(d_192_x3_, 16777216)
        d_194_x4_ = (d_192_x3_) - ((d_193_b4_) * (16777216))
        d_195_b5_ = _dafny.euclidian_division(d_194_x4_, 65536)
        d_196_x5_ = (d_194_x4_) - ((d_195_b5_) * (65536))
        d_197_b6_ = _dafny.euclidian_division(d_196_x5_, 256)
        d_198_b7_ = _dafny.euclidian_modulus(d_196_x5_, 256)
        return _dafny.Seq([d_185_b0_, d_187_b1_, d_189_b2_, d_191_b3_, d_193_b4_, d_195_b5_, d_197_b6_, d_198_b7_])

    @staticmethod
    def SeqToUInt64(s):
        d_199_x0_ = ((s)[0]) * (72057594037927936)
        d_200_x1_ = (d_199_x0_) + (((s)[1]) * (281474976710656))
        d_201_x2_ = (d_200_x1_) + (((s)[2]) * (1099511627776))
        d_202_x3_ = (d_201_x2_) + (((s)[3]) * (4294967296))
        d_203_x4_ = (d_202_x3_) + (((s)[4]) * (16777216))
        d_204_x5_ = (d_203_x4_) + (((s)[5]) * (65536))
        d_205_x6_ = (d_204_x5_) + (((s)[6]) * (256))
        d_206_x_ = (d_205_x6_) + ((s)[7])
        return d_206_x_

    @_dafny.classproperty
    def UINT16__LIMIT(instance):
        return ((BoundedInts.default__).UINT16__MAX) + (1)
    @_dafny.classproperty
    def UINT32__LIMIT(instance):
        return ((BoundedInts.default__).UINT32__MAX) + (1)
    @_dafny.classproperty
    def UINT64__LIMIT(instance):
        return ((BoundedInts.default__).UINT64__MAX) + (1)
    @_dafny.classproperty
    def INT32__MAX__LIMIT(instance):
        return (BoundedInts.default__).INT32__MAX
    @_dafny.classproperty
    def INT64__MAX__LIMIT(instance):
        return (BoundedInts.default__).INT64__MAX

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
