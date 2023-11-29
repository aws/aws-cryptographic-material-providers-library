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
        out152_: Wrappers.Result
        out152_ = (cmc).GetCacheEntry(input)
        res = out152_
        return res

    @staticmethod
    def putEntry(cmc, input):
        res: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        out153_: Wrappers.Result
        out153_ = (cmc).PutCacheEntry(input)
        res = out153_
        return res

    @staticmethod
    def DeriveEncryptionKeyFromBranchKey(branchKey, salt, purpose, cryptoPrimitives):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_709_maybeDerivedBranchKey_: Wrappers.Result
        out154_: Wrappers.Result
        out154_ = (cryptoPrimitives).KdfCounterMode(software_amazon_cryptography_primitives_internaldafny_types.KdfCtrInput_KdfCtrInput(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__256(), branchKey, (AwsKmsHierarchicalKeyring.default__).DERIVED__BRANCH__KEY__EXPECTED__LENGTH, purpose, Wrappers.Option_Some(salt)))
        d_709_maybeDerivedBranchKey_ = out154_
        d_710_derivedBranchKey_: _dafny.Seq
        d_711_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda44_(d_712_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_712_e_)

        d_711_valueOrError0_ = (d_709_maybeDerivedBranchKey_).MapFailure(lambda44_)
        if (d_711_valueOrError0_).IsFailure():
            output = (d_711_valueOrError0_).PropagateFailure()
            return output
        d_710_derivedBranchKey_ = (d_711_valueOrError0_).Extract()
        output = Wrappers.Result_Success(d_710_derivedBranchKey_)
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
        out155_: Wrappers.Result
        out155_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnEncrypt(self, input)
        return out155_

    def OnDecrypt(self, input):
        out156_: Wrappers.Result
        out156_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnDecrypt(self, input)
        return out156_

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
            d_713_GetBranchKeyIdOut_: software_amazon_cryptography_materialproviders_internaldafny_types.GetBranchKeyIdOutput
            d_714_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_materialproviders_internaldafny_types.GetBranchKeyIdOutput.default())()
            out157_: Wrappers.Result
            out157_ = (((self).branchKeyIdSupplier).value).GetBranchKeyId(software_amazon_cryptography_materialproviders_internaldafny_types.GetBranchKeyIdInput_GetBranchKeyIdInput(context))
            d_714_valueOrError0_ = out157_
            if (d_714_valueOrError0_).IsFailure():
                ret = (d_714_valueOrError0_).PropagateFailure()
                return ret
            d_713_GetBranchKeyIdOut_ = (d_714_valueOrError0_).Extract()
            ret = Wrappers.Result_Success((d_713_GetBranchKeyIdOut_).branchKeyId)
            return ret
        return ret

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        d_715_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_715_materials_ = (input).materials
        d_716_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_716_suite_ = (d_715_materials_).algorithmSuite
        d_717_branchKeyIdForEncrypt_: _dafny.Seq
        d_718_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out158_: Wrappers.Result
        out158_ = (self).GetBranchKeyId((d_715_materials_).encryptionContext)
        d_718_valueOrError0_ = out158_
        if (d_718_valueOrError0_).IsFailure():
            res = (d_718_valueOrError0_).PropagateFailure()
            return res
        d_717_branchKeyIdForEncrypt_ = (d_718_valueOrError0_).Extract()
        d_719_branchKeyIdUtf8_: _dafny.Seq
        d_720_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_720_valueOrError1_ = (UTF8.default__.Encode(d_717_branchKeyIdForEncrypt_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_720_valueOrError1_).IsFailure():
            res = (d_720_valueOrError1_).PropagateFailure()
            return res
        d_719_branchKeyIdUtf8_ = (d_720_valueOrError1_).Extract()
        d_721_cacheId_: _dafny.Seq
        d_722_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out159_: Wrappers.Result
        out159_ = (self).GetActiveCacheId(d_717_branchKeyIdForEncrypt_, d_719_branchKeyIdUtf8_, (self).cryptoPrimitives)
        d_722_valueOrError2_ = out159_
        if (d_722_valueOrError2_).IsFailure():
            res = (d_722_valueOrError2_).PropagateFailure()
            return res
        d_721_cacheId_ = (d_722_valueOrError2_).Extract()
        d_723_hierarchicalMaterials_: software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials
        d_724_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials.default())()
        out160_: Wrappers.Result
        out160_ = (self).GetActiveHierarchicalMaterials(d_717_branchKeyIdForEncrypt_, d_721_cacheId_, (self).keyStore)
        d_724_valueOrError3_ = out160_
        if (d_724_valueOrError3_).IsFailure():
            res = (d_724_valueOrError3_).PropagateFailure()
            return res
        d_723_hierarchicalMaterials_ = (d_724_valueOrError3_).Extract()
        d_725_branchKey_: _dafny.Seq
        d_725_branchKey_ = (d_723_hierarchicalMaterials_).branchKey
        d_726_branchKeyVersion_: _dafny.Seq
        d_726_branchKeyVersion_ = (d_723_hierarchicalMaterials_).branchKeyVersion
        d_727_branchKeyVersionAsString_: _dafny.Seq
        d_728_valueOrError4_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_728_valueOrError4_ = (UTF8.default__.Decode(d_726_branchKeyVersion_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_728_valueOrError4_).IsFailure():
            res = (d_728_valueOrError4_).PropagateFailure()
            return res
        d_727_branchKeyVersionAsString_ = (d_728_valueOrError4_).Extract()
        d_729_branchKeyVersionAsBytes_: _dafny.Seq
        d_730_valueOrError5_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_730_valueOrError5_ = (UUID.default__.ToByteArray(d_727_branchKeyVersionAsString_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_730_valueOrError5_).IsFailure():
            res = (d_730_valueOrError5_).PropagateFailure()
            return res
        d_729_branchKeyVersionAsBytes_ = (d_730_valueOrError5_).Extract()
        d_731_kmsHierarchyGenerateAndWrap_: AwsKmsHierarchicalKeyring.KmsHierarchyGenerateAndWrapKeyMaterial
        nw33_ = AwsKmsHierarchicalKeyring.KmsHierarchyGenerateAndWrapKeyMaterial()
        nw33_.ctor__((d_723_hierarchicalMaterials_).branchKey, d_719_branchKeyIdUtf8_, d_729_branchKeyVersionAsBytes_, (self).cryptoPrimitives)
        d_731_kmsHierarchyGenerateAndWrap_ = nw33_
        d_732_kmsHierarchyWrap_: AwsKmsHierarchicalKeyring.KmsHierarchyWrapKeyMaterial
        nw34_ = AwsKmsHierarchicalKeyring.KmsHierarchyWrapKeyMaterial()
        nw34_.ctor__((d_723_hierarchicalMaterials_).branchKey, d_719_branchKeyIdUtf8_, d_729_branchKeyVersionAsBytes_, (self).cryptoPrimitives)
        d_732_kmsHierarchyWrap_ = nw34_
        d_733_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_734_valueOrError6_: Wrappers.Result = Wrappers.Result_Success.default(EdkWrapping.WrapEdkMaterialOutput.default(AwsKmsHierarchicalKeyring.HierarchyWrapInfo.default()))()
        out161_: Wrappers.Result
        out161_ = EdkWrapping.default__.WrapEdkMaterial(d_715_materials_, d_732_kmsHierarchyWrap_, d_731_kmsHierarchyGenerateAndWrap_)
        d_734_valueOrError6_ = out161_
        if (d_734_valueOrError6_).IsFailure():
            res = (d_734_valueOrError6_).PropagateFailure()
            return res
        d_733_wrapOutput_ = (d_734_valueOrError6_).Extract()
        d_735_symmetricSigningKeyList_: Wrappers.Option
        d_735_symmetricSigningKeyList_ = (Wrappers.Option_Some(_dafny.Seq([((d_733_wrapOutput_).symmetricSigningKey).value])) if ((d_733_wrapOutput_).symmetricSigningKey).is_Some else Wrappers.Option_None())
        d_736_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_736_edk_ = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey((Constants.default__).PROVIDER__ID__HIERARCHY, d_719_branchKeyIdUtf8_, (d_733_wrapOutput_).wrappedMaterial)
        if (d_733_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_737_result_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            d_738_valueOrError7_: Wrappers.Result = None
            d_738_valueOrError7_ = Materials.default__.EncryptionMaterialAddDataKey(d_715_materials_, (d_733_wrapOutput_).plaintextDataKey, _dafny.Seq([d_736_edk_]), d_735_symmetricSigningKeyList_)
            if (d_738_valueOrError7_).IsFailure():
                res = (d_738_valueOrError7_).PropagateFailure()
                return res
            d_737_result_ = (d_738_valueOrError7_).Extract()
            res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_737_result_))
            return res
        elif (d_733_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_739_result_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            d_740_valueOrError8_: Wrappers.Result = None
            d_740_valueOrError8_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys(d_715_materials_, _dafny.Seq([d_736_edk_]), d_735_symmetricSigningKeyList_)
            if (d_740_valueOrError8_).IsFailure():
                res = (d_740_valueOrError8_).PropagateFailure()
                return res
            d_739_result_ = (d_740_valueOrError8_).Extract()
            res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_739_result_))
            return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_741_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_741_materials_ = (input).materials
        d_742_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_742_suite_ = ((input).materials).algorithmSuite
        d_743_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_743_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_741_materials_), AwsKmsHierarchicalKeyring.default__.E(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_743_valueOrError0_).IsFailure():
            res = (d_743_valueOrError0_).PropagateFailure()
            return res
        d_744_branchKeyIdForDecrypt_: _dafny.Seq
        d_745_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out162_: Wrappers.Result
        out162_ = (self).GetBranchKeyId((d_741_materials_).encryptionContext)
        d_745_valueOrError1_ = out162_
        if (d_745_valueOrError1_).IsFailure():
            res = (d_745_valueOrError1_).PropagateFailure()
            return res
        d_744_branchKeyIdForDecrypt_ = (d_745_valueOrError1_).Extract()
        d_746_filter_: AwsKmsHierarchicalKeyring.OnDecryptHierarchyEncryptedDataKeyFilter
        nw35_ = AwsKmsHierarchicalKeyring.OnDecryptHierarchyEncryptedDataKeyFilter()
        nw35_.ctor__(d_744_branchKeyIdForDecrypt_)
        d_746_filter_ = nw35_
        d_747_edksToAttempt_: _dafny.Seq
        d_748_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out163_: Wrappers.Result
        out163_ = Actions.default__.FilterWithResult(d_746_filter_, (input).encryptedDataKeys)
        d_748_valueOrError2_ = out163_
        if (d_748_valueOrError2_).IsFailure():
            res = (d_748_valueOrError2_).PropagateFailure()
            return res
        d_747_edksToAttempt_ = (d_748_valueOrError2_).Extract()
        d_749_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_749_valueOrError3_ = Wrappers.default__.Need((0) < (len(d_747_edksToAttempt_)), AwsKmsHierarchicalKeyring.default__.E(_dafny.Seq("Unable to decrypt data key: No Encrypted Data Keys found to match.")))
        if (d_749_valueOrError3_).IsFailure():
            res = (d_749_valueOrError3_).PropagateFailure()
            return res
        d_750_decryptClosure_: Actions.ActionWithResult
        nw36_ = AwsKmsHierarchicalKeyring.DecryptSingleEncryptedDataKey()
        nw36_.ctor__(d_741_materials_, (self).keyStore, (self).cryptoPrimitives, d_744_branchKeyIdForDecrypt_, (self).ttlSeconds, (self).cache)
        d_750_decryptClosure_ = nw36_
        d_751_outcome_: Wrappers.Result
        out164_: Wrappers.Result
        out164_ = Actions.default__.ReduceToSuccess(d_750_decryptClosure_, d_747_edksToAttempt_)
        d_751_outcome_ = out164_
        d_752_SealedDecryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_753_valueOrError4_: Wrappers.Result = None
        def lambda45_(d_754_errors_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_CollectionOfErrors(d_754_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."))

        d_753_valueOrError4_ = (d_751_outcome_).MapFailure(lambda45_)
        if (d_753_valueOrError4_).IsFailure():
            res = (d_753_valueOrError4_).PropagateFailure()
            return res
        d_752_SealedDecryptionMaterials_ = (d_753_valueOrError4_).Extract()
        res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput_OnDecryptOutput(d_752_SealedDecryptionMaterials_))
        return res
        return res

    def GetActiveCacheId(self, branchKeyId, branchKeyIdUtf8, cryptoPrimitives):
        cacheId: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_755_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        def iife39_(_pat_let18_0):
            def iife40_(d_756_branchKeyId_):
                return (True) and (((0) <= (len(d_756_branchKeyId_))) and ((len(d_756_branchKeyId_)) < ((StandardLibrary_mUInt.default__).UINT32__LIMIT)))
            return iife40_(_pat_let18_0)
        d_755_valueOrError0_ = Wrappers.default__.Need((((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).is_Success) and (iife39_(((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).value)), AwsKmsHierarchicalKeyring.default__.E(_dafny.Seq("Invalid Branch Key ID Length")))
        if (d_755_valueOrError0_).IsFailure():
            cacheId = (d_755_valueOrError0_).PropagateFailure()
            return cacheId
        d_757_branchKeyId_: _dafny.Seq
        d_757_branchKeyId_ = (UTF8.default__.Decode(branchKeyIdUtf8)).value
        d_758_lenBranchKey_: _dafny.Seq
        d_758_lenBranchKey_ = StandardLibrary_mUInt.default__.UInt32ToSeq(len(d_757_branchKeyId_))
        d_759_hashAlgorithm_: software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm
        d_759_hashAlgorithm_ = software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__512()
        d_760_maybeBranchKeyDigest_: Wrappers.Result
        out165_: Wrappers.Result
        out165_ = (cryptoPrimitives).Digest(software_amazon_cryptography_primitives_internaldafny_types.DigestInput_DigestInput(d_759_hashAlgorithm_, branchKeyIdUtf8))
        d_760_maybeBranchKeyDigest_ = out165_
        d_761_branchKeyDigest_: _dafny.Seq
        d_762_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda46_(d_763_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_763_e_)

        d_762_valueOrError1_ = (d_760_maybeBranchKeyDigest_).MapFailure(lambda46_)
        if (d_762_valueOrError1_).IsFailure():
            cacheId = (d_762_valueOrError1_).PropagateFailure()
            return cacheId
        d_761_branchKeyDigest_ = (d_762_valueOrError1_).Extract()
        d_764_activeUtf8_: _dafny.Seq
        d_765_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_765_valueOrError2_ = (UTF8.default__.Encode((AwsKmsHierarchicalKeyring.default__).EXPRESSION__ATTRIBUTE__VALUE__STATUS__VALUE)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_765_valueOrError2_).IsFailure():
            cacheId = (d_765_valueOrError2_).PropagateFailure()
            return cacheId
        d_764_activeUtf8_ = (d_765_valueOrError2_).Extract()
        d_766_identifier_: _dafny.Seq
        d_766_identifier_ = (((d_758_lenBranchKey_) + (d_761_branchKeyDigest_)) + (_dafny.Seq([0]))) + (d_764_activeUtf8_)
        d_767_maybeCacheIdDigest_: Wrappers.Result
        out166_: Wrappers.Result
        out166_ = (cryptoPrimitives).Digest(software_amazon_cryptography_primitives_internaldafny_types.DigestInput_DigestInput(d_759_hashAlgorithm_, d_766_identifier_))
        d_767_maybeCacheIdDigest_ = out166_
        d_768_cacheDigest_: _dafny.Seq
        d_769_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda47_(d_770_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_770_e_)

        d_769_valueOrError3_ = (d_767_maybeCacheIdDigest_).MapFailure(lambda47_)
        if (d_769_valueOrError3_).IsFailure():
            cacheId = (d_769_valueOrError3_).PropagateFailure()
            return cacheId
        d_768_cacheDigest_ = (d_769_valueOrError3_).Extract()
        d_771_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_771_valueOrError4_ = Wrappers.default__.Need((len(d_768_cacheDigest_)) == (Digest.default__.Length(d_759_hashAlgorithm_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Digest generated a message not equal to the expected length.")))
        if (d_771_valueOrError4_).IsFailure():
            cacheId = (d_771_valueOrError4_).PropagateFailure()
            return cacheId
        cacheId = Wrappers.Result_Success(_dafny.Seq((d_768_cacheDigest_)[0:32:]))
        return cacheId
        return cacheId

    def GetActiveHierarchicalMaterials(self, branchKeyId, cacheId, keyStore):
        material: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials.default())()
        d_772_getCacheInput_: software_amazon_cryptography_materialproviders_internaldafny_types.GetCacheEntryInput
        d_772_getCacheInput_ = software_amazon_cryptography_materialproviders_internaldafny_types.GetCacheEntryInput_GetCacheEntryInput(cacheId, Wrappers.Option_None())
        d_773_getCacheOutput_: Wrappers.Result
        out167_: Wrappers.Result
        out167_ = AwsKmsHierarchicalKeyring.default__.getEntry((self).cache, d_772_getCacheInput_)
        d_773_getCacheOutput_ = out167_
        if (d_773_getCacheOutput_).is_Failure:
            d_774_maybeGetActiveBranchKeyOutput_: Wrappers.Result
            out168_: Wrappers.Result
            out168_ = (keyStore).GetActiveBranchKey(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyInput_GetActiveBranchKeyInput(branchKeyId))
            d_774_maybeGetActiveBranchKeyOutput_ = out168_
            d_775_getActiveBranchKeyOutput_: software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput
            d_776_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput.default())()
            def lambda48_(d_777_e_):
                return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyKeyStore(d_777_e_)

            d_776_valueOrError0_ = (d_774_maybeGetActiveBranchKeyOutput_).MapFailure(lambda48_)
            if (d_776_valueOrError0_).IsFailure():
                material = (d_776_valueOrError0_).PropagateFailure()
                return material
            d_775_getActiveBranchKeyOutput_ = (d_776_valueOrError0_).Extract()
            d_778_branchKeyMaterials_: software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials
            d_778_branchKeyMaterials_ = (d_775_getActiveBranchKeyOutput_).branchKeyMaterials
            d_779_now_: BoundedInts.int64
            out169_: BoundedInts.int64
            out169_ = Time.default__.CurrentRelativeTime()
            d_779_now_ = out169_
            d_780_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
            d_780_valueOrError1_ = Wrappers.default__.Need(((d_779_now_) + ((self).ttlSeconds)) < ((StandardLibrary_mUInt.default__).INT64__MAX__LIMIT), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("INT64 Overflow when putting cache entry.")))
            if (d_780_valueOrError1_).IsFailure():
                material = (d_780_valueOrError1_).PropagateFailure()
                return material
            d_781_putCacheEntryInput_: software_amazon_cryptography_materialproviders_internaldafny_types.PutCacheEntryInput
            d_781_putCacheEntryInput_ = software_amazon_cryptography_materialproviders_internaldafny_types.PutCacheEntryInput_PutCacheEntryInput(cacheId, software_amazon_cryptography_materialproviders_internaldafny_types.Materials_BranchKey(d_778_branchKeyMaterials_), d_779_now_, ((self).ttlSeconds) + (d_779_now_), Wrappers.Option_None(), Wrappers.Option_None())
            d_782___v0_: tuple
            d_783_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
            out170_: Wrappers.Result
            out170_ = AwsKmsHierarchicalKeyring.default__.putEntry((self).cache, d_781_putCacheEntryInput_)
            d_783_valueOrError2_ = out170_
            if (d_783_valueOrError2_).IsFailure():
                material = (d_783_valueOrError2_).PropagateFailure()
                return material
            d_782___v0_ = (d_783_valueOrError2_).Extract()
            material = Wrappers.Result_Success(d_778_branchKeyMaterials_)
            return material
        elif True:
            d_784_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
            d_784_valueOrError3_ = Wrappers.default__.Need(((((d_773_getCacheOutput_).value).materials).is_BranchKey) and ((((d_773_getCacheOutput_).value).materials) == (software_amazon_cryptography_materialproviders_internaldafny_types.Materials_BranchKey((((d_773_getCacheOutput_).value).materials).BranchKey))), AwsKmsHierarchicalKeyring.default__.E(_dafny.Seq("Invalid Material Type.")))
            if (d_784_valueOrError3_).IsFailure():
                material = (d_784_valueOrError3_).PropagateFailure()
                return material
            material = Wrappers.Result_Success((((d_773_getCacheOutput_).value).materials).BranchKey)
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
        d_785_providerInfo_: _dafny.Seq
        d_785_providerInfo_ = (edk).keyProviderInfo
        d_786_providerId_: _dafny.Seq
        d_786_providerId_ = (edk).keyProviderId
        if (d_786_providerId_) != ((Constants.default__).PROVIDER__ID__HIERARCHY):
            res = Wrappers.Result_Success(False)
            return res
        if not(UTF8.default__.ValidUTF8Seq(d_785_providerInfo_)):
            res = Wrappers.Result_Failure(AwsKmsHierarchicalKeyring.default__.E(_dafny.Seq("Invalid encoding, provider info is not UTF8.")))
            return res
        d_787_branchKeyId_: _dafny.Seq
        d_788_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_788_valueOrError0_ = (UTF8.default__.Decode(d_785_providerInfo_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_788_valueOrError0_).IsFailure():
            res = (d_788_valueOrError0_).PropagateFailure()
            return res
        d_787_branchKeyId_ = (d_788_valueOrError0_).Extract()
        res = Wrappers.Result_Success(((self).branchKeyId) == (d_787_branchKeyId_))
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
        d_789_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_789_valueOrError0_ = Wrappers.default__.Need(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received invalid EDK provider info for Hierarchical Keyring")))
        if (d_789_valueOrError0_).IsFailure():
            res = (d_789_valueOrError0_).PropagateFailure()
            return res
        d_790_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_790_suite_ = ((self).materials).algorithmSuite
        d_791_keyProviderId_: _dafny.Seq
        d_791_keyProviderId_ = (edk).keyProviderId
        d_792_branchKeyIdUtf8_: _dafny.Seq
        d_792_branchKeyIdUtf8_ = (edk).keyProviderInfo
        d_793_ciphertext_: _dafny.Seq
        d_793_ciphertext_ = (edk).ciphertext
        d_794_providerWrappedMaterial_: _dafny.Seq
        d_795_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_795_valueOrError1_ = EdkWrapping.default__.GetProviderWrappedMaterial(d_793_ciphertext_, d_790_suite_)
        if (d_795_valueOrError1_).IsFailure():
            res = (d_795_valueOrError1_).PropagateFailure()
            return res
        d_794_providerWrappedMaterial_ = (d_795_valueOrError1_).Extract()
        d_796_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_796_valueOrError2_ = Wrappers.default__.Need((len(d_794_providerWrappedMaterial_)) >= ((AwsKmsHierarchicalKeyring.default__).EDK__CIPHERTEXT__VERSION__INDEX), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received EDK Ciphertext of incorrect length.")))
        if (d_796_valueOrError2_).IsFailure():
            res = (d_796_valueOrError2_).PropagateFailure()
            return res
        d_797_branchKeyVersionUuid_: _dafny.Seq
        d_797_branchKeyVersionUuid_ = _dafny.Seq((d_794_providerWrappedMaterial_)[(AwsKmsHierarchicalKeyring.default__).EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX:(AwsKmsHierarchicalKeyring.default__).EDK__CIPHERTEXT__VERSION__INDEX:])
        d_798_version_: _dafny.Seq
        d_799_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_799_valueOrError3_ = (UUID.default__.FromByteArray(d_797_branchKeyVersionUuid_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_799_valueOrError3_).IsFailure():
            res = (d_799_valueOrError3_).PropagateFailure()
            return res
        d_798_version_ = (d_799_valueOrError3_).Extract()
        d_800_cacheId_: _dafny.Seq
        d_801_valueOrError4_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out171_: Wrappers.Result
        out171_ = (self).GetVersionCacheId(d_792_branchKeyIdUtf8_, d_798_version_, (self).cryptoPrimitives)
        d_801_valueOrError4_ = out171_
        if (d_801_valueOrError4_).IsFailure():
            res = (d_801_valueOrError4_).PropagateFailure()
            return res
        d_800_cacheId_ = (d_801_valueOrError4_).Extract()
        d_802_hierarchicalMaterials_: software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials
        d_803_valueOrError5_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials.default())()
        out172_: Wrappers.Result
        out172_ = (self).GetHierarchicalMaterialsVersion((self).branchKeyId, d_792_branchKeyIdUtf8_, d_798_version_, d_800_cacheId_)
        d_803_valueOrError5_ = out172_
        if (d_803_valueOrError5_).IsFailure():
            res = (d_803_valueOrError5_).PropagateFailure()
            return res
        d_802_hierarchicalMaterials_ = (d_803_valueOrError5_).Extract()
        d_804_branchKey_: _dafny.Seq
        d_804_branchKey_ = (d_802_hierarchicalMaterials_).branchKey
        d_805_branchKeyVersion_: _dafny.Seq
        d_805_branchKeyVersion_ = (d_802_hierarchicalMaterials_).branchKeyVersion
        d_806_branchKeyVersionAsString_: _dafny.Seq
        d_807_valueOrError6_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_807_valueOrError6_ = (UTF8.default__.Decode(d_805_branchKeyVersion_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_807_valueOrError6_).IsFailure():
            res = (d_807_valueOrError6_).PropagateFailure()
            return res
        d_806_branchKeyVersionAsString_ = (d_807_valueOrError6_).Extract()
        d_808_branchKeyVersionAsBytes_: _dafny.Seq
        d_809_valueOrError7_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_809_valueOrError7_ = (UUID.default__.ToByteArray(d_806_branchKeyVersionAsString_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_809_valueOrError7_).IsFailure():
            res = (d_809_valueOrError7_).PropagateFailure()
            return res
        d_808_branchKeyVersionAsBytes_ = (d_809_valueOrError7_).Extract()
        d_810_maybeCrypto_: Wrappers.Result
        out173_: Wrappers.Result
        out173_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_810_maybeCrypto_ = out173_
        d_811_crypto_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_812_valueOrError8_: Wrappers.Result = None
        def lambda49_(d_813_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_813_e_)

        d_812_valueOrError8_ = (d_810_maybeCrypto_).MapFailure(lambda49_)
        if (d_812_valueOrError8_).IsFailure():
            res = (d_812_valueOrError8_).PropagateFailure()
            return res
        d_811_crypto_ = (d_812_valueOrError8_).Extract()
        d_814_kmsHierarchyUnwrap_: AwsKmsHierarchicalKeyring.KmsHierarchyUnwrapKeyMaterial
        nw37_ = AwsKmsHierarchicalKeyring.KmsHierarchyUnwrapKeyMaterial()
        nw37_.ctor__(d_804_branchKey_, d_792_branchKeyIdUtf8_, d_808_branchKeyVersionAsBytes_, d_811_crypto_)
        d_814_kmsHierarchyUnwrap_ = nw37_
        d_815_unwrapOutputRes_: Wrappers.Result
        out174_: Wrappers.Result
        out174_ = EdkWrapping.default__.UnwrapEdkMaterial((edk).ciphertext, (self).materials, d_814_kmsHierarchyUnwrap_)
        d_815_unwrapOutputRes_ = out174_
        d_816_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_817_valueOrError9_: Wrappers.Result = Wrappers.Result_Success.default(EdkWrapping.UnwrapEdkMaterialOutput.default(AwsKmsHierarchicalKeyring.HierarchyUnwrapInfo.default()))()
        d_817_valueOrError9_ = d_815_unwrapOutputRes_
        if (d_817_valueOrError9_).IsFailure():
            res = (d_817_valueOrError9_).PropagateFailure()
            return res
        d_816_unwrapOutput_ = (d_817_valueOrError9_).Extract()
        d_818_result_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_819_valueOrError10_: Wrappers.Result = None
        d_819_valueOrError10_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_816_unwrapOutput_).plaintextDataKey, (d_816_unwrapOutput_).symmetricSigningKey)
        if (d_819_valueOrError10_).IsFailure():
            res = (d_819_valueOrError10_).PropagateFailure()
            return res
        d_818_result_ = (d_819_valueOrError10_).Extract()
        res = Wrappers.Result_Success(d_818_result_)
        return res
        return res

    def GetVersionCacheId(self, branchKeyIdUtf8, branchKeyVersion, cryptoPrimitives):
        cacheId: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_820_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        def iife41_(_pat_let19_0):
            def iife42_(d_821_branchKeyId_):
                return (True) and (((0) <= (len(d_821_branchKeyId_))) and ((len(d_821_branchKeyId_)) < ((StandardLibrary_mUInt.default__).UINT32__LIMIT)))
            return iife42_(_pat_let19_0)
        d_820_valueOrError0_ = Wrappers.default__.Need((((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).is_Success) and (iife41_(((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).value)), AwsKmsHierarchicalKeyring.default__.E(_dafny.Seq("Invalid Branch Key ID Length")))
        if (d_820_valueOrError0_).IsFailure():
            cacheId = (d_820_valueOrError0_).PropagateFailure()
            return cacheId
        d_822_branchKeyId_: _dafny.Seq
        d_822_branchKeyId_ = (UTF8.default__.Decode(branchKeyIdUtf8)).value
        d_823_lenBranchKey_: _dafny.Seq
        d_823_lenBranchKey_ = StandardLibrary_mUInt.default__.UInt32ToSeq(len(d_822_branchKeyId_))
        d_824_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_824_valueOrError1_ = Wrappers.default__.Need(UTF8.default__.IsASCIIString(branchKeyVersion), AwsKmsHierarchicalKeyring.default__.E(_dafny.Seq("Unable to represent as an ASCII string.")))
        if (d_824_valueOrError1_).IsFailure():
            cacheId = (d_824_valueOrError1_).PropagateFailure()
            return cacheId
        d_825_versionBytes_: _dafny.Seq
        d_825_versionBytes_ = UTF8.default__.EncodeAscii(branchKeyVersion)
        d_826_identifier_: _dafny.Seq
        d_826_identifier_ = (((d_823_lenBranchKey_) + (branchKeyIdUtf8)) + (_dafny.Seq([0]))) + (d_825_versionBytes_)
        d_827_identifierDigestInput_: software_amazon_cryptography_primitives_internaldafny_types.DigestInput
        d_827_identifierDigestInput_ = software_amazon_cryptography_primitives_internaldafny_types.DigestInput_DigestInput(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__512(), d_826_identifier_)
        d_828_maybeCacheDigest_: Wrappers.Result
        out175_: Wrappers.Result
        out175_ = Digest.default__.Digest(d_827_identifierDigestInput_)
        d_828_maybeCacheDigest_ = out175_
        d_829_cacheDigest_: _dafny.Seq
        d_830_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda50_(d_831_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_831_e_)

        d_830_valueOrError2_ = (d_828_maybeCacheDigest_).MapFailure(lambda50_)
        if (d_830_valueOrError2_).IsFailure():
            cacheId = (d_830_valueOrError2_).PropagateFailure()
            return cacheId
        d_829_cacheDigest_ = (d_830_valueOrError2_).Extract()
        cacheId = Wrappers.Result_Success(_dafny.Seq((d_829_cacheDigest_)[0:32:]))
        return cacheId
        return cacheId

    def GetHierarchicalMaterialsVersion(self, branchKeyId, branchKeyIdUtf8, version, cacheId):
        material: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials.default())()
        d_832_getCacheInput_: software_amazon_cryptography_materialproviders_internaldafny_types.GetCacheEntryInput
        d_832_getCacheInput_ = software_amazon_cryptography_materialproviders_internaldafny_types.GetCacheEntryInput_GetCacheEntryInput(cacheId, Wrappers.Option_None())
        d_833_getCacheOutput_: Wrappers.Result
        out176_: Wrappers.Result
        out176_ = AwsKmsHierarchicalKeyring.default__.getEntry((self).cache, d_832_getCacheInput_)
        d_833_getCacheOutput_ = out176_
        if (d_833_getCacheOutput_).is_Failure:
            d_834_maybeGetBranchKeyVersionOutput_: Wrappers.Result
            out177_: Wrappers.Result
            out177_ = ((self).keyStore).GetBranchKeyVersion(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionInput_GetBranchKeyVersionInput(branchKeyId, version))
            d_834_maybeGetBranchKeyVersionOutput_ = out177_
            d_835_getBranchKeyVersionOutput_: software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput
            d_836_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput.default())()
            def lambda51_(d_837_e_):
                return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyKeyStore(d_837_e_)

            d_836_valueOrError0_ = (d_834_maybeGetBranchKeyVersionOutput_).MapFailure(lambda51_)
            if (d_836_valueOrError0_).IsFailure():
                material = (d_836_valueOrError0_).PropagateFailure()
                return material
            d_835_getBranchKeyVersionOutput_ = (d_836_valueOrError0_).Extract()
            d_838_branchKeyMaterials_: software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials
            d_838_branchKeyMaterials_ = (d_835_getBranchKeyVersionOutput_).branchKeyMaterials
            d_839_now_: BoundedInts.int64
            out178_: BoundedInts.int64
            out178_ = Time.default__.CurrentRelativeTime()
            d_839_now_ = out178_
            d_840_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
            d_840_valueOrError1_ = Wrappers.default__.Need(((d_839_now_) + ((self).ttlSeconds)) < ((StandardLibrary_mUInt.default__).INT64__MAX__LIMIT), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("INT64 Overflow when putting cache entry.")))
            if (d_840_valueOrError1_).IsFailure():
                material = (d_840_valueOrError1_).PropagateFailure()
                return material
            d_841_putCacheEntryInput_: software_amazon_cryptography_materialproviders_internaldafny_types.PutCacheEntryInput
            d_841_putCacheEntryInput_ = software_amazon_cryptography_materialproviders_internaldafny_types.PutCacheEntryInput_PutCacheEntryInput(cacheId, software_amazon_cryptography_materialproviders_internaldafny_types.Materials_BranchKey(d_838_branchKeyMaterials_), d_839_now_, ((self).ttlSeconds) + (d_839_now_), Wrappers.Option_None(), Wrappers.Option_None())
            d_842___v1_: tuple
            d_843_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
            out179_: Wrappers.Result
            out179_ = AwsKmsHierarchicalKeyring.default__.putEntry((self).cache, d_841_putCacheEntryInput_)
            d_843_valueOrError2_ = out179_
            if (d_843_valueOrError2_).IsFailure():
                material = (d_843_valueOrError2_).PropagateFailure()
                return material
            d_842___v1_ = (d_843_valueOrError2_).Extract()
            material = Wrappers.Result_Success(d_838_branchKeyMaterials_)
            return material
        elif True:
            d_844_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
            d_844_valueOrError3_ = Wrappers.default__.Need(((((d_833_getCacheOutput_).value).materials).is_BranchKey) and ((((d_833_getCacheOutput_).value).materials) == (software_amazon_cryptography_materialproviders_internaldafny_types.Materials_BranchKey((((d_833_getCacheOutput_).value).materials).BranchKey))), AwsKmsHierarchicalKeyring.default__.E(_dafny.Seq("Invalid Material Type.")))
            if (d_844_valueOrError3_).IsFailure():
                material = (d_844_valueOrError3_).PropagateFailure()
                return material
            material = Wrappers.Result_Success((((d_833_getCacheOutput_).value).materials).BranchKey)
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
        d_845_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_845_suite_ = (input).algorithmSuite
        d_846_wrappedMaterial_: _dafny.Seq
        d_846_wrappedMaterial_ = (input).wrappedMaterial
        d_847_aad_: _dafny.Map
        d_847_aad_ = (input).encryptionContext
        d_848_KeyLength_: BoundedInts.int32
        d_848_KeyLength_ = AlgorithmSuites.default__.GetEncryptKeyLength(d_845_suite_)
        d_849_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_849_valueOrError0_ = Wrappers.default__.Need((len(d_846_wrappedMaterial_)) == (((AwsKmsHierarchicalKeyring.default__).EXPECTED__EDK__CIPHERTEXT__OVERHEAD) + (d_848_KeyLength_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received EDK Ciphertext of incorrect length2.")))
        if (d_849_valueOrError0_).IsFailure():
            res = (d_849_valueOrError0_).PropagateFailure()
            return res
        d_850_salt_: _dafny.Seq
        d_850_salt_ = _dafny.Seq((d_846_wrappedMaterial_)[0:(AwsKmsHierarchicalKeyring.default__).H__WRAP__SALT__LEN:])
        d_851_iv_: _dafny.Seq
        d_851_iv_ = _dafny.Seq((d_846_wrappedMaterial_)[(AwsKmsHierarchicalKeyring.default__).H__WRAP__SALT__LEN:(AwsKmsHierarchicalKeyring.default__).EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX:])
        d_852_branchKeyVersionUuid_: _dafny.Seq
        d_852_branchKeyVersionUuid_ = _dafny.Seq((d_846_wrappedMaterial_)[(AwsKmsHierarchicalKeyring.default__).EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX:(AwsKmsHierarchicalKeyring.default__).EDK__CIPHERTEXT__VERSION__INDEX:])
        d_853_wrappedKey_: _dafny.Seq
        d_853_wrappedKey_ = _dafny.Seq((d_846_wrappedMaterial_)[(AwsKmsHierarchicalKeyring.default__).EDK__CIPHERTEXT__VERSION__INDEX:((AwsKmsHierarchicalKeyring.default__).EDK__CIPHERTEXT__VERSION__INDEX) + (d_848_KeyLength_):])
        d_854_authTag_: _dafny.Seq
        d_854_authTag_ = _dafny.Seq((d_846_wrappedMaterial_)[((AwsKmsHierarchicalKeyring.default__).EDK__CIPHERTEXT__VERSION__INDEX) + (d_848_KeyLength_)::])
        d_855_serializedEC_: _dafny.Seq
        d_856_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_856_valueOrError1_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_856_valueOrError1_).IsFailure():
            res = (d_856_valueOrError1_).PropagateFailure()
            return res
        d_855_serializedEC_ = (d_856_valueOrError1_).Extract()
        d_857_wrappingAad_: _dafny.Seq
        d_857_wrappingAad_ = AwsKmsHierarchicalKeyring.default__.WrappingAad((self).branchKeyIdUtf8, (self).branchKeyVersionAsBytes, d_855_serializedEC_)
        d_858_derivedBranchKey_: _dafny.Seq
        d_859_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out180_: Wrappers.Result
        out180_ = AwsKmsHierarchicalKeyring.default__.DeriveEncryptionKeyFromBranchKey((self).branchKey, d_850_salt_, Wrappers.Option_Some((Constants.default__).PROVIDER__ID__HIERARCHY), (self).crypto)
        d_859_valueOrError2_ = out180_
        if (d_859_valueOrError2_).IsFailure():
            res = (d_859_valueOrError2_).PropagateFailure()
            return res
        d_858_derivedBranchKey_ = (d_859_valueOrError2_).Extract()
        d_860_maybeUnwrappedPdk_: Wrappers.Result
        out181_: Wrappers.Result
        out181_ = ((self).crypto).AESDecrypt(software_amazon_cryptography_primitives_internaldafny_types.AESDecryptInput_AESDecryptInput((AwsKmsHierarchicalKeyring.default__).AES__256__ENC__ALG, d_858_derivedBranchKey_, d_853_wrappedKey_, d_854_authTag_, d_851_iv_, d_857_wrappingAad_))
        d_860_maybeUnwrappedPdk_ = out181_
        d_861_unwrappedPdk_: _dafny.Seq
        d_862_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda52_(d_863_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_863_e_)

        d_862_valueOrError3_ = (d_860_maybeUnwrappedPdk_).MapFailure(lambda52_)
        if (d_862_valueOrError3_).IsFailure():
            res = (d_862_valueOrError3_).PropagateFailure()
            return res
        d_861_unwrappedPdk_ = (d_862_valueOrError3_).Extract()
        d_864_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_864_valueOrError4_ = Wrappers.default__.Need((len(d_861_unwrappedPdk_)) == (AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)), AwsKmsHierarchicalKeyring.default__.E(_dafny.Seq("Invalid Key Length")))
        if (d_864_valueOrError4_).IsFailure():
            res = (d_864_valueOrError4_).PropagateFailure()
            return res
        d_865_output_: MaterialWrapping.UnwrapOutput
        d_865_output_ = MaterialWrapping.UnwrapOutput_UnwrapOutput(d_861_unwrappedPdk_, AwsKmsHierarchicalKeyring.HierarchyUnwrapInfo_HierarchyUnwrapInfo())
        res = Wrappers.Result_Success(d_865_output_)
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
        d_866_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_866_suite_ = (input).algorithmSuite
        d_867_pdkResult_: Wrappers.Result
        out182_: Wrappers.Result
        out182_ = ((self).crypto).GenerateRandomBytes(software_amazon_cryptography_primitives_internaldafny_types.GenerateRandomBytesInput_GenerateRandomBytesInput(AlgorithmSuites.default__.GetEncryptKeyLength(d_866_suite_)))
        d_867_pdkResult_ = out182_
        d_868_pdk_: _dafny.Seq
        d_869_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda53_(d_870_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_870_e_)

        d_869_valueOrError0_ = (d_867_pdkResult_).MapFailure(lambda53_)
        if (d_869_valueOrError0_).IsFailure():
            res = (d_869_valueOrError0_).PropagateFailure()
            return res
        d_868_pdk_ = (d_869_valueOrError0_).Extract()
        d_871_wrap_: AwsKmsHierarchicalKeyring.KmsHierarchyWrapKeyMaterial
        nw38_ = AwsKmsHierarchicalKeyring.KmsHierarchyWrapKeyMaterial()
        nw38_.ctor__((self).branchKey, (self).branchKeyIdUtf8, (self).branchKeyVersionAsBytes, (self).crypto)
        d_871_wrap_ = nw38_
        d_872_wrapOutput_: MaterialWrapping.WrapOutput
        d_873_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(MaterialWrapping.WrapOutput.default(AwsKmsHierarchicalKeyring.HierarchyWrapInfo.default()))()
        out183_: Wrappers.Result
        out183_ = (d_871_wrap_).Invoke(MaterialWrapping.WrapInput_WrapInput(d_868_pdk_, (input).algorithmSuite, (input).encryptionContext))
        d_873_valueOrError1_ = out183_
        if (d_873_valueOrError1_).IsFailure():
            res = (d_873_valueOrError1_).PropagateFailure()
            return res
        d_872_wrapOutput_ = (d_873_valueOrError1_).Extract()
        d_874_output_: MaterialWrapping.GenerateAndWrapOutput
        d_874_output_ = MaterialWrapping.GenerateAndWrapOutput_GenerateAndWrapOutput(d_868_pdk_, (d_872_wrapOutput_).wrappedMaterial, AwsKmsHierarchicalKeyring.HierarchyWrapInfo_HierarchyWrapInfo())
        res = Wrappers.Result_Success(d_874_output_)
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
        d_875_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_875_suite_ = (input).algorithmSuite
        d_876_maybeNonceSalt_: Wrappers.Result
        out184_: Wrappers.Result
        out184_ = ((self).crypto).GenerateRandomBytes(software_amazon_cryptography_primitives_internaldafny_types.GenerateRandomBytesInput_GenerateRandomBytesInput(((AwsKmsHierarchicalKeyring.default__).H__WRAP__SALT__LEN) + ((AwsKmsHierarchicalKeyring.default__).H__WRAP__NONCE__LEN)))
        d_876_maybeNonceSalt_ = out184_
        d_877_saltAndNonce_: _dafny.Seq
        d_878_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda54_(d_879_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_879_e_)

        d_878_valueOrError0_ = (d_876_maybeNonceSalt_).MapFailure(lambda54_)
        if (d_878_valueOrError0_).IsFailure():
            res = (d_878_valueOrError0_).PropagateFailure()
            return res
        d_877_saltAndNonce_ = (d_878_valueOrError0_).Extract()
        d_880_salt_: _dafny.Seq
        d_880_salt_ = _dafny.Seq((d_877_saltAndNonce_)[0:(AwsKmsHierarchicalKeyring.default__).H__WRAP__SALT__LEN:])
        d_881_nonce_: _dafny.Seq
        d_881_nonce_ = _dafny.Seq((d_877_saltAndNonce_)[(AwsKmsHierarchicalKeyring.default__).H__WRAP__SALT__LEN::])
        d_882_serializedEC_: _dafny.Seq
        d_883_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_883_valueOrError1_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_883_valueOrError1_).IsFailure():
            res = (d_883_valueOrError1_).PropagateFailure()
            return res
        d_882_serializedEC_ = (d_883_valueOrError1_).Extract()
        d_884_wrappingAad_: _dafny.Seq
        d_884_wrappingAad_ = AwsKmsHierarchicalKeyring.default__.WrappingAad((self).branchKeyIdUtf8, (self).branchKeyVersionAsBytes, d_882_serializedEC_)
        d_885_derivedBranchKey_: _dafny.Seq
        d_886_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out185_: Wrappers.Result
        out185_ = AwsKmsHierarchicalKeyring.default__.DeriveEncryptionKeyFromBranchKey((self).branchKey, d_880_salt_, Wrappers.Option_Some((Constants.default__).PROVIDER__ID__HIERARCHY), (self).crypto)
        d_886_valueOrError2_ = out185_
        if (d_886_valueOrError2_).IsFailure():
            res = (d_886_valueOrError2_).PropagateFailure()
            return res
        d_885_derivedBranchKey_ = (d_886_valueOrError2_).Extract()
        d_887_maybeWrappedPdk_: Wrappers.Result
        out186_: Wrappers.Result
        out186_ = ((self).crypto).AESEncrypt(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptInput_AESEncryptInput((AwsKmsHierarchicalKeyring.default__).AES__256__ENC__ALG, d_881_nonce_, d_885_derivedBranchKey_, (input).plaintextMaterial, d_884_wrappingAad_))
        d_887_maybeWrappedPdk_ = out186_
        d_888_wrappedPdk_: software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput
        d_889_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput.default())()
        def lambda55_(d_890_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_890_e_)

        d_889_valueOrError3_ = (d_887_maybeWrappedPdk_).MapFailure(lambda55_)
        if (d_889_valueOrError3_).IsFailure():
            res = (d_889_valueOrError3_).PropagateFailure()
            return res
        d_888_wrappedPdk_ = (d_889_valueOrError3_).Extract()
        d_891_output_: MaterialWrapping.WrapOutput
        d_891_output_ = MaterialWrapping.WrapOutput_WrapOutput(((((d_880_salt_) + (d_881_nonce_)) + ((self).branchKeyVersionAsBytes)) + ((d_888_wrappedPdk_).cipherText)) + ((d_888_wrappedPdk_).authTag), AwsKmsHierarchicalKeyring.HierarchyWrapInfo_HierarchyWrapInfo())
        res = Wrappers.Result_Success(d_891_output_)
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
