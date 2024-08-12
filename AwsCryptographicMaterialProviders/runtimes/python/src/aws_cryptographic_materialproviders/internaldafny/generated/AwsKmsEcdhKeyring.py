import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptographic_materialproviders.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import standard_library.internaldafny.generated.Wrappers as Wrappers
import standard_library.internaldafny.generated.BoundedInts as BoundedInts
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import standard_library.internaldafny.generated.UTF8 as UTF8
import com_amazonaws_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import com_amazonaws_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
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
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
import standard_library.internaldafny.generated.Relations as Relations
import standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import standard_library.internaldafny.generated.Math as Math
import standard_library.internaldafny.generated.Seq as Seq
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
import standard_library.internaldafny.generated.UUID as UUID
import standard_library.internaldafny.generated.Time as Time
import standard_library.internaldafny.generated.Streams as Streams
import standard_library.internaldafny.generated.Sorting as Sorting
import standard_library.internaldafny.generated.SortedSets as SortedSets
import standard_library.internaldafny.generated.HexStrings as HexStrings
import standard_library.internaldafny.generated.GetOpt as GetOpt
import standard_library.internaldafny.generated.FloatCompare as FloatCompare
import standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import standard_library.internaldafny.generated.Base64 as Base64
import standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import standard_library.internaldafny.generated.Actions as Actions
import standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStoreErrorMessages as KeyStoreErrorMessages
import aws_cryptographic_materialproviders.internaldafny.generated.KmsArn as KmsArn
import aws_cryptographic_materialproviders.internaldafny.generated.Structure as Structure
import aws_cryptographic_materialproviders.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable
import aws_cryptographic_materialproviders.internaldafny.generated.GetKeys as GetKeys
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import com_amazonaws_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStore as KeyStore
import aws_cryptographic_materialproviders.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_materialproviders.internaldafny.generated.Materials as Materials
import aws_cryptographic_materialproviders.internaldafny.generated.Keyring as Keyring
import aws_cryptographic_materialproviders.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import aws_cryptographic_materialproviders.internaldafny.generated.Constants as Constants
import aws_cryptography_primitives.internaldafny.generated.Aws_Cryptography_Primitives as Aws_Cryptography_Primitives
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialWrapping as MaterialWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_materialproviders.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.EdkWrapping as EdkWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.ErrorMessages as ErrorMessages
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsKeyring as AwsKmsKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.StrictMultiKeyring as StrictMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsDiscoveryKeyring as AwsKmsDiscoveryKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.DiscoveryMultiKeyring as DiscoveryMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkDiscoveryKeyring as AwsKmsMrkDiscoveryKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.MrkAwareDiscoveryMultiKeyring as MrkAwareDiscoveryMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkKeyring as AwsKmsMrkKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.MrkAwareStrictMultiKeyring as MrkAwareStrictMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.LocalCMC as LocalCMC
import aws_cryptographic_materialproviders.internaldafny.generated.SynchronizedLocalCMC as SynchronizedLocalCMC
import aws_cryptographic_materialproviders.internaldafny.generated.StormTracker as StormTracker
import aws_cryptographic_materialproviders.internaldafny.generated.StormTrackingCMC as StormTrackingCMC
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsHierarchicalKeyring as AwsKmsHierarchicalKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsRsaKeyring as AwsKmsRsaKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.EcdhEdkWrapping as EcdhEdkWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.RawECDHKeyring as RawECDHKeyring

