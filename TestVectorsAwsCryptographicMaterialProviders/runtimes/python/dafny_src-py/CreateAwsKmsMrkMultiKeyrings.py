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

# Module: CreateAwsKmsMrkMultiKeyrings

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def CreateAllAwsKmsMrkMultiKeyring(input):
        allAwsKmsMrkMult: _dafny.Seq = _dafny.Seq({})
        allAwsKmsMrkMult = _dafny.Seq([])
        hi4_ = len(TestVectorConstants.default__.AllAwsKMSKeys)
        for d_82_i_ in range(0, hi4_):
            let_tmp_rhs3_ = (TestVectorConstants.default__.AllAwsKMSKeys)[d_82_i_]
            d_83_kmsKeyId_ = let_tmp_rhs3_[0]
            d_84___v0_ = let_tmp_rhs3_[1]
            d_85_keyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
            out22_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
            out22_ = default__.CreateAwsKmsMrkMultiKeyring(Wrappers.Option_Some(d_83_kmsKeyId_), Wrappers.Option_None())
            d_85_keyring_ = out22_
            allAwsKmsMrkMult = (allAwsKmsMrkMult) + (_dafny.Seq([d_85_keyring_]))
        return allAwsKmsMrkMult

    @staticmethod
    def CreateAwsKmsMrkMultiKeyring(kmsKeyId, kmsKeyIds):
        keyring: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring = None
        _dafny.print(_dafny.string_of(_dafny.Seq("\n CreateAwsKmsMrkMultiKeyring: ")))
        _dafny.print(_dafny.string_of(kmsKeyId))
        _dafny.print(_dafny.string_of(_dafny.Seq(" ")))
        _dafny.print(_dafny.string_of(kmsKeyIds))
        d_86_mpl_: software_amazon_cryptography_materialproviders_internaldafny_types.IAwsCryptographicMaterialProvidersClient
        d_87_valueOrError0_: Wrappers.Result = None
        out23_: Wrappers.Result
        out23_ = software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedMaterialProviders(software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedDefaultMaterialProvidersConfig())
        d_87_valueOrError0_ = out23_
        if not(not((d_87_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CreateKeyrings/CreateAwsKmsMrkMultiKeyrings.dfy(53,12): " + _dafny.string_of(d_87_valueOrError0_))
        d_86_mpl_ = (d_87_valueOrError0_).Extract()
        d_88_valueOrError1_: Wrappers.Result = None
        out24_: Wrappers.Result
        out24_ = (d_86_mpl_).CreateAwsKmsMrkMultiKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsMrkMultiKeyringInput_CreateAwsKmsMrkMultiKeyringInput(kmsKeyId, kmsKeyIds, Wrappers.Option_None(), Wrappers.Option_None()))
        d_88_valueOrError1_ = out24_
        if not(not((d_88_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CreateKeyrings/CreateAwsKmsMrkMultiKeyrings.dfy(55,12): " + _dafny.string_of(d_88_valueOrError1_))
        keyring = (d_88_valueOrError1_).Extract()
        return keyring

