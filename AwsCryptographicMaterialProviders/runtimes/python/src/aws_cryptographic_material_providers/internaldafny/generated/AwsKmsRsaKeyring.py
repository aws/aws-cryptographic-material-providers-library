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

# Module: AwsKmsRsaKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def EncryptionContextDigest(cryptoPrimitives, encryptionContext):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_0_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_0_valueOrError0_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD(encryptionContext)
        if (d_0_valueOrError0_).IsFailure():
            output = (d_0_valueOrError0_).PropagateFailure()
            return output
        d_1_canonicalEC_: _dafny.Seq
        d_1_canonicalEC_ = (d_0_valueOrError0_).Extract()
        d_2_DigestInput_: AwsCryptographyPrimitivesTypes.DigestInput
        d_2_DigestInput_ = AwsCryptographyPrimitivesTypes.DigestInput_DigestInput(AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__384(), d_1_canonicalEC_)
        d_3_maybeDigest_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = (cryptoPrimitives).Digest(d_2_DigestInput_)
        d_3_maybeDigest_ = out0_
        d_4_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda0_(d_5_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_5_e_)

        d_4_valueOrError1_ = (d_3_maybeDigest_).MapFailure(lambda0_)
        if (d_4_valueOrError1_).IsFailure():
            output = (d_4_valueOrError1_).PropagateFailure()
            return output
        d_6_digest_: _dafny.Seq
        d_6_digest_ = (d_4_valueOrError1_).Extract()
        output = Wrappers.Result_Success(d_6_digest_)
        return output
        return output

    @_dafny.classproperty
    def MIN__KMS__RSA__KEY__LEN(instance):
        return 2048

