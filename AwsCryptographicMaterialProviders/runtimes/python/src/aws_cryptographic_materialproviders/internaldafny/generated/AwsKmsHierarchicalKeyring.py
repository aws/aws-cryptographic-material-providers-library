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

# Module: AwsKmsHierarchicalKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def getEntry(cmc, input):
        res: Wrappers.Result = None
        out145_: Wrappers.Result
        out145_ = (cmc).GetCacheEntry(input)
        res = out145_
        return res

    @staticmethod
    def putEntry(cmc, input):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out146_: Wrappers.Result
        out146_ = (cmc).PutCacheEntry(input)
        res = out146_
        return res

    @staticmethod
    def DeriveEncryptionKeyFromBranchKey(branchKey, salt, purpose, cryptoPrimitives):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_790_maybeDerivedBranchKey_: Wrappers.Result
        out147_: Wrappers.Result
        out147_ = (cryptoPrimitives).KdfCounterMode(software_amazon_cryptography_primitives_internaldafny_types.KdfCtrInput_KdfCtrInput(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__256(), branchKey, default__.DERIVED__BRANCH__KEY__EXPECTED__LENGTH, purpose, Wrappers.Option_Some(salt)))
        d_790_maybeDerivedBranchKey_ = out147_
        d_791_derivedBranchKey_: _dafny.Seq
        d_792_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda66_(d_793_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_793_e_)

        d_792_valueOrError0_ = (d_790_maybeDerivedBranchKey_).MapFailure(lambda66_)
        if (d_792_valueOrError0_).IsFailure():
            output = (d_792_valueOrError0_).PropagateFailure()
            return output
        d_791_derivedBranchKey_ = (d_792_valueOrError0_).Extract()
        output = Wrappers.Result_Success(d_791_derivedBranchKey_)
        return output

    @staticmethod
    def WrappingAad(branchKeyId, branchKeyVersion, aad):
        return (((Constants.default__.PROVIDER__ID__HIERARCHY) + (branchKeyId)) + (branchKeyVersion)) + (aad)

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
        return software_amazon_cryptography_primitives_internaldafny_types.AES__GCM_AES__GCM(default__.AES__256__ENC__KEY__LENGTH, default__.AES__256__ENC__TAG__LENGTH, default__.AES__256__ENC__IV__LENGTH)
    @_dafny.classproperty
    def H__WRAP__SALT__LEN(instance):
        return 16
    @_dafny.classproperty
    def H__WRAP__NONCE__LEN(instance):
        return 12
    @_dafny.classproperty
    def EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX(instance):
        return (default__.H__WRAP__SALT__LEN) + (default__.H__WRAP__NONCE__LEN)
    @_dafny.classproperty
    def EDK__CIPHERTEXT__VERSION__LENGTH(instance):
        return 16
    @_dafny.classproperty
    def EDK__CIPHERTEXT__VERSION__INDEX(instance):
        return (default__.EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX) + (default__.EDK__CIPHERTEXT__VERSION__LENGTH)
    @_dafny.classproperty
    def EXPECTED__EDK__CIPHERTEXT__OVERHEAD(instance):
        return (default__.EDK__CIPHERTEXT__VERSION__INDEX) + (default__.AES__256__ENC__TAG__LENGTH)
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
        self._cryptoPrimitives: software_amazon_cryptography_primitives_internaldafny_types.IAwsCryptographicPrimitivesClient = None
        self._branchKeyIdSupplier: Wrappers.Option = Wrappers.Option.default()()
        self._branchKeyId: Wrappers.Option = Wrappers.Option.default()()
        self._ttlSeconds: int = None
        self._cache: software_amazon_cryptography_materialproviders_internaldafny_types.ICryptographicMaterialsCache = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsHierarchicalKeyring.AwsKmsHierarchicalKeyring"
    def OnEncrypt(self, input):
        out148_: Wrappers.Result
        out148_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnEncrypt(self, input)
        return out148_

    def OnDecrypt(self, input):
        out149_: Wrappers.Result
        out149_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnDecrypt(self, input)
        return out149_

    def ctor__(self, keyStore, branchKeyId, branchKeyIdSupplier, ttlSeconds, cmc, cryptoPrimitives):
        (self)._keyStore = keyStore
        (self)._branchKeyId = branchKeyId
        (self)._branchKeyIdSupplier = branchKeyIdSupplier
        (self)._ttlSeconds = ttlSeconds
        (self)._cryptoPrimitives = cryptoPrimitives
        (self)._cache = cmc

    def GetBranchKeyId(self, context):
        ret: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        if ((self).branchKeyId).is_Some:
            ret = Wrappers.Result_Success(((self).branchKeyId).value)
            return ret
        elif True:
            d_794_GetBranchKeyIdOut_: software_amazon_cryptography_materialproviders_internaldafny_types.GetBranchKeyIdOutput
            d_795_valueOrError0_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_materialproviders_internaldafny_types.GetBranchKeyIdOutput.default())()
            out150_: Wrappers.Result
            out150_ = (((self).branchKeyIdSupplier).value).GetBranchKeyId(software_amazon_cryptography_materialproviders_internaldafny_types.GetBranchKeyIdInput_GetBranchKeyIdInput(context))
            d_795_valueOrError0_ = out150_
            if (d_795_valueOrError0_).IsFailure():
                ret = (d_795_valueOrError0_).PropagateFailure()
                return ret
            d_794_GetBranchKeyIdOut_ = (d_795_valueOrError0_).Extract()
            ret = Wrappers.Result_Success((d_794_GetBranchKeyIdOut_).branchKeyId)
            return ret
        return ret

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        d_796_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_796_materials_ = (input).materials
        d_797_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_797_suite_ = (d_796_materials_).algorithmSuite
        d_798_branchKeyIdForEncrypt_: _dafny.Seq
        d_799_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out151_: Wrappers.Result
        out151_ = (self).GetBranchKeyId((d_796_materials_).encryptionContext)
        d_799_valueOrError0_ = out151_
        if (d_799_valueOrError0_).IsFailure():
            res = (d_799_valueOrError0_).PropagateFailure()
            return res
        d_798_branchKeyIdForEncrypt_ = (d_799_valueOrError0_).Extract()
        d_800_branchKeyIdUtf8_: _dafny.Seq
        d_801_valueOrError1_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_801_valueOrError1_ = (UTF8.default__.Encode(d_798_branchKeyIdForEncrypt_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_801_valueOrError1_).IsFailure():
            res = (d_801_valueOrError1_).PropagateFailure()
            return res
        d_800_branchKeyIdUtf8_ = (d_801_valueOrError1_).Extract()
        d_802_cacheId_: _dafny.Seq
        d_803_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out152_: Wrappers.Result
        out152_ = (self).GetActiveCacheId(d_798_branchKeyIdForEncrypt_, d_800_branchKeyIdUtf8_, (self).cryptoPrimitives)
        d_803_valueOrError2_ = out152_
        if (d_803_valueOrError2_).IsFailure():
            res = (d_803_valueOrError2_).PropagateFailure()
            return res
        d_802_cacheId_ = (d_803_valueOrError2_).Extract()
        d_804_hierarchicalMaterials_: software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials
        d_805_valueOrError3_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials.default())()
        out153_: Wrappers.Result
        out153_ = (self).GetActiveHierarchicalMaterials(d_798_branchKeyIdForEncrypt_, d_802_cacheId_, (self).keyStore)
        d_805_valueOrError3_ = out153_
        if (d_805_valueOrError3_).IsFailure():
            res = (d_805_valueOrError3_).PropagateFailure()
            return res
        d_804_hierarchicalMaterials_ = (d_805_valueOrError3_).Extract()
        d_806_branchKey_: _dafny.Seq
        d_806_branchKey_ = (d_804_hierarchicalMaterials_).branchKey
        d_807_branchKeyVersion_: _dafny.Seq
        d_807_branchKeyVersion_ = (d_804_hierarchicalMaterials_).branchKeyVersion
        d_808_branchKeyVersionAsString_: _dafny.Seq
        d_809_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_809_valueOrError4_ = (UTF8.default__.Decode(d_807_branchKeyVersion_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_809_valueOrError4_).IsFailure():
            res = (d_809_valueOrError4_).PropagateFailure()
            return res
        d_808_branchKeyVersionAsString_ = (d_809_valueOrError4_).Extract()
        d_810_branchKeyVersionAsBytes_: _dafny.Seq
        d_811_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_811_valueOrError5_ = (UUID.default__.ToByteArray(d_808_branchKeyVersionAsString_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_811_valueOrError5_).IsFailure():
            res = (d_811_valueOrError5_).PropagateFailure()
            return res
        d_810_branchKeyVersionAsBytes_ = (d_811_valueOrError5_).Extract()
        d_812_kmsHierarchyGenerateAndWrap_: KmsHierarchyGenerateAndWrapKeyMaterial
        nw33_ = KmsHierarchyGenerateAndWrapKeyMaterial()
        nw33_.ctor__((d_804_hierarchicalMaterials_).branchKey, d_800_branchKeyIdUtf8_, d_810_branchKeyVersionAsBytes_, (self).cryptoPrimitives)
        d_812_kmsHierarchyGenerateAndWrap_ = nw33_
        d_813_kmsHierarchyWrap_: KmsHierarchyWrapKeyMaterial
        nw34_ = KmsHierarchyWrapKeyMaterial()
        nw34_.ctor__((d_804_hierarchicalMaterials_).branchKey, d_800_branchKeyIdUtf8_, d_810_branchKeyVersionAsBytes_, (self).cryptoPrimitives)
        d_813_kmsHierarchyWrap_ = nw34_
        d_814_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_815_valueOrError6_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.WrapEdkMaterialOutput.default(HierarchyWrapInfo.default()))()
        out154_: Wrappers.Result
        out154_ = EdkWrapping.default__.WrapEdkMaterial(d_796_materials_, d_813_kmsHierarchyWrap_, d_812_kmsHierarchyGenerateAndWrap_)
        d_815_valueOrError6_ = out154_
        if (d_815_valueOrError6_).IsFailure():
            res = (d_815_valueOrError6_).PropagateFailure()
            return res
        d_814_wrapOutput_ = (d_815_valueOrError6_).Extract()
        d_816_symmetricSigningKeyList_: Wrappers.Option
        d_816_symmetricSigningKeyList_ = (Wrappers.Option_Some(_dafny.Seq([((d_814_wrapOutput_).symmetricSigningKey).value])) if ((d_814_wrapOutput_).symmetricSigningKey).is_Some else Wrappers.Option_None())
        d_817_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_817_edk_ = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey(Constants.default__.PROVIDER__ID__HIERARCHY, d_800_branchKeyIdUtf8_, (d_814_wrapOutput_).wrappedMaterial)
        if (d_814_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_818_result_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            d_819_valueOrError7_: Wrappers.Result = None
            d_819_valueOrError7_ = Materials.default__.EncryptionMaterialAddDataKey(d_796_materials_, (d_814_wrapOutput_).plaintextDataKey, _dafny.Seq([d_817_edk_]), d_816_symmetricSigningKeyList_)
            if (d_819_valueOrError7_).IsFailure():
                res = (d_819_valueOrError7_).PropagateFailure()
                return res
            d_818_result_ = (d_819_valueOrError7_).Extract()
            res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_818_result_))
            return res
        elif (d_814_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_820_result_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            d_821_valueOrError8_: Wrappers.Result = None
            d_821_valueOrError8_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys(d_796_materials_, _dafny.Seq([d_817_edk_]), d_816_symmetricSigningKeyList_)
            if (d_821_valueOrError8_).IsFailure():
                res = (d_821_valueOrError8_).PropagateFailure()
                return res
            d_820_result_ = (d_821_valueOrError8_).Extract()
            res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_820_result_))
            return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_822_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_822_materials_ = (input).materials
        d_823_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_823_suite_ = ((input).materials).algorithmSuite
        d_824_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_824_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_822_materials_), default__.E(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_824_valueOrError0_).IsFailure():
            res = (d_824_valueOrError0_).PropagateFailure()
            return res
        d_825_branchKeyIdForDecrypt_: _dafny.Seq
        d_826_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out155_: Wrappers.Result
        out155_ = (self).GetBranchKeyId((d_822_materials_).encryptionContext)
        d_826_valueOrError1_ = out155_
        if (d_826_valueOrError1_).IsFailure():
            res = (d_826_valueOrError1_).PropagateFailure()
            return res
        d_825_branchKeyIdForDecrypt_ = (d_826_valueOrError1_).Extract()
        d_827_filter_: OnDecryptHierarchyEncryptedDataKeyFilter
        nw35_ = OnDecryptHierarchyEncryptedDataKeyFilter()
        nw35_.ctor__(d_825_branchKeyIdForDecrypt_)
        d_827_filter_ = nw35_
        d_828_edksToAttempt_: _dafny.Seq
        d_829_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out156_: Wrappers.Result
        out156_ = Actions.default__.FilterWithResult(d_827_filter_, (input).encryptedDataKeys)
        d_829_valueOrError2_ = out156_
        if (d_829_valueOrError2_).IsFailure():
            res = (d_829_valueOrError2_).PropagateFailure()
            return res
        d_828_edksToAttempt_ = (d_829_valueOrError2_).Extract()
        d_830_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_830_valueOrError3_ = Wrappers.default__.Need((0) < (len(d_828_edksToAttempt_)), default__.E(_dafny.Seq("Unable to decrypt data key: No Encrypted Data Keys found to match.")))
        if (d_830_valueOrError3_).IsFailure():
            res = (d_830_valueOrError3_).PropagateFailure()
            return res
        d_831_decryptClosure_: Actions.ActionWithResult
        nw36_ = DecryptSingleEncryptedDataKey()
        nw36_.ctor__(d_822_materials_, (self).keyStore, (self).cryptoPrimitives, d_825_branchKeyIdForDecrypt_, (self).ttlSeconds, (self).cache)
        d_831_decryptClosure_ = nw36_
        d_832_outcome_: Wrappers.Result
        out157_: Wrappers.Result
        out157_ = Actions.default__.ReduceToSuccess(d_831_decryptClosure_, d_828_edksToAttempt_)
        d_832_outcome_ = out157_
        d_833_SealedDecryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_834_valueOrError4_: Wrappers.Result = None
        def lambda67_(d_835_errors_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_CollectionOfErrors(d_835_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."))

        d_834_valueOrError4_ = (d_832_outcome_).MapFailure(lambda67_)
        if (d_834_valueOrError4_).IsFailure():
            res = (d_834_valueOrError4_).PropagateFailure()
            return res
        d_833_SealedDecryptionMaterials_ = (d_834_valueOrError4_).Extract()
        res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput_OnDecryptOutput(d_833_SealedDecryptionMaterials_))
        return res
        return res

    def GetActiveCacheId(self, branchKeyId, branchKeyIdUtf8, cryptoPrimitives):
        cacheId: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_836_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        def iife24_(_pat_let7_0):
            def iife25_(d_837_branchKeyId_):
                return (True) and (((0) <= (len(d_837_branchKeyId_))) and ((len(d_837_branchKeyId_)) < (StandardLibrary_UInt.default__.UINT32__LIMIT)))
            return iife25_(_pat_let7_0)
        d_836_valueOrError0_ = Wrappers.default__.Need((((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).is_Success) and (iife24_(((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).value)), default__.E(_dafny.Seq("Invalid Branch Key ID Length")))
        if (d_836_valueOrError0_).IsFailure():
            cacheId = (d_836_valueOrError0_).PropagateFailure()
            return cacheId
        d_838_branchKeyId_: _dafny.Seq
        d_838_branchKeyId_ = (UTF8.default__.Decode(branchKeyIdUtf8)).value
        d_839_lenBranchKey_: _dafny.Seq
        d_839_lenBranchKey_ = StandardLibrary_UInt.default__.UInt32ToSeq(len(d_838_branchKeyId_))
        d_840_hashAlgorithm_: software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm
        d_840_hashAlgorithm_ = software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__512()
        d_841_maybeBranchKeyDigest_: Wrappers.Result
        out158_: Wrappers.Result
        out158_ = (cryptoPrimitives).Digest(software_amazon_cryptography_primitives_internaldafny_types.DigestInput_DigestInput(d_840_hashAlgorithm_, branchKeyIdUtf8))
        d_841_maybeBranchKeyDigest_ = out158_
        d_842_branchKeyDigest_: _dafny.Seq
        d_843_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda68_(d_844_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_844_e_)

        d_843_valueOrError1_ = (d_841_maybeBranchKeyDigest_).MapFailure(lambda68_)
        if (d_843_valueOrError1_).IsFailure():
            cacheId = (d_843_valueOrError1_).PropagateFailure()
            return cacheId
        d_842_branchKeyDigest_ = (d_843_valueOrError1_).Extract()
        d_845_activeUtf8_: _dafny.Seq
        d_846_valueOrError2_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_846_valueOrError2_ = (UTF8.default__.Encode(default__.EXPRESSION__ATTRIBUTE__VALUE__STATUS__VALUE)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_846_valueOrError2_).IsFailure():
            cacheId = (d_846_valueOrError2_).PropagateFailure()
            return cacheId
        d_845_activeUtf8_ = (d_846_valueOrError2_).Extract()
        d_847_identifier_: _dafny.Seq
        d_847_identifier_ = (((d_839_lenBranchKey_) + (d_842_branchKeyDigest_)) + (_dafny.Seq([0]))) + (d_845_activeUtf8_)
        d_848_maybeCacheIdDigest_: Wrappers.Result
        out159_: Wrappers.Result
        out159_ = (cryptoPrimitives).Digest(software_amazon_cryptography_primitives_internaldafny_types.DigestInput_DigestInput(d_840_hashAlgorithm_, d_847_identifier_))
        d_848_maybeCacheIdDigest_ = out159_
        d_849_cacheDigest_: _dafny.Seq
        d_850_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda69_(d_851_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_851_e_)

        d_850_valueOrError3_ = (d_848_maybeCacheIdDigest_).MapFailure(lambda69_)
        if (d_850_valueOrError3_).IsFailure():
            cacheId = (d_850_valueOrError3_).PropagateFailure()
            return cacheId
        d_849_cacheDigest_ = (d_850_valueOrError3_).Extract()
        d_852_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_852_valueOrError4_ = Wrappers.default__.Need((len(d_849_cacheDigest_)) == (Digest.default__.Length(d_840_hashAlgorithm_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Digest generated a message not equal to the expected length.")))
        if (d_852_valueOrError4_).IsFailure():
            cacheId = (d_852_valueOrError4_).PropagateFailure()
            return cacheId
        cacheId = Wrappers.Result_Success(_dafny.Seq((d_849_cacheDigest_)[0:32:]))
        return cacheId
        return cacheId

    def GetActiveHierarchicalMaterials(self, branchKeyId, cacheId, keyStore):
        material: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials.default())()
        d_853_getCacheInput_: software_amazon_cryptography_materialproviders_internaldafny_types.GetCacheEntryInput
        d_853_getCacheInput_ = software_amazon_cryptography_materialproviders_internaldafny_types.GetCacheEntryInput_GetCacheEntryInput(cacheId, Wrappers.Option_None())
        d_854_getCacheOutput_: Wrappers.Result
        out160_: Wrappers.Result
        out160_ = default__.getEntry((self).cache, d_853_getCacheInput_)
        d_854_getCacheOutput_ = out160_
        if (d_854_getCacheOutput_).is_Failure:
            d_855_maybeGetActiveBranchKeyOutput_: Wrappers.Result
            out161_: Wrappers.Result
            out161_ = (keyStore).GetActiveBranchKey(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyInput_GetActiveBranchKeyInput(branchKeyId))
            d_855_maybeGetActiveBranchKeyOutput_ = out161_
            d_856_getActiveBranchKeyOutput_: software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput
            d_857_valueOrError0_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput.default())()
            def lambda70_(d_858_e_):
                return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyKeyStore(d_858_e_)

            d_857_valueOrError0_ = (d_855_maybeGetActiveBranchKeyOutput_).MapFailure(lambda70_)
            if (d_857_valueOrError0_).IsFailure():
                material = (d_857_valueOrError0_).PropagateFailure()
                return material
            d_856_getActiveBranchKeyOutput_ = (d_857_valueOrError0_).Extract()
            d_859_branchKeyMaterials_: software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials
            d_859_branchKeyMaterials_ = (d_856_getActiveBranchKeyOutput_).branchKeyMaterials
            d_860_now_: int
            out162_: int
            out162_ = Time.default__.CurrentRelativeTime()
            d_860_now_ = out162_
            d_861_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_861_valueOrError1_ = Wrappers.default__.Need(((d_860_now_) + ((self).ttlSeconds)) < (StandardLibrary_UInt.default__.INT64__MAX__LIMIT), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("INT64 Overflow when putting cache entry.")))
            if (d_861_valueOrError1_).IsFailure():
                material = (d_861_valueOrError1_).PropagateFailure()
                return material
            d_862_putCacheEntryInput_: software_amazon_cryptography_materialproviders_internaldafny_types.PutCacheEntryInput
            d_862_putCacheEntryInput_ = software_amazon_cryptography_materialproviders_internaldafny_types.PutCacheEntryInput_PutCacheEntryInput(cacheId, software_amazon_cryptography_materialproviders_internaldafny_types.Materials_BranchKey(d_859_branchKeyMaterials_), d_860_now_, ((self).ttlSeconds) + (d_860_now_), Wrappers.Option_None(), Wrappers.Option_None())
            d_863___v0_: tuple
            d_864_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            out163_: Wrappers.Result
            out163_ = default__.putEntry((self).cache, d_862_putCacheEntryInput_)
            d_864_valueOrError2_ = out163_
            if (d_864_valueOrError2_).IsFailure():
                material = (d_864_valueOrError2_).PropagateFailure()
                return material
            d_863___v0_ = (d_864_valueOrError2_).Extract()
            material = Wrappers.Result_Success(d_859_branchKeyMaterials_)
            return material
        elif True:
            d_865_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_865_valueOrError3_ = Wrappers.default__.Need(((((d_854_getCacheOutput_).value).materials).is_BranchKey) and ((((d_854_getCacheOutput_).value).materials) == (software_amazon_cryptography_materialproviders_internaldafny_types.Materials_BranchKey((((d_854_getCacheOutput_).value).materials).BranchKey))), default__.E(_dafny.Seq("Invalid Material Type.")))
            if (d_865_valueOrError3_).IsFailure():
                material = (d_865_valueOrError3_).PropagateFailure()
                return material
            material = Wrappers.Result_Success((((d_854_getCacheOutput_).value).materials).BranchKey)
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
        res: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        d_866_providerInfo_: _dafny.Seq
        d_866_providerInfo_ = (edk).keyProviderInfo
        d_867_providerId_: _dafny.Seq
        d_867_providerId_ = (edk).keyProviderId
        if (d_867_providerId_) != (Constants.default__.PROVIDER__ID__HIERARCHY):
            res = Wrappers.Result_Success(False)
            return res
        if not(UTF8.default__.ValidUTF8Seq(d_866_providerInfo_)):
            res = Wrappers.Result_Failure(default__.E(_dafny.Seq("Invalid encoding, provider info is not UTF8.")))
            return res
        d_868_branchKeyId_: _dafny.Seq
        d_869_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_869_valueOrError0_ = (UTF8.default__.Decode(d_866_providerInfo_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_869_valueOrError0_).IsFailure():
            res = (d_869_valueOrError0_).PropagateFailure()
            return res
        d_868_branchKeyId_ = (d_869_valueOrError0_).Extract()
        res = Wrappers.Result_Success(((self).branchKeyId) == (d_868_branchKeyId_))
        return res
        return res

    @property
    def branchKeyId(self):
        return self._branchKeyId

class DecryptSingleEncryptedDataKey(Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._materials: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials = None
        self._keyStore: software_amazon_cryptography_keystore_internaldafny_types.IKeyStoreClient = None
        self._cryptoPrimitives: software_amazon_cryptography_primitives_internaldafny_types.IAwsCryptographicPrimitivesClient = None
        self._branchKeyId: _dafny.Seq = _dafny.Seq({})
        self._ttlSeconds: int = None
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
        d_870_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_870_valueOrError0_ = Wrappers.default__.Need(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received invalid EDK provider info for Hierarchical Keyring")))
        if (d_870_valueOrError0_).IsFailure():
            res = (d_870_valueOrError0_).PropagateFailure()
            return res
        d_871_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_871_suite_ = ((self).materials).algorithmSuite
        d_872_keyProviderId_: _dafny.Seq
        d_872_keyProviderId_ = (edk).keyProviderId
        d_873_branchKeyIdUtf8_: _dafny.Seq
        d_873_branchKeyIdUtf8_ = (edk).keyProviderInfo
        d_874_ciphertext_: _dafny.Seq
        d_874_ciphertext_ = (edk).ciphertext
        d_875_providerWrappedMaterial_: _dafny.Seq
        d_876_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_876_valueOrError1_ = EdkWrapping.default__.GetProviderWrappedMaterial(d_874_ciphertext_, d_871_suite_)
        if (d_876_valueOrError1_).IsFailure():
            res = (d_876_valueOrError1_).PropagateFailure()
            return res
        d_875_providerWrappedMaterial_ = (d_876_valueOrError1_).Extract()
        d_877_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_877_valueOrError2_ = Wrappers.default__.Need((len(d_875_providerWrappedMaterial_)) >= (default__.EDK__CIPHERTEXT__VERSION__INDEX), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received EDK Ciphertext of incorrect length.")))
        if (d_877_valueOrError2_).IsFailure():
            res = (d_877_valueOrError2_).PropagateFailure()
            return res
        d_878_branchKeyVersionUuid_: _dafny.Seq
        d_878_branchKeyVersionUuid_ = _dafny.Seq((d_875_providerWrappedMaterial_)[default__.EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX:default__.EDK__CIPHERTEXT__VERSION__INDEX:])
        d_879_version_: _dafny.Seq
        d_880_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_880_valueOrError3_ = (UUID.default__.FromByteArray(d_878_branchKeyVersionUuid_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_880_valueOrError3_).IsFailure():
            res = (d_880_valueOrError3_).PropagateFailure()
            return res
        d_879_version_ = (d_880_valueOrError3_).Extract()
        d_881_cacheId_: _dafny.Seq
        d_882_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out164_: Wrappers.Result
        out164_ = (self).GetVersionCacheId(d_873_branchKeyIdUtf8_, d_879_version_, (self).cryptoPrimitives)
        d_882_valueOrError4_ = out164_
        if (d_882_valueOrError4_).IsFailure():
            res = (d_882_valueOrError4_).PropagateFailure()
            return res
        d_881_cacheId_ = (d_882_valueOrError4_).Extract()
        d_883_hierarchicalMaterials_: software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials
        d_884_valueOrError5_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials.default())()
        out165_: Wrappers.Result
        out165_ = (self).GetHierarchicalMaterialsVersion((self).branchKeyId, d_873_branchKeyIdUtf8_, d_879_version_, d_881_cacheId_)
        d_884_valueOrError5_ = out165_
        if (d_884_valueOrError5_).IsFailure():
            res = (d_884_valueOrError5_).PropagateFailure()
            return res
        d_883_hierarchicalMaterials_ = (d_884_valueOrError5_).Extract()
        d_885_branchKey_: _dafny.Seq
        d_885_branchKey_ = (d_883_hierarchicalMaterials_).branchKey
        d_886_branchKeyVersion_: _dafny.Seq
        d_886_branchKeyVersion_ = (d_883_hierarchicalMaterials_).branchKeyVersion
        d_887_branchKeyVersionAsString_: _dafny.Seq
        d_888_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_888_valueOrError6_ = (UTF8.default__.Decode(d_886_branchKeyVersion_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_888_valueOrError6_).IsFailure():
            res = (d_888_valueOrError6_).PropagateFailure()
            return res
        d_887_branchKeyVersionAsString_ = (d_888_valueOrError6_).Extract()
        d_889_branchKeyVersionAsBytes_: _dafny.Seq
        d_890_valueOrError7_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_890_valueOrError7_ = (UUID.default__.ToByteArray(d_887_branchKeyVersionAsString_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_890_valueOrError7_).IsFailure():
            res = (d_890_valueOrError7_).PropagateFailure()
            return res
        d_889_branchKeyVersionAsBytes_ = (d_890_valueOrError7_).Extract()
        d_891_maybeCrypto_: Wrappers.Result
        out166_: Wrappers.Result
        out166_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_891_maybeCrypto_ = out166_
        d_892_crypto_: software_amazon_cryptography_primitives_internaldafny_types.IAwsCryptographicPrimitivesClient
        d_893_valueOrError8_: Wrappers.Result = None
        def lambda71_(d_894_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_894_e_)

        d_893_valueOrError8_ = (d_891_maybeCrypto_).MapFailure(lambda71_)
        if (d_893_valueOrError8_).IsFailure():
            res = (d_893_valueOrError8_).PropagateFailure()
            return res
        d_892_crypto_ = (d_893_valueOrError8_).Extract()
        d_895_kmsHierarchyUnwrap_: KmsHierarchyUnwrapKeyMaterial
        nw37_ = KmsHierarchyUnwrapKeyMaterial()
        nw37_.ctor__(d_885_branchKey_, d_873_branchKeyIdUtf8_, d_889_branchKeyVersionAsBytes_, d_892_crypto_)
        d_895_kmsHierarchyUnwrap_ = nw37_
        d_896_unwrapOutputRes_: Wrappers.Result
        out167_: Wrappers.Result
        out167_ = EdkWrapping.default__.UnwrapEdkMaterial((edk).ciphertext, (self).materials, d_895_kmsHierarchyUnwrap_)
        d_896_unwrapOutputRes_ = out167_
        d_897_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_898_valueOrError9_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.UnwrapEdkMaterialOutput.default(HierarchyUnwrapInfo.default()))()
        d_898_valueOrError9_ = d_896_unwrapOutputRes_
        if (d_898_valueOrError9_).IsFailure():
            res = (d_898_valueOrError9_).PropagateFailure()
            return res
        d_897_unwrapOutput_ = (d_898_valueOrError9_).Extract()
        d_899_result_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_900_valueOrError10_: Wrappers.Result = None
        d_900_valueOrError10_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_897_unwrapOutput_).plaintextDataKey, (d_897_unwrapOutput_).symmetricSigningKey)
        if (d_900_valueOrError10_).IsFailure():
            res = (d_900_valueOrError10_).PropagateFailure()
            return res
        d_899_result_ = (d_900_valueOrError10_).Extract()
        res = Wrappers.Result_Success(d_899_result_)
        return res
        return res

    def GetVersionCacheId(self, branchKeyIdUtf8, branchKeyVersion, cryptoPrimitives):
        cacheId: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_901_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        def iife26_(_pat_let8_0):
            def iife27_(d_902_branchKeyId_):
                return (True) and (((0) <= (len(d_902_branchKeyId_))) and ((len(d_902_branchKeyId_)) < (StandardLibrary_UInt.default__.UINT32__LIMIT)))
            return iife27_(_pat_let8_0)
        d_901_valueOrError0_ = Wrappers.default__.Need((((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).is_Success) and (iife26_(((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).value)), default__.E(_dafny.Seq("Invalid Branch Key ID Length")))
        if (d_901_valueOrError0_).IsFailure():
            cacheId = (d_901_valueOrError0_).PropagateFailure()
            return cacheId
        d_903_branchKeyId_: _dafny.Seq
        d_903_branchKeyId_ = (UTF8.default__.Decode(branchKeyIdUtf8)).value
        d_904_lenBranchKey_: _dafny.Seq
        d_904_lenBranchKey_ = StandardLibrary_UInt.default__.UInt32ToSeq(len(d_903_branchKeyId_))
        d_905_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_905_valueOrError1_ = Wrappers.default__.Need(UTF8.default__.IsASCIIString(branchKeyVersion), default__.E(_dafny.Seq("Unable to represent as an ASCII string.")))
        if (d_905_valueOrError1_).IsFailure():
            cacheId = (d_905_valueOrError1_).PropagateFailure()
            return cacheId
        d_906_versionBytes_: _dafny.Seq
        d_906_versionBytes_ = UTF8.default__.EncodeAscii(branchKeyVersion)
        d_907_identifier_: _dafny.Seq
        d_907_identifier_ = (((d_904_lenBranchKey_) + (branchKeyIdUtf8)) + (_dafny.Seq([0]))) + (d_906_versionBytes_)
        d_908_identifierDigestInput_: software_amazon_cryptography_primitives_internaldafny_types.DigestInput
        d_908_identifierDigestInput_ = software_amazon_cryptography_primitives_internaldafny_types.DigestInput_DigestInput(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__512(), d_907_identifier_)
        d_909_maybeCacheDigest_: Wrappers.Result
        out168_: Wrappers.Result
        out168_ = Digest.default__.Digest(d_908_identifierDigestInput_)
        d_909_maybeCacheDigest_ = out168_
        d_910_cacheDigest_: _dafny.Seq
        d_911_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda72_(d_912_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_912_e_)

        d_911_valueOrError2_ = (d_909_maybeCacheDigest_).MapFailure(lambda72_)
        if (d_911_valueOrError2_).IsFailure():
            cacheId = (d_911_valueOrError2_).PropagateFailure()
            return cacheId
        d_910_cacheDigest_ = (d_911_valueOrError2_).Extract()
        cacheId = Wrappers.Result_Success(_dafny.Seq((d_910_cacheDigest_)[0:32:]))
        return cacheId
        return cacheId

    def GetHierarchicalMaterialsVersion(self, branchKeyId, branchKeyIdUtf8, version, cacheId):
        material: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials.default())()
        d_913_getCacheInput_: software_amazon_cryptography_materialproviders_internaldafny_types.GetCacheEntryInput
        d_913_getCacheInput_ = software_amazon_cryptography_materialproviders_internaldafny_types.GetCacheEntryInput_GetCacheEntryInput(cacheId, Wrappers.Option_None())
        d_914_getCacheOutput_: Wrappers.Result
        out169_: Wrappers.Result
        out169_ = default__.getEntry((self).cache, d_913_getCacheInput_)
        d_914_getCacheOutput_ = out169_
        if (d_914_getCacheOutput_).is_Failure:
            d_915_maybeGetBranchKeyVersionOutput_: Wrappers.Result
            out170_: Wrappers.Result
            out170_ = ((self).keyStore).GetBranchKeyVersion(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionInput_GetBranchKeyVersionInput(branchKeyId, version))
            d_915_maybeGetBranchKeyVersionOutput_ = out170_
            d_916_getBranchKeyVersionOutput_: software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput
            d_917_valueOrError0_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput.default())()
            def lambda73_(d_918_e_):
                return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyKeyStore(d_918_e_)

            d_917_valueOrError0_ = (d_915_maybeGetBranchKeyVersionOutput_).MapFailure(lambda73_)
            if (d_917_valueOrError0_).IsFailure():
                material = (d_917_valueOrError0_).PropagateFailure()
                return material
            d_916_getBranchKeyVersionOutput_ = (d_917_valueOrError0_).Extract()
            d_919_branchKeyMaterials_: software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials
            d_919_branchKeyMaterials_ = (d_916_getBranchKeyVersionOutput_).branchKeyMaterials
            d_920_now_: int
            out171_: int
            out171_ = Time.default__.CurrentRelativeTime()
            d_920_now_ = out171_
            d_921_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_921_valueOrError1_ = Wrappers.default__.Need(((d_920_now_) + ((self).ttlSeconds)) < (StandardLibrary_UInt.default__.INT64__MAX__LIMIT), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("INT64 Overflow when putting cache entry.")))
            if (d_921_valueOrError1_).IsFailure():
                material = (d_921_valueOrError1_).PropagateFailure()
                return material
            d_922_putCacheEntryInput_: software_amazon_cryptography_materialproviders_internaldafny_types.PutCacheEntryInput
            d_922_putCacheEntryInput_ = software_amazon_cryptography_materialproviders_internaldafny_types.PutCacheEntryInput_PutCacheEntryInput(cacheId, software_amazon_cryptography_materialproviders_internaldafny_types.Materials_BranchKey(d_919_branchKeyMaterials_), d_920_now_, ((self).ttlSeconds) + (d_920_now_), Wrappers.Option_None(), Wrappers.Option_None())
            d_923___v1_: tuple
            d_924_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            out172_: Wrappers.Result
            out172_ = default__.putEntry((self).cache, d_922_putCacheEntryInput_)
            d_924_valueOrError2_ = out172_
            if (d_924_valueOrError2_).IsFailure():
                material = (d_924_valueOrError2_).PropagateFailure()
                return material
            d_923___v1_ = (d_924_valueOrError2_).Extract()
            material = Wrappers.Result_Success(d_919_branchKeyMaterials_)
            return material
        elif True:
            d_925_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_925_valueOrError3_ = Wrappers.default__.Need(((((d_914_getCacheOutput_).value).materials).is_BranchKey) and ((((d_914_getCacheOutput_).value).materials) == (software_amazon_cryptography_materialproviders_internaldafny_types.Materials_BranchKey((((d_914_getCacheOutput_).value).materials).BranchKey))), default__.E(_dafny.Seq("Invalid Material Type.")))
            if (d_925_valueOrError3_).IsFailure():
                material = (d_925_valueOrError3_).PropagateFailure()
                return material
            material = Wrappers.Result_Success((((d_914_getCacheOutput_).value).materials).BranchKey)
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
        return isinstance(self, HierarchyUnwrapInfo_HierarchyUnwrapInfo)

class HierarchyUnwrapInfo_HierarchyUnwrapInfo(HierarchyUnwrapInfo, NamedTuple('HierarchyUnwrapInfo', [])):
    def __dafnystr__(self) -> str:
        return f'AwsKmsHierarchicalKeyring.HierarchyUnwrapInfo.HierarchyUnwrapInfo'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, HierarchyUnwrapInfo_HierarchyUnwrapInfo)
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
        return isinstance(self, HierarchyWrapInfo_HierarchyWrapInfo)

class HierarchyWrapInfo_HierarchyWrapInfo(HierarchyWrapInfo, NamedTuple('HierarchyWrapInfo', [])):
    def __dafnystr__(self) -> str:
        return f'AwsKmsHierarchicalKeyring.HierarchyWrapInfo.HierarchyWrapInfo'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, HierarchyWrapInfo_HierarchyWrapInfo)
    def __hash__(self) -> int:
        return super().__hash__()


class KmsHierarchyUnwrapKeyMaterial(MaterialWrapping.UnwrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._crypto: software_amazon_cryptography_primitives_internaldafny_types.IAwsCryptographicPrimitivesClient = None
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
        res: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.UnwrapOutput.default(HierarchyUnwrapInfo.default()))()
        d_926_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_926_suite_ = (input).algorithmSuite
        d_927_wrappedMaterial_: _dafny.Seq
        d_927_wrappedMaterial_ = (input).wrappedMaterial
        d_928_aad_: _dafny.Map
        d_928_aad_ = (input).encryptionContext
        d_929_KeyLength_: int
        d_929_KeyLength_ = AlgorithmSuites.default__.GetEncryptKeyLength(d_926_suite_)
        d_930_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_930_valueOrError0_ = Wrappers.default__.Need((len(d_927_wrappedMaterial_)) == ((default__.EXPECTED__EDK__CIPHERTEXT__OVERHEAD) + (d_929_KeyLength_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received EDK Ciphertext of incorrect length2.")))
        if (d_930_valueOrError0_).IsFailure():
            res = (d_930_valueOrError0_).PropagateFailure()
            return res
        d_931_salt_: _dafny.Seq
        d_931_salt_ = _dafny.Seq((d_927_wrappedMaterial_)[0:default__.H__WRAP__SALT__LEN:])
        d_932_iv_: _dafny.Seq
        d_932_iv_ = _dafny.Seq((d_927_wrappedMaterial_)[default__.H__WRAP__SALT__LEN:default__.EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX:])
        d_933_branchKeyVersionUuid_: _dafny.Seq
        d_933_branchKeyVersionUuid_ = _dafny.Seq((d_927_wrappedMaterial_)[default__.EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX:default__.EDK__CIPHERTEXT__VERSION__INDEX:])
        d_934_wrappedKey_: _dafny.Seq
        d_934_wrappedKey_ = _dafny.Seq((d_927_wrappedMaterial_)[default__.EDK__CIPHERTEXT__VERSION__INDEX:(default__.EDK__CIPHERTEXT__VERSION__INDEX) + (d_929_KeyLength_):])
        d_935_authTag_: _dafny.Seq
        d_935_authTag_ = _dafny.Seq((d_927_wrappedMaterial_)[(default__.EDK__CIPHERTEXT__VERSION__INDEX) + (d_929_KeyLength_)::])
        d_936_serializedEC_: _dafny.Seq
        d_937_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_937_valueOrError1_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_937_valueOrError1_).IsFailure():
            res = (d_937_valueOrError1_).PropagateFailure()
            return res
        d_936_serializedEC_ = (d_937_valueOrError1_).Extract()
        d_938_wrappingAad_: _dafny.Seq
        d_938_wrappingAad_ = default__.WrappingAad((self).branchKeyIdUtf8, (self).branchKeyVersionAsBytes, d_936_serializedEC_)
        d_939_derivedBranchKey_: _dafny.Seq
        d_940_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out173_: Wrappers.Result
        out173_ = default__.DeriveEncryptionKeyFromBranchKey((self).branchKey, d_931_salt_, Wrappers.Option_Some(Constants.default__.PROVIDER__ID__HIERARCHY), (self).crypto)
        d_940_valueOrError2_ = out173_
        if (d_940_valueOrError2_).IsFailure():
            res = (d_940_valueOrError2_).PropagateFailure()
            return res
        d_939_derivedBranchKey_ = (d_940_valueOrError2_).Extract()
        d_941_maybeUnwrappedPdk_: Wrappers.Result
        out174_: Wrappers.Result
        out174_ = ((self).crypto).AESDecrypt(software_amazon_cryptography_primitives_internaldafny_types.AESDecryptInput_AESDecryptInput(default__.AES__256__ENC__ALG, d_939_derivedBranchKey_, d_934_wrappedKey_, d_935_authTag_, d_932_iv_, d_938_wrappingAad_))
        d_941_maybeUnwrappedPdk_ = out174_
        d_942_unwrappedPdk_: _dafny.Seq
        d_943_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda74_(d_944_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_944_e_)

        d_943_valueOrError3_ = (d_941_maybeUnwrappedPdk_).MapFailure(lambda74_)
        if (d_943_valueOrError3_).IsFailure():
            res = (d_943_valueOrError3_).PropagateFailure()
            return res
        d_942_unwrappedPdk_ = (d_943_valueOrError3_).Extract()
        d_945_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_945_valueOrError4_ = Wrappers.default__.Need((len(d_942_unwrappedPdk_)) == (AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)), default__.E(_dafny.Seq("Invalid Key Length")))
        if (d_945_valueOrError4_).IsFailure():
            res = (d_945_valueOrError4_).PropagateFailure()
            return res
        d_946_output_: MaterialWrapping.UnwrapOutput
        d_946_output_ = MaterialWrapping.UnwrapOutput_UnwrapOutput(d_942_unwrappedPdk_, HierarchyUnwrapInfo_HierarchyUnwrapInfo())
        res = Wrappers.Result_Success(d_946_output_)
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
        self._crypto: software_amazon_cryptography_primitives_internaldafny_types.IAwsCryptographicPrimitivesClient = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsHierarchicalKeyring.KmsHierarchyGenerateAndWrapKeyMaterial"
    def ctor__(self, branchKey, branchKeyIdUtf8, branchKeyVersionAsBytes, crypto):
        (self)._branchKey = branchKey
        (self)._branchKeyIdUtf8 = branchKeyIdUtf8
        (self)._branchKeyVersionAsBytes = branchKeyVersionAsBytes
        (self)._crypto = crypto

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.GenerateAndWrapOutput.default(HierarchyWrapInfo.default()))()
        d_947_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_947_suite_ = (input).algorithmSuite
        d_948_pdkResult_: Wrappers.Result
        out175_: Wrappers.Result
        out175_ = ((self).crypto).GenerateRandomBytes(software_amazon_cryptography_primitives_internaldafny_types.GenerateRandomBytesInput_GenerateRandomBytesInput(AlgorithmSuites.default__.GetEncryptKeyLength(d_947_suite_)))
        d_948_pdkResult_ = out175_
        d_949_pdk_: _dafny.Seq
        d_950_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda75_(d_951_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_951_e_)

        d_950_valueOrError0_ = (d_948_pdkResult_).MapFailure(lambda75_)
        if (d_950_valueOrError0_).IsFailure():
            res = (d_950_valueOrError0_).PropagateFailure()
            return res
        d_949_pdk_ = (d_950_valueOrError0_).Extract()
        d_952_wrap_: KmsHierarchyWrapKeyMaterial
        nw38_ = KmsHierarchyWrapKeyMaterial()
        nw38_.ctor__((self).branchKey, (self).branchKeyIdUtf8, (self).branchKeyVersionAsBytes, (self).crypto)
        d_952_wrap_ = nw38_
        d_953_wrapOutput_: MaterialWrapping.WrapOutput
        d_954_valueOrError1_: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.WrapOutput.default(HierarchyWrapInfo.default()))()
        out176_: Wrappers.Result
        out176_ = (d_952_wrap_).Invoke(MaterialWrapping.WrapInput_WrapInput(d_949_pdk_, (input).algorithmSuite, (input).encryptionContext))
        d_954_valueOrError1_ = out176_
        if (d_954_valueOrError1_).IsFailure():
            res = (d_954_valueOrError1_).PropagateFailure()
            return res
        d_953_wrapOutput_ = (d_954_valueOrError1_).Extract()
        d_955_output_: MaterialWrapping.GenerateAndWrapOutput
        d_955_output_ = MaterialWrapping.GenerateAndWrapOutput_GenerateAndWrapOutput(d_949_pdk_, (d_953_wrapOutput_).wrappedMaterial, HierarchyWrapInfo_HierarchyWrapInfo())
        res = Wrappers.Result_Success(d_955_output_)
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
        self._crypto: software_amazon_cryptography_primitives_internaldafny_types.IAwsCryptographicPrimitivesClient = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsHierarchicalKeyring.KmsHierarchyWrapKeyMaterial"
    def ctor__(self, branchKey, branchKeyIdUtf8, branchKeyVersionAsBytes, crypto):
        (self)._branchKey = branchKey
        (self)._branchKeyIdUtf8 = branchKeyIdUtf8
        (self)._branchKeyVersionAsBytes = branchKeyVersionAsBytes
        (self)._crypto = crypto

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.WrapOutput.default(HierarchyWrapInfo.default()))()
        d_956_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_956_suite_ = (input).algorithmSuite
        d_957_maybeNonceSalt_: Wrappers.Result
        out177_: Wrappers.Result
        out177_ = ((self).crypto).GenerateRandomBytes(software_amazon_cryptography_primitives_internaldafny_types.GenerateRandomBytesInput_GenerateRandomBytesInput((default__.H__WRAP__SALT__LEN) + (default__.H__WRAP__NONCE__LEN)))
        d_957_maybeNonceSalt_ = out177_
        d_958_saltAndNonce_: _dafny.Seq
        d_959_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda76_(d_960_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_960_e_)

        d_959_valueOrError0_ = (d_957_maybeNonceSalt_).MapFailure(lambda76_)
        if (d_959_valueOrError0_).IsFailure():
            res = (d_959_valueOrError0_).PropagateFailure()
            return res
        d_958_saltAndNonce_ = (d_959_valueOrError0_).Extract()
        d_961_salt_: _dafny.Seq
        d_961_salt_ = _dafny.Seq((d_958_saltAndNonce_)[0:default__.H__WRAP__SALT__LEN:])
        d_962_nonce_: _dafny.Seq
        d_962_nonce_ = _dafny.Seq((d_958_saltAndNonce_)[default__.H__WRAP__SALT__LEN::])
        d_963_serializedEC_: _dafny.Seq
        d_964_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_964_valueOrError1_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_964_valueOrError1_).IsFailure():
            res = (d_964_valueOrError1_).PropagateFailure()
            return res
        d_963_serializedEC_ = (d_964_valueOrError1_).Extract()
        d_965_wrappingAad_: _dafny.Seq
        d_965_wrappingAad_ = default__.WrappingAad((self).branchKeyIdUtf8, (self).branchKeyVersionAsBytes, d_963_serializedEC_)
        d_966_derivedBranchKey_: _dafny.Seq
        d_967_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out178_: Wrappers.Result
        out178_ = default__.DeriveEncryptionKeyFromBranchKey((self).branchKey, d_961_salt_, Wrappers.Option_Some(Constants.default__.PROVIDER__ID__HIERARCHY), (self).crypto)
        d_967_valueOrError2_ = out178_
        if (d_967_valueOrError2_).IsFailure():
            res = (d_967_valueOrError2_).PropagateFailure()
            return res
        d_966_derivedBranchKey_ = (d_967_valueOrError2_).Extract()
        d_968_maybeWrappedPdk_: Wrappers.Result
        out179_: Wrappers.Result
        out179_ = ((self).crypto).AESEncrypt(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptInput_AESEncryptInput(default__.AES__256__ENC__ALG, d_962_nonce_, d_966_derivedBranchKey_, (input).plaintextMaterial, d_965_wrappingAad_))
        d_968_maybeWrappedPdk_ = out179_
        d_969_wrappedPdk_: software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput
        d_970_valueOrError3_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput.default())()
        def lambda77_(d_971_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_971_e_)

        d_970_valueOrError3_ = (d_968_maybeWrappedPdk_).MapFailure(lambda77_)
        if (d_970_valueOrError3_).IsFailure():
            res = (d_970_valueOrError3_).PropagateFailure()
            return res
        d_969_wrappedPdk_ = (d_970_valueOrError3_).Extract()
        d_972_output_: MaterialWrapping.WrapOutput
        d_972_output_ = MaterialWrapping.WrapOutput_WrapOutput(((((d_961_salt_) + (d_962_nonce_)) + ((self).branchKeyVersionAsBytes)) + ((d_969_wrappedPdk_).cipherText)) + ((d_969_wrappedPdk_).authTag), HierarchyWrapInfo_HierarchyWrapInfo())
        res = Wrappers.Result_Success(d_972_output_)
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
