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

# Module: AwsKmsMrkKeyring


class AwsKmsMrkKeyring(Keyring.VerifiableInterface, AwsCryptographyMaterialProvidersTypes.IKeyring):
    def  __init__(self):
        self._client: ComAmazonawsKmsTypes.IKMSClient = None
        self._awsKmsKey: _dafny.Seq = None
        self._grantTokens: _dafny.Seq = None
        self._awsKmsArn: AwsArnParsing.AwsKmsIdentifier = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsMrkKeyring.AwsKmsMrkKeyring"
    def OnDecrypt(self, input):
        out5_: Wrappers.Result
        out5_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnDecrypt(self, input)
        return out5_

    def OnEncrypt(self, input):
        out5_: Wrappers.Result
        out5_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnEncrypt(self, input)
        return out5_

    def ctor__(self, client, awsKmsKey, grantTokens):
        d_0_parsedAwsKmsId_: Wrappers.Result
        d_0_parsedAwsKmsId_ = AwsArnParsing.default__.ParseAwsKmsIdentifier(awsKmsKey)
        (self)._client = client
        (self)._awsKmsKey = awsKmsKey
        (self)._awsKmsArn = (d_0_parsedAwsKmsId_).value
        (self)._grantTokens = grantTokens

    def OnEncrypt_k(self, input):
        output: Wrappers.Result = None
        d_0_materials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_0_materials_ = (input).materials
        d_1_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_1_suite_ = ((input).materials).algorithmSuite
        d_2_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        d_2_valueOrError0_ = AwsKmsUtils.default__.StringifyEncryptionContext(((input).materials).encryptionContext)
        if (d_2_valueOrError0_).IsFailure():
            output = (d_2_valueOrError0_).PropagateFailure()
            return output
        d_3_stringifiedEncCtx_: _dafny.Map
        d_3_stringifiedEncCtx_ = (d_2_valueOrError0_).Extract()
        d_4_kmsGenerateAndWrap_: AwsKmsKeyring.KmsGenerateAndWrapKeyMaterial
        nw0_ = AwsKmsKeyring.KmsGenerateAndWrapKeyMaterial()
        nw0_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_4_kmsGenerateAndWrap_ = nw0_
        d_5_kmsWrap_: AwsKmsKeyring.KmsWrapKeyMaterial
        nw1_ = AwsKmsKeyring.KmsWrapKeyMaterial()
        nw1_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_5_kmsWrap_ = nw1_
        d_6_valueOrError1_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.WrapEdkMaterialOutput.default(AwsKmsKeyring.KmsWrapInfo.default()))()
        out0_: Wrappers.Result
        out0_ = EdkWrapping.default__.WrapEdkMaterial(d_0_materials_, d_5_kmsWrap_, d_4_kmsGenerateAndWrap_)
        d_6_valueOrError1_ = out0_
        if (d_6_valueOrError1_).IsFailure():
            output = (d_6_valueOrError1_).PropagateFailure()
            return output
        d_7_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_7_wrapOutput_ = (d_6_valueOrError1_).Extract()
        d_8_kmsKeyArn_: _dafny.Seq
        d_8_kmsKeyArn_ = ((d_7_wrapOutput_).wrapInfo).kmsKeyArn
        d_9_symmetricSigningKeyList_: Wrappers.Option
        if ((d_7_wrapOutput_).symmetricSigningKey).is_Some:
            d_9_symmetricSigningKeyList_ = Wrappers.Option_Some(_dafny.Seq([((d_7_wrapOutput_).symmetricSigningKey).value]))
        elif True:
            d_9_symmetricSigningKeyList_ = Wrappers.Option_None()
        d_10_valueOrError2_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_10_valueOrError2_ = (UTF8.default__.Encode(d_8_kmsKeyArn_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_10_valueOrError2_).IsFailure():
            output = (d_10_valueOrError2_).PropagateFailure()
            return output
        d_11_providerInfo_: _dafny.Seq
        d_11_providerInfo_ = (d_10_valueOrError2_).Extract()
        d_12_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_12_valueOrError3_ = Wrappers.default__.Need((len(d_11_providerInfo_)) < (StandardLibrary_UInt.default__.UINT16__LIMIT), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS GenerateDataKey: Key ID too long.")))
        if (d_12_valueOrError3_).IsFailure():
            output = (d_12_valueOrError3_).PropagateFailure()
            return output
        d_13_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_13_edk_ = AwsCryptographyMaterialProvidersTypes.EncryptedDataKey_EncryptedDataKey(Constants.default__.PROVIDER__ID, d_11_providerInfo_, (d_7_wrapOutput_).wrappedMaterial)
        if (d_7_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_14_valueOrError4_: Wrappers.Result = None
            d_14_valueOrError4_ = Materials.default__.EncryptionMaterialAddDataKey(d_0_materials_, (d_7_wrapOutput_).plaintextDataKey, _dafny.Seq([d_13_edk_]), d_9_symmetricSigningKeyList_)
            if (d_14_valueOrError4_).IsFailure():
                output = (d_14_valueOrError4_).PropagateFailure()
                return output
            d_15_result_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_15_result_ = (d_14_valueOrError4_).Extract()
            output = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(d_15_result_))
            return output
        elif (d_7_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_16_valueOrError5_: Wrappers.Result = None
            d_16_valueOrError5_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys(d_0_materials_, _dafny.Seq([d_13_edk_]), d_9_symmetricSigningKeyList_)
            if (d_16_valueOrError5_).IsFailure():
                output = (d_16_valueOrError5_).PropagateFailure()
                return output
            d_17_result_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_17_result_ = (d_16_valueOrError5_).Extract()
            output = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(d_17_result_))
            return output
        return output

    def OnDecrypt_k(self, input):
        output: Wrappers.Result = None
        d_0_materials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_0_materials_ = (input).materials
        d_1_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_1_suite_ = ((input).materials).algorithmSuite
        d_2_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_2_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_0_materials_), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_2_valueOrError0_).IsFailure():
            output = (d_2_valueOrError0_).PropagateFailure()
            return output
        d_3_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_3_valueOrError1_ = AwsKmsUtils.default__.OkForDecrypt((self).awsKmsArn, (self).awsKmsKey)
        if (d_3_valueOrError1_).IsFailure():
            output = (d_3_valueOrError1_).PropagateFailure()
            return output
        d_4_filter_: AwsKmsUtils.OnDecryptMrkAwareEncryptedDataKeyFilter
        nw0_ = AwsKmsUtils.OnDecryptMrkAwareEncryptedDataKeyFilter()
        nw0_.ctor__((self).awsKmsArn, Constants.default__.PROVIDER__ID)
        d_4_filter_ = nw0_
        d_5_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out0_: Wrappers.Result
        out0_ = Actions.default__.FilterWithResult(d_4_filter_, (input).encryptedDataKeys)
        d_5_valueOrError2_ = out0_
        if (d_5_valueOrError2_).IsFailure():
            output = (d_5_valueOrError2_).PropagateFailure()
            return output
        d_6_edksToAttempt_: _dafny.Seq
        d_6_edksToAttempt_ = (d_5_valueOrError2_).Extract()
        if (0) == (len(d_6_edksToAttempt_)):
            d_7_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            d_7_valueOrError3_ = ErrorMessages.default__.IncorrectDataKeys((input).encryptedDataKeys, ((input).materials).algorithmSuite, _dafny.Seq(""))
            if (d_7_valueOrError3_).IsFailure():
                output = (d_7_valueOrError3_).PropagateFailure()
                return output
            d_8_errorMessage_: _dafny.Seq
            d_8_errorMessage_ = (d_7_valueOrError3_).Extract()
            output = Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_8_errorMessage_))
            return output
        d_9_decryptClosure_: DecryptSingleEncryptedDataKey
        nw1_ = DecryptSingleEncryptedDataKey()
        nw1_.ctor__(d_0_materials_, (self).client, (self).awsKmsKey, (self).grantTokens)
        d_9_decryptClosure_ = nw1_
        d_10_outcome_: Wrappers.Result
        out1_: Wrappers.Result
        out1_ = Actions.default__.ReduceToSuccess(d_9_decryptClosure_, d_6_edksToAttempt_)
        d_10_outcome_ = out1_
        d_11_valueOrError4_: Wrappers.Result = None
        def lambda0_(d_12_errors_):
            return AwsCryptographyMaterialProvidersTypes.Error_CollectionOfErrors(d_12_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."))

        d_11_valueOrError4_ = (d_10_outcome_).MapFailure(lambda0_)
        if (d_11_valueOrError4_).IsFailure():
            output = (d_11_valueOrError4_).PropagateFailure()
            return output
        d_13_SealedDecryptionMaterials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_13_SealedDecryptionMaterials_ = (d_11_valueOrError4_).Extract()
        output = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnDecryptOutput_OnDecryptOutput(d_13_SealedDecryptionMaterials_))
        return output
        return output

    @property
    def client(self):
        return self._client
    @property
    def awsKmsKey(self):
        return self._awsKmsKey
    @property
    def grantTokens(self):
        return self._grantTokens
    @property
    def awsKmsArn(self):
        return self._awsKmsArn

