import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptographic_material_providers.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import smithy_dafny_standard_library.internaldafny.generated.BoundedInts as BoundedInts
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_Sequence as StandardLibrary_Sequence
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import smithy_dafny_standard_library.internaldafny.generated.UTF8 as UTF8
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
import aws_cryptography_internal_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import aws_cryptography_internal_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
import smithy_dafny_standard_library.internaldafny.generated.Relations as Relations
import smithy_dafny_standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import smithy_dafny_standard_library.internaldafny.generated.Math as Math
import smithy_dafny_standard_library.internaldafny.generated.Seq as Seq
import smithy_dafny_standard_library.internaldafny.generated.Unicode as Unicode
import smithy_dafny_standard_library.internaldafny.generated.Functions as Functions
import smithy_dafny_standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import smithy_dafny_standard_library.internaldafny.generated.FileIO as FileIO
import smithy_dafny_standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import smithy_dafny_standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.MulInternals as MulInternals
import smithy_dafny_standard_library.internaldafny.generated.Mul as Mul
import smithy_dafny_standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.ModInternals as ModInternals
import smithy_dafny_standard_library.internaldafny.generated.DivInternals as DivInternals
import smithy_dafny_standard_library.internaldafny.generated.DivMod as DivMod
import smithy_dafny_standard_library.internaldafny.generated.Power as Power
import smithy_dafny_standard_library.internaldafny.generated.Logarithm as Logarithm
import smithy_dafny_standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import smithy_dafny_standard_library.internaldafny.generated.UUID as UUID
import smithy_dafny_standard_library.internaldafny.generated.OsLang as OsLang
import smithy_dafny_standard_library.internaldafny.generated.Time as Time
import smithy_dafny_standard_library.internaldafny.generated.Streams as Streams
import smithy_dafny_standard_library.internaldafny.generated.Sorting as Sorting
import smithy_dafny_standard_library.internaldafny.generated.SortedSets as SortedSets
import smithy_dafny_standard_library.internaldafny.generated.HexStrings as HexStrings
import smithy_dafny_standard_library.internaldafny.generated.GetOpt as GetOpt
import smithy_dafny_standard_library.internaldafny.generated.FloatCompare as FloatCompare
import smithy_dafny_standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import smithy_dafny_standard_library.internaldafny.generated.Base64 as Base64
import smithy_dafny_standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import smithy_dafny_standard_library.internaldafny.generated.Actions as Actions
import smithy_dafny_standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_material_providers.internaldafny.generated.KeyStoreErrorMessages as KeyStoreErrorMessages
import aws_cryptographic_material_providers.internaldafny.generated.KmsArn as KmsArn
import aws_cryptographic_material_providers.internaldafny.generated.Structure as Structure
import aws_cryptographic_material_providers.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_material_providers.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_material_providers.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_material_providers.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable
import aws_cryptographic_material_providers.internaldafny.generated.GetKeys as GetKeys
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import aws_cryptography_internal_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import aws_cryptography_internal_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import aws_cryptographic_material_providers.internaldafny.generated.KeyStore as KeyStore
import aws_cryptographic_material_providers.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_material_providers.internaldafny.generated.Materials as Materials
import aws_cryptographic_material_providers.internaldafny.generated.Keyring as Keyring
import aws_cryptographic_material_providers.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique

# Module: Constants

