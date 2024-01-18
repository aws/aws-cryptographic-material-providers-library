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
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import Base64
import AlgorithmSuites
import Materials
import Keyring
import Relations
import Seq_MergeSort
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
import Aws_Cryptography
import Aws
import MaterialWrapping
import CanonicalEncryptionContext
import IntermediateKeyWrapping
import EdkWrapping
import AwsKmsKeyring
import StrictMultiKeyring
import AwsKmsDiscoveryKeyring
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import Com_Amazonaws
import Com
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
import Fixtures
import TestCreateKeyStore
import TestConfig
import TestGetKeys
import CleanupItems
import TestCreateKeys
import TestVersionKey
import TestUtils
import TestIntermediateKeyWrapping
import TestDefaultClientProvider
import TestRawAESKeyring
import TestMultiKeyring
import TestRawRSAKeying
import TestAwsKmsRsaKeyring
import TestAwsKmsHierarchicalKeyring

# Module: TestAwsKmsEncryptedDataKeyFilter

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestFailsNonKeyResource():
        d_695_discoveryFilter_: software_amazon_cryptography_materialproviders_internaldafny_types.DiscoveryFilter
        out270_: software_amazon_cryptography_materialproviders_internaldafny_types.DiscoveryFilter
        out270_ = default__.GetDiscoveryFilter()
        d_695_discoveryFilter_ = out270_
        d_696_edkFilter_: AwsKmsDiscoveryKeyring.AwsKmsEncryptedDataKeyFilter
        nw7_ = AwsKmsDiscoveryKeyring.AwsKmsEncryptedDataKeyFilter()
        nw7_.ctor__(Wrappers.Option_Some(d_695_discoveryFilter_))
        d_696_edkFilter_ = nw7_
        d_697_badEdk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        out271_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        out271_ = default__.GetNonKeyEncryptedDataKey()
        d_697_badEdk_ = out271_
        d_698_filterResult_: Wrappers.Result
        out272_: Wrappers.Result
        out272_ = Actions.default__.FilterWithResult(d_696_edkFilter_, _dafny.Seq([d_697_badEdk_]))
        d_698_filterResult_ = out272_
        if not((d_698_filterResult_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsDiscoveryKeryring/TestAwsKmsEncryptedDataKeyFilter.dfy(32,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_699_test_: software_amazon_cryptography_materialproviders_internaldafny_types.Error
        d_699_test_ = (d_698_filterResult_).error
        if not((d_699_test_).is_AwsCryptographicMaterialProvidersException):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsDiscoveryKeryring/TestAwsKmsEncryptedDataKeyFilter.dfy(34,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_699_test_).message) == (_dafny.Seq("Only AWS KMS Keys supported"))):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsDiscoveryKeryring/TestAwsKmsEncryptedDataKeyFilter.dfy(35,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestMatchesKeyringsConfiguration():
        d_700_matchingEdk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        out273_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        out273_ = TestUtils.default__.GenerateMockEncryptedDataKey(_dafny.Seq("aws-kms"), TestUtils.default__.SHARED__TEST__KEY__ARN)
        d_700_matchingEdk_ = out273_
        d_701_mismatchEdkPartition_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        out274_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        out274_ = TestUtils.default__.GenerateMockEncryptedDataKey(_dafny.Seq("aws-kms"), _dafny.Seq("arn:aws-cn:kms:us-west-2:658956600833:key/b3537ef1-d8dc-4780-9f5a-55776cbb2f7f"))
        d_701_mismatchEdkPartition_ = out274_
        d_702_mismatchEdkAccount_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        out275_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        out275_ = TestUtils.default__.GenerateMockEncryptedDataKey(_dafny.Seq("aws-kms"), _dafny.Seq("arn:aws:kms:us-west-2:827585335069:key/b3537ef1-d8dc-4780-9f5a-55776cbb2f7f"))
        d_702_mismatchEdkAccount_ = out275_
        d_703_mismatchEdkProviderId_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        out276_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        out276_ = TestUtils.default__.GenerateMockEncryptedDataKey(_dafny.Seq("aws"), TestUtils.default__.SHARED__TEST__KEY__ARN)
        d_703_mismatchEdkProviderId_ = out276_
        d_704_discoveryFilter_: software_amazon_cryptography_materialproviders_internaldafny_types.DiscoveryFilter
        out277_: software_amazon_cryptography_materialproviders_internaldafny_types.DiscoveryFilter
        out277_ = default__.GetDiscoveryFilter()
        d_704_discoveryFilter_ = out277_
        d_705_edkFilter_: AwsKmsDiscoveryKeyring.AwsKmsEncryptedDataKeyFilter
        nw8_ = AwsKmsDiscoveryKeyring.AwsKmsEncryptedDataKeyFilter()
        nw8_.ctor__(Wrappers.Option_Some(d_704_discoveryFilter_))
        d_705_edkFilter_ = nw8_
        d_706_filterResult_: Wrappers.Result
        out278_: Wrappers.Result
        out278_ = Actions.default__.FilterWithResult(d_705_edkFilter_, _dafny.Seq([d_700_matchingEdk_, d_701_mismatchEdkPartition_, d_702_mismatchEdkAccount_, d_703_mismatchEdkProviderId_]))
        d_706_filterResult_ = out278_
        if not((d_706_filterResult_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsDiscoveryKeryring/TestAwsKmsEncryptedDataKeyFilter.dfy(65,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len((d_706_filterResult_).value)) == (1)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsDiscoveryKeryring/TestAwsKmsEncryptedDataKeyFilter.dfy(66,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_706_filterResult_).value)[0]) == (d_700_matchingEdk_)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsDiscoveryKeryring/TestAwsKmsEncryptedDataKeyFilter.dfy(67,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def GetDiscoveryFilter():
        discoveryFilter: software_amazon_cryptography_materialproviders_internaldafny_types.DiscoveryFilter = software_amazon_cryptography_materialproviders_internaldafny_types.DiscoveryFilter.default()()
        discoveryFilter = software_amazon_cryptography_materialproviders_internaldafny_types.DiscoveryFilter_DiscoveryFilter(TestUtils.default__.ACCOUNT__IDS, TestUtils.default__.PARTITION)
        return discoveryFilter
        return discoveryFilter

    @staticmethod
    def GetNonKeyEncryptedDataKey():
        edk: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey.default()()
        out279_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        out279_ = TestUtils.default__.GenerateMockEncryptedDataKey(_dafny.Seq("aws-kms"), _dafny.Seq("arn:aws:kms:us-west-2:658956600833:alias/b3537ef1-d8dc-4780-9f5a-55776cbb2f7f"))
        edk = out279_
        return edk

