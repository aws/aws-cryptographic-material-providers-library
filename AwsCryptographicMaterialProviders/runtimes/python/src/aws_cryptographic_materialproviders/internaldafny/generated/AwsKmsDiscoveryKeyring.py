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

# Module: AwsKmsDiscoveryKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DiscoveryMatch(arn, discoveryFilter):
        pat_let_tv155_ = arn
        pat_let_tv156_ = arn
        def lambda58_(source22_):
            if source22_.is_None:
                return True
            elif True:
                d_601___mcc_h0_ = source22_.value
                d_602_filter_ = d_601___mcc_h0_
                return (((d_602_filter_).partition) == ((pat_let_tv155_).partition)) and (((d_602_filter_).accountIds) <= (_dafny.Seq([(pat_let_tv156_).account])))

        return (True) and (lambda58_(discoveryFilter))


class AwsKmsDiscoveryKeyring(Keyring.VerifiableInterface, software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring):
    def  __init__(self):
        self._client: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient = None
        self._discoveryFilter: Wrappers.Option = Wrappers.Option.default()()
        self._grantTokens: _dafny.Seq = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsDiscoveryKeyring.AwsKmsDiscoveryKeyring"
    def OnEncrypt(self, input):
        out92_: Wrappers.Result
        out92_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnEncrypt(self, input)
        return out92_

    def OnDecrypt(self, input):
        out93_: Wrappers.Result
        out93_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnDecrypt(self, input)
        return out93_

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
        d_603_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_603_materials_ = (input).materials
        d_604_encryptedDataKeys_: _dafny.Seq
        d_604_encryptedDataKeys_ = (input).encryptedDataKeys
        d_605_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_605_suite_ = ((input).materials).algorithmSuite
        d_606_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_606_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_603_materials_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_606_valueOrError0_).IsFailure():
            res = (d_606_valueOrError0_).PropagateFailure()
            return res
        d_607_edkFilter_: AwsKmsEncryptedDataKeyFilter
        nw9_ = AwsKmsEncryptedDataKeyFilter()
        nw9_.ctor__((self).discoveryFilter)
        d_607_edkFilter_ = nw9_
        d_608_matchingEdks_: _dafny.Seq
        d_609_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out94_: Wrappers.Result
        out94_ = Actions.default__.FilterWithResult(d_607_edkFilter_, d_604_encryptedDataKeys_)
        d_609_valueOrError1_ = out94_
        if (d_609_valueOrError1_).IsFailure():
            res = (d_609_valueOrError1_).PropagateFailure()
            return res
        d_608_matchingEdks_ = (d_609_valueOrError1_).Extract()
        d_610_edkTransform_: AwsKmsEncryptedDataKeyTransformer
        nw10_ = AwsKmsEncryptedDataKeyTransformer()
        nw10_.ctor__()
        d_610_edkTransform_ = nw10_
        d_611_edksToAttempt_: _dafny.Seq
        d_612_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out95_: Wrappers.Result
        out95_ = Actions.default__.DeterministicFlatMapWithResult(d_610_edkTransform_, d_608_matchingEdks_)
        d_612_valueOrError2_ = out95_
        if (d_612_valueOrError2_).IsFailure():
            res = (d_612_valueOrError2_).PropagateFailure()
            return res
        d_611_edksToAttempt_ = (d_612_valueOrError2_).Extract()
        d_613_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_613_valueOrError3_ = Wrappers.default__.Need((0) < (len(d_611_edksToAttempt_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to decrypt data key: No Encrypted Data Keys found to match.")))
        if (d_613_valueOrError3_).IsFailure():
            res = (d_613_valueOrError3_).PropagateFailure()
            return res
        d_614_decryptAction_: AwsKmsEncryptedDataKeyDecryptor
        nw11_ = AwsKmsEncryptedDataKeyDecryptor()
        nw11_.ctor__(d_603_materials_, (self).client, (self).grantTokens)
        d_614_decryptAction_ = nw11_
        d_615_outcome_: Wrappers.Result
        out96_: Wrappers.Result
        out96_ = Actions.default__.ReduceToSuccess(d_614_decryptAction_, d_611_edksToAttempt_)
        d_615_outcome_ = out96_
        def lambda59_(source23_):
            if source23_.is_Success:
                d_616___mcc_h0_ = source23_.value
                d_617_mat_ = d_616___mcc_h0_
                return Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput_OnDecryptOutput(d_617_mat_))
            elif True:
                d_618___mcc_h1_ = source23_.error
                d_619_errors_ = d_618___mcc_h1_
                return Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_CollectionOfErrors(d_619_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`.")))

        res = lambda59_(d_615_outcome_)
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
        self._discoveryFilter: Wrappers.Option = Wrappers.Option.default()()
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsDiscoveryKeyring.AwsKmsEncryptedDataKeyFilter"
    def ctor__(self, discoveryFilter):
        (self)._discoveryFilter = discoveryFilter

    def Invoke(self, edk):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        d_620_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_620_valueOrError0_ = Wrappers.default__.Need(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid AWS KMS encoding, provider info is not UTF8.")))
        if (d_620_valueOrError0_).IsFailure():
            output = (d_620_valueOrError0_).PropagateFailure()
            return output
        d_621_keyId_: _dafny.Seq
        d_622_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_622_valueOrError1_ = (UTF8.default__.Decode((edk).keyProviderInfo)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_622_valueOrError1_).IsFailure():
            output = (d_622_valueOrError1_).PropagateFailure()
            return output
        d_621_keyId_ = (d_622_valueOrError1_).Extract()
        d_623_arn_: AwsArnParsing.AwsArn
        d_624_valueOrError2_: Wrappers.Result = None
        d_624_valueOrError2_ = (AwsArnParsing.default__.ParseAwsKmsArn(d_621_keyId_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_624_valueOrError2_).IsFailure():
            output = (d_624_valueOrError2_).PropagateFailure()
            return output
        d_623_arn_ = (d_624_valueOrError2_).Extract()
        d_625_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_625_valueOrError3_ = Wrappers.default__.Need((((d_623_arn_).resource).resourceType) == (_dafny.Seq("key")), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Only AWS KMS Keys supported")))
        if (d_625_valueOrError3_).IsFailure():
            output = (d_625_valueOrError3_).PropagateFailure()
            return output
        if ((edk).keyProviderId) != (Constants.default__.PROVIDER__ID):
            output = Wrappers.Result_Success(False)
            return output
        if not(default__.DiscoveryMatch(d_623_arn_, (self).discoveryFilter)):
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
        res: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_626_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_626_valueOrError0_ = Wrappers.default__.Need(((edk).keyProviderId) == (Constants.default__.PROVIDER__ID), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encrypted data key was not generated by KMS")))
        if (d_626_valueOrError0_).IsFailure():
            res = (d_626_valueOrError0_).PropagateFailure()
            return res
        d_627_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_627_valueOrError1_ = Wrappers.default__.Need(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid AWS KMS encoding, provider info is not UTF8.")))
        if (d_627_valueOrError1_).IsFailure():
            res = (d_627_valueOrError1_).PropagateFailure()
            return res
        d_628_keyId_: _dafny.Seq
        d_629_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_629_valueOrError2_ = (UTF8.default__.Decode((edk).keyProviderInfo)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_629_valueOrError2_).IsFailure():
            res = (d_629_valueOrError2_).PropagateFailure()
            return res
        d_628_keyId_ = (d_629_valueOrError2_).Extract()
        d_630_arn_: AwsArnParsing.AwsArn
        d_631_valueOrError3_: Wrappers.Result = None
        d_631_valueOrError3_ = (AwsArnParsing.default__.ParseAwsKmsArn(d_628_keyId_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_631_valueOrError3_).IsFailure():
            res = (d_631_valueOrError3_).PropagateFailure()
            return res
        d_630_arn_ = (d_631_valueOrError3_).Extract()
        res = Wrappers.Result_Success(_dafny.Seq([Constants.AwsKmsEdkHelper_AwsKmsEdkHelper(edk, d_630_arn_)]))
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
        d_632_awsKmsKey_: _dafny.Seq
        d_632_awsKmsKey_ = ((helper).arn).ToString()
        d_633___v0_: tuple
        d_634_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_634_valueOrError0_ = AwsKmsUtils.default__.ValidateKmsKeyId(((helper).arn).ToString())
        if (d_634_valueOrError0_).IsFailure():
            res = (d_634_valueOrError0_).PropagateFailure()
            return res
        d_633___v0_ = (d_634_valueOrError0_).Extract()
        d_635_kmsUnwrap_: AwsKmsKeyring.KmsUnwrapKeyMaterial
        nw12_ = AwsKmsKeyring.KmsUnwrapKeyMaterial()
        nw12_.ctor__((self).client, d_632_awsKmsKey_, (self).grantTokens)
        d_635_kmsUnwrap_ = nw12_
        d_636_unwrapOutputRes_: Wrappers.Result
        out97_: Wrappers.Result
        out97_ = EdkWrapping.default__.UnwrapEdkMaterial(((helper).edk).ciphertext, (self).materials, d_635_kmsUnwrap_)
        d_636_unwrapOutputRes_ = out97_
        d_637_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_638_valueOrError1_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.UnwrapEdkMaterialOutput.default(AwsKmsKeyring.KmsUnwrapInfo.default()))()
        d_638_valueOrError1_ = d_636_unwrapOutputRes_
        if (d_638_valueOrError1_).IsFailure():
            res = (d_638_valueOrError1_).PropagateFailure()
            return res
        d_637_unwrapOutput_ = (d_638_valueOrError1_).Extract()
        d_639_result_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_640_valueOrError2_: Wrappers.Result = None
        d_640_valueOrError2_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_637_unwrapOutput_).plaintextDataKey, (d_637_unwrapOutput_).symmetricSigningKey)
        if (d_640_valueOrError2_).IsFailure():
            res = (d_640_valueOrError2_).PropagateFailure()
            return res
        d_639_result_ = (d_640_valueOrError2_).Extract()
        res = Wrappers.Result_Success(d_639_result_)
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
