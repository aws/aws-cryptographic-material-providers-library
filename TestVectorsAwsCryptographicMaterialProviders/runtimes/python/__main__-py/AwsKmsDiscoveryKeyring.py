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

# Module: AwsKmsDiscoveryKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DiscoveryMatch(arn, discoveryFilter):
        pat_let_tv155_ = arn
        pat_let_tv156_ = arn
        def lambda36_(source24_):
            if source24_.is_None:
                return True
            elif True:
                d_519___mcc_h0_ = source24_.value
                d_520_filter_ = d_519___mcc_h0_
                return (((d_520_filter_).partition) == ((pat_let_tv155_).partition)) and (((d_520_filter_).accountIds) <= (_dafny.Seq([(pat_let_tv156_).account])))

        return (True) and (lambda36_(discoveryFilter))


class AwsKmsDiscoveryKeyring(Keyring.VerifiableInterface, software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring):
    def  __init__(self):
        self._client: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient = None
        self._discoveryFilter: Wrappers.Option = Wrappers.Option.default()()
        self._grantTokens: _dafny.Seq = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsDiscoveryKeyring.AwsKmsDiscoveryKeyring"
    def OnEncrypt(self, input):
        out99_: Wrappers.Result
        out99_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnEncrypt(self, input)
        return out99_

    def OnDecrypt(self, input):
        out100_: Wrappers.Result
        out100_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnDecrypt(self, input)
        return out100_

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
        d_521_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_521_materials_ = (input).materials
        d_522_encryptedDataKeys_: _dafny.Seq
        d_522_encryptedDataKeys_ = (input).encryptedDataKeys
        d_523_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_523_suite_ = ((input).materials).algorithmSuite
        d_524_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_524_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_521_materials_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_524_valueOrError0_).IsFailure():
            res = (d_524_valueOrError0_).PropagateFailure()
            return res
        d_525_edkFilter_: AwsKmsEncryptedDataKeyFilter
        nw9_ = AwsKmsEncryptedDataKeyFilter()
        nw9_.ctor__((self).discoveryFilter)
        d_525_edkFilter_ = nw9_
        d_526_matchingEdks_: _dafny.Seq
        d_527_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out101_: Wrappers.Result
        out101_ = Actions.default__.FilterWithResult(d_525_edkFilter_, d_522_encryptedDataKeys_)
        d_527_valueOrError1_ = out101_
        if (d_527_valueOrError1_).IsFailure():
            res = (d_527_valueOrError1_).PropagateFailure()
            return res
        d_526_matchingEdks_ = (d_527_valueOrError1_).Extract()
        d_528_edkTransform_: AwsKmsEncryptedDataKeyTransformer
        nw10_ = AwsKmsEncryptedDataKeyTransformer()
        nw10_.ctor__()
        d_528_edkTransform_ = nw10_
        d_529_edksToAttempt_: _dafny.Seq
        d_530_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out102_: Wrappers.Result
        out102_ = Actions.default__.DeterministicFlatMapWithResult(d_528_edkTransform_, d_526_matchingEdks_)
        d_530_valueOrError2_ = out102_
        if (d_530_valueOrError2_).IsFailure():
            res = (d_530_valueOrError2_).PropagateFailure()
            return res
        d_529_edksToAttempt_ = (d_530_valueOrError2_).Extract()
        d_531_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_531_valueOrError3_ = Wrappers.default__.Need((0) < (len(d_529_edksToAttempt_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to decrypt data key: No Encrypted Data Keys found to match.")))
        if (d_531_valueOrError3_).IsFailure():
            res = (d_531_valueOrError3_).PropagateFailure()
            return res
        d_532_decryptAction_: AwsKmsEncryptedDataKeyDecryptor
        nw11_ = AwsKmsEncryptedDataKeyDecryptor()
        nw11_.ctor__(d_521_materials_, (self).client, (self).grantTokens)
        d_532_decryptAction_ = nw11_
        d_533_outcome_: Wrappers.Result
        out103_: Wrappers.Result
        out103_ = Actions.default__.ReduceToSuccess(d_532_decryptAction_, d_529_edksToAttempt_)
        d_533_outcome_ = out103_
        def lambda37_(source25_):
            if source25_.is_Success:
                d_534___mcc_h0_ = source25_.value
                d_535_mat_ = d_534___mcc_h0_
                return Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput_OnDecryptOutput(d_535_mat_))
            elif True:
                d_536___mcc_h1_ = source25_.error
                d_537_errors_ = d_536___mcc_h1_
                return Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_CollectionOfErrors(d_537_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`.")))

        res = lambda37_(d_533_outcome_)
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
        d_538_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_538_valueOrError0_ = Wrappers.default__.Need(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid AWS KMS encoding, provider info is not UTF8.")))
        if (d_538_valueOrError0_).IsFailure():
            output = (d_538_valueOrError0_).PropagateFailure()
            return output
        d_539_keyId_: _dafny.Seq
        d_540_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_540_valueOrError1_ = (UTF8.default__.Decode((edk).keyProviderInfo)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_540_valueOrError1_).IsFailure():
            output = (d_540_valueOrError1_).PropagateFailure()
            return output
        d_539_keyId_ = (d_540_valueOrError1_).Extract()
        d_541_arn_: AwsArnParsing.AwsArn
        d_542_valueOrError2_: Wrappers.Result = None
        d_542_valueOrError2_ = (AwsArnParsing.default__.ParseAwsKmsArn(d_539_keyId_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_542_valueOrError2_).IsFailure():
            output = (d_542_valueOrError2_).PropagateFailure()
            return output
        d_541_arn_ = (d_542_valueOrError2_).Extract()
        d_543_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_543_valueOrError3_ = Wrappers.default__.Need((((d_541_arn_).resource).resourceType) == (_dafny.Seq("key")), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Only AWS KMS Keys supported")))
        if (d_543_valueOrError3_).IsFailure():
            output = (d_543_valueOrError3_).PropagateFailure()
            return output
        if ((edk).keyProviderId) != (Constants.default__.PROVIDER__ID):
            output = Wrappers.Result_Success(False)
            return output
        if not(default__.DiscoveryMatch(d_541_arn_, (self).discoveryFilter)):
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
        d_544_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_544_valueOrError0_ = Wrappers.default__.Need(((edk).keyProviderId) == (Constants.default__.PROVIDER__ID), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encrypted data key was not generated by KMS")))
        if (d_544_valueOrError0_).IsFailure():
            res = (d_544_valueOrError0_).PropagateFailure()
            return res
        d_545_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_545_valueOrError1_ = Wrappers.default__.Need(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid AWS KMS encoding, provider info is not UTF8.")))
        if (d_545_valueOrError1_).IsFailure():
            res = (d_545_valueOrError1_).PropagateFailure()
            return res
        d_546_keyId_: _dafny.Seq
        d_547_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_547_valueOrError2_ = (UTF8.default__.Decode((edk).keyProviderInfo)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_547_valueOrError2_).IsFailure():
            res = (d_547_valueOrError2_).PropagateFailure()
            return res
        d_546_keyId_ = (d_547_valueOrError2_).Extract()
        d_548_arn_: AwsArnParsing.AwsArn
        d_549_valueOrError3_: Wrappers.Result = None
        d_549_valueOrError3_ = (AwsArnParsing.default__.ParseAwsKmsArn(d_546_keyId_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_549_valueOrError3_).IsFailure():
            res = (d_549_valueOrError3_).PropagateFailure()
            return res
        d_548_arn_ = (d_549_valueOrError3_).Extract()
        res = Wrappers.Result_Success(_dafny.Seq([Constants.AwsKmsEdkHelper_AwsKmsEdkHelper(edk, d_548_arn_)]))
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
        d_550_awsKmsKey_: _dafny.Seq
        d_550_awsKmsKey_ = ((helper).arn).ToString()
        d_551___v0_: tuple
        d_552_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_552_valueOrError0_ = AwsKmsUtils.default__.ValidateKmsKeyId(((helper).arn).ToString())
        if (d_552_valueOrError0_).IsFailure():
            res = (d_552_valueOrError0_).PropagateFailure()
            return res
        d_551___v0_ = (d_552_valueOrError0_).Extract()
        d_553_kmsUnwrap_: AwsKmsKeyring.KmsUnwrapKeyMaterial
        nw12_ = AwsKmsKeyring.KmsUnwrapKeyMaterial()
        nw12_.ctor__((self).client, d_550_awsKmsKey_, (self).grantTokens)
        d_553_kmsUnwrap_ = nw12_
        d_554_unwrapOutputRes_: Wrappers.Result
        out104_: Wrappers.Result
        out104_ = EdkWrapping.default__.UnwrapEdkMaterial(((helper).edk).ciphertext, (self).materials, d_553_kmsUnwrap_)
        d_554_unwrapOutputRes_ = out104_
        d_555_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_556_valueOrError1_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.UnwrapEdkMaterialOutput.default(AwsKmsKeyring.KmsUnwrapInfo.default()))()
        d_556_valueOrError1_ = d_554_unwrapOutputRes_
        if (d_556_valueOrError1_).IsFailure():
            res = (d_556_valueOrError1_).PropagateFailure()
            return res
        d_555_unwrapOutput_ = (d_556_valueOrError1_).Extract()
        d_557_result_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_558_valueOrError2_: Wrappers.Result = None
        d_558_valueOrError2_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_555_unwrapOutput_).plaintextDataKey, (d_555_unwrapOutput_).symmetricSigningKey)
        if (d_558_valueOrError2_).IsFailure():
            res = (d_558_valueOrError2_).PropagateFailure()
            return res
        d_557_result_ = (d_558_valueOrError2_).Extract()
        res = Wrappers.Result_Success(d_557_result_)
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
