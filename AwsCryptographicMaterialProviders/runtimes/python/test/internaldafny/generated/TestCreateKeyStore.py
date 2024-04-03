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

# Module: TestCreateKeyStore

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestCreateKeyStore():
        d_0_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_1_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = software_amazon_cryptography_services_kms_internaldafny.default__.KMSClient()
        d_1_valueOrError0_ = out0_
        if not(not((d_1_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeyStore.dfy(19,21): " + _dafny.string_of(d_1_valueOrError0_))
        d_0_kmsClient_ = (d_1_valueOrError0_).Extract()
        d_2_ddbClient_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_3_valueOrError1_: Wrappers.Result = None
        out1_: Wrappers.Result
        out1_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_3_valueOrError1_ = out1_
        if not(not((d_3_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeyStore.dfy(20,21): " + _dafny.string_of(d_3_valueOrError1_))
        d_2_ddbClient_ = (d_3_valueOrError1_).Extract()
        d_4_kmsConfig_: software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration
        d_4_kmsConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KMSConfiguration_kmsKeyArn(Fixtures.default__.keyArn)
        d_5_keyStoreConfig_: software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig
        d_5_keyStoreConfig_ = software_amazon_cryptography_keystore_internaldafny_types.KeyStoreConfig_KeyStoreConfig(Fixtures.default__.branchKeyStoreName, d_4_kmsConfig_, Fixtures.default__.logicalKeyStoreName, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(d_2_ddbClient_), Wrappers.Option_Some(d_0_kmsClient_))
        d_6_keyStore_: software_amazon_cryptography_keystore_internaldafny.KeyStoreClient
        d_7_valueOrError2_: Wrappers.Result = None
        out2_: Wrappers.Result
        out2_ = software_amazon_cryptography_keystore_internaldafny.default__.KeyStore(d_5_keyStoreConfig_)
        d_7_valueOrError2_ = out2_
        if not(not((d_7_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeyStore.dfy(33,20): " + _dafny.string_of(d_7_valueOrError2_))
        d_6_keyStore_ = (d_7_valueOrError2_).Extract()
        d_8_keyStoreArn_: software_amazon_cryptography_keystore_internaldafny_types.CreateKeyStoreOutput
        d_9_valueOrError3_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyStoreOutput.default())()
        out3_: Wrappers.Result
        out3_ = (d_6_keyStore_).CreateKeyStore(software_amazon_cryptography_keystore_internaldafny_types.CreateKeyStoreInput_CreateKeyStoreInput())
        d_9_valueOrError3_ = out3_
        if not(not((d_9_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeyStore.dfy(36,23): " + _dafny.string_of(d_9_valueOrError3_))
        d_8_keyStoreArn_ = (d_9_valueOrError3_).Extract()
        if not((AwsArnParsing.default__.ParseAmazonDynamodbTableName((d_8_keyStoreArn_).tableArn)).is_Success):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeyStore.dfy(38,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(((AwsArnParsing.default__.ParseAmazonDynamodbTableName((d_8_keyStoreArn_).tableArn)).value) == (Fixtures.default__.branchKeyStoreName)):
            raise _dafny.HaltException("dafny/AwsCryptographyKeyStore/test/TestCreateKeyStore.dfy(39,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

