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

assert "AwsKmsDiscoveryKeyring" == __name__
AwsKmsDiscoveryKeyring = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DiscoveryMatch(arn, discoveryFilter):
        pat_let_tv31_ = arn
        pat_let_tv32_ = arn
        def lambda59_(source26_):
            if source26_.is_None:
                return True
            elif True:
                d_906___mcc_h0_ = source26_.value
                def iife38_(_pat_let13_0):
                    def iife39_(d_907_filter_):
                        return (((d_907_filter_).partition) == ((pat_let_tv31_).partition)) and (((d_907_filter_).accountIds) <= (_dafny.Seq([(pat_let_tv32_).account])))
                    return iife39_(_pat_let13_0)
                return iife38_(d_906___mcc_h0_)

        return (True) and (lambda59_(discoveryFilter))


class AwsKmsDiscoveryKeyring(Keyring.VerifiableInterface, software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring):
    def  __init__(self):
        self._client: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient = None
        self._discoveryFilter: Wrappers.Option = Wrappers.Option_None.default()()
        self._grantTokens: _dafny.Seq = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsDiscoveryKeyring.AwsKmsDiscoveryKeyring"
    def OnEncrypt(self, input):
        out220_: Wrappers.Result
        out220_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnEncrypt(self, input)
        return out220_

    def OnDecrypt(self, input):
        out221_: Wrappers.Result
        out221_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnDecrypt(self, input)
        return out221_

    def ctor__(self, client, discoveryFilter, grantTokens):
        (self)._client = client
        (self)._discoveryFilter = discoveryFilter
        (self)._grantTokens = grantTokens

    def OnEncrypt_k(self, input):
        output: Wrappers.Result = None
        output = Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption is not supported with a Discovery Keyring.")))
        return output
        return output

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_908_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_908_materials_ = (input).materials
        d_909_encryptedDataKeys_: _dafny.Seq
        d_909_encryptedDataKeys_ = (input).encryptedDataKeys
        d_910_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_910_suite_ = ((input).materials).algorithmSuite
        d_911_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_911_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_908_materials_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_911_valueOrError0_).IsFailure():
            res = (d_911_valueOrError0_).PropagateFailure()
            return res
        d_912_edkFilter_: AwsKmsDiscoveryKeyring.AwsKmsEncryptedDataKeyFilter
        nw10_ = AwsKmsDiscoveryKeyring.AwsKmsEncryptedDataKeyFilter()
        nw10_.ctor__((self).discoveryFilter)
        d_912_edkFilter_ = nw10_
        d_913_matchingEdks_: _dafny.Seq
        d_914_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out222_: Wrappers.Result
        out222_ = Actions.default__.FilterWithResult(d_912_edkFilter_, d_909_encryptedDataKeys_)
        d_914_valueOrError1_ = out222_
        if (d_914_valueOrError1_).IsFailure():
            res = (d_914_valueOrError1_).PropagateFailure()
            return res
        d_913_matchingEdks_ = (d_914_valueOrError1_).Extract()
        d_915_edkTransform_: AwsKmsDiscoveryKeyring.AwsKmsEncryptedDataKeyTransformer
        nw11_ = AwsKmsDiscoveryKeyring.AwsKmsEncryptedDataKeyTransformer()
        nw11_.ctor__()
        d_915_edkTransform_ = nw11_
        d_916_edksToAttempt_: _dafny.Seq
        d_917_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out223_: Wrappers.Result
        out223_ = Actions.default__.DeterministicFlatMapWithResult(d_915_edkTransform_, d_913_matchingEdks_)
        d_917_valueOrError2_ = out223_
        if (d_917_valueOrError2_).IsFailure():
            res = (d_917_valueOrError2_).PropagateFailure()
            return res
        d_916_edksToAttempt_ = (d_917_valueOrError2_).Extract()
        d_918_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_918_valueOrError3_ = Wrappers.default__.Need((0) < (len(d_916_edksToAttempt_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to decrypt data key: No Encrypted Data Keys found to match.")))
        if (d_918_valueOrError3_).IsFailure():
            res = (d_918_valueOrError3_).PropagateFailure()
            return res
        d_919_decryptAction_: AwsKmsDiscoveryKeyring.AwsKmsEncryptedDataKeyDecryptor
        nw12_ = AwsKmsDiscoveryKeyring.AwsKmsEncryptedDataKeyDecryptor()
        nw12_.ctor__(d_908_materials_, (self).client, (self).grantTokens)
        d_919_decryptAction_ = nw12_
        d_920_outcome_: Wrappers.Result
        out224_: Wrappers.Result
        out224_ = Actions.default__.ReduceToSuccess(d_919_decryptAction_, d_916_edksToAttempt_)
        d_920_outcome_ = out224_
        def lambda60_(source27_):
            if source27_.is_Success:
                d_921___mcc_h0_ = source27_.value
                def iife40_(_pat_let14_0):
                    def iife41_(d_922_mat_):
                        return Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput_OnDecryptOutput(d_922_mat_))
                    return iife41_(_pat_let14_0)
                return iife40_(d_921___mcc_h0_)
            elif True:
                d_923___mcc_h1_ = source27_.error
                def iife42_(_pat_let15_0):
                    def iife43_(d_924_errors_):
                        return Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_CollectionOfErrors(d_924_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`.")))
                    return iife43_(_pat_let15_0)
                return iife42_(d_923___mcc_h1_)

        res = lambda60_(d_920_outcome_)
        return res
        return res

    @property
    def client(self):
        return self._client
    @property
    def discoveryFilter(self):
        return self._discoveryFilter
    @property
    def grantTokens(self):
        return self._grantTokens

class AwsKmsEncryptedDataKeyFilter(Actions.DeterministicActionWithResult, Actions.DeterministicAction):
    def  __init__(self):
        self._discoveryFilter: Wrappers.Option = Wrappers.Option_None.default()()
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsDiscoveryKeyring.AwsKmsEncryptedDataKeyFilter"
    def ctor__(self, discoveryFilter):
        (self)._discoveryFilter = discoveryFilter

    def Invoke(self, edk):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.bool)()
        d_925_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_925_valueOrError0_ = Wrappers.default__.Need(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid AWS KMS encoding, provider info is not UTF8.")))
        if (d_925_valueOrError0_).IsFailure():
            output = (d_925_valueOrError0_).PropagateFailure()
            return output
        d_926_keyId_: _dafny.Seq
        d_927_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_927_valueOrError1_ = (UTF8.default__.Decode((edk).keyProviderInfo)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_927_valueOrError1_).IsFailure():
            output = (d_927_valueOrError1_).PropagateFailure()
            return output
        d_926_keyId_ = (d_927_valueOrError1_).Extract()
        d_928_arn_: AwsArnParsing.AwsArn
        d_929_valueOrError2_: Wrappers.Result = None
        d_929_valueOrError2_ = (AwsArnParsing.default__.ParseAwsKmsArn(d_926_keyId_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_929_valueOrError2_).IsFailure():
            output = (d_929_valueOrError2_).PropagateFailure()
            return output
        d_928_arn_ = (d_929_valueOrError2_).Extract()
        d_930_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_930_valueOrError3_ = Wrappers.default__.Need((((d_928_arn_).resource).resourceType) == (_dafny.Seq("key")), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Only AWS KMS Keys supported")))
        if (d_930_valueOrError3_).IsFailure():
            output = (d_930_valueOrError3_).PropagateFailure()
            return output
        if ((edk).keyProviderId) != ((Constants.default__).PROVIDER__ID):
            output = Wrappers.Result_Success(False)
            return output
        if not(AwsKmsDiscoveryKeyring.default__.DiscoveryMatch(d_928_arn_, (self).discoveryFilter)):
            output = Wrappers.Result_Success(False)
            return output
        output = Wrappers.Result_Success(True)
        return output
        return output

    @property
    def discoveryFilter(self):
        return self._discoveryFilter

class AwsKmsEncryptedDataKeyTransformer(Actions.DeterministicActionWithResult, Actions.DeterministicAction):
    def  __init__(self):
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsDiscoveryKeyring.AwsKmsEncryptedDataKeyTransformer"
    def ctor__(self):
        pass
        pass

    def Invoke(self, edk):
        res: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_931_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_931_valueOrError0_ = Wrappers.default__.Need(((edk).keyProviderId) == ((Constants.default__).PROVIDER__ID), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encrypted data key was not generated by KMS")))
        if (d_931_valueOrError0_).IsFailure():
            res = (d_931_valueOrError0_).PropagateFailure()
            return res
        d_932_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_932_valueOrError1_ = Wrappers.default__.Need(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid AWS KMS encoding, provider info is not UTF8.")))
        if (d_932_valueOrError1_).IsFailure():
            res = (d_932_valueOrError1_).PropagateFailure()
            return res
        d_933_keyId_: _dafny.Seq
        d_934_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_934_valueOrError2_ = (UTF8.default__.Decode((edk).keyProviderInfo)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_934_valueOrError2_).IsFailure():
            res = (d_934_valueOrError2_).PropagateFailure()
            return res
        d_933_keyId_ = (d_934_valueOrError2_).Extract()
        d_935_arn_: AwsArnParsing.AwsArn
        d_936_valueOrError3_: Wrappers.Result = None
        d_936_valueOrError3_ = (AwsArnParsing.default__.ParseAwsKmsArn(d_933_keyId_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_936_valueOrError3_).IsFailure():
            res = (d_936_valueOrError3_).PropagateFailure()
            return res
        d_935_arn_ = (d_936_valueOrError3_).Extract()
        res = Wrappers.Result_Success(_dafny.Seq([Constants.AwsKmsEdkHelper_AwsKmsEdkHelper(edk, d_935_arn_)]))
        return res
        return res


class AwsKmsEncryptedDataKeyDecryptor(Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._materials: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials = None
        self._client: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient = None
        self._grantTokens: _dafny.Seq = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsDiscoveryKeyring.AwsKmsEncryptedDataKeyDecryptor"
    def ctor__(self, materials, client, grantTokens):
        (self)._materials = materials
        (self)._client = client
        (self)._grantTokens = grantTokens

    def Invoke(self, helper):
        res: Wrappers.Result = None
        d_937_awsKmsKey_: _dafny.Seq
        d_937_awsKmsKey_ = ((helper).arn).ToString()
        d_938___v0_: tuple
        d_939_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        d_939_valueOrError0_ = AwsKmsUtils.default__.ValidateKmsKeyId(((helper).arn).ToString())
        if (d_939_valueOrError0_).IsFailure():
            res = (d_939_valueOrError0_).PropagateFailure()
            return res
        d_938___v0_ = (d_939_valueOrError0_).Extract()
        d_940_kmsUnwrap_: AwsKmsKeyring.KmsUnwrapKeyMaterial
        nw13_ = AwsKmsKeyring.KmsUnwrapKeyMaterial()
        nw13_.ctor__((self).client, d_937_awsKmsKey_, (self).grantTokens)
        d_940_kmsUnwrap_ = nw13_
        d_941_unwrapOutputRes_: Wrappers.Result
        out225_: Wrappers.Result
        out225_ = EdkWrapping.default__.UnwrapEdkMaterial(((helper).edk).ciphertext, (self).materials, d_940_kmsUnwrap_)
        d_941_unwrapOutputRes_ = out225_
        d_942_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_943_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(EdkWrapping.UnwrapEdkMaterialOutput.default(AwsKmsKeyring.KmsUnwrapInfo.default()))()
        d_943_valueOrError1_ = d_941_unwrapOutputRes_
        if (d_943_valueOrError1_).IsFailure():
            res = (d_943_valueOrError1_).PropagateFailure()
            return res
        d_942_unwrapOutput_ = (d_943_valueOrError1_).Extract()
        d_944_result_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_945_valueOrError2_: Wrappers.Result = None
        d_945_valueOrError2_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_942_unwrapOutput_).plaintextDataKey, (d_942_unwrapOutput_).symmetricSigningKey)
        if (d_945_valueOrError2_).IsFailure():
            res = (d_945_valueOrError2_).PropagateFailure()
            return res
        d_944_result_ = (d_945_valueOrError2_).Extract()
        res = Wrappers.Result_Success(d_944_result_)
        return res
        return res

    @property
    def materials(self):
        return self._materials
    @property
    def client(self):
        return self._client
    @property
    def grantTokens(self):
        return self._grantTokens
