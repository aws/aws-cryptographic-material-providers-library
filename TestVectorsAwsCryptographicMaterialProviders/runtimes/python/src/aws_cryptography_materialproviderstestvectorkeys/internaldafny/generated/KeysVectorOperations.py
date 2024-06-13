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
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialWrapping as MaterialWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_materialproviders.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.EdkWrapping as EdkWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsKeyring as AwsKmsKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.StrictMultiKeyring as StrictMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsDiscoveryKeyring as AwsKmsDiscoveryKeyring
import com_amazonaws_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws as Com_Amazonaws
import com_amazonaws_dynamodb.internaldafny.generated.Com as Com
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
import standard_library.internaldafny.generated.UUID as UUID
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsHierarchicalKeyring as AwsKmsHierarchicalKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsRsaKeyring as AwsKmsRsaKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawAESKeyring as RawAESKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.RawRSAKeyring as RawRSAKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.CMM as CMM
import aws_cryptographic_materialproviders.internaldafny.generated.Defaults as Defaults
import aws_cryptographic_materialproviders.internaldafny.generated.Commitment as Commitment
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultCMM as DefaultCMM
import aws_cryptographic_materialproviders.internaldafny.generated.DefaultClientSupplier as DefaultClientSupplier
import aws_cryptographic_materialproviders.internaldafny.generated.RequiredEncryptionContextCMM as RequiredEncryptionContextCMM
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersOperations as AwsCryptographyMaterialProvidersOperations
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialProviders as MaterialProviders
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
import standard_library.internaldafny.generated.JSON_Utils_Views as JSON_Utils_Views
import standard_library.internaldafny.generated.JSON_Utils_Lexers_Core as JSON_Utils_Lexers_Core
import standard_library.internaldafny.generated.JSON_Utils_Lexers_Strings as JSON_Utils_Lexers_Strings
import standard_library.internaldafny.generated.JSON_Utils_Lexers as JSON_Utils_Lexers
import standard_library.internaldafny.generated.JSON_Utils_Cursors as JSON_Utils_Cursors
import standard_library.internaldafny.generated.JSON_Utils_Parsers as JSON_Utils_Parsers
import standard_library.internaldafny.generated.JSON_Utils_Str_CharStrConversion as JSON_Utils_Str_CharStrConversion
import standard_library.internaldafny.generated.JSON_Utils_Str_CharStrEscaping as JSON_Utils_Str_CharStrEscaping
import standard_library.internaldafny.generated.JSON_Utils_Str as JSON_Utils_Str
import standard_library.internaldafny.generated.JSON_Utils_Seq as JSON_Utils_Seq
import standard_library.internaldafny.generated.JSON_Utils_Vectors as JSON_Utils_Vectors
import standard_library.internaldafny.generated.JSON_Utils as JSON_Utils
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
import standard_library.internaldafny.generated.JSON_ConcreteSyntax as JSON_ConcreteSyntax
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
import standard_library.internaldafny.generated.JSON_ZeroCopy as JSON_ZeroCopy
import standard_library.internaldafny.generated.JSON_API as JSON_API
import standard_library.internaldafny.generated.JSON as JSON
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.JSONHelpers as JSONHelpers
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.KeyDescription as KeyDescription
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.KeyMaterial as KeyMaterial
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.CreateStaticKeyrings as CreateStaticKeyrings
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.CreateStaticKeyStores as CreateStaticKeyStores
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.KeyringFromKeyDescription as KeyringFromKeyDescription
import aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.CmmFromKeyDescription as CmmFromKeyDescription

