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
        d_792_maybeDerivedBranchKey_: Wrappers.Result
        out147_: Wrappers.Result
        out147_ = (cryptoPrimitives).KdfCounterMode(software_amazon_cryptography_primitives_internaldafny_types.KdfCtrInput_KdfCtrInput(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__256(), branchKey, default__.DERIVED__BRANCH__KEY__EXPECTED__LENGTH, purpose, Wrappers.Option_Some(salt)))
        d_792_maybeDerivedBranchKey_ = out147_
        d_793_derivedBranchKey_: _dafny.Seq
        d_794_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda66_(d_795_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_795_e_)

        d_794_valueOrError0_ = (d_792_maybeDerivedBranchKey_).MapFailure(lambda66_)
        if (d_794_valueOrError0_).IsFailure():
            output = (d_794_valueOrError0_).PropagateFailure()
            return output
        d_793_derivedBranchKey_ = (d_794_valueOrError0_).Extract()
        output = Wrappers.Result_Success(d_793_derivedBranchKey_)
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
            d_796_GetBranchKeyIdOut_: software_amazon_cryptography_materialproviders_internaldafny_types.GetBranchKeyIdOutput
            d_797_valueOrError0_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_materialproviders_internaldafny_types.GetBranchKeyIdOutput.default())()
            out150_: Wrappers.Result
            out150_ = (((self).branchKeyIdSupplier).value).GetBranchKeyId(software_amazon_cryptography_materialproviders_internaldafny_types.GetBranchKeyIdInput_GetBranchKeyIdInput(context))
            d_797_valueOrError0_ = out150_
            if (d_797_valueOrError0_).IsFailure():
                ret = (d_797_valueOrError0_).PropagateFailure()
                return ret
            d_796_GetBranchKeyIdOut_ = (d_797_valueOrError0_).Extract()
            ret = Wrappers.Result_Success((d_796_GetBranchKeyIdOut_).branchKeyId)
            return ret
        return ret

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        d_798_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_798_materials_ = (input).materials
        d_799_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_799_suite_ = (d_798_materials_).algorithmSuite
        d_800_branchKeyIdForEncrypt_: _dafny.Seq
        d_801_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out151_: Wrappers.Result
        out151_ = (self).GetBranchKeyId((d_798_materials_).encryptionContext)
        d_801_valueOrError0_ = out151_
        if (d_801_valueOrError0_).IsFailure():
            res = (d_801_valueOrError0_).PropagateFailure()
            return res
        d_800_branchKeyIdForEncrypt_ = (d_801_valueOrError0_).Extract()
        d_802_branchKeyIdUtf8_: _dafny.Seq
        d_803_valueOrError1_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_803_valueOrError1_ = (UTF8.default__.Encode(d_800_branchKeyIdForEncrypt_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_803_valueOrError1_).IsFailure():
            res = (d_803_valueOrError1_).PropagateFailure()
            return res
        d_802_branchKeyIdUtf8_ = (d_803_valueOrError1_).Extract()
        d_804_cacheId_: _dafny.Seq
        d_805_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out152_: Wrappers.Result
        out152_ = (self).GetActiveCacheId(d_800_branchKeyIdForEncrypt_, d_802_branchKeyIdUtf8_, (self).cryptoPrimitives)
        d_805_valueOrError2_ = out152_
        if (d_805_valueOrError2_).IsFailure():
            res = (d_805_valueOrError2_).PropagateFailure()
            return res
        d_804_cacheId_ = (d_805_valueOrError2_).Extract()
        d_806_hierarchicalMaterials_: software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials
        d_807_valueOrError3_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials.default())()
        out153_: Wrappers.Result
        out153_ = (self).GetActiveHierarchicalMaterials(d_800_branchKeyIdForEncrypt_, d_804_cacheId_, (self).keyStore)
        d_807_valueOrError3_ = out153_
        if (d_807_valueOrError3_).IsFailure():
            res = (d_807_valueOrError3_).PropagateFailure()
            return res
        d_806_hierarchicalMaterials_ = (d_807_valueOrError3_).Extract()
        d_808_branchKey_: _dafny.Seq
        d_808_branchKey_ = (d_806_hierarchicalMaterials_).branchKey
        d_809_branchKeyVersion_: _dafny.Seq
        d_809_branchKeyVersion_ = (d_806_hierarchicalMaterials_).branchKeyVersion
        d_810_branchKeyVersionAsString_: _dafny.Seq
        d_811_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_811_valueOrError4_ = (UTF8.default__.Decode(d_809_branchKeyVersion_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_811_valueOrError4_).IsFailure():
            res = (d_811_valueOrError4_).PropagateFailure()
            return res
        d_810_branchKeyVersionAsString_ = (d_811_valueOrError4_).Extract()
        d_812_branchKeyVersionAsBytes_: _dafny.Seq
        d_813_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_813_valueOrError5_ = (UUID.default__.ToByteArray(d_810_branchKeyVersionAsString_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_813_valueOrError5_).IsFailure():
            res = (d_813_valueOrError5_).PropagateFailure()
            return res
        d_812_branchKeyVersionAsBytes_ = (d_813_valueOrError5_).Extract()
        d_814_kmsHierarchyGenerateAndWrap_: KmsHierarchyGenerateAndWrapKeyMaterial
        nw33_ = KmsHierarchyGenerateAndWrapKeyMaterial()
        nw33_.ctor__((d_806_hierarchicalMaterials_).branchKey, d_802_branchKeyIdUtf8_, d_812_branchKeyVersionAsBytes_, (self).cryptoPrimitives)
        d_814_kmsHierarchyGenerateAndWrap_ = nw33_
        d_815_kmsHierarchyWrap_: KmsHierarchyWrapKeyMaterial
        nw34_ = KmsHierarchyWrapKeyMaterial()
        nw34_.ctor__((d_806_hierarchicalMaterials_).branchKey, d_802_branchKeyIdUtf8_, d_812_branchKeyVersionAsBytes_, (self).cryptoPrimitives)
        d_815_kmsHierarchyWrap_ = nw34_
        d_816_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_817_valueOrError6_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.WrapEdkMaterialOutput.default(HierarchyWrapInfo.default()))()
        out154_: Wrappers.Result
        out154_ = EdkWrapping.default__.WrapEdkMaterial(d_798_materials_, d_815_kmsHierarchyWrap_, d_814_kmsHierarchyGenerateAndWrap_)
        d_817_valueOrError6_ = out154_
        if (d_817_valueOrError6_).IsFailure():
            res = (d_817_valueOrError6_).PropagateFailure()
            return res
        d_816_wrapOutput_ = (d_817_valueOrError6_).Extract()
        d_818_symmetricSigningKeyList_: Wrappers.Option
        d_818_symmetricSigningKeyList_ = (Wrappers.Option_Some(_dafny.Seq([((d_816_wrapOutput_).symmetricSigningKey).value])) if ((d_816_wrapOutput_).symmetricSigningKey).is_Some else Wrappers.Option_None())
        d_819_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_819_edk_ = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey(Constants.default__.PROVIDER__ID__HIERARCHY, d_802_branchKeyIdUtf8_, (d_816_wrapOutput_).wrappedMaterial)
        if (d_816_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_820_result_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            d_821_valueOrError7_: Wrappers.Result = None
            d_821_valueOrError7_ = Materials.default__.EncryptionMaterialAddDataKey(d_798_materials_, (d_816_wrapOutput_).plaintextDataKey, _dafny.Seq([d_819_edk_]), d_818_symmetricSigningKeyList_)
            if (d_821_valueOrError7_).IsFailure():
                res = (d_821_valueOrError7_).PropagateFailure()
                return res
            d_820_result_ = (d_821_valueOrError7_).Extract()
            res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_820_result_))
            return res
        elif (d_816_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_822_result_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            d_823_valueOrError8_: Wrappers.Result = None
            d_823_valueOrError8_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys(d_798_materials_, _dafny.Seq([d_819_edk_]), d_818_symmetricSigningKeyList_)
            if (d_823_valueOrError8_).IsFailure():
                res = (d_823_valueOrError8_).PropagateFailure()
                return res
            d_822_result_ = (d_823_valueOrError8_).Extract()
            res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_822_result_))
            return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_824_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_824_materials_ = (input).materials
        d_825_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_825_suite_ = ((input).materials).algorithmSuite
        d_826_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_826_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_824_materials_), default__.E(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_826_valueOrError0_).IsFailure():
            res = (d_826_valueOrError0_).PropagateFailure()
            return res
        d_827_branchKeyIdForDecrypt_: _dafny.Seq
        d_828_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out155_: Wrappers.Result
        out155_ = (self).GetBranchKeyId((d_824_materials_).encryptionContext)
        d_828_valueOrError1_ = out155_
        if (d_828_valueOrError1_).IsFailure():
            res = (d_828_valueOrError1_).PropagateFailure()
            return res
        d_827_branchKeyIdForDecrypt_ = (d_828_valueOrError1_).Extract()
        d_829_filter_: OnDecryptHierarchyEncryptedDataKeyFilter
        nw35_ = OnDecryptHierarchyEncryptedDataKeyFilter()
        nw35_.ctor__(d_827_branchKeyIdForDecrypt_)
        d_829_filter_ = nw35_
        d_830_edksToAttempt_: _dafny.Seq
        d_831_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out156_: Wrappers.Result
        out156_ = Actions.default__.FilterWithResult(d_829_filter_, (input).encryptedDataKeys)
        d_831_valueOrError2_ = out156_
        if (d_831_valueOrError2_).IsFailure():
            res = (d_831_valueOrError2_).PropagateFailure()
            return res
        d_830_edksToAttempt_ = (d_831_valueOrError2_).Extract()
        d_832_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_832_valueOrError3_ = Wrappers.default__.Need((0) < (len(d_830_edksToAttempt_)), default__.E(_dafny.Seq("Unable to decrypt data key: No Encrypted Data Keys found to match.")))
        if (d_832_valueOrError3_).IsFailure():
            res = (d_832_valueOrError3_).PropagateFailure()
            return res
        d_833_decryptClosure_: Actions.ActionWithResult
        nw36_ = DecryptSingleEncryptedDataKey()
        nw36_.ctor__(d_824_materials_, (self).keyStore, (self).cryptoPrimitives, d_827_branchKeyIdForDecrypt_, (self).ttlSeconds, (self).cache)
        d_833_decryptClosure_ = nw36_
        d_834_outcome_: Wrappers.Result
        out157_: Wrappers.Result
        out157_ = Actions.default__.ReduceToSuccess(d_833_decryptClosure_, d_830_edksToAttempt_)
        d_834_outcome_ = out157_
        d_835_SealedDecryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_836_valueOrError4_: Wrappers.Result = None
        def lambda67_(d_837_errors_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_CollectionOfErrors(d_837_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."))

        d_836_valueOrError4_ = (d_834_outcome_).MapFailure(lambda67_)
        if (d_836_valueOrError4_).IsFailure():
            res = (d_836_valueOrError4_).PropagateFailure()
            return res
        d_835_SealedDecryptionMaterials_ = (d_836_valueOrError4_).Extract()
        res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput_OnDecryptOutput(d_835_SealedDecryptionMaterials_))
        return res
        return res

    def GetActiveCacheId(self, branchKeyId, branchKeyIdUtf8, cryptoPrimitives):
        cacheId: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_838_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        def iife24_(_pat_let7_0):
            def iife25_(d_839_branchKeyId_):
                return (True) and (((0) <= (len(d_839_branchKeyId_))) and ((len(d_839_branchKeyId_)) < (StandardLibrary_UInt.default__.UINT32__LIMIT)))
            return iife25_(_pat_let7_0)
        d_838_valueOrError0_ = Wrappers.default__.Need((((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).is_Success) and (iife24_(((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).value)), default__.E(_dafny.Seq("Invalid Branch Key ID Length")))
        if (d_838_valueOrError0_).IsFailure():
            cacheId = (d_838_valueOrError0_).PropagateFailure()
            return cacheId
        d_840_branchKeyId_: _dafny.Seq
        d_840_branchKeyId_ = (UTF8.default__.Decode(branchKeyIdUtf8)).value
        d_841_lenBranchKey_: _dafny.Seq
        d_841_lenBranchKey_ = StandardLibrary_UInt.default__.UInt32ToSeq(len(d_840_branchKeyId_))
        d_842_hashAlgorithm_: software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm
        d_842_hashAlgorithm_ = software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__512()
        d_843_maybeBranchKeyDigest_: Wrappers.Result
        out158_: Wrappers.Result
        out158_ = (cryptoPrimitives).Digest(software_amazon_cryptography_primitives_internaldafny_types.DigestInput_DigestInput(d_842_hashAlgorithm_, branchKeyIdUtf8))
        d_843_maybeBranchKeyDigest_ = out158_
        d_844_branchKeyDigest_: _dafny.Seq
        d_845_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda68_(d_846_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_846_e_)

        d_845_valueOrError1_ = (d_843_maybeBranchKeyDigest_).MapFailure(lambda68_)
        if (d_845_valueOrError1_).IsFailure():
            cacheId = (d_845_valueOrError1_).PropagateFailure()
            return cacheId
        d_844_branchKeyDigest_ = (d_845_valueOrError1_).Extract()
        d_847_activeUtf8_: _dafny.Seq
        d_848_valueOrError2_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_848_valueOrError2_ = (UTF8.default__.Encode(default__.EXPRESSION__ATTRIBUTE__VALUE__STATUS__VALUE)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_848_valueOrError2_).IsFailure():
            cacheId = (d_848_valueOrError2_).PropagateFailure()
            return cacheId
        d_847_activeUtf8_ = (d_848_valueOrError2_).Extract()
        d_849_identifier_: _dafny.Seq
        d_849_identifier_ = (((d_841_lenBranchKey_) + (d_844_branchKeyDigest_)) + (_dafny.Seq([0]))) + (d_847_activeUtf8_)
        d_850_maybeCacheIdDigest_: Wrappers.Result
        out159_: Wrappers.Result
        out159_ = (cryptoPrimitives).Digest(software_amazon_cryptography_primitives_internaldafny_types.DigestInput_DigestInput(d_842_hashAlgorithm_, d_849_identifier_))
        d_850_maybeCacheIdDigest_ = out159_
        d_851_cacheDigest_: _dafny.Seq
        d_852_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda69_(d_853_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_853_e_)

        d_852_valueOrError3_ = (d_850_maybeCacheIdDigest_).MapFailure(lambda69_)
        if (d_852_valueOrError3_).IsFailure():
            cacheId = (d_852_valueOrError3_).PropagateFailure()
            return cacheId
        d_851_cacheDigest_ = (d_852_valueOrError3_).Extract()
        d_854_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_854_valueOrError4_ = Wrappers.default__.Need((len(d_851_cacheDigest_)) == (Digest.default__.Length(d_842_hashAlgorithm_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Digest generated a message not equal to the expected length.")))
        if (d_854_valueOrError4_).IsFailure():
            cacheId = (d_854_valueOrError4_).PropagateFailure()
            return cacheId
        cacheId = Wrappers.Result_Success(_dafny.Seq((d_851_cacheDigest_)[0:32:]))
        return cacheId
        return cacheId

    def GetActiveHierarchicalMaterials(self, branchKeyId, cacheId, keyStore):
        material: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials.default())()
        d_855_getCacheInput_: software_amazon_cryptography_materialproviders_internaldafny_types.GetCacheEntryInput
        d_855_getCacheInput_ = software_amazon_cryptography_materialproviders_internaldafny_types.GetCacheEntryInput_GetCacheEntryInput(cacheId, Wrappers.Option_None())
        d_856_getCacheOutput_: Wrappers.Result
        out160_: Wrappers.Result
        out160_ = default__.getEntry((self).cache, d_855_getCacheInput_)
        d_856_getCacheOutput_ = out160_
        if (d_856_getCacheOutput_).is_Failure:
            d_857_maybeGetActiveBranchKeyOutput_: Wrappers.Result
            out161_: Wrappers.Result
            out161_ = (keyStore).GetActiveBranchKey(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyInput_GetActiveBranchKeyInput(branchKeyId))
            d_857_maybeGetActiveBranchKeyOutput_ = out161_
            d_858_getActiveBranchKeyOutput_: software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput
            d_859_valueOrError0_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput.default())()
            def lambda70_(d_860_e_):
                return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyKeyStore(d_860_e_)

            d_859_valueOrError0_ = (d_857_maybeGetActiveBranchKeyOutput_).MapFailure(lambda70_)
            if (d_859_valueOrError0_).IsFailure():
                material = (d_859_valueOrError0_).PropagateFailure()
                return material
            d_858_getActiveBranchKeyOutput_ = (d_859_valueOrError0_).Extract()
            d_861_branchKeyMaterials_: software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials
            d_861_branchKeyMaterials_ = (d_858_getActiveBranchKeyOutput_).branchKeyMaterials
            d_862_now_: int
            out162_: int
            out162_ = Time.default__.CurrentRelativeTime()
            d_862_now_ = out162_
            d_863_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_863_valueOrError1_ = Wrappers.default__.Need(((d_862_now_) + ((self).ttlSeconds)) < (StandardLibrary_UInt.default__.INT64__MAX__LIMIT), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("INT64 Overflow when putting cache entry.")))
            if (d_863_valueOrError1_).IsFailure():
                material = (d_863_valueOrError1_).PropagateFailure()
                return material
            d_864_putCacheEntryInput_: software_amazon_cryptography_materialproviders_internaldafny_types.PutCacheEntryInput
            d_864_putCacheEntryInput_ = software_amazon_cryptography_materialproviders_internaldafny_types.PutCacheEntryInput_PutCacheEntryInput(cacheId, software_amazon_cryptography_materialproviders_internaldafny_types.Materials_BranchKey(d_861_branchKeyMaterials_), d_862_now_, ((self).ttlSeconds) + (d_862_now_), Wrappers.Option_None(), Wrappers.Option_None())
            d_865___v0_: tuple
            d_866_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            out163_: Wrappers.Result
            out163_ = default__.putEntry((self).cache, d_864_putCacheEntryInput_)
            d_866_valueOrError2_ = out163_
            if (d_866_valueOrError2_).IsFailure():
                material = (d_866_valueOrError2_).PropagateFailure()
                return material
            d_865___v0_ = (d_866_valueOrError2_).Extract()
            material = Wrappers.Result_Success(d_861_branchKeyMaterials_)
            return material
        elif True:
            d_867_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_867_valueOrError3_ = Wrappers.default__.Need(((((d_856_getCacheOutput_).value).materials).is_BranchKey) and ((((d_856_getCacheOutput_).value).materials) == (software_amazon_cryptography_materialproviders_internaldafny_types.Materials_BranchKey((((d_856_getCacheOutput_).value).materials).BranchKey))), default__.E(_dafny.Seq("Invalid Material Type.")))
            if (d_867_valueOrError3_).IsFailure():
                material = (d_867_valueOrError3_).PropagateFailure()
                return material
            material = Wrappers.Result_Success((((d_856_getCacheOutput_).value).materials).BranchKey)
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
        d_868_providerInfo_: _dafny.Seq
        d_868_providerInfo_ = (edk).keyProviderInfo
        d_869_providerId_: _dafny.Seq
        d_869_providerId_ = (edk).keyProviderId
        if (d_869_providerId_) != (Constants.default__.PROVIDER__ID__HIERARCHY):
            res = Wrappers.Result_Success(False)
            return res
        if not(UTF8.default__.ValidUTF8Seq(d_868_providerInfo_)):
            res = Wrappers.Result_Failure(default__.E(_dafny.Seq("Invalid encoding, provider info is not UTF8.")))
            return res
        d_870_branchKeyId_: _dafny.Seq
        d_871_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_871_valueOrError0_ = (UTF8.default__.Decode(d_868_providerInfo_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_871_valueOrError0_).IsFailure():
            res = (d_871_valueOrError0_).PropagateFailure()
            return res
        d_870_branchKeyId_ = (d_871_valueOrError0_).Extract()
        res = Wrappers.Result_Success(((self).branchKeyId) == (d_870_branchKeyId_))
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
        d_872_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_872_valueOrError0_ = Wrappers.default__.Need(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received invalid EDK provider info for Hierarchical Keyring")))
        if (d_872_valueOrError0_).IsFailure():
            res = (d_872_valueOrError0_).PropagateFailure()
            return res
        d_873_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_873_suite_ = ((self).materials).algorithmSuite
        d_874_keyProviderId_: _dafny.Seq
        d_874_keyProviderId_ = (edk).keyProviderId
        d_875_branchKeyIdUtf8_: _dafny.Seq
        d_875_branchKeyIdUtf8_ = (edk).keyProviderInfo
        d_876_ciphertext_: _dafny.Seq
        d_876_ciphertext_ = (edk).ciphertext
        d_877_providerWrappedMaterial_: _dafny.Seq
        d_878_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_878_valueOrError1_ = EdkWrapping.default__.GetProviderWrappedMaterial(d_876_ciphertext_, d_873_suite_)
        if (d_878_valueOrError1_).IsFailure():
            res = (d_878_valueOrError1_).PropagateFailure()
            return res
        d_877_providerWrappedMaterial_ = (d_878_valueOrError1_).Extract()
        d_879_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_879_valueOrError2_ = Wrappers.default__.Need((len(d_877_providerWrappedMaterial_)) >= (default__.EDK__CIPHERTEXT__VERSION__INDEX), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received EDK Ciphertext of incorrect length.")))
        if (d_879_valueOrError2_).IsFailure():
            res = (d_879_valueOrError2_).PropagateFailure()
            return res
        d_880_branchKeyVersionUuid_: _dafny.Seq
        d_880_branchKeyVersionUuid_ = _dafny.Seq((d_877_providerWrappedMaterial_)[default__.EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX:default__.EDK__CIPHERTEXT__VERSION__INDEX:])
        d_881_version_: _dafny.Seq
        d_882_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_882_valueOrError3_ = (UUID.default__.FromByteArray(d_880_branchKeyVersionUuid_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_882_valueOrError3_).IsFailure():
            res = (d_882_valueOrError3_).PropagateFailure()
            return res
        d_881_version_ = (d_882_valueOrError3_).Extract()
        d_883_cacheId_: _dafny.Seq
        d_884_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out164_: Wrappers.Result
        out164_ = (self).GetVersionCacheId(d_875_branchKeyIdUtf8_, d_881_version_, (self).cryptoPrimitives)
        d_884_valueOrError4_ = out164_
        if (d_884_valueOrError4_).IsFailure():
            res = (d_884_valueOrError4_).PropagateFailure()
            return res
        d_883_cacheId_ = (d_884_valueOrError4_).Extract()
        d_885_hierarchicalMaterials_: software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials
        d_886_valueOrError5_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials.default())()
        out165_: Wrappers.Result
        out165_ = (self).GetHierarchicalMaterialsVersion((self).branchKeyId, d_875_branchKeyIdUtf8_, d_881_version_, d_883_cacheId_)
        d_886_valueOrError5_ = out165_
        if (d_886_valueOrError5_).IsFailure():
            res = (d_886_valueOrError5_).PropagateFailure()
            return res
        d_885_hierarchicalMaterials_ = (d_886_valueOrError5_).Extract()
        d_887_branchKey_: _dafny.Seq
        d_887_branchKey_ = (d_885_hierarchicalMaterials_).branchKey
        d_888_branchKeyVersion_: _dafny.Seq
        d_888_branchKeyVersion_ = (d_885_hierarchicalMaterials_).branchKeyVersion
        d_889_branchKeyVersionAsString_: _dafny.Seq
        d_890_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_890_valueOrError6_ = (UTF8.default__.Decode(d_888_branchKeyVersion_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_890_valueOrError6_).IsFailure():
            res = (d_890_valueOrError6_).PropagateFailure()
            return res
        d_889_branchKeyVersionAsString_ = (d_890_valueOrError6_).Extract()
        d_891_branchKeyVersionAsBytes_: _dafny.Seq
        d_892_valueOrError7_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_892_valueOrError7_ = (UUID.default__.ToByteArray(d_889_branchKeyVersionAsString_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_892_valueOrError7_).IsFailure():
            res = (d_892_valueOrError7_).PropagateFailure()
            return res
        d_891_branchKeyVersionAsBytes_ = (d_892_valueOrError7_).Extract()
        d_893_maybeCrypto_: Wrappers.Result
        out166_: Wrappers.Result
        out166_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_893_maybeCrypto_ = out166_
        d_894_cryptoPrimitivesX_: software_amazon_cryptography_primitives_internaldafny_types.IAwsCryptographicPrimitivesClient
        d_895_valueOrError8_: Wrappers.Result = None
        def lambda71_(d_896_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_896_e_)

        d_895_valueOrError8_ = (d_893_maybeCrypto_).MapFailure(lambda71_)
        if (d_895_valueOrError8_).IsFailure():
            res = (d_895_valueOrError8_).PropagateFailure()
            return res
        d_894_cryptoPrimitivesX_ = (d_895_valueOrError8_).Extract()
        d_897_cryptoPrimitives_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_897_cryptoPrimitives_ = d_894_cryptoPrimitivesX_
        d_898_kmsHierarchyUnwrap_: KmsHierarchyUnwrapKeyMaterial
        nw37_ = KmsHierarchyUnwrapKeyMaterial()
        nw37_.ctor__(d_887_branchKey_, d_875_branchKeyIdUtf8_, d_891_branchKeyVersionAsBytes_, d_897_cryptoPrimitives_)
        d_898_kmsHierarchyUnwrap_ = nw37_
        d_899_unwrapOutputRes_: Wrappers.Result
        out167_: Wrappers.Result
        out167_ = EdkWrapping.default__.UnwrapEdkMaterial((edk).ciphertext, (self).materials, d_898_kmsHierarchyUnwrap_)
        d_899_unwrapOutputRes_ = out167_
        d_900_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_901_valueOrError9_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.UnwrapEdkMaterialOutput.default(HierarchyUnwrapInfo.default()))()
        d_901_valueOrError9_ = d_899_unwrapOutputRes_
        if (d_901_valueOrError9_).IsFailure():
            res = (d_901_valueOrError9_).PropagateFailure()
            return res
        d_900_unwrapOutput_ = (d_901_valueOrError9_).Extract()
        d_902_result_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_903_valueOrError10_: Wrappers.Result = None
        d_903_valueOrError10_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_900_unwrapOutput_).plaintextDataKey, (d_900_unwrapOutput_).symmetricSigningKey)
        if (d_903_valueOrError10_).IsFailure():
            res = (d_903_valueOrError10_).PropagateFailure()
            return res
        d_902_result_ = (d_903_valueOrError10_).Extract()
        res = Wrappers.Result_Success(d_902_result_)
        return res
        return res

    def GetVersionCacheId(self, branchKeyIdUtf8, branchKeyVersion, cryptoPrimitives):
        cacheId: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_904_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        def iife26_(_pat_let8_0):
            def iife27_(d_905_branchKeyId_):
                return (True) and (((0) <= (len(d_905_branchKeyId_))) and ((len(d_905_branchKeyId_)) < (StandardLibrary_UInt.default__.UINT32__LIMIT)))
            return iife27_(_pat_let8_0)
        d_904_valueOrError0_ = Wrappers.default__.Need((((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).is_Success) and (iife26_(((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).value)), default__.E(_dafny.Seq("Invalid Branch Key ID Length")))
        if (d_904_valueOrError0_).IsFailure():
            cacheId = (d_904_valueOrError0_).PropagateFailure()
            return cacheId
        d_906_branchKeyId_: _dafny.Seq
        d_906_branchKeyId_ = (UTF8.default__.Decode(branchKeyIdUtf8)).value
        d_907_lenBranchKey_: _dafny.Seq
        d_907_lenBranchKey_ = StandardLibrary_UInt.default__.UInt32ToSeq(len(d_906_branchKeyId_))
        d_908_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_908_valueOrError1_ = Wrappers.default__.Need(UTF8.default__.IsASCIIString(branchKeyVersion), default__.E(_dafny.Seq("Unable to represent as an ASCII string.")))
        if (d_908_valueOrError1_).IsFailure():
            cacheId = (d_908_valueOrError1_).PropagateFailure()
            return cacheId
        d_909_versionBytes_: _dafny.Seq
        d_909_versionBytes_ = UTF8.default__.EncodeAscii(branchKeyVersion)
        d_910_identifier_: _dafny.Seq
        d_910_identifier_ = (((d_907_lenBranchKey_) + (branchKeyIdUtf8)) + (_dafny.Seq([0]))) + (d_909_versionBytes_)
        d_911_identifierDigestInput_: software_amazon_cryptography_primitives_internaldafny_types.DigestInput
        d_911_identifierDigestInput_ = software_amazon_cryptography_primitives_internaldafny_types.DigestInput_DigestInput(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__512(), d_910_identifier_)
        d_912_maybeCacheDigest_: Wrappers.Result
        out168_: Wrappers.Result
        out168_ = Digest.default__.Digest(d_911_identifierDigestInput_)
        d_912_maybeCacheDigest_ = out168_
        d_913_cacheDigest_: _dafny.Seq
        d_914_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda72_(d_915_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_915_e_)

        d_914_valueOrError2_ = (d_912_maybeCacheDigest_).MapFailure(lambda72_)
        if (d_914_valueOrError2_).IsFailure():
            cacheId = (d_914_valueOrError2_).PropagateFailure()
            return cacheId
        d_913_cacheDigest_ = (d_914_valueOrError2_).Extract()
        cacheId = Wrappers.Result_Success(_dafny.Seq((d_913_cacheDigest_)[0:32:]))
        return cacheId
        return cacheId

    def GetHierarchicalMaterialsVersion(self, branchKeyId, branchKeyIdUtf8, version, cacheId):
        material: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials.default())()
        d_916_getCacheInput_: software_amazon_cryptography_materialproviders_internaldafny_types.GetCacheEntryInput
        d_916_getCacheInput_ = software_amazon_cryptography_materialproviders_internaldafny_types.GetCacheEntryInput_GetCacheEntryInput(cacheId, Wrappers.Option_None())
        d_917_getCacheOutput_: Wrappers.Result
        out169_: Wrappers.Result
        out169_ = default__.getEntry((self).cache, d_916_getCacheInput_)
        d_917_getCacheOutput_ = out169_
        if (d_917_getCacheOutput_).is_Failure:
            d_918_maybeGetBranchKeyVersionOutput_: Wrappers.Result
            out170_: Wrappers.Result
            out170_ = ((self).keyStore).GetBranchKeyVersion(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionInput_GetBranchKeyVersionInput(branchKeyId, version))
            d_918_maybeGetBranchKeyVersionOutput_ = out170_
            d_919_getBranchKeyVersionOutput_: software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput
            d_920_valueOrError0_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput.default())()
            def lambda73_(d_921_e_):
                return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyKeyStore(d_921_e_)

            d_920_valueOrError0_ = (d_918_maybeGetBranchKeyVersionOutput_).MapFailure(lambda73_)
            if (d_920_valueOrError0_).IsFailure():
                material = (d_920_valueOrError0_).PropagateFailure()
                return material
            d_919_getBranchKeyVersionOutput_ = (d_920_valueOrError0_).Extract()
            d_922_branchKeyMaterials_: software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials
            d_922_branchKeyMaterials_ = (d_919_getBranchKeyVersionOutput_).branchKeyMaterials
            d_923_now_: int
            out171_: int
            out171_ = Time.default__.CurrentRelativeTime()
            d_923_now_ = out171_
            d_924_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_924_valueOrError1_ = Wrappers.default__.Need(((d_923_now_) + ((self).ttlSeconds)) < (StandardLibrary_UInt.default__.INT64__MAX__LIMIT), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("INT64 Overflow when putting cache entry.")))
            if (d_924_valueOrError1_).IsFailure():
                material = (d_924_valueOrError1_).PropagateFailure()
                return material
            d_925_putCacheEntryInput_: software_amazon_cryptography_materialproviders_internaldafny_types.PutCacheEntryInput
            d_925_putCacheEntryInput_ = software_amazon_cryptography_materialproviders_internaldafny_types.PutCacheEntryInput_PutCacheEntryInput(cacheId, software_amazon_cryptography_materialproviders_internaldafny_types.Materials_BranchKey(d_922_branchKeyMaterials_), d_923_now_, ((self).ttlSeconds) + (d_923_now_), Wrappers.Option_None(), Wrappers.Option_None())
            d_926___v1_: tuple
            d_927_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            out172_: Wrappers.Result
            out172_ = default__.putEntry((self).cache, d_925_putCacheEntryInput_)
            d_927_valueOrError2_ = out172_
            if (d_927_valueOrError2_).IsFailure():
                material = (d_927_valueOrError2_).PropagateFailure()
                return material
            d_926___v1_ = (d_927_valueOrError2_).Extract()
            material = Wrappers.Result_Success(d_922_branchKeyMaterials_)
            return material
        elif True:
            d_928_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_928_valueOrError3_ = Wrappers.default__.Need(((((d_917_getCacheOutput_).value).materials).is_BranchKey) and ((((d_917_getCacheOutput_).value).materials) == (software_amazon_cryptography_materialproviders_internaldafny_types.Materials_BranchKey((((d_917_getCacheOutput_).value).materials).BranchKey))), default__.E(_dafny.Seq("Invalid Material Type.")))
            if (d_928_valueOrError3_).IsFailure():
                material = (d_928_valueOrError3_).PropagateFailure()
                return material
            material = Wrappers.Result_Success((((d_917_getCacheOutput_).value).materials).BranchKey)
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
        d_929_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_929_suite_ = (input).algorithmSuite
        d_930_wrappedMaterial_: _dafny.Seq
        d_930_wrappedMaterial_ = (input).wrappedMaterial
        d_931_aad_: _dafny.Map
        d_931_aad_ = (input).encryptionContext
        d_932_KeyLength_: int
        d_932_KeyLength_ = AlgorithmSuites.default__.GetEncryptKeyLength(d_929_suite_)
        d_933_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_933_valueOrError0_ = Wrappers.default__.Need((len(d_930_wrappedMaterial_)) == ((default__.EXPECTED__EDK__CIPHERTEXT__OVERHEAD) + (d_932_KeyLength_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received EDK Ciphertext of incorrect length2.")))
        if (d_933_valueOrError0_).IsFailure():
            res = (d_933_valueOrError0_).PropagateFailure()
            return res
        d_934_salt_: _dafny.Seq
        d_934_salt_ = _dafny.Seq((d_930_wrappedMaterial_)[0:default__.H__WRAP__SALT__LEN:])
        d_935_iv_: _dafny.Seq
        d_935_iv_ = _dafny.Seq((d_930_wrappedMaterial_)[default__.H__WRAP__SALT__LEN:default__.EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX:])
        d_936_branchKeyVersionUuid_: _dafny.Seq
        d_936_branchKeyVersionUuid_ = _dafny.Seq((d_930_wrappedMaterial_)[default__.EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX:default__.EDK__CIPHERTEXT__VERSION__INDEX:])
        d_937_wrappedKey_: _dafny.Seq
        d_937_wrappedKey_ = _dafny.Seq((d_930_wrappedMaterial_)[default__.EDK__CIPHERTEXT__VERSION__INDEX:(default__.EDK__CIPHERTEXT__VERSION__INDEX) + (d_932_KeyLength_):])
        d_938_authTag_: _dafny.Seq
        d_938_authTag_ = _dafny.Seq((d_930_wrappedMaterial_)[(default__.EDK__CIPHERTEXT__VERSION__INDEX) + (d_932_KeyLength_)::])
        d_939_serializedEC_: _dafny.Seq
        d_940_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_940_valueOrError1_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_940_valueOrError1_).IsFailure():
            res = (d_940_valueOrError1_).PropagateFailure()
            return res
        d_939_serializedEC_ = (d_940_valueOrError1_).Extract()
        d_941_wrappingAad_: _dafny.Seq
        d_941_wrappingAad_ = default__.WrappingAad((self).branchKeyIdUtf8, (self).branchKeyVersionAsBytes, d_939_serializedEC_)
        d_942_derivedBranchKey_: _dafny.Seq
        d_943_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out173_: Wrappers.Result
        out173_ = default__.DeriveEncryptionKeyFromBranchKey((self).branchKey, d_934_salt_, Wrappers.Option_Some(Constants.default__.PROVIDER__ID__HIERARCHY), (self).crypto)
        d_943_valueOrError2_ = out173_
        if (d_943_valueOrError2_).IsFailure():
            res = (d_943_valueOrError2_).PropagateFailure()
            return res
        d_942_derivedBranchKey_ = (d_943_valueOrError2_).Extract()
        d_944_maybeUnwrappedPdk_: Wrappers.Result
        out174_: Wrappers.Result
        out174_ = ((self).crypto).AESDecrypt(software_amazon_cryptography_primitives_internaldafny_types.AESDecryptInput_AESDecryptInput(default__.AES__256__ENC__ALG, d_942_derivedBranchKey_, d_937_wrappedKey_, d_938_authTag_, d_935_iv_, d_941_wrappingAad_))
        d_944_maybeUnwrappedPdk_ = out174_
        d_945_unwrappedPdk_: _dafny.Seq
        d_946_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda74_(d_947_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_947_e_)

        d_946_valueOrError3_ = (d_944_maybeUnwrappedPdk_).MapFailure(lambda74_)
        if (d_946_valueOrError3_).IsFailure():
            res = (d_946_valueOrError3_).PropagateFailure()
            return res
        d_945_unwrappedPdk_ = (d_946_valueOrError3_).Extract()
        d_948_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_948_valueOrError4_ = Wrappers.default__.Need((len(d_945_unwrappedPdk_)) == (AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)), default__.E(_dafny.Seq("Invalid Key Length")))
        if (d_948_valueOrError4_).IsFailure():
            res = (d_948_valueOrError4_).PropagateFailure()
            return res
        d_949_output_: MaterialWrapping.UnwrapOutput
        d_949_output_ = MaterialWrapping.UnwrapOutput_UnwrapOutput(d_945_unwrappedPdk_, HierarchyUnwrapInfo_HierarchyUnwrapInfo())
        res = Wrappers.Result_Success(d_949_output_)
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
        d_950_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_950_suite_ = (input).algorithmSuite
        d_951_pdkResult_: Wrappers.Result
        out175_: Wrappers.Result
        out175_ = ((self).crypto).GenerateRandomBytes(software_amazon_cryptography_primitives_internaldafny_types.GenerateRandomBytesInput_GenerateRandomBytesInput(AlgorithmSuites.default__.GetEncryptKeyLength(d_950_suite_)))
        d_951_pdkResult_ = out175_
        d_952_pdk_: _dafny.Seq
        d_953_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda75_(d_954_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_954_e_)

        d_953_valueOrError0_ = (d_951_pdkResult_).MapFailure(lambda75_)
        if (d_953_valueOrError0_).IsFailure():
            res = (d_953_valueOrError0_).PropagateFailure()
            return res
        d_952_pdk_ = (d_953_valueOrError0_).Extract()
        d_955_wrap_: KmsHierarchyWrapKeyMaterial
        nw38_ = KmsHierarchyWrapKeyMaterial()
        nw38_.ctor__((self).branchKey, (self).branchKeyIdUtf8, (self).branchKeyVersionAsBytes, (self).crypto)
        d_955_wrap_ = nw38_
        d_956_wrapOutput_: MaterialWrapping.WrapOutput
        d_957_valueOrError1_: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.WrapOutput.default(HierarchyWrapInfo.default()))()
        out176_: Wrappers.Result
        out176_ = (d_955_wrap_).Invoke(MaterialWrapping.WrapInput_WrapInput(d_952_pdk_, (input).algorithmSuite, (input).encryptionContext))
        d_957_valueOrError1_ = out176_
        if (d_957_valueOrError1_).IsFailure():
            res = (d_957_valueOrError1_).PropagateFailure()
            return res
        d_956_wrapOutput_ = (d_957_valueOrError1_).Extract()
        d_958_output_: MaterialWrapping.GenerateAndWrapOutput
        d_958_output_ = MaterialWrapping.GenerateAndWrapOutput_GenerateAndWrapOutput(d_952_pdk_, (d_956_wrapOutput_).wrappedMaterial, HierarchyWrapInfo_HierarchyWrapInfo())
        res = Wrappers.Result_Success(d_958_output_)
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
        d_959_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_959_suite_ = (input).algorithmSuite
        d_960_maybeNonceSalt_: Wrappers.Result
        out177_: Wrappers.Result
        out177_ = ((self).crypto).GenerateRandomBytes(software_amazon_cryptography_primitives_internaldafny_types.GenerateRandomBytesInput_GenerateRandomBytesInput((default__.H__WRAP__SALT__LEN) + (default__.H__WRAP__NONCE__LEN)))
        d_960_maybeNonceSalt_ = out177_
        d_961_saltAndNonce_: _dafny.Seq
        d_962_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda76_(d_963_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_963_e_)

        d_962_valueOrError0_ = (d_960_maybeNonceSalt_).MapFailure(lambda76_)
        if (d_962_valueOrError0_).IsFailure():
            res = (d_962_valueOrError0_).PropagateFailure()
            return res
        d_961_saltAndNonce_ = (d_962_valueOrError0_).Extract()
        d_964_salt_: _dafny.Seq
        d_964_salt_ = _dafny.Seq((d_961_saltAndNonce_)[0:default__.H__WRAP__SALT__LEN:])
        d_965_nonce_: _dafny.Seq
        d_965_nonce_ = _dafny.Seq((d_961_saltAndNonce_)[default__.H__WRAP__SALT__LEN::])
        d_966_serializedEC_: _dafny.Seq
        d_967_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_967_valueOrError1_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_967_valueOrError1_).IsFailure():
            res = (d_967_valueOrError1_).PropagateFailure()
            return res
        d_966_serializedEC_ = (d_967_valueOrError1_).Extract()
        d_968_wrappingAad_: _dafny.Seq
        d_968_wrappingAad_ = default__.WrappingAad((self).branchKeyIdUtf8, (self).branchKeyVersionAsBytes, d_966_serializedEC_)
        d_969_derivedBranchKey_: _dafny.Seq
        d_970_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out178_: Wrappers.Result
        out178_ = default__.DeriveEncryptionKeyFromBranchKey((self).branchKey, d_964_salt_, Wrappers.Option_Some(Constants.default__.PROVIDER__ID__HIERARCHY), (self).crypto)
        d_970_valueOrError2_ = out178_
        if (d_970_valueOrError2_).IsFailure():
            res = (d_970_valueOrError2_).PropagateFailure()
            return res
        d_969_derivedBranchKey_ = (d_970_valueOrError2_).Extract()
        d_971_maybeWrappedPdk_: Wrappers.Result
        out179_: Wrappers.Result
        out179_ = ((self).crypto).AESEncrypt(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptInput_AESEncryptInput(default__.AES__256__ENC__ALG, d_965_nonce_, d_969_derivedBranchKey_, (input).plaintextMaterial, d_968_wrappingAad_))
        d_971_maybeWrappedPdk_ = out179_
        d_972_wrappedPdk_: software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput
        d_973_valueOrError3_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput.default())()
        def lambda77_(d_974_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_974_e_)

        d_973_valueOrError3_ = (d_971_maybeWrappedPdk_).MapFailure(lambda77_)
        if (d_973_valueOrError3_).IsFailure():
            res = (d_973_valueOrError3_).PropagateFailure()
            return res
        d_972_wrappedPdk_ = (d_973_valueOrError3_).Extract()
        d_975_output_: MaterialWrapping.WrapOutput
        d_975_output_ = MaterialWrapping.WrapOutput_WrapOutput(((((d_964_salt_) + (d_965_nonce_)) + ((self).branchKeyVersionAsBytes)) + ((d_972_wrappedPdk_).cipherText)) + ((d_972_wrappedPdk_).authTag), HierarchyWrapInfo_HierarchyWrapInfo())
        res = Wrappers.Result_Success(d_975_output_)
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