# Module: AwsKmsEcdhKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DeriveSharedSecret(client, senderAwsKmsKey, recipientPublicKey, grantTokens):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1262_deriveSharedSecretRequest_: ComAmazonawsKmsTypes.DeriveSharedSecretRequest
        d_1262_deriveSharedSecretRequest_ = ComAmazonawsKmsTypes.DeriveSharedSecretRequest_DeriveSharedSecretRequest(senderAwsKmsKey, ComAmazonawsKmsTypes.KeyAgreementAlgorithmSpec_ECDH(), recipientPublicKey, Wrappers.Option_Some(grantTokens), Wrappers.Option_None(), Wrappers.Option_None())
        d_1263_maybeDeriveSharedSecret_: Wrappers.Result
        out225_: Wrappers.Result
        out225_ = (client).DeriveSharedSecret(d_1262_deriveSharedSecretRequest_)
        d_1263_maybeDeriveSharedSecret_ = out225_
        d_1264_deriveSharedSecretResponse_: ComAmazonawsKmsTypes.DeriveSharedSecretResponse
        d_1265_valueOrError0_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.DeriveSharedSecretResponse.default())()
        def lambda102_(d_1266_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_ComAmazonawsKms(d_1266_e_)

        d_1265_valueOrError0_ = (d_1263_maybeDeriveSharedSecret_).MapFailure(lambda102_)
        if (d_1265_valueOrError0_).IsFailure():
            res = (d_1265_valueOrError0_).PropagateFailure()
            return res
        d_1264_deriveSharedSecretResponse_ = (d_1265_valueOrError0_).Extract()
        d_1267_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1267_valueOrError1_ = Wrappers.default__.Need(((((((d_1264_deriveSharedSecretResponse_).KeyId).is_Some) and (((d_1264_deriveSharedSecretResponse_).SharedSecret).is_Some)) and (((d_1264_deriveSharedSecretResponse_).KeyAgreementAlgorithm).is_Some)) and ((((d_1264_deriveSharedSecretResponse_).KeyId).value) == (senderAwsKmsKey))) and ((((d_1264_deriveSharedSecretResponse_).KeyAgreementAlgorithm).value) == (ComAmazonawsKmsTypes.KeyAgreementAlgorithmSpec_ECDH())), default__.E(_dafny.Seq("Invalid response from KMS DeriveSharedSecret")))
        if (d_1267_valueOrError1_).IsFailure():
            res = (d_1267_valueOrError1_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(((d_1264_deriveSharedSecretResponse_).SharedSecret).value)
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
        self._cryptoPrimitives: Aws_Cryptography_Primitives.AtomicPrimitivesClient = None
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
        out226_: Wrappers.Result
        out226_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnDecrypt(self, input)
        return out226_

    def OnEncrypt(self, input):
        out227_: Wrappers.Result
        out227_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnEncrypt(self, input)
        return out227_

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
        d_1268_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1268_valueOrError0_ = Wrappers.default__.Need(not(((self).keyAgreementScheme).is_KmsPublicKeyDiscovery), default__.E(_dafny.Seq("KmsPublicKeyDiscovery Key Agreement Scheme is forbidden on encrypt.")))
        if (d_1268_valueOrError0_).IsFailure():
            res = (d_1268_valueOrError0_).PropagateFailure()
            return res
        d_1269_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1269_valueOrError1_ = Wrappers.default__.Need(((self).senderKmsKeyId).is_Some, default__.E(_dafny.Seq("Keyring MUST be configured with a sender KMS Key ID")))
        if (d_1269_valueOrError1_).IsFailure():
            res = (d_1269_valueOrError1_).PropagateFailure()
            return res
        d_1270_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1270_valueOrError2_ = Wrappers.default__.Need(((self).senderPublicKey).is_Some, default__.E(_dafny.Seq("Keyring MUST be configured with a senderPublicKey")))
        if (d_1270_valueOrError2_).IsFailure():
            res = (d_1270_valueOrError2_).PropagateFailure()
            return res
        d_1271_senderKmsKeyId_: _dafny.Seq
        d_1271_senderKmsKeyId_ = ((self).senderKmsKeyId).value
        d_1272_materials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_1272_materials_ = (input).materials
        d_1273_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_1273_suite_ = ((input).materials).algorithmSuite
        d_1274_stringifiedEncCtx_: _dafny.Map
        d_1275_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        d_1275_valueOrError3_ = AwsKmsUtils.default__.StringifyEncryptionContext(((input).materials).encryptionContext)
        if (d_1275_valueOrError3_).IsFailure():
            res = (d_1275_valueOrError3_).PropagateFailure()
            return res
        d_1274_stringifiedEncCtx_ = (d_1275_valueOrError3_).Extract()
        d_1276_sharedSecret_: _dafny.Seq
        d_1277_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out228_: Wrappers.Result
        out228_ = default__.DeriveSharedSecret((self).client, d_1271_senderKmsKeyId_, (self).recipientPublicKey, (self).grantTokens)
        d_1277_valueOrError4_ = out228_
        if (d_1277_valueOrError4_).IsFailure():
            res = (d_1277_valueOrError4_).PropagateFailure()
            return res
        d_1276_sharedSecret_ = (d_1277_valueOrError4_).Extract()
        d_1278_operationCompressedSenderPublicKey_: _dafny.Seq
        d_1278_operationCompressedSenderPublicKey_ = (_dafny.Seq([]) if ((self).compressedSenderPublicKey).is_None else ((self).compressedSenderPublicKey).value)
        d_1279_curveSpecUtf8_: _dafny.Seq
        d_1280_valueOrError5_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_1280_valueOrError5_ = (UTF8.default__.Encode(RawECDHKeyring.default__.CurveSpecTypeToString((self).curveSpec))).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_1280_valueOrError5_).IsFailure():
            res = (d_1280_valueOrError5_).PropagateFailure()
            return res
        d_1279_curveSpecUtf8_ = (d_1280_valueOrError5_).Extract()
        d_1281_canonicalizedEC_: _dafny.Seq
        d_1282_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1282_valueOrError6_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD(((input).materials).encryptionContext)
        if (d_1282_valueOrError6_).IsFailure():
            res = (d_1282_valueOrError6_).PropagateFailure()
            return res
        d_1281_canonicalizedEC_ = (d_1282_valueOrError6_).Extract()
        d_1283_fixedInfo_: _dafny.Seq
        d_1283_fixedInfo_ = EcdhEdkWrapping.default__.SerializeFixedInfo(Constants.default__.ECDH__KDF__UTF8, d_1279_curveSpecUtf8_, d_1278_operationCompressedSenderPublicKey_, (self).compressedRecipientPublicKey, d_1281_canonicalizedEC_, default__.AWS__KMS__ECDH__KEYRING__VERSION)
        d_1284_ecdhGenerateAndWrap_: EcdhEdkWrapping.EcdhGenerateAndWrapKeyMaterial
        nw51_ = EcdhEdkWrapping.EcdhGenerateAndWrapKeyMaterial()
        nw51_.ctor__(d_1276_sharedSecret_, d_1283_fixedInfo_, (self).cryptoPrimitives)
        d_1284_ecdhGenerateAndWrap_ = nw51_
        d_1285_ecdhWrap_: EcdhEdkWrapping.EcdhWrapKeyMaterial
        nw52_ = EcdhEdkWrapping.EcdhWrapKeyMaterial()
        nw52_.ctor__(d_1276_sharedSecret_, d_1283_fixedInfo_, (self).cryptoPrimitives)
        d_1285_ecdhWrap_ = nw52_
        d_1286_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_1287_valueOrError7_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.WrapEdkMaterialOutput.default(EcdhEdkWrapping.EcdhWrapInfo.default()))()
        out229_: Wrappers.Result
        out229_ = EdkWrapping.default__.WrapEdkMaterial(d_1272_materials_, d_1285_ecdhWrap_, d_1284_ecdhGenerateAndWrap_)
        d_1287_valueOrError7_ = out229_
        if (d_1287_valueOrError7_).IsFailure():
            res = (d_1287_valueOrError7_).PropagateFailure()
            return res
        d_1286_wrapOutput_ = (d_1287_valueOrError7_).Extract()
        d_1288_symmetricSigningKeyList_: Wrappers.Option
        d_1288_symmetricSigningKeyList_ = (Wrappers.Option_Some(_dafny.Seq([((d_1286_wrapOutput_).symmetricSigningKey).value])) if ((d_1286_wrapOutput_).symmetricSigningKey).is_Some else Wrappers.Option_None())
        d_1289_valueOrError8_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1289_valueOrError8_ = Wrappers.default__.Need((RawECDHKeyring.default__.ValidCompressedPublicKeyLength(d_1278_operationCompressedSenderPublicKey_)) and (RawECDHKeyring.default__.ValidCompressedPublicKeyLength((self).compressedRecipientPublicKey)), default__.E(_dafny.Seq("Invalid compressed public key length.")))
        if (d_1289_valueOrError8_).IsFailure():
            res = (d_1289_valueOrError8_).PropagateFailure()
            return res
        d_1290_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_1290_edk_ = AwsCryptographyMaterialProvidersTypes.EncryptedDataKey_EncryptedDataKey(Constants.default__.KMS__ECDH__PROVIDER__ID, RawECDHKeyring.default__.SerializeProviderInfo(d_1278_operationCompressedSenderPublicKey_, (self).compressedRecipientPublicKey), (d_1286_wrapOutput_).wrappedMaterial)
        if (d_1286_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_1291_result_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_1292_valueOrError9_: Wrappers.Result = None
            d_1292_valueOrError9_ = Materials.default__.EncryptionMaterialAddDataKey(d_1272_materials_, (d_1286_wrapOutput_).plaintextDataKey, _dafny.Seq([d_1290_edk_]), d_1288_symmetricSigningKeyList_)
            if (d_1292_valueOrError9_).IsFailure():
                res = (d_1292_valueOrError9_).PropagateFailure()
                return res
            d_1291_result_ = (d_1292_valueOrError9_).Extract()
            res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(d_1291_result_))
            return res
        elif (d_1286_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_1293_result_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_1294_valueOrError10_: Wrappers.Result = None
            d_1294_valueOrError10_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys(d_1272_materials_, _dafny.Seq([d_1290_edk_]), d_1288_symmetricSigningKeyList_)
            if (d_1294_valueOrError10_).IsFailure():
                res = (d_1294_valueOrError10_).PropagateFailure()
                return res
            d_1293_result_ = (d_1294_valueOrError10_).Extract()
            res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(d_1293_result_))
            return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_1295_materials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_1295_materials_ = (input).materials
        d_1296_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_1296_suite_ = ((input).materials).algorithmSuite
        d_1297_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1297_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_1295_materials_), default__.E(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_1297_valueOrError0_).IsFailure():
            res = (d_1297_valueOrError0_).PropagateFailure()
            return res
        d_1298_filter_: OnDecryptEcdhDataKeyFilter
        nw53_ = OnDecryptEcdhDataKeyFilter()
        nw53_.ctor__((self).keyAgreementScheme, (self).compressedRecipientPublicKey, (self).compressedSenderPublicKey)
        d_1298_filter_ = nw53_
        d_1299_edksToAttempt_: _dafny.Seq
        d_1300_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out230_: Wrappers.Result
        out230_ = Actions.default__.FilterWithResult(d_1298_filter_, (input).encryptedDataKeys)
        d_1300_valueOrError1_ = out230_
        if (d_1300_valueOrError1_).IsFailure():
            res = (d_1300_valueOrError1_).PropagateFailure()
            return res
        d_1299_edksToAttempt_ = (d_1300_valueOrError1_).Extract()
        if (0) == (len(d_1299_edksToAttempt_)):
            d_1301_errorMessage_: _dafny.Seq
            d_1302_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            d_1302_valueOrError2_ = ErrorMessages.default__.IncorrectDataKeys((input).encryptedDataKeys, ((input).materials).algorithmSuite, _dafny.Seq(""))
            if (d_1302_valueOrError2_).IsFailure():
                res = (d_1302_valueOrError2_).PropagateFailure()
                return res
            d_1301_errorMessage_ = (d_1302_valueOrError2_).Extract()
            res = Wrappers.Result_Failure(default__.E(d_1301_errorMessage_))
            return res
        d_1303_decryptClosure_: Actions.ActionWithResult
        nw54_ = DecryptSingleEncryptedDataKey()
        nw54_.ctor__(d_1295_materials_, (self).cryptoPrimitives, (self).compressedRecipientPublicKey, (self).client, (self).grantTokens, (self).keyAgreementScheme, (self).curveSpec)
        d_1303_decryptClosure_ = nw54_
        d_1304_outcome_: Wrappers.Result
        out231_: Wrappers.Result
        out231_ = Actions.default__.ReduceToSuccess(d_1303_decryptClosure_, d_1299_edksToAttempt_)
        d_1304_outcome_ = out231_
        d_1305_SealedDecryptionMaterials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_1306_valueOrError3_: Wrappers.Result = None
        def lambda103_(d_1307_errors_):
            return AwsCryptographyMaterialProvidersTypes.Error_CollectionOfErrors(d_1307_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."))

        d_1306_valueOrError3_ = (d_1304_outcome_).MapFailure(lambda103_)
        if (d_1306_valueOrError3_).IsFailure():
            res = (d_1306_valueOrError3_).PropagateFailure()
            return res
        d_1305_SealedDecryptionMaterials_ = (d_1306_valueOrError3_).Extract()
        res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnDecryptOutput_OnDecryptOutput(d_1305_SealedDecryptionMaterials_))
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
        self._cryptoPrimitives: Aws_Cryptography_Primitives.AtomicPrimitivesClient = None
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
        d_1308_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1308_valueOrError0_ = Wrappers.default__.Need(UTF8.default__.ValidUTF8Seq((edk).keyProviderId), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received invalid EDK provider id for AWS KMS ECDH Keyring")))
        if (d_1308_valueOrError0_).IsFailure():
            res = (d_1308_valueOrError0_).PropagateFailure()
            return res
        d_1309_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_1309_suite_ = ((self).materials).algorithmSuite
        d_1310_keyProviderId_: _dafny.Seq
        d_1310_keyProviderId_ = (edk).keyProviderId
        d_1311_providerInfo_: _dafny.Seq
        d_1311_providerInfo_ = (edk).keyProviderInfo
        d_1312_ciphertext_: _dafny.Seq
        d_1312_ciphertext_ = (edk).ciphertext
        d_1313_providerWrappedMaterial_: _dafny.Seq
        d_1314_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1314_valueOrError1_ = EdkWrapping.default__.GetProviderWrappedMaterial(d_1312_ciphertext_, d_1309_suite_)
        if (d_1314_valueOrError1_).IsFailure():
            res = (d_1314_valueOrError1_).PropagateFailure()
            return res
        d_1313_providerWrappedMaterial_ = (d_1314_valueOrError1_).Extract()
        d_1315_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1315_valueOrError2_ = Wrappers.default__.Need(((len(d_1311_providerInfo_)) <= (Constants.default__.ECDH__PROVIDER__INFO__521__LEN)) and (RawECDHKeyring.default__.ValidProviderInfoLength(d_1311_providerInfo_)), default__.E(_dafny.Seq("EDK ProviderInfo longer than expected")))
        if (d_1315_valueOrError2_).IsFailure():
            res = (d_1315_valueOrError2_).PropagateFailure()
            return res
        d_1316_keyringVersion_: int
        d_1316_keyringVersion_ = (d_1311_providerInfo_)[0]
        d_1317_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1317_valueOrError3_ = Wrappers.default__.Need((_dafny.Seq([d_1316_keyringVersion_])) == (default__.AWS__KMS__ECDH__KEYRING__VERSION), default__.E(_dafny.Seq("Incorrect Keyring version found in provider info.")))
        if (d_1317_valueOrError3_).IsFailure():
            res = (d_1317_valueOrError3_).PropagateFailure()
            return res
        d_1318_recipientPublicKeyLength_: int
        d_1318_recipientPublicKeyLength_ = StandardLibrary_UInt.default__.SeqToUInt32(_dafny.Seq((d_1311_providerInfo_)[Constants.default__.ECDH__PROVIDER__INFO__RPL__INDEX:Constants.default__.ECDH__PROVIDER__INFO__RPK__INDEX:]))
        d_1319_recipientPublicKeyLengthIndex_: int
        d_1319_recipientPublicKeyLengthIndex_ = (Constants.default__.ECDH__PROVIDER__INFO__RPK__INDEX) + (d_1318_recipientPublicKeyLength_)
        d_1320_senderPublicKeyIndex_: int
        d_1320_senderPublicKeyIndex_ = (d_1319_recipientPublicKeyLengthIndex_) + (Constants.default__.ECDH__PROVIDER__INFO__PUBLIC__KEY__LEN)
        d_1321_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1321_valueOrError4_ = Wrappers.default__.Need(((d_1319_recipientPublicKeyLengthIndex_) + (4)) < (len(d_1311_providerInfo_)), default__.E(_dafny.Seq("Key Provider Info Serialization Error. Serialized length less than expected.")))
        if (d_1321_valueOrError4_).IsFailure():
            res = (d_1321_valueOrError4_).PropagateFailure()
            return res
        d_1322_providerInfoRecipientPublicKey_: _dafny.Seq
        d_1322_providerInfoRecipientPublicKey_ = _dafny.Seq((d_1311_providerInfo_)[Constants.default__.ECDH__PROVIDER__INFO__RPK__INDEX:d_1319_recipientPublicKeyLengthIndex_:])
        d_1323_providerInfoSenderPublicKey_: _dafny.Seq
        d_1323_providerInfoSenderPublicKey_ = _dafny.Seq((d_1311_providerInfo_)[d_1320_senderPublicKeyIndex_::])
        d_1324_senderPublicKey_: _dafny.Seq
        d_1325_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out232_: Wrappers.Result
        out232_ = RawECDHKeyring.default__.DecompressPublicKey(d_1323_providerInfoSenderPublicKey_, (self).curveSpec, (self).cryptoPrimitives)
        d_1325_valueOrError5_ = out232_
        if (d_1325_valueOrError5_).IsFailure():
            res = (d_1325_valueOrError5_).PropagateFailure()
            return res
        d_1324_senderPublicKey_ = (d_1325_valueOrError5_).Extract()
        d_1326_recipientPublicKey_: _dafny.Seq
        d_1327_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out233_: Wrappers.Result
        out233_ = RawECDHKeyring.default__.DecompressPublicKey(d_1322_providerInfoRecipientPublicKey_, (self).curveSpec, (self).cryptoPrimitives)
        d_1327_valueOrError6_ = out233_
        if (d_1327_valueOrError6_).IsFailure():
            res = (d_1327_valueOrError6_).PropagateFailure()
            return res
        d_1326_recipientPublicKey_ = (d_1327_valueOrError6_).Extract()
        d_1328___v0_: bool
        d_1329_valueOrError7_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        out234_: Wrappers.Result
        out234_ = RawECDHKeyring.default__.ValidatePublicKey((self).cryptoPrimitives, (self).curveSpec, d_1324_senderPublicKey_)
        d_1329_valueOrError7_ = out234_
        if (d_1329_valueOrError7_).IsFailure():
            res = (d_1329_valueOrError7_).PropagateFailure()
            return res
        d_1328___v0_ = (d_1329_valueOrError7_).Extract()
        d_1330___v1_: bool
        d_1331_valueOrError8_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        out235_: Wrappers.Result
        out235_ = RawECDHKeyring.default__.ValidatePublicKey((self).cryptoPrimitives, (self).curveSpec, d_1326_recipientPublicKey_)
        d_1331_valueOrError8_ = out235_
        if (d_1331_valueOrError8_).IsFailure():
            res = (d_1331_valueOrError8_).PropagateFailure()
            return res
        d_1330___v1_ = (d_1331_valueOrError8_).Extract()
        d_1332_valueOrError9_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1332_valueOrError9_ = Wrappers.default__.Need((ComAmazonawsKmsTypes.default__.IsValid__PublicKeyType(d_1324_senderPublicKey_)) and (ComAmazonawsKmsTypes.default__.IsValid__PublicKeyType((self).recipientPublicKey)), default__.E(_dafny.Seq("Received serialized sender public key of incorrect length")))
        if (d_1332_valueOrError9_).IsFailure():
            res = (d_1332_valueOrError9_).PropagateFailure()
            return res
        d_1333_sharedSecretPublicKey_: _dafny.Seq = _dafny.Seq({})
        d_1334_sharedSecretKmsKeyId_: _dafny.Seq = _dafny.Seq("")
        if ((self).keyAgreementScheme).is_KmsPublicKeyDiscovery:
            d_1335___v2_: tuple
            d_1336_valueOrError10_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            d_1336_valueOrError10_ = AwsKmsUtils.default__.ValidateKmsKeyId((((self).keyAgreementScheme).KmsPublicKeyDiscovery).recipientKmsIdentifier)
            if (d_1336_valueOrError10_).IsFailure():
                res = (d_1336_valueOrError10_).PropagateFailure()
                return res
            d_1335___v2_ = (d_1336_valueOrError10_).Extract()
            d_1333_sharedSecretPublicKey_ = d_1324_senderPublicKey_
            d_1334_sharedSecretKmsKeyId_ = (((self).keyAgreementScheme).KmsPublicKeyDiscovery).recipientKmsIdentifier
        elif ((self).keyAgreementScheme).is_KmsPrivateKeyToStaticPublicKey:
            d_1337___v3_: tuple
            d_1338_valueOrError11_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            d_1338_valueOrError11_ = AwsKmsUtils.default__.ValidateKmsKeyId((((self).keyAgreementScheme).KmsPrivateKeyToStaticPublicKey).senderKmsIdentifier)
            if (d_1338_valueOrError11_).IsFailure():
                res = (d_1338_valueOrError11_).PropagateFailure()
                return res
            d_1337___v3_ = (d_1338_valueOrError11_).Extract()
            d_1334_sharedSecretKmsKeyId_ = (((self).keyAgreementScheme).KmsPrivateKeyToStaticPublicKey).senderKmsIdentifier
            if ((((self).keyAgreementScheme).KmsPrivateKeyToStaticPublicKey).recipientPublicKey) == (d_1326_recipientPublicKey_):
                d_1333_sharedSecretPublicKey_ = d_1326_recipientPublicKey_
            elif True:
                d_1333_sharedSecretPublicKey_ = d_1324_senderPublicKey_
        elif True:
            raise Exception("unreachable alternative")
        d_1339_valueOrError12_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1339_valueOrError12_ = Wrappers.default__.Need(ComAmazonawsKmsTypes.default__.IsValid__PublicKeyType(d_1333_sharedSecretPublicKey_), default__.E(_dafny.Seq("Received Recipient Public Key of incorrect expected length")))
        if (d_1339_valueOrError12_).IsFailure():
            res = (d_1339_valueOrError12_).PropagateFailure()
            return res
        d_1340_sharedSecret_: _dafny.Seq
        d_1341_valueOrError13_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out236_: Wrappers.Result
        out236_ = default__.DeriveSharedSecret((self).client, d_1334_sharedSecretKmsKeyId_, d_1333_sharedSecretPublicKey_, (self).grantTokens)
        d_1341_valueOrError13_ = out236_
        if (d_1341_valueOrError13_).IsFailure():
            res = (d_1341_valueOrError13_).PropagateFailure()
            return res
        d_1340_sharedSecret_ = (d_1341_valueOrError13_).Extract()
        d_1342_ecdhUnwrap_: EcdhEdkWrapping.EcdhUnwrap
        nw55_ = EcdhEdkWrapping.EcdhUnwrap()
        nw55_.ctor__(d_1323_providerInfoSenderPublicKey_, d_1322_providerInfoRecipientPublicKey_, d_1340_sharedSecret_, default__.AWS__KMS__ECDH__KEYRING__VERSION, (self).curveSpec, (self).cryptoPrimitives)
        d_1342_ecdhUnwrap_ = nw55_
        d_1343_unwrapOutputRes_: Wrappers.Result
        out237_: Wrappers.Result
        out237_ = EdkWrapping.default__.UnwrapEdkMaterial((edk).ciphertext, (self).materials, d_1342_ecdhUnwrap_)
        d_1343_unwrapOutputRes_ = out237_
        d_1344_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_1345_valueOrError14_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.UnwrapEdkMaterialOutput.default(EcdhEdkWrapping.EcdhUnwrapInfo.default()))()
        d_1345_valueOrError14_ = d_1343_unwrapOutputRes_
        if (d_1345_valueOrError14_).IsFailure():
            res = (d_1345_valueOrError14_).PropagateFailure()
            return res
        d_1344_unwrapOutput_ = (d_1345_valueOrError14_).Extract()
        d_1346_result_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_1347_valueOrError15_: Wrappers.Result = None
        d_1347_valueOrError15_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_1344_unwrapOutput_).plaintextDataKey, (d_1344_unwrapOutput_).symmetricSigningKey)
        if (d_1347_valueOrError15_).IsFailure():
            res = (d_1347_valueOrError15_).PropagateFailure()
            return res
        d_1346_result_ = (d_1347_valueOrError15_).Extract()
        res = Wrappers.Result_Success(d_1346_result_)
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
        d_1348_providerInfo_: _dafny.Seq
        d_1348_providerInfo_ = (edk).keyProviderInfo
        d_1349_providerId_: _dafny.Seq
        d_1349_providerId_ = (edk).keyProviderId
        if ((d_1349_providerId_) != (Constants.default__.RAW__ECDH__PROVIDER__ID)) and ((d_1349_providerId_) != (Constants.default__.KMS__ECDH__PROVIDER__ID)):
            res = Wrappers.Result_Success(False)
            return res
        d_1350_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1350_valueOrError0_ = Wrappers.default__.Need(((len(d_1348_providerInfo_)) <= (Constants.default__.ECDH__PROVIDER__INFO__521__LEN)) and (RawECDHKeyring.default__.ValidProviderInfoLength(d_1348_providerInfo_)), default__.E(_dafny.Seq("EDK ProviderInfo longer than expected")))
        if (d_1350_valueOrError0_).IsFailure():
            res = (d_1350_valueOrError0_).PropagateFailure()
            return res
        d_1351_keyringVersion_: int
        d_1351_keyringVersion_ = (d_1348_providerInfo_)[0]
        d_1352_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1352_valueOrError1_ = Wrappers.default__.Need((_dafny.Seq([d_1351_keyringVersion_])) == (default__.AWS__KMS__ECDH__KEYRING__VERSION), default__.E(_dafny.Seq("Incorrect Keyring version found in provider info.")))
        if (d_1352_valueOrError1_).IsFailure():
            res = (d_1352_valueOrError1_).PropagateFailure()
            return res
        d_1353_recipientPublicKeyLength_: int
        d_1353_recipientPublicKeyLength_ = StandardLibrary_UInt.default__.SeqToUInt32(_dafny.Seq((d_1348_providerInfo_)[Constants.default__.ECDH__PROVIDER__INFO__RPL__INDEX:Constants.default__.ECDH__PROVIDER__INFO__RPK__INDEX:]))
        d_1354_recipientPublicKeyLengthIndex_: int
        d_1354_recipientPublicKeyLengthIndex_ = (Constants.default__.ECDH__PROVIDER__INFO__RPK__INDEX) + (d_1353_recipientPublicKeyLength_)
        d_1355_senderPublicKeyIndex_: int
        d_1355_senderPublicKeyIndex_ = (d_1354_recipientPublicKeyLengthIndex_) + (Constants.default__.ECDH__PROVIDER__INFO__PUBLIC__KEY__LEN)
        d_1356_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1356_valueOrError2_ = Wrappers.default__.Need(((d_1354_recipientPublicKeyLengthIndex_) + (4)) < (len(d_1348_providerInfo_)), default__.E(_dafny.Seq("Key Provider Info Serialization Error. Serialized length less than expected.")))
        if (d_1356_valueOrError2_).IsFailure():
            res = (d_1356_valueOrError2_).PropagateFailure()
            return res
        d_1357_providerInfoRecipientPublicKey_: _dafny.Seq
        d_1357_providerInfoRecipientPublicKey_ = _dafny.Seq((d_1348_providerInfo_)[Constants.default__.ECDH__PROVIDER__INFO__RPK__INDEX:d_1354_recipientPublicKeyLengthIndex_:])
        d_1358_providerInfoSenderPublicKey_: _dafny.Seq
        d_1358_providerInfoSenderPublicKey_ = _dafny.Seq((d_1348_providerInfo_)[d_1355_senderPublicKeyIndex_::])
        if ((self).keyAgreementScheme).is_KmsPublicKeyDiscovery:
            res = Wrappers.Result_Success(((self).compressedRecipientPublicKey) == (d_1357_providerInfoRecipientPublicKey_))
            return res
        elif True:
            res = Wrappers.Result_Success(((((self).compressedSenderPublicKey) == (d_1358_providerInfoSenderPublicKey_)) and (((self).compressedRecipientPublicKey) == (d_1357_providerInfoRecipientPublicKey_))) or ((((self).compressedSenderPublicKey) == (d_1357_providerInfoRecipientPublicKey_)) and (((self).compressedRecipientPublicKey) == (d_1358_providerInfoSenderPublicKey_))))
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
