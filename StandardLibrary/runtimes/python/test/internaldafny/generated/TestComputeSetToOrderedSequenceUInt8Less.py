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
import FloatCompareTest as FloatCompareTest
import TestCallMany as TestCallMany
import GetOptTest as GetOptTest
import TestUUID as TestUUID

# Module: TestComputeSetToOrderedSequenceUInt8Less

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def UInt8Greater(x, y):
        return (y) < (x)

    @staticmethod
    def TestSetToOrderedSequenceEmpty():
        d_203_output_: _dafny.Seq
        out13_: _dafny.Seq
        out13_ = SortedSets.default__.SetToOrderedSequence(_dafny.Set({}), StandardLibrary_UInt.default__.UInt8Less)
        d_203_output_ = out13_
        d_204_output2_: _dafny.Seq
        d_204_output2_ = SortedSets.default__.SetToOrderedSequence2(_dafny.Set({}), StandardLibrary_UInt.default__.UInt8Less)
        d_205_expected_: _dafny.Seq
        d_205_expected_ = _dafny.Seq([])
        if not((d_203_output_) == (d_205_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(29,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_204_output2_) == (d_205_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(30,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetToOrderedSequenceOneItem():
        d_206_a_: _dafny.Set
        d_206_a_ = _dafny.Set({_dafny.Seq([0])})
        d_207_output_: _dafny.Seq
        out14_: _dafny.Seq
        out14_ = SortedSets.default__.SetToOrderedSequence(d_206_a_, StandardLibrary_UInt.default__.UInt8Less)
        d_207_output_ = out14_
        d_208_output2_: _dafny.Seq
        d_208_output2_ = SortedSets.default__.SetToOrderedSequence2(d_206_a_, StandardLibrary_UInt.default__.UInt8Less)
        d_209_expected_: _dafny.Seq
        d_209_expected_ = _dafny.Seq([_dafny.Seq([0])])
        if not((d_207_output_) == (d_209_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(38,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_208_output2_) == (d_209_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(39,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetToOrderedSequenceSimple():
        d_210_a_: _dafny.Set
        d_210_a_ = _dafny.Set({_dafny.Seq([0, 2]), _dafny.Seq([0, 1])})
        d_211_output_: _dafny.Seq
        out15_: _dafny.Seq
        out15_ = SortedSets.default__.SetToOrderedSequence(d_210_a_, StandardLibrary_UInt.default__.UInt8Less)
        d_211_output_ = out15_
        d_212_output2_: _dafny.Seq
        d_212_output2_ = SortedSets.default__.SetToOrderedSequence2(d_210_a_, StandardLibrary_UInt.default__.UInt8Less)
        d_213_expected_: _dafny.Seq
        d_213_expected_ = _dafny.Seq([_dafny.Seq([0, 1]), _dafny.Seq([0, 2])])
        if not((d_211_output_) == (d_213_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(47,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_212_output2_) == (d_213_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(48,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetToOrderedSequencePrefix():
        d_214_a_: _dafny.Set
        d_214_a_ = _dafny.Set({_dafny.Seq([0, 1, 2]), _dafny.Seq([0, 1])})
        d_215_output_: _dafny.Seq
        out16_: _dafny.Seq
        out16_ = SortedSets.default__.SetToOrderedSequence(d_214_a_, StandardLibrary_UInt.default__.UInt8Less)
        d_215_output_ = out16_
        d_216_output2_: _dafny.Seq
        d_216_output2_ = SortedSets.default__.SetToOrderedSequence2(d_214_a_, StandardLibrary_UInt.default__.UInt8Less)
        d_217_expected_: _dafny.Seq
        d_217_expected_ = _dafny.Seq([_dafny.Seq([0, 1]), _dafny.Seq([0, 1, 2])])
        if not((d_215_output_) == (d_217_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(56,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_216_output2_) == (d_217_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(57,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetToOrderedSequenceComplex():
        d_218_a_: _dafny.Set
        d_218_a_ = _dafny.Set({_dafny.Seq([0, 1, 2]), _dafny.Seq([1, 1, 2]), _dafny.Seq([0, 1])})
        d_219_output_: _dafny.Seq
        out17_: _dafny.Seq
        out17_ = SortedSets.default__.SetToOrderedSequence(d_218_a_, StandardLibrary_UInt.default__.UInt8Less)
        d_219_output_ = out17_
        d_220_output2_: _dafny.Seq
        d_220_output2_ = SortedSets.default__.SetToOrderedSequence2(d_218_a_, StandardLibrary_UInt.default__.UInt8Less)
        d_221_expected_: _dafny.Seq
        d_221_expected_ = _dafny.Seq([_dafny.Seq([0, 1]), _dafny.Seq([0, 1, 2]), _dafny.Seq([1, 1, 2])])
        if not((d_219_output_) == (d_221_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(65,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_220_output2_) == (d_221_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(66,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetToOrderedSequenceComplexReverse():
        d_222_a_: _dafny.Set
        d_222_a_ = _dafny.Set({_dafny.Seq([0, 1, 2]), _dafny.Seq([1, 1, 2]), _dafny.Seq([0, 1])})
        d_223_output_: _dafny.Seq
        out18_: _dafny.Seq
        out18_ = SortedSets.default__.SetToOrderedSequence(d_222_a_, default__.UInt8Greater)
        d_223_output_ = out18_
        d_224_output2_: _dafny.Seq
        d_224_output2_ = SortedSets.default__.SetToOrderedSequence2(d_222_a_, default__.UInt8Greater)
        d_225_expected_: _dafny.Seq
        d_225_expected_ = _dafny.Seq([_dafny.Seq([1, 1, 2]), _dafny.Seq([0, 1]), _dafny.Seq([0, 1, 2])])
        if not((d_223_output_) == (d_225_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(74,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_224_output2_) == (d_225_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(75,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetSequence():
        d_226_a_: _dafny.Set
        d_226_a_ = _dafny.Set({_dafny.Seq([0, 1, 2]), _dafny.Seq([1, 1, 2]), _dafny.Seq([0, 1])})
        d_227_output_: _dafny.Seq
        d_227_output_ = SortedSets.default__.SetToSequence(d_226_a_)
        if not((_dafny.MultiSet(d_227_output_)) == (_dafny.MultiSet(d_226_a_))):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(81,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestSetToOrderedSequenceManyItems():
        d_228_a_: _dafny.Set
        def iife3_():
            coll2_ = _dafny.Set()
            compr_2_: int
            for compr_2_ in _dafny.IntegerRange(0, BoundedInts.default__.TWO__TO__THE__16):
                d_229_x_: int = compr_2_
                if True:
                    if ((0) <= (d_229_x_)) and ((d_229_x_) < (65535)):
                        coll2_ = coll2_.union(_dafny.Set([StandardLibrary_UInt.default__.UInt16ToSeq(d_229_x_)]))
            return _dafny.Set(coll2_)
        d_228_a_ = iife3_()
        
        d_230_output_: _dafny.Seq
        out19_: _dafny.Seq
        out19_ = SortedSets.default__.SetToOrderedSequence(d_228_a_, StandardLibrary_UInt.default__.UInt8Less)
        d_230_output_ = out19_
        d_231_output2_: _dafny.Seq
        d_231_output2_ = SortedSets.default__.SetToOrderedSequence2(d_228_a_, StandardLibrary_UInt.default__.UInt8Less)
        d_232_expected_: _dafny.Seq
        d_232_expected_ = _dafny.Seq([StandardLibrary_UInt.default__.UInt16ToSeq(d_233_i_) for d_233_i_ in range(65535)])
        if not((d_230_output_) == (d_232_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(89,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_231_output2_) == (d_232_expected_)):
            raise _dafny.HaltException("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(90,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