class AwsKmsRsaKeyring(Keyring.VerifiableInterface, AwsCryptographyMaterialProvidersTypes.IKeyring):
    def  __init__(self):
        self._cryptoPrimitives: AtomicPrimitives.AtomicPrimitivesClient = None
        self._client: Wrappers.Option = Wrappers.Option.default()()
        self._paddingScheme: ComAmazonawsKmsTypes.EncryptionAlgorithmSpec = ComAmazonawsKmsTypes.EncryptionAlgorithmSpec.default()()
        self._awsKmsKey: _dafny.Seq = None
        self._publicKey: Wrappers.Option = Wrappers.Option.default()()
        self._awsKmsArn: AwsArnParsing.AwsKmsIdentifier = None
        self._grantTokens: _dafny.Seq = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsRsaKeyring.AwsKmsRsaKeyring"
    def OnDecrypt(self, input):
        out7_: Wrappers.Result
        out7_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnDecrypt(self, input)
        return out7_

    def OnEncrypt(self, input):
        out7_: Wrappers.Result
        out7_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnEncrypt(self, input)
        return out7_

    def ctor__(self, publicKey, awsKmsKey, paddingScheme, client, cryptoPrimitives, grantTokens):
        d_0_parsedAwsKmsId_: Wrappers.Result
        d_0_parsedAwsKmsId_ = AwsArnParsing.default__.ParseAwsKmsIdentifier(awsKmsKey)
        (self)._publicKey = publicKey
        (self)._awsKmsKey = awsKmsKey
        (self)._awsKmsArn = (d_0_parsedAwsKmsId_).value
        (self)._paddingScheme = paddingScheme
        (self)._client = client
        (self)._cryptoPrimitives = cryptoPrimitives
        (self)._grantTokens = grantTokens

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        d_0_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_0_valueOrError0_ = Wrappers.default__.Need((((self).publicKey).is_Some) and ((len(((self).publicKey).Extract())) > (0)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("A AwsKmsRsaKeyring without a public key cannot provide OnEncrypt")))
        if (d_0_valueOrError0_).IsFailure():
            res = (d_0_valueOrError0_).PropagateFailure()
            return res
        d_1_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1_valueOrError1_ = Wrappers.default__.Need(((((input).materials).algorithmSuite).signature).is_None, AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException((_dafny.Seq("AwsKmsRsaKeyring cannot be used with an Algorithm Suite with asymmetric signing.")) + (_dafny.Seq(" Please specify an algorithm suite without asymmetric signing."))))
        if (d_1_valueOrError1_).IsFailure():
            res = (d_1_valueOrError1_).PropagateFailure()
            return res
        d_2_wrap_: KmsRsaWrapKeyMaterial
        nw0_ = KmsRsaWrapKeyMaterial()
        nw0_.ctor__(((self).publicKey).value, (self).paddingScheme, (self).cryptoPrimitives)
        d_2_wrap_ = nw0_
        d_3_generateAndWrap_: KmsRsaGenerateAndWrapKeyMaterial
        nw1_ = KmsRsaGenerateAndWrapKeyMaterial()
        nw1_.ctor__(((self).publicKey).value, (self).paddingScheme, (self).cryptoPrimitives)
        d_3_generateAndWrap_ = nw1_
        d_4_valueOrError2_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.WrapEdkMaterialOutput.default(KmsRsaWrapInfo.default()))()
        out0_: Wrappers.Result
        out0_ = EdkWrapping.default__.WrapEdkMaterial((input).materials, d_2_wrap_, d_3_generateAndWrap_)
        d_4_valueOrError2_ = out0_
        if (d_4_valueOrError2_).IsFailure():
            res = (d_4_valueOrError2_).PropagateFailure()
            return res
        d_5_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_5_wrapOutput_ = (d_4_valueOrError2_).Extract()
        d_6_symmetricSigningKeyList_: Wrappers.Option
        if ((d_5_wrapOutput_).symmetricSigningKey).is_Some:
            d_6_symmetricSigningKeyList_ = Wrappers.Option_Some(_dafny.Seq([((d_5_wrapOutput_).symmetricSigningKey).value]))
        elif True:
            d_6_symmetricSigningKeyList_ = Wrappers.Option_None()
        d_7_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_7_edk_ = AwsCryptographyMaterialProvidersTypes.EncryptedDataKey_EncryptedDataKey(Constants.default__.RSA__PROVIDER__ID, (UTF8.default__.Encode((self).awsKmsKey)).value, (d_5_wrapOutput_).wrappedMaterial)
        d_8_returnMaterials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials = None
        if (d_5_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_9_valueOrError3_: Wrappers.Result = None
            d_9_valueOrError3_ = Materials.default__.EncryptionMaterialAddDataKey((input).materials, (d_5_wrapOutput_).plaintextDataKey, _dafny.Seq([d_7_edk_]), d_6_symmetricSigningKeyList_)
            if (d_9_valueOrError3_).IsFailure():
                res = (d_9_valueOrError3_).PropagateFailure()
                return res
            d_8_returnMaterials_ = (d_9_valueOrError3_).Extract()
        elif (d_5_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_10_valueOrError4_: Wrappers.Result = None
            d_10_valueOrError4_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys((input).materials, _dafny.Seq([d_7_edk_]), d_6_symmetricSigningKeyList_)
            if (d_10_valueOrError4_).IsFailure():
                res = (d_10_valueOrError4_).PropagateFailure()
                return res
            d_8_returnMaterials_ = (d_10_valueOrError4_).Extract()
        res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(d_8_returnMaterials_))
        return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_0_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_0_valueOrError0_ = Wrappers.default__.Need(((self).client).is_Some, AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("An AwsKmsRsaKeyring without an AWS KMS client cannot provide OnDecrypt")))
        if (d_0_valueOrError0_).IsFailure():
            res = (d_0_valueOrError0_).PropagateFailure()
            return res
        d_1_materials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_1_materials_ = (input).materials
        d_2_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_2_valueOrError1_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_1_materials_), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_2_valueOrError1_).IsFailure():
            res = (d_2_valueOrError1_).PropagateFailure()
            return res
        d_3_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_3_valueOrError2_ = AwsKmsUtils.default__.OkForDecrypt((self).awsKmsArn, (self).awsKmsKey)
        if (d_3_valueOrError2_).IsFailure():
            res = (d_3_valueOrError2_).PropagateFailure()
            return res
        d_4_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_4_valueOrError3_ = Wrappers.default__.Need(((((input).materials).algorithmSuite).signature).is_None, AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException((_dafny.Seq("AwsKmsRsaKeyring cannot be used with an Algorithm Suite with asymmetric signing.")) + (_dafny.Seq(" Please specify an algorithm suite without asymmetric signing."))))
        if (d_4_valueOrError3_).IsFailure():
            res = (d_4_valueOrError3_).PropagateFailure()
            return res
        d_5_filter_: AwsKmsUtils.OnDecryptMrkAwareEncryptedDataKeyFilter
        nw0_ = AwsKmsUtils.OnDecryptMrkAwareEncryptedDataKeyFilter()
        nw0_.ctor__((self).awsKmsArn, Constants.default__.RSA__PROVIDER__ID)
        d_5_filter_ = nw0_
        d_6_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out0_: Wrappers.Result
        out0_ = Actions.default__.FilterWithResult(d_5_filter_, (input).encryptedDataKeys)
        d_6_valueOrError4_ = out0_
        if (d_6_valueOrError4_).IsFailure():
            res = (d_6_valueOrError4_).PropagateFailure()
            return res
        d_7_edksToAttempt_: _dafny.Seq
        d_7_edksToAttempt_ = (d_6_valueOrError4_).Extract()
        if (0) == (len(d_7_edksToAttempt_)):
            d_8_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            d_8_valueOrError5_ = ErrorMessages.default__.IncorrectDataKeys((input).encryptedDataKeys, ((input).materials).algorithmSuite, _dafny.Seq(""))
            if (d_8_valueOrError5_).IsFailure():
                res = (d_8_valueOrError5_).PropagateFailure()
                return res
            d_9_errorMessage_: _dafny.Seq
            d_9_errorMessage_ = (d_8_valueOrError5_).Extract()
            res = Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_9_errorMessage_))
            return res
        d_10_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out1_: Wrappers.Result
        out1_ = default__.EncryptionContextDigest((self).cryptoPrimitives, (d_1_materials_).encryptionContext)
        d_10_valueOrError6_ = out1_
        if (d_10_valueOrError6_).IsFailure():
            res = (d_10_valueOrError6_).PropagateFailure()
            return res
        d_11_encryptionContextDigest_: _dafny.Seq
        d_11_encryptionContextDigest_ = (d_10_valueOrError6_).Extract()
        d_12_decryptClosure_: Actions.ActionWithResult
        nw1_ = DecryptSingleAWSRSAEncryptedDataKey()
        nw1_.ctor__(d_1_materials_, ((self).client).value, (self).awsKmsKey, (self).paddingScheme, d_11_encryptionContextDigest_, (self).grantTokens)
        d_12_decryptClosure_ = nw1_
        d_13_outcome_: Wrappers.Result
        out2_: Wrappers.Result
        out2_ = Actions.default__.ReduceToSuccess(d_12_decryptClosure_, d_7_edksToAttempt_)
        d_13_outcome_ = out2_
        d_14_valueOrError7_: Wrappers.Result = None
        def lambda0_(d_15_errors_):
            return AwsCryptographyMaterialProvidersTypes.Error_CollectionOfErrors(d_15_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."))

        d_14_valueOrError7_ = (d_13_outcome_).MapFailure(lambda0_)
        if (d_14_valueOrError7_).IsFailure():
            res = (d_14_valueOrError7_).PropagateFailure()
            return res
        d_16_SealedDecryptionMaterials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_16_SealedDecryptionMaterials_ = (d_14_valueOrError7_).Extract()
        res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnDecryptOutput_OnDecryptOutput(d_16_SealedDecryptionMaterials_))
        return res
        return res

    @property
    def cryptoPrimitives(self):
        return self._cryptoPrimitives
    @property
    def client(self):
        return self._client
    @property
    def paddingScheme(self):
        return self._paddingScheme
    @property
    def awsKmsKey(self):
        return self._awsKmsKey
    @property
    def publicKey(self):
        return self._publicKey
    @property
    def awsKmsArn(self):
        return self._awsKmsArn
    @property
    def grantTokens(self):
        return self._grantTokens

