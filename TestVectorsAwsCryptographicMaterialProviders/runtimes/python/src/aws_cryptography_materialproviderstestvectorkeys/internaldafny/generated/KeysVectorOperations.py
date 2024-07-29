import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import standard_library.internaldafny.generated.Wrappers as Wrappers
import standard_library.internaldafny.generated.BoundedInts as BoundedInts
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import standard_library.internaldafny.generated.UTF8 as UTF8
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes as AwsCryptographyPrimitivesTypes
import aws_cryptography_primitives.internaldafny.generated.ExternRandom as ExternRandom
import aws_cryptography_primitives.internaldafny.generated.Random as Random
import aws_cryptography_primitives.internaldafny.generated.AESEncryption as AESEncryption
import aws_cryptography_primitives.internaldafny.generated.ExternDigest as ExternDigest
import aws_cryptography_primitives.internaldafny.generated.Digest as Digest
import aws_cryptography_primitives.internaldafny.generated.HMAC as HMAC
import aws_cryptography_primitives.internaldafny.generated.WrappedHMAC as WrappedHMAC
import aws_cryptography_primitives.internaldafny.generated.HKDF as HKDF
import aws_cryptography_primitives.internaldafny.generated.WrappedHKDF as WrappedHKDF
import aws_cryptography_primitives.internaldafny.generated.Signature as Signature
import aws_cryptography_primitives.internaldafny.generated.KdfCtr as KdfCtr
import aws_cryptography_primitives.internaldafny.generated.RSAEncryption as RSAEncryption
import aws_cryptography_primitives.internaldafny.generated.ECDH as ECDH
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesOperations as AwsCryptographyPrimitivesOperations
import aws_cryptography_primitives.internaldafny.generated.AtomicPrimitives as AtomicPrimitives
import com_amazonaws_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import com_amazonaws_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import standard_library.internaldafny.generated.Base64 as Base64
import aws_cryptographic_materialproviders.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_materialproviders.internaldafny.generated.Materials as Materials
import aws_cryptographic_materialproviders.internaldafny.generated.Keyring as Keyring
import standard_library.internaldafny.generated.Relations as Relations
import standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import standard_library.internaldafny.generated.Math as Math
import standard_library.internaldafny.generated.Seq as Seq
import aws_cryptographic_materialproviders.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import standard_library.internaldafny.generated.Actions as Actions
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_materialproviders.internaldafny.generated.Constants as Constants
import standard_library.internaldafny.generated.UUID as UUID
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialWrapping as MaterialWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_materialproviders.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.EdkWrapping as EdkWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.ErrorMessages as ErrorMessages
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsKeyring as AwsKmsKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.StrictMultiKeyring as StrictMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsDiscoveryKeyring as AwsKmsDiscoveryKeyring
import com_amazonaws_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import aws_cryptographic_materialproviders.internaldafny.generated.DiscoveryMultiKeyring as DiscoveryMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkDiscoveryKeyring as AwsKmsMrkDiscoveryKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.MrkAwareDiscoveryMultiKeyring as MrkAwareDiscoveryMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkKeyring as AwsKmsMrkKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.MrkAwareStrictMultiKeyring as MrkAwareStrictMultiKeyring
import standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import standard_library.internaldafny.generated.Time as Time
import aws_cryptographic_materialproviders.internaldafny.generated.LocalCMC as LocalCMC
import aws_cryptographic_materialproviders.internaldafny.generated.SynchronizedLocalCMC as SynchronizedLocalCMC
import standard_library.internaldafny.generated.SortedSets as SortedSets
import aws_cryptographic_materialproviders.internaldafny.generated.StormTracker as StormTracker
import aws_cryptographic_materialproviders.internaldafny.generated.StormTrackingCMC as StormTrackingCMC
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsHierarchicalKeyring as AwsKmsHierarchicalKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsRsaKeyring as AwsKmsRsaKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.EcdhEdkWrapping as EcdhEdkWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.RawECDHKeyring as RawECDHKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsEcdhKeyring as AwsKmsEcdhKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawAESKeyring as RawAESKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawRSAKeyring as RawRSAKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.CMM as CMM
import aws_cryptographic_materialproviders.internaldafny.generated.Defaults as Defaults
import aws_cryptographic_materialproviders.internaldafny.generated.Commitment as Commitment
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultCMM as DefaultCMM
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultClientSupplier as DefaultClientSupplier
import aws_cryptographic_materialproviders.internaldafny.generated.Utils as Utils
import aws_cryptographic_materialproviders.internaldafny.generated.RequiredEncryptionContextCMM as RequiredEncryptionContextCMM
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersOperations as AwsCryptographyMaterialProvidersOperations
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialProviders as MaterialProviders
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStoreErrorMessages as KeyStoreErrorMessages
import aws_cryptographic_materialproviders.internaldafny.generated.KmsArn as KmsArn
import aws_cryptographic_materialproviders.internaldafny.generated.Structure as Structure
import aws_cryptographic_materialproviders.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable
import aws_cryptographic_materialproviders.internaldafny.generated.GetKeys as GetKeys
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStore as KeyStore
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
import standard_library.internaldafny.generated.Unicode as Unicode
import standard_library.internaldafny.generated.Functions as Functions
import standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import standard_library.internaldafny.generated.FileIO as FileIO
import standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import standard_library.internaldafny.generated.MulInternals as MulInternals
import standard_library.internaldafny.generated.Mul as Mul
import standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import standard_library.internaldafny.generated.ModInternals as ModInternals
import standard_library.internaldafny.generated.DivInternals as DivInternals
import standard_library.internaldafny.generated.DivMod as DivMod
import standard_library.internaldafny.generated.Power as Power
import standard_library.internaldafny.generated.Logarithm as Logarithm
import standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import standard_library.internaldafny.generated.Streams as Streams
import standard_library.internaldafny.generated.Sorting as Sorting
import standard_library.internaldafny.generated.HexStrings as HexStrings
import standard_library.internaldafny.generated.GetOpt as GetOpt
import standard_library.internaldafny.generated.FloatCompare as FloatCompare
import standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.MplManifestOptions as MplManifestOptions
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AllAlgorithmSuites as AllAlgorithmSuites
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.WrappedMaterialProviders as WrappedMaterialProviders
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.AwsCryptographyMaterialProvidersTestVectorKeysTypes as AwsCryptographyMaterialProvidersTestVectorKeysTypes
import standard_library.internaldafny.generated.JSON_Utils_Views_Core as JSON_Utils_Views_Core
import standard_library.internaldafny.generated.JSON_Utils_Views_Writers as JSON_Utils_Views_Writers
import standard_library.internaldafny.generated.JSON_Utils_Lexers_Core as JSON_Utils_Lexers_Core
import standard_library.internaldafny.generated.JSON_Utils_Lexers_Strings as JSON_Utils_Lexers_Strings
import standard_library.internaldafny.generated.JSON_Utils_Cursors as JSON_Utils_Cursors
import standard_library.internaldafny.generated.JSON_Utils_Parsers as JSON_Utils_Parsers
import standard_library.internaldafny.generated.JSON_Utils_Str_CharStrConversion as JSON_Utils_Str_CharStrConversion
import standard_library.internaldafny.generated.JSON_Utils_Str_CharStrEscaping as JSON_Utils_Str_CharStrEscaping
import standard_library.internaldafny.generated.JSON_Utils_Str as JSON_Utils_Str
import standard_library.internaldafny.generated.JSON_Utils_Seq as JSON_Utils_Seq
import standard_library.internaldafny.generated.JSON_Utils_Vectors as JSON_Utils_Vectors
import standard_library.internaldafny.generated.JSON_Errors as JSON_Errors
import standard_library.internaldafny.generated.JSON_Values as JSON_Values
import standard_library.internaldafny.generated.JSON_Spec as JSON_Spec
import standard_library.internaldafny.generated.JSON_Grammar as JSON_Grammar
import standard_library.internaldafny.generated.JSON_Serializer_ByteStrConversion as JSON_Serializer_ByteStrConversion
import standard_library.internaldafny.generated.JSON_Serializer as JSON_Serializer
import standard_library.internaldafny.generated.JSON_Deserializer_Uint16StrConversion as JSON_Deserializer_Uint16StrConversion
import standard_library.internaldafny.generated.JSON_Deserializer_ByteStrConversion as JSON_Deserializer_ByteStrConversion
import standard_library.internaldafny.generated.JSON_Deserializer as JSON_Deserializer
import standard_library.internaldafny.generated.JSON_ConcreteSyntax_Spec as JSON_ConcreteSyntax_Spec
import standard_library.internaldafny.generated.JSON_ConcreteSyntax_SpecProperties as JSON_ConcreteSyntax_SpecProperties
import standard_library.internaldafny.generated.JSON_ZeroCopy_Serializer as JSON_ZeroCopy_Serializer
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Core as JSON_ZeroCopy_Deserializer_Core
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Strings as JSON_ZeroCopy_Deserializer_Strings
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Numbers as JSON_ZeroCopy_Deserializer_Numbers
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_ObjectParams as JSON_ZeroCopy_Deserializer_ObjectParams
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Objects as JSON_ZeroCopy_Deserializer_Objects
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_ArrayParams as JSON_ZeroCopy_Deserializer_ArrayParams
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Arrays as JSON_ZeroCopy_Deserializer_Arrays
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Constants as JSON_ZeroCopy_Deserializer_Constants
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Values as JSON_ZeroCopy_Deserializer_Values
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_API as JSON_ZeroCopy_Deserializer_API
import standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer as JSON_ZeroCopy_Deserializer
import standard_library.internaldafny.generated.JSON_ZeroCopy_API as JSON_ZeroCopy_API
import standard_library.internaldafny.generated.JSON_API as JSON_API
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.JSONHelpers as JSONHelpers
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.KeyDescription as KeyDescription
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.KeyMaterial as KeyMaterial
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.CreateStaticKeyrings as CreateStaticKeyrings
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.CreateStaticKeyStores as CreateStaticKeyStores
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.KeyringFromKeyDescription as KeyringFromKeyDescription
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.CmmFromKeyDescription as CmmFromKeyDescription

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
        d_529_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_529_valueOrError0_ = Wrappers.default__.Need(KeyDescription.default__.Keyring_q((input).keyDescription), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Only Keyring key descriptions are supported.")))
        if (d_529_valueOrError0_).IsFailure():
            output = (d_529_valueOrError0_).PropagateFailure()
            return output
        d_530_maybeMpl_: Wrappers.Result
        out33_: Wrappers.Result
        out33_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_530_maybeMpl_ = out33_
        d_531_mpl_: MaterialProviders.MaterialProvidersClient
        d_532_valueOrError1_: Wrappers.Result = None
        def lambda50_(d_533_e_):
            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_533_e_)

        d_532_valueOrError1_ = (d_530_maybeMpl_).MapFailure(lambda50_)
        if (d_532_valueOrError1_).IsFailure():
            output = (d_532_valueOrError1_).PropagateFailure()
            return output
        d_531_mpl_ = (d_532_valueOrError1_).Extract()
        out34_: Wrappers.Result
        out34_ = KeyringFromKeyDescription.default__.ToKeyring(d_531_mpl_, (config).keys, (input).keyDescription)
        output = out34_
        return output

    @staticmethod
    def CreateWrappedTestVectorKeyringEnsuresPublicly(input, output):
        return True

    @staticmethod
    def CreateWrappedTestVectorKeyring(config, input):
        output: Wrappers.Result = None
        d_534_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_534_valueOrError0_ = Wrappers.default__.Need(KeyDescription.default__.Keyring_q((input).keyDescription), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Only Keyring key descriptions are supported.")))
        if (d_534_valueOrError0_).IsFailure():
            output = (d_534_valueOrError0_).PropagateFailure()
            return output
        d_535_maybeMpl_: Wrappers.Result
        out35_: Wrappers.Result
        out35_ = WrappedMaterialProviders.default__.WrappedMaterialProviders(WrappedMaterialProviders.default__.WrappedDefaultMaterialProvidersConfig())
        d_535_maybeMpl_ = out35_
        d_536_wrappedMPL_: AwsCryptographyMaterialProvidersTypes.IAwsCryptographicMaterialProvidersClient
        d_537_valueOrError1_: Wrappers.Result = None
        def lambda51_(d_538_e_):
            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_538_e_)

        d_537_valueOrError1_ = (d_535_maybeMpl_).MapFailure(lambda51_)
        if (d_537_valueOrError1_).IsFailure():
            output = (d_537_valueOrError1_).PropagateFailure()
            return output
        d_536_wrappedMPL_ = (d_537_valueOrError1_).Extract()
        out36_: Wrappers.Result
        out36_ = KeyringFromKeyDescription.default__.ToKeyring(d_536_wrappedMPL_, (config).keys, (input).keyDescription)
        output = out36_
        return output

    @staticmethod
    def CreateWrappedTestVectorCmmEnsuresPublicly(input, output):
        return True

    @staticmethod
    def CreateWrappedTestVectorCmm(config, input):
        output: Wrappers.Result = None
        d_539_maybeMpl_: Wrappers.Result
        out37_: Wrappers.Result
        out37_ = WrappedMaterialProviders.default__.WrappedMaterialProviders(WrappedMaterialProviders.default__.WrappedDefaultMaterialProvidersConfig())
        d_539_maybeMpl_ = out37_
        d_540_wrappedMPL_: AwsCryptographyMaterialProvidersTypes.IAwsCryptographicMaterialProvidersClient
        d_541_valueOrError0_: Wrappers.Result = None
        def lambda52_(d_542_e_):
            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_542_e_)

        d_541_valueOrError0_ = (d_539_maybeMpl_).MapFailure(lambda52_)
        if (d_541_valueOrError0_).IsFailure():
            output = (d_541_valueOrError0_).PropagateFailure()
            return output
        d_540_wrappedMPL_ = (d_541_valueOrError0_).Extract()
        out38_: Wrappers.Result
        out38_ = CmmFromKeyDescription.default__.ToCmm(d_540_wrappedMPL_, (config).keys, (input).keyDescription, (input).forOperation)
        output = out38_
        return output

    @staticmethod
    def GetKeyDescription(config, input):
        def lambda53_(d_544_e_):
            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException((d_544_e_).ToString()))

        d_543_valueOrError0_ = (JSON_API.default__.Deserialize((input).json)).MapFailure(lambda53_)
        if (d_543_valueOrError0_).IsFailure():
            return (d_543_valueOrError0_).PropagateFailure()
        elif True:
            d_545_keyDescriptionJSON_ = (d_543_valueOrError0_).Extract()
            def lambda54_(d_547_e_):
                return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_547_e_))

            d_546_valueOrError1_ = (KeyDescription.default__.ToKeyDescription(d_545_keyDescriptionJSON_)).MapFailure(lambda54_)
            if (d_546_valueOrError1_).IsFailure():
                return (d_546_valueOrError1_).PropagateFailure()
            elif True:
                d_548_keyDescription_ = (d_546_valueOrError1_).Extract()
                return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTestVectorKeysTypes.GetKeyDescriptionOutput_GetKeyDescriptionOutput(d_548_keyDescription_))

    @staticmethod
    def SerializeKeyDescription(config, input):
        def lambda55_(d_550_s_):
            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_550_s_))

        d_549_valueOrError0_ = (KeyDescription.default__.ToJson((input).keyDescription, 2)).MapFailure(lambda55_)
        if (d_549_valueOrError0_).IsFailure():
            return (d_549_valueOrError0_).PropagateFailure()
        elif True:
            d_551_json_ = (d_549_valueOrError0_).Extract()
            def lambda56_(d_553_e_):
                return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException((d_553_e_).ToString()))

            d_552_valueOrError1_ = (JSON_API.default__.Serialize(d_551_json_)).MapFailure(lambda56_)
            if (d_552_valueOrError1_).IsFailure():
                return (d_552_valueOrError1_).PropagateFailure()
            elif True:
                d_554_jsonBytes_ = (d_552_valueOrError1_).Extract()
                return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTestVectorKeysTypes.SerializeKeyDescriptionOutput_SerializeKeyDescriptionOutput(d_554_jsonBytes_))


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

