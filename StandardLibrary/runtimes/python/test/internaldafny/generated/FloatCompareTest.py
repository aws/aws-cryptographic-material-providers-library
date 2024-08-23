import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_ as module_
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
import standard_library.internaldafny.generated.Base64 as Base64
import standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import standard_library.internaldafny.generated.Actions as Actions
import standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import TestUTF8 as TestUTF8
import TestTime as TestTime
import TestComputeSetToOrderedSequenceCharLess as TestComputeSetToOrderedSequenceCharLess
import Sets as Sets
import TestHexStrings as TestHexStrings

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
        for d_98_i_ in range(0, hi0_):
            d_99_negativeTwo_: _dafny.Seq
            d_99_negativeTwo_ = (default__.NEGATIVE__TWO)[d_98_i_]
            hi1_ = len(default__.NEGATIVE__TWO)
            for d_100_j_ in range(d_98_i_, hi1_):
                default__.TestCompareFloat((default__.NEGATIVE__TWO)[d_100_j_], d_99_negativeTwo_, FloatCompare.default__.Equal)
            hi2_ = len(default__.NEGATIVE__ONE)
            for d_101_j_ in range(0, hi2_):
                default__.TestCompareFloat((default__.NEGATIVE__ONE)[d_101_j_], d_99_negativeTwo_, FloatCompare.default__.Greater)
            hi3_ = len(default__.ZERO)
            for d_102_j_ in range(0, hi3_):
                default__.TestCompareFloat((default__.ZERO)[d_102_j_], d_99_negativeTwo_, FloatCompare.default__.Greater)
            hi4_ = len(default__.ONE)
            for d_103_j_ in range(0, hi4_):
                default__.TestCompareFloat((default__.ONE)[d_103_j_], d_99_negativeTwo_, FloatCompare.default__.Greater)
            hi5_ = len(default__.TWO)
            for d_104_j_ in range(0, hi5_):
                default__.TestCompareFloat((default__.TWO)[d_104_j_], d_99_negativeTwo_, FloatCompare.default__.Greater)
        hi6_ = len(default__.NEGATIVE__ONE)
        for d_105_i_ in range(0, hi6_):
            d_106_negativeOne_: _dafny.Seq
            d_106_negativeOne_ = (default__.NEGATIVE__ONE)[d_105_i_]
            hi7_ = len(default__.NEGATIVE__ONE)
            for d_107_j_ in range(d_105_i_, hi7_):
                default__.TestCompareFloat((default__.NEGATIVE__ONE)[d_107_j_], d_106_negativeOne_, FloatCompare.default__.Equal)
            hi8_ = len(default__.ZERO)
            for d_108_j_ in range(0, hi8_):
                default__.TestCompareFloat((default__.ZERO)[d_108_j_], d_106_negativeOne_, FloatCompare.default__.Greater)
            hi9_ = len(default__.ONE)
            for d_109_j_ in range(0, hi9_):
                default__.TestCompareFloat((default__.ONE)[d_109_j_], d_106_negativeOne_, FloatCompare.default__.Greater)
            hi10_ = len(default__.TWO)
            for d_110_j_ in range(0, hi10_):
                default__.TestCompareFloat((default__.TWO)[d_110_j_], d_106_negativeOne_, FloatCompare.default__.Greater)
        hi11_ = len(default__.ZERO)
        for d_111_i_ in range(0, hi11_):
            d_112_zero_: _dafny.Seq
            d_112_zero_ = (default__.ZERO)[d_111_i_]
            hi12_ = len(default__.ZERO)
            for d_113_j_ in range(d_111_i_, hi12_):
                default__.TestCompareFloat((default__.ZERO)[d_113_j_], d_112_zero_, FloatCompare.default__.Equal)
            hi13_ = len(default__.ONE)
            for d_114_j_ in range(0, hi13_):
                default__.TestCompareFloat((default__.ONE)[d_114_j_], d_112_zero_, FloatCompare.default__.Greater)
            hi14_ = len(default__.TWO)
            for d_115_j_ in range(0, hi14_):
                default__.TestCompareFloat((default__.TWO)[d_115_j_], d_112_zero_, FloatCompare.default__.Greater)
        hi15_ = len(default__.ONE)
        for d_116_i_ in range(0, hi15_):
            d_117_one_: _dafny.Seq
            d_117_one_ = (default__.ONE)[d_116_i_]
            hi16_ = len(default__.ONE)
            for d_118_j_ in range(d_116_i_, hi16_):
                default__.TestCompareFloat((default__.ONE)[d_118_j_], d_117_one_, FloatCompare.default__.Equal)
            hi17_ = len(default__.TWO)
            for d_119_j_ in range(0, hi17_):
                default__.TestCompareFloat((default__.TWO)[d_119_j_], d_117_one_, FloatCompare.default__.Greater)
        hi18_ = len(default__.TWO)
        for d_120_i_ in range(0, hi18_):
            d_121_two_: _dafny.Seq
            d_121_two_ = (default__.TWO)[d_120_i_]
            hi19_ = len(default__.TWO)
            for d_122_j_ in range(d_120_i_, hi19_):
                default__.TestCompareFloat((default__.TWO)[d_122_j_], d_121_two_, FloatCompare.default__.Equal)

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
