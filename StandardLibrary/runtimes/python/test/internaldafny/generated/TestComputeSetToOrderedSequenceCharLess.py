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
        d_63_output_: _dafny.Seq
        out5_: _dafny.Seq
        out5_ = SortedSets.default__.SetToOrderedSequence(_dafny.Set({}), default__.CharLess)
        d_63_output_ = out5_
        d_64_output2_: _dafny.Seq
        d_64_output2_ = SortedSets.default__.SetToOrderedSequence2(_dafny.Set({}), default__.CharLess)
        d_65_expected_: _dafny.Seq
        d_65_expected_ = _dafny.Seq([])
        if not((d_63_output_) == (d_65_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceCharLess.dfy(35,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_64_output2_) == (d_65_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceCharLess.dfy(36,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetToOrderedSequenceOneItem():
        d_66_a_: _dafny.Set
        d_66_a_ = _dafny.Set({_dafny.Seq("a")})
        d_67_output_: _dafny.Seq
        out6_: _dafny.Seq
        out6_ = SortedSets.default__.SetToOrderedSequence(d_66_a_, default__.CharLess)
        d_67_output_ = out6_
        d_68_output2_: _dafny.Seq
        d_68_output2_ = SortedSets.default__.SetToOrderedSequence2(d_66_a_, default__.CharLess)
        d_69_expected_: _dafny.Seq
        d_69_expected_ = _dafny.Seq([_dafny.Seq("a")])
        if not((d_67_output_) == (d_69_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceCharLess.dfy(44,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_68_output2_) == (d_69_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceCharLess.dfy(45,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetToOrderedSequenceSimple():
        d_70_a_: _dafny.Set
        d_70_a_ = _dafny.Set({_dafny.Seq("ac"), _dafny.Seq("ab")})
        d_71_output_: _dafny.Seq
        out7_: _dafny.Seq
        out7_ = SortedSets.default__.SetToOrderedSequence(d_70_a_, default__.CharLess)
        d_71_output_ = out7_
        d_72_output2_: _dafny.Seq
        d_72_output2_ = SortedSets.default__.SetToOrderedSequence2(d_70_a_, default__.CharLess)
        d_73_expected_: _dafny.Seq
        d_73_expected_ = _dafny.Seq([_dafny.Seq("ab"), _dafny.Seq("ac")])
        if not((d_71_output_) == (d_73_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceCharLess.dfy(53,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_72_output2_) == (d_73_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceCharLess.dfy(54,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetToOrderedSequencePrefix():
        d_74_a_: _dafny.Set
        d_74_a_ = _dafny.Set({_dafny.Seq("abc"), _dafny.Seq("ab")})
        d_75_output_: _dafny.Seq
        out8_: _dafny.Seq
        out8_ = SortedSets.default__.SetToOrderedSequence(d_74_a_, default__.CharLess)
        d_75_output_ = out8_
        d_76_output2_: _dafny.Seq
        d_76_output2_ = SortedSets.default__.SetToOrderedSequence2(d_74_a_, default__.CharLess)
        d_77_expected_: _dafny.Seq
        d_77_expected_ = _dafny.Seq([_dafny.Seq("ab"), _dafny.Seq("abc")])
        if not((d_75_output_) == (d_77_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceCharLess.dfy(62,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_76_output2_) == (d_77_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceCharLess.dfy(63,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetToOrderedSequenceComplex():
        d_78_a_: _dafny.Set
        d_78_a_ = _dafny.Set({_dafny.Seq("abc"), _dafny.Seq("bbc"), _dafny.Seq("ab")})
        d_79_output_: _dafny.Seq
        out9_: _dafny.Seq
        out9_ = SortedSets.default__.SetToOrderedSequence(d_78_a_, default__.CharLess)
        d_79_output_ = out9_
        d_80_output2_: _dafny.Seq
        d_80_output2_ = SortedSets.default__.SetToOrderedSequence2(d_78_a_, default__.CharLess)
        d_81_expected_: _dafny.Seq
        d_81_expected_ = _dafny.Seq([_dafny.Seq("ab"), _dafny.Seq("abc"), _dafny.Seq("bbc")])
        if not((d_79_output_) == (d_81_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceCharLess.dfy(71,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_80_output2_) == (d_81_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceCharLess.dfy(72,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetToOrderedSequenceComplexReverse():
        d_82_a_: _dafny.Set
        d_82_a_ = _dafny.Set({_dafny.Seq("abc"), _dafny.Seq("bbc"), _dafny.Seq("ab")})
        d_83_output_: _dafny.Seq
        out10_: _dafny.Seq
        out10_ = SortedSets.default__.SetToOrderedSequence(d_82_a_, default__.CharGreater)
        d_83_output_ = out10_
        d_84_output2_: _dafny.Seq
        d_84_output2_ = SortedSets.default__.SetToOrderedSequence2(d_82_a_, default__.CharGreater)
        d_85_expected_: _dafny.Seq
        d_85_expected_ = _dafny.Seq([_dafny.Seq("bbc"), _dafny.Seq("ab"), _dafny.Seq("abc")])
        if not((d_83_output_) == (d_85_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceCharLess.dfy(80,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_84_output2_) == (d_85_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceCharLess.dfy(81,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetSequence():
        d_86_a_: _dafny.Set
        d_86_a_ = _dafny.Set({_dafny.Seq("abc"), _dafny.Seq("bbc"), _dafny.Seq("ab")})
        d_87_output_: _dafny.Seq
        d_87_output_ = SortedSets.default__.SetToSequence(d_86_a_)
        if not((_dafny.MultiSet(d_87_output_)) == (_dafny.MultiSet(d_86_a_))):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceCharLess.dfy(87,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetToOrderedComplexUnicode():
        d_88_a_: _dafny.Set
        d_88_a_ = _dafny.Set({_dafny.Seq("𐐷"), _dafny.Seq("&"), _dafny.Seq("Љ"), _dafny.Seq("ᝀ"), _dafny.Seq("🂡"), _dafny.Seq("｡"), _dafny.Seq("𐀂")})
        d_89_output_: _dafny.Seq
        out11_: _dafny.Seq
        out11_ = SortedSets.default__.SetToOrderedSequence(d_88_a_, default__.CharLess)
        d_89_output_ = out11_
        d_90_output2_: _dafny.Seq
        d_90_output2_ = SortedSets.default__.SetToOrderedSequence2(d_88_a_, default__.CharLess)
        d_91_expected_: _dafny.Seq
        d_91_expected_ = _dafny.Seq([_dafny.Seq("&"), _dafny.Seq("Љ"), _dafny.Seq("ᝀ"), _dafny.Seq("𐀂"), _dafny.Seq("𐐷"), _dafny.Seq("🂡"), _dafny.Seq("｡")])
        if not((d_89_output_) == (d_91_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceCharLess.dfy(116,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_90_output2_) == (d_91_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceCharLess.dfy(117,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

