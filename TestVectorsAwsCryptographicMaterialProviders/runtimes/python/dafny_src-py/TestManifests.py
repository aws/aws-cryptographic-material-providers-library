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
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_dynamodb_internaldafny
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import Base64
import AlgorithmSuites
import Materials
import Keyring
import Relations
import Seq_mMergeSort
import Math
import Seq
import MultiKeyring
import AwsArnParsing
import AwsKmsMrkAreUnique
import Actions
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
import DiscoveryMultiKeyring
import AwsKmsMrkDiscoveryKeyring
import MrkAwareDiscoveryMultiKeyring
import AwsKmsMrkKeyring
import MrkAwareStrictMultiKeyring
import DafnyLibraries
import Time
import LocalCMC
import software_amazon_cryptography_internaldafny_SynchronizedLocalCMC
import SortedSets
import StormTracker
import software_amazon_cryptography_internaldafny_StormTrackingCMC
import UUID
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
import Structure
import KMSKeystoreOperations
import DDBKeystoreOperations
import CreateKeys
import CreateKeyStoreTable
import GetKeys
import AwsCryptographyKeyStoreOperations
import software_amazon_cryptography_keystore_internaldafny
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
import Streams
import Sorting
import HexStrings
import FloatCompare
import ConcurrentCall
import Base64Lemmas
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
        d_677_encryptManifestBv_: _dafny.Seq
        d_678_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out80_: Wrappers.Result
        out80_ = FileIO.default__.ReadBytesFromFile(encryptManifestPath)
        d_678_valueOrError0_ = out80_
        if not(not((d_678_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(28,26): " + _dafny.string_of(d_678_valueOrError0_))
        d_677_encryptManifestBv_ = (d_678_valueOrError0_).Extract()
        d_679_encryptManifestBytes_: _dafny.Seq
        d_679_encryptManifestBytes_ = JSONHelpers.default__.BvToBytes(d_677_encryptManifestBv_)
        d_680_encryptManifestJSON_: JSON_mValues.JSON
        d_681_valueOrError1_: Wrappers.Result = Wrappers.Result.default(JSON_mValues.JSON.default())()
        d_681_valueOrError1_ = JSON_mAPI.default__.Deserialize(d_679_encryptManifestBytes_)
        if not(not((d_681_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(30,28): " + _dafny.string_of(d_681_valueOrError1_))
        d_680_encryptManifestJSON_ = (d_681_valueOrError1_).Extract()
        if not((d_680_encryptManifestJSON_).is_Object):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(31,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_682_keys_: software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny.KeyVectorsClient
        d_683_valueOrError2_: Wrappers.Result = None
        out81_: Wrappers.Result
        out81_ = software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny.default__.KeyVectors(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyVectorsConfig_KeyVectorsConfig(keysManifiestPath))
        d_683_valueOrError2_ = out81_
        if not(not((d_683_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(33,13): " + _dafny.string_of(d_683_valueOrError2_))
        d_682_keys_ = (d_683_valueOrError2_).Extract()
        d_684_jsonTests_: _dafny.Seq
        d_685_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_685_valueOrError3_ = JSONHelpers.default__.GetObject(_dafny.Seq("tests"), (d_680_encryptManifestJSON_).obj)
        if not(not((d_685_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(37,18): " + _dafny.string_of(d_685_valueOrError3_))
        d_684_jsonTests_ = (d_685_valueOrError3_).Extract()
        d_686_encryptVectors_: _dafny.Seq
        d_687_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_687_valueOrError4_ = ParseJsonManifests.default__.BuildEncryptTestVector(d_682_keys_, d_684_jsonTests_)
        if not(not((d_687_valueOrError4_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(38,23): " + _dafny.string_of(d_687_valueOrError4_))
        d_686_encryptVectors_ = (d_687_valueOrError4_).Extract()
        d_688_encryptTests_: _dafny.Seq
        d_689_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out82_: Wrappers.Result
        out82_ = default__.ToEncryptTests(d_682_keys_, d_686_encryptVectors_)
        d_689_valueOrError5_ = out82_
        if not(not((d_689_valueOrError5_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(40,21): " + _dafny.string_of(d_689_valueOrError5_))
        d_688_encryptTests_ = (d_689_valueOrError5_).Extract()
        d_690_decryptTests_: _dafny.Seq
        out83_: _dafny.Seq
        out83_ = default__.TestEncrypts(d_688_encryptTests_, d_682_keys_)
        d_690_decryptTests_ = out83_
        d_691___v0_: _dafny.Seq
        out84_: _dafny.Seq
        out84_ = default__.TestDecrypts(d_690_decryptTests_)
        d_691___v0_ = out84_

    @staticmethod
    def TestEncrypts(tests, keys):
        output: _dafny.Seq = _dafny.Seq({})
        d_692_hasFailure_: bool
        d_692_hasFailure_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("\n=================== Starting Encrypt Tests =================== \n\n")))
        d_693_decryptableTests_: _dafny.Seq
        d_693_decryptableTests_ = _dafny.Seq([])
        hi7_ = len(tests)
        for d_694_i_ in range(0, hi7_):
            d_695_test_: TestVectors.EncryptTest
            d_695_test_ = (tests)[d_694_i_]
            d_696_pass_: bool
            d_697_maybeEncryptionMaterials_: Wrappers.Option
            out85_: bool
            out86_: Wrappers.Option
            out85_, out86_ = TestVectors.default__.TestGetEncryptionMaterials(d_695_test_)
            d_696_pass_ = out85_
            d_697_maybeEncryptionMaterials_ = out86_
            if (d_696_pass_) and (((d_695_test_).vector).is_PositiveEncryptKeyringVector):
                d_693_decryptableTests_ = (d_693_decryptableTests_) + (_dafny.Seq([(d_695_test_, (d_697_maybeEncryptionMaterials_).value)]))
            elif not(d_696_pass_):
                d_692_hasFailure_ = True
        _dafny.print(_dafny.string_of(_dafny.Seq("\n=================== Completed Encrypt Tests =================== \n\n")))
        if not(not(d_692_hasFailure_)):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(79,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_698_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out87_: Wrappers.Result
        out87_ = default__.ToDecryptTests(keys, d_693_decryptableTests_)
        d_698_valueOrError0_ = out87_
        if not(not((d_698_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(80,11): " + _dafny.string_of(d_698_valueOrError0_))
        output = (d_698_valueOrError0_).Extract()
        return output

    @staticmethod
    def TestDecrypts(tests):
        manifest: _dafny.Seq = _dafny.Seq({})
        _dafny.print(_dafny.string_of(_dafny.Seq("\n=================== Starting Decrypt Tests =================== \n\n")))
        d_699_hasFailure_: bool
        d_699_hasFailure_ = False
        hi8_ = len(tests)
        for d_700_i_ in range(0, hi8_):
            d_701_pass_: bool
            out88_: bool
            out88_ = TestVectors.default__.TestDecryptMaterials((tests)[d_700_i_])
            d_701_pass_ = out88_
            if not(d_701_pass_):
                d_699_hasFailure_ = True
        _dafny.print(_dafny.string_of(_dafny.Seq("\n=================== Completed Decrypt Tests =================== \n\n")))
        if not(not(d_699_hasFailure_)):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/TestManifests.dfy(104,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        manifest = default__.ToJSONDecryptManifiest(tests)
        return manifest

    @staticmethod
    def ToEncryptTests(keys, encryptVectors):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_702_encryptTests_: _dafny.Seq
        d_702_encryptTests_ = _dafny.Seq([])
        hi9_ = len(encryptVectors)
        for d_703_i_ in range(0, hi9_):
            d_704_test_: TestVectors.EncryptTest
            d_705_valueOrError0_: Wrappers.Result = None
            out89_: Wrappers.Result
            out89_ = TestVectors.default__.ToEncryptTest(keys, (encryptVectors)[d_703_i_])
            d_705_valueOrError0_ = out89_
            if (d_705_valueOrError0_).IsFailure():
                output = (d_705_valueOrError0_).PropagateFailure()
                return output
            d_704_test_ = (d_705_valueOrError0_).Extract()
            d_702_encryptTests_ = (d_702_encryptTests_) + (_dafny.Seq([d_704_test_]))
        output = Wrappers.Result_Success(d_702_encryptTests_)
        return output
        return output

    @staticmethod
    def ToDecryptTests(keys, tests):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_706_positiveEncryptTests_: _dafny.Seq
        def lambda47_(d_707_r_):
            return (((d_707_r_)[0]).vector).is_PositiveEncryptKeyringVector

        d_706_positiveEncryptTests_ = Seq.default__.Filter(lambda47_, tests)
        d_708_decryptTests_: _dafny.Seq
        d_708_decryptTests_ = _dafny.Seq([])
        hi10_ = len(d_706_positiveEncryptTests_)
        for d_709_i_ in range(0, hi10_):
            d_710_test_: TestVectors.DecryptTest
            d_711_valueOrError0_: Wrappers.Result = None
            out90_: Wrappers.Result
            out90_ = TestVectors.default__.ToDecryptTest(keys, ((d_706_positiveEncryptTests_)[d_709_i_])[0], ((d_706_positiveEncryptTests_)[d_709_i_])[1])
            d_711_valueOrError0_ = out90_
            if (d_711_valueOrError0_).IsFailure():
                output = (d_711_valueOrError0_).PropagateFailure()
                return output
            d_710_test_ = (d_711_valueOrError0_).Extract()
            d_708_decryptTests_ = (d_708_decryptTests_) + (_dafny.Seq([d_710_test_]))
        output = Wrappers.Result_Success(d_708_decryptTests_)
        return output
        return output

    @staticmethod
    def ToJSONDecryptManifiest(tests):
        return _dafny.Seq([])

