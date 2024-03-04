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
        d_692_parsedAwsKmsId_: Wrappers.Result
        d_692_parsedAwsKmsId_ = AwsArnParsing.default__.ParseAwsKmsIdentifier(awsKmsKey)
        (self)._client = client
        (self)._awsKmsKey = awsKmsKey
        (self)._awsKmsArn = (d_692_parsedAwsKmsId_).value
        (self)._grantTokens = grantTokens

    def OnEncrypt_k(self, input):
        output: Wrappers.Result = None
        d_693_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_693_materials_ = (input).materials
        d_694_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_694_suite_ = ((input).materials).algorithmSuite
        d_695_stringifiedEncCtx_: _dafny.Map
        d_696_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        d_696_valueOrError0_ = AwsKmsUtils.default__.StringifyEncryptionContext(((input).materials).encryptionContext)
        if (d_696_valueOrError0_).IsFailure():
            output = (d_696_valueOrError0_).PropagateFailure()
            return output
        d_695_stringifiedEncCtx_ = (d_696_valueOrError0_).Extract()
        d_697_kmsGenerateAndWrap_: AwsKmsKeyring.KmsGenerateAndWrapKeyMaterial
        nw20_ = AwsKmsKeyring.KmsGenerateAndWrapKeyMaterial()
        nw20_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_697_kmsGenerateAndWrap_ = nw20_
        d_698_kmsWrap_: AwsKmsKeyring.KmsWrapKeyMaterial
        nw21_ = AwsKmsKeyring.KmsWrapKeyMaterial()
        nw21_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_698_kmsWrap_ = nw21_
        d_699_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_700_valueOrError1_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.WrapEdkMaterialOutput.default(AwsKmsKeyring.KmsWrapInfo.default()))()
        out107_: Wrappers.Result
        out107_ = EdkWrapping.default__.WrapEdkMaterial(d_693_materials_, d_698_kmsWrap_, d_697_kmsGenerateAndWrap_)
        d_700_valueOrError1_ = out107_
        if (d_700_valueOrError1_).IsFailure():
            output = (d_700_valueOrError1_).PropagateFailure()
            return output
        d_699_wrapOutput_ = (d_700_valueOrError1_).Extract()
        d_701_kmsKeyArn_: _dafny.Seq
        d_701_kmsKeyArn_ = ((d_699_wrapOutput_).wrapInfo).kmsKeyArn
        d_702_symmetricSigningKeyList_: Wrappers.Option
        d_702_symmetricSigningKeyList_ = (Wrappers.Option_Some(_dafny.Seq([((d_699_wrapOutput_).symmetricSigningKey).value])) if ((d_699_wrapOutput_).symmetricSigningKey).is_Some else Wrappers.Option_None())
        d_703_providerInfo_: _dafny.Seq
        d_704_valueOrError2_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_704_valueOrError2_ = (UTF8.default__.Encode(d_701_kmsKeyArn_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_704_valueOrError2_).IsFailure():
            output = (d_704_valueOrError2_).PropagateFailure()
            return output
        d_703_providerInfo_ = (d_704_valueOrError2_).Extract()
        d_705_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_705_valueOrError3_ = Wrappers.default__.Need((len(d_703_providerInfo_)) < (StandardLibrary_UInt.default__.UINT16__LIMIT), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS GenerateDataKey: Key ID too long.")))
        if (d_705_valueOrError3_).IsFailure():
            output = (d_705_valueOrError3_).PropagateFailure()
            return output
        d_706_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_706_edk_ = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey(Constants.default__.PROVIDER__ID, d_703_providerInfo_, (d_699_wrapOutput_).wrappedMaterial)
        if (d_699_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_707_result_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            d_708_valueOrError4_: Wrappers.Result = None
            d_708_valueOrError4_ = Materials.default__.EncryptionMaterialAddDataKey(d_693_materials_, (d_699_wrapOutput_).plaintextDataKey, _dafny.Seq([d_706_edk_]), d_702_symmetricSigningKeyList_)
            if (d_708_valueOrError4_).IsFailure():
                output = (d_708_valueOrError4_).PropagateFailure()
                return output
            d_707_result_ = (d_708_valueOrError4_).Extract()
            output = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_707_result_))
            return output
        elif (d_699_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_709_result_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            d_710_valueOrError5_: Wrappers.Result = None
            d_710_valueOrError5_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys(d_693_materials_, _dafny.Seq([d_706_edk_]), d_702_symmetricSigningKeyList_)
            if (d_710_valueOrError5_).IsFailure():
                output = (d_710_valueOrError5_).PropagateFailure()
                return output
            d_709_result_ = (d_710_valueOrError5_).Extract()
            output = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_709_result_))
            return output
        return output

    def OnDecrypt_k(self, input):
        output: Wrappers.Result = None
        d_711_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_711_materials_ = (input).materials
        d_712_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_712_suite_ = ((input).materials).algorithmSuite
        d_713_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_713_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_711_materials_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_713_valueOrError0_).IsFailure():
            output = (d_713_valueOrError0_).PropagateFailure()
            return output
        d_714_filter_: AwsKmsUtils.OnDecryptMrkAwareEncryptedDataKeyFilter
        nw22_ = AwsKmsUtils.OnDecryptMrkAwareEncryptedDataKeyFilter()
        nw22_.ctor__((self).awsKmsArn, Constants.default__.PROVIDER__ID)
        d_714_filter_ = nw22_
        d_715_edksToAttempt_: _dafny.Seq
        d_716_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out108_: Wrappers.Result
        out108_ = Actions.default__.FilterWithResult(d_714_filter_, (input).encryptedDataKeys)
        d_716_valueOrError1_ = out108_
        if (d_716_valueOrError1_).IsFailure():
            output = (d_716_valueOrError1_).PropagateFailure()
            return output
        d_715_edksToAttempt_ = (d_716_valueOrError1_).Extract()
        d_717_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_717_valueOrError2_ = Wrappers.default__.Need((0) < (len(d_715_edksToAttempt_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to decrypt data key: No Encrypted Data Keys found to match.")))
        if (d_717_valueOrError2_).IsFailure():
            output = (d_717_valueOrError2_).PropagateFailure()
            return output
        d_718_decryptClosure_: DecryptSingleEncryptedDataKey
        nw23_ = DecryptSingleEncryptedDataKey()
        nw23_.ctor__(d_711_materials_, (self).client, (self).awsKmsKey, (self).grantTokens)
        d_718_decryptClosure_ = nw23_
        d_719_outcome_: Wrappers.Result
        out109_: Wrappers.Result
        out109_ = Actions.default__.ReduceToSuccess(d_718_decryptClosure_, d_715_edksToAttempt_)
        d_719_outcome_ = out109_
        d_720_SealedDecryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_721_valueOrError3_: Wrappers.Result = None
        def lambda64_(d_722_errors_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_CollectionOfErrors(d_722_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."))

        d_721_valueOrError3_ = (d_719_outcome_).MapFailure(lambda64_)
        if (d_721_valueOrError3_).IsFailure():
            output = (d_721_valueOrError3_).PropagateFailure()
            return output
        d_720_SealedDecryptionMaterials_ = (d_721_valueOrError3_).Extract()
        output = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput_OnDecryptOutput(d_720_SealedDecryptionMaterials_))
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
        d_723_kmsUnwrap_: AwsKmsKeyring.KmsUnwrapKeyMaterial
        nw24_ = AwsKmsKeyring.KmsUnwrapKeyMaterial()
        nw24_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_723_kmsUnwrap_ = nw24_
        d_724_unwrapOutputRes_: Wrappers.Result
        out110_: Wrappers.Result
        out110_ = EdkWrapping.default__.UnwrapEdkMaterial((edk).ciphertext, (self).materials, d_723_kmsUnwrap_)
        d_724_unwrapOutputRes_ = out110_
        d_725_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_726_valueOrError0_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.UnwrapEdkMaterialOutput.default(AwsKmsKeyring.KmsUnwrapInfo.default()))()
        d_726_valueOrError0_ = d_724_unwrapOutputRes_
        if (d_726_valueOrError0_).IsFailure():
            res = (d_726_valueOrError0_).PropagateFailure()
            return res
        d_725_unwrapOutput_ = (d_726_valueOrError0_).Extract()
        d_727_result_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_728_valueOrError1_: Wrappers.Result = None
        d_728_valueOrError1_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_725_unwrapOutput_).plaintextDataKey, (d_725_unwrapOutput_).symmetricSigningKey)
        if (d_728_valueOrError1_).IsFailure():
            res = (d_728_valueOrError1_).PropagateFailure()
            return res
        d_727_result_ = (d_728_valueOrError1_).Extract()
        res = Wrappers.Result_Success(d_727_result_)
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
