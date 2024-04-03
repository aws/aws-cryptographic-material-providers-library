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

# Module: MplManifestOptions


class ManifestOptions:
    @classmethod
    def default(cls, ):
        return lambda: ManifestOptions_Decrypt(_dafny.Seq(""), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Decrypt(self) -> bool:
        return isinstance(self, ManifestOptions_Decrypt)
    @property
    def is_Encrypt(self) -> bool:
        return isinstance(self, ManifestOptions_Encrypt)
    @property
    def is_EncryptManifest(self) -> bool:
        return isinstance(self, ManifestOptions_EncryptManifest)

class ManifestOptions_Decrypt(ManifestOptions, NamedTuple('Decrypt', [('manifestPath', Any), ('testName', Any)])):
    def __dafnystr__(self) -> str:
        return f'MplManifestOptions.ManifestOptions.Decrypt({_dafny.string_of(self.manifestPath)}, {_dafny.string_of(self.testName)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ManifestOptions_Decrypt) and self.manifestPath == __o.manifestPath and self.testName == __o.testName
    def __hash__(self) -> int:
        return super().__hash__()

class ManifestOptions_Encrypt(ManifestOptions, NamedTuple('Encrypt', [('manifestPath', Any), ('decryptManifestOutput', Any), ('testName', Any)])):
    def __dafnystr__(self) -> str:
        return f'MplManifestOptions.ManifestOptions.Encrypt({_dafny.string_of(self.manifestPath)}, {_dafny.string_of(self.decryptManifestOutput)}, {_dafny.string_of(self.testName)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ManifestOptions_Encrypt) and self.manifestPath == __o.manifestPath and self.decryptManifestOutput == __o.decryptManifestOutput and self.testName == __o.testName
    def __hash__(self) -> int:
        return super().__hash__()

class ManifestOptions_EncryptManifest(ManifestOptions, NamedTuple('EncryptManifest', [('encryptManifestOutput', Any)])):
    def __dafnystr__(self) -> str:
        return f'MplManifestOptions.ManifestOptions.EncryptManifest({_dafny.string_of(self.encryptManifestOutput)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ManifestOptions_EncryptManifest) and self.encryptManifestOutput == __o.encryptManifestOutput
    def __hash__(self) -> int:
        return super().__hash__()

