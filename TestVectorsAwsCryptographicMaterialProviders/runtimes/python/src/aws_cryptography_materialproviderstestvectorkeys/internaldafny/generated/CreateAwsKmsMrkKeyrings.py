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

# Module: CreateAwsKmsMrkKeyrings

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def CreateAllAwsKmsMrkKeyring(input):
        allAwsKmsMrk: _dafny.Seq = _dafny.Seq({})
        allAwsKmsMrk = _dafny.Seq([])
        hi3_ = len(TestVectorConstants.default__.AllAwsKMSKeys)
        for d_71_i_ in range(0, hi3_):
            let_tmp_rhs2_ = (TestVectorConstants.default__.AllAwsKMSKeys)[d_71_i_]
            d_72_kmsKeyId_ = let_tmp_rhs2_[0]
            d_73_region_ = let_tmp_rhs2_[1]
            d_74_keyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
            out17_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
            out17_ = default__.CreateAwsKmsMrkKeyring(d_72_kmsKeyId_, d_73_region_)
            d_74_keyring_ = out17_
            allAwsKmsMrk = (allAwsKmsMrk) + (_dafny.Seq([d_74_keyring_]))
        return allAwsKmsMrk

    @staticmethod
    def CreateAwsKmsMrkKeyring(kmsKeyId, region):
        keyring: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring = None
        _dafny.print(_dafny.string_of(_dafny.Seq("\n CreateAwsKmsMrkKeyring: ")))
        _dafny.print(_dafny.string_of(kmsKeyId))
        _dafny.print(_dafny.string_of(_dafny.Seq(" ")))
        _dafny.print(_dafny.string_of(region))
        d_75_mpl_: software_amazon_cryptography_materialproviders_internaldafny_types.IAwsCryptographicMaterialProvidersClient
        d_76_valueOrError0_: Wrappers.Result = None
        out18_: Wrappers.Result
        out18_ = software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedMaterialProviders(software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedDefaultMaterialProvidersConfig())
        d_76_valueOrError0_ = out18_
        if not(not((d_76_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CreateKeyrings/CreateAwsKmsMrkKeyrings.dfy(53,12): " + _dafny.string_of(d_76_valueOrError0_))
        d_75_mpl_ = (d_76_valueOrError0_).Extract()
        d_77_clientSupplier_: software_amazon_cryptography_materialproviders_internaldafny_types.IClientSupplier
        d_78_valueOrError1_: Wrappers.Result = None
        out19_: Wrappers.Result
        out19_ = (d_75_mpl_).CreateDefaultClientSupplier(software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
        d_78_valueOrError1_ = out19_
        if not(not((d_78_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CreateKeyrings/CreateAwsKmsMrkKeyrings.dfy(55,23): " + _dafny.string_of(d_78_valueOrError1_))
        d_77_clientSupplier_ = (d_78_valueOrError1_).Extract()
        d_79_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_80_valueOrError2_: Wrappers.Result = None
        out20_: Wrappers.Result
        out20_ = (d_77_clientSupplier_).GetClient(software_amazon_cryptography_materialproviders_internaldafny_types.GetClientInput_GetClientInput(region))
        d_80_valueOrError2_ = out20_
        if not(not((d_80_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CreateKeyrings/CreateAwsKmsMrkKeyrings.dfy(56,18): " + _dafny.string_of(d_80_valueOrError2_))
        d_79_kmsClient_ = (d_80_valueOrError2_).Extract()
        d_81_valueOrError3_: Wrappers.Result = None
        out21_: Wrappers.Result
        out21_ = (d_75_mpl_).CreateAwsKmsMrkKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsMrkKeyringInput_CreateAwsKmsMrkKeyringInput(kmsKeyId, d_79_kmsClient_, Wrappers.Option_None()))
        d_81_valueOrError3_ = out21_
        if not(not((d_81_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CreateKeyrings/CreateAwsKmsMrkKeyrings.dfy(58,12): " + _dafny.string_of(d_81_valueOrError3_))
        keyring = (d_81_valueOrError3_).Extract()
        return keyring

