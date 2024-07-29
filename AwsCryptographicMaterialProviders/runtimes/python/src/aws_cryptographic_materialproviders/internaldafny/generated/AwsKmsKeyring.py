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
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialWrapping as MaterialWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_materialproviders.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.EdkWrapping as EdkWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.ErrorMessages as ErrorMessages

# Module: AwsKmsKeyring


class AwsKmsKeyring(Keyring.VerifiableInterface, AwsCryptographyMaterialProvidersTypes.IKeyring):
    def  __init__(self):
        self._client: ComAmazonawsKmsTypes.IKMSClient = None
        self._awsKmsKey: _dafny.Seq = None
        self._grantTokens: _dafny.Seq = None
        self._awsKmsArn: AwsArnParsing.AwsKmsIdentifier = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsKeyring.AwsKmsKeyring"
    def OnDecrypt(self, input):
        out84_: Wrappers.Result
        out84_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnDecrypt(self, input)
        return out84_

    def OnEncrypt(self, input):
        out85_: Wrappers.Result
        out85_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnEncrypt(self, input)
        return out85_

    def ctor__(self, client, awsKmsKey, grantTokens):
        d_557_parsedAwsKmsId_: Wrappers.Result
        d_557_parsedAwsKmsId_ = AwsArnParsing.default__.ParseAwsKmsIdentifier(awsKmsKey)
        (self)._client = client
        (self)._awsKmsKey = awsKmsKey
        (self)._awsKmsArn = (d_557_parsedAwsKmsId_).value
        (self)._grantTokens = grantTokens

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        d_558_materials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_558_materials_ = (input).materials
        d_559_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_559_suite_ = ((input).materials).algorithmSuite
        d_560_stringifiedEncCtx_: _dafny.Map
        d_561_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        d_561_valueOrError0_ = AwsKmsUtils.default__.StringifyEncryptionContext(((input).materials).encryptionContext)
        if (d_561_valueOrError0_).IsFailure():
            res = (d_561_valueOrError0_).PropagateFailure()
            return res
        d_560_stringifiedEncCtx_ = (d_561_valueOrError0_).Extract()
        d_562_kmsGenerateAndWrap_: KmsGenerateAndWrapKeyMaterial
        nw1_ = KmsGenerateAndWrapKeyMaterial()
        nw1_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_562_kmsGenerateAndWrap_ = nw1_
        d_563_kmsWrap_: KmsWrapKeyMaterial
        nw2_ = KmsWrapKeyMaterial()
        nw2_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_563_kmsWrap_ = nw2_
        d_564_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_565_valueOrError1_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.WrapEdkMaterialOutput.default(KmsWrapInfo.default()))()
        out86_: Wrappers.Result
        out86_ = EdkWrapping.default__.WrapEdkMaterial(d_558_materials_, d_563_kmsWrap_, d_562_kmsGenerateAndWrap_)
        d_565_valueOrError1_ = out86_
        if (d_565_valueOrError1_).IsFailure():
            res = (d_565_valueOrError1_).PropagateFailure()
            return res
        d_564_wrapOutput_ = (d_565_valueOrError1_).Extract()
        d_566_kmsKeyArn_: _dafny.Seq
        d_566_kmsKeyArn_ = ((d_564_wrapOutput_).wrapInfo).kmsKeyArn
        d_567_symmetricSigningKeyList_: Wrappers.Option
        d_567_symmetricSigningKeyList_ = (Wrappers.Option_Some(_dafny.Seq([((d_564_wrapOutput_).symmetricSigningKey).value])) if ((d_564_wrapOutput_).symmetricSigningKey).is_Some else Wrappers.Option_None())
        d_568_providerInfo_: _dafny.Seq
        d_569_valueOrError2_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_569_valueOrError2_ = (UTF8.default__.Encode(d_566_kmsKeyArn_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_569_valueOrError2_).IsFailure():
            res = (d_569_valueOrError2_).PropagateFailure()
            return res
        d_568_providerInfo_ = (d_569_valueOrError2_).Extract()
        d_570_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_570_valueOrError3_ = Wrappers.default__.Need((len(d_568_providerInfo_)) < (StandardLibrary_UInt.default__.UINT16__LIMIT), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS GenerateDataKey: Key ID too long.")))
        if (d_570_valueOrError3_).IsFailure():
            res = (d_570_valueOrError3_).PropagateFailure()
            return res
        d_571_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_571_edk_ = AwsCryptographyMaterialProvidersTypes.EncryptedDataKey_EncryptedDataKey(Constants.default__.PROVIDER__ID, d_568_providerInfo_, (d_564_wrapOutput_).wrappedMaterial)
        if (d_564_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_572_result_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_573_valueOrError4_: Wrappers.Result = None
            d_573_valueOrError4_ = Materials.default__.EncryptionMaterialAddDataKey(d_558_materials_, (d_564_wrapOutput_).plaintextDataKey, _dafny.Seq([d_571_edk_]), d_567_symmetricSigningKeyList_)
            if (d_573_valueOrError4_).IsFailure():
                res = (d_573_valueOrError4_).PropagateFailure()
                return res
            d_572_result_ = (d_573_valueOrError4_).Extract()
            res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(d_572_result_))
            return res
        elif (d_564_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_574_result_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_575_valueOrError5_: Wrappers.Result = None
            d_575_valueOrError5_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys(d_558_materials_, _dafny.Seq([d_571_edk_]), d_567_symmetricSigningKeyList_)
            if (d_575_valueOrError5_).IsFailure():
                res = (d_575_valueOrError5_).PropagateFailure()
                return res
            d_574_result_ = (d_575_valueOrError5_).Extract()
            res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(d_574_result_))
            return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_576_materials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_576_materials_ = (input).materials
        d_577_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_577_suite_ = ((input).materials).algorithmSuite
        d_578_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_578_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_576_materials_), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_578_valueOrError0_).IsFailure():
            res = (d_578_valueOrError0_).PropagateFailure()
            return res
        d_579_filter_: OnDecryptEncryptedDataKeyFilter
        nw3_ = OnDecryptEncryptedDataKeyFilter()
        nw3_.ctor__((self).awsKmsKey)
        d_579_filter_ = nw3_
        d_580_edksToAttempt_: _dafny.Seq
        d_581_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out87_: Wrappers.Result
        out87_ = Actions.default__.FilterWithResult(d_579_filter_, (input).encryptedDataKeys)
        d_581_valueOrError1_ = out87_
        if (d_581_valueOrError1_).IsFailure():
            res = (d_581_valueOrError1_).PropagateFailure()
            return res
        d_580_edksToAttempt_ = (d_581_valueOrError1_).Extract()
        if (0) == (len(d_580_edksToAttempt_)):
            d_582_errorMessage_: _dafny.Seq
            d_583_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            d_583_valueOrError2_ = ErrorMessages.default__.IncorrectDataKeys((input).encryptedDataKeys, ((input).materials).algorithmSuite, _dafny.Seq(""))
            if (d_583_valueOrError2_).IsFailure():
                res = (d_583_valueOrError2_).PropagateFailure()
                return res
            d_582_errorMessage_ = (d_583_valueOrError2_).Extract()
            res = Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_582_errorMessage_))
            return res
        d_584_decryptClosure_: Actions.ActionWithResult
        nw4_ = DecryptSingleEncryptedDataKey()
        nw4_.ctor__(d_576_materials_, (self).client, (self).awsKmsKey, (self).grantTokens)
        d_584_decryptClosure_ = nw4_
        d_585_outcome_: Wrappers.Result
        out88_: Wrappers.Result
        out88_ = Actions.default__.ReduceToSuccess(d_584_decryptClosure_, d_580_edksToAttempt_)
        d_585_outcome_ = out88_
        d_586_SealedDecryptionMaterials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_587_valueOrError3_: Wrappers.Result = None
        def lambda60_(d_588_errors_):
            return AwsCryptographyMaterialProvidersTypes.Error_CollectionOfErrors(d_588_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."))

        d_587_valueOrError3_ = (d_585_outcome_).MapFailure(lambda60_)
        if (d_587_valueOrError3_).IsFailure():
            res = (d_587_valueOrError3_).PropagateFailure()
            return res
        d_586_SealedDecryptionMaterials_ = (d_587_valueOrError3_).Extract()
        res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnDecryptOutput_OnDecryptOutput(d_586_SealedDecryptionMaterials_))
        return res
        return res

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

