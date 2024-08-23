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
import TestComputeSetToOrderedSequenceUInt8Less as TestComputeSetToOrderedSequenceUInt8Less
import standard_library.internaldafny.generated.JSON_Utils_Views_Core as JSON_Utils_Views_Core
import standard_library.internaldafny.generated.JSON_Utils_Views_Writers as JSON_Utils_Views_Writers
import standard_library.internaldafny.generated.JSON_Utils_Lexers_Core as JSON_Utils_Lexers_Core
import standard_library.internaldafny.generated.JSON_Utils_Lexers_Strings as JSON_Utils_Lexers_Strings
import standard_library.internaldafny.generated.JSON_Utils_Cursors as JSON_Utils_Cursors
import standard_library.internaldafny.generated.JSON_Utils_Parsers as JSON_Utils_Parsers
import standard_library.internaldafny.generated.JSON_Utils_Str_CharStrConversion as JSON_Utils_Str_CharStrConversion
import standard_library.internaldafny.generated.JSON_Utils_Str_CharStrEscaping as JSON_Utils_Str_CharStrEscaping
import standard_library.internaldafny.generated.JSON_Utils_Str as JSON_Utils_Str
import standard_library.internaldafny.generated.JSON_Utils_Seq as JSON_Utils_Seq
import standard_library.internaldafny.generated.JSON_Utils_Vectors as JSON_Utils_Vectors
import standard_library.internaldafny.generated.JSON_Errors as JSON_Errors
import standard_library.internaldafny.generated.JSON_Values as JSON_Values
import standard_library.internaldafny.generated.JSON_Spec as JSON_Spec
import standard_library.internaldafny.generated.JSON_Grammar as JSON_Grammar
import standard_library.internaldafny.generated.JSON_Serializer_ByteStrConversion as JSON_Serializer_ByteStrConversion
import standard_library.internaldafny.generated.JSON_Serializer as JSON_Serializer
import standard_library.internaldafny.generated.JSON_Deserializer_Uint16StrConversion as JSON_Deserializer_Uint16StrConversion
import standard_library.internaldafny.generated.JSON_Deserializer_ByteStrConversion as JSON_Deserializer_ByteStrConversion
import standard_library.internaldafny.generated.JSON_Deserializer as JSON_Deserializer
import standard_library.internaldafny.generated.JSON_ConcreteSyntax_Spec as JSON_ConcreteSyntax_Spec
import standard_library.internaldafny.generated.JSON_ConcreteSyntax_SpecProperties as JSON_ConcreteSyntax_SpecProperties
import standard_library.internaldafny.generated.JSON_ZeroCopy_Serializer as JSON_ZeroCopy_Serializer
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Core as JSON_ZeroCopy_Deserializer_Core
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Strings as JSON_ZeroCopy_Deserializer_Strings
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Numbers as JSON_ZeroCopy_Deserializer_Numbers
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_ObjectParams as JSON_ZeroCopy_Deserializer_ObjectParams
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Objects as JSON_ZeroCopy_Deserializer_Objects
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_ArrayParams as JSON_ZeroCopy_Deserializer_ArrayParams
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Arrays as JSON_ZeroCopy_Deserializer_Arrays
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Constants as JSON_ZeroCopy_Deserializer_Constants
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Values as JSON_ZeroCopy_Deserializer_Values
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_API as JSON_ZeroCopy_Deserializer_API
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer as JSON_ZeroCopy_Deserializer
import standard_library.internaldafny.generated.JSON_ZeroCopy_API as JSON_ZeroCopy_API
import standard_library.internaldafny.generated.JSON_API as JSON_API

