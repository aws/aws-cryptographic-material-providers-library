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
import TestComputeSetToOrderedSequenceUInt8Less
import JSON_Utils_Views_Core
import JSON_Utils_Views_Writers
import JSON_Utils_Views
import JSON_Utils_Lexers_Core
import JSON_Utils_Lexers_Strings
import JSON_Utils_Lexers
import JSON_Utils_Cursors
import JSON_Utils_Parsers
import JSON_Utils_Str_CharStrConversion
import JSON_Utils_Str_CharStrEscaping
import JSON_Utils_Str
import JSON_Utils_Seq
import JSON_Utils_Vectors
import JSON_Utils
import JSON_Errors
import JSON_Values
import JSON_Spec
import JSON_Grammar
import JSON_Serializer_ByteStrConversion
import JSON_Serializer
import JSON_Deserializer_Uint16StrConversion
import JSON_Deserializer_ByteStrConversion
import JSON_Deserializer
import JSON_ConcreteSyntax_Spec
import JSON_ConcreteSyntax_SpecProperties
import JSON_ConcreteSyntax
import JSON_ZeroCopy_Serializer
import JSON_ZeroCopy_Deserializer_Core
import JSON_ZeroCopy_Deserializer_Strings
import JSON_ZeroCopy_Deserializer_Numbers
import JSON_ZeroCopy_Deserializer_ObjectParams
import JSON_ZeroCopy_Deserializer_Objects
import JSON_ZeroCopy_Deserializer_ArrayParams
import JSON_ZeroCopy_Deserializer_Arrays
import JSON_ZeroCopy_Deserializer_Constants
import JSON_ZeroCopy_Deserializer_Values
import JSON_ZeroCopy_Deserializer_API
import JSON_ZeroCopy_Deserializer
import JSON_ZeroCopy_API
import JSON_ZeroCopy
import JSON_API
import JSON