class DecryptSingleAWSRSAEncryptedDataKey(Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._materials: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials = None
        self._client: ComAmazonawsKmsTypes.IKMSClient = None
        self._awsKmsKey: _dafny.Seq = None
        self._paddingScheme: ComAmazonawsKmsTypes.EncryptionAlgorithmSpec = ComAmazonawsKmsTypes.EncryptionAlgorithmSpec.default()()
        self._encryptionContextDigest: _dafny.Seq = _dafny.Seq({})
        self._grantTokens: _dafny.Seq = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsRsaKeyring.DecryptSingleAWSRSAEncryptedDataKey"
    def ctor__(self, materials, client, awsKmsKey, paddingScheme, encryptionContextDigest, grantTokens):
        (self)._materials = materials
        (self)._client = client
        (self)._awsKmsKey = awsKmsKey
        (self)._paddingScheme = paddingScheme
        (self)._encryptionContextDigest = encryptionContextDigest
        (self)._grantTokens = grantTokens

    def Invoke(self, edk):
        res: Wrappers.Result = None
        d_0_unwrap_: KmsRsaUnwrapKeyMaterial
        nw0_ = KmsRsaUnwrapKeyMaterial()
        nw0_.ctor__((self).client, (self).awsKmsKey, (self).paddingScheme, (self).encryptionContextDigest, (self).grantTokens)
        d_0_unwrap_ = nw0_
        d_1_valueOrError0_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.UnwrapEdkMaterialOutput.default(KmsRsaUnwrapInfo.default()))()
        out0_: Wrappers.Result
        out0_ = EdkWrapping.default__.UnwrapEdkMaterial((edk).ciphertext, (self).materials, d_0_unwrap_)
        d_1_valueOrError0_ = out0_
        if (d_1_valueOrError0_).IsFailure():
            res = (d_1_valueOrError0_).PropagateFailure()
            return res
        d_2_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_2_unwrapOutput_ = (d_1_valueOrError0_).Extract()
        d_3_valueOrError1_: Wrappers.Result = None
        d_3_valueOrError1_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_2_unwrapOutput_).plaintextDataKey, (d_2_unwrapOutput_).symmetricSigningKey)
        if (d_3_valueOrError1_).IsFailure():
            res = (d_3_valueOrError1_).PropagateFailure()
            return res
        d_4_result_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_4_result_ = (d_3_valueOrError1_).Extract()
        res = Wrappers.Result_Success(d_4_result_)
        return res
        return res

    @property
    def materials(self):
        return self._materials
    @property
    def client(self):
        return self._client
    @property
    def awsKmsKey(self):
        return self._awsKmsKey
    @property
    def paddingScheme(self):
        return self._paddingScheme
    @property
    def encryptionContextDigest(self):
        return self._encryptionContextDigest
    @property
    def grantTokens(self):
        return self._grantTokens

