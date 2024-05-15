import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_ as module_
import _dafny as _dafny
import System_ as System_
import standard_library.internaldafny.generated.Wrappers as Wrappers
import standard_library.internaldafny.generated.BoundedInts as BoundedInts
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import standard_library.internaldafny.generated.UTF8 as UTF8
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes as AwsCryptographyPrimitivesTypes
import aws_cryptography_primitives.internaldafny.generated.ExternRandom as ExternRandom
import aws_cryptography_primitives.internaldafny.generated.Random as Random
import aws_cryptography_primitives.internaldafny.generated.AESEncryption as AESEncryption
import aws_cryptography_primitives.internaldafny.generated.ExternDigest as ExternDigest
import aws_cryptography_primitives.internaldafny.generated.Digest as Digest
import aws_cryptography_primitives.internaldafny.generated.HMAC as HMAC
import aws_cryptography_primitives.internaldafny.generated.WrappedHMAC as WrappedHMAC
import aws_cryptography_primitives.internaldafny.generated.HKDF as HKDF
import aws_cryptography_primitives.internaldafny.generated.WrappedHKDF as WrappedHKDF
import aws_cryptography_primitives.internaldafny.generated.Signature as Signature
import aws_cryptography_primitives.internaldafny.generated.KdfCtr as KdfCtr
import aws_cryptography_primitives.internaldafny.generated.RSAEncryption as RSAEncryption
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesOperations as AwsCryptographyPrimitivesOperations
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
import standard_library.internaldafny.generated.Relations as Relations
import standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import standard_library.internaldafny.generated.Math as Math
import standard_library.internaldafny.generated.Seq as Seq
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
import standard_library.internaldafny.generated.UUID as UUID
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
import aws_cryptography_primitives.internaldafny.generated.Aws_Cryptography_Primitives as Aws_Cryptography_Primitives
import aws_cryptography_primitives.internaldafny.generated.Aws_Cryptography as Aws_Cryptography
import aws_cryptography_primitives.internaldafny.generated.Aws as Aws
import TestSignature as TestSignature
import TestAwsCryptographyPrimitivesHKDF as TestAwsCryptographyPrimitivesHKDF
import TestAwsCryptographyPrimitivesGenerateRandomBytes as TestAwsCryptographyPrimitivesGenerateRandomBytes
import ConstantTime as ConstantTime
import ConstantTimeTest as ConstantTimeTest
import TestHKDF__Rfc5869TestVectors as TestHKDF__Rfc5869TestVectors
import TestKDF as TestKDF
import TestKDFK__TestVectors as TestKDFK__TestVectors
import TestAwsCryptographyPrimitivesRSA as TestAwsCryptographyPrimitivesRSA
import TestAwsCryptographyPrimitivesAES as TestAwsCryptographyPrimitivesAES
import TestAwsCryptographyPrimitivesHMAC as TestAwsCryptographyPrimitivesHMAC
import TestAwsCryptographyPrimitivesDigest as TestAwsCryptographyPrimitivesDigest
import TestAwsCryptographyPrimitivesHMacDigest as TestAwsCryptographyPrimitivesHMacDigest
import TestAwsCryptographyPrimitivesAesKdfCtr as TestAwsCryptographyPrimitivesAesKdfCtr
import standard_library.internaldafny.generated.JSON_Utils_Views_Core as JSON_Utils_Views_Core
import standard_library.internaldafny.generated.JSON_Utils_Views_Writers as JSON_Utils_Views_Writers
import standard_library.internaldafny.generated.JSON_Utils_Views as JSON_Utils_Views
import standard_library.internaldafny.generated.JSON_Utils_Lexers_Core as JSON_Utils_Lexers_Core
import standard_library.internaldafny.generated.JSON_Utils_Lexers_Strings as JSON_Utils_Lexers_Strings
import standard_library.internaldafny.generated.JSON_Utils_Lexers as JSON_Utils_Lexers
import standard_library.internaldafny.generated.JSON_Utils_Cursors as JSON_Utils_Cursors
import standard_library.internaldafny.generated.JSON_Utils_Parsers as JSON_Utils_Parsers
import standard_library.internaldafny.generated.JSON_Utils_Str_CharStrConversion as JSON_Utils_Str_CharStrConversion
import standard_library.internaldafny.generated.JSON_Utils_Str_CharStrEscaping as JSON_Utils_Str_CharStrEscaping
import standard_library.internaldafny.generated.JSON_Utils_Str as JSON_Utils_Str
import standard_library.internaldafny.generated.JSON_Utils_Seq as JSON_Utils_Seq
import standard_library.internaldafny.generated.JSON_Utils_Vectors as JSON_Utils_Vectors
import standard_library.internaldafny.generated.JSON_Utils as JSON_Utils
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
import standard_library.internaldafny.generated.JSON_ConcreteSyntax as JSON_ConcreteSyntax
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
import standard_library.internaldafny.generated.JSON_ZeroCopy as JSON_ZeroCopy
import standard_library.internaldafny.generated.JSON_API as JSON_API
import standard_library.internaldafny.generated.JSON as JSON

