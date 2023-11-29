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
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import software_amazon_cryptography_keystore_internaldafny
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

assert "AwsKmsKeyring" == __name__
AwsKmsKeyring = sys.modules[__name__]


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
        out132_: Wrappers.Result
        out132_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnEncrypt(self, input)
        return out132_

    def OnDecrypt(self, input):
        out133_: Wrappers.Result
        out133_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnDecrypt(self, input)
        return out133_

    def ctor__(self, client, awsKmsKey, grantTokens):
        d_605_parsedAwsKmsId_: Wrappers.Result
        d_605_parsedAwsKmsId_ = AwsArnParsing.default__.ParseAwsKmsIdentifier(awsKmsKey)
        (self)._client = client
        (self)._awsKmsKey = awsKmsKey
        (self)._awsKmsArn = (d_605_parsedAwsKmsId_).value
        (self)._grantTokens = grantTokens

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        d_606_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_606_materials_ = (input).materials
        d_607_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_607_suite_ = ((input).materials).algorithmSuite
        d_608_stringifiedEncCtx_: _dafny.Map
        d_609_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Map)()
        d_609_valueOrError0_ = AwsKmsUtils.default__.StringifyEncryptionContext(((input).materials).encryptionContext)
        if (d_609_valueOrError0_).IsFailure():
            res = (d_609_valueOrError0_).PropagateFailure()
            return res
        d_608_stringifiedEncCtx_ = (d_609_valueOrError0_).Extract()
        d_610_kmsGenerateAndWrap_: AwsKmsKeyring.KmsGenerateAndWrapKeyMaterial
        nw2_ = AwsKmsKeyring.KmsGenerateAndWrapKeyMaterial()
        nw2_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_610_kmsGenerateAndWrap_ = nw2_
        d_611_kmsWrap_: AwsKmsKeyring.KmsWrapKeyMaterial
        nw3_ = AwsKmsKeyring.KmsWrapKeyMaterial()
        nw3_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_611_kmsWrap_ = nw3_
        d_612_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_613_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(EdkWrapping.WrapEdkMaterialOutput.default(AwsKmsKeyring.KmsWrapInfo.default()))()
        out134_: Wrappers.Result
        out134_ = EdkWrapping.default__.WrapEdkMaterial(d_606_materials_, d_611_kmsWrap_, d_610_kmsGenerateAndWrap_)
        d_613_valueOrError1_ = out134_
        if (d_613_valueOrError1_).IsFailure():
            res = (d_613_valueOrError1_).PropagateFailure()
            return res
        d_612_wrapOutput_ = (d_613_valueOrError1_).Extract()
        d_614_kmsKeyArn_: _dafny.Seq
        d_614_kmsKeyArn_ = ((d_612_wrapOutput_).wrapInfo).kmsKeyArn
        d_615_symmetricSigningKeyList_: Wrappers.Option
        d_615_symmetricSigningKeyList_ = (Wrappers.Option_Some(_dafny.Seq([((d_612_wrapOutput_).symmetricSigningKey).value])) if ((d_612_wrapOutput_).symmetricSigningKey).is_Some else Wrappers.Option_None())
        d_616_providerInfo_: _dafny.Seq
        d_617_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_617_valueOrError2_ = (UTF8.default__.Encode(d_614_kmsKeyArn_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_617_valueOrError2_).IsFailure():
            res = (d_617_valueOrError2_).PropagateFailure()
            return res
        d_616_providerInfo_ = (d_617_valueOrError2_).Extract()
        d_618_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_618_valueOrError3_ = Wrappers.default__.Need((len(d_616_providerInfo_)) < ((StandardLibrary_mUInt.default__).UINT16__LIMIT), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS GenerateDataKey: Key ID too long.")))
        if (d_618_valueOrError3_).IsFailure():
            res = (d_618_valueOrError3_).PropagateFailure()
            return res
        d_619_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_619_edk_ = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey((Constants.default__).PROVIDER__ID, d_616_providerInfo_, (d_612_wrapOutput_).wrappedMaterial)
        if (d_612_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_620_result_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            d_621_valueOrError4_: Wrappers.Result = None
            d_621_valueOrError4_ = Materials.default__.EncryptionMaterialAddDataKey(d_606_materials_, (d_612_wrapOutput_).plaintextDataKey, _dafny.Seq([d_619_edk_]), d_615_symmetricSigningKeyList_)
            if (d_621_valueOrError4_).IsFailure():
                res = (d_621_valueOrError4_).PropagateFailure()
                return res
            d_620_result_ = (d_621_valueOrError4_).Extract()
            res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_620_result_))
            return res
        elif (d_612_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_622_result_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            d_623_valueOrError5_: Wrappers.Result = None
            d_623_valueOrError5_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys(d_606_materials_, _dafny.Seq([d_619_edk_]), d_615_symmetricSigningKeyList_)
            if (d_623_valueOrError5_).IsFailure():
                res = (d_623_valueOrError5_).PropagateFailure()
                return res
            d_622_result_ = (d_623_valueOrError5_).Extract()
            res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_622_result_))
            return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_624_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_624_materials_ = (input).materials
        d_625_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_625_suite_ = ((input).materials).algorithmSuite
        d_626_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_626_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_624_materials_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_626_valueOrError0_).IsFailure():
            res = (d_626_valueOrError0_).PropagateFailure()
            return res
        d_627_filter_: AwsKmsKeyring.OnDecryptEncryptedDataKeyFilter
        nw4_ = AwsKmsKeyring.OnDecryptEncryptedDataKeyFilter()
        nw4_.ctor__((self).awsKmsKey)
        d_627_filter_ = nw4_
        d_628_edksToAttempt_: _dafny.Seq
        d_629_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out135_: Wrappers.Result
        out135_ = Actions.default__.FilterWithResult(d_627_filter_, (input).encryptedDataKeys)
        d_629_valueOrError1_ = out135_
        if (d_629_valueOrError1_).IsFailure():
            res = (d_629_valueOrError1_).PropagateFailure()
            return res
        d_628_edksToAttempt_ = (d_629_valueOrError1_).Extract()
        d_630_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_630_valueOrError2_ = Wrappers.default__.Need((0) < (len(d_628_edksToAttempt_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to decrypt data key: No Encrypted Data Keys found to match.")))
        if (d_630_valueOrError2_).IsFailure():
            res = (d_630_valueOrError2_).PropagateFailure()
            return res
        d_631_decryptClosure_: Actions.ActionWithResult
        nw5_ = AwsKmsKeyring.DecryptSingleEncryptedDataKey()
        nw5_.ctor__(d_624_materials_, (self).client, (self).awsKmsKey, (self).grantTokens)
        d_631_decryptClosure_ = nw5_
        d_632_outcome_: Wrappers.Result
        out136_: Wrappers.Result
        out136_ = Actions.default__.ReduceToSuccess(d_631_decryptClosure_, d_628_edksToAttempt_)
        d_632_outcome_ = out136_
        d_633_SealedDecryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_634_valueOrError3_: Wrappers.Result = None
        def lambda53_(d_635_errors_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_CollectionOfErrors(d_635_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."))

        d_634_valueOrError3_ = (d_632_outcome_).MapFailure(lambda53_)
        if (d_634_valueOrError3_).IsFailure():
            res = (d_634_valueOrError3_).PropagateFailure()
            return res
        d_633_SealedDecryptionMaterials_ = (d_634_valueOrError3_).Extract()
        res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput_OnDecryptOutput(d_633_SealedDecryptionMaterials_))
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
        res: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.bool)()
        if ((edk).keyProviderId) != ((Constants.default__).PROVIDER__ID):
            res = Wrappers.Result_Success(False)
            return res
        if not(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo)):
            res = Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid AWS KMS encoding, provider info is not UTF8.")))
            return res
        d_636_keyId_: _dafny.Seq
        d_637_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_637_valueOrError0_ = (UTF8.default__.Decode((edk).keyProviderInfo)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_637_valueOrError0_).IsFailure():
            res = (d_637_valueOrError0_).PropagateFailure()
            return res
        d_636_keyId_ = (d_637_valueOrError0_).Extract()
        d_638___v0_: AwsArnParsing.AwsArn
        d_639_valueOrError1_: Wrappers.Result = None
        d_639_valueOrError1_ = (AwsArnParsing.default__.ParseAwsKmsArn(d_636_keyId_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_639_valueOrError1_).IsFailure():
            res = (d_639_valueOrError1_).PropagateFailure()
            return res
        d_638___v0_ = (d_639_valueOrError1_).Extract()
        res = Wrappers.Result_Success(((self).awsKmsKey) == (d_636_keyId_))
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
        d_640_kmsUnwrap_: AwsKmsKeyring.KmsUnwrapKeyMaterial
        nw6_ = AwsKmsKeyring.KmsUnwrapKeyMaterial()
        nw6_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_640_kmsUnwrap_ = nw6_
        d_641_unwrapOutputRes_: Wrappers.Result
        out137_: Wrappers.Result
        out137_ = EdkWrapping.default__.UnwrapEdkMaterial((edk).ciphertext, (self).materials, d_640_kmsUnwrap_)
        d_641_unwrapOutputRes_ = out137_
        d_642_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_643_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(EdkWrapping.UnwrapEdkMaterialOutput.default(AwsKmsKeyring.KmsUnwrapInfo.default()))()
        d_643_valueOrError0_ = d_641_unwrapOutputRes_
        if (d_643_valueOrError0_).IsFailure():
            res = (d_643_valueOrError0_).PropagateFailure()
            return res
        d_642_unwrapOutput_ = (d_643_valueOrError0_).Extract()
        d_644_result_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_645_valueOrError1_: Wrappers.Result = None
        d_645_valueOrError1_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_642_unwrapOutput_).plaintextDataKey, (d_642_unwrapOutput_).symmetricSigningKey)
        if (d_645_valueOrError1_).IsFailure():
            res = (d_645_valueOrError1_).PropagateFailure()
            return res
        d_644_result_ = (d_645_valueOrError1_).Extract()
        res = Wrappers.Result_Success(d_644_result_)
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
        return isinstance(self, AwsKmsKeyring.KmsUnwrapInfo_KmsUnwrapInfo)

class KmsUnwrapInfo_KmsUnwrapInfo(KmsUnwrapInfo, NamedTuple('KmsUnwrapInfo', [])):
    def __dafnystr__(self) -> str:
        return f'AwsKmsKeyring.KmsUnwrapInfo.KmsUnwrapInfo'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AwsKmsKeyring.KmsUnwrapInfo_KmsUnwrapInfo)
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
        return isinstance(self, AwsKmsKeyring.KmsWrapInfo_KmsWrapInfo)

