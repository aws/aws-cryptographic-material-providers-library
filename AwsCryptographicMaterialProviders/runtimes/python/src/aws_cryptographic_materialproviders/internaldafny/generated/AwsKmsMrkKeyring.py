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
        out108_: Wrappers.Result
        out108_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnDecrypt(self, input)
        return out108_

    def OnEncrypt(self, input):
        out109_: Wrappers.Result
        out109_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnEncrypt(self, input)
        return out109_

    def ctor__(self, client, awsKmsKey, grantTokens):
        d_743_parsedAwsKmsId_: Wrappers.Result
        d_743_parsedAwsKmsId_ = AwsArnParsing.default__.ParseAwsKmsIdentifier(awsKmsKey)
        (self)._client = client
        (self)._awsKmsKey = awsKmsKey
        (self)._awsKmsArn = (d_743_parsedAwsKmsId_).value
        (self)._grantTokens = grantTokens

    def OnEncrypt_k(self, input):
        output: Wrappers.Result = None
        d_744_materials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_744_materials_ = (input).materials
        d_745_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_745_suite_ = ((input).materials).algorithmSuite
        d_746_stringifiedEncCtx_: _dafny.Map
        d_747_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        d_747_valueOrError0_ = AwsKmsUtils.default__.StringifyEncryptionContext(((input).materials).encryptionContext)
        if (d_747_valueOrError0_).IsFailure():
            output = (d_747_valueOrError0_).PropagateFailure()
            return output
        d_746_stringifiedEncCtx_ = (d_747_valueOrError0_).Extract()
        d_748_kmsGenerateAndWrap_: AwsKmsKeyring.KmsGenerateAndWrapKeyMaterial
        nw20_ = AwsKmsKeyring.KmsGenerateAndWrapKeyMaterial()
        nw20_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_748_kmsGenerateAndWrap_ = nw20_
        d_749_kmsWrap_: AwsKmsKeyring.KmsWrapKeyMaterial
        nw21_ = AwsKmsKeyring.KmsWrapKeyMaterial()
        nw21_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_749_kmsWrap_ = nw21_
        d_750_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_751_valueOrError1_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.WrapEdkMaterialOutput.default(AwsKmsKeyring.KmsWrapInfo.default()))()
        out110_: Wrappers.Result
        out110_ = EdkWrapping.default__.WrapEdkMaterial(d_744_materials_, d_749_kmsWrap_, d_748_kmsGenerateAndWrap_)
        d_751_valueOrError1_ = out110_
        if (d_751_valueOrError1_).IsFailure():
            output = (d_751_valueOrError1_).PropagateFailure()
            return output
        d_750_wrapOutput_ = (d_751_valueOrError1_).Extract()
        d_752_kmsKeyArn_: _dafny.Seq
        d_752_kmsKeyArn_ = ((d_750_wrapOutput_).wrapInfo).kmsKeyArn
        d_753_symmetricSigningKeyList_: Wrappers.Option
        d_753_symmetricSigningKeyList_ = (Wrappers.Option_Some(_dafny.Seq([((d_750_wrapOutput_).symmetricSigningKey).value])) if ((d_750_wrapOutput_).symmetricSigningKey).is_Some else Wrappers.Option_None())
        d_754_providerInfo_: _dafny.Seq
        d_755_valueOrError2_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_755_valueOrError2_ = (UTF8.default__.Encode(d_752_kmsKeyArn_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_755_valueOrError2_).IsFailure():
            output = (d_755_valueOrError2_).PropagateFailure()
            return output
        d_754_providerInfo_ = (d_755_valueOrError2_).Extract()
        d_756_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_756_valueOrError3_ = Wrappers.default__.Need((len(d_754_providerInfo_)) < (StandardLibrary_UInt.default__.UINT16__LIMIT), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS GenerateDataKey: Key ID too long.")))
        if (d_756_valueOrError3_).IsFailure():
            output = (d_756_valueOrError3_).PropagateFailure()
            return output
        d_757_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_757_edk_ = AwsCryptographyMaterialProvidersTypes.EncryptedDataKey_EncryptedDataKey(Constants.default__.PROVIDER__ID, d_754_providerInfo_, (d_750_wrapOutput_).wrappedMaterial)
        if (d_750_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_758_result_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_759_valueOrError4_: Wrappers.Result = None
            d_759_valueOrError4_ = Materials.default__.EncryptionMaterialAddDataKey(d_744_materials_, (d_750_wrapOutput_).plaintextDataKey, _dafny.Seq([d_757_edk_]), d_753_symmetricSigningKeyList_)
            if (d_759_valueOrError4_).IsFailure():
                output = (d_759_valueOrError4_).PropagateFailure()
                return output
            d_758_result_ = (d_759_valueOrError4_).Extract()
            output = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(d_758_result_))
            return output
        elif (d_750_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_760_result_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_761_valueOrError5_: Wrappers.Result = None
            d_761_valueOrError5_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys(d_744_materials_, _dafny.Seq([d_757_edk_]), d_753_symmetricSigningKeyList_)
            if (d_761_valueOrError5_).IsFailure():
                output = (d_761_valueOrError5_).PropagateFailure()
                return output
            d_760_result_ = (d_761_valueOrError5_).Extract()
            output = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(d_760_result_))
            return output
        return output

    def OnDecrypt_k(self, input):
        output: Wrappers.Result = None
        d_762_materials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_762_materials_ = (input).materials
        d_763_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_763_suite_ = ((input).materials).algorithmSuite
        d_764_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_764_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_762_materials_), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_764_valueOrError0_).IsFailure():
            output = (d_764_valueOrError0_).PropagateFailure()
            return output
        d_765_filter_: AwsKmsUtils.OnDecryptMrkAwareEncryptedDataKeyFilter
        nw22_ = AwsKmsUtils.OnDecryptMrkAwareEncryptedDataKeyFilter()
        nw22_.ctor__((self).awsKmsArn, Constants.default__.PROVIDER__ID)
        d_765_filter_ = nw22_
        d_766_edksToAttempt_: _dafny.Seq
        d_767_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out111_: Wrappers.Result
        out111_ = Actions.default__.FilterWithResult(d_765_filter_, (input).encryptedDataKeys)
        d_767_valueOrError1_ = out111_
        if (d_767_valueOrError1_).IsFailure():
            output = (d_767_valueOrError1_).PropagateFailure()
            return output
        d_766_edksToAttempt_ = (d_767_valueOrError1_).Extract()
        if (0) == (len(d_766_edksToAttempt_)):
            d_768_errorMessage_: _dafny.Seq
            d_769_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            d_769_valueOrError2_ = ErrorMessages.default__.IncorrectDataKeys((input).encryptedDataKeys, ((input).materials).algorithmSuite, _dafny.Seq(""))
            if (d_769_valueOrError2_).IsFailure():
                output = (d_769_valueOrError2_).PropagateFailure()
                return output
            d_768_errorMessage_ = (d_769_valueOrError2_).Extract()
            output = Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_768_errorMessage_))
            return output
        d_770_decryptClosure_: DecryptSingleEncryptedDataKey
        nw23_ = DecryptSingleEncryptedDataKey()
        nw23_.ctor__(d_762_materials_, (self).client, (self).awsKmsKey, (self).grantTokens)
        d_770_decryptClosure_ = nw23_
        d_771_outcome_: Wrappers.Result
        out112_: Wrappers.Result
        out112_ = Actions.default__.ReduceToSuccess(d_770_decryptClosure_, d_766_edksToAttempt_)
        d_771_outcome_ = out112_
        d_772_SealedDecryptionMaterials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_773_valueOrError3_: Wrappers.Result = None
        def lambda71_(d_774_errors_):
            return AwsCryptographyMaterialProvidersTypes.Error_CollectionOfErrors(d_774_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."))

        d_773_valueOrError3_ = (d_771_outcome_).MapFailure(lambda71_)
        if (d_773_valueOrError3_).IsFailure():
            output = (d_773_valueOrError3_).PropagateFailure()
            return output
        d_772_SealedDecryptionMaterials_ = (d_773_valueOrError3_).Extract()
        output = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnDecryptOutput_OnDecryptOutput(d_772_SealedDecryptionMaterials_))
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
        d_775_kmsUnwrap_: AwsKmsKeyring.KmsUnwrapKeyMaterial
        nw24_ = AwsKmsKeyring.KmsUnwrapKeyMaterial()
        nw24_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_775_kmsUnwrap_ = nw24_
        d_776_unwrapOutputRes_: Wrappers.Result
        out113_: Wrappers.Result
        out113_ = EdkWrapping.default__.UnwrapEdkMaterial((edk).ciphertext, (self).materials, d_775_kmsUnwrap_)
        d_776_unwrapOutputRes_ = out113_
        d_777_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_778_valueOrError0_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.UnwrapEdkMaterialOutput.default(AwsKmsKeyring.KmsUnwrapInfo.default()))()
        d_778_valueOrError0_ = d_776_unwrapOutputRes_
        if (d_778_valueOrError0_).IsFailure():
            res = (d_778_valueOrError0_).PropagateFailure()
            return res
        d_777_unwrapOutput_ = (d_778_valueOrError0_).Extract()
        d_779_result_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_780_valueOrError1_: Wrappers.Result = None
        d_780_valueOrError1_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_777_unwrapOutput_).plaintextDataKey, (d_777_unwrapOutput_).symmetricSigningKey)
        if (d_780_valueOrError1_).IsFailure():
            res = (d_780_valueOrError1_).PropagateFailure()
            return res
        d_779_result_ = (d_780_valueOrError1_).Extract()
        res = Wrappers.Result_Success(d_779_result_)
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
