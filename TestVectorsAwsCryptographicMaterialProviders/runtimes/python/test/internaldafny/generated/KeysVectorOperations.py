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
import CreateAwsKmsMrkMultiKeyrings
import CreateRawAesKeyrings
import CreateRawRsaKeyrings
import CreateKeyrings
import software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types
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

assert "KeysVectorOperations" == __name__
KeysVectorOperations = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def CreateTestVectorKeyringEnsuresPublicly(input, output):
        return True

    @staticmethod
    def CreateTestVectorKeyring(config, input):
        output: Wrappers.Result = None
        d_1652_keyDescription_: software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription
        d_1652_keyDescription_ = (input).keyDescription
        d_1653_keyId_: _dafny.Seq
        d_1653_keyId_ = KeysVectorOperations.default__.GetKeyId(d_1652_keyDescription_)
        d_1654_info_: KeyringFromKeyDescription.KeyringInfo
        d_1654_info_ = KeyringFromKeyDescription.KeyringInfo_KeyringInfo(d_1652_keyDescription_, (Wrappers.Option_Some(((config).keys)[d_1653_keyId_]) if (d_1653_keyId_) in ((config).keys) else Wrappers.Option_None()))
        d_1655_maybeMpl_: Wrappers.Result
        out318_: Wrappers.Result
        out318_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_1655_maybeMpl_ = out318_
        d_1656_mpl_: software_amazon_cryptography_materialproviders_internaldafny.MaterialProvidersClient
        d_1657_valueOrError0_: Wrappers.Result = None
        def lambda105_(d_1658_e_):
            return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_1658_e_)

        d_1657_valueOrError0_ = (d_1655_maybeMpl_).MapFailure(lambda105_)
        if (d_1657_valueOrError0_).IsFailure():
            output = (d_1657_valueOrError0_).PropagateFailure()
            return output
        d_1656_mpl_ = (d_1657_valueOrError0_).Extract()
        out319_: Wrappers.Result
        out319_ = KeyringFromKeyDescription.default__.ToKeyring(d_1656_mpl_, d_1654_info_)
        output = out319_
        return output

    @staticmethod
    def CreateWappedTestVectorKeyringEnsuresPublicly(input, output):
        return True

    @staticmethod
    def CreateWappedTestVectorKeyring(config, input):
        output: Wrappers.Result = None
        d_1659_keyDescription_: software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.KeyDescription
        d_1659_keyDescription_ = (input).keyDescription
        d_1660_keyId_: _dafny.Seq
        d_1660_keyId_ = KeysVectorOperations.default__.GetKeyId(d_1659_keyDescription_)
        d_1661_info_: KeyringFromKeyDescription.KeyringInfo
        d_1661_info_ = KeyringFromKeyDescription.KeyringInfo_KeyringInfo(d_1659_keyDescription_, (Wrappers.Option_Some(((config).keys)[d_1660_keyId_]) if (d_1660_keyId_) in ((config).keys) else Wrappers.Option_None()))
        d_1662_maybeMpl_: Wrappers.Result
        out320_: Wrappers.Result
        out320_ = software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedMaterialProviders(software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedDefaultMaterialProvidersConfig())
        d_1662_maybeMpl_ = out320_
        d_1663_wrappedMPL_: software_amazon_cryptography_materialproviders_internaldafny_types.IAwsCryptographicMaterialProvidersClient
        d_1664_valueOrError0_: Wrappers.Result = None
        def lambda106_(d_1665_e_):
            return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_1665_e_)

        d_1664_valueOrError0_ = (d_1662_maybeMpl_).MapFailure(lambda106_)
        if (d_1664_valueOrError0_).IsFailure():
            output = (d_1664_valueOrError0_).PropagateFailure()
            return output
        d_1663_wrappedMPL_ = (d_1664_valueOrError0_).Extract()
        out321_: Wrappers.Result
        out321_ = KeyringFromKeyDescription.default__.ToKeyring(d_1663_wrappedMPL_, d_1661_info_)
        output = out321_
        return output

    @staticmethod
    def GetKeyDescription(config, input):
        def lambda107_(d_1667_e_):
            return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException((d_1667_e_).ToString()))

        d_1666_valueOrError0_ = (JSON_mAPI.default__.Deserialize((input).json)).MapFailure(lambda107_)
        if (d_1666_valueOrError0_).IsFailure():
            return (d_1666_valueOrError0_).PropagateFailure()
        elif True:
            d_1668_keyDescriptionJSON_ = (d_1666_valueOrError0_).Extract()
            def lambda108_(d_1670_e_):
                return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(d_1670_e_))

            d_1669_valueOrError1_ = (KeyDescription.default__.ToKeyDescription(d_1668_keyDescriptionJSON_)).MapFailure(lambda108_)
            if (d_1669_valueOrError1_).IsFailure():
                return (d_1669_valueOrError1_).PropagateFailure()
            elif True:
                d_1671_keyDescription_ = (d_1669_valueOrError1_).Extract()
                return Wrappers.Result_Success(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.GetKeyDescriptionOutput_GetKeyDescriptionOutput(d_1671_keyDescription_))

    @staticmethod
    def SerializeKeyDescription(config, input):
        return Wrappers.Result_Failure(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Not Supported")))

    @staticmethod
    def GetKeyId(input):
        source51_ = input
        if source51_.is_Kms:
            d_1672___mcc_h0_ = source51_.Kms
            d_1673_i_ = d_1672___mcc_h0_
            return (d_1673_i_).keyId
        elif source51_.is_KmsMrk:
            d_1674___mcc_h1_ = source51_.KmsMrk
            d_1675_i_ = d_1674___mcc_h1_
            return (d_1675_i_).keyId
        elif source51_.is_KmsMrkDiscovery:
            d_1676___mcc_h2_ = source51_.KmsMrkDiscovery
            d_1677_i_ = d_1676___mcc_h2_
            return (d_1677_i_).keyId
        elif source51_.is_RSA:
            d_1678___mcc_h3_ = source51_.RSA
            d_1679_i_ = d_1678___mcc_h3_
            return (d_1679_i_).keyId
        elif source51_.is_AES:
            d_1680___mcc_h4_ = source51_.AES
            d_1681_i_ = d_1680___mcc_h4_
            return (d_1681_i_).keyId
        elif source51_.is_Static:
            d_1682___mcc_h5_ = source51_.Static
            d_1683_i_ = d_1682___mcc_h5_
            return (d_1683_i_).keyId
        elif source51_.is_KmsRsa:
            d_1684___mcc_h6_ = source51_.KmsRsa
            d_1685_i_ = d_1684___mcc_h6_
            return (d_1685_i_).keyId
        elif True:
            d_1686___mcc_h7_ = source51_.Hierarchy
            d_1687_i_ = d_1686___mcc_h7_
            return (d_1687_i_).keyId


class Config:
    @classmethod
    def default(cls, ):
        return lambda: Config_Config(_dafny.Map({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Config(self) -> bool:
        return isinstance(self, KeysVectorOperations.Config_Config)

class Config_Config(Config, NamedTuple('Config', [('keys', Any)])):
    def __dafnystr__(self) -> str:
        return f'KeysVectorOperations.Config.Config({_dafny.string_of(self.keys)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeysVectorOperations.Config_Config) and self.keys == __o.keys
    def __hash__(self) -> int:
        return super().__hash__()

