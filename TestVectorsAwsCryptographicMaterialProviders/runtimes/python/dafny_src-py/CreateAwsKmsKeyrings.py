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

# Module: CreateAwsKmsKeyrings

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def CreateAllAwsKmsKeyring(input):
        allAwsKms: _dafny.Seq = _dafny.Seq({})
        allAwsKms = _dafny.Seq([])
        hi1_ = len(TestVectorConstants.default__.AllAwsKMSKeys)
        for d_53_i_ in range(0, hi1_):
            let_tmp_rhs0_ = (TestVectorConstants.default__.AllAwsKMSKeys)[d_53_i_]
            d_54_kmsKeyId_ = let_tmp_rhs0_[0]
            d_55_region_ = let_tmp_rhs0_[1]
            d_56_keyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
            out9_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
            out9_ = default__.CreateAwsKmsKeyring(d_54_kmsKeyId_, d_55_region_)
            d_56_keyring_ = out9_
            allAwsKms = (allAwsKms) + (_dafny.Seq([d_56_keyring_]))
        return allAwsKms

    @staticmethod
    def CreateAwsKmsKeyring(kmsKeyId, region):
        keyring: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring = None
        _dafny.print(_dafny.string_of(_dafny.Seq("\n CreateAwsKmsKeyring: ")))
        _dafny.print(_dafny.string_of(kmsKeyId))
        _dafny.print(_dafny.string_of(_dafny.Seq(" ")))
        _dafny.print(_dafny.string_of(region))
        d_57_mpl_: software_amazon_cryptography_materialproviders_internaldafny_types.IAwsCryptographicMaterialProvidersClient
        d_58_valueOrError0_: Wrappers.Result = None
        out10_: Wrappers.Result
        out10_ = software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedMaterialProviders(software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedDefaultMaterialProvidersConfig())
        d_58_valueOrError0_ = out10_
        if not(not((d_58_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CreateKeyrings/CreateAwsKmsKeyrings.dfy(53,12): " + _dafny.string_of(d_58_valueOrError0_))
        d_57_mpl_ = (d_58_valueOrError0_).Extract()
        d_59_clientSupplier_: software_amazon_cryptography_materialproviders_internaldafny_types.IClientSupplier
        d_60_valueOrError1_: Wrappers.Result = None
        out11_: Wrappers.Result
        out11_ = (d_57_mpl_).CreateDefaultClientSupplier(software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
        d_60_valueOrError1_ = out11_
        if not(not((d_60_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CreateKeyrings/CreateAwsKmsKeyrings.dfy(55,23): " + _dafny.string_of(d_60_valueOrError1_))
        d_59_clientSupplier_ = (d_60_valueOrError1_).Extract()
        d_61_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_62_valueOrError2_: Wrappers.Result = None
        out12_: Wrappers.Result
        out12_ = (d_59_clientSupplier_).GetClient(software_amazon_cryptography_materialproviders_internaldafny_types.GetClientInput_GetClientInput(region))
        d_62_valueOrError2_ = out12_
        if not(not((d_62_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CreateKeyrings/CreateAwsKmsKeyrings.dfy(56,18): " + _dafny.string_of(d_62_valueOrError2_))
        d_61_kmsClient_ = (d_62_valueOrError2_).Extract()
        d_63_valueOrError3_: Wrappers.Result = None
        out13_: Wrappers.Result
        out13_ = (d_57_mpl_).CreateAwsKmsKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsKeyringInput_CreateAwsKmsKeyringInput(kmsKeyId, d_61_kmsClient_, Wrappers.Option_None()))
        d_63_valueOrError3_ = out13_
        if not(not((d_63_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CreateKeyrings/CreateAwsKmsKeyrings.dfy(58,12): " + _dafny.string_of(d_63_valueOrError3_))
        keyring = (d_63_valueOrError3_).Extract()
        return keyring

