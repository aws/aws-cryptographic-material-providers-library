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

# Module: TestSeqReaderReadElements

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def UInt8Greater(x, y):
        return (y) < (x)

    @staticmethod
    def TestSetToOrderedSequenceEmpty():
        d_169_output_: _dafny.Seq
        out5_: _dafny.Seq
        out5_ = SortedSets.default__.SetToOrderedSequence(_dafny.Set({}), StandardLibrary_UInt.default__.UInt8Less)
        d_169_output_ = out5_
        d_170_expected_: _dafny.Seq
        d_170_expected_ = _dafny.Seq([])
        if not((d_169_output_) == (d_170_expected_)):
            raise _dafny.HaltException("test/Sets.dfy(21,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetToOrderedSequenceOneItem():
        d_171_a_: _dafny.Set
        d_171_a_ = _dafny.Set({_dafny.Seq([0])})
        d_172_output_: _dafny.Seq
        out6_: _dafny.Seq
        out6_ = SortedSets.default__.SetToOrderedSequence(d_171_a_, StandardLibrary_UInt.default__.UInt8Less)
        d_172_output_ = out6_
        d_173_expected_: _dafny.Seq
        d_173_expected_ = _dafny.Seq([_dafny.Seq([0])])
        if not((d_172_output_) == (d_173_expected_)):
            raise _dafny.HaltException("test/Sets.dfy(28,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetToOrderedSequenceSimple():
        d_174_a_: _dafny.Set
        d_174_a_ = _dafny.Set({_dafny.Seq([0, 2]), _dafny.Seq([0, 1])})
        d_175_output_: _dafny.Seq
        out7_: _dafny.Seq
        out7_ = SortedSets.default__.SetToOrderedSequence(d_174_a_, StandardLibrary_UInt.default__.UInt8Less)
        d_175_output_ = out7_
        d_176_expected_: _dafny.Seq
        d_176_expected_ = _dafny.Seq([_dafny.Seq([0, 1]), _dafny.Seq([0, 2])])
        if not((d_175_output_) == (d_176_expected_)):
            raise _dafny.HaltException("test/Sets.dfy(35,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetToOrderedSequencePrefix():
        d_177_a_: _dafny.Set
        d_177_a_ = _dafny.Set({_dafny.Seq([0, 1, 2]), _dafny.Seq([0, 1])})
        d_178_output_: _dafny.Seq
        out8_: _dafny.Seq
        out8_ = SortedSets.default__.SetToOrderedSequence(d_177_a_, StandardLibrary_UInt.default__.UInt8Less)
        d_178_output_ = out8_
        d_179_expected_: _dafny.Seq
        d_179_expected_ = _dafny.Seq([_dafny.Seq([0, 1]), _dafny.Seq([0, 1, 2])])
        if not((d_178_output_) == (d_179_expected_)):
            raise _dafny.HaltException("test/Sets.dfy(42,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetToOrderedSequenceComplex():
        d_180_a_: _dafny.Set
        d_180_a_ = _dafny.Set({_dafny.Seq([0, 1, 2]), _dafny.Seq([1, 1, 2]), _dafny.Seq([0, 1])})
        d_181_output_: _dafny.Seq
        out9_: _dafny.Seq
        out9_ = SortedSets.default__.SetToOrderedSequence(d_180_a_, StandardLibrary_UInt.default__.UInt8Less)
        d_181_output_ = out9_
        d_182_expected_: _dafny.Seq
        d_182_expected_ = _dafny.Seq([_dafny.Seq([0, 1]), _dafny.Seq([0, 1, 2]), _dafny.Seq([1, 1, 2])])
        if not((d_181_output_) == (d_182_expected_)):
            raise _dafny.HaltException("test/Sets.dfy(49,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetToOrderedSequenceComplexReverse():
        d_183_a_: _dafny.Set
        d_183_a_ = _dafny.Set({_dafny.Seq([0, 1, 2]), _dafny.Seq([1, 1, 2]), _dafny.Seq([0, 1])})
        d_184_output_: _dafny.Seq
        out10_: _dafny.Seq
        out10_ = SortedSets.default__.SetToOrderedSequence(d_183_a_, default__.UInt8Greater)
        d_184_output_ = out10_
        d_185_expected_: _dafny.Seq
        d_185_expected_ = _dafny.Seq([_dafny.Seq([1, 1, 2]), _dafny.Seq([0, 1]), _dafny.Seq([0, 1, 2])])
        if not((d_184_output_) == (d_185_expected_)):
            raise _dafny.HaltException("test/Sets.dfy(56,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetSequence():
        d_186_a_: _dafny.Set
        d_186_a_ = _dafny.Set({_dafny.Seq([0, 1, 2]), _dafny.Seq([1, 1, 2]), _dafny.Seq([0, 1])})
        d_187_output_: _dafny.Seq
        d_187_output_ = SortedSets.default__.SetToSequence(d_186_a_)
        if not((_dafny.MultiSet(d_187_output_)) == (_dafny.MultiSet(d_186_a_))):
            raise _dafny.HaltException("test/Sets.dfy(62,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetToOrderedSequenceManyItems():
        d_188_a_: _dafny.Set
        def iife2_():
            coll1_ = _dafny.Set()
            compr_1_: int
            for compr_1_ in _dafny.IntegerRange(0, BoundedInts.default__.TWO__TO__THE__16):
                d_189_x_: int = compr_1_
                if ((0) <= (d_189_x_)) and ((d_189_x_) < (65535)):
                    coll1_ = coll1_.union(_dafny.Set([StandardLibrary_UInt.default__.UInt16ToSeq(d_189_x_)]))
            return _dafny.Set(coll1_)
        d_188_a_ = iife2_()
        
        d_190_output_: _dafny.Seq
        out11_: _dafny.Seq
        out11_ = SortedSets.default__.SetToOrderedSequence(d_188_a_, StandardLibrary_UInt.default__.UInt8Less)
        d_190_output_ = out11_
        d_191_expected_: _dafny.Seq
        d_191_expected_ = _dafny.Seq([StandardLibrary_UInt.default__.UInt16ToSeq(d_192_i_) for d_192_i_ in range(65535)])
        if not((d_190_output_) == (d_191_expected_)):
            raise _dafny.HaltException("test/Sets.dfy(69,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

