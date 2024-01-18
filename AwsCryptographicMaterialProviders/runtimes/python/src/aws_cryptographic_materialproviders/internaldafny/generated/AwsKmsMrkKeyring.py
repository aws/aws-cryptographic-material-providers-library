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
import Relations
import Seq_MergeSort
import Math
import Seq
import Unicode
import Functions
import Utf8EncodingForm
import Utf16EncodingForm
import UnicodeStrings
import DafnyLibraries
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
import UUID
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
import AwsKmsKeyring
import StrictMultiKeyring
import AwsKmsDiscoveryKeyring
import DiscoveryMultiKeyring
import AwsKmsMrkDiscoveryKeyring
import MrkAwareDiscoveryMultiKeyring

# Module: AwsKmsMrkKeyring


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
        out105_: Wrappers.Result
        out105_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnEncrypt(self, input)
        return out105_

    def OnDecrypt(self, input):
        out106_: Wrappers.Result
        out106_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnDecrypt(self, input)
        return out106_

    def ctor__(self, client, awsKmsKey, grantTokens):
        d_690_parsedAwsKmsId_: Wrappers.Result
        d_690_parsedAwsKmsId_ = AwsArnParsing.default__.ParseAwsKmsIdentifier(awsKmsKey)
        (self)._client = client
        (self)._awsKmsKey = awsKmsKey
        (self)._awsKmsArn = (d_690_parsedAwsKmsId_).value
        (self)._grantTokens = grantTokens

    def OnEncrypt_k(self, input):
        output: Wrappers.Result = None
        d_691_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_691_materials_ = (input).materials
        d_692_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_692_suite_ = ((input).materials).algorithmSuite
        d_693_stringifiedEncCtx_: _dafny.Map
        d_694_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        d_694_valueOrError0_ = AwsKmsUtils.default__.StringifyEncryptionContext(((input).materials).encryptionContext)
        if (d_694_valueOrError0_).IsFailure():
            output = (d_694_valueOrError0_).PropagateFailure()
            return output
        d_693_stringifiedEncCtx_ = (d_694_valueOrError0_).Extract()
        d_695_kmsGenerateAndWrap_: AwsKmsKeyring.KmsGenerateAndWrapKeyMaterial
        nw20_ = AwsKmsKeyring.KmsGenerateAndWrapKeyMaterial()
        nw20_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_695_kmsGenerateAndWrap_ = nw20_
        d_696_kmsWrap_: AwsKmsKeyring.KmsWrapKeyMaterial
        nw21_ = AwsKmsKeyring.KmsWrapKeyMaterial()
        nw21_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_696_kmsWrap_ = nw21_
        d_697_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_698_valueOrError1_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.WrapEdkMaterialOutput.default(AwsKmsKeyring.KmsWrapInfo.default()))()
        out107_: Wrappers.Result
        out107_ = EdkWrapping.default__.WrapEdkMaterial(d_691_materials_, d_696_kmsWrap_, d_695_kmsGenerateAndWrap_)
        d_698_valueOrError1_ = out107_
        if (d_698_valueOrError1_).IsFailure():
            output = (d_698_valueOrError1_).PropagateFailure()
            return output
        d_697_wrapOutput_ = (d_698_valueOrError1_).Extract()
        d_699_kmsKeyArn_: _dafny.Seq
        d_699_kmsKeyArn_ = ((d_697_wrapOutput_).wrapInfo).kmsKeyArn
        d_700_symmetricSigningKeyList_: Wrappers.Option
        d_700_symmetricSigningKeyList_ = (Wrappers.Option_Some(_dafny.Seq([((d_697_wrapOutput_).symmetricSigningKey).value])) if ((d_697_wrapOutput_).symmetricSigningKey).is_Some else Wrappers.Option_None())
        d_701_providerInfo_: _dafny.Seq
        d_702_valueOrError2_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_702_valueOrError2_ = (UTF8.default__.Encode(d_699_kmsKeyArn_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_702_valueOrError2_).IsFailure():
            output = (d_702_valueOrError2_).PropagateFailure()
            return output
        d_701_providerInfo_ = (d_702_valueOrError2_).Extract()
        d_703_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_703_valueOrError3_ = Wrappers.default__.Need((len(d_701_providerInfo_)) < (StandardLibrary_UInt.default__.UINT16__LIMIT), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS GenerateDataKey: Key ID too long.")))
        if (d_703_valueOrError3_).IsFailure():
            output = (d_703_valueOrError3_).PropagateFailure()
            return output
        d_704_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_704_edk_ = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey(Constants.default__.PROVIDER__ID, d_701_providerInfo_, (d_697_wrapOutput_).wrappedMaterial)
        if (d_697_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_705_result_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            d_706_valueOrError4_: Wrappers.Result = None
            d_706_valueOrError4_ = Materials.default__.EncryptionMaterialAddDataKey(d_691_materials_, (d_697_wrapOutput_).plaintextDataKey, _dafny.Seq([d_704_edk_]), d_700_symmetricSigningKeyList_)
            if (d_706_valueOrError4_).IsFailure():
                output = (d_706_valueOrError4_).PropagateFailure()
                return output
            d_705_result_ = (d_706_valueOrError4_).Extract()
            output = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_705_result_))
            return output
        elif (d_697_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_707_result_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            d_708_valueOrError5_: Wrappers.Result = None
            d_708_valueOrError5_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys(d_691_materials_, _dafny.Seq([d_704_edk_]), d_700_symmetricSigningKeyList_)
            if (d_708_valueOrError5_).IsFailure():
                output = (d_708_valueOrError5_).PropagateFailure()
                return output
            d_707_result_ = (d_708_valueOrError5_).Extract()
            output = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_707_result_))
            return output
        return output

    def OnDecrypt_k(self, input):
        output: Wrappers.Result = None
        d_709_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_709_materials_ = (input).materials
        d_710_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_710_suite_ = ((input).materials).algorithmSuite
        d_711_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_711_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_709_materials_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_711_valueOrError0_).IsFailure():
            output = (d_711_valueOrError0_).PropagateFailure()
            return output
        d_712_filter_: AwsKmsUtils.OnDecryptMrkAwareEncryptedDataKeyFilter
        nw22_ = AwsKmsUtils.OnDecryptMrkAwareEncryptedDataKeyFilter()
        nw22_.ctor__((self).awsKmsArn, Constants.default__.PROVIDER__ID)
        d_712_filter_ = nw22_
        d_713_edksToAttempt_: _dafny.Seq
        d_714_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out108_: Wrappers.Result
        out108_ = Actions.default__.FilterWithResult(d_712_filter_, (input).encryptedDataKeys)
        d_714_valueOrError1_ = out108_
        if (d_714_valueOrError1_).IsFailure():
            output = (d_714_valueOrError1_).PropagateFailure()
            return output
        d_713_edksToAttempt_ = (d_714_valueOrError1_).Extract()
        d_715_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_715_valueOrError2_ = Wrappers.default__.Need((0) < (len(d_713_edksToAttempt_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to decrypt data key: No Encrypted Data Keys found to match.")))
        if (d_715_valueOrError2_).IsFailure():
            output = (d_715_valueOrError2_).PropagateFailure()
            return output
        d_716_decryptClosure_: DecryptSingleEncryptedDataKey
        nw23_ = DecryptSingleEncryptedDataKey()
        nw23_.ctor__(d_709_materials_, (self).client, (self).awsKmsKey, (self).grantTokens)
        d_716_decryptClosure_ = nw23_
        d_717_outcome_: Wrappers.Result
        out109_: Wrappers.Result
        out109_ = Actions.default__.ReduceToSuccess(d_716_decryptClosure_, d_713_edksToAttempt_)
        d_717_outcome_ = out109_
        d_718_SealedDecryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_719_valueOrError3_: Wrappers.Result = None
        def lambda64_(d_720_errors_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_CollectionOfErrors(d_720_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."))

        d_719_valueOrError3_ = (d_717_outcome_).MapFailure(lambda64_)
        if (d_719_valueOrError3_).IsFailure():
            output = (d_719_valueOrError3_).PropagateFailure()
            return output
        d_718_SealedDecryptionMaterials_ = (d_719_valueOrError3_).Extract()
        output = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput_OnDecryptOutput(d_718_SealedDecryptionMaterials_))
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
        d_721_kmsUnwrap_: AwsKmsKeyring.KmsUnwrapKeyMaterial
        nw24_ = AwsKmsKeyring.KmsUnwrapKeyMaterial()
        nw24_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_721_kmsUnwrap_ = nw24_
        d_722_unwrapOutputRes_: Wrappers.Result
        out110_: Wrappers.Result
        out110_ = EdkWrapping.default__.UnwrapEdkMaterial((edk).ciphertext, (self).materials, d_721_kmsUnwrap_)
        d_722_unwrapOutputRes_ = out110_
        d_723_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_724_valueOrError0_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.UnwrapEdkMaterialOutput.default(AwsKmsKeyring.KmsUnwrapInfo.default()))()
        d_724_valueOrError0_ = d_722_unwrapOutputRes_
        if (d_724_valueOrError0_).IsFailure():
            res = (d_724_valueOrError0_).PropagateFailure()
            return res
        d_723_unwrapOutput_ = (d_724_valueOrError0_).Extract()
        d_725_result_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_726_valueOrError1_: Wrappers.Result = None
        d_726_valueOrError1_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_723_unwrapOutput_).plaintextDataKey, (d_723_unwrapOutput_).symmetricSigningKey)
        if (d_726_valueOrError1_).IsFailure():
            res = (d_726_valueOrError1_).PropagateFailure()
            return res
        d_725_result_ = (d_726_valueOrError1_).Extract()
        res = Wrappers.Result_Success(d_725_result_)
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
