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
import AwsKmsKeyring
import StrictMultiKeyring
import AwsKmsDiscoveryKeyring
import DiscoveryMultiKeyring
import AwsKmsMrkDiscoveryKeyring
import MrkAwareDiscoveryMultiKeyring

# assert "AwsKmsMrkKeyring" == __name__
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
        out233_: Wrappers.Result
        out233_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnEncrypt(self, input)
        return out233_

    def OnDecrypt(self, input):
        out234_: Wrappers.Result
        out234_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnDecrypt(self, input)
        return out234_

    def ctor__(self, client, awsKmsKey, grantTokens):
        d_995_parsedAwsKmsId_: Wrappers.Result
        d_995_parsedAwsKmsId_ = AwsArnParsing.default__.ParseAwsKmsIdentifier(awsKmsKey)
        (self)._client = client
        (self)._awsKmsKey = awsKmsKey
        (self)._awsKmsArn = (d_995_parsedAwsKmsId_).value
        (self)._grantTokens = grantTokens

    def OnEncrypt_k(self, input):
        output: Wrappers.Result = None
        d_996_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_996_materials_ = (input).materials
        d_997_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_997_suite_ = ((input).materials).algorithmSuite
        d_998_stringifiedEncCtx_: _dafny.Map
        d_999_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Map)()
        d_999_valueOrError0_ = AwsKmsUtils.default__.StringifyEncryptionContext(((input).materials).encryptionContext)
        if (d_999_valueOrError0_).IsFailure():
            output = (d_999_valueOrError0_).PropagateFailure()
            return output
        d_998_stringifiedEncCtx_ = (d_999_valueOrError0_).Extract()
        d_1000_kmsGenerateAndWrap_: AwsKmsKeyring.KmsGenerateAndWrapKeyMaterial
        nw21_ = AwsKmsKeyring.KmsGenerateAndWrapKeyMaterial()
        nw21_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_1000_kmsGenerateAndWrap_ = nw21_
        d_1001_kmsWrap_: AwsKmsKeyring.KmsWrapKeyMaterial
        nw22_ = AwsKmsKeyring.KmsWrapKeyMaterial()
        nw22_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_1001_kmsWrap_ = nw22_
        d_1002_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_1003_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(EdkWrapping.WrapEdkMaterialOutput.default(AwsKmsKeyring.KmsWrapInfo.default()))()
        out235_: Wrappers.Result
        out235_ = EdkWrapping.default__.WrapEdkMaterial(d_996_materials_, d_1001_kmsWrap_, d_1000_kmsGenerateAndWrap_)
        d_1003_valueOrError1_ = out235_
        if (d_1003_valueOrError1_).IsFailure():
            output = (d_1003_valueOrError1_).PropagateFailure()
            return output
        d_1002_wrapOutput_ = (d_1003_valueOrError1_).Extract()
        d_1004_kmsKeyArn_: _dafny.Seq
        d_1004_kmsKeyArn_ = ((d_1002_wrapOutput_).wrapInfo).kmsKeyArn
        d_1005_symmetricSigningKeyList_: Wrappers.Option
        d_1005_symmetricSigningKeyList_ = (Wrappers.Option_Some(_dafny.Seq([((d_1002_wrapOutput_).symmetricSigningKey).value])) if ((d_1002_wrapOutput_).symmetricSigningKey).is_Some else Wrappers.Option_None())
        d_1006_providerInfo_: _dafny.Seq
        d_1007_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_1007_valueOrError2_ = (UTF8.default__.Encode(d_1004_kmsKeyArn_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_1007_valueOrError2_).IsFailure():
            output = (d_1007_valueOrError2_).PropagateFailure()
            return output
        d_1006_providerInfo_ = (d_1007_valueOrError2_).Extract()
        d_1008_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1008_valueOrError3_ = Wrappers.default__.Need((len(d_1006_providerInfo_)) < ((StandardLibrary_mUInt.default__).UINT16__LIMIT), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid response from AWS KMS GenerateDataKey: Key ID too long.")))
        if (d_1008_valueOrError3_).IsFailure():
            output = (d_1008_valueOrError3_).PropagateFailure()
            return output
        d_1009_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_1009_edk_ = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey((Constants.default__).PROVIDER__ID, d_1006_providerInfo_, (d_1002_wrapOutput_).wrappedMaterial)
        if (d_1002_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_1010_result_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            d_1011_valueOrError4_: Wrappers.Result = None
            d_1011_valueOrError4_ = Materials.default__.EncryptionMaterialAddDataKey(d_996_materials_, (d_1002_wrapOutput_).plaintextDataKey, _dafny.Seq([d_1009_edk_]), d_1005_symmetricSigningKeyList_)
            if (d_1011_valueOrError4_).IsFailure():
                output = (d_1011_valueOrError4_).PropagateFailure()
                return output
            d_1010_result_ = (d_1011_valueOrError4_).Extract()
            output = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_1010_result_))
            return output
        elif (d_1002_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_1012_result_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            d_1013_valueOrError5_: Wrappers.Result = None
            d_1013_valueOrError5_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys(d_996_materials_, _dafny.Seq([d_1009_edk_]), d_1005_symmetricSigningKeyList_)
            if (d_1013_valueOrError5_).IsFailure():
                output = (d_1013_valueOrError5_).PropagateFailure()
                return output
            d_1012_result_ = (d_1013_valueOrError5_).Extract()
            output = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_1012_result_))
            return output
        return output

    def OnDecrypt_k(self, input):
        output: Wrappers.Result = None
        d_1014_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1014_materials_ = (input).materials
        d_1015_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_1015_suite_ = ((input).materials).algorithmSuite
        d_1016_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1016_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_1014_materials_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_1016_valueOrError0_).IsFailure():
            output = (d_1016_valueOrError0_).PropagateFailure()
            return output
        d_1017_filter_: AwsKmsUtils.OnDecryptMrkAwareEncryptedDataKeyFilter
        nw23_ = AwsKmsUtils.OnDecryptMrkAwareEncryptedDataKeyFilter()
        nw23_.ctor__((self).awsKmsArn, (Constants.default__).PROVIDER__ID)
        d_1017_filter_ = nw23_
        d_1018_edksToAttempt_: _dafny.Seq
        d_1019_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out236_: Wrappers.Result
        out236_ = Actions.default__.FilterWithResult(d_1017_filter_, (input).encryptedDataKeys)
        d_1019_valueOrError1_ = out236_
        if (d_1019_valueOrError1_).IsFailure():
            output = (d_1019_valueOrError1_).PropagateFailure()
            return output
        d_1018_edksToAttempt_ = (d_1019_valueOrError1_).Extract()
        d_1020_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1020_valueOrError2_ = Wrappers.default__.Need((0) < (len(d_1018_edksToAttempt_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to decrypt data key: No Encrypted Data Keys found to match.")))
        if (d_1020_valueOrError2_).IsFailure():
            output = (d_1020_valueOrError2_).PropagateFailure()
            return output
        d_1021_decryptClosure_: AwsKmsMrkKeyring.DecryptSingleEncryptedDataKey
        nw24_ = AwsKmsMrkKeyring.DecryptSingleEncryptedDataKey()
        nw24_.ctor__(d_1014_materials_, (self).client, (self).awsKmsKey, (self).grantTokens)
        d_1021_decryptClosure_ = nw24_
        d_1022_outcome_: Wrappers.Result
        out237_: Wrappers.Result
        out237_ = Actions.default__.ReduceToSuccess(d_1021_decryptClosure_, d_1018_edksToAttempt_)
        d_1022_outcome_ = out237_
        d_1023_SealedDecryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1024_valueOrError3_: Wrappers.Result = None
        def lambda65_(d_1025_errors_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_CollectionOfErrors(d_1025_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."))

        d_1024_valueOrError3_ = (d_1022_outcome_).MapFailure(lambda65_)
        if (d_1024_valueOrError3_).IsFailure():
            output = (d_1024_valueOrError3_).PropagateFailure()
            return output
        d_1023_SealedDecryptionMaterials_ = (d_1024_valueOrError3_).Extract()
        output = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput_OnDecryptOutput(d_1023_SealedDecryptionMaterials_))
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
        d_1026_kmsUnwrap_: AwsKmsKeyring.KmsUnwrapKeyMaterial
        nw25_ = AwsKmsKeyring.KmsUnwrapKeyMaterial()
        nw25_.ctor__((self).client, (self).awsKmsKey, (self).grantTokens)
        d_1026_kmsUnwrap_ = nw25_
        d_1027_unwrapOutputRes_: Wrappers.Result
        out238_: Wrappers.Result
        out238_ = EdkWrapping.default__.UnwrapEdkMaterial((edk).ciphertext, (self).materials, d_1026_kmsUnwrap_)
        d_1027_unwrapOutputRes_ = out238_
        d_1028_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_1029_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(EdkWrapping.UnwrapEdkMaterialOutput.default(AwsKmsKeyring.KmsUnwrapInfo.default()))()
        d_1029_valueOrError0_ = d_1027_unwrapOutputRes_
        if (d_1029_valueOrError0_).IsFailure():
            res = (d_1029_valueOrError0_).PropagateFailure()
            return res
        d_1028_unwrapOutput_ = (d_1029_valueOrError0_).Extract()
        d_1030_result_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1031_valueOrError1_: Wrappers.Result = None
        d_1031_valueOrError1_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_1028_unwrapOutput_).plaintextDataKey, (d_1028_unwrapOutput_).symmetricSigningKey)
        if (d_1031_valueOrError1_).IsFailure():
            res = (d_1031_valueOrError1_).PropagateFailure()
            return res
        d_1030_result_ = (d_1031_valueOrError1_).Extract()
        res = Wrappers.Result_Success(d_1030_result_)
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
