import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptographic_materialproviders.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import standard_library.internaldafny.generated.Wrappers as Wrappers
import standard_library.internaldafny.generated.BoundedInts as BoundedInts
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import standard_library.internaldafny.generated.UTF8 as UTF8
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes as AwsCryptographyPrimitivesTypes
import aws_cryptography_primitives.internaldafny.generated.ExternRandom as ExternRandom
import aws_cryptography_primitives.internaldafny.generated.Random as Random
import aws_cryptography_primitives.internaldafny.generated.AESEncryption as AESEncryption
import aws_cryptography_primitives.internaldafny.generated.ExternDigest as ExternDigest
import aws_cryptography_primitives.internaldafny.generated.Digest as Digest
import aws_cryptography_primitives.internaldafny.generated.HMAC as HMAC
import aws_cryptography_primitives.internaldafny.generated.WrappedHMAC as WrappedHMAC
import aws_cryptography_primitives.internaldafny.generated.HKDF as HKDF
import aws_cryptography_primitives.internaldafny.generated.WrappedHKDF as WrappedHKDF
import aws_cryptography_primitives.internaldafny.generated.Signature as Signature
import aws_cryptography_primitives.internaldafny.generated.KdfCtr as KdfCtr
import aws_cryptography_primitives.internaldafny.generated.RSAEncryption as RSAEncryption
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesOperations as AwsCryptographyPrimitivesOperations
import aws_cryptography_primitives.internaldafny.generated.AtomicPrimitives as AtomicPrimitives
import com_amazonaws_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import com_amazonaws_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
import standard_library.internaldafny.generated.Relations as Relations
import standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import standard_library.internaldafny.generated.Math as Math
import standard_library.internaldafny.generated.Seq as Seq
import standard_library.internaldafny.generated.Unicode as Unicode
import standard_library.internaldafny.generated.Functions as Functions
import standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import standard_library.internaldafny.generated.FileIO as FileIO
import standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import standard_library.internaldafny.generated.MulInternals as MulInternals
import standard_library.internaldafny.generated.Mul as Mul
import standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import standard_library.internaldafny.generated.ModInternals as ModInternals
import standard_library.internaldafny.generated.DivInternals as DivInternals
import standard_library.internaldafny.generated.DivMod as DivMod
import standard_library.internaldafny.generated.Power as Power
import standard_library.internaldafny.generated.Logarithm as Logarithm
import standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import standard_library.internaldafny.generated.UUID as UUID
import standard_library.internaldafny.generated.Time as Time
import standard_library.internaldafny.generated.Streams as Streams
import standard_library.internaldafny.generated.Sorting as Sorting
import standard_library.internaldafny.generated.SortedSets as SortedSets
import standard_library.internaldafny.generated.HexStrings as HexStrings
import standard_library.internaldafny.generated.GetOpt as GetOpt
import standard_library.internaldafny.generated.FloatCompare as FloatCompare
import standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import standard_library.internaldafny.generated.Base64 as Base64
import standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import standard_library.internaldafny.generated.Actions as Actions
import standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_materialproviders.internaldafny.generated.Structure as Structure
import aws_cryptographic_materialproviders.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable
import aws_cryptographic_materialproviders.internaldafny.generated.GetKeys as GetKeys
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import com_amazonaws_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws as Com_Amazonaws
import com_amazonaws_dynamodb.internaldafny.generated.Com as Com
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStore as KeyStore
import aws_cryptographic_materialproviders.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_materialproviders.internaldafny.generated.Materials as Materials
import aws_cryptographic_materialproviders.internaldafny.generated.Keyring as Keyring
import aws_cryptographic_materialproviders.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import aws_cryptographic_materialproviders.internaldafny.generated.Constants as Constants
import aws_cryptographic_materialproviders.internaldafny.generated.MaterialWrapping as MaterialWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_materialproviders.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.EdkWrapping as EdkWrapping
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsKeyring as AwsKmsKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.StrictMultiKeyring as StrictMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsDiscoveryKeyring as AwsKmsDiscoveryKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.DiscoveryMultiKeyring as DiscoveryMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkDiscoveryKeyring as AwsKmsMrkDiscoveryKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.MrkAwareDiscoveryMultiKeyring as MrkAwareDiscoveryMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkKeyring as AwsKmsMrkKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.MrkAwareStrictMultiKeyring as MrkAwareStrictMultiKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.LocalCMC as LocalCMC
import aws_cryptographic_materialproviders.internaldafny.generated.SynchronizedLocalCMC as SynchronizedLocalCMC
import aws_cryptographic_materialproviders.internaldafny.generated.StormTracker as StormTracker
import aws_cryptographic_materialproviders.internaldafny.generated.StormTrackingCMC as StormTrackingCMC

# Module: aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsHierarchicalKeyring

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
        d_812_maybeDerivedBranchKey_: Wrappers.Result
        out147_: Wrappers.Result
        out147_ = (cryptoPrimitives).KdfCounterMode(AwsCryptographyPrimitivesTypes.KdfCtrInput_KdfCtrInput(AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__256(), branchKey, default__.DERIVED__BRANCH__KEY__EXPECTED__LENGTH, purpose, Wrappers.Option_Some(salt)))
        d_812_maybeDerivedBranchKey_ = out147_
        d_813_derivedBranchKey_: _dafny.Seq
        d_814_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda66_(d_815_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_815_e_)

        d_814_valueOrError0_ = (d_812_maybeDerivedBranchKey_).MapFailure(lambda66_)
        if (d_814_valueOrError0_).IsFailure():
            output = (d_814_valueOrError0_).PropagateFailure()
            return output
        d_813_derivedBranchKey_ = (d_814_valueOrError0_).Extract()
        output = Wrappers.Result_Success(d_813_derivedBranchKey_)
        return output

    @staticmethod
    def WrappingAad(branchKeyId, branchKeyVersion, aad):
        return (((Constants.default__.PROVIDER__ID__HIERARCHY) + (branchKeyId)) + (branchKeyVersion)) + (aad)

    @staticmethod
    def SerializeEDKCiphertext(encOutput):
        return ((encOutput).cipherText) + ((encOutput).authTag)

    @staticmethod
    def E(s):
        return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(s)

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
        return AwsCryptographyPrimitivesTypes.AES__GCM_AES__GCM(default__.AES__256__ENC__KEY__LENGTH, default__.AES__256__ENC__TAG__LENGTH, default__.AES__256__ENC__IV__LENGTH)
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

