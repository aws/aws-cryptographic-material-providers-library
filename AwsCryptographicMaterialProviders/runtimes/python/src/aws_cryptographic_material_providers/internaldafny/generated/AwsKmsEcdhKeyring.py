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
import aws_cryptographic_material_providers.internaldafny.generated.Constants as Constants
import aws_cryptographic_material_providers.internaldafny.generated.MaterialWrapping as MaterialWrapping
import aws_cryptographic_material_providers.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_material_providers.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_material_providers.internaldafny.generated.EdkWrapping as EdkWrapping
import aws_cryptographic_material_providers.internaldafny.generated.ErrorMessages as ErrorMessages
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsKeyring as AwsKmsKeyring
import aws_cryptographic_material_providers.internaldafny.generated.StrictMultiKeyring as StrictMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsDiscoveryKeyring as AwsKmsDiscoveryKeyring
import aws_cryptographic_material_providers.internaldafny.generated.DiscoveryMultiKeyring as DiscoveryMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkDiscoveryKeyring as AwsKmsMrkDiscoveryKeyring
import aws_cryptographic_material_providers.internaldafny.generated.MrkAwareDiscoveryMultiKeyring as MrkAwareDiscoveryMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkKeyring as AwsKmsMrkKeyring
import aws_cryptographic_material_providers.internaldafny.generated.MrkAwareStrictMultiKeyring as MrkAwareStrictMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.LocalCMC as LocalCMC
import aws_cryptographic_material_providers.internaldafny.generated.SynchronizedLocalCMC as SynchronizedLocalCMC
import aws_cryptographic_material_providers.internaldafny.generated.StormTracker as StormTracker
import aws_cryptographic_material_providers.internaldafny.generated.StormTrackingCMC as StormTrackingCMC
import aws_cryptographic_material_providers.internaldafny.generated.CacheConstants as CacheConstants
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsHierarchicalKeyring as AwsKmsHierarchicalKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsRsaKeyring as AwsKmsRsaKeyring
import aws_cryptographic_material_providers.internaldafny.generated.EcdhEdkWrapping as EcdhEdkWrapping
import aws_cryptographic_material_providers.internaldafny.generated.RawECDHKeyring as RawECDHKeyring