# Module: aws_cryptography_materialproviderstestvectorkeys.internaldafny.generated.KeysVectorOperations

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def CreateTestVectorKeyringEnsuresPublicly(input, output):
        return True

    @staticmethod
    def CreateTestVectorKeyring(config, input):
        output: Wrappers.Result = None
        d_489_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_489_valueOrError0_ = Wrappers.default__.Need(KeyDescription.default__.Keyring_q((input).keyDescription), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Only Keyring key descriptions are supported.")))
        if (d_489_valueOrError0_).IsFailure():
            output = (d_489_valueOrError0_).PropagateFailure()
            return output
        d_490_maybeMpl_: Wrappers.Result
        out40_: Wrappers.Result
        out40_ = MaterialProviders.default__.MaterialProviders(MaterialProviders.default__.DefaultMaterialProvidersConfig())
        d_490_maybeMpl_ = out40_
        d_491_mpl_: MaterialProviders.MaterialProvidersClient
        d_492_valueOrError1_: Wrappers.Result = None
        def lambda42_(d_493_e_):
            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_493_e_)

        d_492_valueOrError1_ = (d_490_maybeMpl_).MapFailure(lambda42_)
        if (d_492_valueOrError1_).IsFailure():
            output = (d_492_valueOrError1_).PropagateFailure()
            return output
        d_491_mpl_ = (d_492_valueOrError1_).Extract()
        out41_: Wrappers.Result
        out41_ = KeyringFromKeyDescription.default__.ToKeyring(d_491_mpl_, (config).keys, (input).keyDescription)
        output = out41_
        return output

    @staticmethod
    def CreateWrappedTestVectorKeyringEnsuresPublicly(input, output):
        return True

    @staticmethod
    def CreateWrappedTestVectorKeyring(config, input):
        output: Wrappers.Result = None
        d_494_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_494_valueOrError0_ = Wrappers.default__.Need(KeyDescription.default__.Keyring_q((input).keyDescription), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Only Keyring key descriptions are supported.")))
        if (d_494_valueOrError0_).IsFailure():
            output = (d_494_valueOrError0_).PropagateFailure()
            return output
        d_495_maybeMpl_: Wrappers.Result
        out42_: Wrappers.Result
        out42_ = WrappedMaterialProviders.default__.WrappedMaterialProviders(WrappedMaterialProviders.default__.WrappedDefaultMaterialProvidersConfig())
        d_495_maybeMpl_ = out42_
        d_496_wrappedMPL_: AwsCryptographyMaterialProvidersTypes.IAwsCryptographicMaterialProvidersClient
        d_497_valueOrError1_: Wrappers.Result = None
        def lambda43_(d_498_e_):
            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_498_e_)

        d_497_valueOrError1_ = (d_495_maybeMpl_).MapFailure(lambda43_)
        if (d_497_valueOrError1_).IsFailure():
            output = (d_497_valueOrError1_).PropagateFailure()
            return output
        d_496_wrappedMPL_ = (d_497_valueOrError1_).Extract()
        out43_: Wrappers.Result
        out43_ = KeyringFromKeyDescription.default__.ToKeyring(d_496_wrappedMPL_, (config).keys, (input).keyDescription)
        output = out43_
        return output

    @staticmethod
    def CreateWrappedTestVectorCmmEnsuresPublicly(input, output):
        return True

    @staticmethod
    def CreateWrappedTestVectorCmm(config, input):
        output: Wrappers.Result = None
        d_499_maybeMpl_: Wrappers.Result
        out44_: Wrappers.Result
        out44_ = WrappedMaterialProviders.default__.WrappedMaterialProviders(WrappedMaterialProviders.default__.WrappedDefaultMaterialProvidersConfig())
        d_499_maybeMpl_ = out44_
        d_500_wrappedMPL_: AwsCryptographyMaterialProvidersTypes.IAwsCryptographicMaterialProvidersClient
        d_501_valueOrError0_: Wrappers.Result = None
        def lambda44_(d_502_e_):
            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_502_e_)

        d_501_valueOrError0_ = (d_499_maybeMpl_).MapFailure(lambda44_)
        if (d_501_valueOrError0_).IsFailure():
            output = (d_501_valueOrError0_).PropagateFailure()
            return output
        d_500_wrappedMPL_ = (d_501_valueOrError0_).Extract()
        out45_: Wrappers.Result
        out45_ = CmmFromKeyDescription.default__.ToCmm(d_500_wrappedMPL_, (config).keys, (input).keyDescription, (input).forOperation)
        output = out45_
        return output

    @staticmethod
    def GetKeyDescription(config, input):
        def lambda45_(d_504_e_):
            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException((d_504_e_).ToString()))

        d_503_valueOrError0_ = (JSON_API.default__.Deserialize((input).json)).MapFailure(lambda45_)
        if (d_503_valueOrError0_).IsFailure():
            return (d_503_valueOrError0_).PropagateFailure()
        elif True:
            d_505_keyDescriptionJSON_ = (d_503_valueOrError0_).Extract()
            def lambda46_(d_507_e_):
                return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_507_e_))

            d_506_valueOrError1_ = (KeyDescription.default__.ToKeyDescription(d_505_keyDescriptionJSON_)).MapFailure(lambda46_)
            if (d_506_valueOrError1_).IsFailure():
                return (d_506_valueOrError1_).PropagateFailure()
            elif True:
                d_508_keyDescription_ = (d_506_valueOrError1_).Extract()
                return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTestVectorKeysTypes.GetKeyDescriptionOutput_GetKeyDescriptionOutput(d_508_keyDescription_))

    @staticmethod
    def SerializeKeyDescription(config, input):
        def lambda47_(d_510_s_):
            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_510_s_))

        d_509_valueOrError0_ = (KeyDescription.default__.ToJson((input).keyDescription, 2)).MapFailure(lambda47_)
        if (d_509_valueOrError0_).IsFailure():
            return (d_509_valueOrError0_).PropagateFailure()
        elif True:
            d_511_json_ = (d_509_valueOrError0_).Extract()
            def lambda48_(d_513_e_):
                return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException((d_513_e_).ToString()))

            d_512_valueOrError1_ = (JSON_API.default__.Serialize(d_511_json_)).MapFailure(lambda48_)
            if (d_512_valueOrError1_).IsFailure():
                return (d_512_valueOrError1_).PropagateFailure()
            elif True:
                d_514_jsonBytes_ = (d_512_valueOrError1_).Extract()
                return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTestVectorKeysTypes.SerializeKeyDescriptionOutput_SerializeKeyDescriptionOutput(d_514_jsonBytes_))


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

