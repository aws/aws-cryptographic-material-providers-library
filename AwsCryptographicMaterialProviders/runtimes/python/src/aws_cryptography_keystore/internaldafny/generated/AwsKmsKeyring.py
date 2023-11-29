import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_mMergeSort
import Math
import Seq
import BoundedInts
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
import StandardLibrary_mUInt
import String
import StandardLibrary
import UUID
import UTF8
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import software_amazon_cryptography_primitives_internaldafny_types
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
import software_amazon_cryptography_keystore_internaldafny
import Fixtures
import TestCreateKeyStore
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
import TestConfig
import TestGetKeys
import CleanupItems
import TestCreateKeys
import TestVersionKey
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsKmsMrkAreUnique
import Constants
import software_amazon_cryptography_primitives_internaldafny
import Aws_mCryptography
import Aws
import MaterialWrapping
import CanonicalEncryptionContext
import IntermediateKeyWrapping
import EdkWrapping

# assert "AwsKmsKeyring" == __name__


class AwsKmsKeyring(Keyring.VerifiableInterface, software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring):
    def  __init__(self):
        self._client: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient = None
        self._awsKmsKey: _dafny.Seq = None
        self._grantTokens: _dafny.Seq = None
        self._awsKmsArn: AwsArnParsing.AwsKmsIdentifier = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsKeyring"
    def OnEncrypt(self, input):
        out209_: Wrappers.Result
        out209_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnEncrypt(self, input)
        return out209_

    def OnDecrypt(self, input):
        out210_: Wrappers.Result
        out210_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnDecrypt(self, input)
        return out210_

    def ctor__(self, client, awsKmsKey, grantTokens):
        d_804_parsedAwsKmsId_: Wrappers.Result
        d_804_parsedAwsKmsId_ = AwsArnParsing.default__.ParseAwsKmsIdentifier(awsKmsKey)
        (self)._client = client
        (self)._awsKmsKey = awsKmsKey
        (self)._awsKmsArn = (d_804_parsedAwsKmsId_).value
        (self)._grantTokens = grantTokens

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        d_805_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_805_materials_ = (input).materials
        d_806_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_806_suite_ = ((input).materials).algorithmSuite
        d_807_stringifiedEncCtx_: _dafny.Map
        d_808_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Map)()
        d_808_valueOrError0_ = AwsKmsUtils.default__.StringifyEncryptionContext(((input).materials).encryptionContext)
        if (d_808_valueOrError0_).IsFailure():
            res = (d_808_valueOrError0_).PropagateFailure()
            return res
        d_807_stringifiedEncCtx_ = (d_808_valueOrError0_).Extract()
        d_809_kmsGenerateAndWrap_: KmsGenerateAndWrapKeyMaterial
        nw2_ = KmsGenerateAndWrapKeyMaterial()
        nw2_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_809_kmsGenerateAndWrap_ = nw2_
        d_810_kmsWrap_: KmsWrapKeyMaterial
        nw3_ = KmsWrapKeyMaterial()
        nw3_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_810_kmsWrap_ = nw3_
        d_811_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_812_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(EdkWrapping.WrapEdkMaterialOutput.default(KmsWrapInfo.default()))()
        out211_: Wrappers.Result
        out211_ = EdkWrapping.default__.WrapEdkMaterial(d_805_materials_, d_810_kmsWrap_, d_809_kmsGenerateAndWrap_)
        d_812_valueOrError1_ = out211_
        if (d_812_valueOrError1_).IsFailure():
            res = (d_812_valueOrError1_).PropagateFailure()
            return res
        d_811_wrapOutput_ = (d_812_valueOrError1_).Extract()
        d_813_kmsKeyArn_: _dafny.Seq
        d_813_kmsKeyArn_ = ((d_811_wrapOutput_).wrapInfo).kmsKeyArn
        d_814_symmetricSigningKeyList_: Wrappers.Option
        d_814_symmetricSigningKeyList_ = (Wrappers.Option_Some(_dafny.Seq([((d_811_wrapOutput_).symmetricSigningKey).value])) if ((d_811_wrapOutput_).symmetricSigningKey).is_Some else Wrappers.Option_None())
        d_815_providerInfo_: _dafny.Seq
        d_816_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_816_valueOrError2_ = (UTF8.default__.Encode(d_813_kmsKeyArn_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_816_valueOrError2_).IsFailure():
            res = (d_816_valueOrError2_).PropagateFailure()
            return res
        d_815_providerInfo_ = (d_816_valueOrError2_).Extract()
        d_817_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_817_valueOrError3_ = Wrappers.default__.Need((len(d_815_providerInfo_)) < ((StandardLibrary_mUInt.default__).UINT16__LIMIT), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS GenerateDataKey: Key ID too long.")))
        if (d_817_valueOrError3_).IsFailure():
            res = (d_817_valueOrError3_).PropagateFailure()
            return res
        d_818_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_818_edk_ = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey((Constants.default__).PROVIDER__ID, d_815_providerInfo_, (d_811_wrapOutput_).wrappedMaterial)
        if (d_811_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_819_result_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            d_820_valueOrError4_: Wrappers.Result = None
            d_820_valueOrError4_ = Materials.default__.EncryptionMaterialAddDataKey(d_805_materials_, (d_811_wrapOutput_).plaintextDataKey, _dafny.Seq([d_818_edk_]), d_814_symmetricSigningKeyList_)
            if (d_820_valueOrError4_).IsFailure():
                res = (d_820_valueOrError4_).PropagateFailure()
                return res
            d_819_result_ = (d_820_valueOrError4_).Extract()
            res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_819_result_))
            return res
        elif (d_811_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_821_result_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            d_822_valueOrError5_: Wrappers.Result = None
            d_822_valueOrError5_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys(d_805_materials_, _dafny.Seq([d_818_edk_]), d_814_symmetricSigningKeyList_)
            if (d_822_valueOrError5_).IsFailure():
                res = (d_822_valueOrError5_).PropagateFailure()
                return res
            d_821_result_ = (d_822_valueOrError5_).Extract()
            res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_821_result_))
            return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_823_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_823_materials_ = (input).materials
        d_824_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_824_suite_ = ((input).materials).algorithmSuite
        d_825_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_825_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_823_materials_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_825_valueOrError0_).IsFailure():
            res = (d_825_valueOrError0_).PropagateFailure()
            return res
        d_826_filter_: OnDecryptEncryptedDataKeyFilter
        nw4_ = OnDecryptEncryptedDataKeyFilter()
        nw4_.ctor__((self).awsKmsKey)
        d_826_filter_ = nw4_
        d_827_edksToAttempt_: _dafny.Seq
        d_828_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out212_: Wrappers.Result
        out212_ = Actions.default__.FilterWithResult(d_826_filter_, (input).encryptedDataKeys)
        d_828_valueOrError1_ = out212_
        if (d_828_valueOrError1_).IsFailure():
            res = (d_828_valueOrError1_).PropagateFailure()
            return res
        d_827_edksToAttempt_ = (d_828_valueOrError1_).Extract()
        d_829_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_829_valueOrError2_ = Wrappers.default__.Need((0) < (len(d_827_edksToAttempt_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to decrypt data key: No Encrypted Data Keys found to match.")))
        if (d_829_valueOrError2_).IsFailure():
            res = (d_829_valueOrError2_).PropagateFailure()
            return res
        d_830_decryptClosure_: Actions.ActionWithResult
        nw5_ = DecryptSingleEncryptedDataKey()
        nw5_.ctor__(d_823_materials_, (self).client, (self).awsKmsKey, (self).grantTokens)
        d_830_decryptClosure_ = nw5_
        d_831_outcome_: Wrappers.Result
        out213_: Wrappers.Result
        out213_ = Actions.default__.ReduceToSuccess(d_830_decryptClosure_, d_827_edksToAttempt_)
        d_831_outcome_ = out213_
        d_832_SealedDecryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_833_valueOrError3_: Wrappers.Result = None
        def lambda54_(d_834_errors_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_CollectionOfErrors(d_834_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."))

        d_833_valueOrError3_ = (d_831_outcome_).MapFailure(lambda54_)
        if (d_833_valueOrError3_).IsFailure():
            res = (d_833_valueOrError3_).PropagateFailure()
            return res
        d_832_SealedDecryptionMaterials_ = (d_833_valueOrError3_).Extract()
        res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput_OnDecryptOutput(d_832_SealedDecryptionMaterials_))
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
        return "OnDecryptEncryptedDataKeyFilter"
    def ctor__(self, awsKmsKey):
        (self)._awsKmsKey = awsKmsKey

    def Invoke(self, edk):
        res: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.bool)()
        if ((edk).keyProviderId) != ((Constants.default__).PROVIDER__ID):
            res = Wrappers.Result_Success(False)
            return res
        if not(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo)):
            res = Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid AWS KMS encoding, provider info is not UTF8.")))
            return res
        d_835_keyId_: _dafny.Seq
        d_836_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_836_valueOrError0_ = (UTF8.default__.Decode((edk).keyProviderInfo)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_836_valueOrError0_).IsFailure():
            res = (d_836_valueOrError0_).PropagateFailure()
            return res
        d_835_keyId_ = (d_836_valueOrError0_).Extract()
        d_837___v0_: AwsArnParsing.AwsArn
        d_838_valueOrError1_: Wrappers.Result = None
        d_838_valueOrError1_ = (AwsArnParsing.default__.ParseAwsKmsArn(d_835_keyId_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_838_valueOrError1_).IsFailure():
            res = (d_838_valueOrError1_).PropagateFailure()
            return res
        d_837___v0_ = (d_838_valueOrError1_).Extract()
        res = Wrappers.Result_Success(((self).awsKmsKey) == (d_835_keyId_))
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
        return "DecryptSingleEncryptedDataKey"
    def ctor__(self, materials, client, awsKmsKey, grantTokens):
        (self)._materials = materials
        (self)._client = client
        (self)._awsKmsKey = awsKmsKey
        (self)._grantTokens = grantTokens

    def Invoke(self, edk):
        res: Wrappers.Result = None
        d_839_kmsUnwrap_: KmsUnwrapKeyMaterial
        nw6_ = KmsUnwrapKeyMaterial()
        nw6_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_839_kmsUnwrap_ = nw6_
        d_840_unwrapOutputRes_: Wrappers.Result
        out214_: Wrappers.Result
        out214_ = EdkWrapping.default__.UnwrapEdkMaterial((edk).ciphertext, (self).materials, d_839_kmsUnwrap_)
        d_840_unwrapOutputRes_ = out214_
        d_841_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_842_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(EdkWrapping.UnwrapEdkMaterialOutput.default(KmsUnwrapInfo.default()))()
        d_842_valueOrError0_ = d_840_unwrapOutputRes_
        if (d_842_valueOrError0_).IsFailure():
            res = (d_842_valueOrError0_).PropagateFailure()
            return res
        d_841_unwrapOutput_ = (d_842_valueOrError0_).Extract()
        d_843_result_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_844_valueOrError1_: Wrappers.Result = None
        d_844_valueOrError1_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_841_unwrapOutput_).plaintextDataKey, (d_841_unwrapOutput_).symmetricSigningKey)
        if (d_844_valueOrError1_).IsFailure():
            res = (d_844_valueOrError1_).PropagateFailure()
            return res
        d_843_result_ = (d_844_valueOrError1_).Extract()
        res = Wrappers.Result_Success(d_843_result_)
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
        return f'KmsUnwrapInfo.KmsUnwrapInfo'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KmsUnwrapInfo_KmsUnwrapInfo)
    def __hash__(self) -> int:
        return super().__hash__()


