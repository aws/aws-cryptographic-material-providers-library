import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_MergeSort
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
import StandardLibrary_UInt
import StandardLibrary_String
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
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsArnParsing
import AwsKmsMrkAreUnique
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
import Constants
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
import software_amazon_cryptography_services_kms_internaldafny
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
        out112_: Wrappers.Result
        out112_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnEncrypt(self, input)
        return out112_

    def OnDecrypt(self, input):
        out113_: Wrappers.Result
        out113_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnDecrypt(self, input)
        return out113_

    def ctor__(self, client, awsKmsKey, grantTokens):
        d_609_parsedAwsKmsId_: Wrappers.Result
        d_609_parsedAwsKmsId_ = AwsArnParsing.default__.ParseAwsKmsIdentifier(awsKmsKey)
        (self)._client = client
        (self)._awsKmsKey = awsKmsKey
        (self)._awsKmsArn = (d_609_parsedAwsKmsId_).value
        (self)._grantTokens = grantTokens

    def OnEncrypt_k(self, input):
        output: Wrappers.Result = None
        d_610_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_610_materials_ = (input).materials
        d_611_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_611_suite_ = ((input).materials).algorithmSuite
        d_612_stringifiedEncCtx_: _dafny.Map
        d_613_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Map)()
        d_613_valueOrError0_ = AwsKmsUtils.default__.StringifyEncryptionContext(((input).materials).encryptionContext)
        if (d_613_valueOrError0_).IsFailure():
            output = (d_613_valueOrError0_).PropagateFailure()
            return output
        d_612_stringifiedEncCtx_ = (d_613_valueOrError0_).Extract()
        d_614_kmsGenerateAndWrap_: AwsKmsKeyring.KmsGenerateAndWrapKeyMaterial
        nw20_ = AwsKmsKeyring.KmsGenerateAndWrapKeyMaterial()
        nw20_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_614_kmsGenerateAndWrap_ = nw20_
        d_615_kmsWrap_: AwsKmsKeyring.KmsWrapKeyMaterial
        nw21_ = AwsKmsKeyring.KmsWrapKeyMaterial()
        nw21_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_615_kmsWrap_ = nw21_
        d_616_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_617_valueOrError1_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.WrapEdkMaterialOutput.default(AwsKmsKeyring.KmsWrapInfo.default()))()
        out114_: Wrappers.Result
        out114_ = EdkWrapping.default__.WrapEdkMaterial(d_610_materials_, d_615_kmsWrap_, d_614_kmsGenerateAndWrap_)
        d_617_valueOrError1_ = out114_
        if (d_617_valueOrError1_).IsFailure():
            output = (d_617_valueOrError1_).PropagateFailure()
            return output
        d_616_wrapOutput_ = (d_617_valueOrError1_).Extract()
        d_618_kmsKeyArn_: _dafny.Seq
        d_618_kmsKeyArn_ = ((d_616_wrapOutput_).wrapInfo).kmsKeyArn
        d_619_symmetricSigningKeyList_: Wrappers.Option
        d_619_symmetricSigningKeyList_ = (Wrappers.Option_Some(_dafny.Seq([((d_616_wrapOutput_).symmetricSigningKey).value])) if ((d_616_wrapOutput_).symmetricSigningKey).is_Some else Wrappers.Option_None())
        d_620_providerInfo_: _dafny.Seq
        d_621_valueOrError2_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_621_valueOrError2_ = (UTF8.default__.Encode(d_618_kmsKeyArn_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_621_valueOrError2_).IsFailure():
            output = (d_621_valueOrError2_).PropagateFailure()
            return output
        d_620_providerInfo_ = (d_621_valueOrError2_).Extract()
        d_622_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_622_valueOrError3_ = Wrappers.default__.Need((len(d_620_providerInfo_)) < (StandardLibrary_UInt.default__.UINT16__LIMIT), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS GenerateDataKey: Key ID too long.")))
        if (d_622_valueOrError3_).IsFailure():
            output = (d_622_valueOrError3_).PropagateFailure()
            return output
        d_623_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_623_edk_ = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey(Constants.default__.PROVIDER__ID, d_620_providerInfo_, (d_616_wrapOutput_).wrappedMaterial)
        if (d_616_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_624_result_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            d_625_valueOrError4_: Wrappers.Result = None
            d_625_valueOrError4_ = Materials.default__.EncryptionMaterialAddDataKey(d_610_materials_, (d_616_wrapOutput_).plaintextDataKey, _dafny.Seq([d_623_edk_]), d_619_symmetricSigningKeyList_)
            if (d_625_valueOrError4_).IsFailure():
                output = (d_625_valueOrError4_).PropagateFailure()
                return output
            d_624_result_ = (d_625_valueOrError4_).Extract()
            output = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_624_result_))
            return output
        elif (d_616_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_626_result_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            d_627_valueOrError5_: Wrappers.Result = None
            d_627_valueOrError5_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys(d_610_materials_, _dafny.Seq([d_623_edk_]), d_619_symmetricSigningKeyList_)
            if (d_627_valueOrError5_).IsFailure():
                output = (d_627_valueOrError5_).PropagateFailure()
                return output
            d_626_result_ = (d_627_valueOrError5_).Extract()
            output = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_626_result_))
            return output
        return output

    def OnDecrypt_k(self, input):
        output: Wrappers.Result = None
        d_628_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_628_materials_ = (input).materials
        d_629_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_629_suite_ = ((input).materials).algorithmSuite
        d_630_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_630_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_628_materials_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_630_valueOrError0_).IsFailure():
            output = (d_630_valueOrError0_).PropagateFailure()
            return output
        d_631_filter_: AwsKmsUtils.OnDecryptMrkAwareEncryptedDataKeyFilter
        nw22_ = AwsKmsUtils.OnDecryptMrkAwareEncryptedDataKeyFilter()
        nw22_.ctor__((self).awsKmsArn, Constants.default__.PROVIDER__ID)
        d_631_filter_ = nw22_
        d_632_edksToAttempt_: _dafny.Seq
        d_633_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out115_: Wrappers.Result
        out115_ = Actions.default__.FilterWithResult(d_631_filter_, (input).encryptedDataKeys)
        d_633_valueOrError1_ = out115_
        if (d_633_valueOrError1_).IsFailure():
            output = (d_633_valueOrError1_).PropagateFailure()
            return output
        d_632_edksToAttempt_ = (d_633_valueOrError1_).Extract()
        d_634_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_634_valueOrError2_ = Wrappers.default__.Need((0) < (len(d_632_edksToAttempt_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to decrypt data key: No Encrypted Data Keys found to match.")))
        if (d_634_valueOrError2_).IsFailure():
            output = (d_634_valueOrError2_).PropagateFailure()
            return output
        d_635_decryptClosure_: DecryptSingleEncryptedDataKey
        nw23_ = DecryptSingleEncryptedDataKey()
        nw23_.ctor__(d_628_materials_, (self).client, (self).awsKmsKey, (self).grantTokens)
        d_635_decryptClosure_ = nw23_
        d_636_outcome_: Wrappers.Result
        out116_: Wrappers.Result
        out116_ = Actions.default__.ReduceToSuccess(d_635_decryptClosure_, d_632_edksToAttempt_)
        d_636_outcome_ = out116_
        d_637_SealedDecryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_638_valueOrError3_: Wrappers.Result = None
        def lambda42_(d_639_errors_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_CollectionOfErrors(d_639_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."))

        d_638_valueOrError3_ = (d_636_outcome_).MapFailure(lambda42_)
        if (d_638_valueOrError3_).IsFailure():
            output = (d_638_valueOrError3_).PropagateFailure()
            return output
        d_637_SealedDecryptionMaterials_ = (d_638_valueOrError3_).Extract()
        output = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput_OnDecryptOutput(d_637_SealedDecryptionMaterials_))
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
        d_640_kmsUnwrap_: AwsKmsKeyring.KmsUnwrapKeyMaterial
        nw24_ = AwsKmsKeyring.KmsUnwrapKeyMaterial()
        nw24_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_640_kmsUnwrap_ = nw24_
        d_641_unwrapOutputRes_: Wrappers.Result
        out117_: Wrappers.Result
        out117_ = EdkWrapping.default__.UnwrapEdkMaterial((edk).ciphertext, (self).materials, d_640_kmsUnwrap_)
        d_641_unwrapOutputRes_ = out117_
        d_642_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_643_valueOrError0_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.UnwrapEdkMaterialOutput.default(AwsKmsKeyring.KmsUnwrapInfo.default()))()
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
