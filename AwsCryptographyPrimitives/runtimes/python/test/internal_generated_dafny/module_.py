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
import software_amazon_cryptography_primitives_internaldafny
import Aws_mCryptography
import Aws
import AesKdfCtr
import TestAwsCryptographyPrimitivesAesKdfCtr
import TestAwsCryptographyPrimitivesHMacDigest
import TestAwsCryptographyPrimitivesDigest
import TestAwsCryptographyPrimitivesHMAC
import TestAwsCryptographyPrimitivesAES
import TestAwsCryptographyPrimitivesRSA
import TestKDF
import TestKDFK__TestVectors
import TestAwsCryptographyPrimitivesHKDF
import TestHKDF__Rfc5869TestVectors
import ConstantTime
import ConstantTimeTest
import TestAwsCryptographyPrimitivesGenerateRandomBytes
import TestSignature
import Relations
import Seq_mMergeSort
import Math
import Seq
import Unicode
import Functions
import Utf8EncodingForm
import Utf16EncodingForm
import UnicodeStrings
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
import DafnyLibraries
import JSON_mUtils_mViews_mCore
import JSON_mUtils_mViews_mWriters
import JSON_mUtils_mViews
import JSON_mUtils_mLexers_mCore
import JSON_mUtils_mLexers_mStrings
import JSON_mUtils_mLexers
import JSON_mUtils_mCursors
import JSON_mUtils_mParsers
import JSON_mUtils_mStr_mCharStrConversion
import JSON_mUtils_mStr_mCharStrEscaping
import JSON_mUtils_mStr
import JSON_mUtils_mSeq
import JSON_mUtils_mVectors
import JSON_mUtils
import JSON_mErrors
import JSON_mValues
import JSON_mSpec
import JSON_mGrammar
import JSON_mSerializer_mByteStrConversion
import JSON_mSerializer
import JSON_mDeserializer_mUint16StrConversion
import JSON_mDeserializer_mByteStrConversion
import JSON_mDeserializer
import JSON_mConcreteSyntax_mSpec
import JSON_mConcreteSyntax_mSpecProperties
import JSON_mConcreteSyntax
import JSON_mZeroCopy_mSerializer
import JSON_mZeroCopy_mDeserializer_mCore
import JSON_mZeroCopy_mDeserializer_mStrings
import JSON_mZeroCopy_mDeserializer_mNumbers
import JSON_mZeroCopy_mDeserializer_mObjectParams
import JSON_mZeroCopy_mDeserializer_mObjects
import JSON_mZeroCopy_mDeserializer_mArrayParams
import JSON_mZeroCopy_mDeserializer_mArrays
import JSON_mZeroCopy_mDeserializer_mConstants
import JSON_mZeroCopy_mDeserializer_mValues
import JSON_mZeroCopy_mDeserializer_mAPI
import JSON_mZeroCopy_mDeserializer
import JSON_mZeroCopy_mAPI
import JSON_mZeroCopy
import JSON_mAPI
import JSON

# assert "module_" == __name__
module_ = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Test____Main____(noArgsParameter__):
        d_151_success_: bool
        d_151_success_ = True
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsCryptographyPrimitivesAesKdfCtr.AesKdfCtrTests: ")))
        try:
            if True:
                TestAwsCryptographyPrimitivesAesKdfCtr.default__.AesKdfCtrTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_152_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_152_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_151_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsCryptographyPrimitivesHMacDigest.DigestTests: ")))
        try:
            if True:
                TestAwsCryptographyPrimitivesHMacDigest.default__.DigestTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_153_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_153_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_151_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsCryptographyPrimitivesDigest.DigestTests: ")))
        try:
            if True:
                TestAwsCryptographyPrimitivesDigest.default__.DigestTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_154_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_154_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_151_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsCryptographyPrimitivesHMAC.HMACTests: ")))
        try:
            if True:
                TestAwsCryptographyPrimitivesHMAC.default__.HMACTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_155_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_155_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_151_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsCryptographyPrimitivesAES.AESDecryptTests: ")))
        try:
            if True:
                TestAwsCryptographyPrimitivesAES.default__.AESDecryptTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_156_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_156_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_151_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsCryptographyPrimitivesAES.AESEncryptTests: ")))
        try:
            if True:
                TestAwsCryptographyPrimitivesAES.default__.AESEncryptTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_157_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_157_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_151_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsCryptographyPrimitivesRSA.RSAEncryptTests: ")))
        try:
            if True:
                TestAwsCryptographyPrimitivesRSA.default__.RSAEncryptTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_158_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_158_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_151_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsCryptographyPrimitivesRSA.GetRSAKeyModulusLength: ")))
        try:
            if True:
                TestAwsCryptographyPrimitivesRSA.default__.GetRSAKeyModulusLength()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_159_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_159_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_151_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsCryptographyPrimitivesRSA.TestingPemParsingInRSAEncryptionForRSAKeyPairStoredInPEM: ")))
        try:
            if True:
                TestAwsCryptographyPrimitivesRSA.default__.TestingPemParsingInRSAEncryptionForRSAKeyPairStoredInPEM()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_160_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_160_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_151_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsCryptographyPrimitivesRSA.TestingPemParsingInRSAEncryptionForOnlyRSAPrivateKeyStoredInPEM: ")))
        try:
            if True:
                TestAwsCryptographyPrimitivesRSA.default__.TestingPemParsingInRSAEncryptionForOnlyRSAPrivateKeyStoredInPEM()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_161_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_161_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_151_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestKDFK_TestVectors.ExpectInternalTestVectors: ")))
        try:
            if True:
                TestKDFK__TestVectors.default__.ExpectInternalTestVectors()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_162_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_162_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_151_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsCryptographyPrimitivesHKDF.TestCase1: ")))
        try:
            if True:
                TestAwsCryptographyPrimitivesHKDF.default__.TestCase1()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_163_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_163_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_151_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestHKDF_Rfc5869TestVectors.ExpectRFCTestVectors: ")))
        try:
            if True:
                TestHKDF__Rfc5869TestVectors.default__.ExpectRFCTestVectors()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_164_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_164_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_151_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("ConstantTimeTest.ConstantTimeTest: ")))
        try:
            if True:
                ConstantTimeTest.default__.ConstantTimeTest()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_165_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_165_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_151_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestAwsCryptographyPrimitivesGenerateRandomBytes.BasicGenerateRandomBytes: ")))
        try:
            if True:
                TestAwsCryptographyPrimitivesGenerateRandomBytes.default__.BasicGenerateRandomBytes()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_166_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_166_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_151_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestSignature.YCompression384: ")))
        try:
            if True:
                TestSignature.default__.YCompression384()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_167_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_167_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_151_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestSignature.YCompression256: ")))
        try:
            if True:
                TestSignature.default__.YCompression256()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_168_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_168_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_151_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestSignature.VerifyMessage384: ")))
        try:
            if True:
                TestSignature.default__.VerifyMessage384()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_169_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_169_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_151_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestSignature.VerifyMessage256: ")))
        try:
            if True:
                TestSignature.default__.VerifyMessage256()
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

