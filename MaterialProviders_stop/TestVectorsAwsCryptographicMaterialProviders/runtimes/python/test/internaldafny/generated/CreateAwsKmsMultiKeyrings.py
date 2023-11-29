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

assert "CreateAwsKmsMultiKeyrings" == __name__
CreateAwsKmsMultiKeyrings = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def CreateAllAwsKmsMultiKeyring(input):
        allAwsKmsMrkMult: _dafny.Seq = _dafny.Seq({})
        allAwsKmsMrkMult = _dafny.Seq([])
        hi13_: int = len((TestVectorConstants.default__).AllAwsKMSKeys)
        for d_1296_i_ in range(0, hi13_):
            let_tmp_rhs14_ = ((TestVectorConstants.default__).AllAwsKMSKeys)[d_1296_i_]
            d_1297_kmsKeyId_ = let_tmp_rhs14_[0]
            d_1298___v0_ = let_tmp_rhs14_[1]
            d_1299_keyring_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
            out270_: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring
            out270_ = CreateAwsKmsMultiKeyrings.default__.CreateAwsKmsMultiKeyring(Wrappers.Option_Some(d_1297_kmsKeyId_), Wrappers.Option_None())
            d_1299_keyring_ = out270_
            allAwsKmsMrkMult = (allAwsKmsMrkMult) + (_dafny.Seq([d_1299_keyring_]))
        return allAwsKmsMrkMult

    @staticmethod
    def CreateAwsKmsMultiKeyring(kmsKeyId, kmsKeyIds):
        keyring: software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring = None
        _dafny.print(_dafny.string_of(_dafny.Seq("\n CreateAwsKmsMultiKeyring: ")))
        _dafny.print(_dafny.string_of(kmsKeyId))
        _dafny.print(_dafny.string_of(_dafny.Seq(" ")))
        _dafny.print(_dafny.string_of(kmsKeyIds))
        d_1300_mpl_: software_amazon_cryptography_materialproviders_internaldafny_types.IAwsCryptographicMaterialProvidersClient
        d_1301_valueOrError0_: Wrappers.Result = None
        out271_: Wrappers.Result
        out271_ = software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedMaterialProviders(software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedDefaultMaterialProvidersConfig())
        d_1301_valueOrError0_ = out271_
        if not(not((d_1301_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CreateKeyrings/CreateAwsKmsMultiKeyrings.dfy(53,12): " + _dafny.string_of(d_1301_valueOrError0_))
        d_1300_mpl_ = (d_1301_valueOrError0_).Extract()
        d_1302_valueOrError1_: Wrappers.Result = None
        out272_: Wrappers.Result
        out272_ = (d_1300_mpl_).CreateAwsKmsMultiKeyring(software_amazon_cryptography_materialproviders_internaldafny_types.CreateAwsKmsMultiKeyringInput_CreateAwsKmsMultiKeyringInput(kmsKeyId, kmsKeyIds, Wrappers.Option_None(), Wrappers.Option_None()))
        d_1302_valueOrError1_ = out272_
        if not(not((d_1302_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("dafny/TestVectorsAwsCryptographicMaterialProviders/src/CreateKeyrings/CreateAwsKmsMultiKeyrings.dfy(55,12): " + _dafny.string_of(d_1302_valueOrError1_))
        keyring = (d_1302_valueOrError1_).Extract()
        return keyring