# Module: AwsKmsEcdhKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DeriveSharedSecret(client, senderAwsKmsKey, recipientPublicKey, grantTokens):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_0_deriveSharedSecretRequest_: ComAmazonawsKmsTypes.DeriveSharedSecretRequest
        d_0_deriveSharedSecretRequest_ = ComAmazonawsKmsTypes.DeriveSharedSecretRequest_DeriveSharedSecretRequest(senderAwsKmsKey, ComAmazonawsKmsTypes.KeyAgreementAlgorithmSpec_ECDH(), recipientPublicKey, Wrappers.Option_Some(grantTokens), Wrappers.Option_None(), Wrappers.Option_None())
        d_1_maybeDeriveSharedSecret_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = (client).DeriveSharedSecret(d_0_deriveSharedSecretRequest_)
        d_1_maybeDeriveSharedSecret_ = out0_
        d_2_valueOrError0_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.DeriveSharedSecretResponse.default())()
        def lambda0_(d_3_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_ComAmazonawsKms(d_3_e_)

        d_2_valueOrError0_ = (d_1_maybeDeriveSharedSecret_).MapFailure(lambda0_)
        if (d_2_valueOrError0_).IsFailure():
            res = (d_2_valueOrError0_).PropagateFailure()
            return res
        d_4_deriveSharedSecretResponse_: ComAmazonawsKmsTypes.DeriveSharedSecretResponse
        d_4_deriveSharedSecretResponse_ = (d_2_valueOrError0_).Extract()
        d_5_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_5_valueOrError1_ = Wrappers.default__.Need(((((((d_4_deriveSharedSecretResponse_).KeyId).is_Some) and (((d_4_deriveSharedSecretResponse_).SharedSecret).is_Some)) and (((d_4_deriveSharedSecretResponse_).KeyAgreementAlgorithm).is_Some)) and ((((d_4_deriveSharedSecretResponse_).KeyId).value) == (senderAwsKmsKey))) and ((((d_4_deriveSharedSecretResponse_).KeyAgreementAlgorithm).value) == (ComAmazonawsKmsTypes.KeyAgreementAlgorithmSpec_ECDH())), default__.E(_dafny.Seq("Invalid response from KMS DeriveSharedSecret")))
        if (d_5_valueOrError1_).IsFailure():
            res = (d_5_valueOrError1_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(((d_4_deriveSharedSecretResponse_).SharedSecret).value)
        return res
        return res

    @staticmethod
    def E(s):
        return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(s)

    @_dafny.classproperty
    def AWS__KMS__ECDH__KEYRING__VERSION(instance):
        return RawECDHKeyring.default__.RAW__ECDH__KEYRING__VERSION

class AwsKmsEcdhKeyring(Keyring.VerifiableInterface, AwsCryptographyMaterialProvidersTypes.IKeyring):
    def  __init__(self):
        self._client: ComAmazonawsKmsTypes.IKMSClient = None
        self._cryptoPrimitives: AtomicPrimitives.AtomicPrimitivesClient = None
        self._keyAgreementScheme: AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations = AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations.default()()
        self._curveSpec: AwsCryptographyPrimitivesTypes.ECDHCurveSpec = AwsCryptographyPrimitivesTypes.ECDHCurveSpec.default()()
        self._grantTokens: _dafny.Seq = None
        self._recipientPublicKey: _dafny.Seq = None
        self._senderPublicKey: Wrappers.Option = Wrappers.Option.default()()
        self._compressedSenderPublicKey: Wrappers.Option = Wrappers.Option.default()()
        self._compressedRecipientPublicKey: _dafny.Seq = _dafny.Seq({})
        self._senderKmsKeyId: Wrappers.Option = Wrappers.Option.default()()
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsEcdhKeyring.AwsKmsEcdhKeyring"
    def OnDecrypt(self, input):
        out9_: Wrappers.Result
        out9_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnDecrypt(self, input)
        return out9_

    def OnEncrypt(self, input):
        out9_: Wrappers.Result
        out9_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnEncrypt(self, input)
        return out9_

    def ctor__(self, KeyAgreementScheme, curveSpec, client, grantTokens, senderKmsKeyId, senderPublicKey, recipientPublicKey, compressedSenderPublicKey, compressedRecipientPublicKey, cryptoPrimitives):
        (self)._keyAgreementScheme = KeyAgreementScheme
        (self)._curveSpec = curveSpec
        (self)._client = client
        (self)._grantTokens = grantTokens
        (self)._recipientPublicKey = recipientPublicKey
        (self)._senderPublicKey = senderPublicKey
        (self)._compressedSenderPublicKey = compressedSenderPublicKey
        (self)._compressedRecipientPublicKey = compressedRecipientPublicKey
        (self)._senderKmsKeyId = senderKmsKeyId
        (self)._cryptoPrimitives = cryptoPrimitives

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        d_0_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_0_valueOrError0_ = Wrappers.default__.Need(not(((self).keyAgreementScheme).is_KmsPublicKeyDiscovery), default__.E(_dafny.Seq("KmsPublicKeyDiscovery Key Agreement Scheme is forbidden on encrypt.")))
        if (d_0_valueOrError0_).IsFailure():
            res = (d_0_valueOrError0_).PropagateFailure()
            return res
        d_1_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1_valueOrError1_ = Wrappers.default__.Need(((self).senderKmsKeyId).is_Some, default__.E(_dafny.Seq("Keyring MUST be configured with a sender KMS Key ID")))
        if (d_1_valueOrError1_).IsFailure():
            res = (d_1_valueOrError1_).PropagateFailure()
            return res
        d_2_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_2_valueOrError2_ = Wrappers.default__.Need(((self).senderPublicKey).is_Some, default__.E(_dafny.Seq("Keyring MUST be configured with a senderPublicKey")))
        if (d_2_valueOrError2_).IsFailure():
            res = (d_2_valueOrError2_).PropagateFailure()
            return res
        d_3_senderKmsKeyId_: _dafny.Seq
        d_3_senderKmsKeyId_ = ((self).senderKmsKeyId).value
        d_4_materials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_4_materials_ = (input).materials
        d_5_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_5_suite_ = ((input).materials).algorithmSuite
        d_6_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        d_6_valueOrError3_ = AwsKmsUtils.default__.StringifyEncryptionContext(((input).materials).encryptionContext)
        if (d_6_valueOrError3_).IsFailure():
            res = (d_6_valueOrError3_).PropagateFailure()
            return res
        d_7_stringifiedEncCtx_: _dafny.Map
        d_7_stringifiedEncCtx_ = (d_6_valueOrError3_).Extract()
        d_8_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out0_: Wrappers.Result
        out0_ = default__.DeriveSharedSecret((self).client, d_3_senderKmsKeyId_, (self).recipientPublicKey, (self).grantTokens)
        d_8_valueOrError4_ = out0_
        if (d_8_valueOrError4_).IsFailure():
            res = (d_8_valueOrError4_).PropagateFailure()
            return res
        d_9_sharedSecret_: _dafny.Seq
        d_9_sharedSecret_ = (d_8_valueOrError4_).Extract()
        d_10_operationCompressedSenderPublicKey_: _dafny.Seq
        if ((self).compressedSenderPublicKey).is_None:
            d_10_operationCompressedSenderPublicKey_ = _dafny.Seq([])
        elif True:
            d_10_operationCompressedSenderPublicKey_ = ((self).compressedSenderPublicKey).value
        d_11_valueOrError5_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_11_valueOrError5_ = (UTF8.default__.Encode(RawECDHKeyring.default__.CurveSpecTypeToString((self).curveSpec))).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_11_valueOrError5_).IsFailure():
            res = (d_11_valueOrError5_).PropagateFailure()
            return res
        d_12_curveSpecUtf8_: _dafny.Seq
        d_12_curveSpecUtf8_ = (d_11_valueOrError5_).Extract()
        d_13_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_13_valueOrError6_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD(((input).materials).encryptionContext)
        if (d_13_valueOrError6_).IsFailure():
            res = (d_13_valueOrError6_).PropagateFailure()
            return res
        d_14_canonicalizedEC_: _dafny.Seq
        d_14_canonicalizedEC_ = (d_13_valueOrError6_).Extract()
        d_15_fixedInfo_: _dafny.Seq
        d_15_fixedInfo_ = EcdhEdkWrapping.default__.SerializeFixedInfo(Constants.default__.ECDH__KDF__UTF8, d_12_curveSpecUtf8_, d_10_operationCompressedSenderPublicKey_, (self).compressedRecipientPublicKey, d_14_canonicalizedEC_, default__.AWS__KMS__ECDH__KEYRING__VERSION)
        d_16_ecdhGenerateAndWrap_: EcdhEdkWrapping.EcdhGenerateAndWrapKeyMaterial
        nw0_ = EcdhEdkWrapping.EcdhGenerateAndWrapKeyMaterial()
        nw0_.ctor__(d_9_sharedSecret_, d_15_fixedInfo_, (self).cryptoPrimitives)
        d_16_ecdhGenerateAndWrap_ = nw0_
        d_17_ecdhWrap_: EcdhEdkWrapping.EcdhWrapKeyMaterial
        nw1_ = EcdhEdkWrapping.EcdhWrapKeyMaterial()
        nw1_.ctor__(d_9_sharedSecret_, d_15_fixedInfo_, (self).cryptoPrimitives)
        d_17_ecdhWrap_ = nw1_
        d_18_valueOrError7_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.WrapEdkMaterialOutput.default(EcdhEdkWrapping.EcdhWrapInfo.default()))()
        out1_: Wrappers.Result
        out1_ = EdkWrapping.default__.WrapEdkMaterial(d_4_materials_, d_17_ecdhWrap_, d_16_ecdhGenerateAndWrap_)
        d_18_valueOrError7_ = out1_
        if (d_18_valueOrError7_).IsFailure():
            res = (d_18_valueOrError7_).PropagateFailure()
            return res
        d_19_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_19_wrapOutput_ = (d_18_valueOrError7_).Extract()
        d_20_symmetricSigningKeyList_: Wrappers.Option
        if ((d_19_wrapOutput_).symmetricSigningKey).is_Some:
            d_20_symmetricSigningKeyList_ = Wrappers.Option_Some(_dafny.Seq([((d_19_wrapOutput_).symmetricSigningKey).value]))
        elif True:
            d_20_symmetricSigningKeyList_ = Wrappers.Option_None()
        d_21_valueOrError8_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_21_valueOrError8_ = Wrappers.default__.Need((RawECDHKeyring.default__.ValidCompressedPublicKeyLength(d_10_operationCompressedSenderPublicKey_)) and (RawECDHKeyring.default__.ValidCompressedPublicKeyLength((self).compressedRecipientPublicKey)), default__.E(_dafny.Seq("Invalid compressed public key length.")))
        if (d_21_valueOrError8_).IsFailure():
            res = (d_21_valueOrError8_).PropagateFailure()
            return res
        d_22_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_22_edk_ = AwsCryptographyMaterialProvidersTypes.EncryptedDataKey_EncryptedDataKey(Constants.default__.KMS__ECDH__PROVIDER__ID, RawECDHKeyring.default__.SerializeProviderInfo(d_10_operationCompressedSenderPublicKey_, (self).compressedRecipientPublicKey), (d_19_wrapOutput_).wrappedMaterial)
        if (d_19_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_23_valueOrError9_: Wrappers.Result = None
            d_23_valueOrError9_ = Materials.default__.EncryptionMaterialAddDataKey(d_4_materials_, (d_19_wrapOutput_).plaintextDataKey, _dafny.Seq([d_22_edk_]), d_20_symmetricSigningKeyList_)
            if (d_23_valueOrError9_).IsFailure():
                res = (d_23_valueOrError9_).PropagateFailure()
                return res
            d_24_result_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_24_result_ = (d_23_valueOrError9_).Extract()
            res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(d_24_result_))
            return res
        elif (d_19_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_25_valueOrError10_: Wrappers.Result = None
            d_25_valueOrError10_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys(d_4_materials_, _dafny.Seq([d_22_edk_]), d_20_symmetricSigningKeyList_)
            if (d_25_valueOrError10_).IsFailure():
                res = (d_25_valueOrError10_).PropagateFailure()
                return res
            d_26_result_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_26_result_ = (d_25_valueOrError10_).Extract()
            res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(d_26_result_))
            return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_0_materials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_0_materials_ = (input).materials
        d_1_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_1_suite_ = ((input).materials).algorithmSuite
        d_2_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_2_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_0_materials_), default__.E(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_2_valueOrError0_).IsFailure():
            res = (d_2_valueOrError0_).PropagateFailure()
            return res
        d_3_filter_: OnDecryptEcdhDataKeyFilter
        nw0_ = OnDecryptEcdhDataKeyFilter()
        nw0_.ctor__((self).keyAgreementScheme, (self).compressedRecipientPublicKey, (self).compressedSenderPublicKey)
        d_3_filter_ = nw0_
        d_4_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out0_: Wrappers.Result
        out0_ = Actions.default__.FilterWithResult(d_3_filter_, (input).encryptedDataKeys)
        d_4_valueOrError1_ = out0_
        if (d_4_valueOrError1_).IsFailure():
            res = (d_4_valueOrError1_).PropagateFailure()
            return res
        d_5_edksToAttempt_: _dafny.Seq
        d_5_edksToAttempt_ = (d_4_valueOrError1_).Extract()
        if (0) == (len(d_5_edksToAttempt_)):
            d_6_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            d_6_valueOrError2_ = ErrorMessages.default__.IncorrectDataKeys((input).encryptedDataKeys, ((input).materials).algorithmSuite, _dafny.Seq(""))
            if (d_6_valueOrError2_).IsFailure():
                res = (d_6_valueOrError2_).PropagateFailure()
                return res
            d_7_errorMessage_: _dafny.Seq
            d_7_errorMessage_ = (d_6_valueOrError2_).Extract()
            res = Wrappers.Result_Failure(default__.E(d_7_errorMessage_))
            return res
        d_8_decryptClosure_: Actions.ActionWithResult
        nw1_ = DecryptSingleEncryptedDataKey()
        nw1_.ctor__(d_0_materials_, (self).cryptoPrimitives, (self).compressedRecipientPublicKey, (self).client, (self).grantTokens, (self).keyAgreementScheme, (self).curveSpec)
        d_8_decryptClosure_ = nw1_
        d_9_outcome_: Wrappers.Result
        out1_: Wrappers.Result
        out1_ = Actions.default__.ReduceToSuccess(d_8_decryptClosure_, d_5_edksToAttempt_)
        d_9_outcome_ = out1_
        d_10_valueOrError3_: Wrappers.Result = None
        def lambda0_(d_11_errors_):
            return AwsCryptographyMaterialProvidersTypes.Error_CollectionOfErrors(d_11_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."))

        d_10_valueOrError3_ = (d_9_outcome_).MapFailure(lambda0_)
        if (d_10_valueOrError3_).IsFailure():
            res = (d_10_valueOrError3_).PropagateFailure()
            return res
        d_12_SealedDecryptionMaterials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_12_SealedDecryptionMaterials_ = (d_10_valueOrError3_).Extract()
        res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnDecryptOutput_OnDecryptOutput(d_12_SealedDecryptionMaterials_))
        return res
        return res

    @property
    def client(self):
        return self._client
    @property
    def cryptoPrimitives(self):
        return self._cryptoPrimitives
    @property
    def keyAgreementScheme(self):
        return self._keyAgreementScheme
    @property
    def curveSpec(self):
        return self._curveSpec
    @property
    def grantTokens(self):
        return self._grantTokens
    @property
    def recipientPublicKey(self):
        return self._recipientPublicKey
    @property
    def senderPublicKey(self):
        return self._senderPublicKey
    @property
    def compressedSenderPublicKey(self):
        return self._compressedSenderPublicKey
    @property
    def compressedRecipientPublicKey(self):
        return self._compressedRecipientPublicKey
    @property
    def senderKmsKeyId(self):
        return self._senderKmsKeyId

