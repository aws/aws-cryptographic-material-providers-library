import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_MergeSort
import Math
import Seq
import BoundedInts
import Unicode
import Functions
import Utf8EncodingForm
import Utf16EncodingForm
import UnicodeStrings
import DafnyLibraries
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
import StandardLibrary_UInt
import StandardLibrary_String
import StandardLibrary
import UUID
import UTF8
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import FloatCompare
import ConcurrentCall

# Module: Base64

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def IsBase64Char(c):
        return (((((c) == ('+')) or ((c) == ('/'))) or ((('0') <= (c)) and ((c) <= ('9')))) or ((('A') <= (c)) and ((c) <= ('Z')))) or ((('a') <= (c)) and ((c) <= ('z')))

    @staticmethod
    def IsUnpaddedBase64String(s):
        def lambda23_(forall_var_5_):
            d_273_k_: str = forall_var_5_
            return not ((d_273_k_) in (s)) or (default__.IsBase64Char(d_273_k_))

        return ((_dafny.euclidian_modulus(len(s), 4)) == (0)) and (_dafny.quantifier((s).UniqueElements, True, lambda23_))

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
        d_274_b0_ = _dafny.euclidian_division(x, 65536)
        d_275_x0_ = (x) - ((d_274_b0_) * (65536))
        d_276_b1_ = _dafny.euclidian_division(d_275_x0_, 256)
        d_277_b2_ = _dafny.euclidian_modulus(d_275_x0_, 256)
        return _dafny.Seq([d_274_b0_, d_276_b1_, d_277_b2_])

    @staticmethod
    def SeqToUInt24(s):
        return ((((s)[0]) * (65536)) + (((s)[1]) * (256))) + ((s)[2])

    @staticmethod
    def UInt24ToIndexSeq(x):
        d_278_b0_ = _dafny.euclidian_division(x, 262144)
        d_279_x0_ = (x) - ((d_278_b0_) * (262144))
        d_280_b1_ = _dafny.euclidian_division(d_279_x0_, 4096)
        d_281_x1_ = (d_279_x0_) - ((d_280_b1_) * (4096))
        d_282_b2_ = _dafny.euclidian_division(d_281_x1_, 64)
        d_283_b3_ = _dafny.euclidian_modulus(d_281_x1_, 64)
        return _dafny.Seq([d_278_b0_, d_280_b1_, d_282_b2_, d_283_b3_])

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
        d_284___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(s)) == (0):
                    return (d_284___accumulator_) + (_dafny.Seq([]))
                elif True:
                    d_284___accumulator_ = (d_284___accumulator_) + (default__.DecodeBlock(_dafny.Seq((s)[:4:])))
                    in79_ = _dafny.Seq((s)[4::])
                    s = in79_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def EncodeRecursively(b):
        d_285___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (len(b)) == (0):
                    return (d_285___accumulator_) + (_dafny.Seq([]))
                elif True:
                    d_285___accumulator_ = (d_285___accumulator_) + (default__.EncodeBlock(_dafny.Seq((b)[:3:])))
                    in80_ = _dafny.Seq((b)[3::])
                    b = in80_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def FromCharsToIndices(s):
        return _dafny.Seq([default__.CharToIndex((s)[d_286_i_]) for d_286_i_ in range(len(s))])

    @staticmethod
    def FromIndicesToChars(b):
        return _dafny.Seq([default__.IndexToChar((b)[d_287_i_]) for d_287_i_ in range(len(b))])

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
        d_288_d_ = default__.DecodeBlock(_dafny.Seq([default__.CharToIndex((s)[0]), default__.CharToIndex((s)[1]), default__.CharToIndex((s)[2]), 0]))
        return _dafny.Seq([(d_288_d_)[0], (d_288_d_)[1]])

    @staticmethod
    def Encode1Padding(b):
        d_289_e_ = default__.EncodeBlock(_dafny.Seq([(b)[0], (b)[1], 0]))
        return _dafny.Seq([default__.IndexToChar((d_289_e_)[0]), default__.IndexToChar((d_289_e_)[1]), default__.IndexToChar((d_289_e_)[2]), '='])

    @staticmethod
    def Is2Padding(s):
        return ((((((len(s)) == (4)) and (default__.IsBase64Char((s)[0]))) and (default__.IsBase64Char((s)[1]))) and ((_dafny.euclidian_modulus(default__.CharToIndex((s)[1]), 16)) == (0))) and (((s)[2]) == ('='))) and (((s)[3]) == ('='))

    @staticmethod
    def Decode2Padding(s):
        d_290_d_ = default__.DecodeBlock(_dafny.Seq([default__.CharToIndex((s)[0]), default__.CharToIndex((s)[1]), 0, 0]))
        return _dafny.Seq([(d_290_d_)[0]])

    @staticmethod
    def Encode2Padding(b):
        d_291_e_ = default__.EncodeBlock(_dafny.Seq([(b)[0], 0, 0]))
        return _dafny.Seq([default__.IndexToChar((d_291_e_)[0]), default__.IndexToChar((d_291_e_)[1]), '=', '='])

    @staticmethod
    def IsBase64String(s):
        d_292_finalBlockStart_ = (len(s)) - (4)
        return ((_dafny.euclidian_modulus(len(s), 4)) == (0)) and ((default__.IsUnpaddedBase64String(s)) or ((default__.IsUnpaddedBase64String(_dafny.Seq((s)[:d_292_finalBlockStart_:]))) and ((default__.Is1Padding(_dafny.Seq((s)[d_292_finalBlockStart_::]))) or (default__.Is2Padding(_dafny.Seq((s)[d_292_finalBlockStart_::]))))))

    @staticmethod
    def DecodeValid(s):
        if (s) == (_dafny.Seq([])):
            return _dafny.Seq([])
        elif True:
            d_293_finalBlockStart_ = (len(s)) - (4)
            d_294_prefix_ = _dafny.Seq((s)[:d_293_finalBlockStart_:])
            d_295_suffix_ = _dafny.Seq((s)[d_293_finalBlockStart_::])
            if default__.Is1Padding(d_295_suffix_):
                return (default__.DecodeUnpadded(d_294_prefix_)) + (default__.Decode1Padding(d_295_suffix_))
            elif default__.Is2Padding(d_295_suffix_):
                return (default__.DecodeUnpadded(d_294_prefix_)) + (default__.Decode2Padding(d_295_suffix_))
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
            d_296_s_ = default__.EncodeUnpadded(b)
            return d_296_s_
        elif (_dafny.euclidian_modulus(len(b), 3)) == (1):
            d_297_s1_ = default__.EncodeUnpadded(_dafny.Seq((b)[:(len(b)) - (1):]))
            d_298_s2_ = default__.Encode2Padding(_dafny.Seq((b)[(len(b)) - (1)::]))
            d_299_s_ = (d_297_s1_) + (d_298_s2_)
            return d_299_s_
        elif True:
            d_300_s1_ = default__.EncodeUnpadded(_dafny.Seq((b)[:(len(b)) - (2):]))
            d_301_s2_ = default__.Encode1Padding(_dafny.Seq((b)[(len(b)) - (2)::]))
            d_302_s_ = (d_300_s1_) + (d_301_s2_)
            return d_302_s_


class index:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)

class uint24:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
