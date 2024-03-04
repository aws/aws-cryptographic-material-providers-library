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
import software.amazon.cryptography.services.dynamodb.internaldafny.types
import software.amazon.cryptography.services.kms.internaldafny.types
import software.amazon.cryptography.primitives.internaldafny.types
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
import software.amazon.cryptography.keystore.internaldafny.types
import software.amazon.cryptography.materialproviders.internaldafny.types
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
                d_603___mcc_h0_ = source22_.value
                d_604_filter_ = d_603___mcc_h0_
                return (((d_604_filter_).partition) == ((pat_let_tv155_).partition)) and (((d_604_filter_).accountIds) <= (_dafny.Seq([(pat_let_tv156_).account])))

        return (True) and (lambda58_(discoveryFilter))


class AwsKmsDiscoveryKeyring(Keyring.VerifiableInterface, software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring):
    def  __init__(self):
        self._client: software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient = None
        self._discoveryFilter: Wrappers.Option = Wrappers.Option.default()()
        self._grantTokens: _dafny.Seq = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsDiscoveryKeyring.AwsKmsDiscoveryKeyring"
    def OnEncrypt(self, input):
        out92_: Wrappers.Result
        out92_ = software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.OnEncrypt(self, input)
        return out92_

    def OnDecrypt(self, input):
        out93_: Wrappers.Result
        out93_ = software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring.OnDecrypt(self, input)
        return out93_

    def ctor__(self, client, discoveryFilter, grantTokens):
        (self)._client = client
        (self)._discoveryFilter = discoveryFilter
        (self)._grantTokens = grantTokens

    def OnEncrypt_k(self, input):
        output: Wrappers.Result = None
        output = Wrappers.Result_Failure(software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption is not supported with a Discovery Keyring.")))
        return output
        return output

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_605_materials_: software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials
        d_605_materials_ = (input).materials
        d_606_encryptedDataKeys_: _dafny.Seq
        d_606_encryptedDataKeys_ = (input).encryptedDataKeys
        d_607_suite_: software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo
        d_607_suite_ = ((input).materials).algorithmSuite
        d_608_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_608_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_605_materials_), software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_608_valueOrError0_).IsFailure():
            res = (d_608_valueOrError0_).PropagateFailure()
            return res
        d_609_edkFilter_: AwsKmsEncryptedDataKeyFilter
        nw9_ = AwsKmsEncryptedDataKeyFilter()
        nw9_.ctor__((self).discoveryFilter)
        d_609_edkFilter_ = nw9_
        d_610_matchingEdks_: _dafny.Seq
        d_611_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out94_: Wrappers.Result
        out94_ = Actions.default__.FilterWithResult(d_609_edkFilter_, d_606_encryptedDataKeys_)
        d_611_valueOrError1_ = out94_
        if (d_611_valueOrError1_).IsFailure():
            res = (d_611_valueOrError1_).PropagateFailure()
            return res
        d_610_matchingEdks_ = (d_611_valueOrError1_).Extract()
        d_612_edkTransform_: AwsKmsEncryptedDataKeyTransformer
        nw10_ = AwsKmsEncryptedDataKeyTransformer()
        nw10_.ctor__()
        d_612_edkTransform_ = nw10_
        d_613_edksToAttempt_: _dafny.Seq
        d_614_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out95_: Wrappers.Result
        out95_ = Actions.default__.DeterministicFlatMapWithResult(d_612_edkTransform_, d_610_matchingEdks_)
        d_614_valueOrError2_ = out95_
        if (d_614_valueOrError2_).IsFailure():
            res = (d_614_valueOrError2_).PropagateFailure()
            return res
        d_613_edksToAttempt_ = (d_614_valueOrError2_).Extract()
        d_615_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_615_valueOrError3_ = Wrappers.default__.Need((0) < (len(d_613_edksToAttempt_)), software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to decrypt data key: No Encrypted Data Keys found to match.")))
        if (d_615_valueOrError3_).IsFailure():
            res = (d_615_valueOrError3_).PropagateFailure()
            return res
        d_616_decryptAction_: AwsKmsEncryptedDataKeyDecryptor
        nw11_ = AwsKmsEncryptedDataKeyDecryptor()
        nw11_.ctor__(d_605_materials_, (self).client, (self).grantTokens)
        d_616_decryptAction_ = nw11_
        d_617_outcome_: Wrappers.Result
        out96_: Wrappers.Result
        out96_ = Actions.default__.ReduceToSuccess(d_616_decryptAction_, d_613_edksToAttempt_)
        d_617_outcome_ = out96_
        def lambda59_(source23_):
            if source23_.is_Success:
                d_618___mcc_h0_ = source23_.value
                d_619_mat_ = d_618___mcc_h0_
                return Wrappers.Result_Success(software.amazon.cryptography.materialproviders.internaldafny.types.OnDecryptOutput_OnDecryptOutput(d_619_mat_))
            elif True:
                d_620___mcc_h1_ = source23_.error
                d_621_errors_ = d_620___mcc_h1_
                return Wrappers.Result_Failure(software.amazon.cryptography.materialproviders.internaldafny.types.Error_CollectionOfErrors(d_621_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`.")))

        res = lambda59_(d_617_outcome_)
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
        d_622_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_622_valueOrError0_ = Wrappers.default__.Need(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo), software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid AWS KMS encoding, provider info is not UTF8.")))
        if (d_622_valueOrError0_).IsFailure():
            output = (d_622_valueOrError0_).PropagateFailure()
            return output
        d_623_keyId_: _dafny.Seq
        d_624_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_624_valueOrError1_ = (UTF8.default__.Decode((edk).keyProviderInfo)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_624_valueOrError1_).IsFailure():
            output = (d_624_valueOrError1_).PropagateFailure()
            return output
        d_623_keyId_ = (d_624_valueOrError1_).Extract()
        d_625_arn_: AwsArnParsing.AwsArn
        d_626_valueOrError2_: Wrappers.Result = None
        d_626_valueOrError2_ = (AwsArnParsing.default__.ParseAwsKmsArn(d_623_keyId_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_626_valueOrError2_).IsFailure():
            output = (d_626_valueOrError2_).PropagateFailure()
            return output
        d_625_arn_ = (d_626_valueOrError2_).Extract()
        d_627_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_627_valueOrError3_ = Wrappers.default__.Need((((d_625_arn_).resource).resourceType) == (_dafny.Seq("key")), software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Only AWS KMS Keys supported")))
        if (d_627_valueOrError3_).IsFailure():
            output = (d_627_valueOrError3_).PropagateFailure()
            return output
        if ((edk).keyProviderId) != (Constants.default__.PROVIDER__ID):
            output = Wrappers.Result_Success(False)
            return output
        if not(default__.DiscoveryMatch(d_625_arn_, (self).discoveryFilter)):
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
        d_628_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_628_valueOrError0_ = Wrappers.default__.Need(((edk).keyProviderId) == (Constants.default__.PROVIDER__ID), software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encrypted data key was not generated by KMS")))
        if (d_628_valueOrError0_).IsFailure():
            res = (d_628_valueOrError0_).PropagateFailure()
            return res
        d_629_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_629_valueOrError1_ = Wrappers.default__.Need(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo), software.amazon.cryptography.materialproviders.internaldafny.types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid AWS KMS encoding, provider info is not UTF8.")))
        if (d_629_valueOrError1_).IsFailure():
            res = (d_629_valueOrError1_).PropagateFailure()
            return res
        d_630_keyId_: _dafny.Seq
        d_631_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_631_valueOrError2_ = (UTF8.default__.Decode((edk).keyProviderInfo)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_631_valueOrError2_).IsFailure():
            res = (d_631_valueOrError2_).PropagateFailure()
            return res
        d_630_keyId_ = (d_631_valueOrError2_).Extract()
        d_632_arn_: AwsArnParsing.AwsArn
        d_633_valueOrError3_: Wrappers.Result = None
        d_633_valueOrError3_ = (AwsArnParsing.default__.ParseAwsKmsArn(d_630_keyId_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_633_valueOrError3_).IsFailure():
            res = (d_633_valueOrError3_).PropagateFailure()
            return res
        d_632_arn_ = (d_633_valueOrError3_).Extract()
        res = Wrappers.Result_Success(_dafny.Seq([Constants.AwsKmsEdkHelper_AwsKmsEdkHelper(edk, d_632_arn_)]))
        return res
        return res


class AwsKmsEncryptedDataKeyDecryptor(Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._materials: software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials = None
        self._client: software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient = None
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
        d_634_awsKmsKey_: _dafny.Seq
        d_634_awsKmsKey_ = ((helper).arn).ToString()
        d_635___v0_: tuple
        d_636_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_636_valueOrError0_ = AwsKmsUtils.default__.ValidateKmsKeyId(((helper).arn).ToString())
        if (d_636_valueOrError0_).IsFailure():
            res = (d_636_valueOrError0_).PropagateFailure()
            return res
        d_635___v0_ = (d_636_valueOrError0_).Extract()
        d_637_kmsUnwrap_: AwsKmsKeyring.KmsUnwrapKeyMaterial
        nw12_ = AwsKmsKeyring.KmsUnwrapKeyMaterial()
        nw12_.ctor__((self).client, d_634_awsKmsKey_, (self).grantTokens)
        d_637_kmsUnwrap_ = nw12_
        d_638_unwrapOutputRes_: Wrappers.Result
        out97_: Wrappers.Result
        out97_ = EdkWrapping.default__.UnwrapEdkMaterial(((helper).edk).ciphertext, (self).materials, d_637_kmsUnwrap_)
        d_638_unwrapOutputRes_ = out97_
        d_639_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_640_valueOrError1_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.UnwrapEdkMaterialOutput.default(AwsKmsKeyring.KmsUnwrapInfo.default()))()
        d_640_valueOrError1_ = d_638_unwrapOutputRes_
        if (d_640_valueOrError1_).IsFailure():
            res = (d_640_valueOrError1_).PropagateFailure()
            return res
        d_639_unwrapOutput_ = (d_640_valueOrError1_).Extract()
        d_641_result_: software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials
        d_642_valueOrError2_: Wrappers.Result = None
        d_642_valueOrError2_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_639_unwrapOutput_).plaintextDataKey, (d_639_unwrapOutput_).symmetricSigningKey)
        if (d_642_valueOrError2_).IsFailure():
            res = (d_642_valueOrError2_).PropagateFailure()
            return res
        d_641_result_ = (d_642_valueOrError2_).Extract()
        res = Wrappers.Result_Success(d_641_result_)
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
