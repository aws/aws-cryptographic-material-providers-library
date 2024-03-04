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
import software_amazon_cryptography_primitives_internaldafny_types
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
import AesKdfCtr
import Relations
import Seq_MergeSort
import Math
import Seq
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
import UUID
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import GetOpt
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
import software_amazon_cryptography_keystore_internaldafny_types
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
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import Com_Amazonaws
import Com
import software_amazon_cryptography_keystore_internaldafny
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsKmsMrkAreUnique
import Constants
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
import LocalCMC
import software_amazon_cryptography_internaldafny_SynchronizedLocalCMC
import StormTracker
import software_amazon_cryptography_internaldafny_StormTrackingCMC
import AwsKmsHierarchicalKeyring
import AwsKmsRsaKeyring
import RawAESKeyring
import RawRSAKeyring

# Module: CMM

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def RequiredEncryptionContextKeys_q(requiredEncryptionContextKeys, encryptionMaterials):
        def lambda91_(forall_var_12_):
            d_1138_k_: _dafny.Seq = forall_var_12_
            return not ((d_1138_k_) in ((requiredEncryptionContextKeys).UnwrapOr(_dafny.Seq([])))) or ((d_1138_k_) in ((encryptionMaterials).requiredEncryptionContextKeys))

        return _dafny.quantifier(((requiredEncryptionContextKeys).UnwrapOr(_dafny.Seq([]))).UniqueElements, True, lambda91_)

    @staticmethod
    def EncryptionContextComplete(input, decryptionMaterials):
        d_1139_reproducedEncryptionContext_ = ((input).reproducedEncryptionContext).UnwrapOr(_dafny.Map({}))
        def lambda92_(forall_var_13_):
            d_1140_k_: _dafny.Seq = forall_var_13_
            return not ((d_1140_k_) in ((d_1139_reproducedEncryptionContext_).keys)) or (((d_1140_k_) in ((decryptionMaterials).encryptionContext)) and ((((decryptionMaterials).encryptionContext)[d_1140_k_]) == ((d_1139_reproducedEncryptionContext_)[d_1140_k_])))

        return _dafny.quantifier(((d_1139_reproducedEncryptionContext_).keys).Elements, True, lambda92_)

    @staticmethod
    def ReproducedEncryptionContext_q(input):
        d_1141_reproducedEncryptionContext_ = ((input).reproducedEncryptionContext).UnwrapOr(_dafny.Map({}))
        def lambda93_(forall_var_14_):
            d_1142_k_: _dafny.Seq = forall_var_14_
            return not (((d_1142_k_) in ((d_1141_reproducedEncryptionContext_).keys)) and ((d_1142_k_) in ((input).encryptionContext))) or ((((input).encryptionContext)[d_1142_k_]) == ((d_1141_reproducedEncryptionContext_)[d_1142_k_]))

        return _dafny.quantifier(((d_1141_reproducedEncryptionContext_).keys).Elements, True, lambda93_)


class VerifiableInterface:
    pass