# Module: module_

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Test____Main____(noArgsParameter__):
        d_234_success_: bool
        d_234_success_ = True
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUTF8.TestEncodeHappyCase: ")))
        try:
            if True:
                TestUTF8.default__.TestEncodeHappyCase()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_235_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_235_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUTF8.TestEncodeInvalidUnicode: ")))
        try:
            if True:
                TestUTF8.default__.TestEncodeInvalidUnicode()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_236_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_236_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUTF8.TestDecodeHappyCase: ")))
        try:
            if True:
                TestUTF8.default__.TestDecodeHappyCase()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_237_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_237_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUTF8.TestDecodeInvalidUnicode: ")))
        try:
            if True:
                TestUTF8.default__.TestDecodeInvalidUnicode()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_238_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_238_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUTF8.Test1Byte: ")))
        try:
            if True:
                TestUTF8.default__.Test1Byte()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_239_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_239_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUTF8.Test2Bytes: ")))
        try:
            if True:
                TestUTF8.default__.Test2Bytes()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_240_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_240_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUTF8.Test3Bytes: ")))
        try:
            if True:
                TestUTF8.default__.Test3Bytes()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_241_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_241_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUTF8.Test4Bytes: ")))
        try:
            if True:
                TestUTF8.default__.Test4Bytes()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_242_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_242_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestTime.TestNonDecreasing: ")))
        try:
            if True:
                TestTime.default__.TestNonDecreasing()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_243_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_243_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestTime.TestPositiveValues: ")))
        try:
            if True:
                TestTime.default__.TestPositiveValues()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_244_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_244_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestTime.TestGetCurrentTimeStamp: ")))
        try:
            if True:
                TestTime.default__.TestGetCurrentTimeStamp()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_245_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_245_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestComputeSetToOrderedSequenceCharLess.TestSetToOrderedSequenceEmpty: ")))
        try:
            if True:
                TestComputeSetToOrderedSequenceCharLess.default__.TestSetToOrderedSequenceEmpty()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_246_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_246_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestComputeSetToOrderedSequenceCharLess.TestSetToOrderedSequenceOneItem: ")))
        try:
            if True:
                TestComputeSetToOrderedSequenceCharLess.default__.TestSetToOrderedSequenceOneItem()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_247_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_247_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestComputeSetToOrderedSequenceCharLess.TestSetToOrderedSequenceSimple: ")))
        try:
            if True:
                TestComputeSetToOrderedSequenceCharLess.default__.TestSetToOrderedSequenceSimple()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_248_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_248_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestComputeSetToOrderedSequenceCharLess.TestSetToOrderedSequencePrefix: ")))
        try:
            if True:
                TestComputeSetToOrderedSequenceCharLess.default__.TestSetToOrderedSequencePrefix()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_249_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_249_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestComputeSetToOrderedSequenceCharLess.TestSetToOrderedSequenceComplex: ")))
        try:
            if True:
                TestComputeSetToOrderedSequenceCharLess.default__.TestSetToOrderedSequenceComplex()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_250_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_250_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestComputeSetToOrderedSequenceCharLess.TestSetToOrderedSequenceComplexReverse: ")))
        try:
            if True:
                TestComputeSetToOrderedSequenceCharLess.default__.TestSetToOrderedSequenceComplexReverse()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_251_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_251_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestComputeSetToOrderedSequenceCharLess.TestSetSequence: ")))
        try:
            if True:
                TestComputeSetToOrderedSequenceCharLess.default__.TestSetSequence()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_252_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_252_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestComputeSetToOrderedSequenceCharLess.TestSetToOrderedComplexUnicode: ")))
        try:
            if True:
                TestComputeSetToOrderedSequenceCharLess.default__.TestSetToOrderedComplexUnicode()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_253_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_253_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestHexStrings.BasicTests: ")))
        try:
            if True:
                TestHexStrings.default__.BasicTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_254_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_254_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("FloatCompareTest.TestOneTwoZeroMatrix: ")))
        try:
            if True:
                FloatCompareTest.default__.TestOneTwoZeroMatrix()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_255_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_255_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("FloatCompareTest.SimpleTests: ")))
        try:
            if True:
                FloatCompareTest.default__.SimpleTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_256_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_256_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("FloatCompareTest.SignTests: ")))
        try:
            if True:
                FloatCompareTest.default__.SignTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_257_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_257_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("FloatCompareTest.ExponentTests: ")))
        try:
            if True:
                FloatCompareTest.default__.ExponentTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_258_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_258_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("FloatCompareTest.ZeroTests: ")))
        try:
            if True:
                FloatCompareTest.default__.ZeroTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_259_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_259_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("FloatCompareTest.ExtremeNumTest: ")))
        try:
            if True:
                FloatCompareTest.default__.ExtremeNumTest()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_260_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_260_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("FloatCompareTest.InvalidTests: ")))
        try:
            if True:
                FloatCompareTest.default__.InvalidTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_261_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_261_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestCallMany.TestBasic: ")))
        try:
            if True:
                TestCallMany.default__.TestBasic()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_262_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_262_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("GetOptTest.TestEmpty: ")))
        try:
            if True:
                GetOptTest.default__.TestEmpty()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_263_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_263_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("GetOptTest.TestShort: ")))
        try:
            if True:
                GetOptTest.default__.TestShort()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_264_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_264_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("GetOptTest.TestLong: ")))
        try:
            if True:
                GetOptTest.default__.TestLong()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_265_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_265_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("GetOptTest.TestRequired: ")))
        try:
            if True:
                GetOptTest.default__.TestRequired()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_266_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_266_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("GetOptTest.TestDeprecated: ")))
        try:
            if True:
                GetOptTest.default__.TestDeprecated()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_267_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_267_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("GetOptTest.TestAlias: ")))
        try:
            if True:
                GetOptTest.default__.TestAlias()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_268_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_268_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("GetOptTest.TestPositionalFail: ")))
        try:
            if True:
                GetOptTest.default__.TestPositionalFail()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_269_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_269_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("GetOptTest.TestPositional: ")))
        try:
            if True:
                GetOptTest.default__.TestPositional()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_270_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_270_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("GetOptTest.TestHelp: ")))
        try:
            if True:
                GetOptTest.default__.TestHelp()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_271_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_271_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("GetOptTest.TestHelpFail: ")))
        try:
            if True:
                GetOptTest.default__.TestHelpFail()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_272_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_272_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("GetOptTest.TestNested: ")))
        try:
            if True:
                GetOptTest.default__.TestNested()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_273_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_273_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("GetOptTest.TestDefault: ")))
        try:
            if True:
                GetOptTest.default__.TestDefault()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_274_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_274_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("GetOptTest.TestDdbec: ")))
        try:
            if True:
                GetOptTest.default__.TestDdbec()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_275_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_275_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUUID.TestFromBytesSuccess: ")))
        try:
            if True:
                TestUUID.default__.TestFromBytesSuccess()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_276_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_276_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUUID.TestFromBytesFailure: ")))
        try:
            if True:
                TestUUID.default__.TestFromBytesFailure()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_277_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_277_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUUID.TestToBytesSuccess: ")))
        try:
            if True:
                TestUUID.default__.TestToBytesSuccess()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_278_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_278_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUUID.TestToBytesFailure: ")))
        try:
            if True:
                TestUUID.default__.TestToBytesFailure()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_279_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_279_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUUID.TestRoundTripStringConversion: ")))
        try:
            if True:
                TestUUID.default__.TestRoundTripStringConversion()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_280_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_280_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUUID.TestRoundTripByteConversion: ")))
        try:
            if True:
                TestUUID.default__.TestRoundTripByteConversion()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_281_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_281_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestUUID.TestGenerateAndConversion: ")))
        try:
            if True:
                TestUUID.default__.TestGenerateAndConversion()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_282_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_282_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestComputeSetToOrderedSequenceUInt8Less.TestSetToOrderedSequenceEmpty: ")))
        try:
            if True:
                TestComputeSetToOrderedSequenceUInt8Less.default__.TestSetToOrderedSequenceEmpty()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_283_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_283_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestComputeSetToOrderedSequenceUInt8Less.TestSetToOrderedSequenceOneItem: ")))
        try:
            if True:
                TestComputeSetToOrderedSequenceUInt8Less.default__.TestSetToOrderedSequenceOneItem()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_284_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_284_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestComputeSetToOrderedSequenceUInt8Less.TestSetToOrderedSequenceSimple: ")))
        try:
            if True:
                TestComputeSetToOrderedSequenceUInt8Less.default__.TestSetToOrderedSequenceSimple()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_285_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_285_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestComputeSetToOrderedSequenceUInt8Less.TestSetToOrderedSequencePrefix: ")))
        try:
            if True:
                TestComputeSetToOrderedSequenceUInt8Less.default__.TestSetToOrderedSequencePrefix()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_286_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_286_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestComputeSetToOrderedSequenceUInt8Less.TestSetToOrderedSequenceComplex: ")))
        try:
            if True:
                TestComputeSetToOrderedSequenceUInt8Less.default__.TestSetToOrderedSequenceComplex()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_287_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_287_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestComputeSetToOrderedSequenceUInt8Less.TestSetToOrderedSequenceComplexReverse: ")))
        try:
            if True:
                TestComputeSetToOrderedSequenceUInt8Less.default__.TestSetToOrderedSequenceComplexReverse()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_288_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_288_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestComputeSetToOrderedSequenceUInt8Less.TestSetSequence: ")))
        try:
            if True:
                TestComputeSetToOrderedSequenceUInt8Less.default__.TestSetSequence()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_289_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_289_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestComputeSetToOrderedSequenceUInt8Less.TestSetToOrderedSequenceManyItems: ")))
        try:
            if True:
                TestComputeSetToOrderedSequenceUInt8Less.default__.TestSetToOrderedSequenceManyItems()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_290_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_290_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_234_success_ = False
        if not(d_234_success_):
            raise _dafny.HaltException("<stdin>(1,0): " + _dafny.string_of(_dafny.Seq("Test failures occurred: see above.\n")))