class default__:
    def  __init__(self):
        pass

    @_dafny.classproperty
    def ECDH__PROVIDER__INFO__RPL__INDEX(instance):
        return 1
    @_dafny.classproperty
    def ECDH__PROVIDER__INFO__PUBLIC__KEY__LEN(instance):
        return 4
    @_dafny.classproperty
    def ECDH__PROVIDER__INFO__RPK__INDEX(instance):
        return (default__.ECDH__PROVIDER__INFO__RPL__INDEX) + (default__.ECDH__PROVIDER__INFO__PUBLIC__KEY__LEN)
    @_dafny.classproperty
    def ECDH__AES__256__ENC__KEY__LENGTH(instance):
        return 32
    @_dafny.classproperty
    def ECDH__AES__256__ENC__TAG__LENGTH(instance):
        return 16
    @_dafny.classproperty
    def ECDH__AES__256__ENC__IV__LENGTH(instance):
        return 12
    @_dafny.classproperty
    def ECDH__AES__256__ENC__ALG(instance):
        return AwsCryptographyPrimitivesTypes.AES__GCM_AES__GCM(default__.ECDH__AES__256__ENC__KEY__LENGTH, default__.ECDH__AES__256__ENC__TAG__LENGTH, default__.ECDH__AES__256__ENC__IV__LENGTH)
    @_dafny.classproperty
    def PROVIDER__ID(instance):
        d_0_s_ = _dafny.Seq([97, 119, 115, 45, 107, 109, 115])
        return d_0_s_
    @_dafny.classproperty
    def UINT32__TO__SEQ__LEN(instance):
        return 4
    @_dafny.classproperty
    def KDF__SALT__LEN(instance):
        return 32
    @_dafny.classproperty
    def KDF__EXPECTED__LEN(instance):
        return 64
    @_dafny.classproperty
    def ECDH__COMMITMENT__KEY__LENGTH(instance):
        return 32
    @_dafny.classproperty
    def ECDH__COMMITMENT__KEY__INDEX(instance):
        return 32
    @_dafny.classproperty
    def ECDH__WRAPPED__KEY__MATERIAL__INDEX(instance):
        return 64
    @_dafny.classproperty
    def ECDH__KDF__STRING(instance):
        return _dafny.Seq("ecdh-key-derivation")
    @_dafny.classproperty
    def ECDH__KDF__PRF__STRING(instance):
        return _dafny.Seq("HMAC_SHA384")
    @_dafny.classproperty
    def ECDH__KDF__DELIMETER(instance):
        return _dafny.Seq([0])
    @_dafny.classproperty
    def ECDH__PROVIDER__INFO__256__LEN(instance):
        return 75
    @_dafny.classproperty
    def ECDH__PROVIDER__INFO__384__LEN(instance):
        return 107
    @_dafny.classproperty
    def ECDH__PROVIDER__INFO__521__LEN(instance):
        return 143
    @_dafny.classproperty
    def ECDH__PUBLIC__KEY__LEN__ECC__NIST__256(instance):
        return 91
    @_dafny.classproperty
    def ECDH__PUBLIC__KEY__LEN__ECC__NIST__384(instance):
        return 120
    @_dafny.classproperty
    def ECDH__PUBLIC__KEY__LEN__ECC__NIST__521(instance):
        return 158
    @_dafny.classproperty
    def ECDH__PUBLIC__KEY__COMPRESSED__LEN__ECC__NIST__256(instance):
        return 33
    @_dafny.classproperty
    def ECDH__PUBLIC__KEY__COMPRESSED__LEN__ECC__NIST__384(instance):
        return 49
    @_dafny.classproperty
    def ECDH__PUBLIC__KEY__COMPRESSED__LEN__ECC__NIST__521(instance):
        return 67
    @_dafny.classproperty
    def CIPHERTEXT__WRAPPED__MATERIAL__INDEX(instance):
        return 68
    @_dafny.classproperty
    def PROVIDER__ID__HIERARCHY(instance):
        d_0_s_ = _dafny.Seq([97, 119, 115, 45, 107, 109, 115, 45, 104, 105, 101, 114, 97, 114, 99, 104, 121])
        return d_0_s_
    @_dafny.classproperty
    def RSA__PROVIDER__ID(instance):
        d_0_s_ = _dafny.Seq([97, 119, 115, 45, 107, 109, 115, 45, 114, 115, 97])
        return d_0_s_
    @_dafny.classproperty
    def KMS__ECDH__PROVIDER__ID(instance):
        return UTF8.default__.EncodeAscii(_dafny.Seq("aws-kms-ecdh"))
    @_dafny.classproperty
    def RAW__ECDH__PROVIDER__ID(instance):
        return UTF8.default__.EncodeAscii(_dafny.Seq("raw-ecdh"))
    @_dafny.classproperty
    def ECDH__KDF__PRF__NAME(instance):
        return UTF8.default__.EncodeAscii(_dafny.Seq("HMAC_SHA384"))
    @_dafny.classproperty
    def ECDH__KDF__UTF8(instance):
        return UTF8.default__.EncodeAscii(_dafny.Seq("ecdh-key-derivation"))

class AwsKmsEncryptedDataKey:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return AwsCryptographyMaterialProvidersTypes.EncryptedDataKey.default()()
    def _Is(source__):
        d_0_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey = source__
        return (((d_0_edk_).keyProviderId) == (default__.PROVIDER__ID)) and (UTF8.default__.ValidUTF8Seq((d_0_edk_).keyProviderInfo))

class AwsKmsEdkHelper:
    @classmethod
    def default(cls, ):
        return lambda: AwsKmsEdkHelper_AwsKmsEdkHelper(AwsCryptographyMaterialProvidersTypes.EncryptedDataKey.default()(), AwsArnParsing.AwsArn.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AwsKmsEdkHelper(self) -> bool:
        return isinstance(self, AwsKmsEdkHelper_AwsKmsEdkHelper)

class AwsKmsEdkHelper_AwsKmsEdkHelper(AwsKmsEdkHelper, NamedTuple('AwsKmsEdkHelper', [('edk', Any), ('arn', Any)])):
    def __dafnystr__(self) -> str:
        return f'Constants.AwsKmsEdkHelper.AwsKmsEdkHelper({_dafny.string_of(self.edk)}, {_dafny.string_of(self.arn)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AwsKmsEdkHelper_AwsKmsEdkHelper) and self.edk == __o.edk and self.arn == __o.arn
    def __hash__(self) -> int:
        return super().__hash__()