class AwsKmsHierarchicalKeyring(Keyring.VerifiableInterface, AwsCryptographyMaterialProvidersTypes.IKeyring):
    def  __init__(self):
        self._keyStore: AwsCryptographyKeyStoreTypes.IKeyStoreClient = None
        self._cryptoPrimitives: AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient = None
        self._branchKeyIdSupplier: Wrappers.Option = Wrappers.Option.default()()
        self._branchKeyId: Wrappers.Option = Wrappers.Option.default()()
        self._ttlSeconds: int = None
        self._cache: AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsCache = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsHierarchicalKeyring.AwsKmsHierarchicalKeyring"
    def OnDecrypt(self, input):
        out148_: Wrappers.Result
        out148_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnDecrypt(self, input)
        return out148_

    def OnEncrypt(self, input):
        out149_: Wrappers.Result
        out149_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnEncrypt(self, input)
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
            d_816_GetBranchKeyIdOut_: AwsCryptographyMaterialProvidersTypes.GetBranchKeyIdOutput
            d_817_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyMaterialProvidersTypes.GetBranchKeyIdOutput.default())()
            out150_: Wrappers.Result
            out150_ = (((self).branchKeyIdSupplier).value).GetBranchKeyId(AwsCryptographyMaterialProvidersTypes.GetBranchKeyIdInput_GetBranchKeyIdInput(context))
            d_817_valueOrError0_ = out150_
            if (d_817_valueOrError0_).IsFailure():
                ret = (d_817_valueOrError0_).PropagateFailure()
                return ret
            d_816_GetBranchKeyIdOut_ = (d_817_valueOrError0_).Extract()
            ret = Wrappers.Result_Success((d_816_GetBranchKeyIdOut_).branchKeyId)
            return ret
        return ret

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        d_818_materials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_818_materials_ = (input).materials
        d_819_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_819_suite_ = (d_818_materials_).algorithmSuite
        d_820_branchKeyIdForEncrypt_: _dafny.Seq
        d_821_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out151_: Wrappers.Result
        out151_ = (self).GetBranchKeyId((d_818_materials_).encryptionContext)
        d_821_valueOrError0_ = out151_
        if (d_821_valueOrError0_).IsFailure():
            res = (d_821_valueOrError0_).PropagateFailure()
            return res
        d_820_branchKeyIdForEncrypt_ = (d_821_valueOrError0_).Extract()
        d_822_branchKeyIdUtf8_: _dafny.Seq
        d_823_valueOrError1_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_823_valueOrError1_ = (UTF8.default__.Encode(d_820_branchKeyIdForEncrypt_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_823_valueOrError1_).IsFailure():
            res = (d_823_valueOrError1_).PropagateFailure()
            return res
        d_822_branchKeyIdUtf8_ = (d_823_valueOrError1_).Extract()
        d_824_cacheId_: _dafny.Seq
        d_825_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out152_: Wrappers.Result
        out152_ = (self).GetActiveCacheId(d_820_branchKeyIdForEncrypt_, d_822_branchKeyIdUtf8_, (self).cryptoPrimitives)
        d_825_valueOrError2_ = out152_
        if (d_825_valueOrError2_).IsFailure():
            res = (d_825_valueOrError2_).PropagateFailure()
            return res
        d_824_cacheId_ = (d_825_valueOrError2_).Extract()
        d_826_hierarchicalMaterials_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
        d_827_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.BranchKeyMaterials.default())()
        out153_: Wrappers.Result
        out153_ = (self).GetActiveHierarchicalMaterials(d_820_branchKeyIdForEncrypt_, d_824_cacheId_, (self).keyStore)
        d_827_valueOrError3_ = out153_
        if (d_827_valueOrError3_).IsFailure():
            res = (d_827_valueOrError3_).PropagateFailure()
            return res
        d_826_hierarchicalMaterials_ = (d_827_valueOrError3_).Extract()
        d_828_branchKey_: _dafny.Seq
        d_828_branchKey_ = (d_826_hierarchicalMaterials_).branchKey
        d_829_branchKeyVersion_: _dafny.Seq
        d_829_branchKeyVersion_ = (d_826_hierarchicalMaterials_).branchKeyVersion
        d_830_branchKeyVersionAsString_: _dafny.Seq
        d_831_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_831_valueOrError4_ = (UTF8.default__.Decode(d_829_branchKeyVersion_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_831_valueOrError4_).IsFailure():
            res = (d_831_valueOrError4_).PropagateFailure()
            return res
        d_830_branchKeyVersionAsString_ = (d_831_valueOrError4_).Extract()
        d_832_branchKeyVersionAsBytes_: _dafny.Seq
        d_833_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_833_valueOrError5_ = (UUID.default__.ToByteArray(d_830_branchKeyVersionAsString_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_833_valueOrError5_).IsFailure():
            res = (d_833_valueOrError5_).PropagateFailure()
            return res
        d_832_branchKeyVersionAsBytes_ = (d_833_valueOrError5_).Extract()
        d_834_kmsHierarchyGenerateAndWrap_: KmsHierarchyGenerateAndWrapKeyMaterial
        nw33_ = KmsHierarchyGenerateAndWrapKeyMaterial()
        nw33_.ctor__((d_826_hierarchicalMaterials_).branchKey, d_822_branchKeyIdUtf8_, d_832_branchKeyVersionAsBytes_, (self).cryptoPrimitives)
        d_834_kmsHierarchyGenerateAndWrap_ = nw33_
        d_835_kmsHierarchyWrap_: KmsHierarchyWrapKeyMaterial
        nw34_ = KmsHierarchyWrapKeyMaterial()
        nw34_.ctor__((d_826_hierarchicalMaterials_).branchKey, d_822_branchKeyIdUtf8_, d_832_branchKeyVersionAsBytes_, (self).cryptoPrimitives)
        d_835_kmsHierarchyWrap_ = nw34_
        d_836_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_837_valueOrError6_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.WrapEdkMaterialOutput.default(HierarchyWrapInfo.default()))()
        out154_: Wrappers.Result
        out154_ = EdkWrapping.default__.WrapEdkMaterial(d_818_materials_, d_835_kmsHierarchyWrap_, d_834_kmsHierarchyGenerateAndWrap_)
        d_837_valueOrError6_ = out154_
        if (d_837_valueOrError6_).IsFailure():
            res = (d_837_valueOrError6_).PropagateFailure()
            return res
        d_836_wrapOutput_ = (d_837_valueOrError6_).Extract()
        d_838_symmetricSigningKeyList_: Wrappers.Option
        d_838_symmetricSigningKeyList_ = (Wrappers.Option_Some(_dafny.Seq([((d_836_wrapOutput_).symmetricSigningKey).value])) if ((d_836_wrapOutput_).symmetricSigningKey).is_Some else Wrappers.Option_None())
        d_839_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_839_edk_ = AwsCryptographyMaterialProvidersTypes.EncryptedDataKey_EncryptedDataKey(Constants.default__.PROVIDER__ID__HIERARCHY, d_822_branchKeyIdUtf8_, (d_836_wrapOutput_).wrappedMaterial)
        if (d_836_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_840_result_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_841_valueOrError7_: Wrappers.Result = None
            d_841_valueOrError7_ = Materials.default__.EncryptionMaterialAddDataKey(d_818_materials_, (d_836_wrapOutput_).plaintextDataKey, _dafny.Seq([d_839_edk_]), d_838_symmetricSigningKeyList_)
            if (d_841_valueOrError7_).IsFailure():
                res = (d_841_valueOrError7_).PropagateFailure()
                return res
            d_840_result_ = (d_841_valueOrError7_).Extract()
            res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(d_840_result_))
            return res
        elif (d_836_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_842_result_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_843_valueOrError8_: Wrappers.Result = None
            d_843_valueOrError8_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys(d_818_materials_, _dafny.Seq([d_839_edk_]), d_838_symmetricSigningKeyList_)
            if (d_843_valueOrError8_).IsFailure():
                res = (d_843_valueOrError8_).PropagateFailure()
                return res
            d_842_result_ = (d_843_valueOrError8_).Extract()
            res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(d_842_result_))
            return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_844_materials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_844_materials_ = (input).materials
        d_845_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_845_suite_ = ((input).materials).algorithmSuite
        d_846_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_846_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_844_materials_), default__.E(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_846_valueOrError0_).IsFailure():
            res = (d_846_valueOrError0_).PropagateFailure()
            return res
        d_847_branchKeyIdForDecrypt_: _dafny.Seq
        d_848_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out155_: Wrappers.Result
        out155_ = (self).GetBranchKeyId((d_844_materials_).encryptionContext)
        d_848_valueOrError1_ = out155_
        if (d_848_valueOrError1_).IsFailure():
            res = (d_848_valueOrError1_).PropagateFailure()
            return res
        d_847_branchKeyIdForDecrypt_ = (d_848_valueOrError1_).Extract()
        d_849_filter_: OnDecryptHierarchyEncryptedDataKeyFilter
        nw35_ = OnDecryptHierarchyEncryptedDataKeyFilter()
        nw35_.ctor__(d_847_branchKeyIdForDecrypt_)
        d_849_filter_ = nw35_
        d_850_edksToAttempt_: _dafny.Seq
        d_851_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out156_: Wrappers.Result
        out156_ = Actions.default__.FilterWithResult(d_849_filter_, (input).encryptedDataKeys)
        d_851_valueOrError2_ = out156_
        if (d_851_valueOrError2_).IsFailure():
            res = (d_851_valueOrError2_).PropagateFailure()
            return res
        d_850_edksToAttempt_ = (d_851_valueOrError2_).Extract()
        d_852_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_852_valueOrError3_ = Wrappers.default__.Need((0) < (len(d_850_edksToAttempt_)), default__.E(_dafny.Seq("Unable to decrypt data key: No Encrypted Data Keys found to match.")))
        if (d_852_valueOrError3_).IsFailure():
            res = (d_852_valueOrError3_).PropagateFailure()
            return res
        d_853_decryptClosure_: Actions.ActionWithResult
        nw36_ = DecryptSingleEncryptedDataKey()
        nw36_.ctor__(d_844_materials_, (self).keyStore, (self).cryptoPrimitives, d_847_branchKeyIdForDecrypt_, (self).ttlSeconds, (self).cache)
        d_853_decryptClosure_ = nw36_
        d_854_outcome_: Wrappers.Result
        out157_: Wrappers.Result
        out157_ = Actions.default__.ReduceToSuccess(d_853_decryptClosure_, d_850_edksToAttempt_)
        d_854_outcome_ = out157_
        d_855_SealedDecryptionMaterials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_856_valueOrError4_: Wrappers.Result = None
        def lambda67_(d_857_errors_):
            return AwsCryptographyMaterialProvidersTypes.Error_CollectionOfErrors(d_857_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."))

        d_856_valueOrError4_ = (d_854_outcome_).MapFailure(lambda67_)
        if (d_856_valueOrError4_).IsFailure():
            res = (d_856_valueOrError4_).PropagateFailure()
            return res
        d_855_SealedDecryptionMaterials_ = (d_856_valueOrError4_).Extract()
        res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnDecryptOutput_OnDecryptOutput(d_855_SealedDecryptionMaterials_))
        return res
        return res

    def GetActiveCacheId(self, branchKeyId, branchKeyIdUtf8, cryptoPrimitives):
        cacheId: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_858_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        def iife24_(_pat_let7_0):
            def iife25_(d_859_branchKeyId_):
                return (True) and (((0) <= (len(d_859_branchKeyId_))) and ((len(d_859_branchKeyId_)) < (StandardLibrary_UInt.default__.UINT32__LIMIT)))
            return iife25_(_pat_let7_0)
        d_858_valueOrError0_ = Wrappers.default__.Need((((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).is_Success) and (iife24_(((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).value)), default__.E(_dafny.Seq("Invalid Branch Key ID Length")))
        if (d_858_valueOrError0_).IsFailure():
            cacheId = (d_858_valueOrError0_).PropagateFailure()
            return cacheId
        d_860_branchKeyId_: _dafny.Seq
        d_860_branchKeyId_ = (UTF8.default__.Decode(branchKeyIdUtf8)).value
        d_861_lenBranchKey_: _dafny.Seq
        d_861_lenBranchKey_ = StandardLibrary_UInt.default__.UInt32ToSeq(len(d_860_branchKeyId_))
        d_862_hashAlgorithm_: AwsCryptographyPrimitivesTypes.DigestAlgorithm
        d_862_hashAlgorithm_ = AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__512()
        d_863_maybeBranchKeyDigest_: Wrappers.Result
        out158_: Wrappers.Result
        out158_ = (cryptoPrimitives).Digest(AwsCryptographyPrimitivesTypes.DigestInput_DigestInput(d_862_hashAlgorithm_, branchKeyIdUtf8))
        d_863_maybeBranchKeyDigest_ = out158_
        d_864_branchKeyDigest_: _dafny.Seq
        d_865_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda68_(d_866_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_866_e_)

        d_865_valueOrError1_ = (d_863_maybeBranchKeyDigest_).MapFailure(lambda68_)
        if (d_865_valueOrError1_).IsFailure():
            cacheId = (d_865_valueOrError1_).PropagateFailure()
            return cacheId
        d_864_branchKeyDigest_ = (d_865_valueOrError1_).Extract()
        d_867_activeUtf8_: _dafny.Seq
        d_868_valueOrError2_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_868_valueOrError2_ = (UTF8.default__.Encode(default__.EXPRESSION__ATTRIBUTE__VALUE__STATUS__VALUE)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_868_valueOrError2_).IsFailure():
            cacheId = (d_868_valueOrError2_).PropagateFailure()
            return cacheId
        d_867_activeUtf8_ = (d_868_valueOrError2_).Extract()
        d_869_identifier_: _dafny.Seq
        d_869_identifier_ = (((d_861_lenBranchKey_) + (d_864_branchKeyDigest_)) + (_dafny.Seq([0]))) + (d_867_activeUtf8_)
        d_870_maybeCacheIdDigest_: Wrappers.Result
        out159_: Wrappers.Result
        out159_ = (cryptoPrimitives).Digest(AwsCryptographyPrimitivesTypes.DigestInput_DigestInput(d_862_hashAlgorithm_, d_869_identifier_))
        d_870_maybeCacheIdDigest_ = out159_
        d_871_cacheDigest_: _dafny.Seq
        d_872_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda69_(d_873_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_873_e_)

        d_872_valueOrError3_ = (d_870_maybeCacheIdDigest_).MapFailure(lambda69_)
        if (d_872_valueOrError3_).IsFailure():
            cacheId = (d_872_valueOrError3_).PropagateFailure()
            return cacheId
        d_871_cacheDigest_ = (d_872_valueOrError3_).Extract()
        d_874_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_874_valueOrError4_ = Wrappers.default__.Need((len(d_871_cacheDigest_)) == (Digest.default__.Length(d_862_hashAlgorithm_)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Digest generated a message not equal to the expected length.")))
        if (d_874_valueOrError4_).IsFailure():
            cacheId = (d_874_valueOrError4_).PropagateFailure()
            return cacheId
        cacheId = Wrappers.Result_Success(_dafny.Seq((d_871_cacheDigest_)[0:32:]))
        return cacheId
        return cacheId

    def GetActiveHierarchicalMaterials(self, branchKeyId, cacheId, keyStore):
        material: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.BranchKeyMaterials.default())()
        d_875_getCacheInput_: AwsCryptographyMaterialProvidersTypes.GetCacheEntryInput
        d_875_getCacheInput_ = AwsCryptographyMaterialProvidersTypes.GetCacheEntryInput_GetCacheEntryInput(cacheId, Wrappers.Option_None())
        d_876_getCacheOutput_: Wrappers.Result
        out160_: Wrappers.Result
        out160_ = default__.getEntry((self).cache, d_875_getCacheInput_)
        d_876_getCacheOutput_ = out160_
        if (d_876_getCacheOutput_).is_Failure:
            d_877_maybeGetActiveBranchKeyOutput_: Wrappers.Result
            out161_: Wrappers.Result
            out161_ = (keyStore).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(branchKeyId))
            d_877_maybeGetActiveBranchKeyOutput_ = out161_
            d_878_getActiveBranchKeyOutput_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
            d_879_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
            def lambda70_(d_880_e_):
                return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyKeyStore(d_880_e_)

            d_879_valueOrError0_ = (d_877_maybeGetActiveBranchKeyOutput_).MapFailure(lambda70_)
            if (d_879_valueOrError0_).IsFailure():
                material = (d_879_valueOrError0_).PropagateFailure()
                return material
            d_878_getActiveBranchKeyOutput_ = (d_879_valueOrError0_).Extract()
            d_881_branchKeyMaterials_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
            d_881_branchKeyMaterials_ = (d_878_getActiveBranchKeyOutput_).branchKeyMaterials
            d_882_now_: int
            out162_: int
            out162_ = Time.default__.CurrentRelativeTime()
            d_882_now_ = out162_
            d_883_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_883_valueOrError1_ = Wrappers.default__.Need(((d_882_now_) + ((self).ttlSeconds)) < (StandardLibrary_UInt.default__.INT64__MAX__LIMIT), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("INT64 Overflow when putting cache entry.")))
            if (d_883_valueOrError1_).IsFailure():
                material = (d_883_valueOrError1_).PropagateFailure()
                return material
            d_884_putCacheEntryInput_: AwsCryptographyMaterialProvidersTypes.PutCacheEntryInput
            d_884_putCacheEntryInput_ = AwsCryptographyMaterialProvidersTypes.PutCacheEntryInput_PutCacheEntryInput(cacheId, AwsCryptographyMaterialProvidersTypes.Materials_BranchKey(d_881_branchKeyMaterials_), d_882_now_, ((self).ttlSeconds) + (d_882_now_), Wrappers.Option_None(), Wrappers.Option_None())
            d_885___v0_: tuple
            d_886_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            out163_: Wrappers.Result
            out163_ = default__.putEntry((self).cache, d_884_putCacheEntryInput_)
            d_886_valueOrError2_ = out163_
            if (d_886_valueOrError2_).IsFailure():
                material = (d_886_valueOrError2_).PropagateFailure()
                return material
            d_885___v0_ = (d_886_valueOrError2_).Extract()
            material = Wrappers.Result_Success(d_881_branchKeyMaterials_)
            return material
        elif True:
            d_887_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_887_valueOrError3_ = Wrappers.default__.Need(((((d_876_getCacheOutput_).value).materials).is_BranchKey) and ((((d_876_getCacheOutput_).value).materials) == (AwsCryptographyMaterialProvidersTypes.Materials_BranchKey((((d_876_getCacheOutput_).value).materials).BranchKey))), default__.E(_dafny.Seq("Invalid Material Type.")))
            if (d_887_valueOrError3_).IsFailure():
                material = (d_887_valueOrError3_).PropagateFailure()
                return material
            material = Wrappers.Result_Success((((d_876_getCacheOutput_).value).materials).BranchKey)
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
        self._branchKeyId: _dafny.Seq = _dafny.Seq("")
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsHierarchicalKeyring.OnDecryptHierarchyEncryptedDataKeyFilter"
    def ctor__(self, branchKeyId):
        (self)._branchKeyId = branchKeyId

    def Invoke(self, edk):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        d_888_providerInfo_: _dafny.Seq
        d_888_providerInfo_ = (edk).keyProviderInfo
        d_889_providerId_: _dafny.Seq
        d_889_providerId_ = (edk).keyProviderId
        if (d_889_providerId_) != (Constants.default__.PROVIDER__ID__HIERARCHY):
            res = Wrappers.Result_Success(False)
            return res
        if not(UTF8.default__.ValidUTF8Seq(d_888_providerInfo_)):
            res = Wrappers.Result_Failure(default__.E(_dafny.Seq("Invalid encoding, provider info is not UTF8.")))
            return res
        d_890_branchKeyId_: _dafny.Seq
        d_891_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_891_valueOrError0_ = (UTF8.default__.Decode(d_888_providerInfo_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_891_valueOrError0_).IsFailure():
            res = (d_891_valueOrError0_).PropagateFailure()
            return res
        d_890_branchKeyId_ = (d_891_valueOrError0_).Extract()
        res = Wrappers.Result_Success(((self).branchKeyId) == (d_890_branchKeyId_))
        return res
        return res

    @property
    def branchKeyId(self):
        return self._branchKeyId

class DecryptSingleEncryptedDataKey(Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._materials: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials = None
        self._keyStore: AwsCryptographyKeyStoreTypes.IKeyStoreClient = None
        self._cryptoPrimitives: AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient = None
        self._branchKeyId: _dafny.Seq = _dafny.Seq("")
        self._ttlSeconds: int = None
        self._cache: AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsCache = None
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
        d_892_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_892_valueOrError0_ = Wrappers.default__.Need(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received invalid EDK provider info for Hierarchical Keyring")))
        if (d_892_valueOrError0_).IsFailure():
            res = (d_892_valueOrError0_).PropagateFailure()
            return res
        d_893_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_893_suite_ = ((self).materials).algorithmSuite
        d_894_keyProviderId_: _dafny.Seq
        d_894_keyProviderId_ = (edk).keyProviderId
        d_895_branchKeyIdUtf8_: _dafny.Seq
        d_895_branchKeyIdUtf8_ = (edk).keyProviderInfo
        d_896_ciphertext_: _dafny.Seq
        d_896_ciphertext_ = (edk).ciphertext
        d_897_providerWrappedMaterial_: _dafny.Seq
        d_898_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_898_valueOrError1_ = EdkWrapping.default__.GetProviderWrappedMaterial(d_896_ciphertext_, d_893_suite_)
        if (d_898_valueOrError1_).IsFailure():
            res = (d_898_valueOrError1_).PropagateFailure()
            return res
        d_897_providerWrappedMaterial_ = (d_898_valueOrError1_).Extract()
        d_899_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_899_valueOrError2_ = Wrappers.default__.Need((len(d_897_providerWrappedMaterial_)) >= (default__.EDK__CIPHERTEXT__VERSION__INDEX), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received EDK Ciphertext of incorrect length.")))
        if (d_899_valueOrError2_).IsFailure():
            res = (d_899_valueOrError2_).PropagateFailure()
            return res
        d_900_branchKeyVersionUuid_: _dafny.Seq
        d_900_branchKeyVersionUuid_ = _dafny.Seq((d_897_providerWrappedMaterial_)[default__.EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX:default__.EDK__CIPHERTEXT__VERSION__INDEX:])
        d_901_version_: _dafny.Seq
        d_902_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_902_valueOrError3_ = (UUID.default__.FromByteArray(d_900_branchKeyVersionUuid_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_902_valueOrError3_).IsFailure():
            res = (d_902_valueOrError3_).PropagateFailure()
            return res
        d_901_version_ = (d_902_valueOrError3_).Extract()
        d_903_cacheId_: _dafny.Seq
        d_904_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out164_: Wrappers.Result
        out164_ = (self).GetVersionCacheId(d_895_branchKeyIdUtf8_, d_901_version_, (self).cryptoPrimitives)
        d_904_valueOrError4_ = out164_
        if (d_904_valueOrError4_).IsFailure():
            res = (d_904_valueOrError4_).PropagateFailure()
            return res
        d_903_cacheId_ = (d_904_valueOrError4_).Extract()
        d_905_hierarchicalMaterials_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
        d_906_valueOrError5_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.BranchKeyMaterials.default())()
        out165_: Wrappers.Result
        out165_ = (self).GetHierarchicalMaterialsVersion((self).branchKeyId, d_895_branchKeyIdUtf8_, d_901_version_, d_903_cacheId_)
        d_906_valueOrError5_ = out165_
        if (d_906_valueOrError5_).IsFailure():
            res = (d_906_valueOrError5_).PropagateFailure()
            return res
        d_905_hierarchicalMaterials_ = (d_906_valueOrError5_).Extract()
        d_907_branchKey_: _dafny.Seq
        d_907_branchKey_ = (d_905_hierarchicalMaterials_).branchKey
        d_908_branchKeyVersion_: _dafny.Seq
        d_908_branchKeyVersion_ = (d_905_hierarchicalMaterials_).branchKeyVersion
        d_909_branchKeyVersionAsString_: _dafny.Seq
        d_910_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_910_valueOrError6_ = (UTF8.default__.Decode(d_908_branchKeyVersion_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_910_valueOrError6_).IsFailure():
            res = (d_910_valueOrError6_).PropagateFailure()
            return res
        d_909_branchKeyVersionAsString_ = (d_910_valueOrError6_).Extract()
        d_911_branchKeyVersionAsBytes_: _dafny.Seq
        d_912_valueOrError7_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_912_valueOrError7_ = (UUID.default__.ToByteArray(d_909_branchKeyVersionAsString_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_912_valueOrError7_).IsFailure():
            res = (d_912_valueOrError7_).PropagateFailure()
            return res
        d_911_branchKeyVersionAsBytes_ = (d_912_valueOrError7_).Extract()
        d_913_maybeCrypto_: Wrappers.Result
        out166_: Wrappers.Result
        out166_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_913_maybeCrypto_ = out166_
        d_914_cryptoPrimitivesX_: AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient
        d_915_valueOrError8_: Wrappers.Result = None
        def lambda71_(d_916_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_916_e_)

        d_915_valueOrError8_ = (d_913_maybeCrypto_).MapFailure(lambda71_)
        if (d_915_valueOrError8_).IsFailure():
            res = (d_915_valueOrError8_).PropagateFailure()
            return res
        d_914_cryptoPrimitivesX_ = (d_915_valueOrError8_).Extract()
        d_917_cryptoPrimitives_: AtomicPrimitives.AtomicPrimitivesClient
        d_917_cryptoPrimitives_ = d_914_cryptoPrimitivesX_
        d_918_kmsHierarchyUnwrap_: KmsHierarchyUnwrapKeyMaterial
        nw37_ = KmsHierarchyUnwrapKeyMaterial()
        nw37_.ctor__(d_907_branchKey_, d_895_branchKeyIdUtf8_, d_911_branchKeyVersionAsBytes_, d_917_cryptoPrimitives_)
        d_918_kmsHierarchyUnwrap_ = nw37_
        d_919_unwrapOutputRes_: Wrappers.Result
        out167_: Wrappers.Result
        out167_ = EdkWrapping.default__.UnwrapEdkMaterial((edk).ciphertext, (self).materials, d_918_kmsHierarchyUnwrap_)
        d_919_unwrapOutputRes_ = out167_
        d_920_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_921_valueOrError9_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.UnwrapEdkMaterialOutput.default(HierarchyUnwrapInfo.default()))()
        d_921_valueOrError9_ = d_919_unwrapOutputRes_
        if (d_921_valueOrError9_).IsFailure():
            res = (d_921_valueOrError9_).PropagateFailure()
            return res
        d_920_unwrapOutput_ = (d_921_valueOrError9_).Extract()
        d_922_result_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_923_valueOrError10_: Wrappers.Result = None
        d_923_valueOrError10_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_920_unwrapOutput_).plaintextDataKey, (d_920_unwrapOutput_).symmetricSigningKey)
        if (d_923_valueOrError10_).IsFailure():
            res = (d_923_valueOrError10_).PropagateFailure()
            return res
        d_922_result_ = (d_923_valueOrError10_).Extract()
        res = Wrappers.Result_Success(d_922_result_)
        return res
        return res

    def GetVersionCacheId(self, branchKeyIdUtf8, branchKeyVersion, cryptoPrimitives):
        cacheId: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_924_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        def iife26_(_pat_let8_0):
            def iife27_(d_925_branchKeyId_):
                return (True) and (((0) <= (len(d_925_branchKeyId_))) and ((len(d_925_branchKeyId_)) < (StandardLibrary_UInt.default__.UINT32__LIMIT)))
            return iife27_(_pat_let8_0)
        d_924_valueOrError0_ = Wrappers.default__.Need((((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).is_Success) and (iife26_(((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).value)), default__.E(_dafny.Seq("Invalid Branch Key ID Length")))
        if (d_924_valueOrError0_).IsFailure():
            cacheId = (d_924_valueOrError0_).PropagateFailure()
            return cacheId
        d_926_branchKeyId_: _dafny.Seq
        d_926_branchKeyId_ = (UTF8.default__.Decode(branchKeyIdUtf8)).value
        d_927_lenBranchKey_: _dafny.Seq
        d_927_lenBranchKey_ = StandardLibrary_UInt.default__.UInt32ToSeq(len(d_926_branchKeyId_))
        d_928_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_928_valueOrError1_ = Wrappers.default__.Need(UTF8.default__.IsASCIIString(branchKeyVersion), default__.E(_dafny.Seq("Unable to represent as an ASCII string.")))
        if (d_928_valueOrError1_).IsFailure():
            cacheId = (d_928_valueOrError1_).PropagateFailure()
            return cacheId
        d_929_versionBytes_: _dafny.Seq
        d_929_versionBytes_ = UTF8.default__.EncodeAscii(branchKeyVersion)
        d_930_identifier_: _dafny.Seq
        d_930_identifier_ = (((d_927_lenBranchKey_) + (branchKeyIdUtf8)) + (_dafny.Seq([0]))) + (d_929_versionBytes_)
        d_931_identifierDigestInput_: AwsCryptographyPrimitivesTypes.DigestInput
        d_931_identifierDigestInput_ = AwsCryptographyPrimitivesTypes.DigestInput_DigestInput(AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__512(), d_930_identifier_)
        d_932_maybeCacheDigest_: Wrappers.Result
        out168_: Wrappers.Result
        out168_ = Digest.default__.Digest(d_931_identifierDigestInput_)
        d_932_maybeCacheDigest_ = out168_
        d_933_cacheDigest_: _dafny.Seq
        d_934_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda72_(d_935_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_935_e_)

        d_934_valueOrError2_ = (d_932_maybeCacheDigest_).MapFailure(lambda72_)
        if (d_934_valueOrError2_).IsFailure():
            cacheId = (d_934_valueOrError2_).PropagateFailure()
            return cacheId
        d_933_cacheDigest_ = (d_934_valueOrError2_).Extract()
        cacheId = Wrappers.Result_Success(_dafny.Seq((d_933_cacheDigest_)[0:32:]))
        return cacheId
        return cacheId

    def GetHierarchicalMaterialsVersion(self, branchKeyId, branchKeyIdUtf8, version, cacheId):
        material: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.BranchKeyMaterials.default())()
        d_936_getCacheInput_: AwsCryptographyMaterialProvidersTypes.GetCacheEntryInput
        d_936_getCacheInput_ = AwsCryptographyMaterialProvidersTypes.GetCacheEntryInput_GetCacheEntryInput(cacheId, Wrappers.Option_None())
        d_937_getCacheOutput_: Wrappers.Result
        out169_: Wrappers.Result
        out169_ = default__.getEntry((self).cache, d_936_getCacheInput_)
        d_937_getCacheOutput_ = out169_
        if (d_937_getCacheOutput_).is_Failure:
            d_938_maybeGetBranchKeyVersionOutput_: Wrappers.Result
            out170_: Wrappers.Result
            out170_ = ((self).keyStore).GetBranchKeyVersion(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput_GetBranchKeyVersionInput(branchKeyId, version))
            d_938_maybeGetBranchKeyVersionOutput_ = out170_
            d_939_getBranchKeyVersionOutput_: AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
            d_940_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
            def lambda73_(d_941_e_):
                return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyKeyStore(d_941_e_)

            d_940_valueOrError0_ = (d_938_maybeGetBranchKeyVersionOutput_).MapFailure(lambda73_)
            if (d_940_valueOrError0_).IsFailure():
                material = (d_940_valueOrError0_).PropagateFailure()
                return material
            d_939_getBranchKeyVersionOutput_ = (d_940_valueOrError0_).Extract()
            d_942_branchKeyMaterials_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
            d_942_branchKeyMaterials_ = (d_939_getBranchKeyVersionOutput_).branchKeyMaterials
            d_943_now_: int
            out171_: int
            out171_ = Time.default__.CurrentRelativeTime()
            d_943_now_ = out171_
            d_944_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_944_valueOrError1_ = Wrappers.default__.Need(((d_943_now_) + ((self).ttlSeconds)) < (StandardLibrary_UInt.default__.INT64__MAX__LIMIT), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("INT64 Overflow when putting cache entry.")))
            if (d_944_valueOrError1_).IsFailure():
                material = (d_944_valueOrError1_).PropagateFailure()
                return material
            d_945_putCacheEntryInput_: AwsCryptographyMaterialProvidersTypes.PutCacheEntryInput
            d_945_putCacheEntryInput_ = AwsCryptographyMaterialProvidersTypes.PutCacheEntryInput_PutCacheEntryInput(cacheId, AwsCryptographyMaterialProvidersTypes.Materials_BranchKey(d_942_branchKeyMaterials_), d_943_now_, ((self).ttlSeconds) + (d_943_now_), Wrappers.Option_None(), Wrappers.Option_None())
            d_946___v1_: tuple
            d_947_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            out172_: Wrappers.Result
            out172_ = default__.putEntry((self).cache, d_945_putCacheEntryInput_)
            d_947_valueOrError2_ = out172_
            if (d_947_valueOrError2_).IsFailure():
                material = (d_947_valueOrError2_).PropagateFailure()
                return material
            d_946___v1_ = (d_947_valueOrError2_).Extract()
            material = Wrappers.Result_Success(d_942_branchKeyMaterials_)
            return material
        elif True:
            d_948_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_948_valueOrError3_ = Wrappers.default__.Need(((((d_937_getCacheOutput_).value).materials).is_BranchKey) and ((((d_937_getCacheOutput_).value).materials) == (AwsCryptographyMaterialProvidersTypes.Materials_BranchKey((((d_937_getCacheOutput_).value).materials).BranchKey))), default__.E(_dafny.Seq("Invalid Material Type.")))
            if (d_948_valueOrError3_).IsFailure():
                material = (d_948_valueOrError3_).PropagateFailure()
                return material
            material = Wrappers.Result_Success((((d_937_getCacheOutput_).value).materials).BranchKey)
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
        self._crypto: AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient = None
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
        d_949_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_949_suite_ = (input).algorithmSuite
        d_950_wrappedMaterial_: _dafny.Seq
        d_950_wrappedMaterial_ = (input).wrappedMaterial
        d_951_aad_: _dafny.Map
        d_951_aad_ = (input).encryptionContext
        d_952_KeyLength_: int
        d_952_KeyLength_ = AlgorithmSuites.default__.GetEncryptKeyLength(d_949_suite_)
        d_953_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_953_valueOrError0_ = Wrappers.default__.Need((len(d_950_wrappedMaterial_)) == ((default__.EXPECTED__EDK__CIPHERTEXT__OVERHEAD) + (d_952_KeyLength_)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received EDK Ciphertext of incorrect length2.")))
        if (d_953_valueOrError0_).IsFailure():
            res = (d_953_valueOrError0_).PropagateFailure()
            return res
        d_954_salt_: _dafny.Seq
        d_954_salt_ = _dafny.Seq((d_950_wrappedMaterial_)[0:default__.H__WRAP__SALT__LEN:])
        d_955_iv_: _dafny.Seq
        d_955_iv_ = _dafny.Seq((d_950_wrappedMaterial_)[default__.H__WRAP__SALT__LEN:default__.EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX:])
        d_956_branchKeyVersionUuid_: _dafny.Seq
        d_956_branchKeyVersionUuid_ = _dafny.Seq((d_950_wrappedMaterial_)[default__.EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX:default__.EDK__CIPHERTEXT__VERSION__INDEX:])
        d_957_wrappedKey_: _dafny.Seq
        d_957_wrappedKey_ = _dafny.Seq((d_950_wrappedMaterial_)[default__.EDK__CIPHERTEXT__VERSION__INDEX:(default__.EDK__CIPHERTEXT__VERSION__INDEX) + (d_952_KeyLength_):])
        d_958_authTag_: _dafny.Seq
        d_958_authTag_ = _dafny.Seq((d_950_wrappedMaterial_)[(default__.EDK__CIPHERTEXT__VERSION__INDEX) + (d_952_KeyLength_)::])
        d_959_serializedEC_: _dafny.Seq
        d_960_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_960_valueOrError1_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_960_valueOrError1_).IsFailure():
            res = (d_960_valueOrError1_).PropagateFailure()
            return res
        d_959_serializedEC_ = (d_960_valueOrError1_).Extract()
        d_961_wrappingAad_: _dafny.Seq
        d_961_wrappingAad_ = default__.WrappingAad((self).branchKeyIdUtf8, (self).branchKeyVersionAsBytes, d_959_serializedEC_)
        d_962_derivedBranchKey_: _dafny.Seq
        d_963_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out173_: Wrappers.Result
        out173_ = default__.DeriveEncryptionKeyFromBranchKey((self).branchKey, d_954_salt_, Wrappers.Option_Some(Constants.default__.PROVIDER__ID__HIERARCHY), (self).crypto)
        d_963_valueOrError2_ = out173_
        if (d_963_valueOrError2_).IsFailure():
            res = (d_963_valueOrError2_).PropagateFailure()
            return res
        d_962_derivedBranchKey_ = (d_963_valueOrError2_).Extract()
        d_964_maybeUnwrappedPdk_: Wrappers.Result
        out174_: Wrappers.Result
        out174_ = ((self).crypto).AESDecrypt(AwsCryptographyPrimitivesTypes.AESDecryptInput_AESDecryptInput(default__.AES__256__ENC__ALG, d_962_derivedBranchKey_, d_957_wrappedKey_, d_958_authTag_, d_955_iv_, d_961_wrappingAad_))
        d_964_maybeUnwrappedPdk_ = out174_
        d_965_unwrappedPdk_: _dafny.Seq
        d_966_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda74_(d_967_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_967_e_)

        d_966_valueOrError3_ = (d_964_maybeUnwrappedPdk_).MapFailure(lambda74_)
        if (d_966_valueOrError3_).IsFailure():
            res = (d_966_valueOrError3_).PropagateFailure()
            return res
        d_965_unwrappedPdk_ = (d_966_valueOrError3_).Extract()
        d_968_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_968_valueOrError4_ = Wrappers.default__.Need((len(d_965_unwrappedPdk_)) == (AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)), default__.E(_dafny.Seq("Invalid Key Length")))
        if (d_968_valueOrError4_).IsFailure():
            res = (d_968_valueOrError4_).PropagateFailure()
            return res
        d_969_output_: MaterialWrapping.UnwrapOutput
        d_969_output_ = MaterialWrapping.UnwrapOutput_UnwrapOutput(d_965_unwrappedPdk_, HierarchyUnwrapInfo_HierarchyUnwrapInfo())
        res = Wrappers.Result_Success(d_969_output_)
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
        self._crypto: AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient = None
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
        d_970_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_970_suite_ = (input).algorithmSuite
        d_971_pdkResult_: Wrappers.Result
        out175_: Wrappers.Result
        out175_ = ((self).crypto).GenerateRandomBytes(AwsCryptographyPrimitivesTypes.GenerateRandomBytesInput_GenerateRandomBytesInput(AlgorithmSuites.default__.GetEncryptKeyLength(d_970_suite_)))
        d_971_pdkResult_ = out175_
        d_972_pdk_: _dafny.Seq
        d_973_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda75_(d_974_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_974_e_)

        d_973_valueOrError0_ = (d_971_pdkResult_).MapFailure(lambda75_)
        if (d_973_valueOrError0_).IsFailure():
            res = (d_973_valueOrError0_).PropagateFailure()
            return res
        d_972_pdk_ = (d_973_valueOrError0_).Extract()
        d_975_wrap_: KmsHierarchyWrapKeyMaterial
        nw38_ = KmsHierarchyWrapKeyMaterial()
        nw38_.ctor__((self).branchKey, (self).branchKeyIdUtf8, (self).branchKeyVersionAsBytes, (self).crypto)
        d_975_wrap_ = nw38_
        d_976_wrapOutput_: MaterialWrapping.WrapOutput
        d_977_valueOrError1_: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.WrapOutput.default(HierarchyWrapInfo.default()))()
        out176_: Wrappers.Result
        out176_ = (d_975_wrap_).Invoke(MaterialWrapping.WrapInput_WrapInput(d_972_pdk_, (input).algorithmSuite, (input).encryptionContext))
        d_977_valueOrError1_ = out176_
        if (d_977_valueOrError1_).IsFailure():
            res = (d_977_valueOrError1_).PropagateFailure()
            return res
        d_976_wrapOutput_ = (d_977_valueOrError1_).Extract()
        d_978_output_: MaterialWrapping.GenerateAndWrapOutput
        d_978_output_ = MaterialWrapping.GenerateAndWrapOutput_GenerateAndWrapOutput(d_972_pdk_, (d_976_wrapOutput_).wrappedMaterial, HierarchyWrapInfo_HierarchyWrapInfo())
        res = Wrappers.Result_Success(d_978_output_)
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
        self._crypto: AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient = None
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
        d_979_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_979_suite_ = (input).algorithmSuite
        d_980_maybeNonceSalt_: Wrappers.Result
        out177_: Wrappers.Result
        out177_ = ((self).crypto).GenerateRandomBytes(AwsCryptographyPrimitivesTypes.GenerateRandomBytesInput_GenerateRandomBytesInput((default__.H__WRAP__SALT__LEN) + (default__.H__WRAP__NONCE__LEN)))
        d_980_maybeNonceSalt_ = out177_
        d_981_saltAndNonce_: _dafny.Seq
        d_982_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda76_(d_983_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_983_e_)

        d_982_valueOrError0_ = (d_980_maybeNonceSalt_).MapFailure(lambda76_)
        if (d_982_valueOrError0_).IsFailure():
            res = (d_982_valueOrError0_).PropagateFailure()
            return res
        d_981_saltAndNonce_ = (d_982_valueOrError0_).Extract()
        d_984_salt_: _dafny.Seq
        d_984_salt_ = _dafny.Seq((d_981_saltAndNonce_)[0:default__.H__WRAP__SALT__LEN:])
        d_985_nonce_: _dafny.Seq
        d_985_nonce_ = _dafny.Seq((d_981_saltAndNonce_)[default__.H__WRAP__SALT__LEN::])
        d_986_serializedEC_: _dafny.Seq
        d_987_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_987_valueOrError1_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_987_valueOrError1_).IsFailure():
            res = (d_987_valueOrError1_).PropagateFailure()
            return res
        d_986_serializedEC_ = (d_987_valueOrError1_).Extract()
        d_988_wrappingAad_: _dafny.Seq
        d_988_wrappingAad_ = default__.WrappingAad((self).branchKeyIdUtf8, (self).branchKeyVersionAsBytes, d_986_serializedEC_)
        d_989_derivedBranchKey_: _dafny.Seq
        d_990_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out178_: Wrappers.Result
        out178_ = default__.DeriveEncryptionKeyFromBranchKey((self).branchKey, d_984_salt_, Wrappers.Option_Some(Constants.default__.PROVIDER__ID__HIERARCHY), (self).crypto)
        d_990_valueOrError2_ = out178_
        if (d_990_valueOrError2_).IsFailure():
            res = (d_990_valueOrError2_).PropagateFailure()
            return res
        d_989_derivedBranchKey_ = (d_990_valueOrError2_).Extract()
        d_991_maybeWrappedPdk_: Wrappers.Result
        out179_: Wrappers.Result
        out179_ = ((self).crypto).AESEncrypt(AwsCryptographyPrimitivesTypes.AESEncryptInput_AESEncryptInput(default__.AES__256__ENC__ALG, d_985_nonce_, d_989_derivedBranchKey_, (input).plaintextMaterial, d_988_wrappingAad_))
        d_991_maybeWrappedPdk_ = out179_
        d_992_wrappedPdk_: AwsCryptographyPrimitivesTypes.AESEncryptOutput
        d_993_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.AESEncryptOutput.default())()
        def lambda77_(d_994_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_994_e_)

        d_993_valueOrError3_ = (d_991_maybeWrappedPdk_).MapFailure(lambda77_)
        if (d_993_valueOrError3_).IsFailure():
            res = (d_993_valueOrError3_).PropagateFailure()
            return res
        d_992_wrappedPdk_ = (d_993_valueOrError3_).Extract()
        d_995_output_: MaterialWrapping.WrapOutput
        d_995_output_ = MaterialWrapping.WrapOutput_WrapOutput(((((d_984_salt_) + (d_985_nonce_)) + ((self).branchKeyVersionAsBytes)) + ((d_992_wrappedPdk_).cipherText)) + ((d_992_wrappedPdk_).authTag), HierarchyWrapInfo_HierarchyWrapInfo())
        res = Wrappers.Result_Success(d_995_output_)
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
