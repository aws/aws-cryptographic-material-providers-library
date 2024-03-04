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
import Relations
import Seq_MergeSort
import Math
import Seq
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import AwsArnParsing
import Actions
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
import Structure
import KMSKeystoreOperations
import DDBKeystoreOperations
import CreateKeys
import CreateKeyStoreTable
import GetKeys
import UUID
import Time
import AwsCryptographyKeyStoreOperations
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import Com_Amazonaws
import Com
import software_amazon_cryptography_keystore_internaldafny
import Base64
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsKmsMrkAreUnique
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
import DiscoveryMultiKeyring
import AwsKmsMrkDiscoveryKeyring
import MrkAwareDiscoveryMultiKeyring
import AwsKmsMrkKeyring
import MrkAwareStrictMultiKeyring
import DafnyLibraries
import LocalCMC
import software_amazon_cryptography_internaldafny_SynchronizedLocalCMC
import SortedSets
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
import AesKdfCtr
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
import StandardLibraryInterop
import Streams
import Sorting
import HexStrings
import GetOpt
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

# Module: TestDefaultClientProvider

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def GetUsWestTwo():
        d_244_mpl_: software_amazon_cryptography_materialproviders_internaldafny_types.IAwsCryptographicMaterialProvidersClient
        d_245_valueOrError0_: Wrappers.Result = None
        out81_: Wrappers.Result
        out81_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_245_valueOrError0_ = out81_
        if not(not((d_245_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestDefaultClientProvider.dfy(18,12): " + _dafny.string_of(d_245_valueOrError0_))
        d_244_mpl_ = (d_245_valueOrError0_).Extract()
        d_246_clientSupplier_: software_amazon_cryptography_materialproviders_internaldafny_types.IClientSupplier
        d_247_valueOrError1_: Wrappers.Result = None
        out82_: Wrappers.Result
        out82_ = (d_244_mpl_).CreateDefaultClientSupplier(software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
        d_247_valueOrError1_ = out82_
        if not(not((d_247_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestDefaultClientProvider.dfy(20,23): " + _dafny.string_of(d_247_valueOrError1_))
        d_246_clientSupplier_ = (d_247_valueOrError1_).Extract()
        d_248_client_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_249_valueOrError2_: Wrappers.Result = None
        out83_: Wrappers.Result
        out83_ = (d_246_clientSupplier_).GetClient(software_amazon_cryptography_materialproviders_internaldafny_types.GetClientInput_GetClientInput(_dafny.Seq("us-west-2")))
        d_249_valueOrError2_ = out83_
        if not(not((d_249_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestDefaultClientProvider.dfy(22,15): " + _dafny.string_of(d_249_valueOrError2_))
        d_248_client_ = (d_249_valueOrError2_).Extract()
        d_250_kmsRequest_: software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyRequest
        d_250_kmsRequest_ = software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyRequest_GenerateDataKeyRequest(TestUtils.default__.SHARED__TEST__KEY__ARN, Wrappers.Option_None(), Wrappers.Option_Some(24), Wrappers.Option_None(), Wrappers.Option_None())
        d_251_kmsReply_: software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyResponse
        d_252_valueOrError3_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyResponse.default())()
        out84_: Wrappers.Result
        out84_ = (d_248_client_).GenerateDataKey(d_250_kmsRequest_)
        d_252_valueOrError3_ = out84_
        if not(not((d_252_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographicMaterialProviders/test/TestDefaultClientProvider.dfy(36,17): " + _dafny.string_of(d_252_valueOrError3_))
        d_251_kmsReply_ = (d_252_valueOrError3_).Extract()

