import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import BoundedInts
import StandardLibrary_mUInt
import String
import StandardLibrary
import UUID
import TestUUID
import ConcurrentCall
import TestCallMany
import FloatCompare

assert "FloatCompareTest" == __name__
FloatCompareTest = sys.modules[__name__]

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
        hi0_: int = len((FloatCompareTest.default__).NEGATIVE__TWO)
        for d_29_i_ in range(0, hi0_):
            d_30_negativeTwo_: _dafny.Seq
            d_30_negativeTwo_ = ((FloatCompareTest.default__).NEGATIVE__TWO)[d_29_i_]
            hi1_: int = len((FloatCompareTest.default__).NEGATIVE__TWO)
            for d_31_j_ in range(d_29_i_, hi1_):
                FloatCompareTest.default__.TestCompareFloat(((FloatCompareTest.default__).NEGATIVE__TWO)[d_31_j_], d_30_negativeTwo_, (FloatCompare.default__).Equal)
            hi2_: int = len((FloatCompareTest.default__).NEGATIVE__ONE)
            for d_32_j_ in range(0, hi2_):
                FloatCompareTest.default__.TestCompareFloat(((FloatCompareTest.default__).NEGATIVE__ONE)[d_32_j_], d_30_negativeTwo_, (FloatCompare.default__).Greater)
            hi3_: int = len((FloatCompareTest.default__).ZERO)
            for d_33_j_ in range(0, hi3_):
                FloatCompareTest.default__.TestCompareFloat(((FloatCompareTest.default__).ZERO)[d_33_j_], d_30_negativeTwo_, (FloatCompare.default__).Greater)
            hi4_: int = len((FloatCompareTest.default__).ONE)
            for d_34_j_ in range(0, hi4_):
                FloatCompareTest.default__.TestCompareFloat(((FloatCompareTest.default__).ONE)[d_34_j_], d_30_negativeTwo_, (FloatCompare.default__).Greater)
            hi5_: int = len((FloatCompareTest.default__).TWO)
            for d_35_j_ in range(0, hi5_):
                FloatCompareTest.default__.TestCompareFloat(((FloatCompareTest.default__).TWO)[d_35_j_], d_30_negativeTwo_, (FloatCompare.default__).Greater)
        hi6_: int = len((FloatCompareTest.default__).NEGATIVE__ONE)
        for d_36_i_ in range(0, hi6_):
            d_37_negativeOne_: _dafny.Seq
            d_37_negativeOne_ = ((FloatCompareTest.default__).NEGATIVE__ONE)[d_36_i_]
            hi7_: int = len((FloatCompareTest.default__).NEGATIVE__ONE)
            for d_38_j_ in range(d_36_i_, hi7_):
                FloatCompareTest.default__.TestCompareFloat(((FloatCompareTest.default__).NEGATIVE__ONE)[d_38_j_], d_37_negativeOne_, (FloatCompare.default__).Equal)
            hi8_: int = len((FloatCompareTest.default__).ZERO)
            for d_39_j_ in range(0, hi8_):
                FloatCompareTest.default__.TestCompareFloat(((FloatCompareTest.default__).ZERO)[d_39_j_], d_37_negativeOne_, (FloatCompare.default__).Greater)
            hi9_: int = len((FloatCompareTest.default__).ONE)
            for d_40_j_ in range(0, hi9_):
                FloatCompareTest.default__.TestCompareFloat(((FloatCompareTest.default__).ONE)[d_40_j_], d_37_negativeOne_, (FloatCompare.default__).Greater)
            hi10_: int = len((FloatCompareTest.default__).TWO)
            for d_41_j_ in range(0, hi10_):
                FloatCompareTest.default__.TestCompareFloat(((FloatCompareTest.default__).TWO)[d_41_j_], d_37_negativeOne_, (FloatCompare.default__).Greater)
        hi11_: int = len((FloatCompareTest.default__).ZERO)
        for d_42_i_ in range(0, hi11_):
            d_43_zero_: _dafny.Seq
            d_43_zero_ = ((FloatCompareTest.default__).ZERO)[d_42_i_]
            hi12_: int = len((FloatCompareTest.default__).ZERO)
            for d_44_j_ in range(d_42_i_, hi12_):
                FloatCompareTest.default__.TestCompareFloat(((FloatCompareTest.default__).ZERO)[d_44_j_], d_43_zero_, (FloatCompare.default__).Equal)
            hi13_: int = len((FloatCompareTest.default__).ONE)
            for d_45_j_ in range(0, hi13_):
                FloatCompareTest.default__.TestCompareFloat(((FloatCompareTest.default__).ONE)[d_45_j_], d_43_zero_, (FloatCompare.default__).Greater)
            hi14_: int = len((FloatCompareTest.default__).TWO)
            for d_46_j_ in range(0, hi14_):
                FloatCompareTest.default__.TestCompareFloat(((FloatCompareTest.default__).TWO)[d_46_j_], d_43_zero_, (FloatCompare.default__).Greater)
        hi15_: int = len((FloatCompareTest.default__).ONE)
        for d_47_i_ in range(0, hi15_):
            d_48_one_: _dafny.Seq
            d_48_one_ = ((FloatCompareTest.default__).ONE)[d_47_i_]
            hi16_: int = len((FloatCompareTest.default__).ONE)
            for d_49_j_ in range(d_47_i_, hi16_):
                FloatCompareTest.default__.TestCompareFloat(((FloatCompareTest.default__).ONE)[d_49_j_], d_48_one_, (FloatCompare.default__).Equal)
            hi17_: int = len((FloatCompareTest.default__).TWO)
            for d_50_j_ in range(0, hi17_):
                FloatCompareTest.default__.TestCompareFloat(((FloatCompareTest.default__).TWO)[d_50_j_], d_48_one_, (FloatCompare.default__).Greater)
        hi18_: int = len((FloatCompareTest.default__).TWO)
        for d_51_i_ in range(0, hi18_):
            d_52_two_: _dafny.Seq
            d_52_two_ = ((FloatCompareTest.default__).TWO)[d_51_i_]
            hi19_: int = len((FloatCompareTest.default__).TWO)
            for d_53_j_ in range(d_51_i_, hi19_):
                FloatCompareTest.default__.TestCompareFloat(((FloatCompareTest.default__).TWO)[d_53_j_], d_52_two_, (FloatCompare.default__).Equal)

    @staticmethod
    def SimpleTests():
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("1"), _dafny.Seq("1"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("2"), _dafny.Seq("1"), (FloatCompare.default__).Greater)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("1.1"), _dafny.Seq("1.2"), (FloatCompare.default__).Less)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("1.2"), _dafny.Seq("1.2"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("1.35"), _dafny.Seq("1.357"), (FloatCompare.default__).Less)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("1.35e2"), _dafny.Seq("13.5e1"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("1.351e2"), _dafny.Seq("13.5e1"), (FloatCompare.default__).Greater)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("1.35e-1"), _dafny.Seq("13.5e-2"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("1"), _dafny.Seq("-2"), (FloatCompare.default__).Greater)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("1.2e7"), _dafny.Seq("2.3e2"), (FloatCompare.default__).Greater)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-1.2e7"), _dafny.Seq("2.3e2"), (FloatCompare.default__).Less)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("1.2e7"), _dafny.Seq("-2.3e2"), (FloatCompare.default__).Greater)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-1.2e7"), _dafny.Seq("-2.3e2"), (FloatCompare.default__).Less)

    @staticmethod
    def SignTests():
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("+1"), _dafny.Seq("1"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("+1e+0"), _dafny.Seq("1"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("+1e-0"), _dafny.Seq("1"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-1"), _dafny.Seq("1"), (FloatCompare.default__).Less)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-1"), _dafny.Seq("+1"), (FloatCompare.default__).Less)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("1"), _dafny.Seq("-1"), (FloatCompare.default__).Greater)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("+1"), _dafny.Seq("-1"), (FloatCompare.default__).Greater)

    @staticmethod
    def ExponentTests():
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("2e0"), _dafny.Seq("2e0"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("1e0"), _dafny.Seq("2e0"), (FloatCompare.default__).Less)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("3e0"), _dafny.Seq("2e0"), (FloatCompare.default__).Greater)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("1e-5"), _dafny.Seq("1e5"), (FloatCompare.default__).Less)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("1e5"), _dafny.Seq("1e-5"), (FloatCompare.default__).Greater)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("1e5"), _dafny.Seq("1e6"), (FloatCompare.default__).Less)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("1e5"), _dafny.Seq("1e4"), (FloatCompare.default__).Greater)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("1e-5"), _dafny.Seq("1e-4"), (FloatCompare.default__).Less)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("1e-5"), _dafny.Seq("1e-6"), (FloatCompare.default__).Greater)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-1e5"), _dafny.Seq("-1e-5"), (FloatCompare.default__).Less)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-1e-5"), _dafny.Seq("-1e5"), (FloatCompare.default__).Greater)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-1e5"), _dafny.Seq("-1e4"), (FloatCompare.default__).Less)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-1e5"), _dafny.Seq("-1e6"), (FloatCompare.default__).Greater)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-1e-5"), _dafny.Seq("-1e-6"), (FloatCompare.default__).Less)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-1e-5"), _dafny.Seq("-1e-4"), (FloatCompare.default__).Greater)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("2"), _dafny.Seq("2e0"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("1"), _dafny.Seq("2e0"), (FloatCompare.default__).Less)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("3"), _dafny.Seq("2e0"), (FloatCompare.default__).Greater)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("20"), _dafny.Seq("2e1"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("19"), _dafny.Seq("2e1"), (FloatCompare.default__).Less)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("21"), _dafny.Seq("2e1"), (FloatCompare.default__).Greater)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-20"), _dafny.Seq("-2e1"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-21"), _dafny.Seq("-2e1"), (FloatCompare.default__).Less)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-19"), _dafny.Seq("-2e1"), (FloatCompare.default__).Greater)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("0.2"), _dafny.Seq("2e-1"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("0.02"), _dafny.Seq("2e-2"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("0.02"), _dafny.Seq(".2e-1"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq(".1"), _dafny.Seq("2e-1"), (FloatCompare.default__).Less)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq(".3"), _dafny.Seq("2e-1"), (FloatCompare.default__).Greater)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-0.2"), _dafny.Seq("-2e-1"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-0.02"), _dafny.Seq("-2e-2"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-0.02"), _dafny.Seq("-.2e-1"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-.3"), _dafny.Seq("-2e-1"), (FloatCompare.default__).Less)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-.1"), _dafny.Seq("-2e-1"), (FloatCompare.default__).Greater)

    @staticmethod
    def ZeroTests():
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-0"), _dafny.Seq("0"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("+0"), _dafny.Seq("0"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("00"), _dafny.Seq("0"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("0.0"), _dafny.Seq("0"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("0"), _dafny.Seq("000"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("0"), _dafny.Seq(".000"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("0.0"), _dafny.Seq("000.00000"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("0"), _dafny.Seq("000.000e0"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("0"), _dafny.Seq("0e+0"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("0"), _dafny.Seq("0e-0"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("0"), _dafny.Seq("0e99"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("0"), _dafny.Seq("0e-99"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("0e+99"), _dafny.Seq("0e-99"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("+0e+99"), _dafny.Seq("-0e-99"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-0e+99"), _dafny.Seq("-0e-99"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-0e+99"), _dafny.Seq("+0e-99"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("01"), _dafny.Seq("1"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("1"), _dafny.Seq("001"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("1.0"), _dafny.Seq("001.00000"), (FloatCompare.default__).Equal)

    @staticmethod
    def ExtremeNumTest():
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("123456789.01234567890123456789012345678"), _dafny.Seq("123456789.01234567890123456789012345678"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("1234567890123456789012345678901234567800000000000000000000000000000"), _dafny.Seq("1234567890123456789012345678901234567800000000000000000000000000000"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq(".000000000000000000000000012345678901234567890123456789012345678"), _dafny.Seq("0.000000000000000000000000012345678901234567890123456789012345678"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("123456789.01234567890123456789012345676"), _dafny.Seq("123456789.01234567890123456789012345678"), (FloatCompare.default__).Less)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("123456789.01234567890123456789012345675"), _dafny.Seq("123456789.01234567890123456789012345676"), (FloatCompare.default__).Less)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("123456789.01234567890123456789012345679"), _dafny.Seq("123456789.01234567890123456789012345678"), (FloatCompare.default__).Greater)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("123456789.01234567890123456789012345677"), _dafny.Seq("123456789.01234567890123456789012345676"), (FloatCompare.default__).Greater)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-123456789.01234567890123456789012345678"), _dafny.Seq("123456789.01234567890123456789012345678"), (FloatCompare.default__).Less)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("123456789.01234567890123456789012345678"), _dafny.Seq("-123456789.01234567890123456789012345678"), (FloatCompare.default__).Greater)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("0000000000000000000000000012345.67e121"), _dafny.Seq("123456700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("12345.67e121"), _dafny.Seq("123456700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("0.00000001e133"), _dafny.Seq("100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("0.00000001e-122"), _dafny.Seq("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("1234567e-136"), _dafny.Seq("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001234567"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("0000000000000000000000000012345.66e121"), _dafny.Seq("123456700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), (FloatCompare.default__).Less)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("0000000000000000000000000012345.68e121"), _dafny.Seq("123456700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), (FloatCompare.default__).Greater)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("12345.67e120"), _dafny.Seq("12345.67e121"), (FloatCompare.default__).Less)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("12345.67e122"), _dafny.Seq("12345.67e121"), (FloatCompare.default__).Greater)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-12345.67e122"), _dafny.Seq("-12345.67e121"), (FloatCompare.default__).Less)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-12345.67e120"), _dafny.Seq("-12345.67e121"), (FloatCompare.default__).Greater)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("12345.67e120"), _dafny.Seq("123456700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), (FloatCompare.default__).Less)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("12345.67e122"), _dafny.Seq("123456700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), (FloatCompare.default__).Greater)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-12345.67e122"), _dafny.Seq("-123456700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), (FloatCompare.default__).Less)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-12345.67e120"), _dafny.Seq("-123456700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), (FloatCompare.default__).Greater)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("0.00000001e-123"), _dafny.Seq("0.00000001e-122"), (FloatCompare.default__).Less)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("0.00000001e-121"), _dafny.Seq("0.00000001e-122"), (FloatCompare.default__).Greater)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-0.00000001e-121"), _dafny.Seq("-0.00000001e-122"), (FloatCompare.default__).Less)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-0.00000001e-123"), _dafny.Seq("-0.00000001e-122"), (FloatCompare.default__).Greater)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("0.00000001e-123"), _dafny.Seq("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), (FloatCompare.default__).Less)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("0.00000001e-121"), _dafny.Seq("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), (FloatCompare.default__).Greater)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-0.00000001e-121"), _dafny.Seq("-0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), (FloatCompare.default__).Less)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-0.00000001e-123"), _dafny.Seq("-0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), (FloatCompare.default__).Greater)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("9.9999999999999999999999999999999999999E+125"), _dafny.Seq("999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq(".99999999999999999999999999999999999999E+126"), _dafny.Seq("999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), _dafny.Seq("999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("9.9999999999999999999999999999999999999E+124"), _dafny.Seq("999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), (FloatCompare.default__).Less)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("9.9999999999999999999999999999999999999E+126"), _dafny.Seq("999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), (FloatCompare.default__).Greater)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("999999999999999999999999999999999999989999999999999999999999999999999999999999999999999999999999999999999999999999999999999999"), _dafny.Seq("999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), (FloatCompare.default__).Less)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), _dafny.Seq("999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), (FloatCompare.default__).Greater)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("1E-130"), _dafny.Seq("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("10E-131"), _dafny.Seq("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), _dafny.Seq("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("1E-131"), _dafny.Seq("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), (FloatCompare.default__).Less)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("1E-129"), _dafny.Seq("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), (FloatCompare.default__).Greater)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000009"), _dafny.Seq("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), (FloatCompare.default__).Less)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002"), _dafny.Seq("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), (FloatCompare.default__).Greater)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-9.9999999999999999999999999999999999999E+125"), _dafny.Seq("-999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-.99999999999999999999999999999999999999E+126"), _dafny.Seq("-999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), _dafny.Seq("-999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-9.9999999999999999999999999999999999999E+126"), _dafny.Seq("-999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), (FloatCompare.default__).Less)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-9.9999999999999999999999999999999999999E+124"), _dafny.Seq("-999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), (FloatCompare.default__).Greater)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), _dafny.Seq("-999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), (FloatCompare.default__).Less)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-99999999999999999999999999999999999998999999999999999999999999999999999999999999999999999999999999999999999999999999999999999"), _dafny.Seq("-999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), (FloatCompare.default__).Greater)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-1E-130"), _dafny.Seq("-0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-10E-131"), _dafny.Seq("-0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), _dafny.Seq("-0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-1E-129"), _dafny.Seq("-0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), (FloatCompare.default__).Less)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-1E-131"), _dafny.Seq("-0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), (FloatCompare.default__).Greater)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002"), _dafny.Seq("-0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), (FloatCompare.default__).Less)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("-0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000009"), _dafny.Seq("-0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), (FloatCompare.default__).Greater)

    @staticmethod
    def InvalidTests():
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("a"), _dafny.Seq("0"), (FloatCompare.default__).Equal)
        FloatCompareTest.default__.TestCompareFloat(_dafny.Seq("a"), _dafny.Seq("b"), (FloatCompare.default__).Equal)

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
