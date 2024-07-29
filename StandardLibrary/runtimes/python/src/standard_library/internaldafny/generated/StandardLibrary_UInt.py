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
        d_177_b0_ = _dafny.euclidian_division(x, 256)
        d_178_b1_ = _dafny.euclidian_modulus(x, 256)
        return _dafny.Seq([d_177_b0_, d_178_b1_])

    @staticmethod
    def SeqToUInt16(s):
        d_179_x0_ = ((s)[0]) * (256)
        return (d_179_x0_) + ((s)[1])

    @staticmethod
    def UInt32ToSeq(x):
        d_180_b0_ = _dafny.euclidian_division(x, 16777216)
        d_181_x0_ = (x) - ((d_180_b0_) * (16777216))
        d_182_b1_ = _dafny.euclidian_division(d_181_x0_, 65536)
        d_183_x1_ = (d_181_x0_) - ((d_182_b1_) * (65536))
        d_184_b2_ = _dafny.euclidian_division(d_183_x1_, 256)
        d_185_b3_ = _dafny.euclidian_modulus(d_183_x1_, 256)
        return _dafny.Seq([d_180_b0_, d_182_b1_, d_184_b2_, d_185_b3_])

    @staticmethod
    def SeqToUInt32(s):
        d_186_x0_ = ((s)[0]) * (16777216)
        d_187_x1_ = (d_186_x0_) + (((s)[1]) * (65536))
        d_188_x2_ = (d_187_x1_) + (((s)[2]) * (256))
        return (d_188_x2_) + ((s)[3])

    @staticmethod
    def UInt64ToSeq(x):
        d_189_b0_ = _dafny.euclidian_division(x, 72057594037927936)
        d_190_x0_ = (x) - ((d_189_b0_) * (72057594037927936))
        d_191_b1_ = _dafny.euclidian_division(d_190_x0_, 281474976710656)
        d_192_x1_ = (d_190_x0_) - ((d_191_b1_) * (281474976710656))
        d_193_b2_ = _dafny.euclidian_division(d_192_x1_, 1099511627776)
        d_194_x2_ = (d_192_x1_) - ((d_193_b2_) * (1099511627776))
        d_195_b3_ = _dafny.euclidian_division(d_194_x2_, 4294967296)
        d_196_x3_ = (d_194_x2_) - ((d_195_b3_) * (4294967296))
        d_197_b4_ = _dafny.euclidian_division(d_196_x3_, 16777216)
        d_198_x4_ = (d_196_x3_) - ((d_197_b4_) * (16777216))
        d_199_b5_ = _dafny.euclidian_division(d_198_x4_, 65536)
        d_200_x5_ = (d_198_x4_) - ((d_199_b5_) * (65536))
        d_201_b6_ = _dafny.euclidian_division(d_200_x5_, 256)
        d_202_b7_ = _dafny.euclidian_modulus(d_200_x5_, 256)
        return _dafny.Seq([d_189_b0_, d_191_b1_, d_193_b2_, d_195_b3_, d_197_b4_, d_199_b5_, d_201_b6_, d_202_b7_])

    @staticmethod
    def SeqToUInt64(s):
        d_203_x0_ = ((s)[0]) * (72057594037927936)
        d_204_x1_ = (d_203_x0_) + (((s)[1]) * (281474976710656))
        d_205_x2_ = (d_204_x1_) + (((s)[2]) * (1099511627776))
        d_206_x3_ = (d_205_x2_) + (((s)[3]) * (4294967296))
        d_207_x4_ = (d_206_x3_) + (((s)[4]) * (16777216))
        d_208_x5_ = (d_207_x4_) + (((s)[5]) * (65536))
        d_209_x6_ = (d_208_x5_) + (((s)[6]) * (256))
        d_210_x_ = (d_209_x6_) + ((s)[7])
        return d_210_x_

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
        d_211_s_: _dafny.Seq = source__
        return default__.HasUint16Len(d_211_s_)

class seq32:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_212_s_: _dafny.Seq = source__
        return default__.HasUint32Len(d_212_s_)

class seq64:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_213_s_: _dafny.Seq = source__
        return default__.HasUint64Len(d_213_s_)
