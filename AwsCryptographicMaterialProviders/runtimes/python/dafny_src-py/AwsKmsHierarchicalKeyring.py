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
import AwsKmsMrkDiscoveryKeyring
import MrkAwareDiscoveryMultiKeyring
import AwsKmsMrkKeyring
import MrkAwareStrictMultiKeyring
import LocalCMC
import software_amazon_cryptography_internaldafny_SynchronizedLocalCMC
import StormTracker
import software_amazon_cryptography_internaldafny_StormTrackingCMC

assert "AwsKmsHierarchicalKeyring" == __name__
AwsKmsHierarchicalKeyring = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def getEntry(cmc, input):
        res: Wrappers.Result = None
        out196_: Wrappers.Result
        out196_ = (cmc).GetCacheEntry(input)
        res = out196_
        return res

    @staticmethod
    def putEntry(cmc, input):
        res: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        out197_: Wrappers.Result
        out197_ = (cmc).PutCacheEntry(input)
        res = out197_
        return res

    @staticmethod
    def DeriveEncryptionKeyFromBranchKey(branchKey, salt, purpose, cryptoPrimitives):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_896_maybeDerivedBranchKey_: Wrappers.Result
        out198_: Wrappers.Result
        out198_ = (cryptoPrimitives).KdfCounterMode(software_amazon_cryptography_primitives_internaldafny_types.KdfCtrInput_KdfCtrInput(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__256(), branchKey, (AwsKmsHierarchicalKeyring.default__).DERIVED__BRANCH__KEY__EXPECTED__LENGTH, purpose, Wrappers.Option_Some(salt)))
        d_896_maybeDerivedBranchKey_ = out198_
        d_897_derivedBranchKey_: _dafny.Seq
        d_898_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda66_(d_899_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_899_e_)

        d_898_valueOrError0_ = (d_896_maybeDerivedBranchKey_).MapFailure(lambda66_)
        if (d_898_valueOrError0_).IsFailure():
            output = (d_898_valueOrError0_).PropagateFailure()
            return output
        d_897_derivedBranchKey_ = (d_898_valueOrError0_).Extract()
        output = Wrappers.Result_Success(d_897_derivedBranchKey_)
        return output

    @staticmethod
    def WrappingAad(branchKeyId, branchKeyVersion, aad):
        return ((((Constants.default__).PROVIDER__ID__HIERARCHY) + (branchKeyId)) + (branchKeyVersion)) + (aad)

    @staticmethod
    def SerializeEDKCiphertext(encOutput):
        return ((encOutput).cipherText) + ((encOutput).authTag)

    @staticmethod
    def E(s):
        return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(s)

    @_dafny.classproperty
    def AES__256__ENC__KEY__LENGTH(instance):
        return 32
    @_dafny.classproperty
    def AES__256__ENC__TAG__LENGTH(instance):
        return 16
    @_dafny.classproperty
    def AES__256__ENC__IV__LENGTH(instance):
        return 12
    @_dafny.classproperty
    def AES__256__ENC__ALG(instance):
        return software_amazon_cryptography_primitives_internaldafny_types.AES__GCM_AES__GCM((AwsKmsHierarchicalKeyring.default__).AES__256__ENC__KEY__LENGTH, (AwsKmsHierarchicalKeyring.default__).AES__256__ENC__TAG__LENGTH, (AwsKmsHierarchicalKeyring.default__).AES__256__ENC__IV__LENGTH)
    @_dafny.classproperty
    def H__WRAP__SALT__LEN(instance):
        return 16
    @_dafny.classproperty
    def H__WRAP__NONCE__LEN(instance):
        return 12
    @_dafny.classproperty
    def EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX(instance):
        return ((AwsKmsHierarchicalKeyring.default__).H__WRAP__SALT__LEN) + ((AwsKmsHierarchicalKeyring.default__).H__WRAP__NONCE__LEN)
    @_dafny.classproperty
    def EDK__CIPHERTEXT__VERSION__LENGTH(instance):
        return 16
    @_dafny.classproperty
    def EDK__CIPHERTEXT__VERSION__INDEX(instance):
        return ((AwsKmsHierarchicalKeyring.default__).EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX) + ((AwsKmsHierarchicalKeyring.default__).EDK__CIPHERTEXT__VERSION__LENGTH)
    @_dafny.classproperty
    def EXPECTED__EDK__CIPHERTEXT__OVERHEAD(instance):
        return ((AwsKmsHierarchicalKeyring.default__).EDK__CIPHERTEXT__VERSION__INDEX) + ((AwsKmsHierarchicalKeyring.default__).AES__256__ENC__TAG__LENGTH)
    @_dafny.classproperty
    def DERIVED__BRANCH__KEY__EXPECTED__LENGTH(instance):
        return 32
    @_dafny.classproperty
    def EXPRESSION__ATTRIBUTE__VALUE__STATUS__VALUE(instance):
        return _dafny.Seq("ACTIVE")
    @_dafny.classproperty
    def BRANCH__KEY__STORE__GSI(instance):
        return _dafny.Seq("Active-Keys")
    @_dafny.classproperty
    def BRANCH__KEY__FIELD(instance):
        return _dafny.Seq("enc")
    @_dafny.classproperty
    def VERSION__FIELD(instance):
        return _dafny.Seq("version")
    @_dafny.classproperty
    def BRANCH__KEY__IDENTIFIER__FIELD(instance):
        return _dafny.Seq("branch-key-id")
    @_dafny.classproperty
    def KEY__CONDITION__EXPRESSION(instance):
        return _dafny.Seq("#status = :status and #branch_key_id = :branch_key_id")
    @_dafny.classproperty
    def EXPRESSION__ATTRIBUTE__NAMES(instance):
        return _dafny.Map({_dafny.Seq("#status"): _dafny.Seq("status"), _dafny.Seq("#branch_key_id"): _dafny.Seq("branch-key-id")})
    @_dafny.classproperty
    def EXPRESSION__ATTRIBUTE__VALUE__STATUS__KEY(instance):
        return _dafny.Seq(":status")
    @_dafny.classproperty
    def EXPRESSION__ATTRIBUTE__VALUE__BRANCH__KEY(instance):
        return _dafny.Seq(":branch_key_id")

