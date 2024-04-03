import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import BoundedInts
import StandardLibrary_UInt
import StandardLibrary_String
import StandardLibrary
import UTF8
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_primitives_internaldafny_types
import ExternRandom
import Random
import AESEncryption
import ExternDigest
import Digest
import HMAC
import WrappedHMAC
import HKDF
import WrappedHKDF
import Signature
import KdfCtr
import RSAEncryption
import AwsCryptographyPrimitivesOperations
import AesKdfCtr
import Relations
import Seq_MergeSort
import Math
import Seq
import Unicode
import Functions
import Utf8EncodingForm
import Utf16EncodingForm
import UnicodeStrings
import FileIO
import GeneralInternals
import MulInternalsNonlinear
import MulInternals
import Mul
import ModInternalsNonlinear
import DivInternalsNonlinear
import ModInternals
import DivInternals
import DivMod
import Power
import Logarithm
import StandardLibraryInterop
import UUID
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import GetOpt
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import AwsArnParsing
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
import Structure
import KMSKeystoreOperations
import DDBKeystoreOperations
import CreateKeys
import CreateKeyStoreTable
import GetKeys
import AwsCryptographyKeyStoreOperations
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import Com_Amazonaws
import Com
import software_amazon_cryptography_keystore_internaldafny
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsKmsMrkAreUnique
import Constants
import software_amazon_cryptography_primitives_internaldafny
import Aws_Cryptography
import Aws
import MaterialWrapping
import CanonicalEncryptionContext
import IntermediateKeyWrapping
import EdkWrapping

# Module: AwsKmsKeyring


