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
import StandardLibrary_String
import StandardLibrary
import UTF8
import software_amazon_cryptography_primitives_internaldafny_types
import ExternRandom
import Random
import AESEncryption
import ExternDigest
import Digest
import HMAC
import WrappedHMAC
import HKDF
import WrappedHKDF
import Signature
import KdfCtr
import RSAEncryption
import AwsCryptographyPrimitivesOperations
import Relations
import Seq_MergeSort
import Math
import Seq
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
import UUID
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
import software_amazon_cryptography_primitives_internaldafny
import Aws_Cryptography
import Aws
import TestSignature
import TestAwsCryptographyPrimitivesHKDF
import TestAwsCryptographyPrimitivesGenerateRandomBytes
import ConstantTime
import ConstantTimeTest
import TestHKDF__Rfc5869TestVectors
import TestKDF
import TestKDFK__TestVectors
import TestAwsCryptographyPrimitivesRSA
import TestAwsCryptographyPrimitivesAES
import TestAwsCryptographyPrimitivesHMAC
import TestAwsCryptographyPrimitivesDigest
import TestAwsCryptographyPrimitivesHMacDigest
import AesKdfCtr
import TestAwsCryptographyPrimitivesAesKdfCtr
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