class AwsKmsHierarchicalKeyring(Keyring.VerifiableInterface, software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring):
    def  __init__(self):
        self._keyStore: software_amazon_cryptography_keystore_internaldafny_types.IKeyStoreClient = None
        self._cryptoPrimitives: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient = None
        self._branchKeyIdSupplier: Wrappers.Option = Wrappers.Option_None.default()()
        self._branchKeyId: Wrappers.Option = Wrappers.Option_None.default()()
        self._ttlSeconds: BoundedInts.int64 = None
        self._cache: software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsCache = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsHierarchicalKeyring.AwsKmsHierarchicalKeyring"
    def OnEncrypt(self, input):
        out199_: Wrappers.Result
        out199_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnEncrypt(self, input)
        return out199_

    def OnDecrypt(self, input):
        out200_: Wrappers.Result
        out200_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnDecrypt(self, input)
        return out200_

    def ctor__(self, keyStore, branchKeyId, branchKeyIdSupplier, ttlSeconds, cmc, cryptoPrimitives):
        (self)._keyStore = keyStore
        (self)._branchKeyId = branchKeyId
        (self)._branchKeyIdSupplier = branchKeyIdSupplier
        (self)._ttlSeconds = ttlSeconds
        (self)._cryptoPrimitives = cryptoPrimitives
        (self)._cache = cmc

    def GetBranchKeyId(self, context):
        ret: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        if ((self).branchKeyId).is_Some:
            ret = Wrappers.Result_Success(((self).branchKeyId).value)
            return ret
        elif True:
            d_900_GetBranchKeyIdOut_: software_amazon_cryptography_materialproviders_internaldafny_types.GetBranchKeyIdOutput
            d_901_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_materialproviders_internaldafny_types.GetBranchKeyIdOutput.default())()
            out201_: Wrappers.Result
            out201_ = (((self).branchKeyIdSupplier).value).GetBranchKeyId(software_amazon_cryptography_materialproviders_internaldafny_types.GetBranchKeyIdInput_GetBranchKeyIdInput(context))
            d_901_valueOrError0_ = out201_
            if (d_901_valueOrError0_).IsFailure():
                ret = (d_901_valueOrError0_).PropagateFailure()
                return ret
            d_900_GetBranchKeyIdOut_ = (d_901_valueOrError0_).Extract()
            ret = Wrappers.Result_Success((d_900_GetBranchKeyIdOut_).branchKeyId)
            return ret
        return ret

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        d_902_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_902_materials_ = (input).materials
        d_903_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_903_suite_ = (d_902_materials_).algorithmSuite
        d_904_branchKeyIdForEncrypt_: _dafny.Seq
        d_905_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out202_: Wrappers.Result
        out202_ = (self).GetBranchKeyId((d_902_materials_).encryptionContext)
        d_905_valueOrError0_ = out202_
        if (d_905_valueOrError0_).IsFailure():
            res = (d_905_valueOrError0_).PropagateFailure()
            return res
        d_904_branchKeyIdForEncrypt_ = (d_905_valueOrError0_).Extract()
        d_906_branchKeyIdUtf8_: _dafny.Seq
        d_907_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_907_valueOrError1_ = (UTF8.default__.Encode(d_904_branchKeyIdForEncrypt_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_907_valueOrError1_).IsFailure():
            res = (d_907_valueOrError1_).PropagateFailure()
            return res
        d_906_branchKeyIdUtf8_ = (d_907_valueOrError1_).Extract()
        d_908_cacheId_: _dafny.Seq
        d_909_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out203_: Wrappers.Result
        out203_ = (self).GetActiveCacheId(d_904_branchKeyIdForEncrypt_, d_906_branchKeyIdUtf8_, (self).cryptoPrimitives)
        d_909_valueOrError2_ = out203_
        if (d_909_valueOrError2_).IsFailure():
            res = (d_909_valueOrError2_).PropagateFailure()
            return res
        d_908_cacheId_ = (d_909_valueOrError2_).Extract()
        d_910_hierarchicalMaterials_: software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials
        d_911_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials.default())()
        out204_: Wrappers.Result
        out204_ = (self).GetActiveHierarchicalMaterials(d_904_branchKeyIdForEncrypt_, d_908_cacheId_, (self).keyStore)
        d_911_valueOrError3_ = out204_
        if (d_911_valueOrError3_).IsFailure():
            res = (d_911_valueOrError3_).PropagateFailure()
            return res
        d_910_hierarchicalMaterials_ = (d_911_valueOrError3_).Extract()
        d_912_branchKey_: _dafny.Seq
        d_912_branchKey_ = (d_910_hierarchicalMaterials_).branchKey
        d_913_branchKeyVersion_: _dafny.Seq
        d_913_branchKeyVersion_ = (d_910_hierarchicalMaterials_).branchKeyVersion
        d_914_branchKeyVersionAsString_: _dafny.Seq
        d_915_valueOrError4_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_915_valueOrError4_ = (UTF8.default__.Decode(d_913_branchKeyVersion_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_915_valueOrError4_).IsFailure():
            res = (d_915_valueOrError4_).PropagateFailure()
            return res
        d_914_branchKeyVersionAsString_ = (d_915_valueOrError4_).Extract()
        d_916_branchKeyVersionAsBytes_: _dafny.Seq
        d_917_valueOrError5_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_917_valueOrError5_ = (UUID.default__.ToByteArray(d_914_branchKeyVersionAsString_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_917_valueOrError5_).IsFailure():
            res = (d_917_valueOrError5_).PropagateFailure()
            return res
        d_916_branchKeyVersionAsBytes_ = (d_917_valueOrError5_).Extract()
        d_918_kmsHierarchyGenerateAndWrap_: AwsKmsHierarchicalKeyring.KmsHierarchyGenerateAndWrapKeyMaterial
        nw34_ = AwsKmsHierarchicalKeyring.KmsHierarchyGenerateAndWrapKeyMaterial()
        nw34_.ctor__((d_910_hierarchicalMaterials_).branchKey, d_906_branchKeyIdUtf8_, d_916_branchKeyVersionAsBytes_, (self).cryptoPrimitives)
        d_918_kmsHierarchyGenerateAndWrap_ = nw34_
        d_919_kmsHierarchyWrap_: AwsKmsHierarchicalKeyring.KmsHierarchyWrapKeyMaterial
        nw35_ = AwsKmsHierarchicalKeyring.KmsHierarchyWrapKeyMaterial()
        nw35_.ctor__((d_910_hierarchicalMaterials_).branchKey, d_906_branchKeyIdUtf8_, d_916_branchKeyVersionAsBytes_, (self).cryptoPrimitives)
        d_919_kmsHierarchyWrap_ = nw35_
        d_920_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_921_valueOrError6_: Wrappers.Result = Wrappers.Result_Success.default(EdkWrapping.WrapEdkMaterialOutput.default(AwsKmsHierarchicalKeyring.HierarchyWrapInfo.default()))()
        out205_: Wrappers.Result
        out205_ = EdkWrapping.default__.WrapEdkMaterial(d_902_materials_, d_919_kmsHierarchyWrap_, d_918_kmsHierarchyGenerateAndWrap_)
        d_921_valueOrError6_ = out205_
        if (d_921_valueOrError6_).IsFailure():
            res = (d_921_valueOrError6_).PropagateFailure()
            return res
        d_920_wrapOutput_ = (d_921_valueOrError6_).Extract()
        d_922_symmetricSigningKeyList_: Wrappers.Option
        d_922_symmetricSigningKeyList_ = (Wrappers.Option_Some(_dafny.Seq([((d_920_wrapOutput_).symmetricSigningKey).value])) if ((d_920_wrapOutput_).symmetricSigningKey).is_Some else Wrappers.Option_None())
        d_923_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_923_edk_ = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey((Constants.default__).PROVIDER__ID__HIERARCHY, d_906_branchKeyIdUtf8_, (d_920_wrapOutput_).wrappedMaterial)
        if (d_920_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_924_result_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            d_925_valueOrError7_: Wrappers.Result = None
            d_925_valueOrError7_ = Materials.default__.EncryptionMaterialAddDataKey(d_902_materials_, (d_920_wrapOutput_).plaintextDataKey, _dafny.Seq([d_923_edk_]), d_922_symmetricSigningKeyList_)
            if (d_925_valueOrError7_).IsFailure():
                res = (d_925_valueOrError7_).PropagateFailure()
                return res
            d_924_result_ = (d_925_valueOrError7_).Extract()
            res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_924_result_))
            return res
        elif (d_920_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_926_result_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            d_927_valueOrError8_: Wrappers.Result = None
            d_927_valueOrError8_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys(d_902_materials_, _dafny.Seq([d_923_edk_]), d_922_symmetricSigningKeyList_)
            if (d_927_valueOrError8_).IsFailure():
                res = (d_927_valueOrError8_).PropagateFailure()
                return res
            d_926_result_ = (d_927_valueOrError8_).Extract()
            res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_926_result_))
            return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_928_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_928_materials_ = (input).materials
        d_929_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_929_suite_ = ((input).materials).algorithmSuite
        d_930_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_930_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_928_materials_), AwsKmsHierarchicalKeyring.default__.E(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_930_valueOrError0_).IsFailure():
            res = (d_930_valueOrError0_).PropagateFailure()
            return res
        d_931_branchKeyIdForDecrypt_: _dafny.Seq
        d_932_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out206_: Wrappers.Result
        out206_ = (self).GetBranchKeyId((d_928_materials_).encryptionContext)
        d_932_valueOrError1_ = out206_
        if (d_932_valueOrError1_).IsFailure():
            res = (d_932_valueOrError1_).PropagateFailure()
            return res
        d_931_branchKeyIdForDecrypt_ = (d_932_valueOrError1_).Extract()
        d_933_filter_: AwsKmsHierarchicalKeyring.OnDecryptHierarchyEncryptedDataKeyFilter
        nw36_ = AwsKmsHierarchicalKeyring.OnDecryptHierarchyEncryptedDataKeyFilter()
        nw36_.ctor__(d_931_branchKeyIdForDecrypt_)
        d_933_filter_ = nw36_
        d_934_edksToAttempt_: _dafny.Seq
        d_935_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out207_: Wrappers.Result
        out207_ = Actions.default__.FilterWithResult(d_933_filter_, (input).encryptedDataKeys)
        d_935_valueOrError2_ = out207_
        if (d_935_valueOrError2_).IsFailure():
            res = (d_935_valueOrError2_).PropagateFailure()
            return res
        d_934_edksToAttempt_ = (d_935_valueOrError2_).Extract()
        d_936_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_936_valueOrError3_ = Wrappers.default__.Need((0) < (len(d_934_edksToAttempt_)), AwsKmsHierarchicalKeyring.default__.E(_dafny.Seq("Unable to decrypt data key: No Encrypted Data Keys found to match.")))
        if (d_936_valueOrError3_).IsFailure():
            res = (d_936_valueOrError3_).PropagateFailure()
            return res
        d_937_decryptClosure_: Actions.ActionWithResult
        nw37_ = AwsKmsHierarchicalKeyring.DecryptSingleEncryptedDataKey()
        nw37_.ctor__(d_928_materials_, (self).keyStore, (self).cryptoPrimitives, d_931_branchKeyIdForDecrypt_, (self).ttlSeconds, (self).cache)
        d_937_decryptClosure_ = nw37_
        d_938_outcome_: Wrappers.Result
        out208_: Wrappers.Result
        out208_ = Actions.default__.ReduceToSuccess(d_937_decryptClosure_, d_934_edksToAttempt_)
        d_938_outcome_ = out208_
        d_939_SealedDecryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_940_valueOrError4_: Wrappers.Result = None
        def lambda67_(d_941_errors_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_CollectionOfErrors(d_941_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."))

        d_940_valueOrError4_ = (d_938_outcome_).MapFailure(lambda67_)
        if (d_940_valueOrError4_).IsFailure():
            res = (d_940_valueOrError4_).PropagateFailure()
            return res
        d_939_SealedDecryptionMaterials_ = (d_940_valueOrError4_).Extract()
        res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput_OnDecryptOutput(d_939_SealedDecryptionMaterials_))
        return res
        return res

    def GetActiveCacheId(self, branchKeyId, branchKeyIdUtf8, cryptoPrimitives):
        cacheId: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_942_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        def iife48_(_pat_let19_0):
            def iife49_(d_943_branchKeyId_):
                return (True) and (((0) <= (len(d_943_branchKeyId_))) and ((len(d_943_branchKeyId_)) < ((StandardLibrary_mUInt.default__).UINT32__LIMIT)))
            return iife49_(_pat_let19_0)
        d_942_valueOrError0_ = Wrappers.default__.Need((((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).is_Success) and (iife48_(((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).value)), AwsKmsHierarchicalKeyring.default__.E(_dafny.Seq("Invalid Branch Key ID Length")))
        if (d_942_valueOrError0_).IsFailure():
            cacheId = (d_942_valueOrError0_).PropagateFailure()
            return cacheId
        d_944_branchKeyId_: _dafny.Seq
        d_944_branchKeyId_ = (UTF8.default__.Decode(branchKeyIdUtf8)).value
        d_945_lenBranchKey_: _dafny.Seq
        d_945_lenBranchKey_ = StandardLibrary_mUInt.default__.UInt32ToSeq(len(d_944_branchKeyId_))
        d_946_hashAlgorithm_: software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm
        d_946_hashAlgorithm_ = software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__512()
        d_947_maybeBranchKeyDigest_: Wrappers.Result
        out209_: Wrappers.Result
        out209_ = (cryptoPrimitives).Digest(software_amazon_cryptography_primitives_internaldafny_types.DigestInput_DigestInput(d_946_hashAlgorithm_, branchKeyIdUtf8))
        d_947_maybeBranchKeyDigest_ = out209_
        d_948_branchKeyDigest_: _dafny.Seq
        d_949_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda68_(d_950_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_950_e_)

        d_949_valueOrError1_ = (d_947_maybeBranchKeyDigest_).MapFailure(lambda68_)
        if (d_949_valueOrError1_).IsFailure():
            cacheId = (d_949_valueOrError1_).PropagateFailure()
            return cacheId
        d_948_branchKeyDigest_ = (d_949_valueOrError1_).Extract()
        d_951_activeUtf8_: _dafny.Seq
        d_952_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_952_valueOrError2_ = (UTF8.default__.Encode((AwsKmsHierarchicalKeyring.default__).EXPRESSION__ATTRIBUTE__VALUE__STATUS__VALUE)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_952_valueOrError2_).IsFailure():
            cacheId = (d_952_valueOrError2_).PropagateFailure()
            return cacheId
        d_951_activeUtf8_ = (d_952_valueOrError2_).Extract()
        d_953_identifier_: _dafny.Seq
        d_953_identifier_ = (((d_945_lenBranchKey_) + (d_948_branchKeyDigest_)) + (_dafny.Seq([0]))) + (d_951_activeUtf8_)
        d_954_maybeCacheIdDigest_: Wrappers.Result
        out210_: Wrappers.Result
        out210_ = (cryptoPrimitives).Digest(software_amazon_cryptography_primitives_internaldafny_types.DigestInput_DigestInput(d_946_hashAlgorithm_, d_953_identifier_))
        d_954_maybeCacheIdDigest_ = out210_
        d_955_cacheDigest_: _dafny.Seq
        d_956_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda69_(d_957_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_957_e_)

        d_956_valueOrError3_ = (d_954_maybeCacheIdDigest_).MapFailure(lambda69_)
        if (d_956_valueOrError3_).IsFailure():
            cacheId = (d_956_valueOrError3_).PropagateFailure()
            return cacheId
        d_955_cacheDigest_ = (d_956_valueOrError3_).Extract()
        d_958_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_958_valueOrError4_ = Wrappers.default__.Need((len(d_955_cacheDigest_)) == (Digest.default__.Length(d_946_hashAlgorithm_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Digest generated a message not equal to the expected length.")))
        if (d_958_valueOrError4_).IsFailure():
            cacheId = (d_958_valueOrError4_).PropagateFailure()
            return cacheId
        cacheId = Wrappers.Result_Success(_dafny.Seq((d_955_cacheDigest_)[0:32:]))
        return cacheId
        return cacheId

    def GetActiveHierarchicalMaterials(self, branchKeyId, cacheId, keyStore):
        material: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials.default())()
        d_959_getCacheInput_: software_amazon_cryptography_materialproviders_internaldafny_types.GetCacheEntryInput
        d_959_getCacheInput_ = software_amazon_cryptography_materialproviders_internaldafny_types.GetCacheEntryInput_GetCacheEntryInput(cacheId, Wrappers.Option_None())
        d_960_getCacheOutput_: Wrappers.Result
        out211_: Wrappers.Result
        out211_ = AwsKmsHierarchicalKeyring.default__.getEntry((self).cache, d_959_getCacheInput_)
        d_960_getCacheOutput_ = out211_
        if (d_960_getCacheOutput_).is_Failure:
            d_961_maybeGetActiveBranchKeyOutput_: Wrappers.Result
            out212_: Wrappers.Result
            out212_ = (keyStore).GetActiveBranchKey(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyInput_GetActiveBranchKeyInput(branchKeyId))
            d_961_maybeGetActiveBranchKeyOutput_ = out212_
            d_962_getActiveBranchKeyOutput_: software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput
            d_963_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput.default())()
            def lambda70_(d_964_e_):
                return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyKeyStore(d_964_e_)

            d_963_valueOrError0_ = (d_961_maybeGetActiveBranchKeyOutput_).MapFailure(lambda70_)
            if (d_963_valueOrError0_).IsFailure():
                material = (d_963_valueOrError0_).PropagateFailure()
                return material
            d_962_getActiveBranchKeyOutput_ = (d_963_valueOrError0_).Extract()
            d_965_branchKeyMaterials_: software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials
            d_965_branchKeyMaterials_ = (d_962_getActiveBranchKeyOutput_).branchKeyMaterials
            d_966_now_: BoundedInts.int64
            out213_: BoundedInts.int64
            out213_ = Time.default__.CurrentRelativeTime()
            d_966_now_ = out213_
            d_967_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
            d_967_valueOrError1_ = Wrappers.default__.Need(((d_966_now_) + ((self).ttlSeconds)) < ((StandardLibrary_mUInt.default__).INT64__MAX__LIMIT), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("INT64 Overflow when putting cache entry.")))
            if (d_967_valueOrError1_).IsFailure():
                material = (d_967_valueOrError1_).PropagateFailure()
                return material
            d_968_putCacheEntryInput_: software_amazon_cryptography_materialproviders_internaldafny_types.PutCacheEntryInput
            d_968_putCacheEntryInput_ = software_amazon_cryptography_materialproviders_internaldafny_types.PutCacheEntryInput_PutCacheEntryInput(cacheId, software_amazon_cryptography_materialproviders_internaldafny_types.Materials_BranchKey(d_965_branchKeyMaterials_), d_966_now_, ((self).ttlSeconds) + (d_966_now_), Wrappers.Option_None(), Wrappers.Option_None())
            d_969___v0_: tuple
            d_970_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
            out214_: Wrappers.Result
            out214_ = AwsKmsHierarchicalKeyring.default__.putEntry((self).cache, d_968_putCacheEntryInput_)
            d_970_valueOrError2_ = out214_
            if (d_970_valueOrError2_).IsFailure():
                material = (d_970_valueOrError2_).PropagateFailure()
                return material
            d_969___v0_ = (d_970_valueOrError2_).Extract()
            material = Wrappers.Result_Success(d_965_branchKeyMaterials_)
            return material
        elif True:
            d_971_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
            d_971_valueOrError3_ = Wrappers.default__.Need(((((d_960_getCacheOutput_).value).materials).is_BranchKey) and ((((d_960_getCacheOutput_).value).materials) == (software_amazon_cryptography_materialproviders_internaldafny_types.Materials_BranchKey((((d_960_getCacheOutput_).value).materials).BranchKey))), AwsKmsHierarchicalKeyring.default__.E(_dafny.Seq("Invalid Material Type.")))
            if (d_971_valueOrError3_).IsFailure():
                material = (d_971_valueOrError3_).PropagateFailure()
                return material
            material = Wrappers.Result_Success((((d_960_getCacheOutput_).value).materials).BranchKey)
            return material
        return material

    @property
    def keyStore(self):
        return self._keyStore
    @property
    def cryptoPrimitives(self):
        return self._cryptoPrimitives
    @property
    def branchKeyIdSupplier(self):
        return self._branchKeyIdSupplier
    @property
    def branchKeyId(self):
        return self._branchKeyId
    @property
    def ttlSeconds(self):
        return self._ttlSeconds
    @property
    def cache(self):
        return self._cache

class OnDecryptHierarchyEncryptedDataKeyFilter(Actions.DeterministicActionWithResult, Actions.DeterministicAction):
    def  __init__(self):
        self._branchKeyId: _dafny.Seq = _dafny.Seq({})
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsHierarchicalKeyring.OnDecryptHierarchyEncryptedDataKeyFilter"
    def ctor__(self, branchKeyId):
        (self)._branchKeyId = branchKeyId

    def Invoke(self, edk):
        res: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.bool)()
        d_972_providerInfo_: _dafny.Seq
        d_972_providerInfo_ = (edk).keyProviderInfo
        d_973_providerId_: _dafny.Seq
        d_973_providerId_ = (edk).keyProviderId
        if (d_973_providerId_) != ((Constants.default__).PROVIDER__ID__HIERARCHY):
            res = Wrappers.Result_Success(False)
            return res
        if not(UTF8.default__.ValidUTF8Seq(d_972_providerInfo_)):
            res = Wrappers.Result_Failure(AwsKmsHierarchicalKeyring.default__.E(_dafny.Seq("Invalid encoding, provider info is not UTF8.")))
            return res
        d_974_branchKeyId_: _dafny.Seq
        d_975_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_975_valueOrError0_ = (UTF8.default__.Decode(d_972_providerInfo_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_975_valueOrError0_).IsFailure():
            res = (d_975_valueOrError0_).PropagateFailure()
            return res
        d_974_branchKeyId_ = (d_975_valueOrError0_).Extract()
        res = Wrappers.Result_Success(((self).branchKeyId) == (d_974_branchKeyId_))
        return res
        return res

    @property
    def branchKeyId(self):
        return self._branchKeyId

class DecryptSingleEncryptedDataKey(Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._materials: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials = None
        self._keyStore: software_amazon_cryptography_keystore_internaldafny_types.IKeyStoreClient = None
        self._cryptoPrimitives: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient = None
        self._branchKeyId: _dafny.Seq = _dafny.Seq({})
        self._ttlSeconds: BoundedInts.int64 = None
        self._cache: software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsCache = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsHierarchicalKeyring.DecryptSingleEncryptedDataKey"
    def ctor__(self, materials, keyStore, cryptoPrimitives, branchKeyId, ttlSeconds, cache):
        (self)._materials = materials
        (self)._keyStore = keyStore
        (self)._cryptoPrimitives = cryptoPrimitives
        (self)._branchKeyId = branchKeyId
        (self)._ttlSeconds = ttlSeconds
        (self)._cache = cache

    def Invoke(self, edk):
        res: Wrappers.Result = None
        d_976_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_976_valueOrError0_ = Wrappers.default__.Need(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received invalid EDK provider info for Hierarchical Keyring")))
        if (d_976_valueOrError0_).IsFailure():
            res = (d_976_valueOrError0_).PropagateFailure()
            return res
        d_977_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_977_suite_ = ((self).materials).algorithmSuite
        d_978_keyProviderId_: _dafny.Seq
        d_978_keyProviderId_ = (edk).keyProviderId
        d_979_branchKeyIdUtf8_: _dafny.Seq
        d_979_branchKeyIdUtf8_ = (edk).keyProviderInfo
        d_980_ciphertext_: _dafny.Seq
        d_980_ciphertext_ = (edk).ciphertext
        d_981_providerWrappedMaterial_: _dafny.Seq
        d_982_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_982_valueOrError1_ = EdkWrapping.default__.GetProviderWrappedMaterial(d_980_ciphertext_, d_977_suite_)
        if (d_982_valueOrError1_).IsFailure():
            res = (d_982_valueOrError1_).PropagateFailure()
            return res
        d_981_providerWrappedMaterial_ = (d_982_valueOrError1_).Extract()
        d_983_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_983_valueOrError2_ = Wrappers.default__.Need((len(d_981_providerWrappedMaterial_)) >= ((AwsKmsHierarchicalKeyring.default__).EDK__CIPHERTEXT__VERSION__INDEX), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received EDK Ciphertext of incorrect length.")))
        if (d_983_valueOrError2_).IsFailure():
            res = (d_983_valueOrError2_).PropagateFailure()
            return res
        d_984_branchKeyVersionUuid_: _dafny.Seq
        d_984_branchKeyVersionUuid_ = _dafny.Seq((d_981_providerWrappedMaterial_)[(AwsKmsHierarchicalKeyring.default__).EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX:(AwsKmsHierarchicalKeyring.default__).EDK__CIPHERTEXT__VERSION__INDEX:])
        d_985_version_: _dafny.Seq
        d_986_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_986_valueOrError3_ = (UUID.default__.FromByteArray(d_984_branchKeyVersionUuid_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_986_valueOrError3_).IsFailure():
            res = (d_986_valueOrError3_).PropagateFailure()
            return res
        d_985_version_ = (d_986_valueOrError3_).Extract()
        d_987_cacheId_: _dafny.Seq
        d_988_valueOrError4_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out215_: Wrappers.Result
        out215_ = (self).GetVersionCacheId(d_979_branchKeyIdUtf8_, d_985_version_, (self).cryptoPrimitives)
        d_988_valueOrError4_ = out215_
        if (d_988_valueOrError4_).IsFailure():
            res = (d_988_valueOrError4_).PropagateFailure()
            return res
        d_987_cacheId_ = (d_988_valueOrError4_).Extract()
        d_989_hierarchicalMaterials_: software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials
        d_990_valueOrError5_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials.default())()
        out216_: Wrappers.Result
        out216_ = (self).GetHierarchicalMaterialsVersion((self).branchKeyId, d_979_branchKeyIdUtf8_, d_985_version_, d_987_cacheId_)
        d_990_valueOrError5_ = out216_
        if (d_990_valueOrError5_).IsFailure():
            res = (d_990_valueOrError5_).PropagateFailure()
            return res
        d_989_hierarchicalMaterials_ = (d_990_valueOrError5_).Extract()
        d_991_branchKey_: _dafny.Seq
        d_991_branchKey_ = (d_989_hierarchicalMaterials_).branchKey
        d_992_branchKeyVersion_: _dafny.Seq
        d_992_branchKeyVersion_ = (d_989_hierarchicalMaterials_).branchKeyVersion
        d_993_branchKeyVersionAsString_: _dafny.Seq
        d_994_valueOrError6_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_994_valueOrError6_ = (UTF8.default__.Decode(d_992_branchKeyVersion_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_994_valueOrError6_).IsFailure():
            res = (d_994_valueOrError6_).PropagateFailure()
            return res
        d_993_branchKeyVersionAsString_ = (d_994_valueOrError6_).Extract()
        d_995_branchKeyVersionAsBytes_: _dafny.Seq
        d_996_valueOrError7_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_996_valueOrError7_ = (UUID.default__.ToByteArray(d_993_branchKeyVersionAsString_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_996_valueOrError7_).IsFailure():
            res = (d_996_valueOrError7_).PropagateFailure()
            return res
        d_995_branchKeyVersionAsBytes_ = (d_996_valueOrError7_).Extract()
        d_997_maybeCrypto_: Wrappers.Result
        out217_: Wrappers.Result
        out217_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_997_maybeCrypto_ = out217_
        d_998_crypto_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_999_valueOrError8_: Wrappers.Result = None
        def lambda71_(d_1000_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1000_e_)

        d_999_valueOrError8_ = (d_997_maybeCrypto_).MapFailure(lambda71_)
        if (d_999_valueOrError8_).IsFailure():
            res = (d_999_valueOrError8_).PropagateFailure()
            return res
        d_998_crypto_ = (d_999_valueOrError8_).Extract()
        d_1001_kmsHierarchyUnwrap_: AwsKmsHierarchicalKeyring.KmsHierarchyUnwrapKeyMaterial
        nw38_ = AwsKmsHierarchicalKeyring.KmsHierarchyUnwrapKeyMaterial()
        nw38_.ctor__(d_991_branchKey_, d_979_branchKeyIdUtf8_, d_995_branchKeyVersionAsBytes_, d_998_crypto_)
        d_1001_kmsHierarchyUnwrap_ = nw38_
        d_1002_unwrapOutputRes_: Wrappers.Result
        out218_: Wrappers.Result
        out218_ = EdkWrapping.default__.UnwrapEdkMaterial((edk).ciphertext, (self).materials, d_1001_kmsHierarchyUnwrap_)
        d_1002_unwrapOutputRes_ = out218_
        d_1003_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_1004_valueOrError9_: Wrappers.Result = Wrappers.Result_Success.default(EdkWrapping.UnwrapEdkMaterialOutput.default(AwsKmsHierarchicalKeyring.HierarchyUnwrapInfo.default()))()
        d_1004_valueOrError9_ = d_1002_unwrapOutputRes_
        if (d_1004_valueOrError9_).IsFailure():
            res = (d_1004_valueOrError9_).PropagateFailure()
            return res
        d_1003_unwrapOutput_ = (d_1004_valueOrError9_).Extract()
        d_1005_result_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1006_valueOrError10_: Wrappers.Result = None
        d_1006_valueOrError10_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_1003_unwrapOutput_).plaintextDataKey, (d_1003_unwrapOutput_).symmetricSigningKey)
        if (d_1006_valueOrError10_).IsFailure():
            res = (d_1006_valueOrError10_).PropagateFailure()
            return res
        d_1005_result_ = (d_1006_valueOrError10_).Extract()
        res = Wrappers.Result_Success(d_1005_result_)
        return res
        return res

    def GetVersionCacheId(self, branchKeyIdUtf8, branchKeyVersion, cryptoPrimitives):
        cacheId: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1007_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        def iife50_(_pat_let20_0):
            def iife51_(d_1008_branchKeyId_):
                return (True) and (((0) <= (len(d_1008_branchKeyId_))) and ((len(d_1008_branchKeyId_)) < ((StandardLibrary_mUInt.default__).UINT32__LIMIT)))
            return iife51_(_pat_let20_0)
        d_1007_valueOrError0_ = Wrappers.default__.Need((((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).is_Success) and (iife50_(((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).value)), AwsKmsHierarchicalKeyring.default__.E(_dafny.Seq("Invalid Branch Key ID Length")))
        if (d_1007_valueOrError0_).IsFailure():
            cacheId = (d_1007_valueOrError0_).PropagateFailure()
            return cacheId
        d_1009_branchKeyId_: _dafny.Seq
        d_1009_branchKeyId_ = (UTF8.default__.Decode(branchKeyIdUtf8)).value
        d_1010_lenBranchKey_: _dafny.Seq
        d_1010_lenBranchKey_ = StandardLibrary_mUInt.default__.UInt32ToSeq(len(d_1009_branchKeyId_))
        d_1011_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1011_valueOrError1_ = Wrappers.default__.Need(UTF8.default__.IsASCIIString(branchKeyVersion), AwsKmsHierarchicalKeyring.default__.E(_dafny.Seq("Unable to represent as an ASCII string.")))
        if (d_1011_valueOrError1_).IsFailure():
            cacheId = (d_1011_valueOrError1_).PropagateFailure()
            return cacheId
        d_1012_versionBytes_: _dafny.Seq
        d_1012_versionBytes_ = UTF8.default__.EncodeAscii(branchKeyVersion)
        d_1013_identifier_: _dafny.Seq
        d_1013_identifier_ = (((d_1010_lenBranchKey_) + (branchKeyIdUtf8)) + (_dafny.Seq([0]))) + (d_1012_versionBytes_)
        d_1014_identifierDigestInput_: software_amazon_cryptography_primitives_internaldafny_types.DigestInput
        d_1014_identifierDigestInput_ = software_amazon_cryptography_primitives_internaldafny_types.DigestInput_DigestInput(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__512(), d_1013_identifier_)
        d_1015_maybeCacheDigest_: Wrappers.Result
        out219_: Wrappers.Result
        out219_ = Digest.default__.Digest(d_1014_identifierDigestInput_)
        d_1015_maybeCacheDigest_ = out219_
        d_1016_cacheDigest_: _dafny.Seq
        d_1017_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda72_(d_1018_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1018_e_)

        d_1017_valueOrError2_ = (d_1015_maybeCacheDigest_).MapFailure(lambda72_)
        if (d_1017_valueOrError2_).IsFailure():
            cacheId = (d_1017_valueOrError2_).PropagateFailure()
            return cacheId
        d_1016_cacheDigest_ = (d_1017_valueOrError2_).Extract()
        cacheId = Wrappers.Result_Success(_dafny.Seq((d_1016_cacheDigest_)[0:32:]))
        return cacheId
        return cacheId

    def GetHierarchicalMaterialsVersion(self, branchKeyId, branchKeyIdUtf8, version, cacheId):
        material: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials.default())()
        d_1019_getCacheInput_: software_amazon_cryptography_materialproviders_internaldafny_types.GetCacheEntryInput
        d_1019_getCacheInput_ = software_amazon_cryptography_materialproviders_internaldafny_types.GetCacheEntryInput_GetCacheEntryInput(cacheId, Wrappers.Option_None())
        d_1020_getCacheOutput_: Wrappers.Result
        out220_: Wrappers.Result
        out220_ = AwsKmsHierarchicalKeyring.default__.getEntry((self).cache, d_1019_getCacheInput_)
        d_1020_getCacheOutput_ = out220_
        if (d_1020_getCacheOutput_).is_Failure:
            d_1021_maybeGetBranchKeyVersionOutput_: Wrappers.Result
            out221_: Wrappers.Result
            out221_ = ((self).keyStore).GetBranchKeyVersion(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionInput_GetBranchKeyVersionInput(branchKeyId, version))
            d_1021_maybeGetBranchKeyVersionOutput_ = out221_
            d_1022_getBranchKeyVersionOutput_: software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput
            d_1023_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput.default())()
            def lambda73_(d_1024_e_):
                return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyKeyStore(d_1024_e_)

            d_1023_valueOrError0_ = (d_1021_maybeGetBranchKeyVersionOutput_).MapFailure(lambda73_)
            if (d_1023_valueOrError0_).IsFailure():
                material = (d_1023_valueOrError0_).PropagateFailure()
                return material
            d_1022_getBranchKeyVersionOutput_ = (d_1023_valueOrError0_).Extract()
            d_1025_branchKeyMaterials_: software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials
            d_1025_branchKeyMaterials_ = (d_1022_getBranchKeyVersionOutput_).branchKeyMaterials
            d_1026_now_: BoundedInts.int64
            out222_: BoundedInts.int64
            out222_ = Time.default__.CurrentRelativeTime()
            d_1026_now_ = out222_
            d_1027_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
            d_1027_valueOrError1_ = Wrappers.default__.Need(((d_1026_now_) + ((self).ttlSeconds)) < ((StandardLibrary_mUInt.default__).INT64__MAX__LIMIT), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("INT64 Overflow when putting cache entry.")))
            if (d_1027_valueOrError1_).IsFailure():
                material = (d_1027_valueOrError1_).PropagateFailure()
                return material
            d_1028_putCacheEntryInput_: software_amazon_cryptography_materialproviders_internaldafny_types.PutCacheEntryInput
            d_1028_putCacheEntryInput_ = software_amazon_cryptography_materialproviders_internaldafny_types.PutCacheEntryInput_PutCacheEntryInput(cacheId, software_amazon_cryptography_materialproviders_internaldafny_types.Materials_BranchKey(d_1025_branchKeyMaterials_), d_1026_now_, ((self).ttlSeconds) + (d_1026_now_), Wrappers.Option_None(), Wrappers.Option_None())
            d_1029___v1_: tuple
            d_1030_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
            out223_: Wrappers.Result
            out223_ = AwsKmsHierarchicalKeyring.default__.putEntry((self).cache, d_1028_putCacheEntryInput_)
            d_1030_valueOrError2_ = out223_
            if (d_1030_valueOrError2_).IsFailure():
                material = (d_1030_valueOrError2_).PropagateFailure()
                return material
            d_1029___v1_ = (d_1030_valueOrError2_).Extract()
            material = Wrappers.Result_Success(d_1025_branchKeyMaterials_)
            return material
        elif True:
            d_1031_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
            d_1031_valueOrError3_ = Wrappers.default__.Need(((((d_1020_getCacheOutput_).value).materials).is_BranchKey) and ((((d_1020_getCacheOutput_).value).materials) == (software_amazon_cryptography_materialproviders_internaldafny_types.Materials_BranchKey((((d_1020_getCacheOutput_).value).materials).BranchKey))), AwsKmsHierarchicalKeyring.default__.E(_dafny.Seq("Invalid Material Type.")))
            if (d_1031_valueOrError3_).IsFailure():
                material = (d_1031_valueOrError3_).PropagateFailure()
                return material
            material = Wrappers.Result_Success((((d_1020_getCacheOutput_).value).materials).BranchKey)
            return material
        return material

    @property
    def materials(self):
        return self._materials
    @property
    def keyStore(self):
        return self._keyStore
    @property
    def cryptoPrimitives(self):
        return self._cryptoPrimitives
    @property
    def branchKeyId(self):
        return self._branchKeyId
    @property
    def ttlSeconds(self):
        return self._ttlSeconds
    @property
    def cache(self):
        return self._cache

class HierarchyUnwrapInfo:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [HierarchyUnwrapInfo_HierarchyUnwrapInfo()]
    @classmethod
    def default(cls, ):
        return lambda: HierarchyUnwrapInfo_HierarchyUnwrapInfo()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_HierarchyUnwrapInfo(self) -> bool:
        return isinstance(self, AwsKmsHierarchicalKeyring.HierarchyUnwrapInfo_HierarchyUnwrapInfo)

class HierarchyUnwrapInfo_HierarchyUnwrapInfo(HierarchyUnwrapInfo, NamedTuple('HierarchyUnwrapInfo', [])):
    def __dafnystr__(self) -> str:
        return f'AwsKmsHierarchicalKeyring.HierarchyUnwrapInfo.HierarchyUnwrapInfo'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AwsKmsHierarchicalKeyring.HierarchyUnwrapInfo_HierarchyUnwrapInfo)
    def __hash__(self) -> int:
        return super().__hash__()


class HierarchyWrapInfo:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [HierarchyWrapInfo_HierarchyWrapInfo()]
    @classmethod
    def default(cls, ):
        return lambda: HierarchyWrapInfo_HierarchyWrapInfo()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_HierarchyWrapInfo(self) -> bool:
        return isinstance(self, AwsKmsHierarchicalKeyring.HierarchyWrapInfo_HierarchyWrapInfo)

class HierarchyWrapInfo_HierarchyWrapInfo(HierarchyWrapInfo, NamedTuple('HierarchyWrapInfo', [])):
    def __dafnystr__(self) -> str:
        return f'AwsKmsHierarchicalKeyring.HierarchyWrapInfo.HierarchyWrapInfo'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AwsKmsHierarchicalKeyring.HierarchyWrapInfo_HierarchyWrapInfo)
    def __hash__(self) -> int:
        return super().__hash__()


class KmsHierarchyUnwrapKeyMaterial(MaterialWrapping.UnwrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._crypto: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient = None
        self._branchKeyIdUtf8: _dafny.Seq = UTF8.ValidUTF8Bytes.default()
        self._branchKeyVersionAsBytes: _dafny.Seq = _dafny.Seq({})
        self._branchKey: _dafny.Seq = _dafny.Seq({})
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsHierarchicalKeyring.KmsHierarchyUnwrapKeyMaterial"
    def ctor__(self, branchKey, branchKeyIdUtf8, branchKeyVersionAsBytes, crypto):
        (self)._branchKey = branchKey
        (self)._branchKeyIdUtf8 = branchKeyIdUtf8
        (self)._branchKeyVersionAsBytes = branchKeyVersionAsBytes
        (self)._crypto = crypto

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result_Success.default(MaterialWrapping.UnwrapOutput.default(AwsKmsHierarchicalKeyring.HierarchyUnwrapInfo.default()))()
        d_1032_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_1032_suite_ = (input).algorithmSuite
        d_1033_wrappedMaterial_: _dafny.Seq
        d_1033_wrappedMaterial_ = (input).wrappedMaterial
        d_1034_aad_: _dafny.Map
        d_1034_aad_ = (input).encryptionContext
        d_1035_KeyLength_: BoundedInts.int32
        d_1035_KeyLength_ = AlgorithmSuites.default__.GetEncryptKeyLength(d_1032_suite_)
        d_1036_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1036_valueOrError0_ = Wrappers.default__.Need((len(d_1033_wrappedMaterial_)) == (((AwsKmsHierarchicalKeyring.default__).EXPECTED__EDK__CIPHERTEXT__OVERHEAD) + (d_1035_KeyLength_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received EDK Ciphertext of incorrect length2.")))
        if (d_1036_valueOrError0_).IsFailure():
            res = (d_1036_valueOrError0_).PropagateFailure()
            return res
        d_1037_salt_: _dafny.Seq
        d_1037_salt_ = _dafny.Seq((d_1033_wrappedMaterial_)[0:(AwsKmsHierarchicalKeyring.default__).H__WRAP__SALT__LEN:])
        d_1038_iv_: _dafny.Seq
        d_1038_iv_ = _dafny.Seq((d_1033_wrappedMaterial_)[(AwsKmsHierarchicalKeyring.default__).H__WRAP__SALT__LEN:(AwsKmsHierarchicalKeyring.default__).EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX:])
        d_1039_branchKeyVersionUuid_: _dafny.Seq
        d_1039_branchKeyVersionUuid_ = _dafny.Seq((d_1033_wrappedMaterial_)[(AwsKmsHierarchicalKeyring.default__).EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX:(AwsKmsHierarchicalKeyring.default__).EDK__CIPHERTEXT__VERSION__INDEX:])
        d_1040_wrappedKey_: _dafny.Seq
        d_1040_wrappedKey_ = _dafny.Seq((d_1033_wrappedMaterial_)[(AwsKmsHierarchicalKeyring.default__).EDK__CIPHERTEXT__VERSION__INDEX:((AwsKmsHierarchicalKeyring.default__).EDK__CIPHERTEXT__VERSION__INDEX) + (d_1035_KeyLength_):])
        d_1041_authTag_: _dafny.Seq
        d_1041_authTag_ = _dafny.Seq((d_1033_wrappedMaterial_)[((AwsKmsHierarchicalKeyring.default__).EDK__CIPHERTEXT__VERSION__INDEX) + (d_1035_KeyLength_)::])
        d_1042_serializedEC_: _dafny.Seq
        d_1043_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1043_valueOrError1_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_1043_valueOrError1_).IsFailure():
            res = (d_1043_valueOrError1_).PropagateFailure()
            return res
        d_1042_serializedEC_ = (d_1043_valueOrError1_).Extract()
        d_1044_wrappingAad_: _dafny.Seq
        d_1044_wrappingAad_ = AwsKmsHierarchicalKeyring.default__.WrappingAad((self).branchKeyIdUtf8, (self).branchKeyVersionAsBytes, d_1042_serializedEC_)
        d_1045_derivedBranchKey_: _dafny.Seq
        d_1046_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out224_: Wrappers.Result
        out224_ = AwsKmsHierarchicalKeyring.default__.DeriveEncryptionKeyFromBranchKey((self).branchKey, d_1037_salt_, Wrappers.Option_Some((Constants.default__).PROVIDER__ID__HIERARCHY), (self).crypto)
        d_1046_valueOrError2_ = out224_
        if (d_1046_valueOrError2_).IsFailure():
            res = (d_1046_valueOrError2_).PropagateFailure()
            return res
        d_1045_derivedBranchKey_ = (d_1046_valueOrError2_).Extract()
        d_1047_maybeUnwrappedPdk_: Wrappers.Result
        out225_: Wrappers.Result
        out225_ = ((self).crypto).AESDecrypt(software_amazon_cryptography_primitives_internaldafny_types.AESDecryptInput_AESDecryptInput((AwsKmsHierarchicalKeyring.default__).AES__256__ENC__ALG, d_1045_derivedBranchKey_, d_1040_wrappedKey_, d_1041_authTag_, d_1038_iv_, d_1044_wrappingAad_))
        d_1047_maybeUnwrappedPdk_ = out225_
        d_1048_unwrappedPdk_: _dafny.Seq
        d_1049_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda74_(d_1050_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1050_e_)

        d_1049_valueOrError3_ = (d_1047_maybeUnwrappedPdk_).MapFailure(lambda74_)
        if (d_1049_valueOrError3_).IsFailure():
            res = (d_1049_valueOrError3_).PropagateFailure()
            return res
        d_1048_unwrappedPdk_ = (d_1049_valueOrError3_).Extract()
        d_1051_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1051_valueOrError4_ = Wrappers.default__.Need((len(d_1048_unwrappedPdk_)) == (AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)), AwsKmsHierarchicalKeyring.default__.E(_dafny.Seq("Invalid Key Length")))
        if (d_1051_valueOrError4_).IsFailure():
            res = (d_1051_valueOrError4_).PropagateFailure()
            return res
        d_1052_output_: MaterialWrapping.UnwrapOutput
        d_1052_output_ = MaterialWrapping.UnwrapOutput_UnwrapOutput(d_1048_unwrappedPdk_, AwsKmsHierarchicalKeyring.HierarchyUnwrapInfo_HierarchyUnwrapInfo())
        res = Wrappers.Result_Success(d_1052_output_)
        return res
        return res

    @property
    def crypto(self):
        return self._crypto
    @property
    def branchKeyIdUtf8(self):
        return self._branchKeyIdUtf8
    @property
    def branchKeyVersionAsBytes(self):
        return self._branchKeyVersionAsBytes
    @property
    def branchKey(self):
        return self._branchKey

class KmsHierarchyGenerateAndWrapKeyMaterial(MaterialWrapping.GenerateAndWrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._branchKey: _dafny.Seq = _dafny.Seq({})
        self._branchKeyIdUtf8: _dafny.Seq = UTF8.ValidUTF8Bytes.default()
        self._branchKeyVersionAsBytes: _dafny.Seq = _dafny.Seq({})
        self._crypto: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsHierarchicalKeyring.KmsHierarchyGenerateAndWrapKeyMaterial"
    def ctor__(self, branchKey, branchKeyIdUtf8, branchKeyVersionAsBytes, crypto):
        (self)._branchKey = branchKey
        (self)._branchKeyIdUtf8 = branchKeyIdUtf8
        (self)._branchKeyVersionAsBytes = branchKeyVersionAsBytes
        (self)._crypto = crypto

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result_Success.default(MaterialWrapping.GenerateAndWrapOutput.default(AwsKmsHierarchicalKeyring.HierarchyWrapInfo.default()))()
        d_1053_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_1053_suite_ = (input).algorithmSuite
        d_1054_pdkResult_: Wrappers.Result
        out226_: Wrappers.Result
        out226_ = ((self).crypto).GenerateRandomBytes(software_amazon_cryptography_primitives_internaldafny_types.GenerateRandomBytesInput_GenerateRandomBytesInput(AlgorithmSuites.default__.GetEncryptKeyLength(d_1053_suite_)))
        d_1054_pdkResult_ = out226_
        d_1055_pdk_: _dafny.Seq
        d_1056_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda75_(d_1057_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1057_e_)

        d_1056_valueOrError0_ = (d_1054_pdkResult_).MapFailure(lambda75_)
        if (d_1056_valueOrError0_).IsFailure():
            res = (d_1056_valueOrError0_).PropagateFailure()
            return res
        d_1055_pdk_ = (d_1056_valueOrError0_).Extract()
        d_1058_wrap_: AwsKmsHierarchicalKeyring.KmsHierarchyWrapKeyMaterial
        nw39_ = AwsKmsHierarchicalKeyring.KmsHierarchyWrapKeyMaterial()
        nw39_.ctor__((self).branchKey, (self).branchKeyIdUtf8, (self).branchKeyVersionAsBytes, (self).crypto)
        d_1058_wrap_ = nw39_
        d_1059_wrapOutput_: MaterialWrapping.WrapOutput
        d_1060_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(MaterialWrapping.WrapOutput.default(AwsKmsHierarchicalKeyring.HierarchyWrapInfo.default()))()
        out227_: Wrappers.Result
        out227_ = (d_1058_wrap_).Invoke(MaterialWrapping.WrapInput_WrapInput(d_1055_pdk_, (input).algorithmSuite, (input).encryptionContext))
        d_1060_valueOrError1_ = out227_
        if (d_1060_valueOrError1_).IsFailure():
            res = (d_1060_valueOrError1_).PropagateFailure()
            return res
        d_1059_wrapOutput_ = (d_1060_valueOrError1_).Extract()
        d_1061_output_: MaterialWrapping.GenerateAndWrapOutput
        d_1061_output_ = MaterialWrapping.GenerateAndWrapOutput_GenerateAndWrapOutput(d_1055_pdk_, (d_1059_wrapOutput_).wrappedMaterial, AwsKmsHierarchicalKeyring.HierarchyWrapInfo_HierarchyWrapInfo())
        res = Wrappers.Result_Success(d_1061_output_)
        return res
        return res

    @property
    def branchKey(self):
        return self._branchKey
    @property
    def branchKeyIdUtf8(self):
        return self._branchKeyIdUtf8
    @property
    def branchKeyVersionAsBytes(self):
        return self._branchKeyVersionAsBytes
    @property
    def crypto(self):
        return self._crypto

class KmsHierarchyWrapKeyMaterial(MaterialWrapping.WrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._branchKey: _dafny.Seq = _dafny.Seq({})
        self._branchKeyIdUtf8: _dafny.Seq = UTF8.ValidUTF8Bytes.default()
        self._branchKeyVersionAsBytes: _dafny.Seq = _dafny.Seq({})
        self._crypto: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsHierarchicalKeyring.KmsHierarchyWrapKeyMaterial"
    def ctor__(self, branchKey, branchKeyIdUtf8, branchKeyVersionAsBytes, crypto):
        (self)._branchKey = branchKey
        (self)._branchKeyIdUtf8 = branchKeyIdUtf8
        (self)._branchKeyVersionAsBytes = branchKeyVersionAsBytes
        (self)._crypto = crypto

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result_Success.default(MaterialWrapping.WrapOutput.default(AwsKmsHierarchicalKeyring.HierarchyWrapInfo.default()))()
        d_1062_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_1062_suite_ = (input).algorithmSuite
        d_1063_maybeNonceSalt_: Wrappers.Result
        out228_: Wrappers.Result
        out228_ = ((self).crypto).GenerateRandomBytes(software_amazon_cryptography_primitives_internaldafny_types.GenerateRandomBytesInput_GenerateRandomBytesInput(((AwsKmsHierarchicalKeyring.default__).H__WRAP__SALT__LEN) + ((AwsKmsHierarchicalKeyring.default__).H__WRAP__NONCE__LEN)))
        d_1063_maybeNonceSalt_ = out228_
        d_1064_saltAndNonce_: _dafny.Seq
        d_1065_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda76_(d_1066_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1066_e_)

        d_1065_valueOrError0_ = (d_1063_maybeNonceSalt_).MapFailure(lambda76_)
        if (d_1065_valueOrError0_).IsFailure():
            res = (d_1065_valueOrError0_).PropagateFailure()
            return res
        d_1064_saltAndNonce_ = (d_1065_valueOrError0_).Extract()
        d_1067_salt_: _dafny.Seq
        d_1067_salt_ = _dafny.Seq((d_1064_saltAndNonce_)[0:(AwsKmsHierarchicalKeyring.default__).H__WRAP__SALT__LEN:])
        d_1068_nonce_: _dafny.Seq
        d_1068_nonce_ = _dafny.Seq((d_1064_saltAndNonce_)[(AwsKmsHierarchicalKeyring.default__).H__WRAP__SALT__LEN::])
        d_1069_serializedEC_: _dafny.Seq
        d_1070_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1070_valueOrError1_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_1070_valueOrError1_).IsFailure():
            res = (d_1070_valueOrError1_).PropagateFailure()
            return res
        d_1069_serializedEC_ = (d_1070_valueOrError1_).Extract()
        d_1071_wrappingAad_: _dafny.Seq
        d_1071_wrappingAad_ = AwsKmsHierarchicalKeyring.default__.WrappingAad((self).branchKeyIdUtf8, (self).branchKeyVersionAsBytes, d_1069_serializedEC_)
        d_1072_derivedBranchKey_: _dafny.Seq
        d_1073_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out229_: Wrappers.Result
        out229_ = AwsKmsHierarchicalKeyring.default__.DeriveEncryptionKeyFromBranchKey((self).branchKey, d_1067_salt_, Wrappers.Option_Some((Constants.default__).PROVIDER__ID__HIERARCHY), (self).crypto)
        d_1073_valueOrError2_ = out229_
        if (d_1073_valueOrError2_).IsFailure():
            res = (d_1073_valueOrError2_).PropagateFailure()
            return res
        d_1072_derivedBranchKey_ = (d_1073_valueOrError2_).Extract()
        d_1074_maybeWrappedPdk_: Wrappers.Result
        out230_: Wrappers.Result
        out230_ = ((self).crypto).AESEncrypt(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptInput_AESEncryptInput((AwsKmsHierarchicalKeyring.default__).AES__256__ENC__ALG, d_1068_nonce_, d_1072_derivedBranchKey_, (input).plaintextMaterial, d_1071_wrappingAad_))
        d_1074_maybeWrappedPdk_ = out230_
        d_1075_wrappedPdk_: software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput
        d_1076_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput.default())()
        def lambda77_(d_1077_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1077_e_)

        d_1076_valueOrError3_ = (d_1074_maybeWrappedPdk_).MapFailure(lambda77_)
        if (d_1076_valueOrError3_).IsFailure():
            res = (d_1076_valueOrError3_).PropagateFailure()
            return res
        d_1075_wrappedPdk_ = (d_1076_valueOrError3_).Extract()
        d_1078_output_: MaterialWrapping.WrapOutput
        d_1078_output_ = MaterialWrapping.WrapOutput_WrapOutput(((((d_1067_salt_) + (d_1068_nonce_)) + ((self).branchKeyVersionAsBytes)) + ((d_1075_wrappedPdk_).cipherText)) + ((d_1075_wrappedPdk_).authTag), AwsKmsHierarchicalKeyring.HierarchyWrapInfo_HierarchyWrapInfo())
        res = Wrappers.Result_Success(d_1078_output_)
        return res
        return res

    @property
    def branchKey(self):
        return self._branchKey
    @property
    def branchKeyIdUtf8(self):
        return self._branchKeyIdUtf8
    @property
    def branchKeyVersionAsBytes(self):
        return self._branchKeyVersionAsBytes
    @property
    def crypto(self):
        return self._crypto
