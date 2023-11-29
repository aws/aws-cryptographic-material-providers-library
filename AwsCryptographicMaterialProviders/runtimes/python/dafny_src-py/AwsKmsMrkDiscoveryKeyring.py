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
import AwsKmsDiscoveryKeyring
import DiscoveryMultiKeyring

assert "AwsKmsMrkDiscoveryKeyring" == __name__
AwsKmsMrkDiscoveryKeyring = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def ToStringForRegion(arn, region):
        if AwsArnParsing.default__.IsMultiRegionAwsKmsArn(arn):
            return (arn).ToArnString(Wrappers.Option_Some(region))
        elif True:
            return (arn).ToString()

    @staticmethod
    def DiscoveryMatch(arn, discoveryFilter, region):
        pat_let_tv33_ = arn
        pat_let_tv34_ = arn
        def lambda60_(source28_):
            if source28_.is_None:
                return True
            elif True:
                d_756___mcc_h0_ = source28_.value
                def iife40_(_pat_let15_0):
                    def iife41_(d_757_filter_):
                        return (((d_757_filter_).partition) == ((pat_let_tv33_).partition)) and (((pat_let_tv34_).account) in ((d_757_filter_).accountIds))
                    return iife41_(_pat_let15_0)
                return iife40_(d_756___mcc_h0_)

        return (lambda60_(discoveryFilter)) and (((region) == ((arn).region) if not(AwsArnParsing.default__.IsMultiRegionAwsKmsArn(arn)) else True))


