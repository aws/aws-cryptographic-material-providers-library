import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.module_ as module_
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
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import smithy_dafny_standard_library.internaldafny.generated.Base64 as Base64
import aws_cryptographic_material_providers.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_material_providers.internaldafny.generated.Materials as Materials
import aws_cryptographic_material_providers.internaldafny.generated.Keyring as Keyring
import smithy_dafny_standard_library.internaldafny.generated.Relations as Relations
import smithy_dafny_standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import smithy_dafny_standard_library.internaldafny.generated.Math as Math
import smithy_dafny_standard_library.internaldafny.generated.Seq as Seq
import aws_cryptographic_material_providers.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import smithy_dafny_standard_library.internaldafny.generated.Actions as Actions
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_material_providers.internaldafny.generated.Constants as Constants
import smithy_dafny_standard_library.internaldafny.generated.UUID as UUID
import aws_cryptographic_material_providers.internaldafny.generated.MaterialWrapping as MaterialWrapping
import smithy_dafny_standard_library.internaldafny.generated.SortedSets as SortedSets
import aws_cryptographic_material_providers.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_material_providers.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_material_providers.internaldafny.generated.EdkWrapping as EdkWrapping
import aws_cryptographic_material_providers.internaldafny.generated.ErrorMessages as ErrorMessages
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsKeyring as AwsKmsKeyring
import aws_cryptographic_material_providers.internaldafny.generated.StrictMultiKeyring as StrictMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsDiscoveryKeyring as AwsKmsDiscoveryKeyring
import aws_cryptography_internal_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import aws_cryptography_internal_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import aws_cryptographic_material_providers.internaldafny.generated.DiscoveryMultiKeyring as DiscoveryMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkDiscoveryKeyring as AwsKmsMrkDiscoveryKeyring
import aws_cryptographic_material_providers.internaldafny.generated.MrkAwareDiscoveryMultiKeyring as MrkAwareDiscoveryMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkKeyring as AwsKmsMrkKeyring
import aws_cryptographic_material_providers.internaldafny.generated.MrkAwareStrictMultiKeyring as MrkAwareStrictMultiKeyring
import smithy_dafny_standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import smithy_dafny_standard_library.internaldafny.generated.OsLang as OsLang
import smithy_dafny_standard_library.internaldafny.generated.Time as Time
import aws_cryptographic_material_providers.internaldafny.generated.LocalCMC as LocalCMC
import aws_cryptographic_material_providers.internaldafny.generated.SynchronizedLocalCMC as SynchronizedLocalCMC
import aws_cryptographic_material_providers.internaldafny.generated.StormTracker as StormTracker
import aws_cryptographic_material_providers.internaldafny.generated.StormTrackingCMC as StormTrackingCMC
import aws_cryptographic_material_providers.internaldafny.generated.CacheConstants as CacheConstants
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsHierarchicalKeyring as AwsKmsHierarchicalKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsRsaKeyring as AwsKmsRsaKeyring
import aws_cryptographic_material_providers.internaldafny.generated.EcdhEdkWrapping as EcdhEdkWrapping
import aws_cryptographic_material_providers.internaldafny.generated.RawECDHKeyring as RawECDHKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsEcdhKeyring as AwsKmsEcdhKeyring
import aws_cryptographic_material_providers.internaldafny.generated.RawAESKeyring as RawAESKeyring
import aws_cryptographic_material_providers.internaldafny.generated.RawRSAKeyring as RawRSAKeyring
import aws_cryptographic_material_providers.internaldafny.generated.CMM as CMM
import aws_cryptographic_material_providers.internaldafny.generated.Defaults as Defaults
import aws_cryptographic_material_providers.internaldafny.generated.Commitment as Commitment
import aws_cryptographic_material_providers.internaldafny.generated.DefaultCMM as DefaultCMM
import aws_cryptographic_material_providers.internaldafny.generated.DefaultClientSupplier as DefaultClientSupplier
import aws_cryptographic_material_providers.internaldafny.generated.Utils as Utils
import aws_cryptographic_material_providers.internaldafny.generated.RequiredEncryptionContextCMM as RequiredEncryptionContextCMM
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersOperations as AwsCryptographyMaterialProvidersOperations
import aws_cryptographic_material_providers.internaldafny.generated.MaterialProviders as MaterialProviders
import aws_cryptographic_material_providers.internaldafny.generated.KeyStoreErrorMessages as KeyStoreErrorMessages
import aws_cryptographic_material_providers.internaldafny.generated.KmsArn as KmsArn
import aws_cryptographic_material_providers.internaldafny.generated.Structure as Structure
import aws_cryptographic_material_providers.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_material_providers.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_material_providers.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_material_providers.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable
import aws_cryptographic_material_providers.internaldafny.generated.GetKeys as GetKeys
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import aws_cryptographic_material_providers.internaldafny.generated.KeyStore as KeyStore
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
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
import smithy_dafny_standard_library.internaldafny.generated.Streams as Streams
import smithy_dafny_standard_library.internaldafny.generated.Sorting as Sorting
import smithy_dafny_standard_library.internaldafny.generated.HexStrings as HexStrings
import smithy_dafny_standard_library.internaldafny.generated.GetOpt as GetOpt
import smithy_dafny_standard_library.internaldafny.generated.FloatCompare as FloatCompare
import smithy_dafny_standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import smithy_dafny_standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.MplManifestOptions as MplManifestOptions
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.AllAlgorithmSuites as AllAlgorithmSuites
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.WrappedMaterialProviders as WrappedMaterialProviders
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.AwsCryptographyMaterialProvidersTestVectorKeysTypes as AwsCryptographyMaterialProvidersTestVectorKeysTypes
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Views_Core as JSON_Utils_Views_Core
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Views_Writers as JSON_Utils_Views_Writers
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Lexers_Core as JSON_Utils_Lexers_Core
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Lexers_Strings as JSON_Utils_Lexers_Strings
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Cursors as JSON_Utils_Cursors
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Parsers as JSON_Utils_Parsers
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Str_CharStrConversion as JSON_Utils_Str_CharStrConversion
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Str_CharStrEscaping as JSON_Utils_Str_CharStrEscaping
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Str as JSON_Utils_Str
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Seq as JSON_Utils_Seq
import smithy_dafny_standard_library.internaldafny.generated.JSON_Utils_Vectors as JSON_Utils_Vectors
import smithy_dafny_standard_library.internaldafny.generated.JSON_Errors as JSON_Errors
import smithy_dafny_standard_library.internaldafny.generated.JSON_Values as JSON_Values
import smithy_dafny_standard_library.internaldafny.generated.JSON_Spec as JSON_Spec
import smithy_dafny_standard_library.internaldafny.generated.JSON_Grammar as JSON_Grammar
import smithy_dafny_standard_library.internaldafny.generated.JSON_Serializer_ByteStrConversion as JSON_Serializer_ByteStrConversion
import smithy_dafny_standard_library.internaldafny.generated.JSON_Serializer as JSON_Serializer
import smithy_dafny_standard_library.internaldafny.generated.JSON_Deserializer_Uint16StrConversion as JSON_Deserializer_Uint16StrConversion
import smithy_dafny_standard_library.internaldafny.generated.JSON_Deserializer_ByteStrConversion as JSON_Deserializer_ByteStrConversion
import smithy_dafny_standard_library.internaldafny.generated.JSON_Deserializer as JSON_Deserializer
import smithy_dafny_standard_library.internaldafny.generated.JSON_ConcreteSyntax_Spec as JSON_ConcreteSyntax_Spec
import smithy_dafny_standard_library.internaldafny.generated.JSON_ConcreteSyntax_SpecProperties as JSON_ConcreteSyntax_SpecProperties
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Serializer as JSON_ZeroCopy_Serializer
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Core as JSON_ZeroCopy_Deserializer_Core
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Strings as JSON_ZeroCopy_Deserializer_Strings
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Numbers as JSON_ZeroCopy_Deserializer_Numbers
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_ObjectParams as JSON_ZeroCopy_Deserializer_ObjectParams
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Objects as JSON_ZeroCopy_Deserializer_Objects
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_ArrayParams as JSON_ZeroCopy_Deserializer_ArrayParams
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Arrays as JSON_ZeroCopy_Deserializer_Arrays
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Constants as JSON_ZeroCopy_Deserializer_Constants
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_Values as JSON_ZeroCopy_Deserializer_Values
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer_API as JSON_ZeroCopy_Deserializer_API
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_Deserializer as JSON_ZeroCopy_Deserializer
import smithy_dafny_standard_library.internaldafny.generated.JSON_ZeroCopy_API as JSON_ZeroCopy_API
import smithy_dafny_standard_library.internaldafny.generated.JSON_API as JSON_API
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.JSONHelpers as JSONHelpers
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.KeyDescription as KeyDescription
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.KeyMaterial as KeyMaterial
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.CreateStaticKeyrings as CreateStaticKeyrings
import aws_cryptography_materialproviders_test_vectors.internaldafny.generated.CreateStaticKeyStores as CreateStaticKeyStores