class AwsKmsKeyring(Keyring.VerifiableInterface, software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring):
    def  __init__(self):
        self._client: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient = None
        self._awsKmsKey: _dafny.Seq = None
        self._grantTokens: _dafny.Seq = None
        self._awsKmsArn: AwsArnParsing.AwsKmsIdentifier = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsKeyring.AwsKmsKeyring"
    def OnEncrypt(self, input):
        out81_: Wrappers.Result
        out81_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnEncrypt(self, input)
        return out81_

    def OnDecrypt(self, input):
        out82_: Wrappers.Result
        out82_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnDecrypt(self, input)
        return out82_

    def ctor__(self, client, awsKmsKey, grantTokens):
        d_521_parsedAwsKmsId_: Wrappers.Result
        d_521_parsedAwsKmsId_ = AwsArnParsing.default__.ParseAwsKmsIdentifier(awsKmsKey)
        (self)._client = client
        (self)._awsKmsKey = awsKmsKey
        (self)._awsKmsArn = (d_521_parsedAwsKmsId_).value
        (self)._grantTokens = grantTokens

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        d_522_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_522_materials_ = (input).materials
        d_523_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_523_suite_ = ((input).materials).algorithmSuite
        d_524_stringifiedEncCtx_: _dafny.Map
        d_525_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        d_525_valueOrError0_ = AwsKmsUtils.default__.StringifyEncryptionContext(((input).materials).encryptionContext)
        if (d_525_valueOrError0_).IsFailure():
            res = (d_525_valueOrError0_).PropagateFailure()
            return res
        d_524_stringifiedEncCtx_ = (d_525_valueOrError0_).Extract()
        d_526_kmsGenerateAndWrap_: KmsGenerateAndWrapKeyMaterial
        nw1_ = KmsGenerateAndWrapKeyMaterial()
        nw1_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_526_kmsGenerateAndWrap_ = nw1_
        d_527_kmsWrap_: KmsWrapKeyMaterial
        nw2_ = KmsWrapKeyMaterial()
        nw2_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_527_kmsWrap_ = nw2_
        d_528_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_529_valueOrError1_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.WrapEdkMaterialOutput.default(KmsWrapInfo.default()))()
        out83_: Wrappers.Result
        out83_ = EdkWrapping.default__.WrapEdkMaterial(d_522_materials_, d_527_kmsWrap_, d_526_kmsGenerateAndWrap_)
        d_529_valueOrError1_ = out83_
        if (d_529_valueOrError1_).IsFailure():
            res = (d_529_valueOrError1_).PropagateFailure()
            return res
        d_528_wrapOutput_ = (d_529_valueOrError1_).Extract()
        d_530_kmsKeyArn_: _dafny.Seq
        d_530_kmsKeyArn_ = ((d_528_wrapOutput_).wrapInfo).kmsKeyArn
        d_531_symmetricSigningKeyList_: Wrappers.Option
        d_531_symmetricSigningKeyList_ = (Wrappers.Option_Some(_dafny.Seq([((d_528_wrapOutput_).symmetricSigningKey).value])) if ((d_528_wrapOutput_).symmetricSigningKey).is_Some else Wrappers.Option_None())
        d_532_providerInfo_: _dafny.Seq
        d_533_valueOrError2_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_533_valueOrError2_ = (UTF8.default__.Encode(d_530_kmsKeyArn_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_533_valueOrError2_).IsFailure():
            res = (d_533_valueOrError2_).PropagateFailure()
            return res
        d_532_providerInfo_ = (d_533_valueOrError2_).Extract()
        d_534_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_534_valueOrError3_ = Wrappers.default__.Need((len(d_532_providerInfo_)) < (StandardLibrary_UInt.default__.UINT16__LIMIT), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS GenerateDataKey: Key ID too long.")))
        if (d_534_valueOrError3_).IsFailure():
            res = (d_534_valueOrError3_).PropagateFailure()
            return res
        d_535_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_535_edk_ = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey(Constants.default__.PROVIDER__ID, d_532_providerInfo_, (d_528_wrapOutput_).wrappedMaterial)
        if (d_528_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_536_result_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            d_537_valueOrError4_: Wrappers.Result = None
            d_537_valueOrError4_ = Materials.default__.EncryptionMaterialAddDataKey(d_522_materials_, (d_528_wrapOutput_).plaintextDataKey, _dafny.Seq([d_535_edk_]), d_531_symmetricSigningKeyList_)
            if (d_537_valueOrError4_).IsFailure():
                res = (d_537_valueOrError4_).PropagateFailure()
                return res
            d_536_result_ = (d_537_valueOrError4_).Extract()
            res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_536_result_))
            return res
        elif (d_528_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_538_result_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            d_539_valueOrError5_: Wrappers.Result = None
            d_539_valueOrError5_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys(d_522_materials_, _dafny.Seq([d_535_edk_]), d_531_symmetricSigningKeyList_)
            if (d_539_valueOrError5_).IsFailure():
                res = (d_539_valueOrError5_).PropagateFailure()
                return res
            d_538_result_ = (d_539_valueOrError5_).Extract()
            res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_538_result_))
            return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_540_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_540_materials_ = (input).materials
        d_541_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_541_suite_ = ((input).materials).algorithmSuite
        d_542_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_542_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_540_materials_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_542_valueOrError0_).IsFailure():
            res = (d_542_valueOrError0_).PropagateFailure()
            return res
        d_543_filter_: OnDecryptEncryptedDataKeyFilter
        nw3_ = OnDecryptEncryptedDataKeyFilter()
        nw3_.ctor__((self).awsKmsKey)
        d_543_filter_ = nw3_
        d_544_edksToAttempt_: _dafny.Seq
        d_545_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out84_: Wrappers.Result
        out84_ = Actions.default__.FilterWithResult(d_543_filter_, (input).encryptedDataKeys)
        d_545_valueOrError1_ = out84_
        if (d_545_valueOrError1_).IsFailure():
            res = (d_545_valueOrError1_).PropagateFailure()
            return res
        d_544_edksToAttempt_ = (d_545_valueOrError1_).Extract()
        d_546_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_546_valueOrError2_ = Wrappers.default__.Need((0) < (len(d_544_edksToAttempt_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to decrypt data key: No Encrypted Data Keys found to match.")))
        if (d_546_valueOrError2_).IsFailure():
            res = (d_546_valueOrError2_).PropagateFailure()
            return res
        d_547_decryptClosure_: Actions.ActionWithResult
        nw4_ = DecryptSingleEncryptedDataKey()
        nw4_.ctor__(d_540_materials_, (self).client, (self).awsKmsKey, (self).grantTokens)
        d_547_decryptClosure_ = nw4_
        d_548_outcome_: Wrappers.Result
        out85_: Wrappers.Result
        out85_ = Actions.default__.ReduceToSuccess(d_547_decryptClosure_, d_544_edksToAttempt_)
        d_548_outcome_ = out85_
        d_549_SealedDecryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_550_valueOrError3_: Wrappers.Result = None
        def lambda53_(d_551_errors_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_CollectionOfErrors(d_551_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."))

        d_550_valueOrError3_ = (d_548_outcome_).MapFailure(lambda53_)
        if (d_550_valueOrError3_).IsFailure():
            res = (d_550_valueOrError3_).PropagateFailure()
            return res
        d_549_SealedDecryptionMaterials_ = (d_550_valueOrError3_).Extract()
        res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput_OnDecryptOutput(d_549_SealedDecryptionMaterials_))
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
            res = Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid AWS KMS encoding, provider info is not UTF8.")))
            return res
        d_552_keyId_: _dafny.Seq
        d_553_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_553_valueOrError0_ = (UTF8.default__.Decode((edk).keyProviderInfo)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_553_valueOrError0_).IsFailure():
            res = (d_553_valueOrError0_).PropagateFailure()
            return res
        d_552_keyId_ = (d_553_valueOrError0_).Extract()
        d_554___v0_: AwsArnParsing.AwsArn
        d_555_valueOrError1_: Wrappers.Result = None
        d_555_valueOrError1_ = (AwsArnParsing.default__.ParseAwsKmsArn(d_552_keyId_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_555_valueOrError1_).IsFailure():
            res = (d_555_valueOrError1_).PropagateFailure()
            return res
        d_554___v0_ = (d_555_valueOrError1_).Extract()
        res = Wrappers.Result_Success(((self).awsKmsKey) == (d_552_keyId_))
        return res
        return res

    @property
    def awsKmsKey(self):
        return self._awsKmsKey

class DecryptSingleEncryptedDataKey(Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._materials: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials = None
        self._client: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient = None
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
        d_556_kmsUnwrap_: KmsUnwrapKeyMaterial
        nw5_ = KmsUnwrapKeyMaterial()
        nw5_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_556_kmsUnwrap_ = nw5_
        d_557_unwrapOutputRes_: Wrappers.Result
        out86_: Wrappers.Result
        out86_ = EdkWrapping.default__.UnwrapEdkMaterial((edk).ciphertext, (self).materials, d_556_kmsUnwrap_)
        d_557_unwrapOutputRes_ = out86_
        d_558_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_559_valueOrError0_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.UnwrapEdkMaterialOutput.default(KmsUnwrapInfo.default()))()
        d_559_valueOrError0_ = d_557_unwrapOutputRes_
        if (d_559_valueOrError0_).IsFailure():
            res = (d_559_valueOrError0_).PropagateFailure()
            return res
        d_558_unwrapOutput_ = (d_559_valueOrError0_).Extract()
        d_560_result_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_561_valueOrError1_: Wrappers.Result = None
        d_561_valueOrError1_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_558_unwrapOutput_).plaintextDataKey, (d_558_unwrapOutput_).symmetricSigningKey)
        if (d_561_valueOrError1_).IsFailure():
            res = (d_561_valueOrError1_).PropagateFailure()
            return res
        d_560_result_ = (d_561_valueOrError1_).Extract()
        res = Wrappers.Result_Success(d_560_result_)
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
        self._client: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient = None
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
        d_562_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_562_valueOrError0_ = Wrappers.default__.Need(software_amazon_cryptography_services_kms_internaldafny_types.default__.IsValid__CiphertextType((input).wrappedMaterial), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Ciphertext length invalid")))
        if (d_562_valueOrError0_).IsFailure():
            res = (d_562_valueOrError0_).PropagateFailure()
            return res
        d_563_stringifiedEncCtx_: _dafny.Map
        d_564_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        d_564_valueOrError1_ = AwsKmsUtils.default__.StringifyEncryptionContext((input).encryptionContext)
        if (d_564_valueOrError1_).IsFailure():
            res = (d_564_valueOrError1_).PropagateFailure()
            return res
        d_563_stringifiedEncCtx_ = (d_564_valueOrError1_).Extract()
        d_565_decryptRequest_: software_amazon_cryptography_services_kms_internaldafny_types.DecryptRequest
        d_565_decryptRequest_ = software_amazon_cryptography_services_kms_internaldafny_types.DecryptRequest_DecryptRequest((input).wrappedMaterial, Wrappers.Option_Some(d_563_stringifiedEncCtx_), Wrappers.Option_Some((self).grantTokens), Wrappers.Option_Some((self).awsKmsKey), Wrappers.Option_None())
        d_566_maybeDecryptResponse_: Wrappers.Result
        out87_: Wrappers.Result
        out87_ = ((self).client).Decrypt(d_565_decryptRequest_)
        d_566_maybeDecryptResponse_ = out87_
        d_567_decryptResponse_: software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse
        d_568_valueOrError2_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse.default())()
        def lambda54_(d_569_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_ComAmazonawsKms(d_569_e_)

        d_568_valueOrError2_ = (d_566_maybeDecryptResponse_).MapFailure(lambda54_)
        if (d_568_valueOrError2_).IsFailure():
            res = (d_568_valueOrError2_).PropagateFailure()
            return res
        d_567_decryptResponse_ = (d_568_valueOrError2_).Extract()
        d_570_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_570_valueOrError3_ = Wrappers.default__.Need((((((d_567_decryptResponse_).KeyId).is_Some) and ((((d_567_decryptResponse_).KeyId).value) == ((self).awsKmsKey))) and (((d_567_decryptResponse_).Plaintext).is_Some)) and ((AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)) == (len(((d_567_decryptResponse_).Plaintext).value))), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from KMS Decrypt")))
        if (d_570_valueOrError3_).IsFailure():
            res = (d_570_valueOrError3_).PropagateFailure()
            return res
        d_571_output_: MaterialWrapping.UnwrapOutput
        d_571_output_ = MaterialWrapping.UnwrapOutput_UnwrapOutput(((d_567_decryptResponse_).Plaintext).value, KmsUnwrapInfo_KmsUnwrapInfo())
        res = Wrappers.Result_Success(d_571_output_)
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
        self._client: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient = None
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
        d_572_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_572_suite_ = (input).algorithmSuite
        d_573_stringifiedEncCtx_: _dafny.Map
        d_574_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        d_574_valueOrError0_ = AwsKmsUtils.default__.StringifyEncryptionContext((input).encryptionContext)
        if (d_574_valueOrError0_).IsFailure():
            res = (d_574_valueOrError0_).PropagateFailure()
            return res
        d_573_stringifiedEncCtx_ = (d_574_valueOrError0_).Extract()
        d_575_generatorRequest_: software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyRequest
        d_575_generatorRequest_ = software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyRequest_GenerateDataKeyRequest((self).awsKmsKey, Wrappers.Option_Some(d_573_stringifiedEncCtx_), Wrappers.Option_Some(AlgorithmSuites.default__.GetEncryptKeyLength(d_572_suite_)), Wrappers.Option_None(), Wrappers.Option_Some((self).grantTokens))
        d_576_maybeGenerateResponse_: Wrappers.Result
        out88_: Wrappers.Result
        out88_ = ((self).client).GenerateDataKey(d_575_generatorRequest_)
        d_576_maybeGenerateResponse_ = out88_
        d_577_generateResponse_: software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyResponse
        d_578_valueOrError1_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyResponse.default())()
        def lambda55_(d_579_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_ComAmazonawsKms(d_579_e_)

        d_578_valueOrError1_ = (d_576_maybeGenerateResponse_).MapFailure(lambda55_)
        if (d_578_valueOrError1_).IsFailure():
            res = (d_578_valueOrError1_).PropagateFailure()
            return res
        d_577_generateResponse_ = (d_578_valueOrError1_).Extract()
        d_580_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_580_valueOrError2_ = Wrappers.default__.Need((((d_577_generateResponse_).KeyId).is_Some) and ((AwsArnParsing.default__.ParseAwsKmsIdentifier(((d_577_generateResponse_).KeyId).value)).is_Success), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from KMS GenerateDataKey:: Invalid Key Id")))
        if (d_580_valueOrError2_).IsFailure():
            res = (d_580_valueOrError2_).PropagateFailure()
            return res
        d_581_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_581_valueOrError3_ = Wrappers.default__.Need((((d_577_generateResponse_).Plaintext).is_Some) and ((AlgorithmSuites.default__.GetEncryptKeyLength(d_572_suite_)) == (len(((d_577_generateResponse_).Plaintext).value))), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS GenerateDataKey: Invalid data key")))
        if (d_581_valueOrError3_).IsFailure():
            res = (d_581_valueOrError3_).PropagateFailure()
            return res
        d_582_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_582_valueOrError4_ = Wrappers.default__.Need((((d_577_generateResponse_).CiphertextBlob).is_Some) and (software_amazon_cryptography_services_kms_internaldafny_types.default__.IsValid__CiphertextType(((d_577_generateResponse_).CiphertextBlob).value)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS GeneratedDataKey: Invalid ciphertext")))
        if (d_582_valueOrError4_).IsFailure():
            res = (d_582_valueOrError4_).PropagateFailure()
            return res
        d_583_output_: MaterialWrapping.GenerateAndWrapOutput
        d_583_output_ = MaterialWrapping.GenerateAndWrapOutput_GenerateAndWrapOutput(((d_577_generateResponse_).Plaintext).value, ((d_577_generateResponse_).CiphertextBlob).value, KmsWrapInfo_KmsWrapInfo(((d_577_generateResponse_).KeyId).value))
        res = Wrappers.Result_Success(d_583_output_)
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
        self._client: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient = None
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
        d_584_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_584_suite_ = (input).algorithmSuite
        d_585_stringifiedEncCtx_: _dafny.Map
        d_586_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        d_586_valueOrError0_ = AwsKmsUtils.default__.StringifyEncryptionContext((input).encryptionContext)
        if (d_586_valueOrError0_).IsFailure():
            res = (d_586_valueOrError0_).PropagateFailure()
            return res
        d_585_stringifiedEncCtx_ = (d_586_valueOrError0_).Extract()
        d_587_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_587_valueOrError1_ = Wrappers.default__.Need(software_amazon_cryptography_services_kms_internaldafny_types.default__.IsValid__PlaintextType((input).plaintextMaterial), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid Plaintext on KMS Encrypt")))
        if (d_587_valueOrError1_).IsFailure():
            res = (d_587_valueOrError1_).PropagateFailure()
            return res
        d_588_encryptRequest_: software_amazon_cryptography_services_kms_internaldafny_types.EncryptRequest
        d_588_encryptRequest_ = software_amazon_cryptography_services_kms_internaldafny_types.EncryptRequest_EncryptRequest((self).awsKmsKey, (input).plaintextMaterial, Wrappers.Option_Some(d_585_stringifiedEncCtx_), Wrappers.Option_Some((self).grantTokens), Wrappers.Option_None())
        d_589_maybeEncryptResponse_: Wrappers.Result
        out89_: Wrappers.Result
        out89_ = ((self).client).Encrypt(d_588_encryptRequest_)
        d_589_maybeEncryptResponse_ = out89_
        d_590_encryptResponse_: software_amazon_cryptography_services_kms_internaldafny_types.EncryptResponse
        d_591_valueOrError2_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_services_kms_internaldafny_types.EncryptResponse.default())()
        def lambda56_(d_592_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_ComAmazonawsKms(d_592_e_)

        d_591_valueOrError2_ = (d_589_maybeEncryptResponse_).MapFailure(lambda56_)
        if (d_591_valueOrError2_).IsFailure():
            res = (d_591_valueOrError2_).PropagateFailure()
            return res
        d_590_encryptResponse_ = (d_591_valueOrError2_).Extract()
        d_593_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_593_valueOrError3_ = Wrappers.default__.Need((((d_590_encryptResponse_).KeyId).is_Some) and ((AwsArnParsing.default__.ParseAwsKmsIdentifier(((d_590_encryptResponse_).KeyId).value)).is_Success), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS Encrypt:: Invalid Key Id")))
        if (d_593_valueOrError3_).IsFailure():
            res = (d_593_valueOrError3_).PropagateFailure()
            return res
        d_594_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_594_valueOrError4_ = Wrappers.default__.Need(((d_590_encryptResponse_).CiphertextBlob).is_Some, software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS Encrypt: Invalid Ciphertext Blob")))
        if (d_594_valueOrError4_).IsFailure():
            res = (d_594_valueOrError4_).PropagateFailure()
            return res
        d_595_output_: MaterialWrapping.WrapOutput
        d_595_output_ = MaterialWrapping.WrapOutput_WrapOutput(((d_590_encryptResponse_).CiphertextBlob).value, KmsWrapInfo_KmsWrapInfo(((d_590_encryptResponse_).KeyId).value))
        res = Wrappers.Result_Success(d_595_output_)
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
