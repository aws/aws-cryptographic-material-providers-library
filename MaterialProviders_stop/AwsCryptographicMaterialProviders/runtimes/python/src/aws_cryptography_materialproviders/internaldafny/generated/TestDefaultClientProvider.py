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

assert "TestDefaultClientProvider" == __name__
TestDefaultClientProvider = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def GetUsWestTwo():
        d_1663_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1664_valueOrError0_: Wrappers.Result = None
        out381_: Wrappers.Result
        out381_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1664_valueOrError0_ = out381_
        if not(not((d_1664_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestDefaultClientProvider.dfy(18,12): " + _dafny.string_of(d_1664_valueOrError0_))
        d_1663_mpl_ = (d_1664_valueOrError0_).Extract()
        d_1665_clientSupplier_: software_amazon_cryptography_materialproviders_internaldafny_types.IClientSupplier
        d_1666_valueOrError1_: Wrappers.Result = None
        out382_: Wrappers.Result
        out382_ = (d_1663_mpl_).CreateDefaultClientSupplier(software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
        d_1666_valueOrError1_ = out382_
        if not(not((d_1666_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestDefaultClientProvider.dfy(20,23): " + _dafny.string_of(d_1666_valueOrError1_))
        d_1665_clientSupplier_ = (d_1666_valueOrError1_).Extract()
        d_1667_client_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_1668_valueOrError2_: Wrappers.Result = None
        out383_: Wrappers.Result
        out383_ = (d_1665_clientSupplier_).GetClient(software_amazon_cryptography_materialproviders_internaldafny_types.GetClientInput_GetClientInput(_dafny.Seq("us-west-2")))
        d_1668_valueOrError2_ = out383_
        if not(not((d_1668_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestDefaultClientProvider.dfy(22,15): " + _dafny.string_of(d_1668_valueOrError2_))
        d_1667_client_ = (d_1668_valueOrError2_).Extract()
        d_1669_kmsRequest_: software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyRequest
        d_1669_kmsRequest_ = software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyRequest_GenerateDataKeyRequest((TestUtils.default__).SHARED__TEST__KEY__ARN, Wrappers.Option_None(), Wrappers.Option_Some(24), Wrappers.Option_None(), Wrappers.Option_None())
        d_1670_kmsReply_: software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyResponse
        d_1671_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyResponse.default())()
        out384_: Wrappers.Result
        out384_ = (d_1667_client_).GenerateDataKey(d_1669_kmsRequest_)
        d_1671_valueOrError3_ = out384_
        if not(not((d_1671_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestDefaultClientProvider.dfy(36,17): " + _dafny.string_of(d_1671_valueOrError3_))
        d_1670_kmsReply_ = (d_1671_valueOrError3_).Extract()

