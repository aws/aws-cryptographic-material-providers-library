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
import software.amazon.cryptography.services.dynamodb.internaldafny.types
import software.amazon.cryptography.services.kms.internaldafny.types
import software.amazon.cryptography.keystore.internaldafny.types
import Relations
import Seq_MergeSort
import Math
import Seq
import software.amazon.cryptography.primitives.internaldafny.types
import software.amazon.cryptography.materialproviders.internaldafny.types
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

# Module: Fixtures

class default__:
    def  __init__(self):
        pass

    @_dafny.classproperty
    def branchKeyStoreName(instance):
        return _dafny.Seq("KeyStoreDdbTable")
    @_dafny.classproperty
    def logicalKeyStoreName(instance):
        return default__.branchKeyStoreName
    @_dafny.classproperty
    def branchKeyId(instance):
        return _dafny.Seq("75789115-1deb-4fe3-a2ec-be9e885d1945")
    @_dafny.classproperty
    def branchKeyIdActiveVersion(instance):
        return _dafny.Seq("fed7ad33-0774-4f97-aa5e-6c766fc8af9f")
    @_dafny.classproperty
    def branchKeyIdWithEC(instance):
        return _dafny.Seq("4bb57643-07c1-419e-92ad-0df0df149d7c")
    @_dafny.classproperty
    def branchKeyIdActiveVersionUtf8Bytes(instance):
        return _dafny.Seq([102, 101, 100, 55, 97, 100, 51, 51, 45, 48, 55, 55, 52, 45, 52, 102, 57, 55, 45, 97, 97, 53, 101, 45, 54, 99, 55, 54, 54, 102, 99, 56, 97, 102, 57, 102])
    @_dafny.classproperty
    def keyArn(instance):
        return _dafny.Seq("arn:aws:kms:us-west-2:370957321024:key/9d989aa2-2f9c-438c-a745-cc57d3ad0126")
    @_dafny.classproperty
    def mkrKeyArn(instance):
        return _dafny.Seq("arn:aws:kms:us-west-2:370957321024:key/mrk-63d386cb70614ea59b32ad65c9315297")
    @_dafny.classproperty
    def keyId(instance):
        return _dafny.Seq("9d989aa2-2f9c-438c-a745-cc57d3ad0126")
