import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import BoundedInts
import StandardLibrary_UInt
import StandardLibrary
import UTF8
import TestUTF8
import Time
import TestTime
import HexStrings
import TestHexStrings
import Relations
import Seq_MergeSort
import Math
import Seq
import SortedSets
import TestSeqReaderReadElements
import Functions
import Sets
import FloatCompare

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
        for d_216_i_ in range(0, hi0_):
            d_217_negativeTwo_: _dafny.Seq
            d_217_negativeTwo_ = (default__.NEGATIVE__TWO)[d_216_i_]
            hi1_ = len(default__.NEGATIVE__TWO)
            for d_218_j_ in range(d_216_i_, hi1_):
                default__.TestCompareFloat((default__.NEGATIVE__TWO)[d_218_j_], d_217_negativeTwo_, FloatCompare.default__.Equal)
            hi2_ = len(default__.NEGATIVE__ONE)
            for d_219_j_ in range(0, hi2_):
                default__.TestCompareFloat((default__.NEGATIVE__ONE)[d_219_j_], d_217_negativeTwo_, FloatCompare.default__.Greater)
            hi3_ = len(default__.ZERO)
            for d_220_j_ in range(0, hi3_):
                default__.TestCompareFloat((default__.ZERO)[d_220_j_], d_217_negativeTwo_, FloatCompare.default__.Greater)
            hi4_ = len(default__.ONE)
            for d_221_j_ in range(0, hi4_):
                default__.TestCompareFloat((default__.ONE)[d_221_j_], d_217_negativeTwo_, FloatCompare.default__.Greater)
            hi5_ = len(default__.TWO)
            for d_222_j_ in range(0, hi5_):
                default__.TestCompareFloat((default__.TWO)[d_222_j_], d_217_negativeTwo_, FloatCompare.default__.Greater)
        hi6_ = len(default__.NEGATIVE__ONE)
        for d_223_i_ in range(0, hi6_):
            d_224_negativeOne_: _dafny.Seq
            d_224_negativeOne_ = (default__.NEGATIVE__ONE)[d_223_i_]
            hi7_ = len(default__.NEGATIVE__ONE)
            for d_225_j_ in range(d_223_i_, hi7_):
                default__.TestCompareFloat((default__.NEGATIVE__ONE)[d_225_j_], d_224_negativeOne_, FloatCompare.default__.Equal)
            hi8_ = len(default__.ZERO)
            for d_226_j_ in range(0, hi8_):
                default__.TestCompareFloat((default__.ZERO)[d_226_j_], d_224_negativeOne_, FloatCompare.default__.Greater)
            hi9_ = len(default__.ONE)
            for d_227_j_ in range(0, hi9_):
                default__.TestCompareFloat((default__.ONE)[d_227_j_], d_224_negativeOne_, FloatCompare.default__.Greater)
            hi10_ = len(default__.TWO)
            for d_228_j_ in range(0, hi10_):
                default__.TestCompareFloat((default__.TWO)[d_228_j_], d_224_negativeOne_, FloatCompare.default__.Greater)
        hi11_ = len(default__.ZERO)
        for d_229_i_ in range(0, hi11_):
            d_230_zero_: _dafny.Seq
            d_230_zero_ = (default__.ZERO)[d_229_i_]
            hi12_ = len(default__.ZERO)
            for d_231_j_ in range(d_229_i_, hi12_):
                default__.TestCompareFloat((default__.ZERO)[d_231_j_], d_230_zero_, FloatCompare.default__.Equal)
            hi13_ = len(default__.ONE)
            for d_232_j_ in range(0, hi13_):
                default__.TestCompareFloat((default__.ONE)[d_232_j_], d_230_zero_, FloatCompare.default__.Greater)
            hi14_ = len(default__.TWO)
            for d_233_j_ in range(0, hi14_):
                default__.TestCompareFloat((default__.TWO)[d_233_j_], d_230_zero_, FloatCompare.default__.Greater)
        hi15_ = len(default__.ONE)
        for d_234_i_ in range(0, hi15_):
            d_235_one_: _dafny.Seq
            d_235_one_ = (default__.ONE)[d_234_i_]
            hi16_ = len(default__.ONE)
            for d_236_j_ in range(d_234_i_, hi16_):
                default__.TestCompareFloat((default__.ONE)[d_236_j_], d_235_one_, FloatCompare.default__.Equal)
            hi17_ = len(default__.TWO)
            for d_237_j_ in range(0, hi17_):
                default__.TestCompareFloat((default__.TWO)[d_237_j_], d_235_one_, FloatCompare.default__.Greater)
        hi18_ = len(default__.TWO)
        for d_238_i_ in range(0, hi18_):
            d_239_two_: _dafny.Seq
            d_239_two_ = (default__.TWO)[d_238_i_]
            hi19_ = len(default__.TWO)
            for d_240_j_ in range(d_238_i_, hi19_):
                default__.TestCompareFloat((default__.TWO)[d_240_j_], d_239_two_, FloatCompare.default__.Equal)

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
