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

# Module: KeyringFromKeyDescription

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def GetKeyId(input):
        while True:
            with _dafny.label():
                source10_ = input
                unmatched10 = True
                if unmatched10:
                    if source10_.is_Kms:
                        d_321_i_ = source10_.Kms
                        unmatched10 = False
                        return (d_321_i_).keyId
                if unmatched10:
                    if source10_.is_KmsMrk:
                        d_322_i_ = source10_.KmsMrk
                        unmatched10 = False
                        return (d_322_i_).keyId
                if unmatched10:
                    if source10_.is_KmsMrkDiscovery:
                        d_323_i_ = source10_.KmsMrkDiscovery
                        unmatched10 = False
                        return (d_323_i_).keyId
                if unmatched10:
                    if source10_.is_RSA:
                        d_324_i_ = source10_.RSA
                        unmatched10 = False
                        return (d_324_i_).keyId
                if unmatched10:
                    if source10_.is_AES:
                        d_325_i_ = source10_.AES
                        unmatched10 = False
                        return (d_325_i_).keyId
                if unmatched10:
                    if source10_.is_ECDH:
                        d_326_i_ = source10_.ECDH
                        unmatched10 = False
                        return (d_326_i_).senderKeyId
                if unmatched10:
                    if source10_.is_KmsECDH:
                        d_327_i_ = source10_.KmsECDH
                        unmatched10 = False
                        return (d_327_i_).senderKeyId
                if unmatched10:
                    if source10_.is_Static:
                        d_328_i_ = source10_.Static
                        unmatched10 = False
                        return (d_328_i_).keyId
                if unmatched10:
                    if source10_.is_Hierarchy:
                        d_329_i_ = source10_.Hierarchy
                        unmatched10 = False
                        return (d_329_i_).keyId
                if unmatched10:
                    if source10_.is_KmsRsa:
                        d_330_i_ = source10_.KmsRsa
                        unmatched10 = False
                        return (d_330_i_).keyId
                if unmatched10:
                    if source10_.is_RequiredEncryptionContext:
                        d_331_i_ = source10_.RequiredEncryptionContext
                        unmatched10 = False
                        in2_ = (d_331_i_).underlying
                        input = in2_
                        raise _dafny.TailCall()
                if unmatched10:
                    unmatched10 = False
                    return _dafny.Seq("")
                raise Exception("unexpected control point")
                break

    @staticmethod
    def GetSenderKeyId(input):
        source11_ = input
        unmatched11 = True
        if unmatched11:
            if source11_.is_ECDH:
                d_332_i_ = source11_.ECDH
                unmatched11 = False
                return (d_332_i_).senderKeyId
        if unmatched11:
            unmatched11 = False
            return _dafny.Seq("")
        raise Exception("unexpected control point")

    @staticmethod
    def GetRecipientKeyId(input):
        source12_ = input
        unmatched12 = True
        if unmatched12:
            if source12_.is_ECDH:
                d_333_i_ = source12_.ECDH
                unmatched12 = False
                return (d_333_i_).recipientKeyId
        if unmatched12:
            if source12_.is_KmsECDH:
                d_334_i_ = source12_.KmsECDH
                unmatched12 = False
                return (d_334_i_).recipientKeyId
        if unmatched12:
            unmatched12 = False
            return _dafny.Seq("")
        raise Exception("unexpected control point")

    @staticmethod
    def GetKeyMaterial(keys, keyDescription):
        d_335_keyId_ = default__.GetKeyId(keyDescription)
        if (d_335_keyId_) in (keys):
            return Wrappers.Option_Some((keys)[d_335_keyId_])
        elif True:
            return Wrappers.Option_None()

    @staticmethod
    def GetSenderKeyMaterial(keys, keyDescription):
        d_336_keyId_ = default__.GetSenderKeyId(keyDescription)
        if (d_336_keyId_) in (keys):
            return Wrappers.Option_Some((keys)[d_336_keyId_])
        elif True:
            return Wrappers.Option_None()

    @staticmethod
    def GetRecipientKeyMaterial(keys, keyDescription):
        d_337_keyId_ = default__.GetRecipientKeyId(keyDescription)
        if (d_337_keyId_) in (keys):
            return Wrappers.Option_Some((keys)[d_337_keyId_])
        elif True:
            return Wrappers.Option_None()

    @staticmethod
    def ToKeyring(mpl, keys, description):
        output: Wrappers.Result = None
        d_338_material_: Wrappers.Option
        d_338_material_ = default__.GetKeyMaterial(keys, description)
        source13_ = description
        unmatched13 = True
        if unmatched13:
            if source13_.is_Static:
                Static0 = source13_.Static
                d_339_key_ = Static0.keyId
                unmatched13 = False
                if True:
                    d_340_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
                    d_340_valueOrError0_ = Wrappers.default__.Need(((d_338_material_).is_Some) and (((d_338_material_).value).is_StaticMaterial), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not type: StaticMaterial")))
                    if (d_340_valueOrError0_).IsFailure():
                        output = (d_340_valueOrError0_).PropagateFailure()
                        return output
                    d_341_encrypt_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
                    d_341_encrypt_ = AwsCryptographyMaterialProvidersTypes.EncryptionMaterials_EncryptionMaterials(((d_338_material_).value).algorithmSuite, ((d_338_material_).value).encryptionContext, ((d_338_material_).value).encryptedDataKeys, ((d_338_material_).value).requiredEncryptionContextKeys, ((d_338_material_).value).plaintextDataKey, ((d_338_material_).value).signingKey, ((d_338_material_).value).symmetricSigningKeys)
                    d_342_decrypt_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
                    d_342_decrypt_ = AwsCryptographyMaterialProvidersTypes.DecryptionMaterials_DecryptionMaterials(((d_338_material_).value).algorithmSuite, ((d_338_material_).value).encryptionContext, ((d_338_material_).value).requiredEncryptionContextKeys, ((d_338_material_).value).plaintextDataKey, ((d_338_material_).value).verificationKey, Wrappers.Option_None())
                    d_343_keyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
                    out2_: AwsCryptographyMaterialProvidersTypes.IKeyring
                    out2_ = CreateStaticKeyrings.default__.CreateStaticMaterialsKeyring(d_341_encrypt_, d_342_decrypt_)
                    d_343_keyring_ = out2_
                    output = Wrappers.Result_Success(d_343_keyring_)
                    return output
        if unmatched13:
            if source13_.is_Kms:
                Kms0 = source13_.Kms
                d_344_key_ = Kms0.keyId
                unmatched13 = False
                if True:
                    d_345_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
                    d_345_valueOrError1_ = Wrappers.default__.Need(((d_338_material_).is_Some) and (((d_338_material_).value).is_KMS), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not type: KMS")))
                    if (d_345_valueOrError1_).IsFailure():
                        output = (d_345_valueOrError1_).PropagateFailure()
                        return output
                    d_346_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
                    d_347_valueOrError2_: Wrappers.Result = None
                    out3_: Wrappers.Result
                    out3_ = default__.getKmsClient(mpl, ((d_338_material_).value).keyIdentifier)
                    d_347_valueOrError2_ = out3_
                    if (d_347_valueOrError2_).IsFailure():
                        output = (d_347_valueOrError2_).PropagateFailure()
                        return output
                    d_346_kmsClient_ = (d_347_valueOrError2_).Extract()
                    d_348_input_: AwsCryptographyMaterialProvidersTypes.CreateAwsKmsKeyringInput
                    d_348_input_ = AwsCryptographyMaterialProvidersTypes.CreateAwsKmsKeyringInput_CreateAwsKmsKeyringInput(((d_338_material_).value).keyIdentifier, d_346_kmsClient_, Wrappers.Option_None())
                    d_349_keyring_: Wrappers.Result
                    out4_: Wrappers.Result
                    out4_ = (mpl).CreateAwsKmsKeyring(d_348_input_)
                    d_349_keyring_ = out4_
                    def lambda19_(d_350_e_):
                        return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_350_e_)

                    output = (d_349_keyring_).MapFailure(lambda19_)
                    return output
        if unmatched13:
            if source13_.is_KmsMrk:
                KmsMrk0 = source13_.KmsMrk
                d_351_key_ = KmsMrk0.keyId
                unmatched13 = False
                if True:
                    d_352_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
                    d_352_valueOrError3_ = Wrappers.default__.Need(((d_338_material_).is_Some) and (((d_338_material_).value).is_KMS), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not type: KMS")))
                    if (d_352_valueOrError3_).IsFailure():
                        output = (d_352_valueOrError3_).PropagateFailure()
                        return output
                    d_353_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
                    d_354_valueOrError4_: Wrappers.Result = None
                    out5_: Wrappers.Result
                    out5_ = default__.getKmsClient(mpl, ((d_338_material_).value).keyIdentifier)
                    d_354_valueOrError4_ = out5_
                    if (d_354_valueOrError4_).IsFailure():
                        output = (d_354_valueOrError4_).PropagateFailure()
                        return output
                    d_353_kmsClient_ = (d_354_valueOrError4_).Extract()
                    d_355_input_: AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMrkKeyringInput
                    d_355_input_ = AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMrkKeyringInput_CreateAwsKmsMrkKeyringInput(((d_338_material_).value).keyIdentifier, d_353_kmsClient_, Wrappers.Option_None())
                    d_356_keyring_: Wrappers.Result
                    out6_: Wrappers.Result
                    out6_ = (mpl).CreateAwsKmsMrkKeyring(d_355_input_)
                    d_356_keyring_ = out6_
                    def lambda20_(d_357_e_):
                        return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_357_e_)

                    output = (d_356_keyring_).MapFailure(lambda20_)
                    return output
        if unmatched13:
            if source13_.is_KmsRsa:
                KmsRsa0 = source13_.KmsRsa
                d_358_key_ = KmsRsa0.keyId
                d_359_encryptionAlgorithm_ = KmsRsa0.encryptionAlgorithm
                unmatched13 = False
                if True:
                    d_360_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome.default()()
                    d_360_valueOrError5_ = Wrappers.default__.Need(((d_338_material_).is_Some) and (((d_338_material_).value).is_KMSAsymetric), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not type: KMSAsymetric")))
                    if (d_360_valueOrError5_).IsFailure():
                        output = (d_360_valueOrError5_).PropagateFailure()
                        return output
                    d_361_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
                    d_362_valueOrError6_: Wrappers.Result = None
                    out7_: Wrappers.Result
                    out7_ = default__.getKmsClient(mpl, ((d_338_material_).value).keyIdentifier)
                    d_362_valueOrError6_ = out7_
                    if (d_362_valueOrError6_).IsFailure():
                        output = (d_362_valueOrError6_).PropagateFailure()
                        return output
                    d_361_kmsClient_ = (d_362_valueOrError6_).Extract()
                    d_363_input_: AwsCryptographyMaterialProvidersTypes.CreateAwsKmsRsaKeyringInput
                    d_363_input_ = AwsCryptographyMaterialProvidersTypes.CreateAwsKmsRsaKeyringInput_CreateAwsKmsRsaKeyringInput(Wrappers.Option_Some(((d_338_material_).value).publicKey), ((d_338_material_).value).keyIdentifier, d_359_encryptionAlgorithm_, Wrappers.Option_Some(d_361_kmsClient_), Wrappers.Option_None())
                    d_364_keyring_: Wrappers.Result
                    out8_: Wrappers.Result
                    out8_ = (mpl).CreateAwsKmsRsaKeyring(d_363_input_)
                    d_364_keyring_ = out8_
                    def lambda21_(d_365_e_):
                        return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_365_e_)

                    output = (d_364_keyring_).MapFailure(lambda21_)
                    return output
        if unmatched13:
            if source13_.is_Hierarchy:
                Hierarchy0 = source13_.Hierarchy
                d_366_key_ = Hierarchy0.keyId
                unmatched13 = False
                if True:
                    d_367_valueOrError7_: Wrappers.Outcome = Wrappers.Outcome.default()()
                    d_367_valueOrError7_ = Wrappers.default__.Need(((d_338_material_).is_Some) and (((d_338_material_).value).is_StaticKeyStoreInformation), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not type: StaticKeyStoreInformation")))
                    if (d_367_valueOrError7_).IsFailure():
                        output = (d_367_valueOrError7_).PropagateFailure()
                        return output
                    d_368_keyStore_: AwsCryptographyKeyStoreTypes.IKeyStoreClient
                    out9_: AwsCryptographyKeyStoreTypes.IKeyStoreClient
                    out9_ = CreateStaticKeyStores.default__.CreateStaticKeyStore((d_338_material_).value)
                    d_368_keyStore_ = out9_
                    d_369_input_: AwsCryptographyMaterialProvidersTypes.CreateAwsKmsHierarchicalKeyringInput
                    d_369_input_ = AwsCryptographyMaterialProvidersTypes.CreateAwsKmsHierarchicalKeyringInput_CreateAwsKmsHierarchicalKeyringInput(Wrappers.Option_Some(((d_338_material_).value).keyIdentifier), Wrappers.Option_None(), d_368_keyStore_, 0, Wrappers.Option_None())
                    d_370_keyring_: Wrappers.Result
                    out10_: Wrappers.Result
                    out10_ = (mpl).CreateAwsKmsHierarchicalKeyring(d_369_input_)
                    d_370_keyring_ = out10_
                    def lambda22_(d_371_e_):
                        return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_371_e_)

                    output = (d_370_keyring_).MapFailure(lambda22_)
                    return output
        if unmatched13:
            if source13_.is_KmsMrkDiscovery:
                KmsMrkDiscovery0 = source13_.KmsMrkDiscovery
                d_372_defaultMrkRegion_ = KmsMrkDiscovery0.defaultMrkRegion
                d_373_awsKmsDiscoveryFilter_ = KmsMrkDiscovery0.awsKmsDiscoveryFilter
                unmatched13 = False
                if True:
                    d_374_valueOrError8_: Wrappers.Outcome = Wrappers.Outcome.default()()
                    d_374_valueOrError8_ = Wrappers.default__.Need((d_338_material_).is_None, AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Discovery has not key")))
                    if (d_374_valueOrError8_).IsFailure():
                        output = (d_374_valueOrError8_).PropagateFailure()
                        return output
                    d_375_input_: AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMrkDiscoveryMultiKeyringInput
                    d_375_input_ = AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMrkDiscoveryMultiKeyringInput_CreateAwsKmsMrkDiscoveryMultiKeyringInput(_dafny.Seq([d_372_defaultMrkRegion_]), d_373_awsKmsDiscoveryFilter_, Wrappers.Option_None(), Wrappers.Option_None())
                    d_376_keyring_: Wrappers.Result
                    out11_: Wrappers.Result
                    out11_ = (mpl).CreateAwsKmsMrkDiscoveryMultiKeyring(d_375_input_)
                    d_376_keyring_ = out11_
                    def lambda23_(d_377_e_):
                        return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_377_e_)

                    output = (d_376_keyring_).MapFailure(lambda23_)
                    return output
        if unmatched13:
            if source13_.is_AES:
                AES0 = source13_.AES
                d_378_key_ = AES0.keyId
                d_379_providerId_ = AES0.providerId
                unmatched13 = False
                if True:
                    d_380_valueOrError9_: Wrappers.Outcome = Wrappers.Outcome.default()()
                    d_380_valueOrError9_ = Wrappers.default__.Need(((d_338_material_).is_Some) and (((d_338_material_).value).is_Symetric), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not type: Symmetric")))
                    if (d_380_valueOrError9_).IsFailure():
                        output = (d_380_valueOrError9_).PropagateFailure()
                        return output
                    d_381_wrappingAlg_: AwsCryptographyMaterialProvidersTypes.AesWrappingAlg
                    d_382_valueOrError10_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyMaterialProvidersTypes.AesWrappingAlg.default())()
                    def lambda24_():
                        source14_ = ((d_338_material_).value).bits
                        unmatched14 = True
                        if unmatched14:
                            if (source14_) == (128):
                                unmatched14 = False
                                return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES128__GCM__IV12__TAG16())
                        if unmatched14:
                            if (source14_) == (192):
                                unmatched14 = False
                                return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES192__GCM__IV12__TAG16())
                        if unmatched14:
                            if (source14_) == (256):
                                unmatched14 = False
                                return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16())
                        if unmatched14:
                            unmatched14 = False
                            return Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not a supported bit length")))
                        raise Exception("unexpected control point")

                    d_382_valueOrError10_ = lambda24_()
                    if (d_382_valueOrError10_).IsFailure():
                        output = (d_382_valueOrError10_).PropagateFailure()
                        return output
                    d_381_wrappingAlg_ = (d_382_valueOrError10_).Extract()
                    d_383_input_: AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput
                    d_383_input_ = AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_379_providerId_, ((d_338_material_).value).keyIdentifier, ((d_338_material_).value).wrappingKey, d_381_wrappingAlg_)
                    d_384_keyring_: Wrappers.Result
                    out12_: Wrappers.Result
                    out12_ = (mpl).CreateRawAesKeyring(d_383_input_)
                    d_384_keyring_ = out12_
                    def lambda25_(d_385_e_):
                        return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_385_e_)

                    output = (d_384_keyring_).MapFailure(lambda25_)
                    return output
        if unmatched13:
            if source13_.is_RSA:
                RSA0 = source13_.RSA
                d_386_key_ = RSA0.keyId
                d_387_providerId_ = RSA0.providerId
                d_388_padding_ = RSA0.padding
                unmatched13 = False
                if True:
                    d_389_valueOrError11_: Wrappers.Outcome = Wrappers.Outcome.default()()
                    d_389_valueOrError11_ = Wrappers.default__.Need(((d_338_material_).is_Some) and ((((d_338_material_).value).is_PrivateRSA) or (((d_338_material_).value).is_PublicRSA)), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not type: PrivateRSA or PublicRSA")))
                    if (d_389_valueOrError11_).IsFailure():
                        output = (d_389_valueOrError11_).PropagateFailure()
                        return output
                    source15_ = d_338_material_
                    unmatched15 = True
                    if unmatched15:
                        if source15_.is_Some:
                            value0 = source15_.value
                            if value0.is_PrivateRSA:
                                d_390_decrypt_ = value0.decrypt
                                d_391_material_ = value0.material
                                d_392_keyIdentifier_ = value0.keyIdentifier
                                unmatched15 = False
                                if True:
                                    d_393_valueOrError12_: Wrappers.Outcome = Wrappers.Outcome.default()()
                                    d_393_valueOrError12_ = Wrappers.default__.Need(d_390_decrypt_, AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Private RSA keys only supports decrypt.")))
                                    if (d_393_valueOrError12_).IsFailure():
                                        output = (d_393_valueOrError12_).PropagateFailure()
                                        return output
                                    d_394_privateKeyPemBytes_: _dafny.Seq
                                    d_395_valueOrError13_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
                                    def lambda26_(d_396_e_):
                                        return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(d_396_e_)

                                    d_395_valueOrError13_ = (UTF8.default__.Encode(d_391_material_)).MapFailure(lambda26_)
                                    if (d_395_valueOrError13_).IsFailure():
                                        output = (d_395_valueOrError13_).PropagateFailure()
                                        return output
                                    d_394_privateKeyPemBytes_ = (d_395_valueOrError13_).Extract()
                                    d_397_input_: AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput
                                    d_397_input_ = AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_387_providerId_, d_392_keyIdentifier_, d_388_padding_, Wrappers.Option_None(), Wrappers.Option_Some(d_394_privateKeyPemBytes_))
                                    d_398_keyring_: Wrappers.Result
                                    out13_: Wrappers.Result
                                    out13_ = (mpl).CreateRawRsaKeyring(d_397_input_)
                                    d_398_keyring_ = out13_
                                    def lambda27_(d_399_e_):
                                        return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_399_e_)

                                    output = (d_398_keyring_).MapFailure(lambda27_)
                                    return output
                    if unmatched15:
                        value1 = source15_.value
                        d_400_encrypt_ = value1.encrypt
                        d_401_material_ = value1.material
                        d_402_keyIdentifier_ = value1.keyIdentifier
                        unmatched15 = False
                        if True:
                            d_403_valueOrError14_: Wrappers.Outcome = Wrappers.Outcome.default()()
                            d_403_valueOrError14_ = Wrappers.default__.Need(d_400_encrypt_, AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Public RSA keys only supports encrypt.")))
                            if (d_403_valueOrError14_).IsFailure():
                                output = (d_403_valueOrError14_).PropagateFailure()
                                return output
                            d_404_publicKeyPemBytes_: _dafny.Seq
                            d_405_valueOrError15_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
                            def lambda28_(d_406_e_):
                                return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(d_406_e_)

                            d_405_valueOrError15_ = (UTF8.default__.Encode(d_401_material_)).MapFailure(lambda28_)
                            if (d_405_valueOrError15_).IsFailure():
                                output = (d_405_valueOrError15_).PropagateFailure()
                                return output
                            d_404_publicKeyPemBytes_ = (d_405_valueOrError15_).Extract()
                            d_407_input_: AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput
                            d_407_input_ = AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_387_providerId_, d_402_keyIdentifier_, d_388_padding_, Wrappers.Option_Some(d_404_publicKeyPemBytes_), Wrappers.Option_None())
                            d_408_keyring_: Wrappers.Result
                            out14_: Wrappers.Result
                            out14_ = (mpl).CreateRawRsaKeyring(d_407_input_)
                            d_408_keyring_ = out14_
                            def lambda29_(d_409_e_):
                                return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_409_e_)

                            output = (d_408_keyring_).MapFailure(lambda29_)
                            return output
        if unmatched13:
            if source13_.is_ECDH:
                ECDH0 = source13_.ECDH
                d_410_senderKeyId_ = ECDH0.senderKeyId
                d_411_recipientKeyId_ = ECDH0.recipientKeyId
                d_412_senderPublicKey_ = ECDH0.senderPublicKey
                d_413_recipientPublicKey_ = ECDH0.recipientPublicKey
                d_414_providerId_ = ECDH0.providerId
                d_415_curveSpec_ = ECDH0.curveSpec
                d_416_keyAgreementScheme_ = ECDH0.keyAgreementScheme
                unmatched13 = False
                if True:
                    d_417_valueOrError16_: Wrappers.Outcome = Wrappers.Outcome.default()()
                    d_417_valueOrError16_ = Wrappers.default__.Need((d_415_curveSpec_) in (KeyDescription.default__.Curve2EccAlgorithmSpec), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Unknown curve spec")))
                    if (d_417_valueOrError16_).IsFailure():
                        output = (d_417_valueOrError16_).PropagateFailure()
                        return output
                    d_418_curveType_: AwsCryptographyPrimitivesTypes.ECDHCurveSpec
                    d_418_curveType_ = (KeyDescription.default__.Curve2EccAlgorithmSpec)[d_415_curveSpec_]
                    d_419_primitives_q_: Wrappers.Result
                    out15_: Wrappers.Result
                    out15_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
                    d_419_primitives_q_ = out15_
                    d_420_primitives_: AtomicPrimitives.AtomicPrimitivesClient
                    d_421_valueOrError17_: Wrappers.Result = None
                    def lambda30_(d_422_e_):
                        return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Unable to create primitives client"))

                    d_421_valueOrError17_ = (d_419_primitives_q_).MapFailure(lambda30_)
                    if (d_421_valueOrError17_).IsFailure():
                        output = (d_421_valueOrError17_).PropagateFailure()
                        return output
                    d_420_primitives_ = (d_421_valueOrError17_).Extract()
                    source16_ = d_416_keyAgreementScheme_
                    unmatched16 = True
                    if unmatched16:
                        if (source16_) == (_dafny.Seq("static")):
                            unmatched16 = False
                            if True:
                                d_423_valueOrError18_: Wrappers.Outcome = Wrappers.Outcome.default()()
                                d_423_valueOrError18_ = Wrappers.default__.Need(((d_338_material_).is_Some) and (((d_338_material_).value).is_PrivateECDH), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not type: PrivateECDH")))
                                if (d_423_valueOrError18_).IsFailure():
                                    output = (d_423_valueOrError18_).PropagateFailure()
                                    return output
                                d_424_senderMaterial_: _dafny.Seq
                                d_425_valueOrError19_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
                                def lambda31_(d_426_e_):
                                    return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(d_426_e_)

                                d_425_valueOrError19_ = (UTF8.default__.Encode(((d_338_material_).value).senderMaterial)).MapFailure(lambda31_)
                                if (d_425_valueOrError19_).IsFailure():
                                    output = (d_425_valueOrError19_).PropagateFailure()
                                    return output
                                d_424_senderMaterial_ = (d_425_valueOrError19_).Extract()
                                d_427_recipientMaterial_: _dafny.Seq
                                d_428_valueOrError20_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
                                def lambda32_(d_429_e_):
                                    return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(d_429_e_)

                                d_428_valueOrError20_ = (UTF8.default__.Encode(((d_338_material_).value).recipientMaterial)).MapFailure(lambda32_)
                                if (d_428_valueOrError20_).IsFailure():
                                    output = (d_428_valueOrError20_).PropagateFailure()
                                    return output
                                d_427_recipientMaterial_ = (d_428_valueOrError20_).Extract()
                                d_430_recipientPublicKey_: _dafny.Seq
                                d_431_valueOrError21_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
                                def lambda33_(d_432_e_):
                                    return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(d_432_e_)

                                d_431_valueOrError21_ = (Base64.default__.Decode(((d_338_material_).value).recipientPublicKey)).MapFailure(lambda33_)
                                if (d_431_valueOrError21_).IsFailure():
                                    output = (d_431_valueOrError21_).PropagateFailure()
                                    return output
                                d_430_recipientPublicKey_ = (d_431_valueOrError21_).Extract()
                                d_433_schema_: AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations
                                d_433_schema_ = AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_RawPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.RawPrivateKeyToStaticPublicKeyInput_RawPrivateKeyToStaticPublicKeyInput(d_424_senderMaterial_, d_430_recipientPublicKey_))
                                d_434_input_: AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput
                                d_434_input_ = AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(d_433_schema_, d_418_curveType_)
                                d_435_keyring_: Wrappers.Result
                                out16_: Wrappers.Result
                                out16_ = (mpl).CreateRawEcdhKeyring(d_434_input_)
                                d_435_keyring_ = out16_
                                def lambda34_(d_436_e_):
                                    return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_436_e_)

                                output = (d_435_keyring_).MapFailure(lambda34_)
                                return output
                    if unmatched16:
                        if (source16_) == (_dafny.Seq("ephemeral")):
                            unmatched16 = False
                            if True:
                                d_437_recipientMaterial_q_: Wrappers.Option
                                d_437_recipientMaterial_q_ = default__.GetRecipientKeyMaterial(keys, description)
                                d_438_valueOrError22_: Wrappers.Outcome = Wrappers.Outcome.default()()
                                d_438_valueOrError22_ = Wrappers.default__.Need(((d_437_recipientMaterial_q_).is_Some) and (((d_437_recipientMaterial_q_).value).is_PrivateECDH), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not type: PrivateECDH")))
                                if (d_438_valueOrError22_).IsFailure():
                                    output = (d_438_valueOrError22_).PropagateFailure()
                                    return output
                                d_439_recipientMaterial_: _dafny.Seq
                                d_440_valueOrError23_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
                                def lambda35_(d_441_e_):
                                    return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(d_441_e_)

                                d_440_valueOrError23_ = (UTF8.default__.Encode(((d_437_recipientMaterial_q_).value).recipientMaterial)).MapFailure(lambda35_)
                                if (d_440_valueOrError23_).IsFailure():
                                    output = (d_440_valueOrError23_).PropagateFailure()
                                    return output
                                d_439_recipientMaterial_ = (d_440_valueOrError23_).Extract()
                                d_442_recipientPublicKey_: _dafny.Seq
                                d_443_valueOrError24_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
                                def lambda36_(d_444_e_):
                                    return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(d_444_e_)

                                d_443_valueOrError24_ = (Base64.default__.Decode(((d_437_recipientMaterial_q_).value).recipientPublicKey)).MapFailure(lambda36_)
                                if (d_443_valueOrError24_).IsFailure():
                                    output = (d_443_valueOrError24_).PropagateFailure()
                                    return output
                                d_442_recipientPublicKey_ = (d_443_valueOrError24_).Extract()
                                d_445_schema_: AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations
                                d_445_schema_ = AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_EphemeralPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.EphemeralPrivateKeyToStaticPublicKeyInput_EphemeralPrivateKeyToStaticPublicKeyInput(d_442_recipientPublicKey_))
                                d_446_input_: AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput
                                d_446_input_ = AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(d_445_schema_, d_418_curveType_)
                                d_447_keyring_: Wrappers.Result
                                out17_: Wrappers.Result
                                out17_ = (mpl).CreateRawEcdhKeyring(d_446_input_)
                                d_447_keyring_ = out17_
                                def lambda37_(d_448_e_):
                                    return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_448_e_)

                                output = (d_447_keyring_).MapFailure(lambda37_)
                                return output
                    if unmatched16:
                        if (source16_) == (_dafny.Seq("discovery")):
                            unmatched16 = False
                            if True:
                                d_449_recipientMaterial_q_: Wrappers.Option
                                d_449_recipientMaterial_q_ = default__.GetRecipientKeyMaterial(keys, description)
                                d_450_valueOrError25_: Wrappers.Outcome = Wrappers.Outcome.default()()
                                d_450_valueOrError25_ = Wrappers.default__.Need(((d_449_recipientMaterial_q_).is_Some) and (((d_449_recipientMaterial_q_).value).is_PrivateECDH), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not type: PrivateECDH")))
                                if (d_450_valueOrError25_).IsFailure():
                                    output = (d_450_valueOrError25_).PropagateFailure()
                                    return output
                                d_451_recipientMaterial_: _dafny.Seq
                                d_452_valueOrError26_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
                                def lambda38_(d_453_e_):
                                    return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(d_453_e_)

                                d_452_valueOrError26_ = (UTF8.default__.Encode(((d_449_recipientMaterial_q_).value).recipientMaterial)).MapFailure(lambda38_)
                                if (d_452_valueOrError26_).IsFailure():
                                    output = (d_452_valueOrError26_).PropagateFailure()
                                    return output
                                d_451_recipientMaterial_ = (d_452_valueOrError26_).Extract()
                                d_454_schema_: AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations
                                d_454_schema_ = AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations_PublicKeyDiscovery(AwsCryptographyMaterialProvidersTypes.PublicKeyDiscoveryInput_PublicKeyDiscoveryInput(d_451_recipientMaterial_))
                                d_455_input_: AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput
                                d_455_input_ = AwsCryptographyMaterialProvidersTypes.CreateRawEcdhKeyringInput_CreateRawEcdhKeyringInput(d_454_schema_, d_418_curveType_)
                                d_456_keyring_: Wrappers.Result
                                out18_: Wrappers.Result
                                out18_ = (mpl).CreateRawEcdhKeyring(d_455_input_)
                                d_456_keyring_ = out18_
                                def lambda39_(d_457_e_):
                                    return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_457_e_)

                                output = (d_456_keyring_).MapFailure(lambda39_)
                                return output
                    if unmatched16:
                        unmatched16 = False
                        if True:
                            output = Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("key agreement schema not recognized")))
                            return output
        if unmatched13:
            if source13_.is_KmsECDH:
                KmsECDH0 = source13_.KmsECDH
                d_458_senderKeyId_ = KmsECDH0.senderKeyId
                d_459_recipientKeyId_ = KmsECDH0.recipientKeyId
                d_460_senderPublicKey_ = KmsECDH0.senderPublicKey
                d_461_recipientPublicKey_ = KmsECDH0.recipientPublicKey
                d_462_curveSpec_ = KmsECDH0.curveSpec
                d_463_keyAgreementScheme_ = KmsECDH0.keyAgreementScheme
                unmatched13 = False
                if True:
                    d_464_valueOrError27_: Wrappers.Outcome = Wrappers.Outcome.default()()
                    d_464_valueOrError27_ = Wrappers.default__.Need((d_462_curveSpec_) in (KeyDescription.default__.KmsKey2EccAlgorithmSpec), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Unknown curve spec")))
                    if (d_464_valueOrError27_).IsFailure():
                        output = (d_464_valueOrError27_).PropagateFailure()
                        return output
                    d_465_curveType_: AwsCryptographyPrimitivesTypes.ECDHCurveSpec
                    d_465_curveType_ = (KeyDescription.default__.KmsKey2EccAlgorithmSpec)[d_462_curveSpec_]
                    source17_ = d_463_keyAgreementScheme_
                    unmatched17 = True
                    if unmatched17:
                        if (source17_) == (_dafny.Seq("static")):
                            unmatched17 = False
                            if True:
                                d_466_valueOrError28_: Wrappers.Outcome = Wrappers.Outcome.default()()
                                d_466_valueOrError28_ = Wrappers.default__.Need(((d_338_material_).is_Some) and (((d_338_material_).value).is_KMSEcdh), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not type: KmsEcdh")))
                                if (d_466_valueOrError28_).IsFailure():
                                    output = (d_466_valueOrError28_).PropagateFailure()
                                    return output
                                d_467_senderKmsKey_: _dafny.Seq
                                d_467_senderKmsKey_ = ((d_338_material_).value).senderMaterial
                                d_468_recipientKmsKey_: _dafny.Seq
                                d_468_recipientKmsKey_ = ((d_338_material_).value).recipientMaterial
                                d_469_valueOrError29_: Wrappers.Outcome = Wrappers.Outcome.default()()
                                d_469_valueOrError29_ = Wrappers.default__.Need((ComAmazonawsKmsTypes.default__.IsValid__KeyIdType(d_467_senderKmsKey_)) and (ComAmazonawsKmsTypes.default__.IsValid__KeyIdType(d_468_recipientKmsKey_)), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not a valid Kms Key Id")))
                                if (d_469_valueOrError29_).IsFailure():
                                    output = (d_469_valueOrError29_).PropagateFailure()
                                    return output
                                d_470_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
                                d_471_valueOrError30_: Wrappers.Result = None
                                out19_: Wrappers.Result
                                out19_ = default__.getKmsClient(mpl, d_467_senderKmsKey_)
                                d_471_valueOrError30_ = out19_
                                if (d_471_valueOrError30_).IsFailure():
                                    output = (d_471_valueOrError30_).PropagateFailure()
                                    return output
                                d_470_kmsClient_ = (d_471_valueOrError30_).Extract()
                                d_472_senderPublicKey_: _dafny.Seq
                                d_473_valueOrError31_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
                                def lambda40_(d_474_e_):
                                    return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(d_474_e_)

                                d_473_valueOrError31_ = (Base64.default__.Decode(((d_338_material_).value).senderPublicKey)).MapFailure(lambda40_)
                                if (d_473_valueOrError31_).IsFailure():
                                    output = (d_473_valueOrError31_).PropagateFailure()
                                    return output
                                d_472_senderPublicKey_ = (d_473_valueOrError31_).Extract()
                                d_475_recipientPublicKey_: _dafny.Seq
                                d_476_valueOrError32_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
                                def lambda41_(d_477_e_):
                                    return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(d_477_e_)

                                d_476_valueOrError32_ = (Base64.default__.Decode(((d_338_material_).value).recipientPublicKey)).MapFailure(lambda41_)
                                if (d_476_valueOrError32_).IsFailure():
                                    output = (d_476_valueOrError32_).PropagateFailure()
                                    return output
                                d_475_recipientPublicKey_ = (d_476_valueOrError32_).Extract()
                                d_478_schema_: AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations
                                d_478_schema_ = AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPrivateKeyToStaticPublicKey(AwsCryptographyMaterialProvidersTypes.KmsPrivateKeyToStaticPublicKeyInput_KmsPrivateKeyToStaticPublicKeyInput(d_467_senderKmsKey_, Wrappers.Option_Some(d_472_senderPublicKey_), d_475_recipientPublicKey_))
                                d_479_input_: AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput
                                d_479_input_ = AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(d_478_schema_, d_465_curveType_, d_470_kmsClient_, Wrappers.Option_None())
                                d_480_keyring_: Wrappers.Result
                                out20_: Wrappers.Result
                                out20_ = (mpl).CreateAwsKmsEcdhKeyring(d_479_input_)
                                d_480_keyring_ = out20_
                                def lambda42_(d_481_e_):
                                    return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_481_e_)

                                output = (d_480_keyring_).MapFailure(lambda42_)
                                return output
                    if unmatched17:
                        if (source17_) == (_dafny.Seq("discovery")):
                            unmatched17 = False
                            if True:
                                d_482_recipientMaterial_q_: Wrappers.Option
                                d_482_recipientMaterial_q_ = default__.GetRecipientKeyMaterial(keys, description)
                                d_483_valueOrError33_: Wrappers.Outcome = Wrappers.Outcome.default()()
                                d_483_valueOrError33_ = Wrappers.default__.Need(((d_482_recipientMaterial_q_).is_Some) and (((d_482_recipientMaterial_q_).value).is_KMSEcdh), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not type: KmsEcdh")))
                                if (d_483_valueOrError33_).IsFailure():
                                    output = (d_483_valueOrError33_).PropagateFailure()
                                    return output
                                d_484_recipientKmsKey_: _dafny.Seq
                                d_484_recipientKmsKey_ = ((d_482_recipientMaterial_q_).value).recipientMaterial
                                d_485_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
                                d_486_valueOrError34_: Wrappers.Result = None
                                out21_: Wrappers.Result
                                out21_ = default__.getKmsClient(mpl, d_484_recipientKmsKey_)
                                d_486_valueOrError34_ = out21_
                                if (d_486_valueOrError34_).IsFailure():
                                    output = (d_486_valueOrError34_).PropagateFailure()
                                    return output
                                d_485_kmsClient_ = (d_486_valueOrError34_).Extract()
                                d_487_schema_: AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations
                                d_487_schema_ = AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations_KmsPublicKeyDiscovery(AwsCryptographyMaterialProvidersTypes.KmsPublicKeyDiscoveryInput_KmsPublicKeyDiscoveryInput(d_484_recipientKmsKey_))
                                d_488_input_: AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput
                                d_488_input_ = AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput_CreateAwsKmsEcdhKeyringInput(d_487_schema_, d_465_curveType_, d_485_kmsClient_, Wrappers.Option_None())
                                d_489_keyring_: Wrappers.Result
                                out22_: Wrappers.Result
                                out22_ = (mpl).CreateAwsKmsEcdhKeyring(d_488_input_)
                                d_489_keyring_ = out22_
                                def lambda43_(d_490_e_):
                                    return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_490_e_)

                                output = (d_489_keyring_).MapFailure(lambda43_)
                                return output
                    if unmatched17:
                        unmatched17 = False
                        if True:
                            output = Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("key agreement schema not recognized")))
                            return output
        if unmatched13:
            d_491_MultiKeyring_ = source13_.Multi
            unmatched13 = False
            if True:
                d_492_generator_: Wrappers.Option
                d_492_generator_ = Wrappers.Option_None()
                if ((d_491_MultiKeyring_).generator).is_Some:
                    d_493_valueOrError35_: Wrappers.Outcome = Wrappers.Outcome.default()()
                    d_493_valueOrError35_ = Wrappers.default__.Need(KeyDescription.default__.Keyring_q(((d_491_MultiKeyring_).generator).value), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Only Keyring key descriptions are supported.")))
                    if (d_493_valueOrError35_).IsFailure():
                        output = (d_493_valueOrError35_).PropagateFailure()
                        return output
                    d_494_generator_k_: AwsCryptographyMaterialProvidersTypes.IKeyring
                    d_495_valueOrError36_: Wrappers.Result = None
                    out23_: Wrappers.Result
                    out23_ = default__.ToKeyring(mpl, keys, ((d_491_MultiKeyring_).generator).value)
                    d_495_valueOrError36_ = out23_
                    if (d_495_valueOrError36_).IsFailure():
                        output = (d_495_valueOrError36_).PropagateFailure()
                        return output
                    d_494_generator_k_ = (d_495_valueOrError36_).Extract()
                    d_492_generator_ = Wrappers.Option_Some(d_494_generator_k_)
                d_496_childKeyrings_: _dafny.Seq
                d_496_childKeyrings_ = _dafny.Seq([])
                hi0_ = len((d_491_MultiKeyring_).childKeyrings)
                for d_497_i_ in range(0, hi0_):
                    d_498_child_: AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription
                    d_498_child_ = ((d_491_MultiKeyring_).childKeyrings)[d_497_i_]
                    d_499_valueOrError37_: Wrappers.Outcome = Wrappers.Outcome.default()()
                    d_499_valueOrError37_ = Wrappers.default__.Need(KeyDescription.default__.Keyring_q(d_498_child_), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Only Keyring key descriptions are supported.")))
                    if (d_499_valueOrError37_).IsFailure():
                        output = (d_499_valueOrError37_).PropagateFailure()
                        return output
                    d_500_childKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
                    d_501_valueOrError38_: Wrappers.Result = None
                    out24_: Wrappers.Result
                    out24_ = default__.ToKeyring(mpl, keys, d_498_child_)
                    d_501_valueOrError38_ = out24_
                    if (d_501_valueOrError38_).IsFailure():
                        output = (d_501_valueOrError38_).PropagateFailure()
                        return output
                    d_500_childKeyring_ = (d_501_valueOrError38_).Extract()
                    d_496_childKeyrings_ = (d_496_childKeyrings_) + (_dafny.Seq([d_500_childKeyring_]))
                d_502_input_: AwsCryptographyMaterialProvidersTypes.CreateMultiKeyringInput
                d_502_input_ = AwsCryptographyMaterialProvidersTypes.CreateMultiKeyringInput_CreateMultiKeyringInput(d_492_generator_, d_496_childKeyrings_)
                d_503_keyring_: Wrappers.Result
                out25_: Wrappers.Result
                out25_ = (mpl).CreateMultiKeyring(d_502_input_)
                d_503_keyring_ = out25_
                def lambda44_(d_504_e_):
                    return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_504_e_)

                output = (d_503_keyring_).MapFailure(lambda44_)
                return output
        return output

    @staticmethod
    def getKmsClient(mpl, maybeKmsArn):
        output: Wrappers.Result = None
        d_505_maybeClientSupplier_: Wrappers.Result
        out26_: Wrappers.Result
        out26_ = (mpl).CreateDefaultClientSupplier(AwsCryptographyMaterialProvidersTypes.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
        d_505_maybeClientSupplier_ = out26_
        d_506_clientSupplier_: AwsCryptographyMaterialProvidersTypes.IClientSupplier
        d_507_valueOrError0_: Wrappers.Result = None
        def lambda45_(d_508_e_):
            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_508_e_)

        d_507_valueOrError0_ = (d_505_maybeClientSupplier_).MapFailure(lambda45_)
        if (d_507_valueOrError0_).IsFailure():
            output = (d_507_valueOrError0_).PropagateFailure()
            return output
        d_506_clientSupplier_ = (d_507_valueOrError0_).Extract()
        d_509_arn_: Wrappers.Result
        d_509_arn_ = AwsArnParsing.default__.IsAwsKmsIdentifierString(maybeKmsArn)
        d_510_region_: Wrappers.Option
        d_510_region_ = (AwsArnParsing.default__.GetRegion((d_509_arn_).value) if (d_509_arn_).is_Success else Wrappers.Option_None())
        d_511_tmp_: Wrappers.Result
        out27_: Wrappers.Result
        out27_ = (d_506_clientSupplier_).GetClient(AwsCryptographyMaterialProvidersTypes.GetClientInput_GetClientInput((d_510_region_).UnwrapOr(_dafny.Seq(""))))
        d_511_tmp_ = out27_
        def lambda46_(d_512_e_):
            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_512_e_)

        output = (d_511_tmp_).MapFailure(lambda46_)
        return output

    @staticmethod
    def GetEcdhPublicKey(client, awsKmsKey):
        res: Wrappers.Result = None
        d_513_getPublicKeyRequest_: ComAmazonawsKmsTypes.GetPublicKeyRequest
        d_513_getPublicKeyRequest_ = ComAmazonawsKmsTypes.GetPublicKeyRequest_GetPublicKeyRequest(awsKmsKey, Wrappers.Option_None())
        d_514_maybePublicKeyResponse_: Wrappers.Result
        out28_: Wrappers.Result
        out28_ = (client).GetPublicKey(d_513_getPublicKeyRequest_)
        d_514_maybePublicKeyResponse_ = out28_
        d_515_getPublicKeyResponse_: ComAmazonawsKmsTypes.GetPublicKeyResponse
        d_516_valueOrError0_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.GetPublicKeyResponse.default())()
        def lambda47_(d_517_e_):
            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_ComAmazonawsKms(d_517_e_)

        d_516_valueOrError0_ = (d_514_maybePublicKeyResponse_).MapFailure(lambda47_)
        if (d_516_valueOrError0_).IsFailure():
            res = (d_516_valueOrError0_).PropagateFailure()
            return res
        d_515_getPublicKeyResponse_ = (d_516_valueOrError0_).Extract()
        d_518_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_518_valueOrError1_ = Wrappers.default__.Need(((((((d_515_getPublicKeyResponse_).KeyId).is_Some) and ((((d_515_getPublicKeyResponse_).KeyId).value) == (awsKmsKey))) and (((d_515_getPublicKeyResponse_).KeyUsage).is_Some)) and ((((d_515_getPublicKeyResponse_).KeyUsage).value) == (ComAmazonawsKmsTypes.KeyUsageType_KEY__AGREEMENT()))) and (((d_515_getPublicKeyResponse_).PublicKey).is_Some), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Invalid response from KMS GetPublicKey")))
        if (d_518_valueOrError1_).IsFailure():
            res = (d_518_valueOrError1_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(((d_515_getPublicKeyResponse_).PublicKey).value)
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

