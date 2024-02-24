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

# Module: TestComputeSetToOrderedSequenceCharLess

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def CharLess(x, y):
        return (x) < (y)

    @staticmethod
    def CharGreater(x, y):
        return (y) < (x)

    @staticmethod
    def TestSetToOrderedSequenceEmpty():
        d_61_output_: _dafny.Seq
        out4_: _dafny.Seq
        out4_ = SortedSets.default__.SetToOrderedSequence(_dafny.Set({}), default__.CharLess)
        d_61_output_ = out4_
        d_62_output2_: _dafny.Seq
        d_62_output2_ = SortedSets.default__.SetToOrderedSequence2(_dafny.Set({}), default__.CharLess)
        d_63_expected_: _dafny.Seq
        d_63_expected_ = _dafny.Seq([])
        if not((d_61_output_) == (d_63_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceCharLess.dfy(35,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_62_output2_) == (d_63_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceCharLess.dfy(36,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetToOrderedSequenceOneItem():
        d_64_a_: _dafny.Set
        d_64_a_ = _dafny.Set({_dafny.Seq("a")})
        d_65_output_: _dafny.Seq
        out5_: _dafny.Seq
        out5_ = SortedSets.default__.SetToOrderedSequence(d_64_a_, default__.CharLess)
        d_65_output_ = out5_
        d_66_output2_: _dafny.Seq
        d_66_output2_ = SortedSets.default__.SetToOrderedSequence2(d_64_a_, default__.CharLess)
        d_67_expected_: _dafny.Seq
        d_67_expected_ = _dafny.Seq([_dafny.Seq("a")])
        if not((d_65_output_) == (d_67_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceCharLess.dfy(44,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_66_output2_) == (d_67_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceCharLess.dfy(45,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetToOrderedSequenceSimple():
        d_68_a_: _dafny.Set
        d_68_a_ = _dafny.Set({_dafny.Seq("ac"), _dafny.Seq("ab")})
        d_69_output_: _dafny.Seq
        out6_: _dafny.Seq
        out6_ = SortedSets.default__.SetToOrderedSequence(d_68_a_, default__.CharLess)
        d_69_output_ = out6_
        d_70_output2_: _dafny.Seq
        d_70_output2_ = SortedSets.default__.SetToOrderedSequence2(d_68_a_, default__.CharLess)
        d_71_expected_: _dafny.Seq
        d_71_expected_ = _dafny.Seq([_dafny.Seq("ab"), _dafny.Seq("ac")])
        if not((d_69_output_) == (d_71_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceCharLess.dfy(53,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_70_output2_) == (d_71_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceCharLess.dfy(54,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetToOrderedSequencePrefix():
        d_72_a_: _dafny.Set
        d_72_a_ = _dafny.Set({_dafny.Seq("abc"), _dafny.Seq("ab")})
        d_73_output_: _dafny.Seq
        out7_: _dafny.Seq
        out7_ = SortedSets.default__.SetToOrderedSequence(d_72_a_, default__.CharLess)
        d_73_output_ = out7_
        d_74_output2_: _dafny.Seq
        d_74_output2_ = SortedSets.default__.SetToOrderedSequence2(d_72_a_, default__.CharLess)
        d_75_expected_: _dafny.Seq
        d_75_expected_ = _dafny.Seq([_dafny.Seq("ab"), _dafny.Seq("abc")])
        if not((d_73_output_) == (d_75_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceCharLess.dfy(62,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_74_output2_) == (d_75_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceCharLess.dfy(63,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetToOrderedSequenceComplex():
        d_76_a_: _dafny.Set
        d_76_a_ = _dafny.Set({_dafny.Seq("abc"), _dafny.Seq("bbc"), _dafny.Seq("ab")})
        d_77_output_: _dafny.Seq
        out8_: _dafny.Seq
        out8_ = SortedSets.default__.SetToOrderedSequence(d_76_a_, default__.CharLess)
        d_77_output_ = out8_
        d_78_output2_: _dafny.Seq
        d_78_output2_ = SortedSets.default__.SetToOrderedSequence2(d_76_a_, default__.CharLess)
        d_79_expected_: _dafny.Seq
        d_79_expected_ = _dafny.Seq([_dafny.Seq("ab"), _dafny.Seq("abc"), _dafny.Seq("bbc")])
        if not((d_77_output_) == (d_79_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceCharLess.dfy(71,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_78_output2_) == (d_79_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceCharLess.dfy(72,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetToOrderedSequenceComplexReverse():
        d_80_a_: _dafny.Set
        d_80_a_ = _dafny.Set({_dafny.Seq("abc"), _dafny.Seq("bbc"), _dafny.Seq("ab")})
        d_81_output_: _dafny.Seq
        out9_: _dafny.Seq
        out9_ = SortedSets.default__.SetToOrderedSequence(d_80_a_, default__.CharGreater)
        d_81_output_ = out9_
        d_82_output2_: _dafny.Seq
        d_82_output2_ = SortedSets.default__.SetToOrderedSequence2(d_80_a_, default__.CharGreater)
        d_83_expected_: _dafny.Seq
        d_83_expected_ = _dafny.Seq([_dafny.Seq("bbc"), _dafny.Seq("ab"), _dafny.Seq("abc")])
        if not((d_81_output_) == (d_83_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceCharLess.dfy(80,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_82_output2_) == (d_83_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceCharLess.dfy(81,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetSequence():
        d_84_a_: _dafny.Set
        d_84_a_ = _dafny.Set({_dafny.Seq("abc"), _dafny.Seq("bbc"), _dafny.Seq("ab")})
        d_85_output_: _dafny.Seq
        d_85_output_ = SortedSets.default__.SetToSequence(d_84_a_)
        if not((_dafny.MultiSet(d_85_output_)) == (_dafny.MultiSet(d_84_a_))):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceCharLess.dfy(87,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetToOrderedComplexUnicode():
        d_86_a_: _dafny.Set
        d_86_a_ = _dafny.Set({_dafny.Seq("𐐷"), _dafny.Seq("&"), _dafny.Seq("Љ"), _dafny.Seq("ᝀ"), _dafny.Seq("🂡"), _dafny.Seq("｡"), _dafny.Seq("𐀂")})
        d_87_output_: _dafny.Seq
        out10_: _dafny.Seq
        out10_ = SortedSets.default__.SetToOrderedSequence(d_86_a_, default__.CharLess)
        d_87_output_ = out10_
        d_88_output2_: _dafny.Seq
        d_88_output2_ = SortedSets.default__.SetToOrderedSequence2(d_86_a_, default__.CharLess)
        d_89_expected_: _dafny.Seq
        d_89_expected_ = _dafny.Seq([_dafny.Seq("&"), _dafny.Seq("Љ"), _dafny.Seq("ᝀ"), _dafny.Seq("𐀂"), _dafny.Seq("𐐷"), _dafny.Seq("🂡"), _dafny.Seq("｡")])
        if not((d_87_output_) == (d_89_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceCharLess.dfy(111,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_88_output2_) == (d_89_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceCharLess.dfy(112,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

