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
import FloatCompareTest
import TestCallMany
import GetOpt
import GetOptTest
import TestUUID

# Module: TestComputeSetToOrderedSequenceUInt8Less

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def UInt8Greater(x, y):
        return (y) < (x)

    @staticmethod
    def TestSetToOrderedSequenceEmpty():
        d_286_output_: _dafny.Seq
        out12_: _dafny.Seq
        out12_ = SortedSets.default__.SetToOrderedSequence(_dafny.Set({}), StandardLibrary_UInt.default__.UInt8Less)
        d_286_output_ = out12_
        d_287_output2_: _dafny.Seq
        d_287_output2_ = SortedSets.default__.SetToOrderedSequence2(_dafny.Set({}), StandardLibrary_UInt.default__.UInt8Less)
        d_288_expected_: _dafny.Seq
        d_288_expected_ = _dafny.Seq([])
        if not((d_286_output_) == (d_288_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(29,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_287_output2_) == (d_288_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(30,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetToOrderedSequenceOneItem():
        d_289_a_: _dafny.Set
        d_289_a_ = _dafny.Set({_dafny.Seq([0])})
        d_290_output_: _dafny.Seq
        out13_: _dafny.Seq
        out13_ = SortedSets.default__.SetToOrderedSequence(d_289_a_, StandardLibrary_UInt.default__.UInt8Less)
        d_290_output_ = out13_
        d_291_output2_: _dafny.Seq
        d_291_output2_ = SortedSets.default__.SetToOrderedSequence2(d_289_a_, StandardLibrary_UInt.default__.UInt8Less)
        d_292_expected_: _dafny.Seq
        d_292_expected_ = _dafny.Seq([_dafny.Seq([0])])
        if not((d_290_output_) == (d_292_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(38,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_291_output2_) == (d_292_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(39,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetToOrderedSequenceSimple():
        d_293_a_: _dafny.Set
        d_293_a_ = _dafny.Set({_dafny.Seq([0, 2]), _dafny.Seq([0, 1])})
        d_294_output_: _dafny.Seq
        out14_: _dafny.Seq
        out14_ = SortedSets.default__.SetToOrderedSequence(d_293_a_, StandardLibrary_UInt.default__.UInt8Less)
        d_294_output_ = out14_
        d_295_output2_: _dafny.Seq
        d_295_output2_ = SortedSets.default__.SetToOrderedSequence2(d_293_a_, StandardLibrary_UInt.default__.UInt8Less)
        d_296_expected_: _dafny.Seq
        d_296_expected_ = _dafny.Seq([_dafny.Seq([0, 1]), _dafny.Seq([0, 2])])
        if not((d_294_output_) == (d_296_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(47,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_295_output2_) == (d_296_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(48,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetToOrderedSequencePrefix():
        d_297_a_: _dafny.Set
        d_297_a_ = _dafny.Set({_dafny.Seq([0, 1, 2]), _dafny.Seq([0, 1])})
        d_298_output_: _dafny.Seq
        out15_: _dafny.Seq
        out15_ = SortedSets.default__.SetToOrderedSequence(d_297_a_, StandardLibrary_UInt.default__.UInt8Less)
        d_298_output_ = out15_
        d_299_output2_: _dafny.Seq
        d_299_output2_ = SortedSets.default__.SetToOrderedSequence2(d_297_a_, StandardLibrary_UInt.default__.UInt8Less)
        d_300_expected_: _dafny.Seq
        d_300_expected_ = _dafny.Seq([_dafny.Seq([0, 1]), _dafny.Seq([0, 1, 2])])
        if not((d_298_output_) == (d_300_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(56,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_299_output2_) == (d_300_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(57,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetToOrderedSequenceComplex():
        d_301_a_: _dafny.Set
        d_301_a_ = _dafny.Set({_dafny.Seq([0, 1, 2]), _dafny.Seq([1, 1, 2]), _dafny.Seq([0, 1])})
        d_302_output_: _dafny.Seq
        out16_: _dafny.Seq
        out16_ = SortedSets.default__.SetToOrderedSequence(d_301_a_, StandardLibrary_UInt.default__.UInt8Less)
        d_302_output_ = out16_
        d_303_output2_: _dafny.Seq
        d_303_output2_ = SortedSets.default__.SetToOrderedSequence2(d_301_a_, StandardLibrary_UInt.default__.UInt8Less)
        d_304_expected_: _dafny.Seq
        d_304_expected_ = _dafny.Seq([_dafny.Seq([0, 1]), _dafny.Seq([0, 1, 2]), _dafny.Seq([1, 1, 2])])
        if not((d_302_output_) == (d_304_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(65,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_303_output2_) == (d_304_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(66,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetToOrderedSequenceComplexReverse():
        d_305_a_: _dafny.Set
        d_305_a_ = _dafny.Set({_dafny.Seq([0, 1, 2]), _dafny.Seq([1, 1, 2]), _dafny.Seq([0, 1])})
        d_306_output_: _dafny.Seq
        out17_: _dafny.Seq
        out17_ = SortedSets.default__.SetToOrderedSequence(d_305_a_, default__.UInt8Greater)
        d_306_output_ = out17_
        d_307_output2_: _dafny.Seq
        d_307_output2_ = SortedSets.default__.SetToOrderedSequence2(d_305_a_, default__.UInt8Greater)
        d_308_expected_: _dafny.Seq
        d_308_expected_ = _dafny.Seq([_dafny.Seq([1, 1, 2]), _dafny.Seq([0, 1]), _dafny.Seq([0, 1, 2])])
        if not((d_306_output_) == (d_308_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(74,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_307_output2_) == (d_308_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(75,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetSequence():
        d_309_a_: _dafny.Set
        d_309_a_ = _dafny.Set({_dafny.Seq([0, 1, 2]), _dafny.Seq([1, 1, 2]), _dafny.Seq([0, 1])})
        d_310_output_: _dafny.Seq
        d_310_output_ = SortedSets.default__.SetToSequence(d_309_a_)
        if not((_dafny.MultiSet(d_310_output_)) == (_dafny.MultiSet(d_309_a_))):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(81,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetToOrderedSequenceManyItems():
        d_311_a_: _dafny.Set
        def iife13_():
            coll2_ = _dafny.Set()
            compr_2_: int
            for compr_2_ in _dafny.IntegerRange(0, BoundedInts.default__.TWO__TO__THE__16):
                d_312_x_: int = compr_2_
                if ((0) <= (d_312_x_)) and ((d_312_x_) < (65535)):
                    coll2_ = coll2_.union(_dafny.Set([StandardLibrary_UInt.default__.UInt16ToSeq(d_312_x_)]))
            return _dafny.Set(coll2_)
        d_311_a_ = iife13_()
        
        d_313_output_: _dafny.Seq
        out18_: _dafny.Seq
        out18_ = SortedSets.default__.SetToOrderedSequence(d_311_a_, StandardLibrary_UInt.default__.UInt8Less)
        d_313_output_ = out18_
        d_314_output2_: _dafny.Seq
        d_314_output2_ = SortedSets.default__.SetToOrderedSequence2(d_311_a_, StandardLibrary_UInt.default__.UInt8Less)
        d_315_expected_: _dafny.Seq
        d_315_expected_ = _dafny.Seq([StandardLibrary_UInt.default__.UInt16ToSeq(d_316_i_) for d_316_i_ in range(65535)])
        if not((d_313_output_) == (d_315_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(89,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_314_output2_) == (d_315_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(90,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