# Module: KeyringFromKeyDescription

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def GetKeyId(input):
        while True:
            with _dafny.label():
                source0_ = input
                if True:
                    if source0_.is_Kms:
                        d_0_i_ = source0_.Kms
                        return (d_0_i_).keyId
                if True:
                    if source0_.is_KmsMrk:
                        d_1_i_ = source0_.KmsMrk
                        return (d_1_i_).keyId
                if True:
                    if source0_.is_KmsMrkDiscovery:
                        d_2_i_ = source0_.KmsMrkDiscovery
                        return (d_2_i_).keyId
                if True:
                    if source0_.is_RSA:
                        d_3_i_ = source0_.RSA
                        return (d_3_i_).keyId
                if True:
                    if source0_.is_AES:
                        d_4_i_ = source0_.AES
                        return (d_4_i_).keyId
                if True:
                    if source0_.is_ECDH:
                        d_5_i_ = source0_.ECDH
                        return (d_5_i_).senderKeyId
                if True:
                    if source0_.is_KmsECDH:
                        d_6_i_ = source0_.KmsECDH
                        return (d_6_i_).senderKeyId
                if True:
                    if source0_.is_Static:
                        d_7_i_ = source0_.Static
                        return (d_7_i_).keyId
                if True:
                    if source0_.is_Hierarchy:
                        d_8_i_ = source0_.Hierarchy
                        return (d_8_i_).keyId
                if True:
                    if source0_.is_KmsRsa:
                        d_9_i_ = source0_.KmsRsa
                        return (d_9_i_).keyId
                if True:
                    if source0_.is_RequiredEncryptionContext:
                        d_10_i_ = source0_.RequiredEncryptionContext
                        in0_ = (d_10_i_).underlying
                        input = in0_
                        raise _dafny.TailCall()
                if True:
                    return _dafny.Seq("")
                break

    @staticmethod
    def GetSenderKeyId(input):
        source0_ = input
        if True:
            if source0_.is_ECDH:
                d_0_i_ = source0_.ECDH
                return (d_0_i_).senderKeyId
        if True:
            return _dafny.Seq("")

    @staticmethod
    def GetRecipientKeyId(input):
        source0_ = input
        if True:
            if source0_.is_ECDH:
                d_0_i_ = source0_.ECDH
                return (d_0_i_).recipientKeyId
        if True:
            if source0_.is_KmsECDH:
                d_1_i_ = source0_.KmsECDH
                return (d_1_i_).recipientKeyId
        if True:
            return _dafny.Seq("")

    @staticmethod
    def GetKeyMaterial(keys, keyDescription):
        d_0_keyId_ = default__.GetKeyId(keyDescription)
        if (d_0_keyId_) in (keys):
            return Wrappers.Option_Some((keys)[d_0_keyId_])
        elif True:
            return Wrappers.Option_None()

    @staticmethod
    def GetSenderKeyMaterial(keys, keyDescription):
        d_0_keyId_ = default__.GetSenderKeyId(keyDescription)
        if (d_0_keyId_) in (keys):
            return Wrappers.Option_Some((keys)[d_0_keyId_])
        elif True:
            return Wrappers.Option_None()

    @staticmethod
    def GetRecipientKeyMaterial(keys, keyDescription):
        d_0_keyId_ = default__.GetRecipientKeyId(keyDescription)
        if (d_0_keyId_) in (keys):
            return Wrappers.Option_Some((keys)[d_0_keyId_])
        elif True:
            return Wrappers.Option_None()

    @staticmethod
    def ToKeyring(mpl, keys, description):
        output: Wrappers.Result = None
        d_0_material_: Wrappers.Option
        d_0_material_ = default__.GetKeyMaterial(keys, description)
        source0_ = description
        with _dafny.label("match0"):
            if True:
                if source0_.is_Static:
                    Static0 = source0_.Static
                    d_1_key_ = Static0.keyId
                    if True:
                        d_2_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
                        d_2_valueOrError0_ = Wrappers.default__.Need(((d_0_material_).is_Some) and (((d_0_material_).value).is_StaticMaterial), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not type: StaticMaterial")))
                        if (d_2_valueOrError0_).IsFailure():
                            output = (d_2_valueOrError0_).PropagateFailure()
                            return output
                        d_3_encrypt_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
                        d_3_encrypt_ = AwsCryptographyMaterialProvidersTypes.EncryptionMaterials_EncryptionMaterials(((d_0_material_).value).algorithmSuite, ((d_0_material_).value).encryptionContext, ((d_0_material_).value).encryptedDataKeys, ((d_0_material_).value).requiredEncryptionContextKeys, ((d_0_material_).value).plaintextDataKey, ((d_0_material_).value).signingKey, ((d_0_material_).value).symmetricSigningKeys)
                        d_4_decrypt_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
                        d_4_decrypt_ = AwsCryptographyMaterialProvidersTypes.DecryptionMaterials_DecryptionMaterials(((d_0_material_).value).algorithmSuite, ((d_0_material_).value).encryptionContext, ((d_0_material_).value).requiredEncryptionContextKeys, ((d_0_material_).value).plaintextDataKey, ((d_0_material_).value).verificationKey, Wrappers.Option_None())
                        d_5_keyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
                        out0_: AwsCryptographyMaterialProvidersTypes.IKeyring
                        out0_ = CreateStaticKeyrings.default__.CreateStaticMaterialsKeyring(d_3_encrypt_, d_4_decrypt_)
                        d_5_keyring_ = out0_
                        output = Wrappers.Result_Success(d_5_keyring_)
                        return output
                    raise _dafny.Break("match0")
            if True:
                if source0_.is_Kms:
                    Kms0 = source0_.Kms
                    d_6_key_ = Kms0.keyId
                    if True:
                        d_7_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
                        d_7_valueOrError1_ = Wrappers.default__.Need(((d_0_material_).is_Some) and (((d_0_material_).value).is_KMS), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not type: KMS")))
                        if (d_7_valueOrError1_).IsFailure():
                            output = (d_7_valueOrError1_).PropagateFailure()
                            return output
                        d_8_valueOrError2_: Wrappers.Result = None
                        out1_: Wrappers.Result
                        out1_ = default__.getKmsClient(mpl, ((d_0_material_).value).keyIdentifier)
                        d_8_valueOrError2_ = out1_
                        if (d_8_valueOrError2_).IsFailure():
                            output = (d_8_valueOrError2_).PropagateFailure()
                            return output
                        d_9_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
                        d_9_kmsClient_ = (d_8_valueOrError2_).Extract()
                        d_10_input_: AwsCryptographyMaterialProvidersTypes.CreateAwsKmsKeyringInput
                        d_10_input_ = AwsCryptographyMaterialProvidersTypes.CreateAwsKmsKeyringInput_CreateAwsKmsKeyringInput(((d_0_material_).value).keyIdentifier, d_9_kmsClient_, Wrappers.Option_None())
                        d_11_keyring_: Wrappers.Result
                        out2_: Wrappers.Result
                        out2_ = (mpl).CreateAwsKmsKeyring(d_10_input_)
                        d_11_keyring_ = out2_
                        def lambda0_(d_12_e_):
                            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_12_e_)

                        output = (d_11_keyring_).MapFailure(lambda0_)
                        return output
                    raise _dafny.Break("match0")
            if True:
                if source0_.is_KmsMrk:
                    KmsMrk0 = source0_.KmsMrk
                    d_13_key_ = KmsMrk0.keyId
                    if True:
                        d_14_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
                        d_14_valueOrError3_ = Wrappers.default__.Need(((d_0_material_).is_Some) and (((d_0_material_).value).is_KMS), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not type: KMS")))
                        if (d_14_valueOrError3_).IsFailure():
                            output = (d_14_valueOrError3_).PropagateFailure()
                            return output
                        d_15_valueOrError4_: Wrappers.Result = None
                        out3_: Wrappers.Result
                        out3_ = default__.getKmsClient(mpl, ((d_0_material_).value).keyIdentifier)
                        d_15_valueOrError4_ = out3_
                        if (d_15_valueOrError4_).IsFailure():
                            output = (d_15_valueOrError4_).PropagateFailure()
                            return output
                        d_16_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
                        d_16_kmsClient_ = (d_15_valueOrError4_).Extract()
                        d_17_input_: AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMrkKeyringInput
                        d_17_input_ = AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMrkKeyringInput_CreateAwsKmsMrkKeyringInput(((d_0_material_).value).keyIdentifier, d_16_kmsClient_, Wrappers.Option_None())
                        d_18_keyring_: Wrappers.Result
                        out4_: Wrappers.Result
                        out4_ = (mpl).CreateAwsKmsMrkKeyring(d_17_input_)
                        d_18_keyring_ = out4_
                        def lambda1_(d_19_e_):
                            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_19_e_)

                        output = (d_18_keyring_).MapFailure(lambda1_)
                        return output
                    raise _dafny.Break("match0")
            if True:
                if source0_.is_KmsRsa:
                    KmsRsa0 = source0_.KmsRsa
                    d_20_key_ = KmsRsa0.keyId
                    d_21_encryptionAlgorithm_ = KmsRsa0.encryptionAlgorithm
                    if True:
                        d_22_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome.default()()
                        d_22_valueOrError5_ = Wrappers.default__.Need(((d_0_material_).is_Some) and (((d_0_material_).value).is_KMSAsymetric), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not type: KMSAsymetric")))
                        if (d_22_valueOrError5_).IsFailure():
                            output = (d_22_valueOrError5_).PropagateFailure()
                            return output
                        d_23_valueOrError6_: Wrappers.Result = None
                        out5_: Wrappers.Result
                        out5_ = default__.getKmsClient(mpl, ((d_0_material_).value).keyIdentifier)
                        d_23_valueOrError6_ = out5_
                        if (d_23_valueOrError6_).IsFailure():
                            output = (d_23_valueOrError6_).PropagateFailure()
                            return output
                        d_24_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
                        d_24_kmsClient_ = (d_23_valueOrError6_).Extract()
                        d_25_input_: AwsCryptographyMaterialProvidersTypes.CreateAwsKmsRsaKeyringInput
                        d_25_input_ = AwsCryptographyMaterialProvidersTypes.CreateAwsKmsRsaKeyringInput_CreateAwsKmsRsaKeyringInput(Wrappers.Option_Some(((d_0_material_).value).publicKey), ((d_0_material_).value).keyIdentifier, d_21_encryptionAlgorithm_, Wrappers.Option_Some(d_24_kmsClient_), Wrappers.Option_None())
                        d_26_keyring_: Wrappers.Result
                        out6_: Wrappers.Result
                        out6_ = (mpl).CreateAwsKmsRsaKeyring(d_25_input_)
                        d_26_keyring_ = out6_
                        def lambda2_(d_27_e_):
                            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_27_e_)

                        output = (d_26_keyring_).MapFailure(lambda2_)
                        return output
                    raise _dafny.Break("match0")
            if True:
                if source0_.is_Hierarchy:
                    Hierarchy0 = source0_.Hierarchy
                    d_28_key_ = Hierarchy0.keyId
                    if True:
                        d_29_valueOrError7_: Wrappers.Outcome = Wrappers.Outcome.default()()
                        d_29_valueOrError7_ = Wrappers.default__.Need(((d_0_material_).is_Some) and (((d_0_material_).value).is_StaticKeyStoreInformation), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not type: StaticKeyStoreInformation")))
                        if (d_29_valueOrError7_).IsFailure():
                            output = (d_29_valueOrError7_).PropagateFailure()
                            return output
                        d_30_keyStore_: AwsCryptographyKeyStoreTypes.IKeyStoreClient
                        out7_: AwsCryptographyKeyStoreTypes.IKeyStoreClient
                        out7_ = CreateStaticKeyStores.default__.CreateStaticKeyStore((d_0_material_).value)
                        d_30_keyStore_ = out7_
                        d_31_input_: AwsCryptographyMaterialProvidersTypes.CreateAwsKmsHierarchicalKeyringInput
                        d_31_input_ = AwsCryptographyMaterialProvidersTypes.CreateAwsKmsHierarchicalKeyringInput_CreateAwsKmsHierarchicalKeyringInput(Wrappers.Option_Some(((d_0_material_).value).keyIdentifier), Wrappers.Option_None(), d_30_keyStore_, 11, Wrappers.Option_None(), Wrappers.Option_None())
                        d_32_keyring_: Wrappers.Result
                        out8_: Wrappers.Result
                        out8_ = (mpl).CreateAwsKmsHierarchicalKeyring(d_31_input_)
                        d_32_keyring_ = out8_
                        def lambda3_(d_33_e_):
                            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_33_e_)

                        output = (d_32_keyring_).MapFailure(lambda3_)
                        return output
                    raise _dafny.Break("match0")
            if True:
                if source0_.is_KmsMrkDiscovery:
                    KmsMrkDiscovery0 = source0_.KmsMrkDiscovery
                    d_34_defaultMrkRegion_ = KmsMrkDiscovery0.defaultMrkRegion
                    d_35_awsKmsDiscoveryFilter_ = KmsMrkDiscovery0.awsKmsDiscoveryFilter
                    if True:
                        d_36_valueOrError8_: Wrappers.Outcome = Wrappers.Outcome.default()()
                        d_36_valueOrError8_ = Wrappers.default__.Need((d_0_material_).is_None, AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Discovery has not key")))
                        if (d_36_valueOrError8_).IsFailure():
                            output = (d_36_valueOrError8_).PropagateFailure()
                            return output
                        d_37_input_: AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMrkDiscoveryMultiKeyringInput
                        d_37_input_ = AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMrkDiscoveryMultiKeyringInput_CreateAwsKmsMrkDiscoveryMultiKeyringInput(_dafny.Seq([d_34_defaultMrkRegion_]), d_35_awsKmsDiscoveryFilter_, Wrappers.Option_None(), Wrappers.Option_None())
                        d_38_keyring_: Wrappers.Result
                        out9_: Wrappers.Result
                        out9_ = (mpl).CreateAwsKmsMrkDiscoveryMultiKeyring(d_37_input_)
                        d_38_keyring_ = out9_
                        def lambda4_(d_39_e_):
                            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_39_e_)

                        output = (d_38_keyring_).MapFailure(lambda4_)
                        return output
                    raise _dafny.Break("match0")
            if True:
                if source0_.is_AES:
                    AES0 = source0_.AES
                    d_40_key_ = AES0.keyId
                    d_41_providerId_ = AES0.providerId
                    if True:
                        d_42_valueOrError9_: Wrappers.Outcome = Wrappers.Outcome.default()()
                        d_42_valueOrError9_ = Wrappers.default__.Need(((d_0_material_).is_Some) and (((d_0_material_).value).is_Symetric), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not type: Symmetric")))
                        if (d_42_valueOrError9_).IsFailure():
                            output = (d_42_valueOrError9_).PropagateFailure()
                            return output
                        d_43_valueOrError10_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyMaterialProvidersTypes.AesWrappingAlg.default())()
                        source1_ = ((d_0_material_).value).bits
                        with _dafny.label("match1"):
                            if True:
                                if (source1_) == (128):
                                    d_43_valueOrError10_ = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES128__GCM__IV12__TAG16())
                                    raise _dafny.Break("match1")
                            if True:
                                if (source1_) == (192):
                                    d_43_valueOrError10_ = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES192__GCM__IV12__TAG16())
                                    raise _dafny.Break("match1")
                            if True:
                                if (source1_) == (256):
                                    d_43_valueOrError10_ = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16())
                                    raise _dafny.Break("match1")
                            if True:
                                d_43_valueOrError10_ = Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not a supported bit length")))
                            pass
                        if (d_43_valueOrError10_).IsFailure():
                            output = (d_43_valueOrError10_).PropagateFailure()
                            return output
                        d_44_wrappingAlg_: AwsCryptographyMaterialProvidersTypes.AesWrappingAlg
                        d_44_wrappingAlg_ = (d_43_valueOrError10_).Extract()
                        d_45_input_: AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput
                        d_45_input_ = AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_41_providerId_, ((d_0_material_).value).keyIdentifier, ((d_0_material_).value).wrappingKey, d_44_wrappingAlg_)
                        d_46_keyring_: Wrappers.Result
                        out10_: Wrappers.Result
                        out10_ = (mpl).CreateRawAesKeyring(d_45_input_)
                        d_46_keyring_ = out10_
                        def lambda5_(d_47_e_):
                            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_47_e_)

                        output = (d_46_keyring_).MapFailure(lambda5_)
                        return output
                    raise _dafny.Break("match0")
            if True:
                if source0_.is_RSA:
                    RSA0 = source0_.RSA
                    d_48_key_ = RSA0.keyId
                    d_49_providerId_ = RSA0.providerId
                    d_50_padding_ = RSA0.padding
                    if True:
                        d_51_valueOrError11_: Wrappers.Outcome = Wrappers.Outcome.default()()
                        d_51_valueOrError11_ = Wrappers.default__.Need(((d_0_material_).is_Some) and ((((d_0_material_).value).is_PrivateRSA) or (((d_0_material_).value).is_PublicRSA)), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not type: PrivateRSA or PublicRSA")))
                        if (d_51_valueOrError11_).IsFailure():
                            output = (d_51_valueOrError11_).PropagateFailure()
                            return output
                        source2_ = d_0_material_
                        with _dafny.label("match2"):
                            if True:
                                if source2_.is_Some:
                                    value0 = source2_.value
                                    if value0.is_PrivateRSA:
                                        d_52_decrypt_ = value0.decrypt
                                        d_53_material_ = value0.material
                                        d_54_keyIdentifier_ = value0.keyIdentifier
                                        if True:
                                            d_55_valueOrError12_: Wrappers.Outcome = Wrappers.Outcome.default()()
                                            d_55_valueOrError12_ = Wrappers.default__.Need(d_52_decrypt_, AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Private RSA keys only supports decrypt.")))
                                            if (d_55_valueOrError12_).IsFailure():
                                                output = (d_55_valueOrError12_).PropagateFailure()
                                                return output
                                            d_56_valueOrError13_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
                                            def lambda6_(d_57_e_):
                                                return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(d_57_e_)

                                            d_56_valueOrError13_ = (UTF8.default__.Encode(d_53_material_)).MapFailure(lambda6_)
                                            if (d_56_valueOrError13_).IsFailure():
                                                output = (d_56_valueOrError13_).PropagateFailure()
                                                return output
                                            d_58_privateKeyPemBytes_: _dafny.Seq
                                            d_58_privateKeyPemBytes_ = (d_56_valueOrError13_).Extract()
                                            d_59_input_: AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput
                                            d_59_input_ = AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_49_providerId_, d_54_keyIdentifier_, d_50_padding_, Wrappers.Option_None(), Wrappers.Option_Some(d_58_privateKeyPemBytes_))
                                            d_60_keyring_: Wrappers.Result
                                            out11_: Wrappers.Result
                                            out11_ = (mpl).CreateRawRsaKeyring(d_59_input_)
                                            d_60_keyring_ = out11_
                                            def lambda7_(d_61_e_):
                                                return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_61_e_)

                                            output = (d_60_keyring_).MapFailure(lambda7_)
                                            return output
                                        raise _dafny.Break("match2")
                            if True:
                                value1 = source2_.value
                                d_62_encrypt_ = value1.encrypt
                                d_63_material_ = value1.material
                                d_64_keyIdentifier_ = value1.keyIdentifier
                                if True:
                                    d_65_valueOrError14_: Wrappers.Outcome = Wrappers.Outcome.default()()
                                    d_65_valueOrError14_ = Wrappers.default__.Need(d_62_encrypt_, AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Public RSA keys only supports encrypt.")))
                                    if (d_65_valueOrError14_).IsFailure():
                                        output = (d_65_valueOrError14_).PropagateFailure()
                                        return output
                                    d_66_valueOrError15_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
                                    def lambda8_(d_67_e_):
                                        return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(d_67_e_)

                                    d_66_valueOrError15_ = (UTF8.default__.Encode(d_63_material_)).MapFailure(lambda8_)
                                    if (d_66_valueOrError15_).IsFailure():
                                        output = (d_66_valueOrError15_).PropagateFailure()
                                        return output
                                    d_68_publicKeyPemBytes_: _dafny.Seq
                                    d_68_publicKeyPemBytes_ = (d_66_valueOrError15_).Extract()
                                    d_69_input_: AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput
                                    d_69_input_ = AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_49_providerId_, d_64_keyIdentifier_, d_50_padding_, Wrappers.Option_Some(d_68_publicKeyPemBytes_), Wrappers.Option_None())
                                    d_70_keyring_: Wrappers.Result
                                    out12_: Wrappers.Result
                                    out12_ = (mpl).CreateRawRsaKeyring(d_69_input_)
                                    d_70_keyring_ = out12_
                                    def lambda9_(d_71_e_):
                                        return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_71_e_)

                                    output = (d_70_keyring_).MapFailure(lambda9_)
                                    return output
                            pass
                    raise _dafny.Break("match0")
            if True:
                if source0_.is_ECDH:
                    ECDH0 = source0_.ECDH
                    d_72_senderKeyId_ = ECDH0.senderKeyId
                    d_73_recipientKeyId_ = ECDH0.recipientKeyId
                    d_74_senderPublicKey_ = ECDH0.senderPublicKey
                    d_75_recipientPublicKey_ = ECDH0.recipientPublicKey
                    d_76_providerId_ = ECDH0.providerId
                    d_77_curveSpec_ = ECDH0.curveSpec
                    d_78_keyAgreementScheme_ = ECDH0.keyAgreementScheme
                    if True:
                        d_79_valueOrError16_: Wrappers.Outcome = Wrappers.Outcome.default()()
                        d_79_valueOrError16_ = Wrappers.default__.Need((d_77_curveSpec_) in (KeyDescription.default__.Curve2EccAlgorithmSpec), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Unknown curve spec")))
                        if (d_79_valueOrError16_).IsFailure():
                            output = (d_79_valueOrError16_).PropagateFailure()
                            return output
                        d_80_curveType_: AwsCryptographyPrimitivesTypes.ECDHCurveSpec
                        d_80_curveType_ = (KeyDescription.default__.Curve2EccAlgorithmSpec)[d_77_curveSpec_]
                        d_81_primitives_q_: Wrappers.Result
                        out13_: Wrappers.Result
                        out13_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
                        d_81_primitives_q_ = out13_
                        d_82_valueOrError17_: Wrappers.Result = None
                        def lambda10_(d_83_e_):
                            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Unable to create primitives client"))

                        d_82_valueOrError17_ = (d_81_primitives_q_).MapFailure(lambda10_)
                        if (d_82_valueOrError17_).IsFailure():
                            output = (d_82_valueOrError17_).PropagateFailure()
                            return output
                        d_84_primitives_: AtomicPrimitives.AtomicPrimitivesClient
                        d_84_primitives_ = (d_82_valueOrError17_).Extract()
                        source3_ = d_78_keyAgreementScheme_
                        with _dafny.label("match3"):
                            if True:
                                if (source3_) == (_dafny.Seq("static")):
                                    if True:
                                        d_85_valueOrError18_: Wrappers.Outcome = Wrappers.Outcome.default()()
                                        d_85_valueOrError18_ = Wrappers.default__.Need(((d_0_material_).is_Some) and (((d_0_material_).value).is_PrivateECDH), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not type: PrivateECDH")))
                                        if (d_85_valueOrError18_).IsFailure():
                                            output = (d_85_valueOrError18_).PropagateFailure()
                                            return output
                                        d_86_valueOrError19_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
                                        def lambda11_(d_87_e_):
                                            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(d_87_e_)

                                        d_86_valueOrError19_ = (UTF8.default__.Encode(((d_0_material_).value).senderMaterial)).MapFailure(lambda11_)
                                        if (d_86_valueOrError19_).IsFailure():
                                            output = (d_86_valueOrError19_).PropagateFailure()
                                            return output
                                        d_88_senderMaterial_: _dafny.Seq
                                        d_88_senderMaterial_ = (d_86_valueOrError19_).Extract()
                                        d_89_valueOrError20_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
                                        def lambda12_(d_90_e_):
                                            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(d_90_e_)

                                        d_89_valueOrError20_ = (UTF8.default__.Encode(((d_0_material_).value).recipientMaterial)).MapFailure(lambda12_)
                                        if (d_89_valueOrError20_).IsFailure():
                                            output = (d_89_valueOrError20_).PropagateFailure()
                                            return output
                                        d_91_recipientMaterial_: _dafny.Seq
                                        d_91_recipientMaterial_ = (d_89_valueOrError20_).Extract()
                                        d_92_valueOrError21_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
                                        def lambda13_(d_93_e_):
                                            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(d_93_e_)

                                        d_92_valueOrError21_ = (Base64.default__.Decode(((d_0_material_).value).recipientPublicKey)).MapFailure(lambda13_)
                                        if (d_92_valueOrError21_).IsFailure():
                                            output = (d_92_valueOrError21_).PropagateFailure()
                                            return output
                                        d_94_recipientPublicKey_: _dafny.Seq
                                        d_94_recipientPublicKey_ = (d_92_valueOrError21_).Extract()
                                        d_95_schema_: AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations
                                        d_95_schema_ = AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_88_senderMaterial_, d_94_recipientPublicKey_))
                                        d_96_input_: AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput
                                        d_96_input_ = AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(d_95_schema_, d_80_curveType_)
                                        d_97_keyring_: Wrappers.Result
                                        out14_: Wrappers.Result
                                        out14_ = (mpl).CreateRawEcdhKeyring(d_96_input_)
                                        d_97_keyring_ = out14_
                                        def lambda14_(d_98_e_):
                                            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_98_e_)

                                        output = (d_97_keyring_).MapFailure(lambda14_)
                                        return output
                                    raise _dafny.Break("match3")
                            if True:
                                if (source3_) == (_dafny.Seq("ephemeral")):
                                    if True:
                                        d_99_recipientMaterial_q_: Wrappers.Option
                                        d_99_recipientMaterial_q_ = default__.GetRecipientKeyMaterial(keys, description)
                                        d_100_valueOrError22_: Wrappers.Outcome = Wrappers.Outcome.default()()
                                        d_100_valueOrError22_ = Wrappers.default__.Need(((d_99_recipientMaterial_q_).is_Some) and (((d_99_recipientMaterial_q_).value).is_PrivateECDH), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not type: PrivateECDH")))
                                        if (d_100_valueOrError22_).IsFailure():
                                            output = (d_100_valueOrError22_).PropagateFailure()
                                            return output
                                        d_101_valueOrError23_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
                                        def lambda15_(d_102_e_):
                                            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(d_102_e_)

                                        d_101_valueOrError23_ = (UTF8.default__.Encode(((d_99_recipientMaterial_q_).value).recipientMaterial)).MapFailure(lambda15_)
                                        if (d_101_valueOrError23_).IsFailure():
                                            output = (d_101_valueOrError23_).PropagateFailure()
                                            return output
                                        d_103_recipientMaterial_: _dafny.Seq
                                        d_103_recipientMaterial_ = (d_101_valueOrError23_).Extract()
                                        d_104_valueOrError24_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
                                        def lambda16_(d_105_e_):
                                            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(d_105_e_)

                                        d_104_valueOrError24_ = (Base64.default__.Decode(((d_99_recipientMaterial_q_).value).recipientPublicKey)).MapFailure(lambda16_)
                                        if (d_104_valueOrError24_).IsFailure():
                                            output = (d_104_valueOrError24_).PropagateFailure()
                                            return output
                                        d_106_recipientPublicKey_: _dafny.Seq
                                        d_106_recipientPublicKey_ = (d_104_valueOrError24_).Extract()
                                        d_107_schema_: AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations
                                        d_107_schema_ = AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_EphemeralPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.EphemeralPrivateKeyToStaticPublicKeyInput_EphemeralPrivateKeyToStaticPublicKeyInput(d_106_recipientPublicKey_))
                                        d_108_input_: AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput
                                        d_108_input_ = AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(d_107_schema_, d_80_curveType_)
                                        d_109_keyring_: Wrappers.Result
                                        out15_: Wrappers.Result
                                        out15_ = (mpl).CreateRawEcdhKeyring(d_108_input_)
                                        d_109_keyring_ = out15_
                                        def lambda17_(d_110_e_):
                                            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_110_e_)

                                        output = (d_109_keyring_).MapFailure(lambda17_)
                                        return output
                                    raise _dafny.Break("match3")
                            if True:
                                if (source3_) == (_dafny.Seq("discovery")):
                                    if True:
                                        d_111_recipientMaterial_q_: Wrappers.Option
                                        d_111_recipientMaterial_q_ = default__.GetRecipientKeyMaterial(keys, description)
                                        d_112_valueOrError25_: Wrappers.Outcome = Wrappers.Outcome.default()()
                                        d_112_valueOrError25_ = Wrappers.default__.Need(((d_111_recipientMaterial_q_).is_Some) and (((d_111_recipientMaterial_q_).value).is_PrivateECDH), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not type: PrivateECDH")))
                                        if (d_112_valueOrError25_).IsFailure():
                                            output = (d_112_valueOrError25_).PropagateFailure()
                                            return output
                                        d_113_valueOrError26_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
                                        def lambda18_(d_114_e_):
                                            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(d_114_e_)

                                        d_113_valueOrError26_ = (UTF8.default__.Encode(((d_111_recipientMaterial_q_).value).recipientMaterial)).MapFailure(lambda18_)
                                        if (d_113_valueOrError26_).IsFailure():
                                            output = (d_113_valueOrError26_).PropagateFailure()
                                            return output
                                        d_115_recipientMaterial_: _dafny.Seq
                                        d_115_recipientMaterial_ = (d_113_valueOrError26_).Extract()
                                        d_116_schema_: AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations
                                        d_116_schema_ = AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_PublicKeyDiscovery(AwsCryptographyMaterialProvidersTypes.PublicKeyDiscoveryInput_PublicKeyDiscoveryInput(d_115_recipientMaterial_))
                                        d_117_input_: AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput
                                        d_117_input_ = AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(d_116_schema_, d_80_curveType_)
                                        d_118_keyring_: Wrappers.Result
                                        out16_: Wrappers.Result
                                        out16_ = (mpl).CreateRawEcdhKeyring(d_117_input_)
                                        d_118_keyring_ = out16_
                                        def lambda19_(d_119_e_):
                                            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_119_e_)

                                        output = (d_118_keyring_).MapFailure(lambda19_)
                                        return output
                                    raise _dafny.Break("match3")
                            if True:
                                if True:
                                    output = Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("key agreement schema not recognized")))
                                    return output
                            pass
                    raise _dafny.Break("match0")
            if True:
                if source0_.is_KmsECDH:
                    KmsECDH0 = source0_.KmsECDH
                    d_120_senderKeyId_ = KmsECDH0.senderKeyId
                    d_121_recipientKeyId_ = KmsECDH0.recipientKeyId
                    d_122_senderPublicKey_ = KmsECDH0.senderPublicKey
                    d_123_recipientPublicKey_ = KmsECDH0.recipientPublicKey
                    d_124_curveSpec_ = KmsECDH0.curveSpec
                    d_125_keyAgreementScheme_ = KmsECDH0.keyAgreementScheme
                    if True:
                        d_126_valueOrError27_: Wrappers.Outcome = Wrappers.Outcome.default()()
                        d_126_valueOrError27_ = Wrappers.default__.Need((d_124_curveSpec_) in (KeyDescription.default__.KmsKey2EccAlgorithmSpec), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Unknown curve spec")))
                        if (d_126_valueOrError27_).IsFailure():
                            output = (d_126_valueOrError27_).PropagateFailure()
                            return output
                        d_127_curveType_: AwsCryptographyPrimitivesTypes.ECDHCurveSpec
                        d_127_curveType_ = (KeyDescription.default__.KmsKey2EccAlgorithmSpec)[d_124_curveSpec_]
                        source4_ = d_125_keyAgreementScheme_
                        with _dafny.label("match4"):
                            if True:
                                if (source4_) == (_dafny.Seq("static")):
                                    if True:
                                        d_128_valueOrError28_: Wrappers.Outcome = Wrappers.Outcome.default()()
                                        d_128_valueOrError28_ = Wrappers.default__.Need(((d_0_material_).is_Some) and (((d_0_material_).value).is_KMSEcdh), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not type: KmsEcdh")))
                                        if (d_128_valueOrError28_).IsFailure():
                                            output = (d_128_valueOrError28_).PropagateFailure()
                                            return output
                                        d_129_senderKmsKey_: _dafny.Seq
                                        d_129_senderKmsKey_ = ((d_0_material_).value).senderMaterial
                                        d_130_recipientKmsKey_: _dafny.Seq
                                        d_130_recipientKmsKey_ = ((d_0_material_).value).recipientMaterial
                                        d_131_valueOrError29_: Wrappers.Outcome = Wrappers.Outcome.default()()
                                        d_131_valueOrError29_ = Wrappers.default__.Need((ComAmazonawsKmsTypes.default__.IsValid__KeyIdType(d_129_senderKmsKey_)) and (ComAmazonawsKmsTypes.default__.IsValid__KeyIdType(d_130_recipientKmsKey_)), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not a valid Kms Key Id")))
                                        if (d_131_valueOrError29_).IsFailure():
                                            output = (d_131_valueOrError29_).PropagateFailure()
                                            return output
                                        d_132_valueOrError30_: Wrappers.Result = None
                                        out17_: Wrappers.Result
                                        out17_ = default__.getKmsClient(mpl, d_129_senderKmsKey_)
                                        d_132_valueOrError30_ = out17_
                                        if (d_132_valueOrError30_).IsFailure():
                                            output = (d_132_valueOrError30_).PropagateFailure()
                                            return output
                                        d_133_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
                                        d_133_kmsClient_ = (d_132_valueOrError30_).Extract()
                                        d_134_valueOrError31_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
                                        def lambda20_(d_135_e_):
                                            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(d_135_e_)

                                        d_134_valueOrError31_ = (Base64.default__.Decode(((d_0_material_).value).senderPublicKey)).MapFailure(lambda20_)
                                        if (d_134_valueOrError31_).IsFailure():
                                            output = (d_134_valueOrError31_).PropagateFailure()
                                            return output
                                        d_136_senderPublicKey_: _dafny.Seq
                                        d_136_senderPublicKey_ = (d_134_valueOrError31_).Extract()
                                        d_137_valueOrError32_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
                                        def lambda21_(d_138_e_):
                                            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(d_138_e_)

                                        d_137_valueOrError32_ = (Base64.default__.Decode(((d_0_material_).value).recipientPublicKey)).MapFailure(lambda21_)
                                        if (d_137_valueOrError32_).IsFailure():
                                            output = (d_137_valueOrError32_).PropagateFailure()
                                            return output
                                        d_139_recipientPublicKey_: _dafny.Seq
                                        d_139_recipientPublicKey_ = (d_137_valueOrError32_).Extract()
                                        d_140_schema_: AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations
                                        d_140_schema_ = AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_129_senderKmsKey_, Wrappers.Option_Some(d_136_senderPublicKey_), d_139_recipientPublicKey_))
                                        d_141_input_: AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput
                                        d_141_input_ = AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(d_140_schema_, d_127_curveType_, d_133_kmsClient_, Wrappers.Option_None())
                                        d_142_keyring_: Wrappers.Result
                                        out18_: Wrappers.Result
                                        out18_ = (mpl).CreateAwsKmsEcdhKeyring(d_141_input_)
                                        d_142_keyring_ = out18_
                                        def lambda22_(d_143_e_):
                                            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_143_e_)

                                        output = (d_142_keyring_).MapFailure(lambda22_)
                                        return output
                                    raise _dafny.Break("match4")
                            if True:
                                if (source4_) == (_dafny.Seq("discovery")):
                                    if True:
                                        d_144_recipientMaterial_q_: Wrappers.Option
                                        d_144_recipientMaterial_q_ = default__.GetRecipientKeyMaterial(keys, description)
                                        d_145_valueOrError33_: Wrappers.Outcome = Wrappers.Outcome.default()()
                                        d_145_valueOrError33_ = Wrappers.default__.Need(((d_144_recipientMaterial_q_).is_Some) and (((d_144_recipientMaterial_q_).value).is_KMSEcdh), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not type: KmsEcdh")))
                                        if (d_145_valueOrError33_).IsFailure():
                                            output = (d_145_valueOrError33_).PropagateFailure()
                                            return output
                                        d_146_recipientKmsKey_: _dafny.Seq
                                        d_146_recipientKmsKey_ = ((d_144_recipientMaterial_q_).value).recipientMaterial
                                        d_147_valueOrError34_: Wrappers.Result = None
                                        out19_: Wrappers.Result
                                        out19_ = default__.getKmsClient(mpl, d_146_recipientKmsKey_)
                                        d_147_valueOrError34_ = out19_
                                        if (d_147_valueOrError34_).IsFailure():
                                            output = (d_147_valueOrError34_).PropagateFailure()
                                            return output
                                        d_148_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
                                        d_148_kmsClient_ = (d_147_valueOrError34_).Extract()
                                        d_149_schema_: AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations
                                        d_149_schema_ = AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPublicKeyDiscovery(AwsCryptographyMaterialProvidersTypes.KmsPublicKeyDiscoveryInput_KmsPublicKeyDiscoveryInput(d_146_recipientKmsKey_))
                                        d_150_input_: AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput
                                        d_150_input_ = AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(d_149_schema_, d_127_curveType_, d_148_kmsClient_, Wrappers.Option_None())
                                        d_151_keyring_: Wrappers.Result
                                        out20_: Wrappers.Result
                                        out20_ = (mpl).CreateAwsKmsEcdhKeyring(d_150_input_)
                                        d_151_keyring_ = out20_
                                        def lambda23_(d_152_e_):
                                            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_152_e_)

                                        output = (d_151_keyring_).MapFailure(lambda23_)
                                        return output
                                    raise _dafny.Break("match4")
                            if True:
                                if True:
                                    output = Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("key agreement schema not recognized")))
                                    return output
                            pass
                    raise _dafny.Break("match0")
            if True:
                d_153_MultiKeyring_ = source0_.Multi
                if True:
                    d_154_generator_: Wrappers.Option
                    d_154_generator_ = Wrappers.Option_None()
                    if ((d_153_MultiKeyring_).generator).is_Some:
                        d_155_valueOrError35_: Wrappers.Outcome = Wrappers.Outcome.default()()
                        d_155_valueOrError35_ = Wrappers.default__.Need(KeyDescription.default__.Keyring_q(((d_153_MultiKeyring_).generator).value), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Only Keyring key descriptions are supported.")))
                        if (d_155_valueOrError35_).IsFailure():
                            output = (d_155_valueOrError35_).PropagateFailure()
                            return output
                        d_156_valueOrError36_: Wrappers.Result = None
                        out21_: Wrappers.Result
                        out21_ = default__.ToKeyring(mpl, keys, ((d_153_MultiKeyring_).generator).value)
                        d_156_valueOrError36_ = out21_
                        if (d_156_valueOrError36_).IsFailure():
                            output = (d_156_valueOrError36_).PropagateFailure()
                            return output
                        d_157_generator_k_: AwsCryptographyMaterialProvidersTypes.IKeyring
                        d_157_generator_k_ = (d_156_valueOrError36_).Extract()
                        d_154_generator_ = Wrappers.Option_Some(d_157_generator_k_)
                    d_158_childKeyrings_: _dafny.Seq
                    d_158_childKeyrings_ = _dafny.Seq([])
                    hi0_ = len((d_153_MultiKeyring_).childKeyrings)
                    for d_159_i_ in range(0, hi0_):
                        d_160_child_: AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription
                        d_160_child_ = ((d_153_MultiKeyring_).childKeyrings)[d_159_i_]
                        d_161_valueOrError37_: Wrappers.Outcome = Wrappers.Outcome.default()()
                        d_161_valueOrError37_ = Wrappers.default__.Need(KeyDescription.default__.Keyring_q(d_160_child_), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Only Keyring key descriptions are supported.")))
                        if (d_161_valueOrError37_).IsFailure():
                            output = (d_161_valueOrError37_).PropagateFailure()
                            return output
                        d_162_valueOrError38_: Wrappers.Result = None
                        out22_: Wrappers.Result
                        out22_ = default__.ToKeyring(mpl, keys, d_160_child_)
                        d_162_valueOrError38_ = out22_
                        if (d_162_valueOrError38_).IsFailure():
                            output = (d_162_valueOrError38_).PropagateFailure()
                            return output
                        d_163_childKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
                        d_163_childKeyring_ = (d_162_valueOrError38_).Extract()
                        d_158_childKeyrings_ = (d_158_childKeyrings_) + (_dafny.Seq([d_163_childKeyring_]))
                    d_164_input_: AwsCryptographyMaterialProvidersTypes.CreateMultiKeyringInput
                    d_164_input_ = AwsCryptographyMaterialProvidersTypes.CreateMultiKeyringInput_CreateMultiKeyringInput(d_154_generator_, d_158_childKeyrings_)
                    d_165_keyring_: Wrappers.Result
                    out23_: Wrappers.Result
                    out23_ = (mpl).CreateMultiKeyring(d_164_input_)
                    d_165_keyring_ = out23_
                    def lambda24_(d_166_e_):
                        return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_166_e_)

                    output = (d_165_keyring_).MapFailure(lambda24_)
                    return output
            pass
        return output

    @staticmethod
    def getKmsClient(mpl, maybeKmsArn):
        output: Wrappers.Result = None
        d_0_maybeClientSupplier_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = (mpl).CreateDefaultClientSupplier(AwsCryptographyMaterialProvidersTypes.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
        d_0_maybeClientSupplier_ = out0_
        d_1_valueOrError0_: Wrappers.Result = None
        def lambda0_(d_2_e_):
            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_2_e_)

        d_1_valueOrError0_ = (d_0_maybeClientSupplier_).MapFailure(lambda0_)
        if (d_1_valueOrError0_).IsFailure():
            output = (d_1_valueOrError0_).PropagateFailure()
            return output
        d_3_clientSupplier_: AwsCryptographyMaterialProvidersTypes.IClientSupplier
        d_3_clientSupplier_ = (d_1_valueOrError0_).Extract()
        d_4_arn_: Wrappers.Result
        d_4_arn_ = AwsArnParsing.default__.IsAwsKmsIdentifierString(maybeKmsArn)
        d_5_region_: Wrappers.Option
        if (d_4_arn_).is_Success:
            d_5_region_ = AwsArnParsing.default__.GetRegion((d_4_arn_).value)
        elif True:
            d_5_region_ = Wrappers.Option_None()
        d_6_tmp_: Wrappers.Result
        out1_: Wrappers.Result
        out1_ = (d_3_clientSupplier_).GetClient(AwsCryptographyMaterialProvidersTypes.GetClientInput_GetClientInput((d_5_region_).UnwrapOr(_dafny.Seq(""))))
        d_6_tmp_ = out1_
        def lambda1_(d_7_e_):
            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_7_e_)

        output = (d_6_tmp_).MapFailure(lambda1_)
        return output

    @staticmethod
    def GetEcdhPublicKey(client, awsKmsKey):
        res: Wrappers.Result = None
        d_0_getPublicKeyRequest_: ComAmazonawsKmsTypes.GetPublicKeyRequest
        d_0_getPublicKeyRequest_ = ComAmazonawsKmsTypes.GetPublicKeyRequest_GetPublicKeyRequest(awsKmsKey, Wrappers.Option_None())
        d_1_maybePublicKeyResponse_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = (client).GetPublicKey(d_0_getPublicKeyRequest_)
        d_1_maybePublicKeyResponse_ = out0_
        d_2_valueOrError0_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.GetPublicKeyResponse.default())()
        def lambda0_(d_3_e_):
            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_ComAmazonawsKms(d_3_e_)

        d_2_valueOrError0_ = (d_1_maybePublicKeyResponse_).MapFailure(lambda0_)
        if (d_2_valueOrError0_).IsFailure():
            res = (d_2_valueOrError0_).PropagateFailure()
            return res
        d_4_getPublicKeyResponse_: ComAmazonawsKmsTypes.GetPublicKeyResponse
        d_4_getPublicKeyResponse_ = (d_2_valueOrError0_).Extract()
        d_5_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_5_valueOrError1_ = Wrappers.default__.Need(((((((d_4_getPublicKeyResponse_).KeyId).is_Some) and ((((d_4_getPublicKeyResponse_).KeyId).value) == (awsKmsKey))) and (((d_4_getPublicKeyResponse_).KeyUsage).is_Some)) and ((((d_4_getPublicKeyResponse_).KeyUsage).value) == (ComAmazonawsKmsTypes.KeyUsageType_KEY__AGREEMENT()))) and (((d_4_getPublicKeyResponse_).PublicKey).is_Some), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Invalid response from KMS GetPublicKey")))
        if (d_5_valueOrError1_).IsFailure():
            res = (d_5_valueOrError1_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(((d_4_getPublicKeyResponse_).PublicKey).value)
        return res
        return res


class KeyringInfo:
    @classmethod
    def default(cls, ):
        return lambda: KeyringInfo_KeyringInfo(AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.default()(), Wrappers.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KeyringInfo(self) -> bool:
        return isinstance(self, KeyringInfo_KeyringInfo)

class KeyringInfo_KeyringInfo(KeyringInfo, NamedTuple('KeyringInfo', [('description', Any), ('material', Any)])):
    def __dafnystr__(self) -> str:
        return f'KeyringFromKeyDescription.KeyringInfo.KeyringInfo({_dafny.string_of(self.description)}, {_dafny.string_of(self.material)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KeyringInfo_KeyringInfo) and self.description == __o.description and self.material == __o.material
    def __hash__(self) -> int:
        return super().__hash__()