class DecryptSingleEncryptedDataKey(Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._materials: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials = None
        self._client: ComAmazonawsKmsTypes.IKMSClient = None
        self._awsKmsKey: _dafny.Seq = None
        self._grantTokens: _dafny.Seq = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsMrkKeyring.DecryptSingleEncryptedDataKey"
    def ctor__(self, materials, client, awsKmsKey, grantTokens):
        (self)._materials = materials
        (self)._client = client
        (self)._awsKmsKey = awsKmsKey
        (self)._grantTokens = grantTokens

    def Invoke(self, edk):
        res: Wrappers.Result = None
        d_0_kmsUnwrap_: AwsKmsKeyring.KmsUnwrapKeyMaterial
        nw0_ = AwsKmsKeyring.KmsUnwrapKeyMaterial()
        nw0_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_0_kmsUnwrap_ = nw0_
        d_1_unwrapOutputRes_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = EdkWrapping.default__.UnwrapEdkMaterial((edk).ciphertext, (self).materials, d_0_kmsUnwrap_)
        d_1_unwrapOutputRes_ = out0_
        d_2_valueOrError0_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.UnwrapEdkMaterialOutput.default(AwsKmsKeyring.KmsUnwrapInfo.default()))()
        d_2_valueOrError0_ = d_1_unwrapOutputRes_
        if (d_2_valueOrError0_).IsFailure():
            res = (d_2_valueOrError0_).PropagateFailure()
            return res
        d_3_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_3_unwrapOutput_ = (d_2_valueOrError0_).Extract()
        d_4_valueOrError1_: Wrappers.Result = None
        d_4_valueOrError1_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_3_unwrapOutput_).plaintextDataKey, (d_3_unwrapOutput_).symmetricSigningKey)
        if (d_4_valueOrError1_).IsFailure():
            res = (d_4_valueOrError1_).PropagateFailure()
            return res
        d_5_result_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_5_result_ = (d_4_valueOrError1_).Extract()
        res = Wrappers.Result_Success(d_5_result_)
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
    def grantTokens(self):
        return self._grantTokens
