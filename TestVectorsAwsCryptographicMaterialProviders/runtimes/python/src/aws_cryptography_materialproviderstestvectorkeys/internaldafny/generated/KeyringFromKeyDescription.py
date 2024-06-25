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
                        d_273_i_ = source10_.Kms
                        unmatched10 = False
                        return (d_273_i_).keyId
                if unmatched10:
                    if source10_.is_KmsMrk:
                        d_274_i_ = source10_.KmsMrk
                        unmatched10 = False
                        return (d_274_i_).keyId
                if unmatched10:
                    if source10_.is_KmsMrkDiscovery:
                        d_275_i_ = source10_.KmsMrkDiscovery
                        unmatched10 = False
                        return (d_275_i_).keyId
                if unmatched10:
                    if source10_.is_RSA:
                        d_276_i_ = source10_.RSA
                        unmatched10 = False
                        return (d_276_i_).keyId
                if unmatched10:
                    if source10_.is_AES:
                        d_277_i_ = source10_.AES
                        unmatched10 = False
                        return (d_277_i_).keyId
                if unmatched10:
                    if source10_.is_Static:
                        d_278_i_ = source10_.Static
                        unmatched10 = False
                        return (d_278_i_).keyId
                if unmatched10:
                    if source10_.is_Hierarchy:
                        d_279_i_ = source10_.Hierarchy
                        unmatched10 = False
                        return (d_279_i_).keyId
                if unmatched10:
                    if source10_.is_KmsRsa:
                        d_280_i_ = source10_.KmsRsa
                        unmatched10 = False
                        return (d_280_i_).keyId
                if unmatched10:
                    if source10_.is_RequiredEncryptionContext:
                        d_281_i_ = source10_.RequiredEncryptionContext
                        unmatched10 = False
                        in2_ = (d_281_i_).underlying
                        input = in2_
                        raise _dafny.TailCall()
                if unmatched10:
                    d_282___v0_ = source10_.Multi
                    unmatched10 = False
                    return _dafny.Seq("")
                raise Exception("unexpected control point")
                break

    @staticmethod
    def GetKeyMaterial(keys, keyDescription):
        d_283_keyId_ = default__.GetKeyId(keyDescription)
        if (d_283_keyId_) in (keys):
            return Wrappers.Option_Some((keys)[d_283_keyId_])
        elif True:
            return Wrappers.Option_None()

    @staticmethod
    def ToKeyring(mpl, keys, description):
        output: Wrappers.Result = None
        d_284_material_: Wrappers.Option
        d_284_material_ = default__.GetKeyMaterial(keys, description)
        source11_ = description
        unmatched11 = True
        if unmatched11:
            if source11_.is_Static:
                Static0 = source11_.Static
                d_285_key_ = Static0.keyId
                unmatched11 = False
                if True:
                    d_286_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
                    d_286_valueOrError0_ = Wrappers.default__.Need(((d_284_material_).is_Some) and (((d_284_material_).value).is_StaticMaterial), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not type: StaticMaterial")))
                    if (d_286_valueOrError0_).IsFailure():
                        output = (d_286_valueOrError0_).PropagateFailure()
                        return output
                    d_287_encrypt_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
                    d_287_encrypt_ = AwsCryptographyMaterialProvidersTypes.EncryptionMaterials_EncryptionMaterials(((d_284_material_).value).algorithmSuite, ((d_284_material_).value).encryptionContext, ((d_284_material_).value).encryptedDataKeys, ((d_284_material_).value).requiredEncryptionContextKeys, ((d_284_material_).value).plaintextDataKey, ((d_284_material_).value).signingKey, ((d_284_material_).value).symmetricSigningKeys)
                    d_288_decrypt_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
                    d_288_decrypt_ = AwsCryptographyMaterialProvidersTypes.DecryptionMaterials_DecryptionMaterials(((d_284_material_).value).algorithmSuite, ((d_284_material_).value).encryptionContext, ((d_284_material_).value).requiredEncryptionContextKeys, ((d_284_material_).value).plaintextDataKey, ((d_284_material_).value).verificationKey, Wrappers.Option_None())
                    d_289_keyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
                    out2_: AwsCryptographyMaterialProvidersTypes.IKeyring
                    out2_ = CreateStaticKeyrings.default__.CreateStaticMaterialsKeyring(d_287_encrypt_, d_288_decrypt_)
                    d_289_keyring_ = out2_
                    output = Wrappers.Result_Success(d_289_keyring_)
                    return output
        if unmatched11:
            if source11_.is_Kms:
                Kms0 = source11_.Kms
                d_290_key_ = Kms0.keyId
                unmatched11 = False
                if True:
                    d_291_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
                    d_291_valueOrError1_ = Wrappers.default__.Need(((d_284_material_).is_Some) and (((d_284_material_).value).is_KMS), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not type: KMS")))
                    if (d_291_valueOrError1_).IsFailure():
                        output = (d_291_valueOrError1_).PropagateFailure()
                        return output
                    d_292_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
                    d_293_valueOrError2_: Wrappers.Result = None
                    out3_: Wrappers.Result
                    out3_ = default__.getKmsClient(mpl, ((d_284_material_).value).keyIdentifier)
                    d_293_valueOrError2_ = out3_
                    if (d_293_valueOrError2_).IsFailure():
                        output = (d_293_valueOrError2_).PropagateFailure()
                        return output
                    d_292_kmsClient_ = (d_293_valueOrError2_).Extract()
                    d_294_input_: AwsCryptographyMaterialProvidersTypes.CreateAwsKmsKeyringInput
                    d_294_input_ = AwsCryptographyMaterialProvidersTypes.CreateAwsKmsKeyringInput_CreateAwsKmsKeyringInput(((d_284_material_).value).keyIdentifier, d_292_kmsClient_, Wrappers.Option_None())
                    d_295_keyring_: Wrappers.Result
                    out4_: Wrappers.Result
                    out4_ = (mpl).CreateAwsKmsKeyring(d_294_input_)
                    d_295_keyring_ = out4_
                    def lambda19_(d_296_e_):
                        return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_296_e_)

                    output = (d_295_keyring_).MapFailure(lambda19_)
                    return output
        if unmatched11:
            if source11_.is_KmsMrk:
                KmsMrk0 = source11_.KmsMrk
                d_297_key_ = KmsMrk0.keyId
                unmatched11 = False
                if True:
                    d_298_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
                    d_298_valueOrError3_ = Wrappers.default__.Need(((d_284_material_).is_Some) and (((d_284_material_).value).is_KMS), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not type: KMS")))
                    if (d_298_valueOrError3_).IsFailure():
                        output = (d_298_valueOrError3_).PropagateFailure()
                        return output
                    d_299_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
                    d_300_valueOrError4_: Wrappers.Result = None
                    out5_: Wrappers.Result
                    out5_ = default__.getKmsClient(mpl, ((d_284_material_).value).keyIdentifier)
                    d_300_valueOrError4_ = out5_
                    if (d_300_valueOrError4_).IsFailure():
                        output = (d_300_valueOrError4_).PropagateFailure()
                        return output
                    d_299_kmsClient_ = (d_300_valueOrError4_).Extract()
                    d_301_input_: AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMrkKeyringInput
                    d_301_input_ = AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMrkKeyringInput_CreateAwsKmsMrkKeyringInput(((d_284_material_).value).keyIdentifier, d_299_kmsClient_, Wrappers.Option_None())
                    d_302_keyring_: Wrappers.Result
                    out6_: Wrappers.Result
                    out6_ = (mpl).CreateAwsKmsMrkKeyring(d_301_input_)
                    d_302_keyring_ = out6_
                    def lambda20_(d_303_e_):
                        return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_303_e_)

                    output = (d_302_keyring_).MapFailure(lambda20_)
                    return output
        if unmatched11:
            if source11_.is_KmsRsa:
                KmsRsa0 = source11_.KmsRsa
                d_304_key_ = KmsRsa0.keyId
                d_305_encryptionAlgorithm_ = KmsRsa0.encryptionAlgorithm
                unmatched11 = False
                if True:
                    d_306_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome.default()()
                    d_306_valueOrError5_ = Wrappers.default__.Need(((d_284_material_).is_Some) and (((d_284_material_).value).is_KMSAsymetric), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not type: KMSAsymetric")))
                    if (d_306_valueOrError5_).IsFailure():
                        output = (d_306_valueOrError5_).PropagateFailure()
                        return output
                    d_307_kmsClient_: ComAmazonawsKmsTypes.IKMSClient
                    d_308_valueOrError6_: Wrappers.Result = None
                    out7_: Wrappers.Result
                    out7_ = default__.getKmsClient(mpl, ((d_284_material_).value).keyIdentifier)
                    d_308_valueOrError6_ = out7_
                    if (d_308_valueOrError6_).IsFailure():
                        output = (d_308_valueOrError6_).PropagateFailure()
                        return output
                    d_307_kmsClient_ = (d_308_valueOrError6_).Extract()
                    d_309_input_: AwsCryptographyMaterialProvidersTypes.CreateAwsKmsRsaKeyringInput
                    d_309_input_ = AwsCryptographyMaterialProvidersTypes.CreateAwsKmsRsaKeyringInput_CreateAwsKmsRsaKeyringInput(Wrappers.Option_Some(((d_284_material_).value).publicKey), ((d_284_material_).value).keyIdentifier, d_305_encryptionAlgorithm_, Wrappers.Option_Some(d_307_kmsClient_), Wrappers.Option_None())
                    d_310_keyring_: Wrappers.Result
                    out8_: Wrappers.Result
                    out8_ = (mpl).CreateAwsKmsRsaKeyring(d_309_input_)
                    d_310_keyring_ = out8_
                    def lambda21_(d_311_e_):
                        return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_311_e_)

                    output = (d_310_keyring_).MapFailure(lambda21_)
                    return output
        if unmatched11:
            if source11_.is_Hierarchy:
                Hierarchy0 = source11_.Hierarchy
                d_312_key_ = Hierarchy0.keyId
                unmatched11 = False
                if True:
                    d_313_valueOrError7_: Wrappers.Outcome = Wrappers.Outcome.default()()
                    d_313_valueOrError7_ = Wrappers.default__.Need(((d_284_material_).is_Some) and (((d_284_material_).value).is_StaticKeyStoreInformation), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not type: StaticKeyStoreInformation")))
                    if (d_313_valueOrError7_).IsFailure():
                        output = (d_313_valueOrError7_).PropagateFailure()
                        return output
                    d_314_keyStore_: AwsCryptographyKeyStoreTypes.IKeyStoreClient
                    out9_: AwsCryptographyKeyStoreTypes.IKeyStoreClient
                    out9_ = CreateStaticKeyStores.default__.CreateStaticKeyStore((d_284_material_).value)
                    d_314_keyStore_ = out9_
                    d_315_input_: AwsCryptographyMaterialProvidersTypes.CreateAwsKmsHierarchicalKeyringInput
                    d_315_input_ = AwsCryptographyMaterialProvidersTypes.CreateAwsKmsHierarchicalKeyringInput_CreateAwsKmsHierarchicalKeyringInput(Wrappers.Option_Some(((d_284_material_).value).keyIdentifier), Wrappers.Option_None(), d_314_keyStore_, 0, Wrappers.Option_None())
                    d_316_keyring_: Wrappers.Result
                    out10_: Wrappers.Result
                    out10_ = (mpl).CreateAwsKmsHierarchicalKeyring(d_315_input_)
                    d_316_keyring_ = out10_
                    def lambda22_(d_317_e_):
                        return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_317_e_)

                    output = (d_316_keyring_).MapFailure(lambda22_)
                    return output
        if unmatched11:
            if source11_.is_KmsMrkDiscovery:
                KmsMrkDiscovery0 = source11_.KmsMrkDiscovery
                d_318___v1_ = KmsMrkDiscovery0.keyId
                d_319_defaultMrkRegion_ = KmsMrkDiscovery0.defaultMrkRegion
                d_320_awsKmsDiscoveryFilter_ = KmsMrkDiscovery0.awsKmsDiscoveryFilter
                unmatched11 = False
                if True:
                    d_321_valueOrError8_: Wrappers.Outcome = Wrappers.Outcome.default()()
                    d_321_valueOrError8_ = Wrappers.default__.Need((d_284_material_).is_None, AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Discovery has not key")))
                    if (d_321_valueOrError8_).IsFailure():
                        output = (d_321_valueOrError8_).PropagateFailure()
                        return output
                    d_322_input_: AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMrkDiscoveryMultiKeyringInput
                    d_322_input_ = AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMrkDiscoveryMultiKeyringInput_CreateAwsKmsMrkDiscoveryMultiKeyringInput(_dafny.Seq([d_319_defaultMrkRegion_]), d_320_awsKmsDiscoveryFilter_, Wrappers.Option_None(), Wrappers.Option_None())
                    d_323_keyring_: Wrappers.Result
                    out11_: Wrappers.Result
                    out11_ = (mpl).CreateAwsKmsMrkDiscoveryMultiKeyring(d_322_input_)
                    d_323_keyring_ = out11_
                    def lambda23_(d_324_e_):
                        return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_324_e_)

                    output = (d_323_keyring_).MapFailure(lambda23_)
                    return output
        if unmatched11:
            if source11_.is_AES:
                AES0 = source11_.AES
                d_325_key_ = AES0.keyId
                d_326_providerId_ = AES0.providerId
                unmatched11 = False
                if True:
                    d_327_valueOrError9_: Wrappers.Outcome = Wrappers.Outcome.default()()
                    d_327_valueOrError9_ = Wrappers.default__.Need(((d_284_material_).is_Some) and (((d_284_material_).value).is_Symetric), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not type: Symmetric")))
                    if (d_327_valueOrError9_).IsFailure():
                        output = (d_327_valueOrError9_).PropagateFailure()
                        return output
                    d_328_wrappingAlg_: AwsCryptographyMaterialProvidersTypes.AesWrappingAlg
                    d_329_valueOrError10_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyMaterialProvidersTypes.AesWrappingAlg.default())()
                    def lambda24_():
                        source12_ = ((d_284_material_).value).bits
                        unmatched12 = True
                        if unmatched12:
                            if (source12_) == (128):
                                unmatched12 = False
                                return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES128__GCM__IV12__TAG16())
                        if unmatched12:
                            if (source12_) == (192):
                                unmatched12 = False
                                return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES192__GCM__IV12__TAG16())
                        if unmatched12:
                            if (source12_) == (256):
                                unmatched12 = False
                                return Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.AesWrappingAlg_ALG__AES256__GCM__IV12__TAG16())
                        if unmatched12:
                            d_330___v2_ = source12_
                            unmatched12 = False
                            return Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not a supported bit length")))
                        raise Exception("unexpected control point")

                    d_329_valueOrError10_ = lambda24_()
                    if (d_329_valueOrError10_).IsFailure():
                        output = (d_329_valueOrError10_).PropagateFailure()
                        return output
                    d_328_wrappingAlg_ = (d_329_valueOrError10_).Extract()
                    d_331_input_: AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput
                    d_331_input_ = AwsCryptographyMaterialProvidersTypes.CreateRawAesKeyringInput_CreateRawAesKeyringInput(d_326_providerId_, ((d_284_material_).value).keyIdentifier, ((d_284_material_).value).wrappingKey, d_328_wrappingAlg_)
                    d_332_keyring_: Wrappers.Result
                    out12_: Wrappers.Result
                    out12_ = (mpl).CreateRawAesKeyring(d_331_input_)
                    d_332_keyring_ = out12_
                    def lambda25_(d_333_e_):
                        return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_333_e_)

                    output = (d_332_keyring_).MapFailure(lambda25_)
                    return output
        if unmatched11:
            if source11_.is_RSA:
                RSA0 = source11_.RSA
                d_334_key_ = RSA0.keyId
                d_335_providerId_ = RSA0.providerId
                d_336_padding_ = RSA0.padding
                unmatched11 = False
                if True:
                    d_337_valueOrError11_: Wrappers.Outcome = Wrappers.Outcome.default()()
                    d_337_valueOrError11_ = Wrappers.default__.Need(((d_284_material_).is_Some) and ((((d_284_material_).value).is_PrivateRSA) or (((d_284_material_).value).is_PublicRSA)), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Not type: PrivateRSA or PublicRSA")))
                    if (d_337_valueOrError11_).IsFailure():
                        output = (d_337_valueOrError11_).PropagateFailure()
                        return output
                    source13_ = d_284_material_
                    unmatched13 = True
                    if unmatched13:
                        if source13_.is_Some:
                            value0 = source13_.value
                            if value0.is_PrivateRSA:
                                d_338___v3_ = value0.name
                                d_339___v4_ = value0.encrypt
                                d_340_decrypt_ = value0.decrypt
                                d_341___v5_ = value0.algorithm
                                d_342___v6_ = value0.bits
                                d_343___v7_ = value0.encoding
                                d_344_material_ = value0.material
                                d_345_keyIdentifier_ = value0.keyIdentifier
                                unmatched13 = False
                                if True:
                                    d_346_valueOrError12_: Wrappers.Outcome = Wrappers.Outcome.default()()
                                    d_346_valueOrError12_ = Wrappers.default__.Need(d_340_decrypt_, AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Private RSA keys only supports decrypt.")))
                                    if (d_346_valueOrError12_).IsFailure():
                                        output = (d_346_valueOrError12_).PropagateFailure()
                                        return output
                                    d_347_privateKeyPemBytes_: _dafny.Seq
                                    d_348_valueOrError13_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
                                    def lambda26_(d_349_e_):
                                        return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(d_349_e_)

                                    d_348_valueOrError13_ = (UTF8.default__.Encode(d_344_material_)).MapFailure(lambda26_)
                                    if (d_348_valueOrError13_).IsFailure():
                                        output = (d_348_valueOrError13_).PropagateFailure()
                                        return output
                                    d_347_privateKeyPemBytes_ = (d_348_valueOrError13_).Extract()
                                    d_350_input_: AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput
                                    d_350_input_ = AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_335_providerId_, d_345_keyIdentifier_, d_336_padding_, Wrappers.Option_None(), Wrappers.Option_Some(d_347_privateKeyPemBytes_))
                                    d_351_keyring_: Wrappers.Result
                                    out13_: Wrappers.Result
                                    out13_ = (mpl).CreateRawRsaKeyring(d_350_input_)
                                    d_351_keyring_ = out13_
                                    def lambda27_(d_352_e_):
                                        return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_352_e_)

                                    output = (d_351_keyring_).MapFailure(lambda27_)
                                    return output
                    if unmatched13:
                        value1 = source13_.value
                        d_353___v8_ = value1.name
                        d_354_encrypt_ = value1.encrypt
                        d_355___v9_ = value1.decrypt
                        d_356___v10_ = value1.bits
                        d_357___v11_ = value1.algorithm
                        d_358___v12_ = value1.encoding
                        d_359_material_ = value1.material
                        d_360_keyIdentifier_ = value1.keyIdentifier
                        unmatched13 = False
                        if True:
                            d_361_valueOrError14_: Wrappers.Outcome = Wrappers.Outcome.default()()
                            d_361_valueOrError14_ = Wrappers.default__.Need(d_354_encrypt_, AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Public RSA keys only supports encrypt.")))
                            if (d_361_valueOrError14_).IsFailure():
                                output = (d_361_valueOrError14_).PropagateFailure()
                                return output
                            d_362_publicKeyPemBytes_: _dafny.Seq
                            d_363_valueOrError15_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
                            def lambda28_(d_364_e_):
                                return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(d_364_e_)

                            d_363_valueOrError15_ = (UTF8.default__.Encode(d_359_material_)).MapFailure(lambda28_)
                            if (d_363_valueOrError15_).IsFailure():
                                output = (d_363_valueOrError15_).PropagateFailure()
                                return output
                            d_362_publicKeyPemBytes_ = (d_363_valueOrError15_).Extract()
                            d_365_input_: AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput
                            d_365_input_ = AwsCryptographyMaterialProvidersTypes.CreateRawRsaKeyringInput_CreateRawRsaKeyringInput(d_335_providerId_, d_360_keyIdentifier_, d_336_padding_, Wrappers.Option_Some(d_362_publicKeyPemBytes_), Wrappers.Option_None())
                            d_366_keyring_: Wrappers.Result
                            out14_: Wrappers.Result
                            out14_ = (mpl).CreateRawRsaKeyring(d_365_input_)
                            d_366_keyring_ = out14_
                            def lambda29_(d_367_e_):
                                return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_367_e_)

                            output = (d_366_keyring_).MapFailure(lambda29_)
                            return output
        if unmatched11:
            d_368_MultiKeyring_ = source11_.Multi
            unmatched11 = False
            if True:
                d_369_generator_: Wrappers.Option
                d_369_generator_ = Wrappers.Option_None()
                if ((d_368_MultiKeyring_).generator).is_Some:
                    d_370_valueOrError16_: Wrappers.Outcome = Wrappers.Outcome.default()()
                    d_370_valueOrError16_ = Wrappers.default__.Need(KeyDescription.default__.Keyring_q(((d_368_MultiKeyring_).generator).value), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Only Keyring key descriptions are supported.")))
                    if (d_370_valueOrError16_).IsFailure():
                        output = (d_370_valueOrError16_).PropagateFailure()
                        return output
                    d_371_generator_k_: AwsCryptographyMaterialProvidersTypes.IKeyring
                    d_372_valueOrError17_: Wrappers.Result = None
                    out15_: Wrappers.Result
                    out15_ = default__.ToKeyring(mpl, keys, ((d_368_MultiKeyring_).generator).value)
                    d_372_valueOrError17_ = out15_
                    if (d_372_valueOrError17_).IsFailure():
                        output = (d_372_valueOrError17_).PropagateFailure()
                        return output
                    d_371_generator_k_ = (d_372_valueOrError17_).Extract()
                    d_369_generator_ = Wrappers.Option_Some(d_371_generator_k_)
                d_373_childKeyrings_: _dafny.Seq
                d_373_childKeyrings_ = _dafny.Seq([])
                hi0_ = len((d_368_MultiKeyring_).childKeyrings)
                for d_374_i_ in range(0, hi0_):
                    d_375_child_: AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription
                    d_375_child_ = ((d_368_MultiKeyring_).childKeyrings)[d_374_i_]
                    d_376_valueOrError18_: Wrappers.Outcome = Wrappers.Outcome.default()()
                    d_376_valueOrError18_ = Wrappers.default__.Need(KeyDescription.default__.Keyring_q(d_375_child_), AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_KeyVectorException(_dafny.Seq("Only Keyring key descriptions are supported.")))
                    if (d_376_valueOrError18_).IsFailure():
                        output = (d_376_valueOrError18_).PropagateFailure()
                        return output
                    d_377_childKeyring_: AwsCryptographyMaterialProvidersTypes.IKeyring
                    d_378_valueOrError19_: Wrappers.Result = None
                    out16_: Wrappers.Result
                    out16_ = default__.ToKeyring(mpl, keys, d_375_child_)
                    d_378_valueOrError19_ = out16_
                    if (d_378_valueOrError19_).IsFailure():
                        output = (d_378_valueOrError19_).PropagateFailure()
                        return output
                    d_377_childKeyring_ = (d_378_valueOrError19_).Extract()
                    d_373_childKeyrings_ = (d_373_childKeyrings_) + (_dafny.Seq([d_377_childKeyring_]))
                d_379_input_: AwsCryptographyMaterialProvidersTypes.CreateMultiKeyringInput
                d_379_input_ = AwsCryptographyMaterialProvidersTypes.CreateMultiKeyringInput_CreateMultiKeyringInput(d_369_generator_, d_373_childKeyrings_)
                d_380_keyring_: Wrappers.Result
                out17_: Wrappers.Result
                out17_ = (mpl).CreateMultiKeyring(d_379_input_)
                d_380_keyring_ = out17_
                def lambda30_(d_381_e_):
                    return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_381_e_)

                output = (d_380_keyring_).MapFailure(lambda30_)
                return output
        return output

    @staticmethod
    def getKmsClient(mpl, maybeKmsArn):
        output: Wrappers.Result = None
        d_382_maybeClientSupplier_: Wrappers.Result
        out18_: Wrappers.Result
        out18_ = (mpl).CreateDefaultClientSupplier(AwsCryptographyMaterialProvidersTypes.CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput())
        d_382_maybeClientSupplier_ = out18_
        d_383_clientSupplier_: AwsCryptographyMaterialProvidersTypes.IClientSupplier
        d_384_valueOrError0_: Wrappers.Result = None
        def lambda31_(d_385_e_):
            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_385_e_)

        d_384_valueOrError0_ = (d_382_maybeClientSupplier_).MapFailure(lambda31_)
        if (d_384_valueOrError0_).IsFailure():
            output = (d_384_valueOrError0_).PropagateFailure()
            return output
        d_383_clientSupplier_ = (d_384_valueOrError0_).Extract()
        d_386_arn_: Wrappers.Result
        d_386_arn_ = AwsArnParsing.default__.IsAwsKmsIdentifierString(maybeKmsArn)
        d_387_region_: Wrappers.Option
        d_387_region_ = (AwsArnParsing.default__.GetRegion((d_386_arn_).value) if (d_386_arn_).is_Success else Wrappers.Option_None())
        d_388_tmp_: Wrappers.Result
        out19_: Wrappers.Result
        out19_ = (d_383_clientSupplier_).GetClient(AwsCryptographyMaterialProvidersTypes.GetClientInput_GetClientInput((d_387_region_).UnwrapOr(_dafny.Seq(""))))
        d_388_tmp_ = out19_
        def lambda32_(d_389_e_):
            return AwsCryptographyMaterialProvidersTestVectorKeysTypes.Error_AwsCryptographyMaterialProviders(d_389_e_)

        output = (d_388_tmp_).MapFailure(lambda32_)
        return output


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