class DecryptSingleEncryptedDataKey(Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._materials: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials = None
        self._cryptoPrimitives: AtomicPrimitives.AtomicPrimitivesClient = None
        self._recipientPublicKey: _dafny.Seq = _dafny.Seq({})
        self._keyAgreementScheme: AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations = AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations.default()()
        self._client: ComAmazonawsKmsTypes.IKMSClient = None
        self._curveSpec: AwsCryptographyPrimitivesTypes.ECDHCurveSpec = AwsCryptographyPrimitivesTypes.ECDHCurveSpec.default()()
        self._grantTokens: _dafny.Seq = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsEcdhKeyring.DecryptSingleEncryptedDataKey"
    def ctor__(self, materials, cryptoPrimitives, recipientPublicKey, client, grantTokens, keyAgreementScheme, curveSpec):
        (self)._materials = materials
        (self)._cryptoPrimitives = cryptoPrimitives
        (self)._recipientPublicKey = recipientPublicKey
        (self)._keyAgreementScheme = keyAgreementScheme
        (self)._client = client
        (self)._curveSpec = curveSpec
        (self)._grantTokens = grantTokens

    def Invoke(self, edk):
        res: Wrappers.Result = None
        d_0_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_0_valueOrError0_ = Wrappers.default__.Need(UTF8.default__.ValidUTF8Seq((edk).keyProviderId), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received invalid EDK provider id for AWS KMS ECDH Keyring")))
        if (d_0_valueOrError0_).IsFailure():
            res = (d_0_valueOrError0_).PropagateFailure()
            return res
        d_1_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_1_suite_ = ((self).materials).algorithmSuite
        d_2_keyProviderId_: _dafny.Seq
        d_2_keyProviderId_ = (edk).keyProviderId
        d_3_providerInfo_: _dafny.Seq
        d_3_providerInfo_ = (edk).keyProviderInfo
        d_4_ciphertext_: _dafny.Seq
        d_4_ciphertext_ = (edk).ciphertext
        d_5_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_5_valueOrError1_ = EdkWrapping.default__.GetProviderWrappedMaterial(d_4_ciphertext_, d_1_suite_)
        if (d_5_valueOrError1_).IsFailure():
            res = (d_5_valueOrError1_).PropagateFailure()
            return res
        d_6_providerWrappedMaterial_: _dafny.Seq
        d_6_providerWrappedMaterial_ = (d_5_valueOrError1_).Extract()
        d_7_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_7_valueOrError2_ = Wrappers.default__.Need(((len(d_3_providerInfo_)) <= (Constants.default__.ECDH__PROVIDER__INFO__521__LEN)) and (RawECDHKeyring.default__.ValidProviderInfoLength(d_3_providerInfo_)), default__.E(_dafny.Seq("EDK ProviderInfo longer than expected")))
        if (d_7_valueOrError2_).IsFailure():
            res = (d_7_valueOrError2_).PropagateFailure()
            return res
        d_8_keyringVersion_: int
        d_8_keyringVersion_ = (d_3_providerInfo_)[0]
        d_9_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_9_valueOrError3_ = Wrappers.default__.Need((_dafny.Seq([d_8_keyringVersion_])) == (default__.AWS__KMS__ECDH__KEYRING__VERSION), default__.E(_dafny.Seq("Incorrect Keyring version found in provider info.")))
        if (d_9_valueOrError3_).IsFailure():
            res = (d_9_valueOrError3_).PropagateFailure()
            return res
        d_10_recipientPublicKeyLength_: int
        d_10_recipientPublicKeyLength_ = StandardLibrary_UInt.default__.SeqToUInt32(_dafny.Seq((d_3_providerInfo_)[Constants.default__.ECDH__PROVIDER__INFO__RPL__INDEX:Constants.default__.ECDH__PROVIDER__INFO__RPK__INDEX:]))
        d_11_recipientPublicKeyLengthIndex_: int
        d_11_recipientPublicKeyLengthIndex_ = (Constants.default__.ECDH__PROVIDER__INFO__RPK__INDEX) + (d_10_recipientPublicKeyLength_)
        d_12_senderPublicKeyIndex_: int
        d_12_senderPublicKeyIndex_ = (d_11_recipientPublicKeyLengthIndex_) + (Constants.default__.ECDH__PROVIDER__INFO__PUBLIC__KEY__LEN)
        d_13_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_13_valueOrError4_ = Wrappers.default__.Need(((d_11_recipientPublicKeyLengthIndex_) + (4)) < (len(d_3_providerInfo_)), default__.E(_dafny.Seq("Key Provider Info Serialization Error. Serialized length less than expected.")))
        if (d_13_valueOrError4_).IsFailure():
            res = (d_13_valueOrError4_).PropagateFailure()
            return res
        d_14_providerInfoRecipientPublicKey_: _dafny.Seq
        d_14_providerInfoRecipientPublicKey_ = _dafny.Seq((d_3_providerInfo_)[Constants.default__.ECDH__PROVIDER__INFO__RPK__INDEX:d_11_recipientPublicKeyLengthIndex_:])
        d_15_providerInfoSenderPublicKey_: _dafny.Seq
        d_15_providerInfoSenderPublicKey_ = _dafny.Seq((d_3_providerInfo_)[d_12_senderPublicKeyIndex_::])
        d_16_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out0_: Wrappers.Result
        out0_ = RawECDHKeyring.default__.DecompressPublicKey(d_15_providerInfoSenderPublicKey_, (self).curveSpec, (self).cryptoPrimitives)
        d_16_valueOrError5_ = out0_
        if (d_16_valueOrError5_).IsFailure():
            res = (d_16_valueOrError5_).PropagateFailure()
            return res
        d_17_senderPublicKey_: _dafny.Seq
        d_17_senderPublicKey_ = (d_16_valueOrError5_).Extract()
        d_18_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out1_: Wrappers.Result
        out1_ = RawECDHKeyring.default__.DecompressPublicKey(d_14_providerInfoRecipientPublicKey_, (self).curveSpec, (self).cryptoPrimitives)
        d_18_valueOrError6_ = out1_
        if (d_18_valueOrError6_).IsFailure():
            res = (d_18_valueOrError6_).PropagateFailure()
            return res
        d_19_recipientPublicKey_: _dafny.Seq
        d_19_recipientPublicKey_ = (d_18_valueOrError6_).Extract()
        d_20_valueOrError7_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        out2_: Wrappers.Result
        out2_ = RawECDHKeyring.default__.ValidatePublicKey((self).cryptoPrimitives, (self).curveSpec, d_17_senderPublicKey_)
        d_20_valueOrError7_ = out2_
        if (d_20_valueOrError7_).IsFailure():
            res = (d_20_valueOrError7_).PropagateFailure()
            return res
        d_21___v0_: bool
        d_21___v0_ = (d_20_valueOrError7_).Extract()
        d_22_valueOrError8_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        out3_: Wrappers.Result
        out3_ = RawECDHKeyring.default__.ValidatePublicKey((self).cryptoPrimitives, (self).curveSpec, d_19_recipientPublicKey_)
        d_22_valueOrError8_ = out3_
        if (d_22_valueOrError8_).IsFailure():
            res = (d_22_valueOrError8_).PropagateFailure()
            return res
        d_23___v1_: bool
        d_23___v1_ = (d_22_valueOrError8_).Extract()
        d_24_valueOrError9_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_24_valueOrError9_ = Wrappers.default__.Need((ComAmazonawsKmsTypes.default__.IsValid__PublicKeyType(d_17_senderPublicKey_)) and (ComAmazonawsKmsTypes.default__.IsValid__PublicKeyType((self).recipientPublicKey)), default__.E(_dafny.Seq("Received serialized sender public key of incorrect length")))
        if (d_24_valueOrError9_).IsFailure():
            res = (d_24_valueOrError9_).PropagateFailure()
            return res
        d_25_sharedSecretPublicKey_: _dafny.Seq = _dafny.Seq({})
        d_26_sharedSecretKmsKeyId_: _dafny.Seq = _dafny.Seq("")
        source0_ = (self).keyAgreementScheme
        with _dafny.label("match0"):
            if True:
                if source0_.is_KmsPublicKeyDiscovery:
                    d_27_kmsPublicKeyDiscovery_ = source0_.KmsPublicKeyDiscovery
                    if True:
                        d_28_valueOrError10_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
                        d_28_valueOrError10_ = AwsKmsUtils.default__.ValidateKmsKeyId((d_27_kmsPublicKeyDiscovery_).recipientKmsIdentifier)
                        if (d_28_valueOrError10_).IsFailure():
                            res = (d_28_valueOrError10_).PropagateFailure()
                            return res
                        d_29___v2_: tuple
                        d_29___v2_ = (d_28_valueOrError10_).Extract()
                        d_25_sharedSecretPublicKey_ = d_17_senderPublicKey_
                        d_26_sharedSecretKmsKeyId_ = (d_27_kmsPublicKeyDiscovery_).recipientKmsIdentifier
                    raise _dafny.Break("match0")
            if True:
                d_30_kmsPrivateKeyToStaticPublicKey_ = source0_.KmsPrivateKeyToStaticPublicKey
                if True:
                    d_31_valueOrError11_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
                    d_31_valueOrError11_ = AwsKmsUtils.default__.ValidateKmsKeyId((d_30_kmsPrivateKeyToStaticPublicKey_).senderKmsIdentifier)
                    if (d_31_valueOrError11_).IsFailure():
                        res = (d_31_valueOrError11_).PropagateFailure()
                        return res
                    d_32___v3_: tuple
                    d_32___v3_ = (d_31_valueOrError11_).Extract()
                    d_26_sharedSecretKmsKeyId_ = (d_30_kmsPrivateKeyToStaticPublicKey_).senderKmsIdentifier
                    if ((d_30_kmsPrivateKeyToStaticPublicKey_).recipientPublicKey) == (d_19_recipientPublicKey_):
                        d_25_sharedSecretPublicKey_ = d_19_recipientPublicKey_
                    elif True:
                        d_25_sharedSecretPublicKey_ = d_17_senderPublicKey_
            pass
        d_33_valueOrError12_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_33_valueOrError12_ = Wrappers.default__.Need(ComAmazonawsKmsTypes.default__.IsValid__PublicKeyType(d_25_sharedSecretPublicKey_), default__.E(_dafny.Seq("Received Recipient Public Key of incorrect expected length")))
        if (d_33_valueOrError12_).IsFailure():
            res = (d_33_valueOrError12_).PropagateFailure()
            return res
        d_34_valueOrError13_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out4_: Wrappers.Result
        out4_ = default__.DeriveSharedSecret((self).client, d_26_sharedSecretKmsKeyId_, d_25_sharedSecretPublicKey_, (self).grantTokens)
        d_34_valueOrError13_ = out4_
        if (d_34_valueOrError13_).IsFailure():
            res = (d_34_valueOrError13_).PropagateFailure()
            return res
        d_35_sharedSecret_: _dafny.Seq
        d_35_sharedSecret_ = (d_34_valueOrError13_).Extract()
        d_36_ecdhUnwrap_: EcdhEdkWrapping.EcdhUnwrap
        nw0_ = EcdhEdkWrapping.EcdhUnwrap()
        nw0_.ctor__(d_15_providerInfoSenderPublicKey_, d_14_providerInfoRecipientPublicKey_, d_35_sharedSecret_, default__.AWS__KMS__ECDH__KEYRING__VERSION, (self).curveSpec, (self).cryptoPrimitives)
        d_36_ecdhUnwrap_ = nw0_
        d_37_unwrapOutputRes_: Wrappers.Result
        out5_: Wrappers.Result
        out5_ = EdkWrapping.default__.UnwrapEdkMaterial((edk).ciphertext, (self).materials, d_36_ecdhUnwrap_)
        d_37_unwrapOutputRes_ = out5_
        d_38_valueOrError14_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.UnwrapEdkMaterialOutput.default(EcdhEdkWrapping.EcdhUnwrapInfo.default()))()
        d_38_valueOrError14_ = d_37_unwrapOutputRes_
        if (d_38_valueOrError14_).IsFailure():
            res = (d_38_valueOrError14_).PropagateFailure()
            return res
        d_39_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_39_unwrapOutput_ = (d_38_valueOrError14_).Extract()
        d_40_valueOrError15_: Wrappers.Result = None
        d_40_valueOrError15_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_39_unwrapOutput_).plaintextDataKey, (d_39_unwrapOutput_).symmetricSigningKey)
        if (d_40_valueOrError15_).IsFailure():
            res = (d_40_valueOrError15_).PropagateFailure()
            return res
        d_41_result_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_41_result_ = (d_40_valueOrError15_).Extract()
        res = Wrappers.Result_Success(d_41_result_)
        return res
        return res

    @property
    def materials(self):
        return self._materials
    @property
    def cryptoPrimitives(self):
        return self._cryptoPrimitives
    @property
    def recipientPublicKey(self):
        return self._recipientPublicKey
    @property
    def keyAgreementScheme(self):
        return self._keyAgreementScheme
    @property
    def client(self):
        return self._client
    @property
    def curveSpec(self):
        return self._curveSpec
    @property
    def grantTokens(self):
        return self._grantTokens

