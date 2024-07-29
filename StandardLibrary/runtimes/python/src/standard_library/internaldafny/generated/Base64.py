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
import standard_library.internaldafny.generated.UTF8 as UTF8
import standard_library.internaldafny.generated.Time as Time
import standard_library.internaldafny.generated.Streams as Streams
import standard_library.internaldafny.generated.Sorting as Sorting
import standard_library.internaldafny.generated.SortedSets as SortedSets
import standard_library.internaldafny.generated.HexStrings as HexStrings
import standard_library.internaldafny.generated.GetOpt as GetOpt
import standard_library.internaldafny.generated.FloatCompare as FloatCompare
import standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall

# Module: Base64

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def IsBase64Char(c):
        return (((((c) == ('+')) or ((c) == ('/'))) or ((('0') <= (c)) and ((c) <= ('9')))) or ((('A') <= (c)) and ((c) <= ('Z')))) or ((('a') <= (c)) and ((c) <= ('z')))

    @staticmethod
    def IsUnpaddedBase64String(s):
        def lambda26_(forall_var_6_):
            d_371_k_: str = forall_var_6_
            return not ((d_371_k_) in (s)) or (default__.IsBase64Char(d_371_k_))

        return ((_dafny.euclidian_modulus(len(s), 4)) == (0)) and (_dafny.quantifier((s).UniqueElements, True, lambda26_))

    @staticmethod
    def IndexToChar(i):
        if (i) == (63):
            return '/'
        elif (i) == (62):
            return '+'
        elif ((52) <= (i)) and ((i) <= (61)):
            return chr((i) - (4))
        elif ((26) <= (i)) and ((i) <= (51)):
            return _dafny.plus_char(chr(i), chr(71))
        elif True:
            return _dafny.plus_char(chr(i), chr(65))

    @staticmethod
    def CharToIndex(c):
        if (c) == ('/'):
            return 63
        elif (c) == ('+'):
            return 62
        elif (('0') <= (c)) and ((c) <= ('9')):
            return ord(_dafny.plus_char(c, chr(4)))
        elif (('a') <= (c)) and ((c) <= ('z')):
            return ord(_dafny.minus_char(c, chr(71)))
        elif True:
            return ord(_dafny.minus_char(c, chr(65)))

    @staticmethod
    def UInt24ToSeq(x):
        d_372_b0_ = _dafny.euclidian_division(x, 65536)
        d_373_x0_ = (x) - ((d_372_b0_) * (65536))
        d_374_b1_ = _dafny.euclidian_division(d_373_x0_, 256)
        d_375_b2_ = _dafny.euclidian_modulus(d_373_x0_, 256)
        return _dafny.Seq([d_372_b0_, d_374_b1_, d_375_b2_])

    @staticmethod
    def SeqToUInt24(s):
        return ((((s)[0]) * (65536)) + (((s)[1]) * (256))) + ((s)[2])

    @staticmethod
    def UInt24ToIndexSeq(x):
        d_376_b0_ = _dafny.euclidian_division(x, 262144)
        d_377_x0_ = (x) - ((d_376_b0_) * (262144))
        d_378_b1_ = _dafny.euclidian_division(d_377_x0_, 4096)
        d_379_x1_ = (d_377_x0_) - ((d_378_b1_) * (4096))
        d_380_b2_ = _dafny.euclidian_division(d_379_x1_, 64)
        d_381_b3_ = _dafny.euclidian_modulus(d_379_x1_, 64)
        return _dafny.Seq([d_376_b0_, d_378_b1_, d_380_b2_, d_381_b3_])

    @staticmethod
    def IndexSeqToUInt24(s):
        return (((((s)[0]) * (262144)) + (((s)[1]) * (4096))) + (((s)[2]) * (64))) + ((s)[3])

    @staticmethod
    def DecodeBlock(s):
        return default__.UInt24ToSeq(default__.IndexSeqToUInt24(s))

    @staticmethod
    def EncodeBlock(s):
        return default__.UInt24ToIndexSeq(default__.SeqToUInt24(s))

    @staticmethod
    def DecodeRecursively(s):
        d_382___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(s)) == (0):
                    return (d_382___accumulator_) + (_dafny.Seq([]))
                elif True:
                    d_382___accumulator_ = (d_382___accumulator_) + (default__.DecodeBlock(_dafny.Seq((s)[:4:])))
                    in182_ = _dafny.Seq((s)[4::])
                    s = in182_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def EncodeRecursively(b):
        d_383___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(b)) == (0):
                    return (d_383___accumulator_) + (_dafny.Seq([]))
                elif True:
                    d_383___accumulator_ = (d_383___accumulator_) + (default__.EncodeBlock(_dafny.Seq((b)[:3:])))
                    in183_ = _dafny.Seq((b)[3::])
                    b = in183_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def FromCharsToIndices(s):
        return _dafny.Seq([default__.CharToIndex((s)[d_384_i_]) for d_384_i_ in range(len(s))])

    @staticmethod
    def FromIndicesToChars(b):
        return _dafny.Seq([default__.IndexToChar((b)[d_385_i_]) for d_385_i_ in range(len(b))])

    @staticmethod
    def DecodeUnpadded(s):
        return default__.DecodeRecursively(default__.FromCharsToIndices(s))

    @staticmethod
    def EncodeUnpadded(b):
        return default__.FromIndicesToChars(default__.EncodeRecursively(b))

    @staticmethod
    def Is1Padding(s):
        return ((((((len(s)) == (4)) and (default__.IsBase64Char((s)[0]))) and (default__.IsBase64Char((s)[1]))) and (default__.IsBase64Char((s)[2]))) and ((_dafny.euclidian_modulus(default__.CharToIndex((s)[2]), 4)) == (0))) and (((s)[3]) == ('='))

    @staticmethod
    def Decode1Padding(s):
        d_386_d_ = default__.DecodeBlock(_dafny.Seq([default__.CharToIndex((s)[0]), default__.CharToIndex((s)[1]), default__.CharToIndex((s)[2]), 0]))
        return _dafny.Seq([(d_386_d_)[0], (d_386_d_)[1]])

    @staticmethod
    def Encode1Padding(b):
        d_387_e_ = default__.EncodeBlock(_dafny.Seq([(b)[0], (b)[1], 0]))
        return _dafny.Seq([default__.IndexToChar((d_387_e_)[0]), default__.IndexToChar((d_387_e_)[1]), default__.IndexToChar((d_387_e_)[2]), '='])

    @staticmethod
    def Is2Padding(s):
        return ((((((len(s)) == (4)) and (default__.IsBase64Char((s)[0]))) and (default__.IsBase64Char((s)[1]))) and ((_dafny.euclidian_modulus(default__.CharToIndex((s)[1]), 16)) == (0))) and (((s)[2]) == ('='))) and (((s)[3]) == ('='))

    @staticmethod
    def Decode2Padding(s):
        d_388_d_ = default__.DecodeBlock(_dafny.Seq([default__.CharToIndex((s)[0]), default__.CharToIndex((s)[1]), 0, 0]))
        return _dafny.Seq([(d_388_d_)[0]])

    @staticmethod
    def Encode2Padding(b):
        d_389_e_ = default__.EncodeBlock(_dafny.Seq([(b)[0], 0, 0]))
        return _dafny.Seq([default__.IndexToChar((d_389_e_)[0]), default__.IndexToChar((d_389_e_)[1]), '=', '='])

    @staticmethod
    def IsBase64String(s):
        d_390_finalBlockStart_ = (len(s)) - (4)
        return ((_dafny.euclidian_modulus(len(s), 4)) == (0)) and ((default__.IsUnpaddedBase64String(s)) or ((default__.IsUnpaddedBase64String(_dafny.Seq((s)[:d_390_finalBlockStart_:]))) and ((default__.Is1Padding(_dafny.Seq((s)[d_390_finalBlockStart_::]))) or (default__.Is2Padding(_dafny.Seq((s)[d_390_finalBlockStart_::]))))))

    @staticmethod
    def DecodeValid(s):
        if (s) == (_dafny.Seq([])):
            return _dafny.Seq([])
        elif True:
            d_391_finalBlockStart_ = (len(s)) - (4)
            d_392_prefix_ = _dafny.Seq((s)[:d_391_finalBlockStart_:])
            d_393_suffix_ = _dafny.Seq((s)[d_391_finalBlockStart_::])
            if default__.Is1Padding(d_393_suffix_):
                return (default__.DecodeUnpadded(d_392_prefix_)) + (default__.Decode1Padding(d_393_suffix_))
            elif default__.Is2Padding(d_393_suffix_):
                return (default__.DecodeUnpadded(d_392_prefix_)) + (default__.Decode2Padding(d_393_suffix_))
            elif True:
                return default__.DecodeUnpadded(s)

    @staticmethod
    def Decode(s):
        if default__.IsBase64String(s):
            return Wrappers.Result_Success(default__.DecodeValid(s))
        elif True:
            return Wrappers.Result_Failure(_dafny.Seq("The encoding is malformed"))

    @staticmethod
    def Encode(b):
        if (_dafny.euclidian_modulus(len(b), 3)) == (0):
            d_394_s_ = default__.EncodeUnpadded(b)
            return d_394_s_
        elif (_dafny.euclidian_modulus(len(b), 3)) == (1):
            d_395_s1_ = default__.EncodeUnpadded(_dafny.Seq((b)[:(len(b)) - (1):]))
            d_396_s2_ = default__.Encode2Padding(_dafny.Seq((b)[(len(b)) - (1)::]))
            d_397_s_ = (d_395_s1_) + (d_396_s2_)
            return d_397_s_
        elif True:
            d_398_s1_ = default__.EncodeUnpadded(_dafny.Seq((b)[:(len(b)) - (2):]))
            d_399_s2_ = default__.Encode1Padding(_dafny.Seq((b)[(len(b)) - (2)::]))
            d_400_s_ = (d_398_s1_) + (d_399_s2_)
            return d_400_s_


class index:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_401_x_: int = source__
        return ((0) <= (d_401_x_)) and ((d_401_x_) < (64))

class uint24:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
    def _Is(source__):
        d_402_x_: int = source__
        return ((0) <= (d_402_x_)) and ((d_402_x_) < (16777216))
