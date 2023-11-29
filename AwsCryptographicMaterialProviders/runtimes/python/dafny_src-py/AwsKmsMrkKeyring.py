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
import AwsKmsKeyring
import StrictMultiKeyring
import AwsKmsDiscoveryKeyring
import DiscoveryMultiKeyring
import AwsKmsMrkDiscoveryKeyring
import MrkAwareDiscoveryMultiKeyring

assert "AwsKmsMrkKeyring" == __name__
AwsKmsMrkKeyring = sys.modules[__name__]


class AwsKmsMrkKeyring(Keyring.VerifiableInterface, software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring):
    def  __init__(self):
        self._client: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient = None
        self._awsKmsKey: _dafny.Seq = None
        self._grantTokens: _dafny.Seq = None
        self._awsKmsArn: AwsArnParsing.AwsKmsIdentifier = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsMrkKeyring.AwsKmsMrkKeyring"
    def OnEncrypt(self, input):
        out156_: Wrappers.Result
        out156_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnEncrypt(self, input)
        return out156_

    def OnDecrypt(self, input):
        out157_: Wrappers.Result
        out157_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnDecrypt(self, input)
        return out157_

    def ctor__(self, client, awsKmsKey, grantTokens):
        d_796_parsedAwsKmsId_: Wrappers.Result
        d_796_parsedAwsKmsId_ = AwsArnParsing.default__.ParseAwsKmsIdentifier(awsKmsKey)
        (self)._client = client
        (self)._awsKmsKey = awsKmsKey
        (self)._awsKmsArn = (d_796_parsedAwsKmsId_).value
        (self)._grantTokens = grantTokens

    def OnEncrypt_k(self, input):
        output: Wrappers.Result = None
        d_797_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_797_materials_ = (input).materials
        d_798_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_798_suite_ = ((input).materials).algorithmSuite
        d_799_stringifiedEncCtx_: _dafny.Map
        d_800_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Map)()
        d_800_valueOrError0_ = AwsKmsUtils.default__.StringifyEncryptionContext(((input).materials).encryptionContext)
        if (d_800_valueOrError0_).IsFailure():
            output = (d_800_valueOrError0_).PropagateFailure()
            return output
        d_799_stringifiedEncCtx_ = (d_800_valueOrError0_).Extract()
        d_801_kmsGenerateAndWrap_: AwsKmsKeyring.KmsGenerateAndWrapKeyMaterial
        nw21_ = AwsKmsKeyring.KmsGenerateAndWrapKeyMaterial()
        nw21_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_801_kmsGenerateAndWrap_ = nw21_
        d_802_kmsWrap_: AwsKmsKeyring.KmsWrapKeyMaterial
        nw22_ = AwsKmsKeyring.KmsWrapKeyMaterial()
        nw22_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_802_kmsWrap_ = nw22_
        d_803_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_804_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(EdkWrapping.WrapEdkMaterialOutput.default(AwsKmsKeyring.KmsWrapInfo.default()))()
        out158_: Wrappers.Result
        out158_ = EdkWrapping.default__.WrapEdkMaterial(d_797_materials_, d_802_kmsWrap_, d_801_kmsGenerateAndWrap_)
        d_804_valueOrError1_ = out158_
        if (d_804_valueOrError1_).IsFailure():
            output = (d_804_valueOrError1_).PropagateFailure()
            return output
        d_803_wrapOutput_ = (d_804_valueOrError1_).Extract()
        d_805_kmsKeyArn_: _dafny.Seq
        d_805_kmsKeyArn_ = ((d_803_wrapOutput_).wrapInfo).kmsKeyArn
        d_806_symmetricSigningKeyList_: Wrappers.Option
        d_806_symmetricSigningKeyList_ = (Wrappers.Option_Some(_dafny.Seq([((d_803_wrapOutput_).symmetricSigningKey).value])) if ((d_803_wrapOutput_).symmetricSigningKey).is_Some else Wrappers.Option_None())
        d_807_providerInfo_: _dafny.Seq
        d_808_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_808_valueOrError2_ = (UTF8.default__.Encode(d_805_kmsKeyArn_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_808_valueOrError2_).IsFailure():
            output = (d_808_valueOrError2_).PropagateFailure()
            return output
        d_807_providerInfo_ = (d_808_valueOrError2_).Extract()
        d_809_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_809_valueOrError3_ = Wrappers.default__.Need((len(d_807_providerInfo_)) < ((StandardLibrary_mUInt.default__).UINT16__LIMIT), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS GenerateDataKey: Key ID too long.")))
        if (d_809_valueOrError3_).IsFailure():
            output = (d_809_valueOrError3_).PropagateFailure()
            return output
        d_810_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_810_edk_ = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey((Constants.default__).PROVIDER__ID, d_807_providerInfo_, (d_803_wrapOutput_).wrappedMaterial)
        if (d_803_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_811_result_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            d_812_valueOrError4_: Wrappers.Result = None
            d_812_valueOrError4_ = Materials.default__.EncryptionMaterialAddDataKey(d_797_materials_, (d_803_wrapOutput_).plaintextDataKey, _dafny.Seq([d_810_edk_]), d_806_symmetricSigningKeyList_)
            if (d_812_valueOrError4_).IsFailure():
                output = (d_812_valueOrError4_).PropagateFailure()
                return output
            d_811_result_ = (d_812_valueOrError4_).Extract()
            output = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_811_result_))
            return output
        elif (d_803_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_813_result_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            d_814_valueOrError5_: Wrappers.Result = None
            d_814_valueOrError5_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys(d_797_materials_, _dafny.Seq([d_810_edk_]), d_806_symmetricSigningKeyList_)
            if (d_814_valueOrError5_).IsFailure():
                output = (d_814_valueOrError5_).PropagateFailure()
                return output
            d_813_result_ = (d_814_valueOrError5_).Extract()
            output = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_813_result_))
            return output
        return output

    def OnDecrypt_k(self, input):
        output: Wrappers.Result = None
        d_815_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_815_materials_ = (input).materials
        d_816_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_816_suite_ = ((input).materials).algorithmSuite
        d_817_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_817_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_815_materials_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_817_valueOrError0_).IsFailure():
            output = (d_817_valueOrError0_).PropagateFailure()
            return output
        d_818_filter_: AwsKmsUtils.OnDecryptMrkAwareEncryptedDataKeyFilter
        nw23_ = AwsKmsUtils.OnDecryptMrkAwareEncryptedDataKeyFilter()
        nw23_.ctor__((self).awsKmsArn, (Constants.default__).PROVIDER__ID)
        d_818_filter_ = nw23_
        d_819_edksToAttempt_: _dafny.Seq
        d_820_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out159_: Wrappers.Result
        out159_ = Actions.default__.FilterWithResult(d_818_filter_, (input).encryptedDataKeys)
        d_820_valueOrError1_ = out159_
        if (d_820_valueOrError1_).IsFailure():
            output = (d_820_valueOrError1_).PropagateFailure()
            return output
        d_819_edksToAttempt_ = (d_820_valueOrError1_).Extract()
        d_821_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_821_valueOrError2_ = Wrappers.default__.Need((0) < (len(d_819_edksToAttempt_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to decrypt data key: No Encrypted Data Keys found to match.")))
        if (d_821_valueOrError2_).IsFailure():
            output = (d_821_valueOrError2_).PropagateFailure()
            return output
        d_822_decryptClosure_: AwsKmsMrkKeyring.DecryptSingleEncryptedDataKey
        nw24_ = AwsKmsMrkKeyring.DecryptSingleEncryptedDataKey()
        nw24_.ctor__(d_815_materials_, (self).client, (self).awsKmsKey, (self).grantTokens)
        d_822_decryptClosure_ = nw24_
        d_823_outcome_: Wrappers.Result
        out160_: Wrappers.Result
        out160_ = Actions.default__.ReduceToSuccess(d_822_decryptClosure_, d_819_edksToAttempt_)
        d_823_outcome_ = out160_
        d_824_SealedDecryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_825_valueOrError3_: Wrappers.Result = None
        def lambda64_(d_826_errors_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_CollectionOfErrors(d_826_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."))

        d_825_valueOrError3_ = (d_823_outcome_).MapFailure(lambda64_)
        if (d_825_valueOrError3_).IsFailure():
            output = (d_825_valueOrError3_).PropagateFailure()
            return output
        d_824_SealedDecryptionMaterials_ = (d_825_valueOrError3_).Extract()
        output = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput_OnDecryptOutput(d_824_SealedDecryptionMaterials_))
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
        self._materials: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials = None
        self._client: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient = None
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
        d_827_kmsUnwrap_: AwsKmsKeyring.KmsUnwrapKeyMaterial
        nw25_ = AwsKmsKeyring.KmsUnwrapKeyMaterial()
        nw25_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_827_kmsUnwrap_ = nw25_
        d_828_unwrapOutputRes_: Wrappers.Result
        out161_: Wrappers.Result
        out161_ = EdkWrapping.default__.UnwrapEdkMaterial((edk).ciphertext, (self).materials, d_827_kmsUnwrap_)
        d_828_unwrapOutputRes_ = out161_
        d_829_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_830_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(EdkWrapping.UnwrapEdkMaterialOutput.default(AwsKmsKeyring.KmsUnwrapInfo.default()))()
        d_830_valueOrError0_ = d_828_unwrapOutputRes_
        if (d_830_valueOrError0_).IsFailure():
            res = (d_830_valueOrError0_).PropagateFailure()
            return res
        d_829_unwrapOutput_ = (d_830_valueOrError0_).Extract()
        d_831_result_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_832_valueOrError1_: Wrappers.Result = None
        d_832_valueOrError1_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_829_unwrapOutput_).plaintextDataKey, (d_829_unwrapOutput_).symmetricSigningKey)
        if (d_832_valueOrError1_).IsFailure():
            res = (d_832_valueOrError1_).PropagateFailure()
            return res
        d_831_result_ = (d_832_valueOrError1_).Extract()
        res = Wrappers.Result_Success(d_831_result_)
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