# Module: module_

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Test____Main____(noArgsParameter__):
        d_151_success_: bool
        d_151_success_ = True
        _dafny.print(_dafny.string_of(_dafny.Seq("TestSignature.YCompression384: ")))
        try:
            if True:
                TestSignature.default__.YCompression384()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_152_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_152_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_151_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestSignature.YCompression256: ")))
        try:
            if True:
                TestSignature.default__.YCompression256()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_153_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_153_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_151_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestSignature.VerifyMessage384: ")))
        try:
            if True:
                TestSignature.default__.VerifyMessage384()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_154_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_154_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_151_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestSignature.VerifyMessage256: ")))
        try:
            if True:
                TestSignature.default__.VerifyMessage256()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_155_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_155_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_151_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsCryptographyPrimitivesHKDF.TestCase1: ")))
        try:
            if True:
                TestAwsCryptographyPrimitivesHKDF.default__.TestCase1()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_156_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_156_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_151_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsCryptographyPrimitivesGenerateRandomBytes.BasicGenerateRandomBytes: ")))
        try:
            if True:
                TestAwsCryptographyPrimitivesGenerateRandomBytes.default__.BasicGenerateRandomBytes()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_157_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_157_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_151_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("ConstantTimeTest.ConstantTimeTest: ")))
        try:
            if True:
                ConstantTimeTest.default__.ConstantTimeTest()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_158_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_158_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_151_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestHKDF_Rfc5869TestVectors.ExpectRFCTestVectors: ")))
        try:
            if True:
                TestHKDF__Rfc5869TestVectors.default__.ExpectRFCTestVectors()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_159_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_159_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_151_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestKDFK_TestVectors.ExpectInternalTestVectors: ")))
        try:
            if True:
                TestKDFK__TestVectors.default__.ExpectInternalTestVectors()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_160_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_160_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_151_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsCryptographyPrimitivesRSA.RSAEncryptTests: ")))
        try:
            if True:
                TestAwsCryptographyPrimitivesRSA.default__.RSAEncryptTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_161_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_161_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_151_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsCryptographyPrimitivesRSA.GetRSAKeyModulusLength: ")))
        try:
            if True:
                TestAwsCryptographyPrimitivesRSA.default__.GetRSAKeyModulusLength()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_162_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_162_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_151_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsCryptographyPrimitivesRSA.TestingPemParsingInRSAEncryptionForRSAKeyPairStoredInPEM: ")))
        try:
            if True:
                TestAwsCryptographyPrimitivesRSA.default__.TestingPemParsingInRSAEncryptionForRSAKeyPairStoredInPEM()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_163_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_163_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_151_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsCryptographyPrimitivesRSA.TestingPemParsingInRSAEncryptionForOnlyRSAPrivateKeyStoredInPEM: ")))
        try:
            if True:
                TestAwsCryptographyPrimitivesRSA.default__.TestingPemParsingInRSAEncryptionForOnlyRSAPrivateKeyStoredInPEM()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_164_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_164_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_151_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsCryptographyPrimitivesAES.AESDecryptTests: ")))
        try:
            if True:
                TestAwsCryptographyPrimitivesAES.default__.AESDecryptTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_165_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_165_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_151_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsCryptographyPrimitivesAES.AESEncryptTests: ")))
        try:
            if True:
                TestAwsCryptographyPrimitivesAES.default__.AESEncryptTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_166_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_166_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_151_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsCryptographyPrimitivesHMAC.HMACTests: ")))
        try:
            if True:
                TestAwsCryptographyPrimitivesHMAC.default__.HMACTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_167_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_167_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_151_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsCryptographyPrimitivesDigest.DigestTests: ")))
        try:
            if True:
                TestAwsCryptographyPrimitivesDigest.default__.DigestTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_168_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_168_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_151_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsCryptographyPrimitivesHMacDigest.DigestTests: ")))
        try:
            if True:
                TestAwsCryptographyPrimitivesHMacDigest.default__.DigestTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_169_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_169_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_151_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsCryptographyPrimitivesAesKdfCtr.AesKdfCtrTests: ")))
        try:
            if True:
                TestAwsCryptographyPrimitivesAesKdfCtr.default__.AesKdfCtrTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_170_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_170_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_151_success_ = False
        if not(d_151_success_):
            raise _dafny.HaltException("<stdin>(1,0): " + _dafny.string_of(_dafny.Seq("Test failures occurred: see above.\n")))