class KmsWrapInfo:
    @classmethod
    def default(cls, ):
        return lambda: KmsWrapInfo_KmsWrapInfo(_dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KmsWrapInfo(self) -> bool:
        return isinstance(self, KmsWrapInfo_KmsWrapInfo)

class KmsWrapInfo_KmsWrapInfo(KmsWrapInfo, NamedTuple('KmsWrapInfo', [('kmsKeyArn', Any)])):
    def __dafnystr__(self) -> str:
        return f'KmsWrapInfo.KmsWrapInfo({_dafny.string_of(self.kmsKeyArn)})'
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
        return "KmsUnwrapKeyMaterial"
    def ctor__(self, client, awsKmsKey, grantTokens):
        (self)._client = client
        (self)._awsKmsKey = awsKmsKey
        (self)._grantTokens = grantTokens

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result_Success.default(MaterialWrapping.UnwrapOutput.default(KmsUnwrapInfo.default()))()
        d_845_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_845_valueOrError0_ = Wrappers.default__.Need(software_amazon_cryptography_services_kms_internaldafny_types.default__.IsValid__CiphertextType((input).wrappedMaterial), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Ciphertext length invalid")))
        if (d_845_valueOrError0_).IsFailure():
            res = (d_845_valueOrError0_).PropagateFailure()
            return res
        d_846_stringifiedEncCtx_: _dafny.Map
        d_847_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Map)()
        d_847_valueOrError1_ = AwsKmsUtils.default__.StringifyEncryptionContext((input).encryptionContext)
        if (d_847_valueOrError1_).IsFailure():
            res = (d_847_valueOrError1_).PropagateFailure()
            return res
        d_846_stringifiedEncCtx_ = (d_847_valueOrError1_).Extract()
        d_848_decryptRequest_: software_amazon_cryptography_services_kms_internaldafny_types.DecryptRequest
        d_848_decryptRequest_ = software_amazon_cryptography_services_kms_internaldafny_types.DecryptRequest_DecryptRequest((input).wrappedMaterial, Wrappers.Option_Some(d_846_stringifiedEncCtx_), Wrappers.Option_Some((self).grantTokens), Wrappers.Option_Some((self).awsKmsKey), Wrappers.Option_None())
        d_849_maybeDecryptResponse_: Wrappers.Result
        out215_: Wrappers.Result
        out215_ = ((self).client).Decrypt(d_848_decryptRequest_)
        d_849_maybeDecryptResponse_ = out215_
        d_850_decryptResponse_: software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse
        d_851_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse.default())()
        def lambda55_(d_852_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_ComAmazonawsKms(d_852_e_)

        d_851_valueOrError2_ = (d_849_maybeDecryptResponse_).MapFailure(lambda55_)
        if (d_851_valueOrError2_).IsFailure():
            res = (d_851_valueOrError2_).PropagateFailure()
            return res
        d_850_decryptResponse_ = (d_851_valueOrError2_).Extract()
        d_853_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_853_valueOrError3_ = Wrappers.default__.Need((((((d_850_decryptResponse_).KeyId).is_Some) and ((((d_850_decryptResponse_).KeyId).value) == ((self).awsKmsKey))) and (((d_850_decryptResponse_).Plaintext).is_Some)) and ((AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)) == (len(((d_850_decryptResponse_).Plaintext).value))), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from KMS Decrypt")))
        if (d_853_valueOrError3_).IsFailure():
            res = (d_853_valueOrError3_).PropagateFailure()
            return res
        d_854_output_: MaterialWrapping.UnwrapOutput
        d_854_output_ = MaterialWrapping.UnwrapOutput_UnwrapOutput(((d_850_decryptResponse_).Plaintext).value, KmsUnwrapInfo_KmsUnwrapInfo())
        res = Wrappers.Result_Success(d_854_output_)
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
        return "KmsGenerateAndWrapKeyMaterial"
    def ctor__(self, client, awsKmsKey, grantTokens):
        (self)._client = client
        (self)._awsKmsKey = awsKmsKey
        (self)._grantTokens = grantTokens

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result_Success.default(MaterialWrapping.GenerateAndWrapOutput.default(KmsWrapInfo.default()))()
        d_855_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_855_suite_ = (input).algorithmSuite
        d_856_stringifiedEncCtx_: _dafny.Map
        d_857_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Map)()
        d_857_valueOrError0_ = AwsKmsUtils.default__.StringifyEncryptionContext((input).encryptionContext)
        if (d_857_valueOrError0_).IsFailure():
            res = (d_857_valueOrError0_).PropagateFailure()
            return res
        d_856_stringifiedEncCtx_ = (d_857_valueOrError0_).Extract()
        d_858_generatorRequest_: software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyRequest
        d_858_generatorRequest_ = software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyRequest_GenerateDataKeyRequest((self).awsKmsKey, Wrappers.Option_Some(d_856_stringifiedEncCtx_), Wrappers.Option_Some(AlgorithmSuites.default__.GetEncryptKeyLength(d_855_suite_)), Wrappers.Option_None(), Wrappers.Option_Some((self).grantTokens))
        d_859_maybeGenerateResponse_: Wrappers.Result
        out216_: Wrappers.Result
        out216_ = ((self).client).GenerateDataKey(d_858_generatorRequest_)
        d_859_maybeGenerateResponse_ = out216_
        d_860_generateResponse_: software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyResponse
        d_861_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyResponse.default())()
        def lambda56_(d_862_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_ComAmazonawsKms(d_862_e_)

        d_861_valueOrError1_ = (d_859_maybeGenerateResponse_).MapFailure(lambda56_)
        if (d_861_valueOrError1_).IsFailure():
            res = (d_861_valueOrError1_).PropagateFailure()
            return res
        d_860_generateResponse_ = (d_861_valueOrError1_).Extract()
        d_863_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_863_valueOrError2_ = Wrappers.default__.Need((((d_860_generateResponse_).KeyId).is_Some) and ((AwsArnParsing.default__.ParseAwsKmsIdentifier(((d_860_generateResponse_).KeyId).value)).is_Success), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from KMS GenerateDataKey:: Invalid Key Id")))
        if (d_863_valueOrError2_).IsFailure():
            res = (d_863_valueOrError2_).PropagateFailure()
            return res
        d_864_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_864_valueOrError3_ = Wrappers.default__.Need((((d_860_generateResponse_).Plaintext).is_Some) and ((AlgorithmSuites.default__.GetEncryptKeyLength(d_855_suite_)) == (len(((d_860_generateResponse_).Plaintext).value))), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS GenerateDataKey: Invalid data key")))
        if (d_864_valueOrError3_).IsFailure():
            res = (d_864_valueOrError3_).PropagateFailure()
            return res
        d_865_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_865_valueOrError4_ = Wrappers.default__.Need((((d_860_generateResponse_).CiphertextBlob).is_Some) and (software_amazon_cryptography_services_kms_internaldafny_types.default__.IsValid__CiphertextType(((d_860_generateResponse_).CiphertextBlob).value)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS GeneratedDataKey: Invalid ciphertext")))
        if (d_865_valueOrError4_).IsFailure():
            res = (d_865_valueOrError4_).PropagateFailure()
            return res
        d_866_output_: MaterialWrapping.GenerateAndWrapOutput
        d_866_output_ = MaterialWrapping.GenerateAndWrapOutput_GenerateAndWrapOutput(((d_860_generateResponse_).Plaintext).value, ((d_860_generateResponse_).CiphertextBlob).value, KmsWrapInfo_KmsWrapInfo(((d_860_generateResponse_).KeyId).value))
        res = Wrappers.Result_Success(d_866_output_)
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
        return "KmsWrapKeyMaterial"
    def ctor__(self, client, awsKmsKey, grantTokens):
        (self)._client = client
        (self)._awsKmsKey = awsKmsKey
        (self)._grantTokens = grantTokens

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result_Success.default(MaterialWrapping.WrapOutput.default(KmsWrapInfo.default()))()
        d_867_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_867_suite_ = (input).algorithmSuite
        d_868_stringifiedEncCtx_: _dafny.Map
        d_869_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Map)()
        d_869_valueOrError0_ = AwsKmsUtils.default__.StringifyEncryptionContext((input).encryptionContext)
        if (d_869_valueOrError0_).IsFailure():
            res = (d_869_valueOrError0_).PropagateFailure()
            return res
        d_868_stringifiedEncCtx_ = (d_869_valueOrError0_).Extract()
        d_870_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_870_valueOrError1_ = Wrappers.default__.Need(software_amazon_cryptography_services_kms_internaldafny_types.default__.IsValid__PlaintextType((input).plaintextMaterial), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid Plaintext on KMS Encrypt")))
        if (d_870_valueOrError1_).IsFailure():
            res = (d_870_valueOrError1_).PropagateFailure()
            return res
        d_871_encryptRequest_: software_amazon_cryptography_services_kms_internaldafny_types.EncryptRequest
        d_871_encryptRequest_ = software_amazon_cryptography_services_kms_internaldafny_types.EncryptRequest_EncryptRequest((self).awsKmsKey, (input).plaintextMaterial, Wrappers.Option_Some(d_868_stringifiedEncCtx_), Wrappers.Option_Some((self).grantTokens), Wrappers.Option_None())
        d_872_maybeEncryptResponse_: Wrappers.Result
        out217_: Wrappers.Result
        out217_ = ((self).client).Encrypt(d_871_encryptRequest_)
        d_872_maybeEncryptResponse_ = out217_
        d_873_encryptResponse_: software_amazon_cryptography_services_kms_internaldafny_types.EncryptResponse
        d_874_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_kms_internaldafny_types.EncryptResponse.default())()
        def lambda57_(d_875_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_ComAmazonawsKms(d_875_e_)

        d_874_valueOrError2_ = (d_872_maybeEncryptResponse_).MapFailure(lambda57_)
        if (d_874_valueOrError2_).IsFailure():
            res = (d_874_valueOrError2_).PropagateFailure()
            return res
        d_873_encryptResponse_ = (d_874_valueOrError2_).Extract()
        d_876_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_876_valueOrError3_ = Wrappers.default__.Need((((d_873_encryptResponse_).KeyId).is_Some) and ((AwsArnParsing.default__.ParseAwsKmsIdentifier(((d_873_encryptResponse_).KeyId).value)).is_Success), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS Encrypt:: Invalid Key Id")))
        if (d_876_valueOrError3_).IsFailure():
            res = (d_876_valueOrError3_).PropagateFailure()
            return res
        d_877_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_877_valueOrError4_ = Wrappers.default__.Need(((d_873_encryptResponse_).CiphertextBlob).is_Some, software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS Encrypt: Invalid Ciphertext Blob")))
        if (d_877_valueOrError4_).IsFailure():
            res = (d_877_valueOrError4_).PropagateFailure()
            return res
        d_878_output_: MaterialWrapping.WrapOutput
        d_878_output_ = MaterialWrapping.WrapOutput_WrapOutput(((d_873_encryptResponse_).CiphertextBlob).value, KmsWrapInfo_KmsWrapInfo(((d_873_encryptResponse_).KeyId).value))
        res = Wrappers.Result_Success(d_878_output_)
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