class OnDecryptEncryptedDataKeyFilter(Actions.DeterministicActionWithResult, Actions.DeterministicAction):
    def  __init__(self):
        self._awsKmsKey: _dafny.Seq = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsKeyring.OnDecryptEncryptedDataKeyFilter"
    def ctor__(self, awsKmsKey):
        (self)._awsKmsKey = awsKmsKey

    def Invoke(self, edk):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        if ((edk).keyProviderId) != (Constants.default__.PROVIDER__ID):
            res = Wrappers.Result_Success(False)
            return res
        if not(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo)):
            res = Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid AWS KMS encoding, provider info is not UTF8.")))
            return res
        d_589_keyId_: _dafny.Seq
        d_590_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_590_valueOrError0_ = (UTF8.default__.Decode((edk).keyProviderInfo)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_590_valueOrError0_).IsFailure():
            res = (d_590_valueOrError0_).PropagateFailure()
            return res
        d_589_keyId_ = (d_590_valueOrError0_).Extract()
        d_591___v0_: AwsArnParsing.AwsArn
        d_592_valueOrError1_: Wrappers.Result = None
        d_592_valueOrError1_ = (AwsArnParsing.default__.ParseAwsKmsArn(d_589_keyId_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_592_valueOrError1_).IsFailure():
            res = (d_592_valueOrError1_).PropagateFailure()
            return res
        d_591___v0_ = (d_592_valueOrError1_).Extract()
        res = Wrappers.Result_Success(((self).awsKmsKey) == (d_589_keyId_))
        return res
        return res

    @property
    def awsKmsKey(self):
        return self._awsKmsKey

class DecryptSingleEncryptedDataKey(Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._materials: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials = None
        self._client: ComAmazonawsKmsTypes.IKMSClient = None
        self._awsKmsKey: _dafny.Seq = None
        self._grantTokens: _dafny.Seq = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsKeyring.DecryptSingleEncryptedDataKey"
    def ctor__(self, materials, client, awsKmsKey, grantTokens):
        (self)._materials = materials
        (self)._client = client
        (self)._awsKmsKey = awsKmsKey
        (self)._grantTokens = grantTokens

    def Invoke(self, edk):
        res: Wrappers.Result = None
        d_593_kmsUnwrap_: KmsUnwrapKeyMaterial
        nw5_ = KmsUnwrapKeyMaterial()
        nw5_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_593_kmsUnwrap_ = nw5_
        d_594_unwrapOutputRes_: Wrappers.Result
        out89_: Wrappers.Result
        out89_ = EdkWrapping.default__.UnwrapEdkMaterial((edk).ciphertext, (self).materials, d_593_kmsUnwrap_)
        d_594_unwrapOutputRes_ = out89_
        d_595_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_596_valueOrError0_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.UnwrapEdkMaterialOutput.default(KmsUnwrapInfo.default()))()
        d_596_valueOrError0_ = d_594_unwrapOutputRes_
        if (d_596_valueOrError0_).IsFailure():
            res = (d_596_valueOrError0_).PropagateFailure()
            return res
        d_595_unwrapOutput_ = (d_596_valueOrError0_).Extract()
        d_597_result_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_598_valueOrError1_: Wrappers.Result = None
        d_598_valueOrError1_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_595_unwrapOutput_).plaintextDataKey, (d_595_unwrapOutput_).symmetricSigningKey)
        if (d_598_valueOrError1_).IsFailure():
            res = (d_598_valueOrError1_).PropagateFailure()
            return res
        d_597_result_ = (d_598_valueOrError1_).Extract()
        res = Wrappers.Result_Success(d_597_result_)
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