class AwsKmsMrkDiscoveryKeyring(Keyring.VerifiableInterface, software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring):
    def  __init__(self):
        self._client: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient = None
        self._region: _dafny.Seq = _dafny.Seq({})
        self._discoveryFilter: Wrappers.Option = Wrappers.Option_None.default()()
        self._grantTokens: _dafny.Seq = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsMrkDiscoveryKeyring.AwsKmsMrkDiscoveryKeyring"
    def OnEncrypt(self, input):
        out150_: Wrappers.Result
        out150_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnEncrypt(self, input)
        return out150_

    def OnDecrypt(self, input):
        out151_: Wrappers.Result
        out151_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnDecrypt(self, input)
        return out151_

    def ctor__(self, client, region, discoveryFilter, grantTokens):
        (self)._client = client
        (self)._region = region
        (self)._discoveryFilter = discoveryFilter
        (self)._grantTokens = grantTokens

    def OnEncrypt_k(self, input):
        output: Wrappers.Result = None
        output = Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption is not supported with a Discovery Keyring.")))
        return output
        return output

    def OnDecrypt_k(self, input):
        output: Wrappers.Result = None
        d_758_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_758_materials_ = (input).materials
        d_759_encryptedDataKeys_: _dafny.Seq
        d_759_encryptedDataKeys_ = (input).encryptedDataKeys
        d_760_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_760_suite_ = ((input).materials).algorithmSuite
        d_761_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_761_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_758_materials_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_761_valueOrError0_).IsFailure():
            output = (d_761_valueOrError0_).PropagateFailure()
            return output
        d_762_edkFilterTransform_: AwsKmsMrkDiscoveryKeyring.AwsKmsEncryptedDataKeyFilterTransform
        nw16_ = AwsKmsMrkDiscoveryKeyring.AwsKmsEncryptedDataKeyFilterTransform()
        nw16_.ctor__((self).region, (self).discoveryFilter)
        d_762_edkFilterTransform_ = nw16_
        d_763_edksToAttempt_: _dafny.Seq
        d_764_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out152_: Wrappers.Result
        out152_ = Actions.default__.DeterministicFlatMapWithResult(d_762_edkFilterTransform_, d_759_encryptedDataKeys_)
        d_764_valueOrError1_ = out152_
        if (d_764_valueOrError1_).IsFailure():
            output = (d_764_valueOrError1_).PropagateFailure()
            return output
        d_763_edksToAttempt_ = (d_764_valueOrError1_).Extract()
        d_765_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_765_valueOrError2_ = Wrappers.default__.Need((0) < (len(d_763_edksToAttempt_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to decrypt data key: No Encrypted Data Keys found to match.")))
        if (d_765_valueOrError2_).IsFailure():
            output = (d_765_valueOrError2_).PropagateFailure()
            return output
        d_766_decryptAction_: AwsKmsMrkDiscoveryKeyring.AwsKmsEncryptedDataKeyDecryptor
        nw17_ = AwsKmsMrkDiscoveryKeyring.AwsKmsEncryptedDataKeyDecryptor()
        nw17_.ctor__(d_758_materials_, (self).client, (self).region, (self).grantTokens)
        d_766_decryptAction_ = nw17_
        d_767_outcome_: Wrappers.Result
        out153_: Wrappers.Result
        out153_ = Actions.default__.ReduceToSuccess(d_766_decryptAction_, d_763_edksToAttempt_)
        d_767_outcome_ = out153_
        def lambda61_(source29_):
            if source29_.is_Success:
                d_768___mcc_h0_ = source29_.value
                def iife42_(_pat_let16_0):
                    def iife43_(d_769_mat_):
                        return Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput_OnDecryptOutput(d_769_mat_))
                    return iife43_(_pat_let16_0)
                return iife42_(d_768___mcc_h0_)
            elif True:
                d_770___mcc_h1_ = source29_.error
                def iife44_(_pat_let17_0):
                    def iife45_(d_771_errors_):
                        return Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_CollectionOfErrors(d_771_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`.")))
                    return iife45_(_pat_let17_0)
                return iife44_(d_770___mcc_h1_)

        output = lambda61_(d_767_outcome_)
        return output
        return output

    @property
    def client(self):
        return self._client
    @property
    def region(self):
        return self._region
    @property
    def discoveryFilter(self):
        return self._discoveryFilter
    @property
    def grantTokens(self):
        return self._grantTokens

class AwsKmsEncryptedDataKeyFilterTransform(Actions.DeterministicActionWithResult, Actions.DeterministicAction):
    def  __init__(self):
        self._region: _dafny.Seq = _dafny.Seq({})
        self._discoveryFilter: Wrappers.Option = Wrappers.Option_None.default()()
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsMrkDiscoveryKeyring.AwsKmsEncryptedDataKeyFilterTransform"
    def ctor__(self, region, discoveryFilter):
        (self)._region = region
        (self)._discoveryFilter = discoveryFilter

    def Invoke(self, edk):
        res: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        if ((edk).keyProviderId) != ((Constants.default__).PROVIDER__ID):
            res = Wrappers.Result_Success(_dafny.Seq([]))
            return res
        d_772_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_772_valueOrError0_ = Wrappers.default__.Need(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid AWS KMS encoding, provider info is not UTF8.")))
        if (d_772_valueOrError0_).IsFailure():
            res = (d_772_valueOrError0_).PropagateFailure()
            return res
        d_773_keyId_: _dafny.Seq
        d_774_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda62_(d_775_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(d_775_e_)

        d_774_valueOrError1_ = (UTF8.default__.Decode((edk).keyProviderInfo)).MapFailure(lambda62_)
        if (d_774_valueOrError1_).IsFailure():
            res = (d_774_valueOrError1_).PropagateFailure()
            return res
        d_773_keyId_ = (d_774_valueOrError1_).Extract()
        d_776_arn_: AwsArnParsing.AwsArn
        d_777_valueOrError2_: Wrappers.Result = None
        def lambda63_(d_778_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(d_778_e_)

        d_777_valueOrError2_ = (AwsArnParsing.default__.ParseAwsKmsArn(d_773_keyId_)).MapFailure(lambda63_)
        if (d_777_valueOrError2_).IsFailure():
            res = (d_777_valueOrError2_).PropagateFailure()
            return res
        d_776_arn_ = (d_777_valueOrError2_).Extract()
        d_779_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_779_valueOrError3_ = Wrappers.default__.Need((((d_776_arn_).resource).resourceType) == (_dafny.Seq("key")), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Only AWS KMS Keys supported")))
        if (d_779_valueOrError3_).IsFailure():
            res = (d_779_valueOrError3_).PropagateFailure()
            return res
        if not(AwsKmsMrkDiscoveryKeyring.default__.DiscoveryMatch(d_776_arn_, (self).discoveryFilter, (self).region)):
            res = Wrappers.Result_Success(_dafny.Seq([]))
            return res
        res = Wrappers.Result_Success(_dafny.Seq([Constants.AwsKmsEdkHelper_AwsKmsEdkHelper(edk, d_776_arn_)]))
        return res
        return res

    @property
    def region(self):
        return self._region
    @property
    def discoveryFilter(self):
        return self._discoveryFilter

class AwsKmsEncryptedDataKeyDecryptor(Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._materials: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials = None
        self._client: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient = None
        self._region: _dafny.Seq = _dafny.Seq({})
        self._grantTokens: _dafny.Seq = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsMrkDiscoveryKeyring.AwsKmsEncryptedDataKeyDecryptor"
    def ctor__(self, materials, client, region, grantTokens):
        (self)._materials = materials
        (self)._client = client
        (self)._region = region
        (self)._grantTokens = grantTokens

    def Invoke(self, helper):
        res: Wrappers.Result = None
        d_780_awsKmsKey_: _dafny.Seq
        d_780_awsKmsKey_ = AwsKmsMrkDiscoveryKeyring.default__.ToStringForRegion((helper).arn, (self).region)
        d_781___v0_: tuple
        d_782_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        d_782_valueOrError0_ = AwsKmsUtils.default__.ValidateKmsKeyId(d_780_awsKmsKey_)
        if (d_782_valueOrError0_).IsFailure():
            res = (d_782_valueOrError0_).PropagateFailure()
            return res
        d_781___v0_ = (d_782_valueOrError0_).Extract()
        d_783_kmsUnwrap_: AwsKmsKeyring.KmsUnwrapKeyMaterial
        nw18_ = AwsKmsKeyring.KmsUnwrapKeyMaterial()
        nw18_.ctor__((self).client, d_780_awsKmsKey_, (self).grantTokens)
        d_783_kmsUnwrap_ = nw18_
        d_784_unwrapOutputRes_: Wrappers.Result
        out154_: Wrappers.Result
        out154_ = EdkWrapping.default__.UnwrapEdkMaterial(((helper).edk).ciphertext, (self).materials, d_783_kmsUnwrap_)
        d_784_unwrapOutputRes_ = out154_
        d_785_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_786_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(EdkWrapping.UnwrapEdkMaterialOutput.default(AwsKmsKeyring.KmsUnwrapInfo.default()))()
        d_786_valueOrError1_ = d_784_unwrapOutputRes_
        if (d_786_valueOrError1_).IsFailure():
            res = (d_786_valueOrError1_).PropagateFailure()
            return res
        d_785_unwrapOutput_ = (d_786_valueOrError1_).Extract()
        res = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_785_unwrapOutput_).plaintextDataKey, (d_785_unwrapOutput_).symmetricSigningKey)
        return res

    @property
    def materials(self):
        return self._materials
    @property
    def client(self):
        return self._client
    @property
    def region(self):
        return self._region
    @property
    def grantTokens(self):
        return self._grantTokens
