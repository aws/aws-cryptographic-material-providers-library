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
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import AwsArnParsing
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
import Structure
import KMSKeystoreOperations
import DDBKeystoreOperations
import CreateKeys
import CreateKeyStoreTable
import GetKeys
import AwsCryptographyKeyStoreOperations
import software_amazon_cryptography_keystore_internaldafny
import Fixtures
import TestCreateKeyStore
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
import TestConfig
import TestGetKeys
import CleanupItems
import TestCreateKeys
import TestVersionKey
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsKmsMrkAreUnique
import Constants
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
import TestUtils
import TestIntermediateKeyWrapping
import TestDefaultClientProvider
import TestRawAESKeyring
import TestMultiKeyring
import TestRawRSAKeying
import TestAwsKmsRsaKeyring
import TestAwsKmsHierarchicalKeyring

assert "TestAwsKmsEncryptedDataKeyFilter" == __name__
TestAwsKmsEncryptedDataKeyFilter = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestFailsNonKeyResource():
        d_2114_discoveryFilter_: software_amazon_cryptography_materialproviders_internaldafny_types.DiscoveryFilter
        out570_: software_amazon_cryptography_materialproviders_internaldafny_types.DiscoveryFilter
        out570_ = TestAwsKmsEncryptedDataKeyFilter.default__.GetDiscoveryFilter()
        d_2114_discoveryFilter_ = out570_
        d_2115_edkFilter_: AwsKmsDiscoveryKeyring.AwsKmsEncryptedDataKeyFilter
        nw81_ = AwsKmsDiscoveryKeyring.AwsKmsEncryptedDataKeyFilter()
        nw81_.ctor__(Wrappers.Option_Some(d_2114_discoveryFilter_))
        d_2115_edkFilter_ = nw81_
        d_2116_badEdk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        out571_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        out571_ = TestAwsKmsEncryptedDataKeyFilter.default__.GetNonKeyEncryptedDataKey()
        d_2116_badEdk_ = out571_
        d_2117_filterResult_: Wrappers.Result
        out572_: Wrappers.Result
        out572_ = Actions.default__.FilterWithResult(d_2115_edkFilter_, _dafny.Seq([d_2116_badEdk_]))
        d_2117_filterResult_ = out572_
        if not((d_2117_filterResult_).is_Failure):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsDiscoveryKeryring/TestAwsKmsEncryptedDataKeyFilter.dfy(32,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_2118_test_: software_amazon_cryptography_materialproviders_internaldafny_types.Error
        d_2118_test_ = (d_2117_filterResult_).error
        if not((d_2118_test_).is_AwsCryptographicMaterialProvidersException):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsDiscoveryKeryring/TestAwsKmsEncryptedDataKeyFilter.dfy(34,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((d_2118_test_).message) == (_dafny.Seq("Only AWS KMS Keys supported"))):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsDiscoveryKeryring/TestAwsKmsEncryptedDataKeyFilter.dfy(35,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def TestMatchesKeyringsConfiguration():
        d_2119_matchingEdk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        out573_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        out573_ = TestUtils.default__.GenerateMockEncryptedDataKey(_dafny.Seq("aws-kms"), (TestUtils.default__).SHARED__TEST__KEY__ARN)
        d_2119_matchingEdk_ = out573_
        d_2120_mismatchEdkPartition_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        out574_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        out574_ = TestUtils.default__.GenerateMockEncryptedDataKey(_dafny.Seq("aws-kms"), _dafny.Seq("arn:aws-cn:kms:us-west-2:658956600833:key/b3537ef1-d8dc-4780-9f5a-55776cbb2f7f"))
        d_2120_mismatchEdkPartition_ = out574_
        d_2121_mismatchEdkAccount_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        out575_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        out575_ = TestUtils.default__.GenerateMockEncryptedDataKey(_dafny.Seq("aws-kms"), _dafny.Seq("arn:aws:kms:us-west-2:827585335069:key/b3537ef1-d8dc-4780-9f5a-55776cbb2f7f"))
        d_2121_mismatchEdkAccount_ = out575_
        d_2122_mismatchEdkProviderId_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        out576_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        out576_ = TestUtils.default__.GenerateMockEncryptedDataKey(_dafny.Seq("aws"), (TestUtils.default__).SHARED__TEST__KEY__ARN)
        d_2122_mismatchEdkProviderId_ = out576_
        d_2123_discoveryFilter_: software_amazon_cryptography_materialproviders_internaldafny_types.DiscoveryFilter
        out577_: software_amazon_cryptography_materialproviders_internaldafny_types.DiscoveryFilter
        out577_ = TestAwsKmsEncryptedDataKeyFilter.default__.GetDiscoveryFilter()
        d_2123_discoveryFilter_ = out577_
        d_2124_edkFilter_: AwsKmsDiscoveryKeyring.AwsKmsEncryptedDataKeyFilter
        nw82_ = AwsKmsDiscoveryKeyring.AwsKmsEncryptedDataKeyFilter()
        nw82_.ctor__(Wrappers.Option_Some(d_2123_discoveryFilter_))
        d_2124_edkFilter_ = nw82_
        d_2125_filterResult_: Wrappers.Result
        out578_: Wrappers.Result
        out578_ = Actions.default__.FilterWithResult(d_2124_edkFilter_, _dafny.Seq([d_2119_matchingEdk_, d_2120_mismatchEdkPartition_, d_2121_mismatchEdkAccount_, d_2122_mismatchEdkProviderId_]))
        d_2125_filterResult_ = out578_
        if not((d_2125_filterResult_).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsDiscoveryKeryring/TestAwsKmsEncryptedDataKeyFilter.dfy(65,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len((d_2125_filterResult_).value)) == (1)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsDiscoveryKeryring/TestAwsKmsEncryptedDataKeyFilter.dfy(66,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_2125_filterResult_).value)[0]) == (d_2119_matchingEdk_)):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/Keyrings/AwsKms/AwsKmsDiscoveryKeryring/TestAwsKmsEncryptedDataKeyFilter.dfy(67,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def GetDiscoveryFilter():
        discoveryFilter: software_amazon_cryptography_materialproviders_internaldafny_types.DiscoveryFilter = software_amazon_cryptography_materialproviders_internaldafny_types.DiscoveryFilter_DiscoveryFilter.default()()
        discoveryFilter = software_amazon_cryptography_materialproviders_internaldafny_types.DiscoveryFilter_DiscoveryFilter((TestUtils.default__).ACCOUNT__IDS, (TestUtils.default__).PARTITION)
        return discoveryFilter
        return discoveryFilter

    @staticmethod
    def GetNonKeyEncryptedDataKey():
        edk: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey.default()()
        out579_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        out579_ = TestUtils.default__.GenerateMockEncryptedDataKey(_dafny.Seq("aws-kms"), _dafny.Seq("arn:aws:kms:us-west-2:658956600833:alias/b3537ef1-d8dc-4780-9f5a-55776cbb2f7f"))
        edk = out579_
        return edk