class KmsUnwrapInfo:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [KmsUnwrapInfo_KmsUnwrapInfo()]
    @classmethod
    def default(cls, ):
        return lambda: KmsUnwrapInfo_KmsUnwrapInfo()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KmsUnwrapInfo(self) -> bool:
        return isinstance(self, KmsUnwrapInfo_KmsUnwrapInfo)

class KmsUnwrapInfo_KmsUnwrapInfo(KmsUnwrapInfo, NamedTuple('KmsUnwrapInfo', [])):
    def __dafnystr__(self) -> str:
        return f'AwsKmsKeyring.KmsUnwrapInfo.KmsUnwrapInfo'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KmsUnwrapInfo_KmsUnwrapInfo)
    def __hash__(self) -> int:
        return super().__hash__()


class KmsWrapInfo:
    @classmethod
    def default(cls, ):
        return lambda: KmsWrapInfo_KmsWrapInfo(_dafny.Seq(""))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KmsWrapInfo(self) -> bool:
        return isinstance(self, KmsWrapInfo_KmsWrapInfo)

class KmsWrapInfo_KmsWrapInfo(KmsWrapInfo, NamedTuple('KmsWrapInfo', [('kmsKeyArn', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsKmsKeyring.KmsWrapInfo.KmsWrapInfo({_dafny.string_of(self.kmsKeyArn)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KmsWrapInfo_KmsWrapInfo) and self.kmsKeyArn == __o.kmsKeyArn
    def __hash__(self) -> int:
        return super().__hash__()


class KmsUnwrapKeyMaterial(MaterialWrapping.UnwrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._client: ComAmazonawsKmsTypes.IKMSClient = None
        self._grantTokens: _dafny.Seq = None
        self._awsKmsKey: _dafny.Seq = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsKeyring.KmsUnwrapKeyMaterial"
    def ctor__(self, client, awsKmsKey, grantTokens):
        (self)._client = client
        (self)._awsKmsKey = awsKmsKey
        (self)._grantTokens = grantTokens

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.UnwrapOutput.default(KmsUnwrapInfo.default()))()
        d_599_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_599_valueOrError0_ = Wrappers.default__.Need(ComAmazonawsKmsTypes.default__.IsValid__CiphertextType((input).wrappedMaterial), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Ciphertext length invalid")))
        if (d_599_valueOrError0_).IsFailure():
            res = (d_599_valueOrError0_).PropagateFailure()
            return res
        d_600_stringifiedEncCtx_: _dafny.Map
        d_601_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        d_601_valueOrError1_ = AwsKmsUtils.default__.StringifyEncryptionContext((input).encryptionContext)
        if (d_601_valueOrError1_).IsFailure():
            res = (d_601_valueOrError1_).PropagateFailure()
            return res
        d_600_stringifiedEncCtx_ = (d_601_valueOrError1_).Extract()
        d_602_decryptRequest_: ComAmazonawsKmsTypes.DecryptRequest
        d_602_decryptRequest_ = ComAmazonawsKmsTypes.DecryptRequest_DecryptRequest((input).wrappedMaterial, Wrappers.Option_Some(d_600_stringifiedEncCtx_), Wrappers.Option_Some((self).grantTokens), Wrappers.Option_Some((self).awsKmsKey), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_603_maybeDecryptResponse_: Wrappers.Result
        out90_: Wrappers.Result
        out90_ = ((self).client).Decrypt(d_602_decryptRequest_)
        d_603_maybeDecryptResponse_ = out90_
        d_604_decryptResponse_: ComAmazonawsKmsTypes.DecryptResponse
        d_605_valueOrError2_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.DecryptResponse.default())()
        def lambda61_(d_606_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_ComAmazonawsKms(d_606_e_)

        d_605_valueOrError2_ = (d_603_maybeDecryptResponse_).MapFailure(lambda61_)
        if (d_605_valueOrError2_).IsFailure():
            res = (d_605_valueOrError2_).PropagateFailure()
            return res
        d_604_decryptResponse_ = (d_605_valueOrError2_).Extract()
        d_607_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_607_valueOrError3_ = Wrappers.default__.Need((((((d_604_decryptResponse_).KeyId).is_Some) and ((((d_604_decryptResponse_).KeyId).value) == ((self).awsKmsKey))) and (((d_604_decryptResponse_).Plaintext).is_Some)) and ((AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)) == (len(((d_604_decryptResponse_).Plaintext).value))), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from KMS Decrypt")))
        if (d_607_valueOrError3_).IsFailure():
            res = (d_607_valueOrError3_).PropagateFailure()
            return res
        d_608_output_: MaterialWrapping.UnwrapOutput
        d_608_output_ = MaterialWrapping.UnwrapOutput_UnwrapOutput(((d_604_decryptResponse_).Plaintext).value, KmsUnwrapInfo_KmsUnwrapInfo())
        res = Wrappers.Result_Success(d_608_output_)
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

class KmsGenerateAndWrapKeyMaterial(MaterialWrapping.GenerateAndWrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._client: ComAmazonawsKmsTypes.IKMSClient = None
        self._awsKmsKey: _dafny.Seq = None
        self._grantTokens: _dafny.Seq = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsKeyring.KmsGenerateAndWrapKeyMaterial"
    def ctor__(self, client, awsKmsKey, grantTokens):
        (self)._client = client
        (self)._awsKmsKey = awsKmsKey
        (self)._grantTokens = grantTokens

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.GenerateAndWrapOutput.default(KmsWrapInfo.default()))()
        d_609_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_609_suite_ = (input).algorithmSuite
        d_610_stringifiedEncCtx_: _dafny.Map
        d_611_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        d_611_valueOrError0_ = AwsKmsUtils.default__.StringifyEncryptionContext((input).encryptionContext)
        if (d_611_valueOrError0_).IsFailure():
            res = (d_611_valueOrError0_).PropagateFailure()
            return res
        d_610_stringifiedEncCtx_ = (d_611_valueOrError0_).Extract()
        d_612_generatorRequest_: ComAmazonawsKmsTypes.GenerateDataKeyRequest
        d_612_generatorRequest_ = ComAmazonawsKmsTypes.GenerateDataKeyRequest_GenerateDataKeyRequest((self).awsKmsKey, Wrappers.Option_Some(d_610_stringifiedEncCtx_), Wrappers.Option_Some(AlgorithmSuites.default__.GetEncryptKeyLength(d_609_suite_)), Wrappers.Option_None(), Wrappers.Option_Some((self).grantTokens), Wrappers.Option_None(), Wrappers.Option_None())
        d_613_maybeGenerateResponse_: Wrappers.Result
        out91_: Wrappers.Result
        out91_ = ((self).client).GenerateDataKey(d_612_generatorRequest_)
        d_613_maybeGenerateResponse_ = out91_
        d_614_generateResponse_: ComAmazonawsKmsTypes.GenerateDataKeyResponse
        d_615_valueOrError1_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.GenerateDataKeyResponse.default())()
        def lambda62_(d_616_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_ComAmazonawsKms(d_616_e_)

        d_615_valueOrError1_ = (d_613_maybeGenerateResponse_).MapFailure(lambda62_)
        if (d_615_valueOrError1_).IsFailure():
            res = (d_615_valueOrError1_).PropagateFailure()
            return res
        d_614_generateResponse_ = (d_615_valueOrError1_).Extract()
        d_617_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_617_valueOrError2_ = Wrappers.default__.Need((((d_614_generateResponse_).KeyId).is_Some) and ((AwsArnParsing.default__.ParseAwsKmsIdentifier(((d_614_generateResponse_).KeyId).value)).is_Success), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from KMS GenerateDataKey:: Invalid Key Id")))
        if (d_617_valueOrError2_).IsFailure():
            res = (d_617_valueOrError2_).PropagateFailure()
            return res
        d_618_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_618_valueOrError3_ = Wrappers.default__.Need((((d_614_generateResponse_).Plaintext).is_Some) and ((AlgorithmSuites.default__.GetEncryptKeyLength(d_609_suite_)) == (len(((d_614_generateResponse_).Plaintext).value))), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS GenerateDataKey: Invalid data key")))
        if (d_618_valueOrError3_).IsFailure():
            res = (d_618_valueOrError3_).PropagateFailure()
            return res
        d_619_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_619_valueOrError4_ = Wrappers.default__.Need((((d_614_generateResponse_).CiphertextBlob).is_Some) and (ComAmazonawsKmsTypes.default__.IsValid__CiphertextType(((d_614_generateResponse_).CiphertextBlob).value)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS GeneratedDataKey: Invalid ciphertext")))
        if (d_619_valueOrError4_).IsFailure():
            res = (d_619_valueOrError4_).PropagateFailure()
            return res
        d_620_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_620_valueOrError5_ = Wrappers.default__.Need((True) and (((d_614_generateResponse_).CiphertextForRecipient).is_None), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS GeneratedDataKey: Invalid CiphertextForRecipient")))
        if (d_620_valueOrError5_).IsFailure():
            res = (d_620_valueOrError5_).PropagateFailure()
            return res
        d_621_output_: MaterialWrapping.GenerateAndWrapOutput
        d_621_output_ = MaterialWrapping.GenerateAndWrapOutput_GenerateAndWrapOutput(((d_614_generateResponse_).Plaintext).value, ((d_614_generateResponse_).CiphertextBlob).value, KmsWrapInfo_KmsWrapInfo(((d_614_generateResponse_).KeyId).value))
        res = Wrappers.Result_Success(d_621_output_)
        return res
        return res

    @property
    def client(self):
        return self._client
    @property
    def awsKmsKey(self):
        return self._awsKmsKey
    @property
    def grantTokens(self):
        return self._grantTokens

class KmsWrapKeyMaterial(MaterialWrapping.WrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._client: ComAmazonawsKmsTypes.IKMSClient = None
        self._awsKmsKey: _dafny.Seq = None
        self._grantTokens: _dafny.Seq = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsKeyring.KmsWrapKeyMaterial"
    def ctor__(self, client, awsKmsKey, grantTokens):
        (self)._client = client
        (self)._awsKmsKey = awsKmsKey
        (self)._grantTokens = grantTokens

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.WrapOutput.default(KmsWrapInfo.default()))()
        d_622_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_622_suite_ = (input).algorithmSuite
        d_623_stringifiedEncCtx_: _dafny.Map
        d_624_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        d_624_valueOrError0_ = AwsKmsUtils.default__.StringifyEncryptionContext((input).encryptionContext)
        if (d_624_valueOrError0_).IsFailure():
            res = (d_624_valueOrError0_).PropagateFailure()
            return res
        d_623_stringifiedEncCtx_ = (d_624_valueOrError0_).Extract()
        d_625_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_625_valueOrError1_ = Wrappers.default__.Need(ComAmazonawsKmsTypes.default__.IsValid__PlaintextType((input).plaintextMaterial), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid Plaintext on KMS Encrypt")))
        if (d_625_valueOrError1_).IsFailure():
            res = (d_625_valueOrError1_).PropagateFailure()
            return res
        d_626_encryptRequest_: ComAmazonawsKmsTypes.EncryptRequest
        d_626_encryptRequest_ = ComAmazonawsKmsTypes.EncryptRequest_EncryptRequest((self).awsKmsKey, (input).plaintextMaterial, Wrappers.Option_Some(d_623_stringifiedEncCtx_), Wrappers.Option_Some((self).grantTokens), Wrappers.Option_None(), Wrappers.Option_None())
        d_627_maybeEncryptResponse_: Wrappers.Result
        out92_: Wrappers.Result
        out92_ = ((self).client).Encrypt(d_626_encryptRequest_)
        d_627_maybeEncryptResponse_ = out92_
        d_628_encryptResponse_: ComAmazonawsKmsTypes.EncryptResponse
        d_629_valueOrError2_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.EncryptResponse.default())()
        def lambda63_(d_630_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_ComAmazonawsKms(d_630_e_)

        d_629_valueOrError2_ = (d_627_maybeEncryptResponse_).MapFailure(lambda63_)
        if (d_629_valueOrError2_).IsFailure():
            res = (d_629_valueOrError2_).PropagateFailure()
            return res
        d_628_encryptResponse_ = (d_629_valueOrError2_).Extract()
        d_631_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_631_valueOrError3_ = Wrappers.default__.Need((((d_628_encryptResponse_).KeyId).is_Some) and ((AwsArnParsing.default__.ParseAwsKmsIdentifier(((d_628_encryptResponse_).KeyId).value)).is_Success), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS Encrypt:: Invalid Key Id")))
        if (d_631_valueOrError3_).IsFailure():
            res = (d_631_valueOrError3_).PropagateFailure()
            return res
        d_632_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_632_valueOrError4_ = Wrappers.default__.Need(((d_628_encryptResponse_).CiphertextBlob).is_Some, AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS Encrypt: Invalid Ciphertext Blob")))
        if (d_632_valueOrError4_).IsFailure():
            res = (d_632_valueOrError4_).PropagateFailure()
            return res
        d_633_output_: MaterialWrapping.WrapOutput
        d_633_output_ = MaterialWrapping.WrapOutput_WrapOutput(((d_628_encryptResponse_).CiphertextBlob).value, KmsWrapInfo_KmsWrapInfo(((d_628_encryptResponse_).KeyId).value))
        res = Wrappers.Result_Success(d_633_output_)
        return res
        return res

    @property
    def client(self):
        return self._client
    @property
    def awsKmsKey(self):
        return self._awsKmsKey
    @property
    def grantTokens(self):
        return self._grantTokens
