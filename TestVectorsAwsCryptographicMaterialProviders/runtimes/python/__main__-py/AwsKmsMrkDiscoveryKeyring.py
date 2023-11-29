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
import Aws_mCryptography
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

# Module: AwsKmsMrkDiscoveryKeyring

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
        def lambda38_(source26_):
            if source26_.is_None:
                return True
            elif True:
                d_569___mcc_h0_ = source26_.value
                def iife31_(_pat_let14_0):
                    def iife32_(d_570_filter_):
                        return (((d_570_filter_).partition) == ((pat_let_tv33_).partition)) and (((pat_let_tv34_).account) in ((d_570_filter_).accountIds))
                    return iife32_(_pat_let14_0)
                return iife31_(d_569___mcc_h0_)

        return (lambda38_(discoveryFilter)) and (((region) == ((arn).region) if not(AwsArnParsing.default__.IsMultiRegionAwsKmsArn(arn)) else True))


class AwsKmsMrkDiscoveryKeyring(Keyring.VerifiableInterface, software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring):
    def  __init__(self):
        self._client: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient = None
        self._region: _dafny.Seq = _dafny.Seq({})
        self._discoveryFilter: Wrappers.Option = Wrappers.Option.default()()
        self._grantTokens: _dafny.Seq = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsMrkDiscoveryKeyring.AwsKmsMrkDiscoveryKeyring"
    def OnEncrypt(self, input):
        out106_: Wrappers.Result
        out106_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnEncrypt(self, input)
        return out106_

    def OnDecrypt(self, input):
        out107_: Wrappers.Result
        out107_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnDecrypt(self, input)
        return out107_

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
        d_571_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_571_materials_ = (input).materials
        d_572_encryptedDataKeys_: _dafny.Seq
        d_572_encryptedDataKeys_ = (input).encryptedDataKeys
        d_573_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_573_suite_ = ((input).materials).algorithmSuite
        d_574_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_574_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_571_materials_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_574_valueOrError0_).IsFailure():
            output = (d_574_valueOrError0_).PropagateFailure()
            return output
        d_575_edkFilterTransform_: AwsKmsEncryptedDataKeyFilterTransform
        nw15_ = AwsKmsEncryptedDataKeyFilterTransform()
        nw15_.ctor__((self).region, (self).discoveryFilter)
        d_575_edkFilterTransform_ = nw15_
        d_576_edksToAttempt_: _dafny.Seq
        d_577_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out108_: Wrappers.Result
        out108_ = Actions.default__.DeterministicFlatMapWithResult(d_575_edkFilterTransform_, d_572_encryptedDataKeys_)
        d_577_valueOrError1_ = out108_
        if (d_577_valueOrError1_).IsFailure():
            output = (d_577_valueOrError1_).PropagateFailure()
            return output
        d_576_edksToAttempt_ = (d_577_valueOrError1_).Extract()
        d_578_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_578_valueOrError2_ = Wrappers.default__.Need((0) < (len(d_576_edksToAttempt_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to decrypt data key: No Encrypted Data Keys found to match.")))
        if (d_578_valueOrError2_).IsFailure():
            output = (d_578_valueOrError2_).PropagateFailure()
            return output
        d_579_decryptAction_: AwsKmsEncryptedDataKeyDecryptor
        nw16_ = AwsKmsEncryptedDataKeyDecryptor()
        nw16_.ctor__(d_571_materials_, (self).client, (self).region, (self).grantTokens)
        d_579_decryptAction_ = nw16_
        d_580_outcome_: Wrappers.Result
        out109_: Wrappers.Result
        out109_ = Actions.default__.ReduceToSuccess(d_579_decryptAction_, d_576_edksToAttempt_)
        d_580_outcome_ = out109_
        def lambda39_(source27_):
            if source27_.is_Success:
                d_581___mcc_h0_ = source27_.value
                def iife33_(_pat_let15_0):
                    def iife34_(d_582_mat_):
                        return Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput_OnDecryptOutput(d_582_mat_))
                    return iife34_(_pat_let15_0)
                return iife33_(d_581___mcc_h0_)
            elif True:
                d_583___mcc_h1_ = source27_.error
                def iife35_(_pat_let16_0):
                    def iife36_(d_584_errors_):
                        return Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_CollectionOfErrors(d_584_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`.")))
                    return iife36_(_pat_let16_0)
                return iife35_(d_583___mcc_h1_)

        output = lambda39_(d_580_outcome_)
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
        self._discoveryFilter: Wrappers.Option = Wrappers.Option.default()()
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsMrkDiscoveryKeyring.AwsKmsEncryptedDataKeyFilterTransform"
    def ctor__(self, region, discoveryFilter):
        (self)._region = region
        (self)._discoveryFilter = discoveryFilter

    def Invoke(self, edk):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        if ((edk).keyProviderId) != (Constants.default__.PROVIDER__ID):
            res = Wrappers.Result_Success(_dafny.Seq([]))
            return res
        d_585_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_585_valueOrError0_ = Wrappers.default__.Need(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid AWS KMS encoding, provider info is not UTF8.")))
        if (d_585_valueOrError0_).IsFailure():
            res = (d_585_valueOrError0_).PropagateFailure()
            return res
        d_586_keyId_: _dafny.Seq
        d_587_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda40_(d_588_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(d_588_e_)

        d_587_valueOrError1_ = (UTF8.default__.Decode((edk).keyProviderInfo)).MapFailure(lambda40_)
        if (d_587_valueOrError1_).IsFailure():
            res = (d_587_valueOrError1_).PropagateFailure()
            return res
        d_586_keyId_ = (d_587_valueOrError1_).Extract()
        d_589_arn_: AwsArnParsing.AwsArn
        d_590_valueOrError2_: Wrappers.Result = None
        def lambda41_(d_591_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(d_591_e_)

        d_590_valueOrError2_ = (AwsArnParsing.default__.ParseAwsKmsArn(d_586_keyId_)).MapFailure(lambda41_)
        if (d_590_valueOrError2_).IsFailure():
            res = (d_590_valueOrError2_).PropagateFailure()
            return res
        d_589_arn_ = (d_590_valueOrError2_).Extract()
        d_592_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_592_valueOrError3_ = Wrappers.default__.Need((((d_589_arn_).resource).resourceType) == (_dafny.Seq("key")), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Only AWS KMS Keys supported")))
        if (d_592_valueOrError3_).IsFailure():
            res = (d_592_valueOrError3_).PropagateFailure()
            return res
        if not(default__.DiscoveryMatch(d_589_arn_, (self).discoveryFilter, (self).region)):
            res = Wrappers.Result_Success(_dafny.Seq([]))
            return res
        res = Wrappers.Result_Success(_dafny.Seq([Constants.AwsKmsEdkHelper_AwsKmsEdkHelper(edk, d_589_arn_)]))
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
        d_593_awsKmsKey_: _dafny.Seq
        d_593_awsKmsKey_ = default__.ToStringForRegion((helper).arn, (self).region)
        d_594___v0_: tuple
        d_595_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_595_valueOrError0_ = AwsKmsUtils.default__.ValidateKmsKeyId(d_593_awsKmsKey_)
        if (d_595_valueOrError0_).IsFailure():
            res = (d_595_valueOrError0_).PropagateFailure()
            return res
        d_594___v0_ = (d_595_valueOrError0_).Extract()
        d_596_kmsUnwrap_: AwsKmsKeyring.KmsUnwrapKeyMaterial
        nw17_ = AwsKmsKeyring.KmsUnwrapKeyMaterial()
        nw17_.ctor__((self).client, d_593_awsKmsKey_, (self).grantTokens)
        d_596_kmsUnwrap_ = nw17_
        d_597_unwrapOutputRes_: Wrappers.Result
        out110_: Wrappers.Result
        out110_ = EdkWrapping.default__.UnwrapEdkMaterial(((helper).edk).ciphertext, (self).materials, d_596_kmsUnwrap_)
        d_597_unwrapOutputRes_ = out110_
        d_598_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_599_valueOrError1_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.UnwrapEdkMaterialOutput.default(AwsKmsKeyring.KmsUnwrapInfo.default()))()
        d_599_valueOrError1_ = d_597_unwrapOutputRes_
        if (d_599_valueOrError1_).IsFailure():
            res = (d_599_valueOrError1_).PropagateFailure()
            return res
        d_598_unwrapOutput_ = (d_599_valueOrError1_).Extract()
        res = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_598_unwrapOutput_).plaintextDataKey, (d_598_unwrapOutput_).symmetricSigningKey)
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
