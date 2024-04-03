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
                d_623___mcc_h0_ = source22_.value
                d_624_filter_ = d_623___mcc_h0_
                return (((d_624_filter_).partition) == ((pat_let_tv155_).partition)) and (((d_624_filter_).accountIds) <= (_dafny.Seq([(pat_let_tv156_).account])))

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
        d_625_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_625_materials_ = (input).materials
        d_626_encryptedDataKeys_: _dafny.Seq
        d_626_encryptedDataKeys_ = (input).encryptedDataKeys
        d_627_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_627_suite_ = ((input).materials).algorithmSuite
        d_628_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_628_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_625_materials_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_628_valueOrError0_).IsFailure():
            res = (d_628_valueOrError0_).PropagateFailure()
            return res
        d_629_edkFilter_: AwsKmsEncryptedDataKeyFilter
        nw9_ = AwsKmsEncryptedDataKeyFilter()
        nw9_.ctor__((self).discoveryFilter)
        d_629_edkFilter_ = nw9_
        d_630_matchingEdks_: _dafny.Seq
        d_631_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out94_: Wrappers.Result
        out94_ = Actions.default__.FilterWithResult(d_629_edkFilter_, d_626_encryptedDataKeys_)
        d_631_valueOrError1_ = out94_
        if (d_631_valueOrError1_).IsFailure():
            res = (d_631_valueOrError1_).PropagateFailure()
            return res
        d_630_matchingEdks_ = (d_631_valueOrError1_).Extract()
        d_632_edkTransform_: AwsKmsEncryptedDataKeyTransformer
        nw10_ = AwsKmsEncryptedDataKeyTransformer()
        nw10_.ctor__()
        d_632_edkTransform_ = nw10_
        d_633_edksToAttempt_: _dafny.Seq
        d_634_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out95_: Wrappers.Result
        out95_ = Actions.default__.DeterministicFlatMapWithResult(d_632_edkTransform_, d_630_matchingEdks_)
        d_634_valueOrError2_ = out95_
        if (d_634_valueOrError2_).IsFailure():
            res = (d_634_valueOrError2_).PropagateFailure()
            return res
        d_633_edksToAttempt_ = (d_634_valueOrError2_).Extract()
        d_635_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_635_valueOrError3_ = Wrappers.default__.Need((0) < (len(d_633_edksToAttempt_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to decrypt data key: No Encrypted Data Keys found to match.")))
        if (d_635_valueOrError3_).IsFailure():
            res = (d_635_valueOrError3_).PropagateFailure()
            return res
        d_636_decryptAction_: AwsKmsEncryptedDataKeyDecryptor
        nw11_ = AwsKmsEncryptedDataKeyDecryptor()
        nw11_.ctor__(d_625_materials_, (self).client, (self).grantTokens)
        d_636_decryptAction_ = nw11_
        d_637_outcome_: Wrappers.Result
        out96_: Wrappers.Result
        out96_ = Actions.default__.ReduceToSuccess(d_636_decryptAction_, d_633_edksToAttempt_)
        d_637_outcome_ = out96_
        def lambda59_(source23_):
            if source23_.is_Success:
                d_638___mcc_h0_ = source23_.value
                d_639_mat_ = d_638___mcc_h0_
                return Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput_OnDecryptOutput(d_639_mat_))
            elif True:
                d_640___mcc_h1_ = source23_.error
                d_641_errors_ = d_640___mcc_h1_
                return Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_CollectionOfErrors(d_641_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`.")))

        res = lambda59_(d_637_outcome_)
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
        d_642_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_642_valueOrError0_ = Wrappers.default__.Need(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid AWS KMS encoding, provider info is not UTF8.")))
        if (d_642_valueOrError0_).IsFailure():
            output = (d_642_valueOrError0_).PropagateFailure()
            return output
        d_643_keyId_: _dafny.Seq
        d_644_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_644_valueOrError1_ = (UTF8.default__.Decode((edk).keyProviderInfo)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_644_valueOrError1_).IsFailure():
            output = (d_644_valueOrError1_).PropagateFailure()
            return output
        d_643_keyId_ = (d_644_valueOrError1_).Extract()
        d_645_arn_: AwsArnParsing.AwsArn
        d_646_valueOrError2_: Wrappers.Result = None
        d_646_valueOrError2_ = (AwsArnParsing.default__.ParseAwsKmsArn(d_643_keyId_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_646_valueOrError2_).IsFailure():
            output = (d_646_valueOrError2_).PropagateFailure()
            return output
        d_645_arn_ = (d_646_valueOrError2_).Extract()
        d_647_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_647_valueOrError3_ = Wrappers.default__.Need((((d_645_arn_).resource).resourceType) == (_dafny.Seq("key")), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Only AWS KMS Keys supported")))
        if (d_647_valueOrError3_).IsFailure():
            output = (d_647_valueOrError3_).PropagateFailure()
            return output
        if ((edk).keyProviderId) != (Constants.default__.PROVIDER__ID):
            output = Wrappers.Result_Success(False)
            return output
        if not(default__.DiscoveryMatch(d_645_arn_, (self).discoveryFilter)):
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
        d_648_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_648_valueOrError0_ = Wrappers.default__.Need(((edk).keyProviderId) == (Constants.default__.PROVIDER__ID), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encrypted data key was not generated by KMS")))
        if (d_648_valueOrError0_).IsFailure():
            res = (d_648_valueOrError0_).PropagateFailure()
            return res
        d_649_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_649_valueOrError1_ = Wrappers.default__.Need(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid AWS KMS encoding, provider info is not UTF8.")))
        if (d_649_valueOrError1_).IsFailure():
            res = (d_649_valueOrError1_).PropagateFailure()
            return res
        d_650_keyId_: _dafny.Seq
        d_651_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_651_valueOrError2_ = (UTF8.default__.Decode((edk).keyProviderInfo)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_651_valueOrError2_).IsFailure():
            res = (d_651_valueOrError2_).PropagateFailure()
            return res
        d_650_keyId_ = (d_651_valueOrError2_).Extract()
        d_652_arn_: AwsArnParsing.AwsArn
        d_653_valueOrError3_: Wrappers.Result = None
        d_653_valueOrError3_ = (AwsArnParsing.default__.ParseAwsKmsArn(d_650_keyId_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_653_valueOrError3_).IsFailure():
            res = (d_653_valueOrError3_).PropagateFailure()
            return res
        d_652_arn_ = (d_653_valueOrError3_).Extract()
        res = Wrappers.Result_Success(_dafny.Seq([Constants.AwsKmsEdkHelper_AwsKmsEdkHelper(edk, d_652_arn_)]))
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
        d_654_awsKmsKey_: _dafny.Seq
        d_654_awsKmsKey_ = ((helper).arn).ToString()
        d_655___v0_: tuple
        d_656_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_656_valueOrError0_ = AwsKmsUtils.default__.ValidateKmsKeyId(((helper).arn).ToString())
        if (d_656_valueOrError0_).IsFailure():
            res = (d_656_valueOrError0_).PropagateFailure()
            return res
        d_655___v0_ = (d_656_valueOrError0_).Extract()
        d_657_kmsUnwrap_: AwsKmsKeyring.KmsUnwrapKeyMaterial
        nw12_ = AwsKmsKeyring.KmsUnwrapKeyMaterial()
        nw12_.ctor__((self).client, d_654_awsKmsKey_, (self).grantTokens)
        d_657_kmsUnwrap_ = nw12_
        d_658_unwrapOutputRes_: Wrappers.Result
        out97_: Wrappers.Result
        out97_ = EdkWrapping.default__.UnwrapEdkMaterial(((helper).edk).ciphertext, (self).materials, d_657_kmsUnwrap_)
        d_658_unwrapOutputRes_ = out97_
        d_659_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_660_valueOrError1_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.UnwrapEdkMaterialOutput.default(AwsKmsKeyring.KmsUnwrapInfo.default()))()
        d_660_valueOrError1_ = d_658_unwrapOutputRes_
        if (d_660_valueOrError1_).IsFailure():
            res = (d_660_valueOrError1_).PropagateFailure()
            return res
        d_659_unwrapOutput_ = (d_660_valueOrError1_).Extract()
        d_661_result_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_662_valueOrError2_: Wrappers.Result = None
        d_662_valueOrError2_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_659_unwrapOutput_).plaintextDataKey, (d_659_unwrapOutput_).symmetricSigningKey)
        if (d_662_valueOrError2_).IsFailure():
            res = (d_662_valueOrError2_).PropagateFailure()
            return res
        d_661_result_ = (d_662_valueOrError2_).Extract()
        res = Wrappers.Result_Success(d_661_result_)
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