class KmsRsaUnwrapInfo:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [KmsRsaUnwrapInfo_KmsRsaUnwrapInfo()]
    @classmethod
    def default(cls, ):
        return lambda: KmsRsaUnwrapInfo_KmsRsaUnwrapInfo()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KmsRsaUnwrapInfo(self) -> bool:
        return isinstance(self, KmsRsaUnwrapInfo_KmsRsaUnwrapInfo)

class KmsRsaUnwrapInfo_KmsRsaUnwrapInfo(KmsRsaUnwrapInfo, NamedTuple('KmsRsaUnwrapInfo', [])):
    def __dafnystr__(self) -> str:
        return f'AwsKmsRsaKeyring.KmsRsaUnwrapInfo.KmsRsaUnwrapInfo'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KmsRsaUnwrapInfo_KmsRsaUnwrapInfo)
    def __hash__(self) -> int:
        return super().__hash__()


class KmsRsaWrapInfo:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [KmsRsaWrapInfo_KmsRsaWrapInfo()]
    @classmethod
    def default(cls, ):
        return lambda: KmsRsaWrapInfo_KmsRsaWrapInfo()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KmsRsaWrapInfo(self) -> bool:
        return isinstance(self, KmsRsaWrapInfo_KmsRsaWrapInfo)

class KmsRsaWrapInfo_KmsRsaWrapInfo(KmsRsaWrapInfo, NamedTuple('KmsRsaWrapInfo', [])):
    def __dafnystr__(self) -> str:
        return f'AwsKmsRsaKeyring.KmsRsaWrapInfo.KmsRsaWrapInfo'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KmsRsaWrapInfo_KmsRsaWrapInfo)
    def __hash__(self) -> int:
        return super().__hash__()


