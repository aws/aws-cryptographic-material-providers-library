import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_mMergeSort
import Math
import Seq
import BoundedInts
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
import StandardLibrary_mUInt
import String
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
import DafnyLibraries
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsArnParsing
import AwsKmsMrkAreUnique
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
import Constants
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
import MaterialWrapping
import CanonicalEncryptionContext
import IntermediateKeyWrapping
import EdkWrapping
import AwsKmsKeyring
import StrictMultiKeyring
import AwsKmsDiscoveryKeyring
import software_amazon_cryptography_services_kms_internaldafny
import DiscoveryMultiKeyring
import AwsKmsMrkDiscoveryKeyring
import MrkAwareDiscoveryMultiKeyring
import AwsKmsMrkKeyring
import MrkAwareStrictMultiKeyring
import LocalCMC
import software_amazon_cryptography_internaldafny_SynchronizedLocalCMC
import StormTracker
import software_amazon_cryptography_internaldafny_StormTrackingCMC
import AwsKmsHierarchicalKeyring
import AwsKmsRsaKeyring
import RawAESKeyring
import RawRSAKeyring
import CMM
import Defaults
import Commitment
import DefaultCMM
import DefaultClientSupplier
import RequiredEncryptionContextCMM
import AwsCryptographyMaterialProvidersOperations
import software_amazon_cryptography_materialproviders_internaldafny
import software_amazon_cryptography_materialproviders_internaldafny_wrapped
import TestVectorsUtils
import TestVectorConstants
import KeyringExpectations
import CreateAwsKmsKeyrings
import CreateAwsKmsMultiKeyrings
import CreateAwsKmsMrkKeyrings
import CreateAwsKmsMrkMultiKeyrings
import CreateRawAesKeyrings
import CreateRawRsaKeyrings
import CreateKeyrings
import software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types
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
import JSONHelpers
import KeyDescription
import KeyMaterial
import CreateStaticKeyrings
import CreateStaticKeyStores
import KeyringFromKeyDescription
import KeysVectorOperations
import software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny
import TestVectors
import CompleteVectors
import ParseJsonManifests

