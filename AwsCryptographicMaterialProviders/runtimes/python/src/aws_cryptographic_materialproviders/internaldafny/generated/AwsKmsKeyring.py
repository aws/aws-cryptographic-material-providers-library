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
        out83_: Wrappers.Result
        out83_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnDecrypt(self, input)
        return out83_

    def OnEncrypt(self, input):
        out84_: Wrappers.Result
        out84_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnEncrypt(self, input)
        return out84_

    def ctor__(self, client, awsKmsKey, grantTokens):
        d_551_parsedAwsKmsId_: Wrappers.Result
        d_551_parsedAwsKmsId_ = AwsArnParsing.default__.ParseAwsKmsIdentifier(awsKmsKey)
        (self)._client = client
        (self)._awsKmsKey = awsKmsKey
        (self)._awsKmsArn = (d_551_parsedAwsKmsId_).value
        (self)._grantTokens = grantTokens

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        d_552_materials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_552_materials_ = (input).materials
        d_553_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_553_suite_ = ((input).materials).algorithmSuite
        d_554_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        d_554_valueOrError0_ = AwsKmsUtils.default__.StringifyEncryptionContext(((input).materials).encryptionContext)
        if (d_554_valueOrError0_).IsFailure():
            res = (d_554_valueOrError0_).PropagateFailure()
            return res
        d_555_stringifiedEncCtx_: _dafny.Map
        d_555_stringifiedEncCtx_ = (d_554_valueOrError0_).Extract()
        d_556_kmsGenerateAndWrap_: KmsGenerateAndWrapKeyMaterial
        nw1_ = KmsGenerateAndWrapKeyMaterial()
        nw1_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_556_kmsGenerateAndWrap_ = nw1_
        d_557_kmsWrap_: KmsWrapKeyMaterial
        nw2_ = KmsWrapKeyMaterial()
        nw2_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_557_kmsWrap_ = nw2_
        d_558_valueOrError1_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.WrapEdkMaterialOutput.default(KmsWrapInfo.default()))()
        out85_: Wrappers.Result
        out85_ = EdkWrapping.default__.WrapEdkMaterial(d_552_materials_, d_557_kmsWrap_, d_556_kmsGenerateAndWrap_)
        d_558_valueOrError1_ = out85_
        if (d_558_valueOrError1_).IsFailure():
            res = (d_558_valueOrError1_).PropagateFailure()
            return res
        d_559_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_559_wrapOutput_ = (d_558_valueOrError1_).Extract()
        d_560_kmsKeyArn_: _dafny.Seq
        d_560_kmsKeyArn_ = ((d_559_wrapOutput_).wrapInfo).kmsKeyArn
        d_561_symmetricSigningKeyList_: Wrappers.Option
        if ((d_559_wrapOutput_).symmetricSigningKey).is_Some:
            d_561_symmetricSigningKeyList_ = Wrappers.Option_Some(_dafny.Seq([((d_559_wrapOutput_).symmetricSigningKey).value]))
        elif True:
            d_561_symmetricSigningKeyList_ = Wrappers.Option_None()
        d_562_valueOrError2_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_562_valueOrError2_ = (UTF8.default__.Encode(d_560_kmsKeyArn_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_562_valueOrError2_).IsFailure():
            res = (d_562_valueOrError2_).PropagateFailure()
            return res
        d_563_providerInfo_: _dafny.Seq
        d_563_providerInfo_ = (d_562_valueOrError2_).Extract()
        d_564_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_564_valueOrError3_ = Wrappers.default__.Need((len(d_563_providerInfo_)) < (StandardLibrary_UInt.default__.UINT16__LIMIT), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS GenerateDataKey: Key ID too long.")))
        if (d_564_valueOrError3_).IsFailure():
            res = (d_564_valueOrError3_).PropagateFailure()
            return res
        d_565_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_565_edk_ = AwsCryptographyMaterialProvidersTypes.EncryptedDataKey_EncryptedDataKey(Constants.default__.PROVIDER__ID, d_563_providerInfo_, (d_559_wrapOutput_).wrappedMaterial)
        if (d_559_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_566_valueOrError4_: Wrappers.Result = None
            d_566_valueOrError4_ = Materials.default__.EncryptionMaterialAddDataKey(d_552_materials_, (d_559_wrapOutput_).plaintextDataKey, _dafny.Seq([d_565_edk_]), d_561_symmetricSigningKeyList_)
            if (d_566_valueOrError4_).IsFailure():
                res = (d_566_valueOrError4_).PropagateFailure()
                return res
            d_567_result_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_567_result_ = (d_566_valueOrError4_).Extract()
            res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(d_567_result_))
            return res
        elif (d_559_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_568_valueOrError5_: Wrappers.Result = None
            d_568_valueOrError5_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys(d_552_materials_, _dafny.Seq([d_565_edk_]), d_561_symmetricSigningKeyList_)
            if (d_568_valueOrError5_).IsFailure():
                res = (d_568_valueOrError5_).PropagateFailure()
                return res
            d_569_result_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_569_result_ = (d_568_valueOrError5_).Extract()
            res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(d_569_result_))
            return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_570_materials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_570_materials_ = (input).materials
        d_571_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_571_suite_ = ((input).materials).algorithmSuite
        d_572_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_572_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_570_materials_), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_572_valueOrError0_).IsFailure():
            res = (d_572_valueOrError0_).PropagateFailure()
            return res
        d_573_filter_: OnDecryptEncryptedDataKeyFilter
        nw3_ = OnDecryptEncryptedDataKeyFilter()
        nw3_.ctor__((self).awsKmsKey)
        d_573_filter_ = nw3_
        d_574_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out86_: Wrappers.Result
        out86_ = Actions.default__.FilterWithResult(d_573_filter_, (input).encryptedDataKeys)
        d_574_valueOrError1_ = out86_
        if (d_574_valueOrError1_).IsFailure():
            res = (d_574_valueOrError1_).PropagateFailure()
            return res
        d_575_edksToAttempt_: _dafny.Seq
        d_575_edksToAttempt_ = (d_574_valueOrError1_).Extract()
        if (0) == (len(d_575_edksToAttempt_)):
            d_576_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            d_576_valueOrError2_ = ErrorMessages.default__.IncorrectDataKeys((input).encryptedDataKeys, ((input).materials).algorithmSuite, _dafny.Seq(""))
            if (d_576_valueOrError2_).IsFailure():
                res = (d_576_valueOrError2_).PropagateFailure()
                return res
            d_577_errorMessage_: _dafny.Seq
            d_577_errorMessage_ = (d_576_valueOrError2_).Extract()
            res = Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_577_errorMessage_))
            return res
        d_578_decryptClosure_: Actions.ActionWithResult
        nw4_ = DecryptSingleEncryptedDataKey()
        nw4_.ctor__(d_570_materials_, (self).client, (self).awsKmsKey, (self).grantTokens)
        d_578_decryptClosure_ = nw4_
        d_579_outcome_: Wrappers.Result
        out87_: Wrappers.Result
        out87_ = Actions.default__.ReduceToSuccess(d_578_decryptClosure_, d_575_edksToAttempt_)
        d_579_outcome_ = out87_
        d_580_valueOrError3_: Wrappers.Result = None
        def lambda59_(d_581_errors_):
            return AwsCryptographyMaterialProvidersTypes.Error_CollectionOfErrors(d_581_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."))

        d_580_valueOrError3_ = (d_579_outcome_).MapFailure(lambda59_)
        if (d_580_valueOrError3_).IsFailure():
            res = (d_580_valueOrError3_).PropagateFailure()
            return res
        d_582_SealedDecryptionMaterials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_582_SealedDecryptionMaterials_ = (d_580_valueOrError3_).Extract()
        res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnDecryptOutput_OnDecryptOutput(d_582_SealedDecryptionMaterials_))
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
        d_583_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_583_valueOrError0_ = (UTF8.default__.Decode((edk).keyProviderInfo)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_583_valueOrError0_).IsFailure():
            res = (d_583_valueOrError0_).PropagateFailure()
            return res
        d_584_keyId_: _dafny.Seq
        d_584_keyId_ = (d_583_valueOrError0_).Extract()
        d_585_valueOrError1_: Wrappers.Result = None
        d_585_valueOrError1_ = (AwsArnParsing.default__.ParseAwsKmsArn(d_584_keyId_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_585_valueOrError1_).IsFailure():
            res = (d_585_valueOrError1_).PropagateFailure()
            return res
        d_586___v0_: AwsArnParsing.AwsArn
        d_586___v0_ = (d_585_valueOrError1_).Extract()
        res = Wrappers.Result_Success(((self).awsKmsKey) == (d_584_keyId_))
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
        d_587_kmsUnwrap_: KmsUnwrapKeyMaterial
        nw5_ = KmsUnwrapKeyMaterial()
        nw5_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_587_kmsUnwrap_ = nw5_
        d_588_unwrapOutputRes_: Wrappers.Result
        out88_: Wrappers.Result
        out88_ = EdkWrapping.default__.UnwrapEdkMaterial((edk).ciphertext, (self).materials, d_587_kmsUnwrap_)
        d_588_unwrapOutputRes_ = out88_
        d_589_valueOrError0_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.UnwrapEdkMaterialOutput.default(KmsUnwrapInfo.default()))()
        d_589_valueOrError0_ = d_588_unwrapOutputRes_
        if (d_589_valueOrError0_).IsFailure():
            res = (d_589_valueOrError0_).PropagateFailure()
            return res
        d_590_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_590_unwrapOutput_ = (d_589_valueOrError0_).Extract()
        d_591_valueOrError1_: Wrappers.Result = None
        d_591_valueOrError1_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_590_unwrapOutput_).plaintextDataKey, (d_590_unwrapOutput_).symmetricSigningKey)
        if (d_591_valueOrError1_).IsFailure():
            res = (d_591_valueOrError1_).PropagateFailure()
            return res
        d_592_result_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_592_result_ = (d_591_valueOrError1_).Extract()
        res = Wrappers.Result_Success(d_592_result_)
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
        d_593_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_593_valueOrError0_ = Wrappers.default__.Need(ComAmazonawsKmsTypes.default__.IsValid__CiphertextType((input).wrappedMaterial), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Ciphertext length invalid")))
        if (d_593_valueOrError0_).IsFailure():
            res = (d_593_valueOrError0_).PropagateFailure()
            return res
        d_594_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        d_594_valueOrError1_ = AwsKmsUtils.default__.StringifyEncryptionContext((input).encryptionContext)
        if (d_594_valueOrError1_).IsFailure():
            res = (d_594_valueOrError1_).PropagateFailure()
            return res
        d_595_stringifiedEncCtx_: _dafny.Map
        d_595_stringifiedEncCtx_ = (d_594_valueOrError1_).Extract()
        d_596_decryptRequest_: ComAmazonawsKmsTypes.DecryptRequest
        d_596_decryptRequest_ = ComAmazonawsKmsTypes.DecryptRequest_DecryptRequest((input).wrappedMaterial, Wrappers.Option_Some(d_595_stringifiedEncCtx_), Wrappers.Option_Some((self).grantTokens), Wrappers.Option_Some((self).awsKmsKey), Wrappers.Option_None())
        d_597_maybeDecryptResponse_: Wrappers.Result
        out89_: Wrappers.Result
        out89_ = ((self).client).Decrypt(d_596_decryptRequest_)
        d_597_maybeDecryptResponse_ = out89_
        d_598_valueOrError2_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.DecryptResponse.default())()
        def lambda60_(d_599_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_ComAmazonawsKms(d_599_e_)

        d_598_valueOrError2_ = (d_597_maybeDecryptResponse_).MapFailure(lambda60_)
        if (d_598_valueOrError2_).IsFailure():
            res = (d_598_valueOrError2_).PropagateFailure()
            return res
        d_600_decryptResponse_: ComAmazonawsKmsTypes.DecryptResponse
        d_600_decryptResponse_ = (d_598_valueOrError2_).Extract()
        d_601_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_601_valueOrError3_ = Wrappers.default__.Need((((((d_600_decryptResponse_).KeyId).is_Some) and ((((d_600_decryptResponse_).KeyId).value) == ((self).awsKmsKey))) and (((d_600_decryptResponse_).Plaintext).is_Some)) and ((AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)) == (len(((d_600_decryptResponse_).Plaintext).value))), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from KMS Decrypt")))
        if (d_601_valueOrError3_).IsFailure():
            res = (d_601_valueOrError3_).PropagateFailure()
            return res
        d_602_output_: MaterialWrapping.UnwrapOutput
        d_602_output_ = MaterialWrapping.UnwrapOutput_UnwrapOutput(((d_600_decryptResponse_).Plaintext).value, KmsUnwrapInfo_KmsUnwrapInfo())
        res = Wrappers.Result_Success(d_602_output_)
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
        d_603_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_603_suite_ = (input).algorithmSuite
        d_604_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        d_604_valueOrError0_ = AwsKmsUtils.default__.StringifyEncryptionContext((input).encryptionContext)
        if (d_604_valueOrError0_).IsFailure():
            res = (d_604_valueOrError0_).PropagateFailure()
            return res
        d_605_stringifiedEncCtx_: _dafny.Map
        d_605_stringifiedEncCtx_ = (d_604_valueOrError0_).Extract()
        d_606_generatorRequest_: ComAmazonawsKmsTypes.GenerateDataKeyRequest
        d_606_generatorRequest_ = ComAmazonawsKmsTypes.GenerateDataKeyRequest_GenerateDataKeyRequest((self).awsKmsKey, Wrappers.Option_Some(d_605_stringifiedEncCtx_), Wrappers.Option_Some(AlgorithmSuites.default__.GetEncryptKeyLength(d_603_suite_)), Wrappers.Option_None(), Wrappers.Option_Some((self).grantTokens))
        d_607_maybeGenerateResponse_: Wrappers.Result
        out90_: Wrappers.Result
        out90_ = ((self).client).GenerateDataKey(d_606_generatorRequest_)
        d_607_maybeGenerateResponse_ = out90_
        d_608_valueOrError1_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.GenerateDataKeyResponse.default())()
        def lambda61_(d_609_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_ComAmazonawsKms(d_609_e_)

        d_608_valueOrError1_ = (d_607_maybeGenerateResponse_).MapFailure(lambda61_)
        if (d_608_valueOrError1_).IsFailure():
            res = (d_608_valueOrError1_).PropagateFailure()
            return res
        d_610_generateResponse_: ComAmazonawsKmsTypes.GenerateDataKeyResponse
        d_610_generateResponse_ = (d_608_valueOrError1_).Extract()
        d_611_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_611_valueOrError2_ = Wrappers.default__.Need((((d_610_generateResponse_).KeyId).is_Some) and ((AwsArnParsing.default__.ParseAwsKmsIdentifier(((d_610_generateResponse_).KeyId).value)).is_Success), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from KMS GenerateDataKey:: Invalid Key Id")))
        if (d_611_valueOrError2_).IsFailure():
            res = (d_611_valueOrError2_).PropagateFailure()
            return res
        d_612_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_612_valueOrError3_ = Wrappers.default__.Need((((d_610_generateResponse_).Plaintext).is_Some) and ((AlgorithmSuites.default__.GetEncryptKeyLength(d_603_suite_)) == (len(((d_610_generateResponse_).Plaintext).value))), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS GenerateDataKey: Invalid data key")))
        if (d_612_valueOrError3_).IsFailure():
            res = (d_612_valueOrError3_).PropagateFailure()
            return res
        d_613_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_613_valueOrError4_ = Wrappers.default__.Need((((d_610_generateResponse_).CiphertextBlob).is_Some) and (ComAmazonawsKmsTypes.default__.IsValid__CiphertextType(((d_610_generateResponse_).CiphertextBlob).value)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS GeneratedDataKey: Invalid ciphertext")))
        if (d_613_valueOrError4_).IsFailure():
            res = (d_613_valueOrError4_).PropagateFailure()
            return res
        d_614_output_: MaterialWrapping.GenerateAndWrapOutput
        d_614_output_ = MaterialWrapping.GenerateAndWrapOutput_GenerateAndWrapOutput(((d_610_generateResponse_).Plaintext).value, ((d_610_generateResponse_).CiphertextBlob).value, KmsWrapInfo_KmsWrapInfo(((d_610_generateResponse_).KeyId).value))
        res = Wrappers.Result_Success(d_614_output_)
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
        d_615_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_615_suite_ = (input).algorithmSuite
        d_616_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        d_616_valueOrError0_ = AwsKmsUtils.default__.StringifyEncryptionContext((input).encryptionContext)
        if (d_616_valueOrError0_).IsFailure():
            res = (d_616_valueOrError0_).PropagateFailure()
            return res
        d_617_stringifiedEncCtx_: _dafny.Map
        d_617_stringifiedEncCtx_ = (d_616_valueOrError0_).Extract()
        d_618_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_618_valueOrError1_ = Wrappers.default__.Need(ComAmazonawsKmsTypes.default__.IsValid__PlaintextType((input).plaintextMaterial), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid Plaintext on KMS Encrypt")))
        if (d_618_valueOrError1_).IsFailure():
            res = (d_618_valueOrError1_).PropagateFailure()
            return res
        d_619_encryptRequest_: ComAmazonawsKmsTypes.EncryptRequest
        d_619_encryptRequest_ = ComAmazonawsKmsTypes.EncryptRequest_EncryptRequest((self).awsKmsKey, (input).plaintextMaterial, Wrappers.Option_Some(d_617_stringifiedEncCtx_), Wrappers.Option_Some((self).grantTokens), Wrappers.Option_None())
        d_620_maybeEncryptResponse_: Wrappers.Result
        out91_: Wrappers.Result
        out91_ = ((self).client).Encrypt(d_619_encryptRequest_)
        d_620_maybeEncryptResponse_ = out91_
        d_621_valueOrError2_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsKmsTypes.EncryptResponse.default())()
        def lambda62_(d_622_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_ComAmazonawsKms(d_622_e_)

        d_621_valueOrError2_ = (d_620_maybeEncryptResponse_).MapFailure(lambda62_)
        if (d_621_valueOrError2_).IsFailure():
            res = (d_621_valueOrError2_).PropagateFailure()
            return res
        d_623_encryptResponse_: ComAmazonawsKmsTypes.EncryptResponse
        d_623_encryptResponse_ = (d_621_valueOrError2_).Extract()
        d_624_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_624_valueOrError3_ = Wrappers.default__.Need((((d_623_encryptResponse_).KeyId).is_Some) and ((AwsArnParsing.default__.ParseAwsKmsIdentifier(((d_623_encryptResponse_).KeyId).value)).is_Success), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS Encrypt:: Invalid Key Id")))
        if (d_624_valueOrError3_).IsFailure():
            res = (d_624_valueOrError3_).PropagateFailure()
            return res
        d_625_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_625_valueOrError4_ = Wrappers.default__.Need(((d_623_encryptResponse_).CiphertextBlob).is_Some, AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS Encrypt: Invalid Ciphertext Blob")))
        if (d_625_valueOrError4_).IsFailure():
            res = (d_625_valueOrError4_).PropagateFailure()
            return res
        d_626_output_: MaterialWrapping.WrapOutput
        d_626_output_ = MaterialWrapping.WrapOutput_WrapOutput(((d_623_encryptResponse_).CiphertextBlob).value, KmsWrapInfo_KmsWrapInfo(((d_623_encryptResponse_).KeyId).value))
        res = Wrappers.Result_Success(d_626_output_)
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
