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
import Base64
import Base64Lemmas
import Actions
import TestUTF8
import TestTime
import TestComputeSetToOrderedSequenceCharLess
import Sets
import TestHexStrings

# Module: FloatCompareTest

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestCompareFloat(x, y, ret):
        if (FloatCompare.default__.CompareFloat(x, y)) != (ret):
            _dafny.print(_dafny.string_of(_dafny.Seq("CompareFloat(")))
            _dafny.print(_dafny.string_of(x))
            _dafny.print(_dafny.string_of(_dafny.Seq(", ")))
            _dafny.print(_dafny.string_of(y))
            _dafny.print(_dafny.string_of(_dafny.Seq(") was ")))
            _dafny.print(_dafny.string_of(FloatCompare.default__.CompareFloat(x, y)))
            _dafny.print(_dafny.string_of(_dafny.Seq(" but should have been ")))
            _dafny.print(_dafny.string_of(ret))
            _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
        if (FloatCompare.default__.CompareFloat(y, x)) != ((0) - (ret)):
            _dafny.print(_dafny.string_of(_dafny.Seq("CompareFloat(")))
            _dafny.print(_dafny.string_of(y))
            _dafny.print(_dafny.string_of(_dafny.Seq(", ")))
            _dafny.print(_dafny.string_of(x))
            _dafny.print(_dafny.string_of(_dafny.Seq(") was ")))
            _dafny.print(_dafny.string_of(FloatCompare.default__.CompareFloat(y, x)))
            _dafny.print(_dafny.string_of(_dafny.Seq(" but should have been ")))
            _dafny.print(_dafny.string_of((0) - (ret)))
            _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
        if not((FloatCompare.default__.CompareFloat(x, y)) == (ret)):
            raise _dafny.HaltException("test/FloatCompare.dfy(165,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((FloatCompare.default__.CompareFloat(y, x)) == ((0) - (ret))):
            raise _dafny.HaltException("test/FloatCompare.dfy(166,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestOneTwoZeroMatrix():
        hi0_ = len(default__.NEGATIVE__TWO)
        for d_96_i_ in range(0, hi0_):
            d_97_negativeTwo_: _dafny.Seq
            d_97_negativeTwo_ = (default__.NEGATIVE__TWO)[d_96_i_]
            hi1_ = len(default__.NEGATIVE__TWO)
            for d_98_j_ in range(d_96_i_, hi1_):
                default__.TestCompareFloat((default__.NEGATIVE__TWO)[d_98_j_], d_97_negativeTwo_, FloatCompare.default__.Equal)
            hi2_ = len(default__.NEGATIVE__ONE)
            for d_99_j_ in range(0, hi2_):
                default__.TestCompareFloat((default__.NEGATIVE__ONE)[d_99_j_], d_97_negativeTwo_, FloatCompare.default__.Greater)
            hi3_ = len(default__.ZERO)
            for d_100_j_ in range(0, hi3_):
                default__.TestCompareFloat((default__.ZERO)[d_100_j_], d_97_negativeTwo_, FloatCompare.default__.Greater)
            hi4_ = len(default__.ONE)
            for d_101_j_ in range(0, hi4_):
                default__.TestCompareFloat((default__.ONE)[d_101_j_], d_97_negativeTwo_, FloatCompare.default__.Greater)
            hi5_ = len(default__.TWO)
            for d_102_j_ in range(0, hi5_):
                default__.TestCompareFloat((default__.TWO)[d_102_j_], d_97_negativeTwo_, FloatCompare.default__.Greater)
        hi6_ = len(default__.NEGATIVE__ONE)
        for d_103_i_ in range(0, hi6_):
            d_104_negativeOne_: _dafny.Seq
            d_104_negativeOne_ = (default__.NEGATIVE__ONE)[d_103_i_]
            hi7_ = len(default__.NEGATIVE__ONE)
            for d_105_j_ in range(d_103_i_, hi7_):
                default__.TestCompareFloat((default__.NEGATIVE__ONE)[d_105_j_], d_104_negativeOne_, FloatCompare.default__.Equal)
            hi8_ = len(default__.ZERO)
            for d_106_j_ in range(0, hi8_):
                default__.TestCompareFloat((default__.ZERO)[d_106_j_], d_104_negativeOne_, FloatCompare.default__.Greater)
            hi9_ = len(default__.ONE)
            for d_107_j_ in range(0, hi9_):
                default__.TestCompareFloat((default__.ONE)[d_107_j_], d_104_negativeOne_, FloatCompare.default__.Greater)
            hi10_ = len(default__.TWO)
            for d_108_j_ in range(0, hi10_):
                default__.TestCompareFloat((default__.TWO)[d_108_j_], d_104_negativeOne_, FloatCompare.default__.Greater)
        hi11_ = len(default__.ZERO)
        for d_109_i_ in range(0, hi11_):
            d_110_zero_: _dafny.Seq
            d_110_zero_ = (default__.ZERO)[d_109_i_]
            hi12_ = len(default__.ZERO)
            for d_111_j_ in range(d_109_i_, hi12_):
                default__.TestCompareFloat((default__.ZERO)[d_111_j_], d_110_zero_, FloatCompare.default__.Equal)
            hi13_ = len(default__.ONE)
            for d_112_j_ in range(0, hi13_):
                default__.TestCompareFloat((default__.ONE)[d_112_j_], d_110_zero_, FloatCompare.default__.Greater)
            hi14_ = len(default__.TWO)
            for d_113_j_ in range(0, hi14_):
                default__.TestCompareFloat((default__.TWO)[d_113_j_], d_110_zero_, FloatCompare.default__.Greater)
        hi15_ = len(default__.ONE)
        for d_114_i_ in range(0, hi15_):
            d_115_one_: _dafny.Seq
            d_115_one_ = (default__.ONE)[d_114_i_]
            hi16_ = len(default__.ONE)
            for d_116_j_ in range(d_114_i_, hi16_):
                default__.TestCompareFloat((default__.ONE)[d_116_j_], d_115_one_, FloatCompare.default__.Equal)
            hi17_ = len(default__.TWO)
            for d_117_j_ in range(0, hi17_):
                default__.TestCompareFloat((default__.TWO)[d_117_j_], d_115_one_, FloatCompare.default__.Greater)
        hi18_ = len(default__.TWO)
        for d_118_i_ in range(0, hi18_):
            d_119_two_: _dafny.Seq
            d_119_two_ = (default__.TWO)[d_118_i_]
            hi19_ = len(default__.TWO)
            for d_120_j_ in range(d_118_i_, hi19_):
                default__.TestCompareFloat((default__.TWO)[d_120_j_], d_119_two_, FloatCompare.default__.Equal)

    @staticmethod
    def SimpleTests():
        default__.TestCompareFloat(_dafny.Seq("1"), _dafny.Seq("1"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("2"), _dafny.Seq("1"), FloatCompare.default__.Greater)
        default__.TestCompareFloat(_dafny.Seq("1.1"), _dafny.Seq("1.2"), FloatCompare.default__.Less)
        default__.TestCompareFloat(_dafny.Seq("1.2"), _dafny.Seq("1.2"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("1.35"), _dafny.Seq("1.357"), FloatCompare.default__.Less)
        default__.TestCompareFloat(_dafny.Seq("1.35e2"), _dafny.Seq("13.5e1"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("1.351e2"), _dafny.Seq("13.5e1"), FloatCompare.default__.Greater)
        default__.TestCompareFloat(_dafny.Seq("1.35e-1"), _dafny.Seq("13.5e-2"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("1"), _dafny.Seq("-2"), FloatCompare.default__.Greater)
        default__.TestCompareFloat(_dafny.Seq("1.2e7"), _dafny.Seq("2.3e2"), FloatCompare.default__.Greater)
        default__.TestCompareFloat(_dafny.Seq("-1.2e7"), _dafny.Seq("2.3e2"), FloatCompare.default__.Less)
        default__.TestCompareFloat(_dafny.Seq("1.2e7"), _dafny.Seq("-2.3e2"), FloatCompare.default__.Greater)
        default__.TestCompareFloat(_dafny.Seq("-1.2e7"), _dafny.Seq("-2.3e2"), FloatCompare.default__.Less)

    @staticmethod
    def SignTests():
        default__.TestCompareFloat(_dafny.Seq("+1"), _dafny.Seq("1"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("+1e+0"), _dafny.Seq("1"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("+1e-0"), _dafny.Seq("1"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("-1"), _dafny.Seq("1"), FloatCompare.default__.Less)
        default__.TestCompareFloat(_dafny.Seq("-1"), _dafny.Seq("+1"), FloatCompare.default__.Less)
        default__.TestCompareFloat(_dafny.Seq("1"), _dafny.Seq("-1"), FloatCompare.default__.Greater)
        default__.TestCompareFloat(_dafny.Seq("+1"), _dafny.Seq("-1"), FloatCompare.default__.Greater)

    @staticmethod
    def ExponentTests():
        default__.TestCompareFloat(_dafny.Seq("2e0"), _dafny.Seq("2e0"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("1e0"), _dafny.Seq("2e0"), FloatCompare.default__.Less)
        default__.TestCompareFloat(_dafny.Seq("3e0"), _dafny.Seq("2e0"), FloatCompare.default__.Greater)
        default__.TestCompareFloat(_dafny.Seq("1e-5"), _dafny.Seq("1e5"), FloatCompare.default__.Less)
        default__.TestCompareFloat(_dafny.Seq("1e5"), _dafny.Seq("1e-5"), FloatCompare.default__.Greater)
        default__.TestCompareFloat(_dafny.Seq("1e5"), _dafny.Seq("1e6"), FloatCompare.default__.Less)
        default__.TestCompareFloat(_dafny.Seq("1e5"), _dafny.Seq("1e4"), FloatCompare.default__.Greater)
        default__.TestCompareFloat(_dafny.Seq("1e-5"), _dafny.Seq("1e-4"), FloatCompare.default__.Less)
        default__.TestCompareFloat(_dafny.Seq("1e-5"), _dafny.Seq("1e-6"), FloatCompare.default__.Greater)
        default__.TestCompareFloat(_dafny.Seq("-1e5"), _dafny.Seq("-1e-5"), FloatCompare.default__.Less)
        default__.TestCompareFloat(_dafny.Seq("-1e-5"), _dafny.Seq("-1e5"), FloatCompare.default__.Greater)
        default__.TestCompareFloat(_dafny.Seq("-1e5"), _dafny.Seq("-1e4"), FloatCompare.default__.Less)
        default__.TestCompareFloat(_dafny.Seq("-1e5"), _dafny.Seq("-1e6"), FloatCompare.default__.Greater)
        default__.TestCompareFloat(_dafny.Seq("-1e-5"), _dafny.Seq("-1e-6"), FloatCompare.default__.Less)
        default__.TestCompareFloat(_dafny.Seq("-1e-5"), _dafny.Seq("-1e-4"), FloatCompare.default__.Greater)
        default__.TestCompareFloat(_dafny.Seq("2"), _dafny.Seq("2e0"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("1"), _dafny.Seq("2e0"), FloatCompare.default__.Less)
        default__.TestCompareFloat(_dafny.Seq("3"), _dafny.Seq("2e0"), FloatCompare.default__.Greater)
        default__.TestCompareFloat(_dafny.Seq("20"), _dafny.Seq("2e1"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("19"), _dafny.Seq("2e1"), FloatCompare.default__.Less)
        default__.TestCompareFloat(_dafny.Seq("21"), _dafny.Seq("2e1"), FloatCompare.default__.Greater)
        default__.TestCompareFloat(_dafny.Seq("-20"), _dafny.Seq("-2e1"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("-21"), _dafny.Seq("-2e1"), FloatCompare.default__.Less)
        default__.TestCompareFloat(_dafny.Seq("-19"), _dafny.Seq("-2e1"), FloatCompare.default__.Greater)
        default__.TestCompareFloat(_dafny.Seq("0.2"), _dafny.Seq("2e-1"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("0.02"), _dafny.Seq("2e-2"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("0.02"), _dafny.Seq(".2e-1"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq(".1"), _dafny.Seq("2e-1"), FloatCompare.default__.Less)
        default__.TestCompareFloat(_dafny.Seq(".3"), _dafny.Seq("2e-1"), FloatCompare.default__.Greater)
        default__.TestCompareFloat(_dafny.Seq("-0.2"), _dafny.Seq("-2e-1"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("-0.02"), _dafny.Seq("-2e-2"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("-0.02"), _dafny.Seq("-.2e-1"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("-.3"), _dafny.Seq("-2e-1"), FloatCompare.default__.Less)
        default__.TestCompareFloat(_dafny.Seq("-.1"), _dafny.Seq("-2e-1"), FloatCompare.default__.Greater)

    @staticmethod
    def ZeroTests():
        default__.TestCompareFloat(_dafny.Seq("-0"), _dafny.Seq("0"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("+0"), _dafny.Seq("0"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("00"), _dafny.Seq("0"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("0.0"), _dafny.Seq("0"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("0"), _dafny.Seq("000"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("0"), _dafny.Seq(".000"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("0.0"), _dafny.Seq("000.00000"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("0"), _dafny.Seq("000.000e0"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("0"), _dafny.Seq("0e+0"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("0"), _dafny.Seq("0e-0"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("0"), _dafny.Seq("0e99"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("0"), _dafny.Seq("0e-99"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("0e+99"), _dafny.Seq("0e-99"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("+0e+99"), _dafny.Seq("-0e-99"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("-0e+99"), _dafny.Seq("-0e-99"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("-0e+99"), _dafny.Seq("+0e-99"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("01"), _dafny.Seq("1"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("1"), _dafny.Seq("001"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("1.0"), _dafny.Seq("001.00000"), FloatCompare.default__.Equal)

    @staticmethod
    def ExtremeNumTest():
        default__.TestCompareFloat(_dafny.Seq("123456789.01234567890123456789012345678"), _dafny.Seq("123456789.01234567890123456789012345678"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("1234567890123456789012345678901234567800000000000000000000000000000"), _dafny.Seq("1234567890123456789012345678901234567800000000000000000000000000000"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq(".000000000000000000000000012345678901234567890123456789012345678"), _dafny.Seq("0.000000000000000000000000012345678901234567890123456789012345678"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("123456789.01234567890123456789012345676"), _dafny.Seq("123456789.01234567890123456789012345678"), FloatCompare.default__.Less)
        default__.TestCompareFloat(_dafny.Seq("123456789.01234567890123456789012345675"), _dafny.Seq("123456789.01234567890123456789012345676"), FloatCompare.default__.Less)
        default__.TestCompareFloat(_dafny.Seq("123456789.01234567890123456789012345679"), _dafny.Seq("123456789.01234567890123456789012345678"), FloatCompare.default__.Greater)
        default__.TestCompareFloat(_dafny.Seq("123456789.01234567890123456789012345677"), _dafny.Seq("123456789.01234567890123456789012345676"), FloatCompare.default__.Greater)
        default__.TestCompareFloat(_dafny.Seq("-123456789.01234567890123456789012345678"), _dafny.Seq("123456789.01234567890123456789012345678"), FloatCompare.default__.Less)
        default__.TestCompareFloat(_dafny.Seq("123456789.01234567890123456789012345678"), _dafny.Seq("-123456789.01234567890123456789012345678"), FloatCompare.default__.Greater)
        default__.TestCompareFloat(_dafny.Seq("0000000000000000000000000012345.67e121"), _dafny.Seq("123456700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("12345.67e121"), _dafny.Seq("123456700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("0.00000001e133"), _dafny.Seq("100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("0.00000001e-122"), _dafny.Seq("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("1234567e-136"), _dafny.Seq("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001234567"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("0000000000000000000000000012345.66e121"), _dafny.Seq("123456700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), FloatCompare.default__.Less)
        default__.TestCompareFloat(_dafny.Seq("0000000000000000000000000012345.68e121"), _dafny.Seq("123456700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), FloatCompare.default__.Greater)
        default__.TestCompareFloat(_dafny.Seq("12345.67e120"), _dafny.Seq("12345.67e121"), FloatCompare.default__.Less)
        default__.TestCompareFloat(_dafny.Seq("12345.67e122"), _dafny.Seq("12345.67e121"), FloatCompare.default__.Greater)
        default__.TestCompareFloat(_dafny.Seq("-12345.67e122"), _dafny.Seq("-12345.67e121"), FloatCompare.default__.Less)
        default__.TestCompareFloat(_dafny.Seq("-12345.67e120"), _dafny.Seq("-12345.67e121"), FloatCompare.default__.Greater)
        default__.TestCompareFloat(_dafny.Seq("12345.67e120"), _dafny.Seq("123456700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), FloatCompare.default__.Less)
        default__.TestCompareFloat(_dafny.Seq("12345.67e122"), _dafny.Seq("123456700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), FloatCompare.default__.Greater)
        default__.TestCompareFloat(_dafny.Seq("-12345.67e122"), _dafny.Seq("-123456700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), FloatCompare.default__.Less)
        default__.TestCompareFloat(_dafny.Seq("-12345.67e120"), _dafny.Seq("-123456700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), FloatCompare.default__.Greater)
        default__.TestCompareFloat(_dafny.Seq("0.00000001e-123"), _dafny.Seq("0.00000001e-122"), FloatCompare.default__.Less)
        default__.TestCompareFloat(_dafny.Seq("0.00000001e-121"), _dafny.Seq("0.00000001e-122"), FloatCompare.default__.Greater)
        default__.TestCompareFloat(_dafny.Seq("-0.00000001e-121"), _dafny.Seq("-0.00000001e-122"), FloatCompare.default__.Less)
        default__.TestCompareFloat(_dafny.Seq("-0.00000001e-123"), _dafny.Seq("-0.00000001e-122"), FloatCompare.default__.Greater)
        default__.TestCompareFloat(_dafny.Seq("0.00000001e-123"), _dafny.Seq("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), FloatCompare.default__.Less)
        default__.TestCompareFloat(_dafny.Seq("0.00000001e-121"), _dafny.Seq("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), FloatCompare.default__.Greater)
        default__.TestCompareFloat(_dafny.Seq("-0.00000001e-121"), _dafny.Seq("-0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), FloatCompare.default__.Less)
        default__.TestCompareFloat(_dafny.Seq("-0.00000001e-123"), _dafny.Seq("-0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), FloatCompare.default__.Greater)
        default__.TestCompareFloat(_dafny.Seq("9.9999999999999999999999999999999999999E+125"), _dafny.Seq("999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq(".99999999999999999999999999999999999999E+126"), _dafny.Seq("999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), _dafny.Seq("999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("9.9999999999999999999999999999999999999E+124"), _dafny.Seq("999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), FloatCompare.default__.Less)
        default__.TestCompareFloat(_dafny.Seq("9.9999999999999999999999999999999999999E+126"), _dafny.Seq("999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), FloatCompare.default__.Greater)
        default__.TestCompareFloat(_dafny.Seq("999999999999999999999999999999999999989999999999999999999999999999999999999999999999999999999999999999999999999999999999999999"), _dafny.Seq("999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), FloatCompare.default__.Less)
        default__.TestCompareFloat(_dafny.Seq("999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), _dafny.Seq("999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), FloatCompare.default__.Greater)
        default__.TestCompareFloat(_dafny.Seq("1E-130"), _dafny.Seq("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("10E-131"), _dafny.Seq("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), _dafny.Seq("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("1E-131"), _dafny.Seq("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), FloatCompare.default__.Less)
        default__.TestCompareFloat(_dafny.Seq("1E-129"), _dafny.Seq("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), FloatCompare.default__.Greater)
        default__.TestCompareFloat(_dafny.Seq("0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000009"), _dafny.Seq("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), FloatCompare.default__.Less)
        default__.TestCompareFloat(_dafny.Seq("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002"), _dafny.Seq("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), FloatCompare.default__.Greater)
        default__.TestCompareFloat(_dafny.Seq("-9.9999999999999999999999999999999999999E+125"), _dafny.Seq("-999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("-.99999999999999999999999999999999999999E+126"), _dafny.Seq("-999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("-999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), _dafny.Seq("-999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("-9.9999999999999999999999999999999999999E+126"), _dafny.Seq("-999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), FloatCompare.default__.Less)
        default__.TestCompareFloat(_dafny.Seq("-9.9999999999999999999999999999999999999E+124"), _dafny.Seq("-999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), FloatCompare.default__.Greater)
        default__.TestCompareFloat(_dafny.Seq("-999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), _dafny.Seq("-999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), FloatCompare.default__.Less)
        default__.TestCompareFloat(_dafny.Seq("-99999999999999999999999999999999999998999999999999999999999999999999999999999999999999999999999999999999999999999999999999999"), _dafny.Seq("-999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), FloatCompare.default__.Greater)
        default__.TestCompareFloat(_dafny.Seq("-1E-130"), _dafny.Seq("-0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("-10E-131"), _dafny.Seq("-0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("-0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), _dafny.Seq("-0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("-1E-129"), _dafny.Seq("-0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), FloatCompare.default__.Less)
        default__.TestCompareFloat(_dafny.Seq("-1E-131"), _dafny.Seq("-0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), FloatCompare.default__.Greater)
        default__.TestCompareFloat(_dafny.Seq("-0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002"), _dafny.Seq("-0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), FloatCompare.default__.Less)
        default__.TestCompareFloat(_dafny.Seq("-0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000009"), _dafny.Seq("-0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), FloatCompare.default__.Greater)

    @staticmethod
    def InvalidTests():
        default__.TestCompareFloat(_dafny.Seq("a"), _dafny.Seq("0"), FloatCompare.default__.Equal)
        default__.TestCompareFloat(_dafny.Seq("a"), _dafny.Seq("b"), FloatCompare.default__.Equal)

    @_dafny.classproperty
    def NEGATIVE__TWO(instance):
        return _dafny.Seq([_dafny.Seq("-2"), _dafny.Seq("-2."), _dafny.Seq("-2.0"), _dafny.Seq("-2e0"), _dafny.Seq("-2.e0"), _dafny.Seq("-2.0e0"), _dafny.Seq("-2.0e+0"), _dafny.Seq("-2.0e-0"), _dafny.Seq("-.2e1"), _dafny.Seq("-0.2e1"), _dafny.Seq("-0.2e+1"), _dafny.Seq("-0.02e2"), _dafny.Seq("-20e-1"), _dafny.Seq("-20.e-1"), _dafny.Seq("-200.0e-2")])
    @_dafny.classproperty
    def NEGATIVE__ONE(instance):
        return _dafny.Seq([_dafny.Seq("-1"), _dafny.Seq("-1."), _dafny.Seq("-1.0"), _dafny.Seq("-1e0"), _dafny.Seq("-1.e0"), _dafny.Seq("-1.0e0"), _dafny.Seq("-1.0e+0"), _dafny.Seq("-1.0e-0"), _dafny.Seq("-.1e1"), _dafny.Seq("-0.1e1"), _dafny.Seq("-0.1e+1"), _dafny.Seq("-0.01e2"), _dafny.Seq("-10e-1"), _dafny.Seq("-10.e-1"), _dafny.Seq("-100.0e-2")])
    @_dafny.classproperty
    def ZERO(instance):
        return _dafny.Seq([_dafny.Seq("0"), _dafny.Seq("+0"), _dafny.Seq("-0"), _dafny.Seq("0."), _dafny.Seq("+0."), _dafny.Seq("-0."), _dafny.Seq("00"), _dafny.Seq("+00"), _dafny.Seq("-00"), _dafny.Seq("0.0"), _dafny.Seq("+0.0"), _dafny.Seq("-0.0"), _dafny.Seq("00.00"), _dafny.Seq("+00.00"), _dafny.Seq("-00.00"), _dafny.Seq(".0"), _dafny.Seq("+.0"), _dafny.Seq("-.0"), _dafny.Seq("0e0"), _dafny.Seq("+0e0"), _dafny.Seq("+0e+0"), _dafny.Seq("+0e-0"), _dafny.Seq("-0e0"), _dafny.Seq("-0e+0"), _dafny.Seq("-0e-0"), _dafny.Seq("0e-99"), _dafny.Seq("+0e-99"), _dafny.Seq("-0e-99"), _dafny.Seq("0e99"), _dafny.Seq("+0e99"), _dafny.Seq("-0e99"), _dafny.Seq("0e+99"), _dafny.Seq("+0e+99"), _dafny.Seq("-0e+99")])
    @_dafny.classproperty
    def ONE(instance):
        return _dafny.Seq([_dafny.Seq("1"), _dafny.Seq("1."), _dafny.Seq("1.0"), _dafny.Seq("1e0"), _dafny.Seq("1.e0"), _dafny.Seq("1.0e0"), _dafny.Seq("1.0e+0"), _dafny.Seq("1.0e-0"), _dafny.Seq(".1e1"), _dafny.Seq("0.1e1"), _dafny.Seq("0.1e+1"), _dafny.Seq("0.01e2"), _dafny.Seq("10e-1"), _dafny.Seq("10.e-1"), _dafny.Seq("100.0e-2"), _dafny.Seq("+1"), _dafny.Seq("+1."), _dafny.Seq("+1.0"), _dafny.Seq("+1e0"), _dafny.Seq("+1.e0"), _dafny.Seq("+1.0e0"), _dafny.Seq("+1.0e+0"), _dafny.Seq("+1.0e-0"), _dafny.Seq("+.1e1"), _dafny.Seq("+0.1e1"), _dafny.Seq("+0.1e+1"), _dafny.Seq("+0.01e2"), _dafny.Seq("+10e-1"), _dafny.Seq("+10.e-1"), _dafny.Seq("+100.0e-2")])
    @_dafny.classproperty
    def TWO(instance):
        return _dafny.Seq([_dafny.Seq("2"), _dafny.Seq("2."), _dafny.Seq("2.0"), _dafny.Seq("2e0"), _dafny.Seq("2.e0"), _dafny.Seq("2.0e0"), _dafny.Seq("2.0e+0"), _dafny.Seq("2.0e-0"), _dafny.Seq(".2e1"), _dafny.Seq("0.2e1"), _dafny.Seq("0.2e+1"), _dafny.Seq("0.02e2"), _dafny.Seq("20e-1"), _dafny.Seq("20.e-1"), _dafny.Seq("200.0e-2"), _dafny.Seq("+2"), _dafny.Seq("+2."), _dafny.Seq("+2.0"), _dafny.Seq("+2e0"), _dafny.Seq("+2.e0"), _dafny.Seq("+2.0e0"), _dafny.Seq("+2.0e+0"), _dafny.Seq("+2.0e-0"), _dafny.Seq("+.2e1"), _dafny.Seq("+0.2e1"), _dafny.Seq("+0.2e+1"), _dafny.Seq("+0.02e2"), _dafny.Seq("+20e-1"), _dafny.Seq("+20.e-1"), _dafny.Seq("+200.0e-2")])
