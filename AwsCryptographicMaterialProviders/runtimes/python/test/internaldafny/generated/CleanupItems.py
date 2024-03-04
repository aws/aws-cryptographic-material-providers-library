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

# Module: CleanupItems

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DeleteVersion(branchKeyIdentifier, branchKeyVersion, ddbClient):
        d_93___v0_: Wrappers.Result
        out38_: Wrappers.Result
        out38_ = (ddbClient).DeleteItem(software_amazon_cryptography_services_dynamodb_internaldafny_types.DeleteItemInput_DeleteItemInput(Fixtures.default__.branchKeyStoreName, _dafny.Map({Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD: software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S(branchKeyIdentifier), Structure.default__.TYPE__FIELD: software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S((Structure.default__.BRANCH__KEY__TYPE__PREFIX) + (branchKeyVersion))}), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None()))
        d_93___v0_ = out38_

    @staticmethod
    def DeleteActive(branchKeyIdentifier, ddbClient):
        d_94___v1_: Wrappers.Result
        out39_: Wrappers.Result
        out39_ = (ddbClient).DeleteItem(software_amazon_cryptography_services_dynamodb_internaldafny_types.DeleteItemInput_DeleteItemInput(Fixtures.default__.branchKeyStoreName, _dafny.Map({Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD: software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S(branchKeyIdentifier), Structure.default__.TYPE__FIELD: software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S(Structure.default__.BRANCH__KEY__ACTIVE__TYPE)}), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None()))
        d_94___v1_ = out39_
        d_95___v2_: Wrappers.Result
        out40_: Wrappers.Result
        out40_ = (ddbClient).DeleteItem(software_amazon_cryptography_services_dynamodb_internaldafny_types.DeleteItemInput_DeleteItemInput(Fixtures.default__.branchKeyStoreName, _dafny.Map({Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD: software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S(branchKeyIdentifier), Structure.default__.TYPE__FIELD: software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S(Structure.default__.BEACON__KEY__TYPE__VALUE)}), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None()))
        d_95___v2_ = out40_

