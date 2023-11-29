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

assert "AwsKmsDiscoveryKeyring" == __name__
AwsKmsDiscoveryKeyring = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DiscoveryMatch(arn, discoveryFilter):
        pat_let_tv31_ = arn
        pat_let_tv32_ = arn
        def lambda58_(source26_):
            if source26_.is_None:
                return True
            elif True:
                d_707___mcc_h0_ = source26_.value
                def iife34_(_pat_let12_0):
                    def iife35_(d_708_filter_):
                        return (((d_708_filter_).partition) == ((pat_let_tv31_).partition)) and (((d_708_filter_).accountIds) <= (_dafny.Seq([(pat_let_tv32_).account])))
                    return iife35_(_pat_let12_0)
                return iife34_(d_707___mcc_h0_)

        return (True) and (lambda58_(discoveryFilter))


class AwsKmsDiscoveryKeyring(Keyring.VerifiableInterface, software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring):
    def  __init__(self):
        self._client: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient = None
        self._discoveryFilter: Wrappers.Option = Wrappers.Option_None.default()()
        self._grantTokens: _dafny.Seq = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsDiscoveryKeyring.AwsKmsDiscoveryKeyring"
    def OnEncrypt(self, input):
        out143_: Wrappers.Result
        out143_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnEncrypt(self, input)
        return out143_

    def OnDecrypt(self, input):
        out144_: Wrappers.Result
        out144_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnDecrypt(self, input)
        return out144_

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
        d_709_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_709_materials_ = (input).materials
        d_710_encryptedDataKeys_: _dafny.Seq
        d_710_encryptedDataKeys_ = (input).encryptedDataKeys
        d_711_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_711_suite_ = ((input).materials).algorithmSuite
        d_712_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_712_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_709_materials_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_712_valueOrError0_).IsFailure():
            res = (d_712_valueOrError0_).PropagateFailure()
            return res
        d_713_edkFilter_: AwsKmsDiscoveryKeyring.AwsKmsEncryptedDataKeyFilter
        nw10_ = AwsKmsDiscoveryKeyring.AwsKmsEncryptedDataKeyFilter()
        nw10_.ctor__((self).discoveryFilter)
        d_713_edkFilter_ = nw10_
        d_714_matchingEdks_: _dafny.Seq
        d_715_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out145_: Wrappers.Result
        out145_ = Actions.default__.FilterWithResult(d_713_edkFilter_, d_710_encryptedDataKeys_)
        d_715_valueOrError1_ = out145_
        if (d_715_valueOrError1_).IsFailure():
            res = (d_715_valueOrError1_).PropagateFailure()
            return res
        d_714_matchingEdks_ = (d_715_valueOrError1_).Extract()
        d_716_edkTransform_: AwsKmsDiscoveryKeyring.AwsKmsEncryptedDataKeyTransformer
        nw11_ = AwsKmsDiscoveryKeyring.AwsKmsEncryptedDataKeyTransformer()
        nw11_.ctor__()
        d_716_edkTransform_ = nw11_
        d_717_edksToAttempt_: _dafny.Seq
        d_718_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out146_: Wrappers.Result
        out146_ = Actions.default__.DeterministicFlatMapWithResult(d_716_edkTransform_, d_714_matchingEdks_)
        d_718_valueOrError2_ = out146_
        if (d_718_valueOrError2_).IsFailure():
            res = (d_718_valueOrError2_).PropagateFailure()
            return res
        d_717_edksToAttempt_ = (d_718_valueOrError2_).Extract()
        d_719_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_719_valueOrError3_ = Wrappers.default__.Need((0) < (len(d_717_edksToAttempt_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to decrypt data key: No Encrypted Data Keys found to match.")))
        if (d_719_valueOrError3_).IsFailure():
            res = (d_719_valueOrError3_).PropagateFailure()
            return res
        d_720_decryptAction_: AwsKmsDiscoveryKeyring.AwsKmsEncryptedDataKeyDecryptor
        nw12_ = AwsKmsDiscoveryKeyring.AwsKmsEncryptedDataKeyDecryptor()
        nw12_.ctor__(d_709_materials_, (self).client, (self).grantTokens)
        d_720_decryptAction_ = nw12_
        d_721_outcome_: Wrappers.Result
        out147_: Wrappers.Result
        out147_ = Actions.default__.ReduceToSuccess(d_720_decryptAction_, d_717_edksToAttempt_)
        d_721_outcome_ = out147_
        def lambda59_(source27_):
            if source27_.is_Success:
                d_722___mcc_h0_ = source27_.value
                def iife36_(_pat_let13_0):
                    def iife37_(d_723_mat_):
                        return Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput_OnDecryptOutput(d_723_mat_))
                    return iife37_(_pat_let13_0)
                return iife36_(d_722___mcc_h0_)
            elif True:
                d_724___mcc_h1_ = source27_.error
                def iife38_(_pat_let14_0):
                    def iife39_(d_725_errors_):
                        return Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_CollectionOfErrors(d_725_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`.")))
                    return iife39_(_pat_let14_0)
                return iife38_(d_724___mcc_h1_)

        res = lambda59_(d_721_outcome_)
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
        d_726_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_726_valueOrError0_ = Wrappers.default__.Need(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid AWS KMS encoding, provider info is not UTF8.")))
        if (d_726_valueOrError0_).IsFailure():
            output = (d_726_valueOrError0_).PropagateFailure()
            return output
        d_727_keyId_: _dafny.Seq
        d_728_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_728_valueOrError1_ = (UTF8.default__.Decode((edk).keyProviderInfo)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_728_valueOrError1_).IsFailure():
            output = (d_728_valueOrError1_).PropagateFailure()
            return output
        d_727_keyId_ = (d_728_valueOrError1_).Extract()
        d_729_arn_: AwsArnParsing.AwsArn
        d_730_valueOrError2_: Wrappers.Result = None
        d_730_valueOrError2_ = (AwsArnParsing.default__.ParseAwsKmsArn(d_727_keyId_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_730_valueOrError2_).IsFailure():
            output = (d_730_valueOrError2_).PropagateFailure()
            return output
        d_729_arn_ = (d_730_valueOrError2_).Extract()
        d_731_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_731_valueOrError3_ = Wrappers.default__.Need((((d_729_arn_).resource).resourceType) == (_dafny.Seq("key")), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Only AWS KMS Keys supported")))
        if (d_731_valueOrError3_).IsFailure():
            output = (d_731_valueOrError3_).PropagateFailure()
            return output
        if ((edk).keyProviderId) != ((Constants.default__).PROVIDER__ID):
            output = Wrappers.Result_Success(False)
            return output
        if not(AwsKmsDiscoveryKeyring.default__.DiscoveryMatch(d_729_arn_, (self).discoveryFilter)):
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
        d_732_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_732_valueOrError0_ = Wrappers.default__.Need(((edk).keyProviderId) == ((Constants.default__).PROVIDER__ID), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encrypted data key was not generated by KMS")))
        if (d_732_valueOrError0_).IsFailure():
            res = (d_732_valueOrError0_).PropagateFailure()
            return res
        d_733_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_733_valueOrError1_ = Wrappers.default__.Need(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid AWS KMS encoding, provider info is not UTF8.")))
        if (d_733_valueOrError1_).IsFailure():
            res = (d_733_valueOrError1_).PropagateFailure()
            return res
        d_734_keyId_: _dafny.Seq
        d_735_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_735_valueOrError2_ = (UTF8.default__.Decode((edk).keyProviderInfo)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_735_valueOrError2_).IsFailure():
            res = (d_735_valueOrError2_).PropagateFailure()
            return res
        d_734_keyId_ = (d_735_valueOrError2_).Extract()
        d_736_arn_: AwsArnParsing.AwsArn
        d_737_valueOrError3_: Wrappers.Result = None
        d_737_valueOrError3_ = (AwsArnParsing.default__.ParseAwsKmsArn(d_734_keyId_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_737_valueOrError3_).IsFailure():
            res = (d_737_valueOrError3_).PropagateFailure()
            return res
        d_736_arn_ = (d_737_valueOrError3_).Extract()
        res = Wrappers.Result_Success(_dafny.Seq([Constants.AwsKmsEdkHelper_AwsKmsEdkHelper(edk, d_736_arn_)]))
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
        d_738_awsKmsKey_: _dafny.Seq
        d_738_awsKmsKey_ = ((helper).arn).ToString()
        d_739___v0_: tuple
        d_740_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        d_740_valueOrError0_ = AwsKmsUtils.default__.ValidateKmsKeyId(((helper).arn).ToString())
        if (d_740_valueOrError0_).IsFailure():
            res = (d_740_valueOrError0_).PropagateFailure()
            return res
        d_739___v0_ = (d_740_valueOrError0_).Extract()
        d_741_kmsUnwrap_: AwsKmsKeyring.KmsUnwrapKeyMaterial
        nw13_ = AwsKmsKeyring.KmsUnwrapKeyMaterial()
        nw13_.ctor__((self).client, d_738_awsKmsKey_, (self).grantTokens)
        d_741_kmsUnwrap_ = nw13_
        d_742_unwrapOutputRes_: Wrappers.Result
        out148_: Wrappers.Result
        out148_ = EdkWrapping.default__.UnwrapEdkMaterial(((helper).edk).ciphertext, (self).materials, d_741_kmsUnwrap_)
        d_742_unwrapOutputRes_ = out148_
        d_743_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_744_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(EdkWrapping.UnwrapEdkMaterialOutput.default(AwsKmsKeyring.KmsUnwrapInfo.default()))()
        d_744_valueOrError1_ = d_742_unwrapOutputRes_
        if (d_744_valueOrError1_).IsFailure():
            res = (d_744_valueOrError1_).PropagateFailure()
            return res
        d_743_unwrapOutput_ = (d_744_valueOrError1_).Extract()
        d_745_result_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_746_valueOrError2_: Wrappers.Result = None
        d_746_valueOrError2_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_743_unwrapOutput_).plaintextDataKey, (d_743_unwrapOutput_).symmetricSigningKey)
        if (d_746_valueOrError2_).IsFailure():
            res = (d_746_valueOrError2_).PropagateFailure()
            return res
        d_745_result_ = (d_746_valueOrError2_).Extract()
        res = Wrappers.Result_Success(d_745_result_)
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