class KmsRsaGenerateAndWrapKeyMaterial(MaterialWrapping.GenerateAndWrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._publicKey: _dafny.Seq = _dafny.Seq({})
        self._cryptoPrimitives: AtomicPrimitives.AtomicPrimitivesClient = None
        self._paddingScheme: ComAmazonawsKmsTypes.EncryptionAlgorithmSpec = ComAmazonawsKmsTypes.EncryptionAlgorithmSpec.default()()
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsRsaKeyring.KmsRsaGenerateAndWrapKeyMaterial"
    def ctor__(self, publicKey, paddingScheme, cryptoPrimitives):
        (self)._publicKey = publicKey
        (self)._cryptoPrimitives = cryptoPrimitives
        (self)._paddingScheme = paddingScheme

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.GenerateAndWrapOutput.default(KmsRsaWrapInfo.default()))()
        d_0_generateBytesResult_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = ((self).cryptoPrimitives).GenerateRandomBytes(AwsCryptographyPrimitivesTypes.GenerateRandomBytesInput_GenerateRandomBytesInput(AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)))
        d_0_generateBytesResult_ = out0_
        d_1_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda0_(d_2_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_2_e_)

        d_1_valueOrError0_ = (d_0_generateBytesResult_).MapFailure(lambda0_)
        if (d_1_valueOrError0_).IsFailure():
            res = (d_1_valueOrError0_).PropagateFailure()
            return res
        d_3_plaintextMaterial_: _dafny.Seq
        d_3_plaintextMaterial_ = (d_1_valueOrError0_).Extract()
        d_4_wrap_: KmsRsaWrapKeyMaterial
        nw0_ = KmsRsaWrapKeyMaterial()
        nw0_.ctor__((self).publicKey, (self).paddingScheme, (self).cryptoPrimitives)
        d_4_wrap_ = nw0_
        d_5_valueOrError1_: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.WrapOutput.default(KmsRsaWrapInfo.default()))()
        out1_: Wrappers.Result
        out1_ = (d_4_wrap_).Invoke(MaterialWrapping.WrapInput_WrapInput(d_3_plaintextMaterial_, (input).algorithmSuite, (input).encryptionContext))
        d_5_valueOrError1_ = out1_
        if (d_5_valueOrError1_).IsFailure():
            res = (d_5_valueOrError1_).PropagateFailure()
            return res
        d_6_wrapOutput_: MaterialWrapping.WrapOutput
        d_6_wrapOutput_ = (d_5_valueOrError1_).Extract()
        d_7_output_: MaterialWrapping.GenerateAndWrapOutput
        d_7_output_ = MaterialWrapping.GenerateAndWrapOutput_GenerateAndWrapOutput(d_3_plaintextMaterial_, (d_6_wrapOutput_).wrappedMaterial, KmsRsaWrapInfo_KmsRsaWrapInfo())
        res = Wrappers.Result_Success(d_7_output_)
        return res
        return res

    @property
    def publicKey(self):
        return self._publicKey
    @property
    def cryptoPrimitives(self):
        return self._cryptoPrimitives
    @property
    def paddingScheme(self):
        return self._paddingScheme

