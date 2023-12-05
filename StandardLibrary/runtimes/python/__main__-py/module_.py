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
import FloatCompareTest
import ConcurrentCall
import TestCallMany
import UUID
import TestUUID

# Module: module_

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Test____Main____(noArgsParameter__):
        d_270_success_: bool
        d_270_success_ = True
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUTF8.TestEncodeHappyCase: ")))
        try:
            if True:
                TestUTF8.default__.TestEncodeHappyCase()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_271_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_271_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_270_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUTF8.TestEncodeInvalidUnicode: ")))
        try:
            if True:
                TestUTF8.default__.TestEncodeInvalidUnicode()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_272_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_272_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_270_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUTF8.TestDecodeHappyCase: ")))
        try:
            if True:
                TestUTF8.default__.TestDecodeHappyCase()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_273_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_273_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_270_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUTF8.TestDecodeInvalidUnicode: ")))
        try:
            if True:
                TestUTF8.default__.TestDecodeInvalidUnicode()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_274_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_274_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_270_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUTF8.Test1Byte: ")))
        try:
            if True:
                TestUTF8.default__.Test1Byte()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_275_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_275_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_270_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUTF8.Test2Bytes: ")))
        try:
            if True:
                TestUTF8.default__.Test2Bytes()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_276_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_276_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_270_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUTF8.Test3Bytes: ")))
        try:
            if True:
                TestUTF8.default__.Test3Bytes()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_277_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_277_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_270_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUTF8.Test4Bytes: ")))
        try:
            if True:
                TestUTF8.default__.Test4Bytes()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_278_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_278_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_270_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestTime.TestNonDecreasing: ")))
        try:
            if True:
                TestTime.default__.TestNonDecreasing()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_279_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_279_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_270_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestTime.TestPositiveValues: ")))
        try:
            if True:
                TestTime.default__.TestPositiveValues()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_280_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_280_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_270_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestHexStrings.BasicTests: ")))
        try:
            if True:
                TestHexStrings.default__.BasicTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_281_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_281_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_270_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestSeqReaderReadElements.TestSetToOrderedSequenceEmpty: ")))
        try:
            if True:
                TestSeqReaderReadElements.default__.TestSetToOrderedSequenceEmpty()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_282_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_282_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_270_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestSeqReaderReadElements.TestSetToOrderedSequenceOneItem: ")))
        try:
            if True:
                TestSeqReaderReadElements.default__.TestSetToOrderedSequenceOneItem()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_283_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_283_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_270_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestSeqReaderReadElements.TestSetToOrderedSequenceSimple: ")))
        try:
            if True:
                TestSeqReaderReadElements.default__.TestSetToOrderedSequenceSimple()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_284_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_284_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_270_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestSeqReaderReadElements.TestSetToOrderedSequencePrefix: ")))
        try:
            if True:
                TestSeqReaderReadElements.default__.TestSetToOrderedSequencePrefix()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_285_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_285_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_270_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestSeqReaderReadElements.TestSetToOrderedSequenceComplex: ")))
        try:
            if True:
                TestSeqReaderReadElements.default__.TestSetToOrderedSequenceComplex()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_286_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_286_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_270_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestSeqReaderReadElements.TestSetToOrderedSequenceComplexReverse: ")))
        try:
            if True:
                TestSeqReaderReadElements.default__.TestSetToOrderedSequenceComplexReverse()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_287_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_287_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_270_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestSeqReaderReadElements.TestSetSequence: ")))
        try:
            if True:
                TestSeqReaderReadElements.default__.TestSetSequence()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_288_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_288_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_270_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestSeqReaderReadElements.TestSetToOrderedSequenceManyItems: ")))
        try:
            if True:
                TestSeqReaderReadElements.default__.TestSetToOrderedSequenceManyItems()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_289_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_289_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_270_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("FloatCompareTest.TestOneTwoZeroMatrix: ")))
        try:
            if True:
                FloatCompareTest.default__.TestOneTwoZeroMatrix()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_290_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_290_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_270_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("FloatCompareTest.SimpleTests: ")))
        try:
            if True:
                FloatCompareTest.default__.SimpleTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_291_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_291_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_270_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("FloatCompareTest.SignTests: ")))
        try:
            if True:
                FloatCompareTest.default__.SignTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_292_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_292_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_270_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("FloatCompareTest.ExponentTests: ")))
        try:
            if True:
                FloatCompareTest.default__.ExponentTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_293_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_293_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_270_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("FloatCompareTest.ZeroTests: ")))
        try:
            if True:
                FloatCompareTest.default__.ZeroTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_294_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_294_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_270_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("FloatCompareTest.ExtremeNumTest: ")))
        try:
            if True:
                FloatCompareTest.default__.ExtremeNumTest()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_295_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_295_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_270_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("FloatCompareTest.InvalidTests: ")))
        try:
            if True:
                FloatCompareTest.default__.InvalidTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_296_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_296_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_270_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestCallMany.TestBasic: ")))
        try:
            if True:
                TestCallMany.default__.TestBasic()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_297_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_297_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_270_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUUID.TestFromBytesSuccess: ")))
        try:
            if True:
                TestUUID.default__.TestFromBytesSuccess()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_298_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_298_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_270_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUUID.TestFromBytesFailure: ")))
        try:
            if True:
                TestUUID.default__.TestFromBytesFailure()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_299_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_299_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_270_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUUID.TestToBytesSuccess: ")))
        try:
            if True:
                TestUUID.default__.TestToBytesSuccess()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_300_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_300_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_270_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUUID.TestToBytesFailure: ")))
        try:
            if True:
                TestUUID.default__.TestToBytesFailure()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_301_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_301_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_270_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUUID.TestRoundTripStringConversion: ")))
        try:
            if True:
                TestUUID.default__.TestRoundTripStringConversion()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_302_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_302_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_270_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUUID.TestRoundTripByteConversion: ")))
        try:
            if True:
                TestUUID.default__.TestRoundTripByteConversion()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_303_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_303_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_270_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUUID.TestGenerateAndConversion: ")))
        try:
            if True:
                TestUUID.default__.TestGenerateAndConversion()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_304_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_304_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_270_success_ = False
        if not(d_270_success_):
            raise _dafny.HaltException("<stdin>(1,0): " + _dafny.string_of(_dafny.Seq("Test failures occurred: see above.\n")))

