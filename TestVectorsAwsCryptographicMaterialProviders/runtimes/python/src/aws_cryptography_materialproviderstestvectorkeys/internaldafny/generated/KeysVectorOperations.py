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
import AesKdfCtr
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
import StandardLibraryInterop
import Streams
import Sorting
import HexStrings
import GetOpt
import FloatCompare
import ConcurrentCall
import Base64Lemmas
import MplManifestOptions
import AllAlgorithmSuites
import software_amazon_cryptography_materialproviders_internaldafny_wrapped
import software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types
import JSON_Utils_Views_Core
import JSON_Utils_Views_Writers
import JSON_Utils_Views
import JSON_Utils_Lexers_Core
import JSON_Utils_Lexers_Strings
import JSON_Utils_Lexers
import JSON_Utils_Cursors
import JSON_Utils_Parsers
import JSON_Utils_Str_CharStrConversion
import JSON_Utils_Str_CharStrEscaping
import JSON_Utils_Str
import JSON_Utils_Seq
import JSON_Utils_Vectors
import JSON_Utils
import JSON_Errors
import JSON_Values
import JSON_Spec
import JSON_Grammar
import JSON_Serializer_ByteStrConversion
import JSON_Serializer
import JSON_Deserializer_Uint16StrConversion
import JSON_Deserializer_ByteStrConversion
import JSON_Deserializer
import JSON_ConcreteSyntax_Spec
import JSON_ConcreteSyntax_SpecProperties
import JSON_ConcreteSyntax
import JSON_ZeroCopy_Serializer
import JSON_ZeroCopy_Deserializer_Core
import JSON_ZeroCopy_Deserializer_Strings
import JSON_ZeroCopy_Deserializer_Numbers
import JSON_ZeroCopy_Deserializer_ObjectParams
import JSON_ZeroCopy_Deserializer_Objects
import JSON_ZeroCopy_Deserializer_ArrayParams
import JSON_ZeroCopy_Deserializer_Arrays
import JSON_ZeroCopy_Deserializer_Constants
import JSON_ZeroCopy_Deserializer_Values
import JSON_ZeroCopy_Deserializer_API
import JSON_ZeroCopy_Deserializer
import JSON_ZeroCopy_API
import JSON_ZeroCopy
import JSON_API
import JSON
import JSONHelpers
import KeyDescription
import KeyMaterial
import CreateStaticKeyrings
import CreateStaticKeyStores
import KeyringFromKeyDescription
import CmmFromKeyDescription

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
        d_487_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_487_valueOrError0_ = Wrappers.default__.Need(KeyDescription.default__.Keyring_q((input).keyDescription), software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Only Keyring key descriptions are supported.")))
        if (d_487_valueOrError0_).IsFailure():
            output = (d_487_valueOrError0_).PropagateFailure()
            return output
        d_488_maybeMpl_: Wrappers.Result
        out40_: Wrappers.Result
        out40_ = software_amazon_cryptography_materialproviders_internaldafny.default__.MaterialProviders(software_amazon_cryptography_materialproviders_internaldafny.default__.DefaultMaterialProvidersConfig())
        d_488_maybeMpl_ = out40_
        d_489_mpl_: software_amazon_cryptography_materialproviders_internaldafny_types.IAwsCryptographicMaterialProvidersClient
        d_490_valueOrError1_: Wrappers.Result = None
        def lambda42_(d_491_e_):
            return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_491_e_)

        d_490_valueOrError1_ = (d_488_maybeMpl_).MapFailure(lambda42_)
        if (d_490_valueOrError1_).IsFailure():
            output = (d_490_valueOrError1_).PropagateFailure()
            return output
        d_489_mpl_ = (d_490_valueOrError1_).Extract()
        out41_: Wrappers.Result
        out41_ = KeyringFromKeyDescription.default__.ToKeyring(d_489_mpl_, (config).keys, (input).keyDescription)
        output = out41_
        return output

    @staticmethod
    def CreateWrappedTestVectorKeyringEnsuresPublicly(input, output):
        return True

    @staticmethod
    def CreateWrappedTestVectorKeyring(config, input):
        output: Wrappers.Result = None
        d_492_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_492_valueOrError0_ = Wrappers.default__.Need(KeyDescription.default__.Keyring_q((input).keyDescription), software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_KeyVectorException(_dafny.Seq("Only Keyring key descriptions are supported.")))
        if (d_492_valueOrError0_).IsFailure():
            output = (d_492_valueOrError0_).PropagateFailure()
            return output
        d_493_maybeMpl_: Wrappers.Result
        out42_: Wrappers.Result
        out42_ = software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedMaterialProviders(software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedDefaultMaterialProvidersConfig())
        d_493_maybeMpl_ = out42_
        d_494_wrappedMPL_: software_amazon_cryptography_materialproviders_internaldafny_types.IAwsCryptographicMaterialProvidersClient
        d_495_valueOrError1_: Wrappers.Result = None
        def lambda43_(d_496_e_):
            return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_496_e_)

        d_495_valueOrError1_ = (d_493_maybeMpl_).MapFailure(lambda43_)
        if (d_495_valueOrError1_).IsFailure():
            output = (d_495_valueOrError1_).PropagateFailure()
            return output
        d_494_wrappedMPL_ = (d_495_valueOrError1_).Extract()
        out43_: Wrappers.Result
        out43_ = KeyringFromKeyDescription.default__.ToKeyring(d_494_wrappedMPL_, (config).keys, (input).keyDescription)
        output = out43_
        return output

    @staticmethod
    def CreateWrappedTestVectorCmmEnsuresPublicly(input, output):
        return True

    @staticmethod
    def CreateWrappedTestVectorCmm(config, input):
        output: Wrappers.Result = None
        d_497_maybeMpl_: Wrappers.Result
        out44_: Wrappers.Result
        out44_ = software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedMaterialProviders(software_amazon_cryptography_materialproviders_internaldafny_wrapped.default__.WrappedDefaultMaterialProvidersConfig())
        d_497_maybeMpl_ = out44_
        d_498_wrappedMPL_: software_amazon_cryptography_materialproviders_internaldafny_types.IAwsCryptographicMaterialProvidersClient
        d_499_valueOrError0_: Wrappers.Result = None
        def lambda44_(d_500_e_):
            return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(d_500_e_)

        d_499_valueOrError0_ = (d_497_maybeMpl_).MapFailure(lambda44_)
        if (d_499_valueOrError0_).IsFailure():
            output = (d_499_valueOrError0_).PropagateFailure()
            return output
        d_498_wrappedMPL_ = (d_499_valueOrError0_).Extract()
        out45_: Wrappers.Result
        out45_ = CmmFromKeyDescription.default__.ToCmm(d_498_wrappedMPL_, (config).keys, (input).keyDescription, (input).forOperation)
        output = out45_
        return output

    @staticmethod
    def GetKeyDescription(config, input):
        def lambda45_(d_502_e_):
            return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException((d_502_e_).ToString()))

        d_501_valueOrError0_ = (JSON_API.default__.Deserialize((input).json)).MapFailure(lambda45_)
        if (d_501_valueOrError0_).IsFailure():
            return (d_501_valueOrError0_).PropagateFailure()
        elif True:
            d_503_keyDescriptionJSON_ = (d_501_valueOrError0_).Extract()
            def lambda46_(d_505_e_):
                return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(d_505_e_))

            d_504_valueOrError1_ = (KeyDescription.default__.ToKeyDescription(d_503_keyDescriptionJSON_)).MapFailure(lambda46_)
            if (d_504_valueOrError1_).IsFailure():
                return (d_504_valueOrError1_).PropagateFailure()
            elif True:
                d_506_keyDescription_ = (d_504_valueOrError1_).Extract()
                return Wrappers.Result_Success(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.GetKeyDescriptionOutput_GetKeyDescriptionOutput(d_506_keyDescription_))

    @staticmethod
    def SerializeKeyDescription(config, input):
        def lambda47_(d_508_s_):
            return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(d_508_s_))

        d_507_valueOrError0_ = (KeyDescription.default__.ToJson((input).keyDescription, 2)).MapFailure(lambda47_)
        if (d_507_valueOrError0_).IsFailure():
            return (d_507_valueOrError0_).PropagateFailure()
        elif True:
            d_509_json_ = (d_507_valueOrError0_).Extract()
            def lambda48_(d_511_e_):
                return software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.Error_AwsCryptographyMaterialProviders(software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException((d_511_e_).ToString()))

            d_510_valueOrError1_ = (JSON_API.default__.Serialize(d_509_json_)).MapFailure(lambda48_)
            if (d_510_valueOrError1_).IsFailure():
                return (d_510_valueOrError1_).PropagateFailure()
            elif True:
                d_512_jsonBytes_ = (d_510_valueOrError1_).Extract()
                return Wrappers.Result_Success(software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny_types.SerializeKeyDescriptionOutput_SerializeKeyDescriptionOutput(d_512_jsonBytes_))


class Config:
    @classmethod
    def default(cls, ):
        return lambda: Config_Config(_dafny.Map({}), JSON_Values.JSON.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Config(self) -> bool:
        return isinstance(self, Config_Config)

class Config_Config(Config, NamedTuple('Config', [('keys', Any), ('keysJson', Any)])):
    def __dafnystr__(self) -> str:
        return f'KeysVectorOperations.Config.Config({_dafny.string_of(self.keys)}, {_dafny.string_of(self.keysJson)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Config_Config) and self.keys == __o.keys and self.keysJson == __o.keysJson
    def __hash__(self) -> int:
        return super().__hash__()