class KmsRsaWrapKeyMaterial(MaterialWrapping.WrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._publicKey: _dafny.Seq = _dafny.Seq({})
        self._cryptoPrimitives: AtomicPrimitives.AtomicPrimitivesClient = None
        self._paddingScheme: ComAmazonawsKmsTypes.EncryptionAlgorithmSpec = ComAmazonawsKmsTypes.EncryptionAlgorithmSpec.default()()
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsRsaKeyring.KmsRsaWrapKeyMaterial"
    def ctor__(self, publicKey, paddingScheme, cryptoPrimitives):
        (self)._publicKey = publicKey
        (self)._cryptoPrimitives = cryptoPrimitives
        (self)._paddingScheme = paddingScheme

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.WrapOutput.default(KmsRsaWrapInfo.default()))()
        d_0_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out0_: Wrappers.Result
        out0_ = default__.EncryptionContextDigest((self).cryptoPrimitives, (input).encryptionContext)
        d_0_valueOrError0_ = out0_
        if (d_0_valueOrError0_).IsFailure():
            res = (d_0_valueOrError0_).PropagateFailure()
            return res
        d_1_encryptionContextDigest_: _dafny.Seq
        d_1_encryptionContextDigest_ = (d_0_valueOrError0_).Extract()
        d_2_padding_: AwsCryptographyPrimitivesTypes.RSAPaddingMode
        source0_ = (self).paddingScheme
        with _dafny.label("match0"):
            if True:
                if source0_.is_RSAES__OAEP__SHA__1:
                    d_2_padding_ = AwsCryptographyPrimitivesTypes.RSAPaddingMode_OAEP__SHA1()
                    raise _dafny.Break("match0")
            if True:
                d_2_padding_ = AwsCryptographyPrimitivesTypes.RSAPaddingMode_OAEP__SHA256()
            pass
        d_3_RSAEncryptOutput_: Wrappers.Result
        out1_: Wrappers.Result
        out1_ = ((self).cryptoPrimitives).RSAEncrypt(AwsCryptographyPrimitivesTypes.RSAEncryptInput_RSAEncryptInput(d_2_padding_, (self).publicKey, (d_1_encryptionContextDigest_) + ((input).plaintextMaterial)))
        d_3_RSAEncryptOutput_ = out1_
        d_4_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda0_(d_5_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_5_e_)

        d_4_valueOrError1_ = (d_3_RSAEncryptOutput_).MapFailure(lambda0_)
        if (d_4_valueOrError1_).IsFailure():
            res = (d_4_valueOrError1_).PropagateFailure()
            return res
        d_6_ciphertext_: _dafny.Seq
        d_6_ciphertext_ = (d_4_valueOrError1_).Extract()
        d_7_output_: MaterialWrapping.WrapOutput
        d_7_output_ = MaterialWrapping.WrapOutput_WrapOutput(d_6_ciphertext_, KmsRsaWrapInfo_KmsRsaWrapInfo())
        res = Wrappers.Result_Success(d_7_output_)
        return res
        return res

    @property
    def publicKey(self):
        return self._publicKey
    @property
    def cryptoPrimitives(self):
        return self._cryptoPrimitives
    @property
    def paddingScheme(self):
        return self._paddingScheme

