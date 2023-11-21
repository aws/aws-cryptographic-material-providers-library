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
import FloatCompareTest
import Relations
import Seq_mMergeSort
import Math
import Seq
import SortedSets

assert "TestSeqReaderReadElements" == __name__
TestSeqReaderReadElements = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def UInt8Greater(x, y):
        return (y) < (x)

    @staticmethod
    def TestSetToOrderedSequenceEmpty():
        d_54_output_: _dafny.Seq
        out1_: _dafny.Seq
        out1_ = SortedSets.default__.SetToOrderedSequence(_dafny.Set({}), StandardLibrary_mUInt.default__.UInt8Less)
        d_54_output_ = out1_
        d_55_expected_: _dafny.Seq
        d_55_expected_ = _dafny.Seq([])
        if not((d_54_output_) == (d_55_expected_)):
            raise _dafny.HaltException("test/Sets.dfy(21,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetToOrderedSequenceOneItem():
        d_56_a_: _dafny.Set
        d_56_a_ = _dafny.Set({_dafny.Seq([0])})
        d_57_output_: _dafny.Seq
        out2_: _dafny.Seq
        out2_ = SortedSets.default__.SetToOrderedSequence(d_56_a_, StandardLibrary_mUInt.default__.UInt8Less)
        d_57_output_ = out2_
        d_58_expected_: _dafny.Seq
        d_58_expected_ = _dafny.Seq([_dafny.Seq([0])])
        if not((d_57_output_) == (d_58_expected_)):
            raise _dafny.HaltException("test/Sets.dfy(28,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetToOrderedSequenceSimple():
        d_59_a_: _dafny.Set
        d_59_a_ = _dafny.Set({_dafny.Seq([0, 2]), _dafny.Seq([0, 1])})
        d_60_output_: _dafny.Seq
        out3_: _dafny.Seq
        out3_ = SortedSets.default__.SetToOrderedSequence(d_59_a_, StandardLibrary_mUInt.default__.UInt8Less)
        d_60_output_ = out3_
        d_61_expected_: _dafny.Seq
        d_61_expected_ = _dafny.Seq([_dafny.Seq([0, 1]), _dafny.Seq([0, 2])])
        if not((d_60_output_) == (d_61_expected_)):
            raise _dafny.HaltException("test/Sets.dfy(35,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetToOrderedSequencePrefix():
        d_62_a_: _dafny.Set
        d_62_a_ = _dafny.Set({_dafny.Seq([0, 1, 2]), _dafny.Seq([0, 1])})
        d_63_output_: _dafny.Seq
        out4_: _dafny.Seq
        out4_ = SortedSets.default__.SetToOrderedSequence(d_62_a_, StandardLibrary_mUInt.default__.UInt8Less)
        d_63_output_ = out4_
        d_64_expected_: _dafny.Seq
        d_64_expected_ = _dafny.Seq([_dafny.Seq([0, 1]), _dafny.Seq([0, 1, 2])])
        if not((d_63_output_) == (d_64_expected_)):
            raise _dafny.HaltException("test/Sets.dfy(42,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetToOrderedSequenceComplex():
        d_65_a_: _dafny.Set
        d_65_a_ = _dafny.Set({_dafny.Seq([0, 1, 2]), _dafny.Seq([1, 1, 2]), _dafny.Seq([0, 1])})
        d_66_output_: _dafny.Seq
        out5_: _dafny.Seq
        out5_ = SortedSets.default__.SetToOrderedSequence(d_65_a_, StandardLibrary_mUInt.default__.UInt8Less)
        d_66_output_ = out5_
        d_67_expected_: _dafny.Seq
        d_67_expected_ = _dafny.Seq([_dafny.Seq([0, 1]), _dafny.Seq([0, 1, 2]), _dafny.Seq([1, 1, 2])])
        if not((d_66_output_) == (d_67_expected_)):
            raise _dafny.HaltException("test/Sets.dfy(49,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetToOrderedSequenceComplexReverse():
        d_68_a_: _dafny.Set
        d_68_a_ = _dafny.Set({_dafny.Seq([0, 1, 2]), _dafny.Seq([1, 1, 2]), _dafny.Seq([0, 1])})
        d_69_output_: _dafny.Seq
        out6_: _dafny.Seq
        out6_ = SortedSets.default__.SetToOrderedSequence(d_68_a_, TestSeqReaderReadElements.default__.UInt8Greater)
        d_69_output_ = out6_
        d_70_expected_: _dafny.Seq
        d_70_expected_ = _dafny.Seq([_dafny.Seq([1, 1, 2]), _dafny.Seq([0, 1]), _dafny.Seq([0, 1, 2])])
        if not((d_69_output_) == (d_70_expected_)):
            raise _dafny.HaltException("test/Sets.dfy(56,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetSequence():
        d_71_a_: _dafny.Set
        d_71_a_ = _dafny.Set({_dafny.Seq([0, 1, 2]), _dafny.Seq([1, 1, 2]), _dafny.Seq([0, 1])})
        d_72_output_: _dafny.Seq
        d_72_output_ = SortedSets.default__.SetToSequence(d_71_a_)
        if not((_dafny.MultiSet(d_72_output_)) == (_dafny.MultiSet(d_71_a_))):
            raise _dafny.HaltException("test/Sets.dfy(62,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetToOrderedSequenceManyItems():
        d_73_a_: _dafny.Set
        def iife0_():
            coll0_ = _dafny.Set()
            compr_0_: int
            for compr_0_ in _dafny.IntegerRange(0, (BoundedInts.default__).TWO__TO__THE__16):
                d_74_x_: BoundedInts.uint16 = compr_0_
                if ((0) <= (d_74_x_)) and ((d_74_x_) < (65535)):
                    coll0_ = coll0_.union(_dafny.Set([StandardLibrary_mUInt.default__.UInt16ToSeq(d_74_x_)]))
            return _dafny.Set(coll0_)
        d_73_a_ = iife0_()
        
        d_75_output_: _dafny.Seq
        out7_: _dafny.Seq
        out7_ = SortedSets.default__.SetToOrderedSequence(d_73_a_, StandardLibrary_mUInt.default__.UInt8Less)
        d_75_output_ = out7_
        d_76_expected_: _dafny.Seq
        d_76_expected_ = _dafny.Seq([StandardLibrary_mUInt.default__.UInt16ToSeq(d_77_i_) for d_77_i_ in range(65535)])
        if not((d_75_output_) == (d_76_expected_)):
            raise _dafny.HaltException("test/Sets.dfy(69,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

