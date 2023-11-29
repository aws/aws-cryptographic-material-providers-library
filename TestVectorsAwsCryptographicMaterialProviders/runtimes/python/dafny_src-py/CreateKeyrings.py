import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import BoundedInts
import StandardLibrary_mUInt
import String
import StandardLibrary
import UTF8
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_dynamodb_internaldafny
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import Base64
import AlgorithmSuites
import Materials
import Keyring
import Relations
import Seq_mMergeSort
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
import Streams
import Sorting
import HexStrings
import FloatCompare
import ConcurrentCall
import Base64Lemmas
import software_amazon_cryptography_materialproviders_internaldafny_wrapped
import TestVectorsUtils
import TestVectorConstants
import KeyringExpectations
import CreateAwsKmsKeyrings
import CreateAwsKmsMultiKeyrings
import CreateAwsKmsMrkKeyrings
import CreateAwsKmsMrkMultiKeyrings
import CreateRawAesKeyrings
import CreateRawRsaKeyrings

# Module: CreateKeyrings

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def CreateAllEncryptDecryptKeyrings():
        all: _dafny.Seq = _dafny.Seq({})
        all = _dafny.Seq([])
        hi5_ = len(TestVectorConstants.default__.AllEncryptDecryptKeyrings)
        for d_116_i_ in range(0, hi5_):
            d_117_keyringType_: TestVectorConstants.EncryptDecryptKeyrings
            d_117_keyringType_ = (TestVectorConstants.default__.AllEncryptDecryptKeyrings)[d_116_i_]
            source2_ = d_117_keyringType_
            if source2_.is_AwsKmsKeyring:
                d_118_allAwsKms_: _dafny.Seq
                out39_: _dafny.Seq
                out39_ = CreateAwsKmsKeyrings.default__.CreateAllAwsKmsKeyring(d_117_keyringType_)
                d_118_allAwsKms_ = out39_
                all = (all) + (d_118_allAwsKms_)
            elif source2_.is_AwsKmsMultiKeyring:
                d_119_allAwsKms_: _dafny.Seq
                out40_: _dafny.Seq
                out40_ = CreateAwsKmsMultiKeyrings.default__.CreateAllAwsKmsMultiKeyring(d_117_keyringType_)
                d_119_allAwsKms_ = out40_
                all = (all) + (d_119_allAwsKms_)
            elif source2_.is_AwsKmsMrkKeyring:
                d_120_allAwsKmsMrk_: _dafny.Seq
                out41_: _dafny.Seq
                out41_ = CreateAwsKmsMrkKeyrings.default__.CreateAllAwsKmsMrkKeyring(d_117_keyringType_)
                d_120_allAwsKmsMrk_ = out41_
                all = (all) + (d_120_allAwsKmsMrk_)
            elif source2_.is_AwsKmsMrkMultiKeyring:
                d_121_allAwsKmsMrkMult_: _dafny.Seq
                out42_: _dafny.Seq
                out42_ = CreateAwsKmsMrkMultiKeyrings.default__.CreateAllAwsKmsMrkMultiKeyring(d_117_keyringType_)
                d_121_allAwsKmsMrkMult_ = out42_
                all = (all) + (d_121_allAwsKmsMrkMult_)
            elif source2_.is_RawAesKeyring:
                d_122_allRSA_: _dafny.Seq
                out43_: _dafny.Seq
                out43_ = CreateRawAesKeyrings.default__.CreateAllRawAesKeyring(d_117_keyringType_)
                d_122_allRSA_ = out43_
                all = (all) + (d_122_allRSA_)
            elif True:
                d_123_allAES_: _dafny.Seq
                out44_: _dafny.Seq
                out44_ = CreateRawRsaKeyrings.default__.CreateAllRawRsaKeyring(d_117_keyringType_)
                d_123_allAES_ = out44_
                all = (all) + (d_123_allAES_)
        return all

