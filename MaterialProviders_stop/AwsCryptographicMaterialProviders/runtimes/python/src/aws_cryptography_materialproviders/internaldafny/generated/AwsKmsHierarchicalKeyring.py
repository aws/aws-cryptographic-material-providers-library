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
        out273_: Wrappers.Result
        out273_ = (cmc).GetCacheEntry(input)
        res = out273_
        return res

    @staticmethod
    def putEntry(cmc, input):
        res: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        out274_: Wrappers.Result
        out274_ = (cmc).PutCacheEntry(input)
        res = out274_
        return res

    @staticmethod
    def DeriveEncryptionKeyFromBranchKey(branchKey, salt, purpose, cryptoPrimitives):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1095_maybeDerivedBranchKey_: Wrappers.Result
        out275_: Wrappers.Result
        out275_ = (cryptoPrimitives).KdfCounterMode(software_amazon_cryptography_primitives_internaldafny_types.KdfCtrInput_KdfCtrInput(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__256(), branchKey, (AwsKmsHierarchicalKeyring.default__).DERIVED__BRANCH__KEY__EXPECTED__LENGTH, purpose, Wrappers.Option_Some(salt)))
        d_1095_maybeDerivedBranchKey_ = out275_
        d_1096_derivedBranchKey_: _dafny.Seq
        d_1097_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda67_(d_1098_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1098_e_)

        d_1097_valueOrError0_ = (d_1095_maybeDerivedBranchKey_).MapFailure(lambda67_)
        if (d_1097_valueOrError0_).IsFailure():
            output = (d_1097_valueOrError0_).PropagateFailure()
            return output
        d_1096_derivedBranchKey_ = (d_1097_valueOrError0_).Extract()
        output = Wrappers.Result_Success(d_1096_derivedBranchKey_)
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
        out276_: Wrappers.Result
        out276_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnEncrypt(self, input)
        return out276_

    def OnDecrypt(self, input):
        out277_: Wrappers.Result
        out277_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnDecrypt(self, input)
        return out277_

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
            d_1099_GetBranchKeyIdOut_: software_amazon_cryptography_materialproviders_internaldafny_types.GetBranchKeyIdOutput
            d_1100_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_materialproviders_internaldafny_types.GetBranchKeyIdOutput.default())()
            out278_: Wrappers.Result
            out278_ = (((self).branchKeyIdSupplier).value).GetBranchKeyId(software_amazon_cryptography_materialproviders_internaldafny_types.GetBranchKeyIdInput_GetBranchKeyIdInput(context))
            d_1100_valueOrError0_ = out278_
            if (d_1100_valueOrError0_).IsFailure():
                ret = (d_1100_valueOrError0_).PropagateFailure()
                return ret
            d_1099_GetBranchKeyIdOut_ = (d_1100_valueOrError0_).Extract()
            ret = Wrappers.Result_Success((d_1099_GetBranchKeyIdOut_).branchKeyId)
            return ret
        return ret

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        d_1101_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_1101_materials_ = (input).materials
        d_1102_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_1102_suite_ = (d_1101_materials_).algorithmSuite
        d_1103_branchKeyIdForEncrypt_: _dafny.Seq
        d_1104_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out279_: Wrappers.Result
        out279_ = (self).GetBranchKeyId((d_1101_materials_).encryptionContext)
        d_1104_valueOrError0_ = out279_
        if (d_1104_valueOrError0_).IsFailure():
            res = (d_1104_valueOrError0_).PropagateFailure()
            return res
        d_1103_branchKeyIdForEncrypt_ = (d_1104_valueOrError0_).Extract()
        d_1105_branchKeyIdUtf8_: _dafny.Seq
        d_1106_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_1106_valueOrError1_ = (UTF8.default__.Encode(d_1103_branchKeyIdForEncrypt_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_1106_valueOrError1_).IsFailure():
            res = (d_1106_valueOrError1_).PropagateFailure()
            return res
        d_1105_branchKeyIdUtf8_ = (d_1106_valueOrError1_).Extract()
        d_1107_cacheId_: _dafny.Seq
        d_1108_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out280_: Wrappers.Result
        out280_ = (self).GetActiveCacheId(d_1103_branchKeyIdForEncrypt_, d_1105_branchKeyIdUtf8_, (self).cryptoPrimitives)
        d_1108_valueOrError2_ = out280_
        if (d_1108_valueOrError2_).IsFailure():
            res = (d_1108_valueOrError2_).PropagateFailure()
            return res
        d_1107_cacheId_ = (d_1108_valueOrError2_).Extract()
        d_1109_hierarchicalMaterials_: software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials
        d_1110_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials.default())()
        out281_: Wrappers.Result
        out281_ = (self).GetActiveHierarchicalMaterials(d_1103_branchKeyIdForEncrypt_, d_1107_cacheId_, (self).keyStore)
        d_1110_valueOrError3_ = out281_
        if (d_1110_valueOrError3_).IsFailure():
            res = (d_1110_valueOrError3_).PropagateFailure()
            return res
        d_1109_hierarchicalMaterials_ = (d_1110_valueOrError3_).Extract()
        d_1111_branchKey_: _dafny.Seq
        d_1111_branchKey_ = (d_1109_hierarchicalMaterials_).branchKey
        d_1112_branchKeyVersion_: _dafny.Seq
        d_1112_branchKeyVersion_ = (d_1109_hierarchicalMaterials_).branchKeyVersion
        d_1113_branchKeyVersionAsString_: _dafny.Seq
        d_1114_valueOrError4_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1114_valueOrError4_ = (UTF8.default__.Decode(d_1112_branchKeyVersion_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_1114_valueOrError4_).IsFailure():
            res = (d_1114_valueOrError4_).PropagateFailure()
            return res
        d_1113_branchKeyVersionAsString_ = (d_1114_valueOrError4_).Extract()
        d_1115_branchKeyVersionAsBytes_: _dafny.Seq
        d_1116_valueOrError5_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1116_valueOrError5_ = (UUID.default__.ToByteArray(d_1113_branchKeyVersionAsString_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_1116_valueOrError5_).IsFailure():
            res = (d_1116_valueOrError5_).PropagateFailure()
            return res
        d_1115_branchKeyVersionAsBytes_ = (d_1116_valueOrError5_).Extract()
        d_1117_kmsHierarchyGenerateAndWrap_: AwsKmsHierarchicalKeyring.KmsHierarchyGenerateAndWrapKeyMaterial
        nw34_ = AwsKmsHierarchicalKeyring.KmsHierarchyGenerateAndWrapKeyMaterial()
        nw34_.ctor__((d_1109_hierarchicalMaterials_).branchKey, d_1105_branchKeyIdUtf8_, d_1115_branchKeyVersionAsBytes_, (self).cryptoPrimitives)
        d_1117_kmsHierarchyGenerateAndWrap_ = nw34_
        d_1118_kmsHierarchyWrap_: AwsKmsHierarchicalKeyring.KmsHierarchyWrapKeyMaterial
        nw35_ = AwsKmsHierarchicalKeyring.KmsHierarchyWrapKeyMaterial()
        nw35_.ctor__((d_1109_hierarchicalMaterials_).branchKey, d_1105_branchKeyIdUtf8_, d_1115_branchKeyVersionAsBytes_, (self).cryptoPrimitives)
        d_1118_kmsHierarchyWrap_ = nw35_
        d_1119_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_1120_valueOrError6_: Wrappers.Result = Wrappers.Result_Success.default(EdkWrapping.WrapEdkMaterialOutput.default(AwsKmsHierarchicalKeyring.HierarchyWrapInfo.default()))()
        out282_: Wrappers.Result
        out282_ = EdkWrapping.default__.WrapEdkMaterial(d_1101_materials_, d_1118_kmsHierarchyWrap_, d_1117_kmsHierarchyGenerateAndWrap_)
        d_1120_valueOrError6_ = out282_
        if (d_1120_valueOrError6_).IsFailure():
            res = (d_1120_valueOrError6_).PropagateFailure()
            return res
        d_1119_wrapOutput_ = (d_1120_valueOrError6_).Extract()
        d_1121_symmetricSigningKeyList_: Wrappers.Option
        d_1121_symmetricSigningKeyList_ = (Wrappers.Option_Some(_dafny.Seq([((d_1119_wrapOutput_).symmetricSigningKey).value])) if ((d_1119_wrapOutput_).symmetricSigningKey).is_Some else Wrappers.Option_None())
        d_1122_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_1122_edk_ = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey((Constants.default__).PROVIDER__ID__HIERARCHY, d_1105_branchKeyIdUtf8_, (d_1119_wrapOutput_).wrappedMaterial)
        if (d_1119_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_1123_result_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            d_1124_valueOrError7_: Wrappers.Result = None
            d_1124_valueOrError7_ = Materials.default__.EncryptionMaterialAddDataKey(d_1101_materials_, (d_1119_wrapOutput_).plaintextDataKey, _dafny.Seq([d_1122_edk_]), d_1121_symmetricSigningKeyList_)
            if (d_1124_valueOrError7_).IsFailure():
                res = (d_1124_valueOrError7_).PropagateFailure()
                return res
            d_1123_result_ = (d_1124_valueOrError7_).Extract()
            res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_1123_result_))
            return res
        elif (d_1119_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_1125_result_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            d_1126_valueOrError8_: Wrappers.Result = None
            d_1126_valueOrError8_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys(d_1101_materials_, _dafny.Seq([d_1122_edk_]), d_1121_symmetricSigningKeyList_)
            if (d_1126_valueOrError8_).IsFailure():
                res = (d_1126_valueOrError8_).PropagateFailure()
                return res
            d_1125_result_ = (d_1126_valueOrError8_).Extract()
            res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_1125_result_))
            return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_1127_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1127_materials_ = (input).materials
        d_1128_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_1128_suite_ = ((input).materials).algorithmSuite
        d_1129_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1129_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_1127_materials_), AwsKmsHierarchicalKeyring.default__.E(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_1129_valueOrError0_).IsFailure():
            res = (d_1129_valueOrError0_).PropagateFailure()
            return res
        d_1130_branchKeyIdForDecrypt_: _dafny.Seq
        d_1131_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out283_: Wrappers.Result
        out283_ = (self).GetBranchKeyId((d_1127_materials_).encryptionContext)
        d_1131_valueOrError1_ = out283_
        if (d_1131_valueOrError1_).IsFailure():
            res = (d_1131_valueOrError1_).PropagateFailure()
            return res
        d_1130_branchKeyIdForDecrypt_ = (d_1131_valueOrError1_).Extract()
        d_1132_filter_: AwsKmsHierarchicalKeyring.OnDecryptHierarchyEncryptedDataKeyFilter
        nw36_ = AwsKmsHierarchicalKeyring.OnDecryptHierarchyEncryptedDataKeyFilter()
        nw36_.ctor__(d_1130_branchKeyIdForDecrypt_)
        d_1132_filter_ = nw36_
        d_1133_edksToAttempt_: _dafny.Seq
        d_1134_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out284_: Wrappers.Result
        out284_ = Actions.default__.FilterWithResult(d_1132_filter_, (input).encryptedDataKeys)
        d_1134_valueOrError2_ = out284_
        if (d_1134_valueOrError2_).IsFailure():
            res = (d_1134_valueOrError2_).PropagateFailure()
            return res
        d_1133_edksToAttempt_ = (d_1134_valueOrError2_).Extract()
        d_1135_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1135_valueOrError3_ = Wrappers.default__.Need((0) < (len(d_1133_edksToAttempt_)), AwsKmsHierarchicalKeyring.default__.E(_dafny.Seq("Unable to decrypt data key: No Encrypted Data Keys found to match.")))
        if (d_1135_valueOrError3_).IsFailure():
            res = (d_1135_valueOrError3_).PropagateFailure()
            return res
        d_1136_decryptClosure_: Actions.ActionWithResult
        nw37_ = AwsKmsHierarchicalKeyring.DecryptSingleEncryptedDataKey()
        nw37_.ctor__(d_1127_materials_, (self).keyStore, (self).cryptoPrimitives, d_1130_branchKeyIdForDecrypt_, (self).ttlSeconds, (self).cache)
        d_1136_decryptClosure_ = nw37_
        d_1137_outcome_: Wrappers.Result
        out285_: Wrappers.Result
        out285_ = Actions.default__.ReduceToSuccess(d_1136_decryptClosure_, d_1133_edksToAttempt_)
        d_1137_outcome_ = out285_
        d_1138_SealedDecryptionMaterials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1139_valueOrError4_: Wrappers.Result = None
        def lambda68_(d_1140_errors_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_CollectionOfErrors(d_1140_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."))

        d_1139_valueOrError4_ = (d_1137_outcome_).MapFailure(lambda68_)
        if (d_1139_valueOrError4_).IsFailure():
            res = (d_1139_valueOrError4_).PropagateFailure()
            return res
        d_1138_SealedDecryptionMaterials_ = (d_1139_valueOrError4_).Extract()
        res = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput_OnDecryptOutput(d_1138_SealedDecryptionMaterials_))
        return res
        return res

    def GetActiveCacheId(self, branchKeyId, branchKeyIdUtf8, cryptoPrimitives):
        cacheId: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1141_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        def iife52_(_pat_let20_0):
            def iife53_(d_1142_branchKeyId_):
                return (True) and (((0) <= (len(d_1142_branchKeyId_))) and ((len(d_1142_branchKeyId_)) < ((StandardLibrary_mUInt.default__).UINT32__LIMIT)))
            return iife53_(_pat_let20_0)
        d_1141_valueOrError0_ = Wrappers.default__.Need((((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).is_Success) and (iife52_(((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).value)), AwsKmsHierarchicalKeyring.default__.E(_dafny.Seq("Invalid Branch Key ID Length")))
        if (d_1141_valueOrError0_).IsFailure():
            cacheId = (d_1141_valueOrError0_).PropagateFailure()
            return cacheId
        d_1143_branchKeyId_: _dafny.Seq
        d_1143_branchKeyId_ = (UTF8.default__.Decode(branchKeyIdUtf8)).value
        d_1144_lenBranchKey_: _dafny.Seq
        d_1144_lenBranchKey_ = StandardLibrary_mUInt.default__.UInt32ToSeq(len(d_1143_branchKeyId_))
        d_1145_hashAlgorithm_: software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm
        d_1145_hashAlgorithm_ = software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__512()
        d_1146_maybeBranchKeyDigest_: Wrappers.Result
        out286_: Wrappers.Result
        out286_ = (cryptoPrimitives).Digest(software_amazon_cryptography_primitives_internaldafny_types.DigestInput_DigestInput(d_1145_hashAlgorithm_, branchKeyIdUtf8))
        d_1146_maybeBranchKeyDigest_ = out286_
        d_1147_branchKeyDigest_: _dafny.Seq
        d_1148_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda69_(d_1149_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1149_e_)

        d_1148_valueOrError1_ = (d_1146_maybeBranchKeyDigest_).MapFailure(lambda69_)
        if (d_1148_valueOrError1_).IsFailure():
            cacheId = (d_1148_valueOrError1_).PropagateFailure()
            return cacheId
        d_1147_branchKeyDigest_ = (d_1148_valueOrError1_).Extract()
        d_1150_activeUtf8_: _dafny.Seq
        d_1151_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(UTF8.ValidUTF8Bytes.default)()
        d_1151_valueOrError2_ = (UTF8.default__.Encode((AwsKmsHierarchicalKeyring.default__).EXPRESSION__ATTRIBUTE__VALUE__STATUS__VALUE)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_1151_valueOrError2_).IsFailure():
            cacheId = (d_1151_valueOrError2_).PropagateFailure()
            return cacheId
        d_1150_activeUtf8_ = (d_1151_valueOrError2_).Extract()
        d_1152_identifier_: _dafny.Seq
        d_1152_identifier_ = (((d_1144_lenBranchKey_) + (d_1147_branchKeyDigest_)) + (_dafny.Seq([0]))) + (d_1150_activeUtf8_)
        d_1153_maybeCacheIdDigest_: Wrappers.Result
        out287_: Wrappers.Result
        out287_ = (cryptoPrimitives).Digest(software_amazon_cryptography_primitives_internaldafny_types.DigestInput_DigestInput(d_1145_hashAlgorithm_, d_1152_identifier_))
        d_1153_maybeCacheIdDigest_ = out287_
        d_1154_cacheDigest_: _dafny.Seq
        d_1155_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda70_(d_1156_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1156_e_)

        d_1155_valueOrError3_ = (d_1153_maybeCacheIdDigest_).MapFailure(lambda70_)
        if (d_1155_valueOrError3_).IsFailure():
            cacheId = (d_1155_valueOrError3_).PropagateFailure()
            return cacheId
        d_1154_cacheDigest_ = (d_1155_valueOrError3_).Extract()
        d_1157_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1157_valueOrError4_ = Wrappers.default__.Need((len(d_1154_cacheDigest_)) == (Digest.default__.Length(d_1145_hashAlgorithm_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Digest generated a message not equal to the expected length.")))
        if (d_1157_valueOrError4_).IsFailure():
            cacheId = (d_1157_valueOrError4_).PropagateFailure()
            return cacheId
        cacheId = Wrappers.Result_Success(_dafny.Seq((d_1154_cacheDigest_)[0:32:]))
        return cacheId
        return cacheId

    def GetActiveHierarchicalMaterials(self, branchKeyId, cacheId, keyStore):
        material: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials.default())()
        d_1158_getCacheInput_: software_amazon_cryptography_materialproviders_internaldafny_types.GetCacheEntryInput
        d_1158_getCacheInput_ = software_amazon_cryptography_materialproviders_internaldafny_types.GetCacheEntryInput_GetCacheEntryInput(cacheId, Wrappers.Option_None())
        d_1159_getCacheOutput_: Wrappers.Result
        out288_: Wrappers.Result
        out288_ = AwsKmsHierarchicalKeyring.default__.getEntry((self).cache, d_1158_getCacheInput_)
        d_1159_getCacheOutput_ = out288_
        if (d_1159_getCacheOutput_).is_Failure:
            d_1160_maybeGetActiveBranchKeyOutput_: Wrappers.Result
            out289_: Wrappers.Result
            out289_ = (keyStore).GetActiveBranchKey(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyInput_GetActiveBranchKeyInput(branchKeyId))
            d_1160_maybeGetActiveBranchKeyOutput_ = out289_
            d_1161_getActiveBranchKeyOutput_: software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput
            d_1162_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.GetActiveBranchKeyOutput.default())()
            def lambda71_(d_1163_e_):
                return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyKeyStore(d_1163_e_)

            d_1162_valueOrError0_ = (d_1160_maybeGetActiveBranchKeyOutput_).MapFailure(lambda71_)
            if (d_1162_valueOrError0_).IsFailure():
                material = (d_1162_valueOrError0_).PropagateFailure()
                return material
            d_1161_getActiveBranchKeyOutput_ = (d_1162_valueOrError0_).Extract()
            d_1164_branchKeyMaterials_: software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials
            d_1164_branchKeyMaterials_ = (d_1161_getActiveBranchKeyOutput_).branchKeyMaterials
            d_1165_now_: BoundedInts.int64
            out290_: BoundedInts.int64
            out290_ = Time.default__.CurrentRelativeTime()
            d_1165_now_ = out290_
            d_1166_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
            d_1166_valueOrError1_ = Wrappers.default__.Need(((d_1165_now_) + ((self).ttlSeconds)) < ((StandardLibrary_mUInt.default__).INT64__MAX__LIMIT), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("INT64 Overflow when putting cache entry.")))
            if (d_1166_valueOrError1_).IsFailure():
                material = (d_1166_valueOrError1_).PropagateFailure()
                return material
            d_1167_putCacheEntryInput_: software_amazon_cryptography_materialproviders_internaldafny_types.PutCacheEntryInput
            d_1167_putCacheEntryInput_ = software_amazon_cryptography_materialproviders_internaldafny_types.PutCacheEntryInput_PutCacheEntryInput(cacheId, software_amazon_cryptography_materialproviders_internaldafny_types.Materials_BranchKey(d_1164_branchKeyMaterials_), d_1165_now_, ((self).ttlSeconds) + (d_1165_now_), Wrappers.Option_None(), Wrappers.Option_None())
            d_1168___v0_: tuple
            d_1169_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
            out291_: Wrappers.Result
            out291_ = AwsKmsHierarchicalKeyring.default__.putEntry((self).cache, d_1167_putCacheEntryInput_)
            d_1169_valueOrError2_ = out291_
            if (d_1169_valueOrError2_).IsFailure():
                material = (d_1169_valueOrError2_).PropagateFailure()
                return material
            d_1168___v0_ = (d_1169_valueOrError2_).Extract()
            material = Wrappers.Result_Success(d_1164_branchKeyMaterials_)
            return material
        elif True:
            d_1170_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
            d_1170_valueOrError3_ = Wrappers.default__.Need(((((d_1159_getCacheOutput_).value).materials).is_BranchKey) and ((((d_1159_getCacheOutput_).value).materials) == (software_amazon_cryptography_materialproviders_internaldafny_types.Materials_BranchKey((((d_1159_getCacheOutput_).value).materials).BranchKey))), AwsKmsHierarchicalKeyring.default__.E(_dafny.Seq("Invalid Material Type.")))
            if (d_1170_valueOrError3_).IsFailure():
                material = (d_1170_valueOrError3_).PropagateFailure()
                return material
            material = Wrappers.Result_Success((((d_1159_getCacheOutput_).value).materials).BranchKey)
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
        d_1171_providerInfo_: _dafny.Seq
        d_1171_providerInfo_ = (edk).keyProviderInfo
        d_1172_providerId_: _dafny.Seq
        d_1172_providerId_ = (edk).keyProviderId
        if (d_1172_providerId_) != ((Constants.default__).PROVIDER__ID__HIERARCHY):
            res = Wrappers.Result_Success(False)
            return res
        if not(UTF8.default__.ValidUTF8Seq(d_1171_providerInfo_)):
            res = Wrappers.Result_Failure(AwsKmsHierarchicalKeyring.default__.E(_dafny.Seq("Invalid encoding, provider info is not UTF8.")))
            return res
        d_1173_branchKeyId_: _dafny.Seq
        d_1174_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1174_valueOrError0_ = (UTF8.default__.Decode(d_1171_providerInfo_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_1174_valueOrError0_).IsFailure():
            res = (d_1174_valueOrError0_).PropagateFailure()
            return res
        d_1173_branchKeyId_ = (d_1174_valueOrError0_).Extract()
        res = Wrappers.Result_Success(((self).branchKeyId) == (d_1173_branchKeyId_))
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
        d_1175_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1175_valueOrError0_ = Wrappers.default__.Need(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received invalid EDK provider info for Hierarchical Keyring")))
        if (d_1175_valueOrError0_).IsFailure():
            res = (d_1175_valueOrError0_).PropagateFailure()
            return res
        d_1176_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_1176_suite_ = ((self).materials).algorithmSuite
        d_1177_keyProviderId_: _dafny.Seq
        d_1177_keyProviderId_ = (edk).keyProviderId
        d_1178_branchKeyIdUtf8_: _dafny.Seq
        d_1178_branchKeyIdUtf8_ = (edk).keyProviderInfo
        d_1179_ciphertext_: _dafny.Seq
        d_1179_ciphertext_ = (edk).ciphertext
        d_1180_providerWrappedMaterial_: _dafny.Seq
        d_1181_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1181_valueOrError1_ = EdkWrapping.default__.GetProviderWrappedMaterial(d_1179_ciphertext_, d_1176_suite_)
        if (d_1181_valueOrError1_).IsFailure():
            res = (d_1181_valueOrError1_).PropagateFailure()
            return res
        d_1180_providerWrappedMaterial_ = (d_1181_valueOrError1_).Extract()
        d_1182_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1182_valueOrError2_ = Wrappers.default__.Need((len(d_1180_providerWrappedMaterial_)) >= ((AwsKmsHierarchicalKeyring.default__).EDK__CIPHERTEXT__VERSION__INDEX), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received EDK Ciphertext of incorrect length.")))
        if (d_1182_valueOrError2_).IsFailure():
            res = (d_1182_valueOrError2_).PropagateFailure()
            return res
        d_1183_branchKeyVersionUuid_: _dafny.Seq
        d_1183_branchKeyVersionUuid_ = _dafny.Seq((d_1180_providerWrappedMaterial_)[(AwsKmsHierarchicalKeyring.default__).EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX:(AwsKmsHierarchicalKeyring.default__).EDK__CIPHERTEXT__VERSION__INDEX:])
        d_1184_version_: _dafny.Seq
        d_1185_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1185_valueOrError3_ = (UUID.default__.FromByteArray(d_1183_branchKeyVersionUuid_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_1185_valueOrError3_).IsFailure():
            res = (d_1185_valueOrError3_).PropagateFailure()
            return res
        d_1184_version_ = (d_1185_valueOrError3_).Extract()
        d_1186_cacheId_: _dafny.Seq
        d_1187_valueOrError4_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out292_: Wrappers.Result
        out292_ = (self).GetVersionCacheId(d_1178_branchKeyIdUtf8_, d_1184_version_, (self).cryptoPrimitives)
        d_1187_valueOrError4_ = out292_
        if (d_1187_valueOrError4_).IsFailure():
            res = (d_1187_valueOrError4_).PropagateFailure()
            return res
        d_1186_cacheId_ = (d_1187_valueOrError4_).Extract()
        d_1188_hierarchicalMaterials_: software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials
        d_1189_valueOrError5_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials.default())()
        out293_: Wrappers.Result
        out293_ = (self).GetHierarchicalMaterialsVersion((self).branchKeyId, d_1178_branchKeyIdUtf8_, d_1184_version_, d_1186_cacheId_)
        d_1189_valueOrError5_ = out293_
        if (d_1189_valueOrError5_).IsFailure():
            res = (d_1189_valueOrError5_).PropagateFailure()
            return res
        d_1188_hierarchicalMaterials_ = (d_1189_valueOrError5_).Extract()
        d_1190_branchKey_: _dafny.Seq
        d_1190_branchKey_ = (d_1188_hierarchicalMaterials_).branchKey
        d_1191_branchKeyVersion_: _dafny.Seq
        d_1191_branchKeyVersion_ = (d_1188_hierarchicalMaterials_).branchKeyVersion
        d_1192_branchKeyVersionAsString_: _dafny.Seq
        d_1193_valueOrError6_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1193_valueOrError6_ = (UTF8.default__.Decode(d_1191_branchKeyVersion_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_1193_valueOrError6_).IsFailure():
            res = (d_1193_valueOrError6_).PropagateFailure()
            return res
        d_1192_branchKeyVersionAsString_ = (d_1193_valueOrError6_).Extract()
        d_1194_branchKeyVersionAsBytes_: _dafny.Seq
        d_1195_valueOrError7_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1195_valueOrError7_ = (UUID.default__.ToByteArray(d_1192_branchKeyVersionAsString_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_1195_valueOrError7_).IsFailure():
            res = (d_1195_valueOrError7_).PropagateFailure()
            return res
        d_1194_branchKeyVersionAsBytes_ = (d_1195_valueOrError7_).Extract()
        d_1196_maybeCrypto_: Wrappers.Result
        out294_: Wrappers.Result
        out294_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_1196_maybeCrypto_ = out294_
        d_1197_crypto_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_1198_valueOrError8_: Wrappers.Result = None
        def lambda72_(d_1199_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1199_e_)

        d_1198_valueOrError8_ = (d_1196_maybeCrypto_).MapFailure(lambda72_)
        if (d_1198_valueOrError8_).IsFailure():
            res = (d_1198_valueOrError8_).PropagateFailure()
            return res
        d_1197_crypto_ = (d_1198_valueOrError8_).Extract()
        d_1200_kmsHierarchyUnwrap_: AwsKmsHierarchicalKeyring.KmsHierarchyUnwrapKeyMaterial
        nw38_ = AwsKmsHierarchicalKeyring.KmsHierarchyUnwrapKeyMaterial()
        nw38_.ctor__(d_1190_branchKey_, d_1178_branchKeyIdUtf8_, d_1194_branchKeyVersionAsBytes_, d_1197_crypto_)
        d_1200_kmsHierarchyUnwrap_ = nw38_
        d_1201_unwrapOutputRes_: Wrappers.Result
        out295_: Wrappers.Result
        out295_ = EdkWrapping.default__.UnwrapEdkMaterial((edk).ciphertext, (self).materials, d_1200_kmsHierarchyUnwrap_)
        d_1201_unwrapOutputRes_ = out295_
        d_1202_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_1203_valueOrError9_: Wrappers.Result = Wrappers.Result_Success.default(EdkWrapping.UnwrapEdkMaterialOutput.default(AwsKmsHierarchicalKeyring.HierarchyUnwrapInfo.default()))()
        d_1203_valueOrError9_ = d_1201_unwrapOutputRes_
        if (d_1203_valueOrError9_).IsFailure():
            res = (d_1203_valueOrError9_).PropagateFailure()
            return res
        d_1202_unwrapOutput_ = (d_1203_valueOrError9_).Extract()
        d_1204_result_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1205_valueOrError10_: Wrappers.Result = None
        d_1205_valueOrError10_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_1202_unwrapOutput_).plaintextDataKey, (d_1202_unwrapOutput_).symmetricSigningKey)
        if (d_1205_valueOrError10_).IsFailure():
            res = (d_1205_valueOrError10_).PropagateFailure()
            return res
        d_1204_result_ = (d_1205_valueOrError10_).Extract()
        res = Wrappers.Result_Success(d_1204_result_)
        return res
        return res

    def GetVersionCacheId(self, branchKeyIdUtf8, branchKeyVersion, cryptoPrimitives):
        cacheId: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1206_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        def iife54_(_pat_let21_0):
            def iife55_(d_1207_branchKeyId_):
                return (True) and (((0) <= (len(d_1207_branchKeyId_))) and ((len(d_1207_branchKeyId_)) < ((StandardLibrary_mUInt.default__).UINT32__LIMIT)))
            return iife55_(_pat_let21_0)
        d_1206_valueOrError0_ = Wrappers.default__.Need((((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).is_Success) and (iife54_(((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).value)), AwsKmsHierarchicalKeyring.default__.E(_dafny.Seq("Invalid Branch Key ID Length")))
        if (d_1206_valueOrError0_).IsFailure():
            cacheId = (d_1206_valueOrError0_).PropagateFailure()
            return cacheId
        d_1208_branchKeyId_: _dafny.Seq
        d_1208_branchKeyId_ = (UTF8.default__.Decode(branchKeyIdUtf8)).value
        d_1209_lenBranchKey_: _dafny.Seq
        d_1209_lenBranchKey_ = StandardLibrary_mUInt.default__.UInt32ToSeq(len(d_1208_branchKeyId_))
        d_1210_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1210_valueOrError1_ = Wrappers.default__.Need(UTF8.default__.IsASCIIString(branchKeyVersion), AwsKmsHierarchicalKeyring.default__.E(_dafny.Seq("Unable to represent as an ASCII string.")))
        if (d_1210_valueOrError1_).IsFailure():
            cacheId = (d_1210_valueOrError1_).PropagateFailure()
            return cacheId
        d_1211_versionBytes_: _dafny.Seq
        d_1211_versionBytes_ = UTF8.default__.EncodeAscii(branchKeyVersion)
        d_1212_identifier_: _dafny.Seq
        d_1212_identifier_ = (((d_1209_lenBranchKey_) + (branchKeyIdUtf8)) + (_dafny.Seq([0]))) + (d_1211_versionBytes_)
        d_1213_identifierDigestInput_: software_amazon_cryptography_primitives_internaldafny_types.DigestInput
        d_1213_identifierDigestInput_ = software_amazon_cryptography_primitives_internaldafny_types.DigestInput_DigestInput(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__512(), d_1212_identifier_)
        d_1214_maybeCacheDigest_: Wrappers.Result
        out296_: Wrappers.Result
        out296_ = Digest.default__.Digest(d_1213_identifierDigestInput_)
        d_1214_maybeCacheDigest_ = out296_
        d_1215_cacheDigest_: _dafny.Seq
        d_1216_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda73_(d_1217_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1217_e_)

        d_1216_valueOrError2_ = (d_1214_maybeCacheDigest_).MapFailure(lambda73_)
        if (d_1216_valueOrError2_).IsFailure():
            cacheId = (d_1216_valueOrError2_).PropagateFailure()
            return cacheId
        d_1215_cacheDigest_ = (d_1216_valueOrError2_).Extract()
        cacheId = Wrappers.Result_Success(_dafny.Seq((d_1215_cacheDigest_)[0:32:]))
        return cacheId
        return cacheId

    def GetHierarchicalMaterialsVersion(self, branchKeyId, branchKeyIdUtf8, version, cacheId):
        material: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials.default())()
        d_1218_getCacheInput_: software_amazon_cryptography_materialproviders_internaldafny_types.GetCacheEntryInput
        d_1218_getCacheInput_ = software_amazon_cryptography_materialproviders_internaldafny_types.GetCacheEntryInput_GetCacheEntryInput(cacheId, Wrappers.Option_None())
        d_1219_getCacheOutput_: Wrappers.Result
        out297_: Wrappers.Result
        out297_ = AwsKmsHierarchicalKeyring.default__.getEntry((self).cache, d_1218_getCacheInput_)
        d_1219_getCacheOutput_ = out297_
        if (d_1219_getCacheOutput_).is_Failure:
            d_1220_maybeGetBranchKeyVersionOutput_: Wrappers.Result
            out298_: Wrappers.Result
            out298_ = ((self).keyStore).GetBranchKeyVersion(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionInput_GetBranchKeyVersionInput(branchKeyId, version))
            d_1220_maybeGetBranchKeyVersionOutput_ = out298_
            d_1221_getBranchKeyVersionOutput_: software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput
            d_1222_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_keystore_internaldafny_types.GetBranchKeyVersionOutput.default())()
            def lambda74_(d_1223_e_):
                return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyKeyStore(d_1223_e_)

            d_1222_valueOrError0_ = (d_1220_maybeGetBranchKeyVersionOutput_).MapFailure(lambda74_)
            if (d_1222_valueOrError0_).IsFailure():
                material = (d_1222_valueOrError0_).PropagateFailure()
                return material
            d_1221_getBranchKeyVersionOutput_ = (d_1222_valueOrError0_).Extract()
            d_1224_branchKeyMaterials_: software_amazon_cryptography_keystore_internaldafny_types.BranchKeyMaterials
            d_1224_branchKeyMaterials_ = (d_1221_getBranchKeyVersionOutput_).branchKeyMaterials
            d_1225_now_: BoundedInts.int64
            out299_: BoundedInts.int64
            out299_ = Time.default__.CurrentRelativeTime()
            d_1225_now_ = out299_
            d_1226_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
            d_1226_valueOrError1_ = Wrappers.default__.Need(((d_1225_now_) + ((self).ttlSeconds)) < ((StandardLibrary_mUInt.default__).INT64__MAX__LIMIT), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("INT64 Overflow when putting cache entry.")))
            if (d_1226_valueOrError1_).IsFailure():
                material = (d_1226_valueOrError1_).PropagateFailure()
                return material
            d_1227_putCacheEntryInput_: software_amazon_cryptography_materialproviders_internaldafny_types.PutCacheEntryInput
            d_1227_putCacheEntryInput_ = software_amazon_cryptography_materialproviders_internaldafny_types.PutCacheEntryInput_PutCacheEntryInput(cacheId, software_amazon_cryptography_materialproviders_internaldafny_types.Materials_BranchKey(d_1224_branchKeyMaterials_), d_1225_now_, ((self).ttlSeconds) + (d_1225_now_), Wrappers.Option_None(), Wrappers.Option_None())
            d_1228___v1_: tuple
            d_1229_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
            out300_: Wrappers.Result
            out300_ = AwsKmsHierarchicalKeyring.default__.putEntry((self).cache, d_1227_putCacheEntryInput_)
            d_1229_valueOrError2_ = out300_
            if (d_1229_valueOrError2_).IsFailure():
                material = (d_1229_valueOrError2_).PropagateFailure()
                return material
            d_1228___v1_ = (d_1229_valueOrError2_).Extract()
            material = Wrappers.Result_Success(d_1224_branchKeyMaterials_)
            return material
        elif True:
            d_1230_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
            d_1230_valueOrError3_ = Wrappers.default__.Need(((((d_1219_getCacheOutput_).value).materials).is_BranchKey) and ((((d_1219_getCacheOutput_).value).materials) == (software_amazon_cryptography_materialproviders_internaldafny_types.Materials_BranchKey((((d_1219_getCacheOutput_).value).materials).BranchKey))), AwsKmsHierarchicalKeyring.default__.E(_dafny.Seq("Invalid Material Type.")))
            if (d_1230_valueOrError3_).IsFailure():
                material = (d_1230_valueOrError3_).PropagateFailure()
                return material
            material = Wrappers.Result_Success((((d_1219_getCacheOutput_).value).materials).BranchKey)
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
        d_1231_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_1231_suite_ = (input).algorithmSuite
        d_1232_wrappedMaterial_: _dafny.Seq
        d_1232_wrappedMaterial_ = (input).wrappedMaterial
        d_1233_aad_: _dafny.Map
        d_1233_aad_ = (input).encryptionContext
        d_1234_KeyLength_: BoundedInts.int32
        d_1234_KeyLength_ = AlgorithmSuites.default__.GetEncryptKeyLength(d_1231_suite_)
        d_1235_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1235_valueOrError0_ = Wrappers.default__.Need((len(d_1232_wrappedMaterial_)) == (((AwsKmsHierarchicalKeyring.default__).EXPECTED__EDK__CIPHERTEXT__OVERHEAD) + (d_1234_KeyLength_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received EDK Ciphertext of incorrect length2.")))
        if (d_1235_valueOrError0_).IsFailure():
            res = (d_1235_valueOrError0_).PropagateFailure()
            return res
        d_1236_salt_: _dafny.Seq
        d_1236_salt_ = _dafny.Seq((d_1232_wrappedMaterial_)[0:(AwsKmsHierarchicalKeyring.default__).H__WRAP__SALT__LEN:])
        d_1237_iv_: _dafny.Seq
        d_1237_iv_ = _dafny.Seq((d_1232_wrappedMaterial_)[(AwsKmsHierarchicalKeyring.default__).H__WRAP__SALT__LEN:(AwsKmsHierarchicalKeyring.default__).EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX:])
        d_1238_branchKeyVersionUuid_: _dafny.Seq
        d_1238_branchKeyVersionUuid_ = _dafny.Seq((d_1232_wrappedMaterial_)[(AwsKmsHierarchicalKeyring.default__).EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX:(AwsKmsHierarchicalKeyring.default__).EDK__CIPHERTEXT__VERSION__INDEX:])
        d_1239_wrappedKey_: _dafny.Seq
        d_1239_wrappedKey_ = _dafny.Seq((d_1232_wrappedMaterial_)[(AwsKmsHierarchicalKeyring.default__).EDK__CIPHERTEXT__VERSION__INDEX:((AwsKmsHierarchicalKeyring.default__).EDK__CIPHERTEXT__VERSION__INDEX) + (d_1234_KeyLength_):])
        d_1240_authTag_: _dafny.Seq
        d_1240_authTag_ = _dafny.Seq((d_1232_wrappedMaterial_)[((AwsKmsHierarchicalKeyring.default__).EDK__CIPHERTEXT__VERSION__INDEX) + (d_1234_KeyLength_)::])
        d_1241_serializedEC_: _dafny.Seq
        d_1242_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1242_valueOrError1_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_1242_valueOrError1_).IsFailure():
            res = (d_1242_valueOrError1_).PropagateFailure()
            return res
        d_1241_serializedEC_ = (d_1242_valueOrError1_).Extract()
        d_1243_wrappingAad_: _dafny.Seq
        d_1243_wrappingAad_ = AwsKmsHierarchicalKeyring.default__.WrappingAad((self).branchKeyIdUtf8, (self).branchKeyVersionAsBytes, d_1241_serializedEC_)
        d_1244_derivedBranchKey_: _dafny.Seq
        d_1245_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out301_: Wrappers.Result
        out301_ = AwsKmsHierarchicalKeyring.default__.DeriveEncryptionKeyFromBranchKey((self).branchKey, d_1236_salt_, Wrappers.Option_Some((Constants.default__).PROVIDER__ID__HIERARCHY), (self).crypto)
        d_1245_valueOrError2_ = out301_
        if (d_1245_valueOrError2_).IsFailure():
            res = (d_1245_valueOrError2_).PropagateFailure()
            return res
        d_1244_derivedBranchKey_ = (d_1245_valueOrError2_).Extract()
        d_1246_maybeUnwrappedPdk_: Wrappers.Result
        out302_: Wrappers.Result
        out302_ = ((self).crypto).AESDecrypt(software_amazon_cryptography_primitives_internaldafny_types.AESDecryptInput_AESDecryptInput((AwsKmsHierarchicalKeyring.default__).AES__256__ENC__ALG, d_1244_derivedBranchKey_, d_1239_wrappedKey_, d_1240_authTag_, d_1237_iv_, d_1243_wrappingAad_))
        d_1246_maybeUnwrappedPdk_ = out302_
        d_1247_unwrappedPdk_: _dafny.Seq
        d_1248_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda75_(d_1249_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1249_e_)

        d_1248_valueOrError3_ = (d_1246_maybeUnwrappedPdk_).MapFailure(lambda75_)
        if (d_1248_valueOrError3_).IsFailure():
            res = (d_1248_valueOrError3_).PropagateFailure()
            return res
        d_1247_unwrappedPdk_ = (d_1248_valueOrError3_).Extract()
        d_1250_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_1250_valueOrError4_ = Wrappers.default__.Need((len(d_1247_unwrappedPdk_)) == (AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)), AwsKmsHierarchicalKeyring.default__.E(_dafny.Seq("Invalid Key Length")))
        if (d_1250_valueOrError4_).IsFailure():
            res = (d_1250_valueOrError4_).PropagateFailure()
            return res
        d_1251_output_: MaterialWrapping.UnwrapOutput
        d_1251_output_ = MaterialWrapping.UnwrapOutput_UnwrapOutput(d_1247_unwrappedPdk_, AwsKmsHierarchicalKeyring.HierarchyUnwrapInfo_HierarchyUnwrapInfo())
        res = Wrappers.Result_Success(d_1251_output_)
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
        d_1252_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_1252_suite_ = (input).algorithmSuite
        d_1253_pdkResult_: Wrappers.Result
        out303_: Wrappers.Result
        out303_ = ((self).crypto).GenerateRandomBytes(software_amazon_cryptography_primitives_internaldafny_types.GenerateRandomBytesInput_GenerateRandomBytesInput(AlgorithmSuites.default__.GetEncryptKeyLength(d_1252_suite_)))
        d_1253_pdkResult_ = out303_
        d_1254_pdk_: _dafny.Seq
        d_1255_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda76_(d_1256_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1256_e_)

        d_1255_valueOrError0_ = (d_1253_pdkResult_).MapFailure(lambda76_)
        if (d_1255_valueOrError0_).IsFailure():
            res = (d_1255_valueOrError0_).PropagateFailure()
            return res
        d_1254_pdk_ = (d_1255_valueOrError0_).Extract()
        d_1257_wrap_: AwsKmsHierarchicalKeyring.KmsHierarchyWrapKeyMaterial
        nw39_ = AwsKmsHierarchicalKeyring.KmsHierarchyWrapKeyMaterial()
        nw39_.ctor__((self).branchKey, (self).branchKeyIdUtf8, (self).branchKeyVersionAsBytes, (self).crypto)
        d_1257_wrap_ = nw39_
        d_1258_wrapOutput_: MaterialWrapping.WrapOutput
        d_1259_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(MaterialWrapping.WrapOutput.default(AwsKmsHierarchicalKeyring.HierarchyWrapInfo.default()))()
        out304_: Wrappers.Result
        out304_ = (d_1257_wrap_).Invoke(MaterialWrapping.WrapInput_WrapInput(d_1254_pdk_, (input).algorithmSuite, (input).encryptionContext))
        d_1259_valueOrError1_ = out304_
        if (d_1259_valueOrError1_).IsFailure():
            res = (d_1259_valueOrError1_).PropagateFailure()
            return res
        d_1258_wrapOutput_ = (d_1259_valueOrError1_).Extract()
        d_1260_output_: MaterialWrapping.GenerateAndWrapOutput
        d_1260_output_ = MaterialWrapping.GenerateAndWrapOutput_GenerateAndWrapOutput(d_1254_pdk_, (d_1258_wrapOutput_).wrappedMaterial, AwsKmsHierarchicalKeyring.HierarchyWrapInfo_HierarchyWrapInfo())
        res = Wrappers.Result_Success(d_1260_output_)
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
        d_1261_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_1261_suite_ = (input).algorithmSuite
        d_1262_maybeNonceSalt_: Wrappers.Result
        out305_: Wrappers.Result
        out305_ = ((self).crypto).GenerateRandomBytes(software_amazon_cryptography_primitives_internaldafny_types.GenerateRandomBytesInput_GenerateRandomBytesInput(((AwsKmsHierarchicalKeyring.default__).H__WRAP__SALT__LEN) + ((AwsKmsHierarchicalKeyring.default__).H__WRAP__NONCE__LEN)))
        d_1262_maybeNonceSalt_ = out305_
        d_1263_saltAndNonce_: _dafny.Seq
        d_1264_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        def lambda77_(d_1265_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1265_e_)

        d_1264_valueOrError0_ = (d_1262_maybeNonceSalt_).MapFailure(lambda77_)
        if (d_1264_valueOrError0_).IsFailure():
            res = (d_1264_valueOrError0_).PropagateFailure()
            return res
        d_1263_saltAndNonce_ = (d_1264_valueOrError0_).Extract()
        d_1266_salt_: _dafny.Seq
        d_1266_salt_ = _dafny.Seq((d_1263_saltAndNonce_)[0:(AwsKmsHierarchicalKeyring.default__).H__WRAP__SALT__LEN:])
        d_1267_nonce_: _dafny.Seq
        d_1267_nonce_ = _dafny.Seq((d_1263_saltAndNonce_)[(AwsKmsHierarchicalKeyring.default__).H__WRAP__SALT__LEN::])
        d_1268_serializedEC_: _dafny.Seq
        d_1269_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_1269_valueOrError1_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_1269_valueOrError1_).IsFailure():
            res = (d_1269_valueOrError1_).PropagateFailure()
            return res
        d_1268_serializedEC_ = (d_1269_valueOrError1_).Extract()
        d_1270_wrappingAad_: _dafny.Seq
        d_1270_wrappingAad_ = AwsKmsHierarchicalKeyring.default__.WrappingAad((self).branchKeyIdUtf8, (self).branchKeyVersionAsBytes, d_1268_serializedEC_)
        d_1271_derivedBranchKey_: _dafny.Seq
        d_1272_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out306_: Wrappers.Result
        out306_ = AwsKmsHierarchicalKeyring.default__.DeriveEncryptionKeyFromBranchKey((self).branchKey, d_1266_salt_, Wrappers.Option_Some((Constants.default__).PROVIDER__ID__HIERARCHY), (self).crypto)
        d_1272_valueOrError2_ = out306_
        if (d_1272_valueOrError2_).IsFailure():
            res = (d_1272_valueOrError2_).PropagateFailure()
            return res
        d_1271_derivedBranchKey_ = (d_1272_valueOrError2_).Extract()
        d_1273_maybeWrappedPdk_: Wrappers.Result
        out307_: Wrappers.Result
        out307_ = ((self).crypto).AESEncrypt(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptInput_AESEncryptInput((AwsKmsHierarchicalKeyring.default__).AES__256__ENC__ALG, d_1267_nonce_, d_1271_derivedBranchKey_, (input).plaintextMaterial, d_1270_wrappingAad_))
        d_1273_maybeWrappedPdk_ = out307_
        d_1274_wrappedPdk_: software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput
        d_1275_valueOrError3_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput.default())()
        def lambda78_(d_1276_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1276_e_)

        d_1275_valueOrError3_ = (d_1273_maybeWrappedPdk_).MapFailure(lambda78_)
        if (d_1275_valueOrError3_).IsFailure():
            res = (d_1275_valueOrError3_).PropagateFailure()
            return res
        d_1274_wrappedPdk_ = (d_1275_valueOrError3_).Extract()
        d_1277_output_: MaterialWrapping.WrapOutput
        d_1277_output_ = MaterialWrapping.WrapOutput_WrapOutput(((((d_1266_salt_) + (d_1267_nonce_)) + ((self).branchKeyVersionAsBytes)) + ((d_1274_wrappedPdk_).cipherText)) + ((d_1274_wrappedPdk_).authTag), AwsKmsHierarchicalKeyring.HierarchyWrapInfo_HierarchyWrapInfo())
        res = Wrappers.Result_Success(d_1277_output_)
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