# Module: module_

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Test____Main____(noArgsParameter__):
        d_317_success_: bool
        d_317_success_ = True
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUTF8.TestEncodeHappyCase: ")))
        try:
            if True:
                TestUTF8.default__.TestEncodeHappyCase()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_318_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_318_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUTF8.TestEncodeInvalidUnicode: ")))
        try:
            if True:
                TestUTF8.default__.TestEncodeInvalidUnicode()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_319_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_319_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUTF8.TestDecodeHappyCase: ")))
        try:
            if True:
                TestUTF8.default__.TestDecodeHappyCase()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_320_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_320_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUTF8.TestDecodeInvalidUnicode: ")))
        try:
            if True:
                TestUTF8.default__.TestDecodeInvalidUnicode()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_321_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_321_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUTF8.Test1Byte: ")))
        try:
            if True:
                TestUTF8.default__.Test1Byte()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_322_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_322_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUTF8.Test2Bytes: ")))
        try:
            if True:
                TestUTF8.default__.Test2Bytes()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_323_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_323_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUTF8.Test3Bytes: ")))
        try:
            if True:
                TestUTF8.default__.Test3Bytes()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_324_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_324_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUTF8.Test4Bytes: ")))
        try:
            if True:
                TestUTF8.default__.Test4Bytes()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_325_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_325_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestTime.TestNonDecreasing: ")))
        try:
            if True:
                TestTime.default__.TestNonDecreasing()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_326_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_326_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestTime.TestPositiveValues: ")))
        try:
            if True:
                TestTime.default__.TestPositiveValues()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_327_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_327_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestComputeSetToOrderedSequenceCharLess.TestSetToOrderedSequenceEmpty: ")))
        try:
            if True:
                TestComputeSetToOrderedSequenceCharLess.default__.TestSetToOrderedSequenceEmpty()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_328_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_328_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestComputeSetToOrderedSequenceCharLess.TestSetToOrderedSequenceOneItem: ")))
        try:
            if True:
                TestComputeSetToOrderedSequenceCharLess.default__.TestSetToOrderedSequenceOneItem()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_329_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_329_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestComputeSetToOrderedSequenceCharLess.TestSetToOrderedSequenceSimple: ")))
        try:
            if True:
                TestComputeSetToOrderedSequenceCharLess.default__.TestSetToOrderedSequenceSimple()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_330_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_330_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestComputeSetToOrderedSequenceCharLess.TestSetToOrderedSequencePrefix: ")))
        try:
            if True:
                TestComputeSetToOrderedSequenceCharLess.default__.TestSetToOrderedSequencePrefix()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_331_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_331_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestComputeSetToOrderedSequenceCharLess.TestSetToOrderedSequenceComplex: ")))
        try:
            if True:
                TestComputeSetToOrderedSequenceCharLess.default__.TestSetToOrderedSequenceComplex()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_332_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_332_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestComputeSetToOrderedSequenceCharLess.TestSetToOrderedSequenceComplexReverse: ")))
        try:
            if True:
                TestComputeSetToOrderedSequenceCharLess.default__.TestSetToOrderedSequenceComplexReverse()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_333_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_333_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestComputeSetToOrderedSequenceCharLess.TestSetSequence: ")))
        try:
            if True:
                TestComputeSetToOrderedSequenceCharLess.default__.TestSetSequence()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_334_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_334_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestComputeSetToOrderedSequenceCharLess.TestSetToOrderedComplexUnicode: ")))
        try:
            if True:
                TestComputeSetToOrderedSequenceCharLess.default__.TestSetToOrderedComplexUnicode()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_335_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_335_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestHexStrings.BasicTests: ")))
        try:
            if True:
                TestHexStrings.default__.BasicTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_336_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_336_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("FloatCompareTest.TestOneTwoZeroMatrix: ")))
        try:
            if True:
                FloatCompareTest.default__.TestOneTwoZeroMatrix()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_337_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_337_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("FloatCompareTest.SimpleTests: ")))
        try:
            if True:
                FloatCompareTest.default__.SimpleTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_338_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_338_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("FloatCompareTest.SignTests: ")))
        try:
            if True:
                FloatCompareTest.default__.SignTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_339_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_339_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("FloatCompareTest.ExponentTests: ")))
        try:
            if True:
                FloatCompareTest.default__.ExponentTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_340_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_340_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("FloatCompareTest.ZeroTests: ")))
        try:
            if True:
                FloatCompareTest.default__.ZeroTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_341_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_341_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("FloatCompareTest.ExtremeNumTest: ")))
        try:
            if True:
                FloatCompareTest.default__.ExtremeNumTest()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_342_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_342_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("FloatCompareTest.InvalidTests: ")))
        try:
            if True:
                FloatCompareTest.default__.InvalidTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_343_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_343_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestCallMany.TestBasic: ")))
        try:
            if True:
                TestCallMany.default__.TestBasic()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_344_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_344_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("GetOptTest.TestEmpty: ")))
        try:
            if True:
                GetOptTest.default__.TestEmpty()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_345_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_345_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("GetOptTest.TestShort: ")))
        try:
            if True:
                GetOptTest.default__.TestShort()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_346_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_346_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("GetOptTest.TestLong: ")))
        try:
            if True:
                GetOptTest.default__.TestLong()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_347_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_347_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("GetOptTest.TestRequired: ")))
        try:
            if True:
                GetOptTest.default__.TestRequired()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_348_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_348_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("GetOptTest.TestDeprecated: ")))
        try:
            if True:
                GetOptTest.default__.TestDeprecated()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_349_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_349_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("GetOptTest.TestAlias: ")))
        try:
            if True:
                GetOptTest.default__.TestAlias()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_350_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_350_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("GetOptTest.TestPositionalFail: ")))
        try:
            if True:
                GetOptTest.default__.TestPositionalFail()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_351_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_351_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("GetOptTest.TestPositional: ")))
        try:
            if True:
                GetOptTest.default__.TestPositional()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_352_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_352_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("GetOptTest.TestHelp: ")))
        try:
            if True:
                GetOptTest.default__.TestHelp()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_353_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_353_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("GetOptTest.TestHelpFail: ")))
        try:
            if True:
                GetOptTest.default__.TestHelpFail()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_354_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_354_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("GetOptTest.TestNested: ")))
        try:
            if True:
                GetOptTest.default__.TestNested()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_355_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_355_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("GetOptTest.TestDefault: ")))
        try:
            if True:
                GetOptTest.default__.TestDefault()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_356_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_356_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("GetOptTest.TestDdbec: ")))
        try:
            if True:
                GetOptTest.default__.TestDdbec()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_357_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_357_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUUID.TestFromBytesSuccess: ")))
        try:
            if True:
                TestUUID.default__.TestFromBytesSuccess()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_358_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_358_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUUID.TestFromBytesFailure: ")))
        try:
            if True:
                TestUUID.default__.TestFromBytesFailure()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_359_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_359_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUUID.TestToBytesSuccess: ")))
        try:
            if True:
                TestUUID.default__.TestToBytesSuccess()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_360_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_360_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUUID.TestToBytesFailure: ")))
        try:
            if True:
                TestUUID.default__.TestToBytesFailure()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_361_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_361_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUUID.TestRoundTripStringConversion: ")))
        try:
            if True:
                TestUUID.default__.TestRoundTripStringConversion()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_362_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_362_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUUID.TestRoundTripByteConversion: ")))
        try:
            if True:
                TestUUID.default__.TestRoundTripByteConversion()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_363_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_363_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUUID.TestGenerateAndConversion: ")))
        try:
            if True:
                TestUUID.default__.TestGenerateAndConversion()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_364_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_364_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestComputeSetToOrderedSequenceUInt8Less.TestSetToOrderedSequenceEmpty: ")))
        try:
            if True:
                TestComputeSetToOrderedSequenceUInt8Less.default__.TestSetToOrderedSequenceEmpty()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_365_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_365_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestComputeSetToOrderedSequenceUInt8Less.TestSetToOrderedSequenceOneItem: ")))
        try:
            if True:
                TestComputeSetToOrderedSequenceUInt8Less.default__.TestSetToOrderedSequenceOneItem()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_366_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_366_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestComputeSetToOrderedSequenceUInt8Less.TestSetToOrderedSequenceSimple: ")))
        try:
            if True:
                TestComputeSetToOrderedSequenceUInt8Less.default__.TestSetToOrderedSequenceSimple()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_367_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_367_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestComputeSetToOrderedSequenceUInt8Less.TestSetToOrderedSequencePrefix: ")))
        try:
            if True:
                TestComputeSetToOrderedSequenceUInt8Less.default__.TestSetToOrderedSequencePrefix()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_368_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_368_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestComputeSetToOrderedSequenceUInt8Less.TestSetToOrderedSequenceComplex: ")))
        try:
            if True:
                TestComputeSetToOrderedSequenceUInt8Less.default__.TestSetToOrderedSequenceComplex()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_369_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_369_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestComputeSetToOrderedSequenceUInt8Less.TestSetToOrderedSequenceComplexReverse: ")))
        try:
            if True:
                TestComputeSetToOrderedSequenceUInt8Less.default__.TestSetToOrderedSequenceComplexReverse()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_370_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_370_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestComputeSetToOrderedSequenceUInt8Less.TestSetSequence: ")))
        try:
            if True:
                TestComputeSetToOrderedSequenceUInt8Less.default__.TestSetSequence()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_371_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_371_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestComputeSetToOrderedSequenceUInt8Less.TestSetToOrderedSequenceManyItems: ")))
        try:
            if True:
                TestComputeSetToOrderedSequenceUInt8Less.default__.TestSetToOrderedSequenceManyItems()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_372_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_372_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_317_success_ = False
        if not(d_317_success_):
            raise _dafny.HaltException("<stdin>(1,0): " + _dafny.string_of(_dafny.Seq("Test failures occurred: see above.\n")))

