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

# Module: standard_library.internaldafny.generated.StandardLibrary_UInt

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
        d_186_b0_ = _dafny.euclidian_division(x, 256)
        d_187_b1_ = _dafny.euclidian_modulus(x, 256)
        return _dafny.Seq([d_186_b0_, d_187_b1_])

    @staticmethod
    def SeqToUInt16(s):
        d_188_x0_ = ((s)[0]) * (256)
        return (d_188_x0_) + ((s)[1])

    @staticmethod
    def UInt32ToSeq(x):
        d_189_b0_ = _dafny.euclidian_division(x, 16777216)
        d_190_x0_ = (x) - ((d_189_b0_) * (16777216))
        d_191_b1_ = _dafny.euclidian_division(d_190_x0_, 65536)
        d_192_x1_ = (d_190_x0_) - ((d_191_b1_) * (65536))
        d_193_b2_ = _dafny.euclidian_division(d_192_x1_, 256)
        d_194_b3_ = _dafny.euclidian_modulus(d_192_x1_, 256)
        return _dafny.Seq([d_189_b0_, d_191_b1_, d_193_b2_, d_194_b3_])

    @staticmethod
    def SeqToUInt32(s):
        d_195_x0_ = ((s)[0]) * (16777216)
        d_196_x1_ = (d_195_x0_) + (((s)[1]) * (65536))
        d_197_x2_ = (d_196_x1_) + (((s)[2]) * (256))
        return (d_197_x2_) + ((s)[3])

    @staticmethod
    def UInt64ToSeq(x):
        d_198_b0_ = _dafny.euclidian_division(x, 72057594037927936)
        d_199_x0_ = (x) - ((d_198_b0_) * (72057594037927936))
        d_200_b1_ = _dafny.euclidian_division(d_199_x0_, 281474976710656)
        d_201_x1_ = (d_199_x0_) - ((d_200_b1_) * (281474976710656))
        d_202_b2_ = _dafny.euclidian_division(d_201_x1_, 1099511627776)
        d_203_x2_ = (d_201_x1_) - ((d_202_b2_) * (1099511627776))
        d_204_b3_ = _dafny.euclidian_division(d_203_x2_, 4294967296)
        d_205_x3_ = (d_203_x2_) - ((d_204_b3_) * (4294967296))
        d_206_b4_ = _dafny.euclidian_division(d_205_x3_, 16777216)
        d_207_x4_ = (d_205_x3_) - ((d_206_b4_) * (16777216))
        d_208_b5_ = _dafny.euclidian_division(d_207_x4_, 65536)
        d_209_x5_ = (d_207_x4_) - ((d_208_b5_) * (65536))
        d_210_b6_ = _dafny.euclidian_division(d_209_x5_, 256)
        d_211_b7_ = _dafny.euclidian_modulus(d_209_x5_, 256)
        return _dafny.Seq([d_198_b0_, d_200_b1_, d_202_b2_, d_204_b3_, d_206_b4_, d_208_b5_, d_210_b6_, d_211_b7_])

    @staticmethod
    def SeqToUInt64(s):
        d_212_x0_ = ((s)[0]) * (72057594037927936)
        d_213_x1_ = (d_212_x0_) + (((s)[1]) * (281474976710656))
        d_214_x2_ = (d_213_x1_) + (((s)[2]) * (1099511627776))
        d_215_x3_ = (d_214_x2_) + (((s)[3]) * (4294967296))
        d_216_x4_ = (d_215_x3_) + (((s)[4]) * (16777216))
        d_217_x5_ = (d_216_x4_) + (((s)[5]) * (65536))
        d_218_x6_ = (d_217_x5_) + (((s)[6]) * (256))
        d_219_x_ = (d_218_x6_) + ((s)[7])
        return d_219_x_

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
        d_220_s_: _dafny.Seq = source__
        return default__.HasUint16Len(d_220_s_)

class seq32:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_221_s_: _dafny.Seq = source__
        return default__.HasUint32Len(d_221_s_)

class seq64:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return _dafny.Seq({})
    def _Is(source__):
        d_222_s_: _dafny.Seq = source__
        return default__.HasUint64Len(d_222_s_)
