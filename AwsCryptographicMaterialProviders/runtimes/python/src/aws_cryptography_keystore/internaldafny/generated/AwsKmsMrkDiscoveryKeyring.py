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

# assert "AwsKmsMrkDiscoveryKeyring" == __name__
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
        def lambda61_(source28_):
            if source28_.is_None:
                return True
            elif True:
                d_955___mcc_h0_ = source28_.value
                def iife44_(_pat_let16_0):
                    def iife45_(d_956_filter_):
                        return (((d_956_filter_).partition) == ((pat_let_tv33_).partition)) and (((pat_let_tv34_).account) in ((d_956_filter_).accountIds))
                    return iife45_(_pat_let16_0)
                return iife44_(d_955___mcc_h0_)

        return (lambda61_(discoveryFilter)) and (((region) == ((arn).region) if not(AwsArnParsing.default__.IsMultiRegionAwsKmsArn(arn)) else True))


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
        out227_: Wrappers.Result
        out227_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnEncrypt(self, input)
        return out227_

    def OnDecrypt(self, input):
        out228_: Wrappers.Result
        out228_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnDecrypt(self, input)
        return out228_

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
        d_957_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_957_materials_ = (input).materials
        d_958_encryptedDataKeys_: _dafny.Seq
        d_958_encryptedDataKeys_ = (input).encryptedDataKeys
        d_959_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_959_suite_ = ((input).materials).algorithmSuite
        d_960_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_960_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_957_materials_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_960_valueOrError0_).IsFailure():
            output = (d_960_valueOrError0_).PropagateFailure()
            return output
        d_961_edkFilterTransform_: AwsKmsMrkDiscoveryKeyring.AwsKmsEncryptedDataKeyFilterTransform
        nw16_ = AwsKmsMrkDiscoveryKeyring.AwsKmsEncryptedDataKeyFilterTransform()
        nw16_.ctor__((self).region, (self).discoveryFilter)
        d_961_edkFilterTransform_ = nw16_
        d_962_edksToAttempt_: _dafny.Seq
        d_963_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out229_: Wrappers.Result
        out229_ = Actions.default__.DeterministicFlatMapWithResult(d_961_edkFilterTransform_, d_958_encryptedDataKeys_)
        d_963_valueOrError1_ = out229_
        if (d_963_valueOrError1_).IsFailure():
            output = (d_963_valueOrError1_).PropagateFailure()
            return output
        d_962_edksToAttempt_ = (d_963_valueOrError1_).Extract()
        d_964_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_964_valueOrError2_ = Wrappers.default__.Need((0) < (len(d_962_edksToAttempt_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to decrypt data key: No Encrypted Data Keys found to match.")))
        if (d_964_valueOrError2_).IsFailure():
            output = (d_964_valueOrError2_).PropagateFailure()
            return output
        d_965_decryptAction_: AwsKmsMrkDiscoveryKeyring.AwsKmsEncryptedDataKeyDecryptor
        nw17_ = AwsKmsMrkDiscoveryKeyring.AwsKmsEncryptedDataKeyDecryptor()
        nw17_.ctor__(d_957_materials_, (self).client, (self).region, (self).grantTokens)
        d_965_decryptAction_ = nw17_
        d_966_outcome_: Wrappers.Result
        out230_: Wrappers.Result
        out230_ = Actions.default__.ReduceToSuccess(d_965_decryptAction_, d_962_edksToAttempt_)
        d_966_outcome_ = out230_
        def lambda62_(source29_):
            if source29_.is_Success:
                d_967___mcc_h0_ = source29_.value
                def iife46_(_pat_let17_0):
                    def iife47_(d_968_mat_):
                        return Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput_OnDecryptOutput(d_968_mat_))
                    return iife47_(_pat_let17_0)
                return iife46_(d_967___mcc_h0_)
            elif True:
                d_969___mcc_h1_ = source29_.error
                def iife48_(_pat_let18_0):
                    def iife49_(d_970_errors_):
                        return Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_CollectionOfErrors(d_970_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`.")))
                    return iife49_(_pat_let18_0)
                return iife48_(d_969___mcc_h1_)

        output = lambda62_(d_966_outcome_)
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
        d_971_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_971_valueOrError0_ = Wrappers.default__.Need(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid AWS KMS encoding, provider info is not UTF8.")))
        if (d_971_valueOrError0_).IsFailure():
            res = (d_971_valueOrError0_).PropagateFailure()
            return res
        d_972_keyId_: _dafny.Seq
        d_973_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda63_(d_974_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(d_974_e_)

        d_973_valueOrError1_ = (UTF8.default__.Decode((edk).keyProviderInfo)).MapFailure(lambda63_)
        if (d_973_valueOrError1_).IsFailure():
            res = (d_973_valueOrError1_).PropagateFailure()
            return res
        d_972_keyId_ = (d_973_valueOrError1_).Extract()
        d_975_arn_: AwsArnParsing.AwsArn
        d_976_valueOrError2_: Wrappers.Result = None
        def lambda64_(d_977_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(d_977_e_)

        d_976_valueOrError2_ = (AwsArnParsing.default__.ParseAwsKmsArn(d_972_keyId_)).MapFailure(lambda64_)
        if (d_976_valueOrError2_).IsFailure():
            res = (d_976_valueOrError2_).PropagateFailure()
            return res
        d_975_arn_ = (d_976_valueOrError2_).Extract()
        d_978_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_978_valueOrError3_ = Wrappers.default__.Need((((d_975_arn_).resource).resourceType) == (_dafny.Seq("key")), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Only AWS KMS Keys supported")))
        if (d_978_valueOrError3_).IsFailure():
            res = (d_978_valueOrError3_).PropagateFailure()
            return res
        if not(AwsKmsMrkDiscoveryKeyring.default__.DiscoveryMatch(d_975_arn_, (self).discoveryFilter, (self).region)):
            res = Wrappers.Result_Success(_dafny.Seq([]))
            return res
        res = Wrappers.Result_Success(_dafny.Seq([Constants.AwsKmsEdkHelper_AwsKmsEdkHelper(edk, d_975_arn_)]))
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
        d_979_awsKmsKey_: _dafny.Seq
        d_979_awsKmsKey_ = AwsKmsMrkDiscoveryKeyring.default__.ToStringForRegion((helper).arn, (self).region)
        d_980___v0_: tuple
        d_981_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        d_981_valueOrError0_ = AwsKmsUtils.default__.ValidateKmsKeyId(d_979_awsKmsKey_)
        if (d_981_valueOrError0_).IsFailure():
            res = (d_981_valueOrError0_).PropagateFailure()
            return res
        d_980___v0_ = (d_981_valueOrError0_).Extract()
        d_982_kmsUnwrap_: AwsKmsKeyring.KmsUnwrapKeyMaterial
        nw18_ = AwsKmsKeyring.KmsUnwrapKeyMaterial()
        nw18_.ctor__((self).client, d_979_awsKmsKey_, (self).grantTokens)
        d_982_kmsUnwrap_ = nw18_
        d_983_unwrapOutputRes_: Wrappers.Result
        out231_: Wrappers.Result
        out231_ = EdkWrapping.default__.UnwrapEdkMaterial(((helper).edk).ciphertext, (self).materials, d_982_kmsUnwrap_)
        d_983_unwrapOutputRes_ = out231_
        d_984_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_985_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(EdkWrapping.UnwrapEdkMaterialOutput.default(AwsKmsKeyring.KmsUnwrapInfo.default()))()
        d_985_valueOrError1_ = d_983_unwrapOutputRes_
        if (d_985_valueOrError1_).IsFailure():
            res = (d_985_valueOrError1_).PropagateFailure()
            return res
        d_984_unwrapOutput_ = (d_985_valueOrError1_).Extract()
        res = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_984_unwrapOutput_).plaintextDataKey, (d_984_unwrapOutput_).symmetricSigningKey)
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
