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
import CreateKeyrings
import software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types
import JSON_mUtils_mViews_mCore
import JSON_mUtils_mViews_mWriters
import JSON_mUtils_mViews
import JSON_mUtils_mLexers_mCore
import JSON_mUtils_mLexers_mStrings
import JSON_mUtils_mLexers
import JSON_mUtils_mCursors
import JSON_mUtils_mParsers
import JSON_mUtils_mStr_mCharStrConversion
import JSON_mUtils_mStr_mCharStrEscaping
import JSON_mUtils_mStr
import JSON_mUtils_mSeq
import JSON_mUtils_mVectors
import JSON_mUtils
import JSON_mErrors
import JSON_mValues
import JSON_mSpec
import JSON_mGrammar
import JSON_mSerializer_mByteStrConversion
import JSON_mSerializer
import JSON_mDeserializer_mUint16StrConversion
import JSON_mDeserializer_mByteStrConversion
import JSON_mDeserializer
import JSON_mConcreteSyntax_mSpec
import JSON_mConcreteSyntax_mSpecProperties
import JSON_mConcreteSyntax
import JSON_mZeroCopy_mSerializer
import JSON_mZeroCopy_mDeserializer_mCore
import JSON_mZeroCopy_mDeserializer_mStrings
import JSON_mZeroCopy_mDeserializer_mNumbers
import JSON_mZeroCopy_mDeserializer_mObjectParams
import JSON_mZeroCopy_mDeserializer_mObjects
import JSON_mZeroCopy_mDeserializer_mArrayParams
import JSON_mZeroCopy_mDeserializer_mArrays
import JSON_mZeroCopy_mDeserializer_mConstants
import JSON_mZeroCopy_mDeserializer_mValues
import JSON_mZeroCopy_mDeserializer_mAPI
import JSON_mZeroCopy_mDeserializer
import JSON_mZeroCopy_mAPI
import JSON_mZeroCopy
import JSON_mAPI
import JSON
import JSONHelpers
import KeyDescription
import KeyMaterial
import CreateStaticKeyrings
import CreateStaticKeyStores
import KeyringFromKeyDescription