class OnDecryptEcdhDataKeyFilter(Actions.DeterministicActionWithResult, Actions.DeterministicAction):
    def  __init__(self):
        self._keyAgreementScheme: AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations = AwsCryptographyMaterialProvidersTypes.KmsEcdhStaticConfigurations.default()()
        self._compressedRecipientPublicKey: _dafny.Seq = _dafny.Seq({})
        self._compressedSenderPublicKey: _dafny.Seq = _dafny.Seq({})
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsEcdhKeyring.OnDecryptEcdhDataKeyFilter"
    def ctor__(self, keyAgreementScheme, compressedRecipientPublicKey, compressedSenderPublicKey):
        (self)._keyAgreementScheme = keyAgreementScheme
        (self)._compressedRecipientPublicKey = compressedRecipientPublicKey
        if (compressedSenderPublicKey).is_Some:
            (self)._compressedSenderPublicKey = (compressedSenderPublicKey).value
        elif True:
            (self)._compressedSenderPublicKey = _dafny.Seq([])

    def Invoke(self, edk):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        d_0_providerInfo_: _dafny.Seq
        d_0_providerInfo_ = (edk).keyProviderInfo
        d_1_providerId_: _dafny.Seq
        d_1_providerId_ = (edk).keyProviderId
        if ((d_1_providerId_) != (Constants.default__.RAW__ECDH__PROVIDER__ID)) and ((d_1_providerId_) != (Constants.default__.KMS__ECDH__PROVIDER__ID)):
            res = Wrappers.Result_Success(False)
            return res
        d_2_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_2_valueOrError0_ = Wrappers.default__.Need(((len(d_0_providerInfo_)) <= (Constants.default__.ECDH__PROVIDER__INFO__521__LEN)) and (RawECDHKeyring.default__.ValidProviderInfoLength(d_0_providerInfo_)), default__.E(_dafny.Seq("EDK ProviderInfo longer than expected")))
        if (d_2_valueOrError0_).IsFailure():
            res = (d_2_valueOrError0_).PropagateFailure()
            return res
        d_3_keyringVersion_: int
        d_3_keyringVersion_ = (d_0_providerInfo_)[0]
        d_4_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_4_valueOrError1_ = Wrappers.default__.Need((_dafny.Seq([d_3_keyringVersion_])) == (default__.AWS__KMS__ECDH__KEYRING__VERSION), default__.E(_dafny.Seq("Incorrect Keyring version found in provider info.")))
        if (d_4_valueOrError1_).IsFailure():
            res = (d_4_valueOrError1_).PropagateFailure()
            return res
        d_5_recipientPublicKeyLength_: int
        d_5_recipientPublicKeyLength_ = StandardLibrary_UInt.default__.SeqToUInt32(_dafny.Seq((d_0_providerInfo_)[Constants.default__.ECDH__PROVIDER__INFO__RPL__INDEX:Constants.default__.ECDH__PROVIDER__INFO__RPK__INDEX:]))
        d_6_recipientPublicKeyLengthIndex_: int
        d_6_recipientPublicKeyLengthIndex_ = (Constants.default__.ECDH__PROVIDER__INFO__RPK__INDEX) + (d_5_recipientPublicKeyLength_)
        d_7_senderPublicKeyIndex_: int
        d_7_senderPublicKeyIndex_ = (d_6_recipientPublicKeyLengthIndex_) + (Constants.default__.ECDH__PROVIDER__INFO__PUBLIC__KEY__LEN)
        d_8_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_8_valueOrError2_ = Wrappers.default__.Need(((d_6_recipientPublicKeyLengthIndex_) + (4)) < (len(d_0_providerInfo_)), default__.E(_dafny.Seq("Key Provider Info Serialization Error. Serialized length less than expected.")))
        if (d_8_valueOrError2_).IsFailure():
            res = (d_8_valueOrError2_).PropagateFailure()
            return res
        d_9_providerInfoRecipientPublicKey_: _dafny.Seq
        d_9_providerInfoRecipientPublicKey_ = _dafny.Seq((d_0_providerInfo_)[Constants.default__.ECDH__PROVIDER__INFO__RPK__INDEX:d_6_recipientPublicKeyLengthIndex_:])
        d_10_providerInfoSenderPublicKey_: _dafny.Seq
        d_10_providerInfoSenderPublicKey_ = _dafny.Seq((d_0_providerInfo_)[d_7_senderPublicKeyIndex_::])
        if ((self).keyAgreementScheme).is_KmsPublicKeyDiscovery:
            res = Wrappers.Result_Success(((self).compressedRecipientPublicKey) == (d_9_providerInfoRecipientPublicKey_))
            return res
        elif True:
            res = Wrappers.Result_Success(((((self).compressedSenderPublicKey) == (d_10_providerInfoSenderPublicKey_)) and (((self).compressedRecipientPublicKey) == (d_9_providerInfoRecipientPublicKey_))) or ((((self).compressedSenderPublicKey) == (d_9_providerInfoRecipientPublicKey_)) and (((self).compressedRecipientPublicKey) == (d_10_providerInfoSenderPublicKey_))))
            return res
        return res

    @property
    def keyAgreementScheme(self):
        return self._keyAgreementScheme
    @property
    def compressedRecipientPublicKey(self):
        return self._compressedRecipientPublicKey
    @property
    def compressedSenderPublicKey(self):
        return self._compressedSenderPublicKey
