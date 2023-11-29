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

# assert "CMM" == __name__
CMM = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def RequiredEncryptionContextKeys_q(requiredEncryptionContextKeys, encryptionMaterials):
        def lambda92_(forall_var_13_):
            d_1440_k_: _dafny.Seq = forall_var_13_
            return not ((d_1440_k_) in ((requiredEncryptionContextKeys).UnwrapOr(_dafny.Seq([])))) or ((d_1440_k_) in ((encryptionMaterials).requiredEncryptionContextKeys))

        return _dafny.quantifier(((requiredEncryptionContextKeys).UnwrapOr(_dafny.Seq([]))).UniqueElements, True, lambda92_)

    @staticmethod
    def EncryptionContextComplete(input, decryptionMaterials):
        d_1441_reproducedEncryptionContext_ = ((input).reproducedEncryptionContext).UnwrapOr(_dafny.Map({}))
        def lambda93_(forall_var_14_):
            d_1442_k_: _dafny.Seq = forall_var_14_
            return not ((d_1442_k_) in ((d_1441_reproducedEncryptionContext_).keys)) or (((d_1442_k_) in ((decryptionMaterials).encryptionContext)) and ((((decryptionMaterials).encryptionContext)[d_1442_k_]) == ((d_1441_reproducedEncryptionContext_)[d_1442_k_])))

        return _dafny.quantifier(((d_1441_reproducedEncryptionContext_).keys).Elements, True, lambda93_)

    @staticmethod
    def ReproducedEncryptionContext_q(input):
        d_1443_reproducedEncryptionContext_ = ((input).reproducedEncryptionContext).UnwrapOr(_dafny.Map({}))
        def lambda94_(forall_var_15_):
            d_1444_k_: _dafny.Seq = forall_var_15_
            return not (((d_1444_k_) in ((d_1443_reproducedEncryptionContext_).keys)) and ((d_1444_k_) in ((input).encryptionContext))) or ((((input).encryptionContext)[d_1444_k_]) == ((d_1443_reproducedEncryptionContext_)[d_1444_k_]))

        return _dafny.quantifier(((d_1443_reproducedEncryptionContext_).keys).Elements, True, lambda94_)


class VerifiableInterface:
    pass