# Module: KeysVectorOperations

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def CreateTestVectorKeyringEnsuresPublicly(input, output):
        return True

    @staticmethod
    def CreateTestVectorKeyring(config, input):
        output: Wrappers.Result = None
        d_420_keyDescription_: software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription
        d_420_keyDescription_ = (input).keyDescription
        d_421_keyId_: _dafny.Seq
        d_421_keyId_ = default__.GetKeyId(d_420_keyDescription_)
        d_422_info_: KeyringFromKeyDescription.KeyringInfo
        d_422_info_ = KeyringFromKeyDescription.KeyringInfo_KeyringInfo(d_420_keyDescription_, (Wrappers.Option_Some(((config).keys)[d_421_keyId_]) if (d_421_keyId_) in ((config).keys) else Wrappers.Option_None()))
        d_423_maybeMpl_: Wrappers.Result
        out62_: Wrappers.Result
        out62_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_423_maybeMpl_ = out62_
        d_424_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_425_valueOrError0_: Wrappers.Result = None
        def lambda23_(d_426_e_):
            return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_AwsCryptographyMaterialProviders(d_426_e_)

        d_425_valueOrError0_ = (d_423_maybeMpl_).MapFailure(lambda23_)
        if (d_425_valueOrError0_).IsFailure():
            output = (d_425_valueOrError0_).PropagateFailure()
            return output
        d_424_mpl_ = (d_425_valueOrError0_).Extract()
        out63_: Wrappers.Result
        out63_ = KeyringFromKeyDescription.default__.ToKeyring(d_424_mpl_, d_422_info_)
        output = out63_
        return output

    @staticmethod
    def CreateWappedTestVectorKeyringEnsuresPublicly(input, output):
        return True

    @staticmethod
    def CreateWappedTestVectorKeyring(config, input):
        output: Wrappers.Result = None
        d_427_keyDescription_: software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.KeyDescription
        d_427_keyDescription_ = (input).keyDescription
        d_428_keyId_: _dafny.Seq
        d_428_keyId_ = default__.GetKeyId(d_427_keyDescription_)
        d_429_info_: KeyringFromKeyDescription.KeyringInfo
        d_429_info_ = KeyringFromKeyDescription.KeyringInfo_KeyringInfo(d_427_keyDescription_, (Wrappers.Option_Some(((config).keys)[d_428_keyId_]) if (d_428_keyId_) in ((config).keys) else Wrappers.Option_None()))
        d_430_maybeMpl_: Wrappers.Result
        out64_: Wrappers.Result
        out64_ = software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedMaterialProviders(software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedDefaultMaterialProvidersConfig())
        d_430_maybeMpl_ = out64_
        d_431_wrappedMPL_: software_amazon_cryptography_materialproviders_internaldafny_types.IAwsCryptographicMaterialProvidersClient
        d_432_valueOrError0_: Wrappers.Result = None
        def lambda24_(d_433_e_):
            return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_AwsCryptographyMaterialProviders(d_433_e_)

        d_432_valueOrError0_ = (d_430_maybeMpl_).MapFailure(lambda24_)
        if (d_432_valueOrError0_).IsFailure():
            output = (d_432_valueOrError0_).PropagateFailure()
            return output
        d_431_wrappedMPL_ = (d_432_valueOrError0_).Extract()
        out65_: Wrappers.Result
        out65_ = KeyringFromKeyDescription.default__.ToKeyring(d_431_wrappedMPL_, d_429_info_)
        output = out65_
        return output

    @staticmethod
    def GetKeyDescription(config, input):
        def lambda25_(d_435_e_):
            return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_AwsCryptographyMaterialProviders(software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException((d_435_e_).ToString()))

        d_434_valueOrError0_ = (JSON_mAPI.default__.Deserialize((input).json)).MapFailure(lambda25_)
        if (d_434_valueOrError0_).IsFailure():
            return (d_434_valueOrError0_).PropagateFailure()
        elif True:
            d_436_keyDescriptionJSON_ = (d_434_valueOrError0_).Extract()
            def lambda26_(d_438_e_):
                return software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_AwsCryptographyMaterialProviders(software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(d_438_e_))

            d_437_valueOrError1_ = (KeyDescription.default__.ToKeyDescription(d_436_keyDescriptionJSON_)).MapFailure(lambda26_)
            if (d_437_valueOrError1_).IsFailure():
                return (d_437_valueOrError1_).PropagateFailure()
            elif True:
                d_439_keyDescription_ = (d_437_valueOrError1_).Extract()
                return Wrappers.Result_Success(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.GetKeyDescriptionOutput_GetKeyDescriptionOutput(d_439_keyDescription_))

    @staticmethod
    def SerializeKeyDescription(config, input):
        return Wrappers.Result_Failure(software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types.Error_KeyVectorException(_dafny.Seq("Not Supported")))

    @staticmethod
    def GetKeyId(input):
        source14_ = input
        if source14_.is_Kms:
            d_440___mcc_h0_ = source14_.Kms
            d_441_i_ = d_440___mcc_h0_
            return (d_441_i_).keyId
        elif source14_.is_KmsMrk:
            d_442___mcc_h1_ = source14_.KmsMrk
            d_443_i_ = d_442___mcc_h1_
            return (d_443_i_).keyId
        elif source14_.is_KmsMrkDiscovery:
            d_444___mcc_h2_ = source14_.KmsMrkDiscovery
            d_445_i_ = d_444___mcc_h2_
            return (d_445_i_).keyId
        elif source14_.is_RSA:
            d_446___mcc_h3_ = source14_.RSA
            d_447_i_ = d_446___mcc_h3_
            return (d_447_i_).keyId
        elif source14_.is_AES:
            d_448___mcc_h4_ = source14_.AES
            d_449_i_ = d_448___mcc_h4_
            return (d_449_i_).keyId
        elif source14_.is_Static:
            d_450___mcc_h5_ = source14_.Static
            d_451_i_ = d_450___mcc_h5_
            return (d_451_i_).keyId
        elif source14_.is_KmsRsa:
            d_452___mcc_h6_ = source14_.KmsRsa
            d_453_i_ = d_452___mcc_h6_
            return (d_453_i_).keyId
        elif True:
            d_454___mcc_h7_ = source14_.Hierarchy
            d_455_i_ = d_454___mcc_h7_
            return (d_455_i_).keyId


class Config:
    @classmethod
    def default(cls, ):
        return lambda: Config_Config(_dafny.Map({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Config(self) -> bool:
        return isinstance(self, Config_Config)

class Config_Config(Config, NamedTuple('Config', [('keys', Any)])):
    def __dafnystr__(self) -> str:
        return f'KeysVectorOperations.Config.Config({_dafny.string_of(self.keys)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Config_Config) and self.keys == __o.keys
    def __hash__(self) -> int:
        return super().__hash__()

