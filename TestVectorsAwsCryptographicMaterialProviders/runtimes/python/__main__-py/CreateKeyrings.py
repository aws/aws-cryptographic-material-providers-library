import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_MergeSort
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
import StandardLibrary_UInt
import StandardLibrary_String
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
        hi16_ = len(TestVectorConstants.default__.AllEncryptDecryptKeyrings)
        for d_1350_i_ in range(0, hi16_):
            d_1351_keyringType_: TestVectorConstants.EncryptDecryptKeyrings
            d_1351_keyringType_ = (TestVectorConstants.default__.AllEncryptDecryptKeyrings)[d_1350_i_]
            source39_ = d_1351_keyringType_
            if source39_.is_AwsKmsKeyring:
                d_1352_allAwsKms_: _dafny.Seq
                out295_: _dafny.Seq
                out295_ = CreateAwsKmsKeyrings.default__.CreateAllAwsKmsKeyring(d_1351_keyringType_)
                d_1352_allAwsKms_ = out295_
                all = (all) + (d_1352_allAwsKms_)
            elif source39_.is_AwsKmsMultiKeyring:
                d_1353_allAwsKms_: _dafny.Seq
                out296_: _dafny.Seq
                out296_ = CreateAwsKmsMultiKeyrings.default__.CreateAllAwsKmsMultiKeyring(d_1351_keyringType_)
                d_1353_allAwsKms_ = out296_
                all = (all) + (d_1353_allAwsKms_)
            elif source39_.is_AwsKmsMrkKeyring:
                d_1354_allAwsKmsMrk_: _dafny.Seq
                out297_: _dafny.Seq
                out297_ = CreateAwsKmsMrkKeyrings.default__.CreateAllAwsKmsMrkKeyring(d_1351_keyringType_)
                d_1354_allAwsKmsMrk_ = out297_
                all = (all) + (d_1354_allAwsKmsMrk_)
            elif source39_.is_AwsKmsMrkMultiKeyring:
                d_1355_allAwsKmsMrkMult_: _dafny.Seq
                out298_: _dafny.Seq
                out298_ = CreateAwsKmsMrkMultiKeyrings.default__.CreateAllAwsKmsMrkMultiKeyring(d_1351_keyringType_)
                d_1355_allAwsKmsMrkMult_ = out298_
                all = (all) + (d_1355_allAwsKmsMrkMult_)
            elif source39_.is_RawAesKeyring:
                d_1356_allRSA_: _dafny.Seq
                out299_: _dafny.Seq
                out299_ = CreateRawAesKeyrings.default__.CreateAllRawAesKeyring(d_1351_keyringType_)
                d_1356_allRSA_ = out299_
                all = (all) + (d_1356_allRSA_)
            elif True:
                d_1357_allAES_: _dafny.Seq
                out300_: _dafny.Seq
                out300_ = CreateRawRsaKeyrings.default__.CreateAllRawRsaKeyring(d_1351_keyringType_)
                d_1357_allAES_ = out300_
                all = (all) + (d_1357_allAES_)
        return all

