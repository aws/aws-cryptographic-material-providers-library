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

# Module: CreateAwsKmsMrkMultiKeyrings

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def CreateAllAwsKmsMrkMultiKeyring(input):
        allAwsKmsMrkMult: _dafny.Seq = _dafny.Seq({})
        allAwsKmsMrkMult = _dafny.Seq([])
        hi15_ = len(TestVectorConstants.default__.AllAwsKMSKeys)
        for d_1316_i_ in range(0, hi15_):
            let_tmp_rhs16_ = (TestVectorConstants.default__.AllAwsKMSKeys)[d_1316_i_]
            d_1317_kmsKeyId_ = let_tmp_rhs16_[0]
            d_1318___v0_ = let_tmp_rhs16_[1]
            d_1319_keyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
            out278_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
            out278_ = default__.CreateAwsKmsMrkMultiKeyring(Wrappers.Option_Some(d_1317_kmsKeyId_), Wrappers.Option_None())
            d_1319_keyring_ = out278_
            allAwsKmsMrkMult = (allAwsKmsMrkMult) + (_dafny.Seq([d_1319_keyring_]))
        return allAwsKmsMrkMult

    @staticmethod
    def CreateAwsKmsMrkMultiKeyring(kmsKeyId, kmsKeyIds):
        keyring: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring = None
        _dafny.print(_dafny.string_of(_dafny.Seq("\n CreateAwsKmsMrkMultiKeyring: ")))
        _dafny.print(_dafny.string_of(kmsKeyId))
        _dafny.print(_dafny.string_of(_dafny.Seq(" ")))
        _dafny.print(_dafny.string_of(kmsKeyIds))
        d_1320_mpl_: software_amazon_cryptography_materialproviders_internaldafny_types.IAwsCryptographicMaterialProvidersClient
        d_1321_valueOrError0_: Wrappers.Result = None
        out279_: Wrappers.Result
        out279_ = software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedMaterialProviders(software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedDefaultMaterialProvidersConfig())
        d_1321_valueOrError0_ = out279_
        if not(not((d_1321_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CreateKeyrings/CreateAwsKmsMrkMultiKeyrings.dfy(53,12): " + _dafny.string_of(d_1321_valueOrError0_))
        d_1320_mpl_ = (d_1321_valueOrError0_).Extract()
        d_1322_valueOrError1_: Wrappers.Result = None
        out280_: Wrappers.Result
        out280_ = (d_1320_mpl_).CreateAwsKmsMrkMultiKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsMrkMultiKeyringInput_CreateAwsKmsMrkMultiKeyringInput(kmsKeyId, kmsKeyIds, Wrappers.Option_None(), Wrappers.Option_None()))
        d_1322_valueOrError1_ = out280_
        if not(not((d_1322_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CreateKeyrings/CreateAwsKmsMrkMultiKeyrings.dfy(55,12): " + _dafny.string_of(d_1322_valueOrError1_))
        keyring = (d_1322_valueOrError1_).Extract()
        return keyring