class KmsWrapInfo_KmsWrapInfo(KmsWrapInfo, NamedTuple('KmsWrapInfo', [('kmsKeyArn', Any)])):
    def __dafnystr__(self) -> str:
        return f'AwsKmsKeyring.KmsWrapInfo.KmsWrapInfo({_dafny.string_of(self.kmsKeyArn)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AwsKmsKeyring.KmsWrapInfo_KmsWrapInfo) and self.kmsKeyArn == __o.kmsKeyArn
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
        res: Wrappers.Result = Wrappers.Result_Success.default(MaterialWrapping.UnwrapOutput.default(AwsKmsKeyring.KmsUnwrapInfo.default()))()
        d_646_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_646_valueOrError0_ = Wrappers.default__.Need(software_amazon_cryptography_services_kms_internaldafny_types.default__.IsValid__CiphertextType((input).wrappedMaterial), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Ciphertext length invalid")))
        if (d_646_valueOrError0_).IsFailure():
            res = (d_646_valueOrError0_).PropagateFailure()
            return res
        d_647_stringifiedEncCtx_: _dafny.Map
        d_648_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Map)()
        d_648_valueOrError1_ = AwsKmsUtils.default__.StringifyEncryptionContext((input).encryptionContext)
        if (d_648_valueOrError1_).IsFailure():
            res = (d_648_valueOrError1_).PropagateFailure()
            return res
        d_647_stringifiedEncCtx_ = (d_648_valueOrError1_).Extract()
        d_649_decryptRequest_: software_amazon_cryptography_services_kms_internaldafny_types.DecryptRequest
        d_649_decryptRequest_ = software_amazon_cryptography_services_kms_internaldafny_types.DecryptRequest_DecryptRequest((input).wrappedMaterial, Wrappers.Option_Some(d_647_stringifiedEncCtx_), Wrappers.Option_Some((self).grantTokens), Wrappers.Option_Some((self).awsKmsKey), Wrappers.Option_None())
        d_650_maybeDecryptResponse_: Wrappers.Result
        out138_: Wrappers.Result
        out138_ = ((self).client).Decrypt(d_649_decryptRequest_)
        d_650_maybeDecryptResponse_ = out138_
        d_651_decryptResponse_: software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse
        d_652_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse.default())()
        def lambda54_(d_653_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_ComAmazonawsKms(d_653_e_)

        d_652_valueOrError2_ = (d_650_maybeDecryptResponse_).MapFailure(lambda54_)
        if (d_652_valueOrError2_).IsFailure():
            res = (d_652_valueOrError2_).PropagateFailure()
            return res
        d_651_decryptResponse_ = (d_652_valueOrError2_).Extract()
        d_654_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_654_valueOrError3_ = Wrappers.default__.Need((((((d_651_decryptResponse_).KeyId).is_Some) and ((((d_651_decryptResponse_).KeyId).value) == ((self).awsKmsKey))) and (((d_651_decryptResponse_).Plaintext).is_Some)) and ((AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)) == (len(((d_651_decryptResponse_).Plaintext).value))), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from KMS Decrypt")))
        if (d_654_valueOrError3_).IsFailure():
            res = (d_654_valueOrError3_).PropagateFailure()
            return res
        d_655_output_: MaterialWrapping.UnwrapOutput
        d_655_output_ = MaterialWrapping.UnwrapOutput_UnwrapOutput(((d_651_decryptResponse_).Plaintext).value, AwsKmsKeyring.KmsUnwrapInfo_KmsUnwrapInfo())
        res = Wrappers.Result_Success(d_655_output_)
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
        res: Wrappers.Result = Wrappers.Result_Success.default(MaterialWrapping.GenerateAndWrapOutput.default(AwsKmsKeyring.KmsWrapInfo.default()))()
        d_656_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_656_suite_ = (input).algorithmSuite
        d_657_stringifiedEncCtx_: _dafny.Map
        d_658_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Map)()
        d_658_valueOrError0_ = AwsKmsUtils.default__.StringifyEncryptionContext((input).encryptionContext)
        if (d_658_valueOrError0_).IsFailure():
            res = (d_658_valueOrError0_).PropagateFailure()
            return res
        d_657_stringifiedEncCtx_ = (d_658_valueOrError0_).Extract()
        d_659_generatorRequest_: software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyRequest
        d_659_generatorRequest_ = software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyRequest_GenerateDataKeyRequest((self).awsKmsKey, Wrappers.Option_Some(d_657_stringifiedEncCtx_), Wrappers.Option_Some(AlgorithmSuites.default__.GetEncryptKeyLength(d_656_suite_)), Wrappers.Option_None(), Wrappers.Option_Some((self).grantTokens))
        d_660_maybeGenerateResponse_: Wrappers.Result
        out139_: Wrappers.Result
        out139_ = ((self).client).GenerateDataKey(d_659_generatorRequest_)
        d_660_maybeGenerateResponse_ = out139_
        d_661_generateResponse_: software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyResponse
        d_662_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyResponse.default())()
        def lambda55_(d_663_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_ComAmazonawsKms(d_663_e_)

        d_662_valueOrError1_ = (d_660_maybeGenerateResponse_).MapFailure(lambda55_)
        if (d_662_valueOrError1_).IsFailure():
            res = (d_662_valueOrError1_).PropagateFailure()
            return res
        d_661_generateResponse_ = (d_662_valueOrError1_).Extract()
        d_664_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_664_valueOrError2_ = Wrappers.default__.Need((((d_661_generateResponse_).KeyId).is_Some) and ((AwsArnParsing.default__.ParseAwsKmsIdentifier(((d_661_generateResponse_).KeyId).value)).is_Success), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from KMS GenerateDataKey:: Invalid Key Id")))
        if (d_664_valueOrError2_).IsFailure():
            res = (d_664_valueOrError2_).PropagateFailure()
            return res
        d_665_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_665_valueOrError3_ = Wrappers.default__.Need((((d_661_generateResponse_).Plaintext).is_Some) and ((AlgorithmSuites.default__.GetEncryptKeyLength(d_656_suite_)) == (len(((d_661_generateResponse_).Plaintext).value))), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS GenerateDataKey: Invalid data key")))
        if (d_665_valueOrError3_).IsFailure():
            res = (d_665_valueOrError3_).PropagateFailure()
            return res
        d_666_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_666_valueOrError4_ = Wrappers.default__.Need((((d_661_generateResponse_).CiphertextBlob).is_Some) and (software_amazon_cryptography_services_kms_internaldafny_types.default__.IsValid__CiphertextType(((d_661_generateResponse_).CiphertextBlob).value)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS GeneratedDataKey: Invalid ciphertext")))
        if (d_666_valueOrError4_).IsFailure():
            res = (d_666_valueOrError4_).PropagateFailure()
            return res
        d_667_output_: MaterialWrapping.GenerateAndWrapOutput
        d_667_output_ = MaterialWrapping.GenerateAndWrapOutput_GenerateAndWrapOutput(((d_661_generateResponse_).Plaintext).value, ((d_661_generateResponse_).CiphertextBlob).value, AwsKmsKeyring.KmsWrapInfo_KmsWrapInfo(((d_661_generateResponse_).KeyId).value))
        res = Wrappers.Result_Success(d_667_output_)
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
        res: Wrappers.Result = Wrappers.Result_Success.default(MaterialWrapping.WrapOutput.default(AwsKmsKeyring.KmsWrapInfo.default()))()
        d_668_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_668_suite_ = (input).algorithmSuite
        d_669_stringifiedEncCtx_: _dafny.Map
        d_670_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Map)()
        d_670_valueOrError0_ = AwsKmsUtils.default__.StringifyEncryptionContext((input).encryptionContext)
        if (d_670_valueOrError0_).IsFailure():
            res = (d_670_valueOrError0_).PropagateFailure()
            return res
        d_669_stringifiedEncCtx_ = (d_670_valueOrError0_).Extract()
        d_671_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_671_valueOrError1_ = Wrappers.default__.Need(software_amazon_cryptography_services_kms_internaldafny_types.default__.IsValid__PlaintextType((input).plaintextMaterial), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid Plaintext on KMS Encrypt")))
        if (d_671_valueOrError1_).IsFailure():
            res = (d_671_valueOrError1_).PropagateFailure()
            return res
        d_672_encryptRequest_: software_amazon_cryptography_services_kms_internaldafny_types.EncryptRequest
        d_672_encryptRequest_ = software_amazon_cryptography_services_kms_internaldafny_types.EncryptRequest_EncryptRequest((self).awsKmsKey, (input).plaintextMaterial, Wrappers.Option_Some(d_669_stringifiedEncCtx_), Wrappers.Option_Some((self).grantTokens), Wrappers.Option_None())
        d_673_maybeEncryptResponse_: Wrappers.Result
        out140_: Wrappers.Result
        out140_ = ((self).client).Encrypt(d_672_encryptRequest_)
        d_673_maybeEncryptResponse_ = out140_
        d_674_encryptResponse_: software_amazon_cryptography_services_kms_internaldafny_types.EncryptResponse
        d_675_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_kms_internaldafny_types.EncryptResponse.default())()
        def lambda56_(d_676_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_ComAmazonawsKms(d_676_e_)

        d_675_valueOrError2_ = (d_673_maybeEncryptResponse_).MapFailure(lambda56_)
        if (d_675_valueOrError2_).IsFailure():
            res = (d_675_valueOrError2_).PropagateFailure()
            return res
        d_674_encryptResponse_ = (d_675_valueOrError2_).Extract()
        d_677_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_677_valueOrError3_ = Wrappers.default__.Need((((d_674_encryptResponse_).KeyId).is_Some) and ((AwsArnParsing.default__.ParseAwsKmsIdentifier(((d_674_encryptResponse_).KeyId).value)).is_Success), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS Encrypt:: Invalid Key Id")))
        if (d_677_valueOrError3_).IsFailure():
            res = (d_677_valueOrError3_).PropagateFailure()
            return res
        d_678_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_678_valueOrError4_ = Wrappers.default__.Need(((d_674_encryptResponse_).CiphertextBlob).is_Some, software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS Encrypt: Invalid Ciphertext Blob")))
        if (d_678_valueOrError4_).IsFailure():
            res = (d_678_valueOrError4_).PropagateFailure()
            return res
        d_679_output_: MaterialWrapping.WrapOutput
        d_679_output_ = MaterialWrapping.WrapOutput_WrapOutput(((d_674_encryptResponse_).CiphertextBlob).value, AwsKmsKeyring.KmsWrapInfo_KmsWrapInfo(((d_674_encryptResponse_).KeyId).value))
        res = Wrappers.Result_Success(d_679_output_)
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
