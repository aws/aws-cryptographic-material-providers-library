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

# Module: CreateAwsKmsKeyrings

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def CreateAllAwsKmsKeyring(input):
        allAwsKms: _dafny.Seq = _dafny.Seq({})
        allAwsKms = _dafny.Seq([])
        hi12_ = len(TestVectorConstants.default__.AllAwsKMSKeys)
        for d_1287_i_ in range(0, hi12_):
            let_tmp_rhs13_ = (TestVectorConstants.default__.AllAwsKMSKeys)[d_1287_i_]
            d_1288_kmsKeyId_ = let_tmp_rhs13_[0]
            d_1289_region_ = let_tmp_rhs13_[1]
            d_1290_keyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
            out265_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
            out265_ = default__.CreateAwsKmsKeyring(d_1288_kmsKeyId_, d_1289_region_)
            d_1290_keyring_ = out265_
            allAwsKms = (allAwsKms) + (_dafny.Seq([d_1290_keyring_]))
        return allAwsKms

    @staticmethod
    def CreateAwsKmsKeyring(kmsKeyId, region):
        keyring: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring = None
        _dafny.print(_dafny.string_of(_dafny.Seq("\n CreateAwsKmsKeyring: ")))
        _dafny.print(_dafny.string_of(kmsKeyId))
        _dafny.print(_dafny.string_of(_dafny.Seq(" ")))
        _dafny.print(_dafny.string_of(region))
        d_1291_mpl_: software_amazon_cryptography_materialproviders_internaldafny_types.IAwsCryptographicMaterialProvidersClient
        d_1292_valueOrError0_: Wrappers.Result = None
        out266_: Wrappers.Result
        out266_ = software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedMaterialProviders(software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedDefaultMaterialProvidersConfig())
        d_1292_valueOrError0_ = out266_
        if not(not((d_1292_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CreateKeyrings/CreateAwsKmsKeyrings.dfy(53,12): " + _dafny.string_of(d_1292_valueOrError0_))
        d_1291_mpl_ = (d_1292_valueOrError0_).Extract()
        d_1293_clientSupplier_: software_amazon_cryptography_materialproviders_internaldafny_types.IClientSupplier
        d_1294_valueOrError1_: Wrappers.Result = None
        out267_: Wrappers.Result
        out267_ = (d_1291_mpl_).CreateDefaultClientSupplier(software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
        d_1294_valueOrError1_ = out267_
        if not(not((d_1294_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CreateKeyrings/CreateAwsKmsKeyrings.dfy(55,23): " + _dafny.string_of(d_1294_valueOrError1_))
        d_1293_clientSupplier_ = (d_1294_valueOrError1_).Extract()
        d_1295_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_1296_valueOrError2_: Wrappers.Result = None
        out268_: Wrappers.Result
        out268_ = (d_1293_clientSupplier_).GetClient(software_amazon_cryptography_materialproviders_internaldafny_types.GetClientInput_GetClientInput(region))
        d_1296_valueOrError2_ = out268_
        if not(not((d_1296_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CreateKeyrings/CreateAwsKmsKeyrings.dfy(56,18): " + _dafny.string_of(d_1296_valueOrError2_))
        d_1295_kmsClient_ = (d_1296_valueOrError2_).Extract()
        d_1297_valueOrError3_: Wrappers.Result = None
        out269_: Wrappers.Result
        out269_ = (d_1291_mpl_).CreateAwsKmsKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsKeyringInput_CreateAwsKmsKeyringInput(kmsKeyId, d_1295_kmsClient_, Wrappers.Option_None()))
        d_1297_valueOrError3_ = out269_
        if not(not((d_1297_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CreateKeyrings/CreateAwsKmsKeyrings.dfy(58,12): " + _dafny.string_of(d_1297_valueOrError3_))
        keyring = (d_1297_valueOrError3_).Extract()
        return keyring

