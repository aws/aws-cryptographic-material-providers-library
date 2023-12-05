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

# Module: CreateAwsKmsMrkKeyrings

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def CreateAllAwsKmsMrkKeyring(input):
        allAwsKmsMrk: _dafny.Seq = _dafny.Seq({})
        allAwsKmsMrk = _dafny.Seq([])
        hi14_ = len(TestVectorConstants.default__.AllAwsKMSKeys)
        for d_1305_i_ in range(0, hi14_):
            let_tmp_rhs15_ = (TestVectorConstants.default__.AllAwsKMSKeys)[d_1305_i_]
            d_1306_kmsKeyId_ = let_tmp_rhs15_[0]
            d_1307_region_ = let_tmp_rhs15_[1]
            d_1308_keyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
            out273_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
            out273_ = default__.CreateAwsKmsMrkKeyring(d_1306_kmsKeyId_, d_1307_region_)
            d_1308_keyring_ = out273_
            allAwsKmsMrk = (allAwsKmsMrk) + (_dafny.Seq([d_1308_keyring_]))
        return allAwsKmsMrk

    @staticmethod
    def CreateAwsKmsMrkKeyring(kmsKeyId, region):
        keyring: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring = None
        _dafny.print(_dafny.string_of(_dafny.Seq("\n CreateAwsKmsMrkKeyring: ")))
        _dafny.print(_dafny.string_of(kmsKeyId))
        _dafny.print(_dafny.string_of(_dafny.Seq(" ")))
        _dafny.print(_dafny.string_of(region))
        d_1309_mpl_: software_amazon_cryptography_materialproviders_internaldafny_types.IAwsCryptographicMaterialProvidersClient
        d_1310_valueOrError0_: Wrappers.Result = None
        out274_: Wrappers.Result
        out274_ = software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedMaterialProviders(software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedDefaultMaterialProvidersConfig())
        d_1310_valueOrError0_ = out274_
        if not(not((d_1310_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CreateKeyrings/CreateAwsKmsMrkKeyrings.dfy(53,12): " + _dafny.string_of(d_1310_valueOrError0_))
        d_1309_mpl_ = (d_1310_valueOrError0_).Extract()
        d_1311_clientSupplier_: software_amazon_cryptography_materialproviders_internaldafny_types.IClientSupplier
        d_1312_valueOrError1_: Wrappers.Result = None
        out275_: Wrappers.Result
        out275_ = (d_1309_mpl_).CreateDefaultClientSupplier(software_amazon_cryptography_materialproviders_internaldafny_types.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
        d_1312_valueOrError1_ = out275_
        if not(not((d_1312_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CreateKeyrings/CreateAwsKmsMrkKeyrings.dfy(55,23): " + _dafny.string_of(d_1312_valueOrError1_))
        d_1311_clientSupplier_ = (d_1312_valueOrError1_).Extract()
        d_1313_kmsClient_: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient
        d_1314_valueOrError2_: Wrappers.Result = None
        out276_: Wrappers.Result
        out276_ = (d_1311_clientSupplier_).GetClient(software_amazon_cryptography_materialproviders_internaldafny_types.GetClientInput_GetClientInput(region))
        d_1314_valueOrError2_ = out276_
        if not(not((d_1314_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CreateKeyrings/CreateAwsKmsMrkKeyrings.dfy(56,18): " + _dafny.string_of(d_1314_valueOrError2_))
        d_1313_kmsClient_ = (d_1314_valueOrError2_).Extract()
        d_1315_valueOrError3_: Wrappers.Result = None
        out277_: Wrappers.Result
        out277_ = (d_1309_mpl_).CreateAwsKmsMrkKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsMrkKeyringInput_CreateAwsKmsMrkKeyringInput(kmsKeyId, d_1313_kmsClient_, Wrappers.Option_None()))
        d_1315_valueOrError3_ = out277_
        if not(not((d_1315_valueOrError3_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CreateKeyrings/CreateAwsKmsMrkKeyrings.dfy(58,12): " + _dafny.string_of(d_1315_valueOrError3_))
        keyring = (d_1315_valueOrError3_).Extract()
        return keyring