class KmsRsaUnwrapKeyMaterial(MaterialWrapping.UnwrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._client: ComAmazonawsKmsTypes.IKMSClient = None
        self._grantTokens: _dafny.Seq = None
        self._awsKmsKey: _dafny.Seq = None
        self._paddingScheme: ComAmazonawsKmsTypes.EncryptionAlgorithmSpec = ComAmazonawsKmsTypes.EncryptionAlgorithmSpec.default()()
        self._encryptionContextDigest: _dafny.Seq = _dafny.Seq({})
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsRsaKeyring.KmsRsaUnwrapKeyMaterial"
    def ctor__(self, client, awsKmsKey, paddingScheme, encryptionContextDigest, grantTokens):
        (self)._client = client
        (self)._awsKmsKey = awsKmsKey
        (self)._paddingScheme = paddingScheme
        (self)._encryptionContextDigest = encryptionContextDigest
        (self)._grantTokens = grantTokens

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.UnwrapOutput.default(KmsRsaUnwrapInfo.default()))()
        d_0_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_0_valueOrError0_ = Wrappers.default__.Need(ComAmazonawsKmsTypes.default__.IsValid__CiphertextType((input).wrappedMaterial), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Ciphertext length invalid")))
        if (d_0_valueOrError0_).IsFailure():
            res = (d_0_valueOrError0_).PropagateFailure()
            return res
        d_1_decryptRequest_: ComAmazonawsKmsTypes.DecryptRequest
        d_1_decryptRequest_ = ComAmazonawsKmsTypes.DecryptRequest_DecryptRequest((input).wrappedMaterial, Wrappers.Option_None(), Wrappers.Option_Some((self).grantTokens), Wrappers.Option_Some((self).awsKmsKey), Wrappers.Option_Some((self).paddingScheme), Wrappers.Option_None(), Wrappers.Option_None())
        d_2_maybeDecryptResponse_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = ((self).client).Decrypt(d_1_decryptRequest_)
        d_2_maybeDecryptResponse_ = out0_
        d_3_valueOrError1_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.DecryptResponse.default())()
        def lambda0_(d_4_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_ComAmazonawsKms(d_4_e_)

        d_3_valueOrError1_ = (d_2_maybeDecryptResponse_).MapFailure(lambda0_)
        if (d_3_valueOrError1_).IsFailure():
            res = (d_3_valueOrError1_).PropagateFailure()
            return res
        d_5_decryptResponse_: ComAmazonawsKmsTypes.DecryptResponse
        d_5_decryptResponse_ = (d_3_valueOrError1_).Extract()
        d_6_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_6_valueOrError2_ = Wrappers.default__.Need(((((d_5_decryptResponse_).KeyId).is_Some) and ((((d_5_decryptResponse_).KeyId).value) == ((self).awsKmsKey))) and (((d_5_decryptResponse_).Plaintext).is_Some), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from KMS Decrypt")))
        if (d_6_valueOrError2_).IsFailure():
            res = (d_6_valueOrError2_).PropagateFailure()
            return res
        d_7_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_7_valueOrError3_ = Wrappers.default__.Need((((self).encryptionContextDigest) <= (((d_5_decryptResponse_).Plaintext).value)) and (((AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)) + (len((self).encryptionContextDigest))) == (len(((d_5_decryptResponse_).Plaintext).value))), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption context digest does not match expected value.")))
        if (d_7_valueOrError3_).IsFailure():
            res = (d_7_valueOrError3_).PropagateFailure()
            return res
        d_8_output_: MaterialWrapping.UnwrapOutput
        d_8_output_ = MaterialWrapping.UnwrapOutput_UnwrapOutput(_dafny.Seq((((d_5_decryptResponse_).Plaintext).value)[len((self).encryptionContextDigest)::]), KmsRsaUnwrapInfo_KmsRsaUnwrapInfo())
        res = Wrappers.Result_Success(d_8_output_)
        return res
        return res

    @property
    def client(self):
        return self._client
    @property
    def grantTokens(self):
        return self._grantTokens
    @property
    def awsKmsKey(self):
        return self._awsKmsKey
    @property
    def paddingScheme(self):
        return self._paddingScheme
    @property
    def encryptionContextDigest(self):
        return self._encryptionContextDigest