# Module: TestManifests

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def StartEncrypt(encryptManifestPath, keysManifiestPath):
        d_1911_encryptManifestBv_: _dafny.Seq
        d_1912_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out336_: Wrappers.Result
        out336_ = FileIO.default__.ReadBytesFromFile(encryptManifestPath)
        d_1912_valueOrError0_ = out336_
        if not(not((d_1912_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(28,26): " + _dafny.string_of(d_1912_valueOrError0_))
        d_1911_encryptManifestBv_ = (d_1912_valueOrError0_).Extract()
        d_1913_encryptManifestBytes_: _dafny.Seq
        d_1913_encryptManifestBytes_ = JSONHelpers.default__.BvToBytes(d_1911_encryptManifestBv_)
        d_1914_encryptManifestJSON_: JSON_mValues.JSON
        d_1915_valueOrError1_: Wrappers.Result = Wrappers.Result.default(JSON_mValues.JSON.default())()
        d_1915_valueOrError1_ = JSON_mAPI.default__.Deserialize(d_1913_encryptManifestBytes_)
        if not(not((d_1915_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(30,28): " + _dafny.string_of(d_1915_valueOrError1_))
        d_1914_encryptManifestJSON_ = (d_1915_valueOrError1_).Extract()
        if not((d_1914_encryptManifestJSON_).is_Object):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(31,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1916_keys_: software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny.KeyVectorsClient
        d_1917_valueOrError2_: Wrappers.Result = None
        out337_: Wrappers.Result
        out337_ = software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny.default__.KeyVectors(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyVectorsConfig_KeyVectorsConfig(keysManifiestPath))
        d_1917_valueOrError2_ = out337_
        if not(not((d_1917_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(33,13): " + _dafny.string_of(d_1917_valueOrError2_))
        d_1916_keys_ = (d_1917_valueOrError2_).Extract()
        d_1918_jsonTests_: _dafny.Seq
        d_1919_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1919_valueOrError3_ = JSONHelpers.default__.GetObject(_dafny.Seq("tests"), (d_1914_encryptManifestJSON_).obj)
        if not(not((d_1919_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(37,18): " + _dafny.string_of(d_1919_valueOrError3_))
        d_1918_jsonTests_ = (d_1919_valueOrError3_).Extract()
        d_1920_encryptVectors_: _dafny.Seq
        d_1921_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1921_valueOrError4_ = ParseJsonManifests.default__.BuildEncryptTestVector(d_1916_keys_, d_1918_jsonTests_)
        if not(not((d_1921_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(38,23): " + _dafny.string_of(d_1921_valueOrError4_))
        d_1920_encryptVectors_ = (d_1921_valueOrError4_).Extract()
        d_1922_encryptTests_: _dafny.Seq
        d_1923_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out338_: Wrappers.Result
        out338_ = default__.ToEncryptTests(d_1916_keys_, d_1920_encryptVectors_)
        d_1923_valueOrError5_ = out338_
        if not(not((d_1923_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(40,21): " + _dafny.string_of(d_1923_valueOrError5_))
        d_1922_encryptTests_ = (d_1923_valueOrError5_).Extract()
        d_1924_decryptTests_: _dafny.Seq
        out339_: _dafny.Seq
        out339_ = default__.TestEncrypts(d_1922_encryptTests_, d_1916_keys_)
        d_1924_decryptTests_ = out339_
        d_1925___v0_: _dafny.Seq
        out340_: _dafny.Seq
        out340_ = default__.TestDecrypts(d_1924_decryptTests_)
        d_1925___v0_ = out340_

    @staticmethod
    def TestEncrypts(tests, keys):
        output: _dafny.Seq = _dafny.Seq({})
        d_1926_hasFailure_: bool
        d_1926_hasFailure_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("\n=================== Starting Encrypt Tests =================== \n\n")))
        d_1927_decryptableTests_: _dafny.Seq
        d_1927_decryptableTests_ = _dafny.Seq([])
        hi18_ = len(tests)
        for d_1928_i_ in range(0, hi18_):
            d_1929_test_: TestVectors.EncryptTest
            d_1929_test_ = (tests)[d_1928_i_]
            d_1930_pass_: bool
            d_1931_maybeEncryptionMaterials_: Wrappers.Option
            out341_: bool
            out342_: Wrappers.Option
            out341_, out342_ = TestVectors.default__.TestGetEncryptionMaterials(d_1929_test_)
            d_1930_pass_ = out341_
            d_1931_maybeEncryptionMaterials_ = out342_
            if (d_1930_pass_) and (((d_1929_test_).vector).is_PositiveEncryptKeyringVector):
                d_1927_decryptableTests_ = (d_1927_decryptableTests_) + (_dafny.Seq([(d_1929_test_, (d_1931_maybeEncryptionMaterials_).value)]))
            elif not(d_1930_pass_):
                d_1926_hasFailure_ = True
        _dafny.print(_dafny.string_of(_dafny.Seq("\n=================== Completed Encrypt Tests =================== \n\n")))
        if not(not(d_1926_hasFailure_)):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(79,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_1932_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out343_: Wrappers.Result
        out343_ = default__.ToDecryptTests(keys, d_1927_decryptableTests_)
        d_1932_valueOrError0_ = out343_
        if not(not((d_1932_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(80,11): " + _dafny.string_of(d_1932_valueOrError0_))
        output = (d_1932_valueOrError0_).Extract()
        return output

    @staticmethod
    def TestDecrypts(tests):
        manifest: _dafny.Seq = _dafny.Seq({})
        _dafny.print(_dafny.string_of(_dafny.Seq("\n=================== Starting Decrypt Tests =================== \n\n")))
        d_1933_hasFailure_: bool
        d_1933_hasFailure_ = False
        hi19_ = len(tests)
        for d_1934_i_ in range(0, hi19_):
            d_1935_pass_: bool
            out344_: bool
            out344_ = TestVectors.default__.TestDecryptMaterials((tests)[d_1934_i_])
            d_1935_pass_ = out344_
            if not(d_1935_pass_):
                d_1933_hasFailure_ = True
        _dafny.print(_dafny.string_of(_dafny.Seq("\n=================== Completed Decrypt Tests =================== \n\n")))
        if not(not(d_1933_hasFailure_)):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(104,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        manifest = default__.ToJSONDecryptManifiest(tests)
        return manifest

    @staticmethod
    def ToEncryptTests(keys, encryptVectors):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1936_encryptTests_: _dafny.Seq
        d_1936_encryptTests_ = _dafny.Seq([])
        hi20_ = len(encryptVectors)
        for d_1937_i_ in range(0, hi20_):
            d_1938_test_: TestVectors.EncryptTest
            d_1939_valueOrError0_: Wrappers.Result = None
            out345_: Wrappers.Result
            out345_ = TestVectors.default__.ToEncryptTest(keys, (encryptVectors)[d_1937_i_])
            d_1939_valueOrError0_ = out345_
            if (d_1939_valueOrError0_).IsFailure():
                output = (d_1939_valueOrError0_).PropagateFailure()
                return output
            d_1938_test_ = (d_1939_valueOrError0_).Extract()
            d_1936_encryptTests_ = (d_1936_encryptTests_) + (_dafny.Seq([d_1938_test_]))
        output = Wrappers.Result_Success(d_1936_encryptTests_)
        return output
        return output

    @staticmethod
    def ToDecryptTests(keys, tests):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1940_positiveEncryptTests_: _dafny.Seq
        def lambda129_(d_1941_r_):
            return (((d_1941_r_)[0]).vector).is_PositiveEncryptKeyringVector

        d_1940_positiveEncryptTests_ = Seq.default__.Filter(lambda129_, tests)
        d_1942_decryptTests_: _dafny.Seq
        d_1942_decryptTests_ = _dafny.Seq([])
        hi21_ = len(d_1940_positiveEncryptTests_)
        for d_1943_i_ in range(0, hi21_):
            d_1944_test_: TestVectors.DecryptTest
            d_1945_valueOrError0_: Wrappers.Result = None
            out346_: Wrappers.Result
            out346_ = TestVectors.default__.ToDecryptTest(keys, ((d_1940_positiveEncryptTests_)[d_1943_i_])[0], ((d_1940_positiveEncryptTests_)[d_1943_i_])[1])
            d_1945_valueOrError0_ = out346_
            if (d_1945_valueOrError0_).IsFailure():
                output = (d_1945_valueOrError0_).PropagateFailure()
                return output
            d_1944_test_ = (d_1945_valueOrError0_).Extract()
            d_1942_decryptTests_ = (d_1942_decryptTests_) + (_dafny.Seq([d_1944_test_]))
        output = Wrappers.Result_Success(d_1942_decryptTests_)
        return output
        return output

    @staticmethod
    def ToJSONDecryptManifiest(tests):
        return _dafny.Seq([])

