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

# Module: TestVectorConstants

class default__:
    def  __init__(self):
        pass

    @_dafny.classproperty
    def AllEncryptDecryptKeyrings(instance):
        return _dafny.Seq([EncryptDecryptKeyrings_AwsKmsKeyring(), EncryptDecryptKeyrings_AwsKmsMultiKeyring(), EncryptDecryptKeyrings_AwsKmsMrkKeyring(), EncryptDecryptKeyrings_AwsKmsMrkMultiKeyring(), EncryptDecryptKeyrings_RawAesKeyring(), EncryptDecryptKeyrings_RawRsaKeyring()])
    @_dafny.classproperty
    def AllESDKAlgorithmSuiteIds(instance):
        return _dafny.Seq([software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__NO__KDF(), software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__NO__KDF(), software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF(), software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256(), software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256(), software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256(), software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256(), software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384(), software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384(), software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY(), software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384()])
    @_dafny.classproperty
    def AllDBEAlgorithmSuiteIds(instance):
        return _dafny.Seq([software_amazon_cryptography_materialproviders_internaldafny_types.DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384(), software_amazon_cryptography_materialproviders_internaldafny_types.DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384()])
    @_dafny.classproperty
    def AllAlgorithmSuiteIds(instance):
        return _dafny.Seq([software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__NO__KDF()), software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__NO__KDF()), software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF()), software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256()), software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256()), software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256()), software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256()), software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384()), software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384()), software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY()), software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384()), software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_DBE(software_amazon_cryptography_materialproviders_internaldafny_types.DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384()), software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_DBE(software_amazon_cryptography_materialproviders_internaldafny_types.DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384())])
    @_dafny.classproperty
    def AllAwsKMSKeys(instance):
        return _dafny.Seq([(_dafny.Seq("arn:aws:kms:us-west-2:658956600833:key/b3537ef1-d8dc-4780-9f5a-55776cbb2f7f"), _dafny.Seq("us-west-2"))])

class EncryptDecryptKeyrings:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [EncryptDecryptKeyrings_AwsKmsKeyring(), EncryptDecryptKeyrings_AwsKmsMultiKeyring(), EncryptDecryptKeyrings_AwsKmsMrkKeyring(), EncryptDecryptKeyrings_AwsKmsMrkMultiKeyring(), EncryptDecryptKeyrings_RawAesKeyring(), EncryptDecryptKeyrings_RawRsaKeyring()]
    @classmethod
    def default(cls, ):
        return lambda: EncryptDecryptKeyrings_AwsKmsKeyring()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AwsKmsKeyring(self) -> bool:
        return isinstance(self, EncryptDecryptKeyrings_AwsKmsKeyring)
    @property
    def is_AwsKmsMultiKeyring(self) -> bool:
        return isinstance(self, EncryptDecryptKeyrings_AwsKmsMultiKeyring)
    @property
    def is_AwsKmsMrkKeyring(self) -> bool:
        return isinstance(self, EncryptDecryptKeyrings_AwsKmsMrkKeyring)
    @property
    def is_AwsKmsMrkMultiKeyring(self) -> bool:
        return isinstance(self, EncryptDecryptKeyrings_AwsKmsMrkMultiKeyring)
    @property
    def is_RawAesKeyring(self) -> bool:
        return isinstance(self, EncryptDecryptKeyrings_RawAesKeyring)
    @property
    def is_RawRsaKeyring(self) -> bool:
        return isinstance(self, EncryptDecryptKeyrings_RawRsaKeyring)

class EncryptDecryptKeyrings_AwsKmsKeyring(EncryptDecryptKeyrings, NamedTuple('AwsKmsKeyring', [])):
    def __dafnystr__(self) -> str:
        return f'TestVectorConstants.EncryptDecryptKeyrings.AwsKmsKeyring'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, EncryptDecryptKeyrings_AwsKmsKeyring)
    def __hash__(self) -> int:
        return super().__hash__()

class EncryptDecryptKeyrings_AwsKmsMultiKeyring(EncryptDecryptKeyrings, NamedTuple('AwsKmsMultiKeyring', [])):
    def __dafnystr__(self) -> str:
        return f'TestVectorConstants.EncryptDecryptKeyrings.AwsKmsMultiKeyring'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, EncryptDecryptKeyrings_AwsKmsMultiKeyring)
    def __hash__(self) -> int:
        return super().__hash__()

class EncryptDecryptKeyrings_AwsKmsMrkKeyring(EncryptDecryptKeyrings, NamedTuple('AwsKmsMrkKeyring', [])):
    def __dafnystr__(self) -> str:
        return f'TestVectorConstants.EncryptDecryptKeyrings.AwsKmsMrkKeyring'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, EncryptDecryptKeyrings_AwsKmsMrkKeyring)
    def __hash__(self) -> int:
        return super().__hash__()

class EncryptDecryptKeyrings_AwsKmsMrkMultiKeyring(EncryptDecryptKeyrings, NamedTuple('AwsKmsMrkMultiKeyring', [])):
    def __dafnystr__(self) -> str:
        return f'TestVectorConstants.EncryptDecryptKeyrings.AwsKmsMrkMultiKeyring'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, EncryptDecryptKeyrings_AwsKmsMrkMultiKeyring)
    def __hash__(self) -> int:
        return super().__hash__()

class EncryptDecryptKeyrings_RawAesKeyring(EncryptDecryptKeyrings, NamedTuple('RawAesKeyring', [])):
    def __dafnystr__(self) -> str:
        return f'TestVectorConstants.EncryptDecryptKeyrings.RawAesKeyring'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, EncryptDecryptKeyrings_RawAesKeyring)
    def __hash__(self) -> int:
        return super().__hash__()

class EncryptDecryptKeyrings_RawRsaKeyring(EncryptDecryptKeyrings, NamedTuple('RawRsaKeyring', [])):
    def __dafnystr__(self) -> str:
        return f'TestVectorConstants.EncryptDecryptKeyrings.RawRsaKeyring'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, EncryptDecryptKeyrings_RawRsaKeyring)
    def __hash__(self) -> int:
        return super().__hash__()

