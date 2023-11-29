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

# Module: CMM

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def RequiredEncryptionContextKeys_q(requiredEncryptionContextKeys, encryptionMaterials):
        def lambda69_(forall_var_8_):
            d_1054_k_: _dafny.Seq = forall_var_8_
            return not ((d_1054_k_) in ((requiredEncryptionContextKeys).UnwrapOr(_dafny.Seq([])))) or ((d_1054_k_) in ((encryptionMaterials).requiredEncryptionContextKeys))

        return _dafny.quantifier(((requiredEncryptionContextKeys).UnwrapOr(_dafny.Seq([]))).UniqueElements, True, lambda69_)

    @staticmethod
    def EncryptionContextComplete(input, decryptionMaterials):
        d_1055_reproducedEncryptionContext_ = ((input).reproducedEncryptionContext).UnwrapOr(_dafny.Map({}))
        def lambda70_(forall_var_9_):
            d_1056_k_: _dafny.Seq = forall_var_9_
            return not ((d_1056_k_) in ((d_1055_reproducedEncryptionContext_).keys)) or (((d_1056_k_) in ((decryptionMaterials).encryptionContext)) and ((((decryptionMaterials).encryptionContext)[d_1056_k_]) == ((d_1055_reproducedEncryptionContext_)[d_1056_k_])))

        return _dafny.quantifier(((d_1055_reproducedEncryptionContext_).keys).Elements, True, lambda70_)

    @staticmethod
    def ReproducedEncryptionContext_q(input):
        d_1057_reproducedEncryptionContext_ = ((input).reproducedEncryptionContext).UnwrapOr(_dafny.Map({}))
        def lambda71_(forall_var_10_):
            d_1058_k_: _dafny.Seq = forall_var_10_
            return not (((d_1058_k_) in ((d_1057_reproducedEncryptionContext_).keys)) and ((d_1058_k_) in ((input).encryptionContext))) or ((((input).encryptionContext)[d_1058_k_]) == ((d_1057_reproducedEncryptionContext_)[d_1058_k_]))

        return _dafny.quantifier(((d_1057_reproducedEncryptionContext_).keys).Elements, True, lambda71_)


class VerifiableInterface:
    pass
