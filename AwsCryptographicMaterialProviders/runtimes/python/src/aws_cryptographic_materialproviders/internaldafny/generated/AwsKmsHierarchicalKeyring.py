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
import aws_cryptography_primitives.internaldafny.generated.ECDH as ECDH
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
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStoreErrorMessages as KeyStoreErrorMessages
import aws_cryptographic_materialproviders.internaldafny.generated.KmsArn as KmsArn
import aws_cryptographic_materialproviders.internaldafny.generated.Structure as Structure
import aws_cryptographic_materialproviders.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_materialproviders.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable
import aws_cryptographic_materialproviders.internaldafny.generated.GetKeys as GetKeys
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import com_amazonaws_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
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
import aws_cryptographic_materialproviders.internaldafny.generated.ErrorMessages as ErrorMessages
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

# Module: AwsKmsHierarchicalKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def getEntry(cmc, input):
        res: Wrappers.Result = None
        out150_: Wrappers.Result
        out150_ = (cmc).GetCacheEntry(input)
        res = out150_
        return res

    @staticmethod
    def putEntry(cmc, input):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out151_: Wrappers.Result
        out151_ = (cmc).PutCacheEntry(input)
        res = out151_
        return res

    @staticmethod
    def DeriveEncryptionKeyFromBranchKey(branchKey, salt, purpose, cryptoPrimitives):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_843_maybeDerivedBranchKey_: Wrappers.Result
        out152_: Wrappers.Result
        out152_ = (cryptoPrimitives).KdfCounterMode(AwsCryptographyPrimitivesTypes.KdfCtrInput_KdfCtrInput(AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__256(), branchKey, default__.DERIVED__BRANCH__KEY__EXPECTED__LENGTH, purpose, Wrappers.Option_Some(salt)))
        d_843_maybeDerivedBranchKey_ = out152_
        d_844_derivedBranchKey_: _dafny.Seq
        d_845_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda73_(d_846_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_846_e_)

        d_845_valueOrError0_ = (d_843_maybeDerivedBranchKey_).MapFailure(lambda73_)
        if (d_845_valueOrError0_).IsFailure():
            output = (d_845_valueOrError0_).PropagateFailure()
            return output
        d_844_derivedBranchKey_ = (d_845_valueOrError0_).Extract()
        output = Wrappers.Result_Success(d_844_derivedBranchKey_)
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
        self._cryptoPrimitives: AtomicPrimitives.AtomicPrimitivesClient = None
        self._branchKeyIdSupplier: Wrappers.Option = Wrappers.Option.default()()
        self._branchKeyId: Wrappers.Option = Wrappers.Option.default()()
        self._ttlSeconds: int = None
        self._cache: AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsCache = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsHierarchicalKeyring.AwsKmsHierarchicalKeyring"
    def OnDecrypt(self, input):
        out153_: Wrappers.Result
        out153_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnDecrypt(self, input)
        return out153_

    def OnEncrypt(self, input):
        out154_: Wrappers.Result
        out154_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnEncrypt(self, input)
        return out154_

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
            d_847_GetBranchKeyIdOut_: AwsCryptographyMaterialProvidersTypes.GetBranchKeyIdOutput
            d_848_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyMaterialProvidersTypes.GetBranchKeyIdOutput.default())()
            out155_: Wrappers.Result
            out155_ = (((self).branchKeyIdSupplier).value).GetBranchKeyId(AwsCryptographyMaterialProvidersTypes.GetBranchKeyIdInput_GetBranchKeyIdInput(context))
            d_848_valueOrError0_ = out155_
            if (d_848_valueOrError0_).IsFailure():
                ret = (d_848_valueOrError0_).PropagateFailure()
                return ret
            d_847_GetBranchKeyIdOut_ = (d_848_valueOrError0_).Extract()
            ret = Wrappers.Result_Success((d_847_GetBranchKeyIdOut_).branchKeyId)
            return ret
        return ret

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        d_849_materials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_849_materials_ = (input).materials
        d_850_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_850_suite_ = (d_849_materials_).algorithmSuite
        d_851_branchKeyIdForEncrypt_: _dafny.Seq
        d_852_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out156_: Wrappers.Result
        out156_ = (self).GetBranchKeyId((d_849_materials_).encryptionContext)
        d_852_valueOrError0_ = out156_
        if (d_852_valueOrError0_).IsFailure():
            res = (d_852_valueOrError0_).PropagateFailure()
            return res
        d_851_branchKeyIdForEncrypt_ = (d_852_valueOrError0_).Extract()
        d_853_branchKeyIdUtf8_: _dafny.Seq
        d_854_valueOrError1_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_854_valueOrError1_ = (UTF8.default__.Encode(d_851_branchKeyIdForEncrypt_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_854_valueOrError1_).IsFailure():
            res = (d_854_valueOrError1_).PropagateFailure()
            return res
        d_853_branchKeyIdUtf8_ = (d_854_valueOrError1_).Extract()
        d_855_cacheId_: _dafny.Seq
        d_856_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out157_: Wrappers.Result
        out157_ = (self).GetActiveCacheId(d_851_branchKeyIdForEncrypt_, d_853_branchKeyIdUtf8_, (self).cryptoPrimitives)
        d_856_valueOrError2_ = out157_
        if (d_856_valueOrError2_).IsFailure():
            res = (d_856_valueOrError2_).PropagateFailure()
            return res
        d_855_cacheId_ = (d_856_valueOrError2_).Extract()
        d_857_hierarchicalMaterials_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
        d_858_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.BranchKeyMaterials.default())()
        out158_: Wrappers.Result
        out158_ = (self).GetActiveHierarchicalMaterials(d_851_branchKeyIdForEncrypt_, d_855_cacheId_, (self).keyStore)
        d_858_valueOrError3_ = out158_
        if (d_858_valueOrError3_).IsFailure():
            res = (d_858_valueOrError3_).PropagateFailure()
            return res
        d_857_hierarchicalMaterials_ = (d_858_valueOrError3_).Extract()
        d_859_branchKey_: _dafny.Seq
        d_859_branchKey_ = (d_857_hierarchicalMaterials_).branchKey
        d_860_branchKeyVersion_: _dafny.Seq
        d_860_branchKeyVersion_ = (d_857_hierarchicalMaterials_).branchKeyVersion
        d_861_branchKeyVersionAsString_: _dafny.Seq
        d_862_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_862_valueOrError4_ = (UTF8.default__.Decode(d_860_branchKeyVersion_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_862_valueOrError4_).IsFailure():
            res = (d_862_valueOrError4_).PropagateFailure()
            return res
        d_861_branchKeyVersionAsString_ = (d_862_valueOrError4_).Extract()
        d_863_branchKeyVersionAsBytes_: _dafny.Seq
        d_864_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_864_valueOrError5_ = (UUID.default__.ToByteArray(d_861_branchKeyVersionAsString_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_864_valueOrError5_).IsFailure():
            res = (d_864_valueOrError5_).PropagateFailure()
            return res
        d_863_branchKeyVersionAsBytes_ = (d_864_valueOrError5_).Extract()
        d_865_kmsHierarchyGenerateAndWrap_: KmsHierarchyGenerateAndWrapKeyMaterial
        nw33_ = KmsHierarchyGenerateAndWrapKeyMaterial()
        nw33_.ctor__((d_857_hierarchicalMaterials_).branchKey, d_853_branchKeyIdUtf8_, d_863_branchKeyVersionAsBytes_, (self).cryptoPrimitives)
        d_865_kmsHierarchyGenerateAndWrap_ = nw33_
        d_866_kmsHierarchyWrap_: KmsHierarchyWrapKeyMaterial
        nw34_ = KmsHierarchyWrapKeyMaterial()
        nw34_.ctor__((d_857_hierarchicalMaterials_).branchKey, d_853_branchKeyIdUtf8_, d_863_branchKeyVersionAsBytes_, (self).cryptoPrimitives)
        d_866_kmsHierarchyWrap_ = nw34_
        d_867_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_868_valueOrError6_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.WrapEdkMaterialOutput.default(HierarchyWrapInfo.default()))()
        out159_: Wrappers.Result
        out159_ = EdkWrapping.default__.WrapEdkMaterial(d_849_materials_, d_866_kmsHierarchyWrap_, d_865_kmsHierarchyGenerateAndWrap_)
        d_868_valueOrError6_ = out159_
        if (d_868_valueOrError6_).IsFailure():
            res = (d_868_valueOrError6_).PropagateFailure()
            return res
        d_867_wrapOutput_ = (d_868_valueOrError6_).Extract()
        d_869_symmetricSigningKeyList_: Wrappers.Option
        d_869_symmetricSigningKeyList_ = (Wrappers.Option_Some(_dafny.Seq([((d_867_wrapOutput_).symmetricSigningKey).value])) if ((d_867_wrapOutput_).symmetricSigningKey).is_Some else Wrappers.Option_None())
        d_870_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_870_edk_ = AwsCryptographyMaterialProvidersTypes.EncryptedDataKey_EncryptedDataKey(Constants.default__.PROVIDER__ID__HIERARCHY, d_853_branchKeyIdUtf8_, (d_867_wrapOutput_).wrappedMaterial)
        if (d_867_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_871_result_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_872_valueOrError7_: Wrappers.Result = None
            d_872_valueOrError7_ = Materials.default__.EncryptionMaterialAddDataKey(d_849_materials_, (d_867_wrapOutput_).plaintextDataKey, _dafny.Seq([d_870_edk_]), d_869_symmetricSigningKeyList_)
            if (d_872_valueOrError7_).IsFailure():
                res = (d_872_valueOrError7_).PropagateFailure()
                return res
            d_871_result_ = (d_872_valueOrError7_).Extract()
            res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(d_871_result_))
            return res
        elif (d_867_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_873_result_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_874_valueOrError8_: Wrappers.Result = None
            d_874_valueOrError8_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys(d_849_materials_, _dafny.Seq([d_870_edk_]), d_869_symmetricSigningKeyList_)
            if (d_874_valueOrError8_).IsFailure():
                res = (d_874_valueOrError8_).PropagateFailure()
                return res
            d_873_result_ = (d_874_valueOrError8_).Extract()
            res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(d_873_result_))
            return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_875_materials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_875_materials_ = (input).materials
        d_876_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_876_suite_ = ((input).materials).algorithmSuite
        d_877_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_877_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_875_materials_), default__.E(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_877_valueOrError0_).IsFailure():
            res = (d_877_valueOrError0_).PropagateFailure()
            return res
        d_878_branchKeyIdForDecrypt_: _dafny.Seq
        d_879_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out160_: Wrappers.Result
        out160_ = (self).GetBranchKeyId((d_875_materials_).encryptionContext)
        d_879_valueOrError1_ = out160_
        if (d_879_valueOrError1_).IsFailure():
            res = (d_879_valueOrError1_).PropagateFailure()
            return res
        d_878_branchKeyIdForDecrypt_ = (d_879_valueOrError1_).Extract()
        d_880_filter_: OnDecryptHierarchyEncryptedDataKeyFilter
        nw35_ = OnDecryptHierarchyEncryptedDataKeyFilter()
        nw35_.ctor__(d_878_branchKeyIdForDecrypt_)
        d_880_filter_ = nw35_
        d_881_edksToAttempt_: _dafny.Seq
        d_882_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out161_: Wrappers.Result
        out161_ = Actions.default__.FilterWithResult(d_880_filter_, (input).encryptedDataKeys)
        d_882_valueOrError2_ = out161_
        if (d_882_valueOrError2_).IsFailure():
            res = (d_882_valueOrError2_).PropagateFailure()
            return res
        d_881_edksToAttempt_ = (d_882_valueOrError2_).Extract()
        if (0) == (len(d_881_edksToAttempt_)):
            d_883_errorMessage_: _dafny.Seq
            d_884_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            d_884_valueOrError3_ = ErrorMessages.default__.IncorrectDataKeys((input).encryptedDataKeys, ((input).materials).algorithmSuite, _dafny.Seq(""))
            if (d_884_valueOrError3_).IsFailure():
                res = (d_884_valueOrError3_).PropagateFailure()
                return res
            d_883_errorMessage_ = (d_884_valueOrError3_).Extract()
            res = Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_883_errorMessage_))
            return res
        d_885_decryptClosure_: Actions.ActionWithResult
        nw36_ = DecryptSingleEncryptedDataKey()
        nw36_.ctor__(d_875_materials_, (self).keyStore, (self).cryptoPrimitives, d_878_branchKeyIdForDecrypt_, (self).ttlSeconds, (self).cache)
        d_885_decryptClosure_ = nw36_
        d_886_outcome_: Wrappers.Result
        out162_: Wrappers.Result
        out162_ = Actions.default__.ReduceToSuccess(d_885_decryptClosure_, d_881_edksToAttempt_)
        d_886_outcome_ = out162_
        d_887_SealedDecryptionMaterials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_888_valueOrError4_: Wrappers.Result = None
        def lambda74_(d_889_errors_):
            return AwsCryptographyMaterialProvidersTypes.Error_CollectionOfErrors(d_889_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."))

        d_888_valueOrError4_ = (d_886_outcome_).MapFailure(lambda74_)
        if (d_888_valueOrError4_).IsFailure():
            res = (d_888_valueOrError4_).PropagateFailure()
            return res
        d_887_SealedDecryptionMaterials_ = (d_888_valueOrError4_).Extract()
        res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnDecryptOutput_OnDecryptOutput(d_887_SealedDecryptionMaterials_))
        return res
        return res

    def GetActiveCacheId(self, branchKeyId, branchKeyIdUtf8, cryptoPrimitives):
        cacheId: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_890_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        def iife26_(_pat_let8_0):
            def iife27_(d_891_branchKeyId_):
                return (True) and (((0) <= (len(d_891_branchKeyId_))) and ((len(d_891_branchKeyId_)) < (StandardLibrary_UInt.default__.UINT32__LIMIT)))
            return iife27_(_pat_let8_0)
        d_890_valueOrError0_ = Wrappers.default__.Need((((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).is_Success) and (iife26_(((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).value)), default__.E(_dafny.Seq("Invalid Branch Key ID Length")))
        if (d_890_valueOrError0_).IsFailure():
            cacheId = (d_890_valueOrError0_).PropagateFailure()
            return cacheId
        d_892_branchKeyId_: _dafny.Seq
        d_892_branchKeyId_ = (UTF8.default__.Decode(branchKeyIdUtf8)).value
        d_893_lenBranchKey_: _dafny.Seq
        d_893_lenBranchKey_ = StandardLibrary_UInt.default__.UInt32ToSeq(len(d_892_branchKeyId_))
        d_894_hashAlgorithm_: AwsCryptographyPrimitivesTypes.DigestAlgorithm
        d_894_hashAlgorithm_ = AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__512()
        d_895_maybeBranchKeyDigest_: Wrappers.Result
        out163_: Wrappers.Result
        out163_ = (cryptoPrimitives).Digest(AwsCryptographyPrimitivesTypes.DigestInput_DigestInput(d_894_hashAlgorithm_, branchKeyIdUtf8))
        d_895_maybeBranchKeyDigest_ = out163_
        d_896_branchKeyDigest_: _dafny.Seq
        d_897_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda75_(d_898_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_898_e_)

        d_897_valueOrError1_ = (d_895_maybeBranchKeyDigest_).MapFailure(lambda75_)
        if (d_897_valueOrError1_).IsFailure():
            cacheId = (d_897_valueOrError1_).PropagateFailure()
            return cacheId
        d_896_branchKeyDigest_ = (d_897_valueOrError1_).Extract()
        d_899_activeUtf8_: _dafny.Seq
        d_900_valueOrError2_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_900_valueOrError2_ = (UTF8.default__.Encode(default__.EXPRESSION__ATTRIBUTE__VALUE__STATUS__VALUE)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_900_valueOrError2_).IsFailure():
            cacheId = (d_900_valueOrError2_).PropagateFailure()
            return cacheId
        d_899_activeUtf8_ = (d_900_valueOrError2_).Extract()
        d_901_identifier_: _dafny.Seq
        d_901_identifier_ = (((d_893_lenBranchKey_) + (d_896_branchKeyDigest_)) + (_dafny.Seq([0]))) + (d_899_activeUtf8_)
        d_902_maybeCacheIdDigest_: Wrappers.Result
        out164_: Wrappers.Result
        out164_ = (cryptoPrimitives).Digest(AwsCryptographyPrimitivesTypes.DigestInput_DigestInput(d_894_hashAlgorithm_, d_901_identifier_))
        d_902_maybeCacheIdDigest_ = out164_
        d_903_cacheDigest_: _dafny.Seq
        d_904_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda76_(d_905_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_905_e_)

        d_904_valueOrError3_ = (d_902_maybeCacheIdDigest_).MapFailure(lambda76_)
        if (d_904_valueOrError3_).IsFailure():
            cacheId = (d_904_valueOrError3_).PropagateFailure()
            return cacheId
        d_903_cacheDigest_ = (d_904_valueOrError3_).Extract()
        d_906_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_906_valueOrError4_ = Wrappers.default__.Need((len(d_903_cacheDigest_)) == (Digest.default__.Length(d_894_hashAlgorithm_)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Digest generated a message not equal to the expected length.")))
        if (d_906_valueOrError4_).IsFailure():
            cacheId = (d_906_valueOrError4_).PropagateFailure()
            return cacheId
        cacheId = Wrappers.Result_Success(_dafny.Seq((d_903_cacheDigest_)[0:32:]))
        return cacheId
        return cacheId

    def GetActiveHierarchicalMaterials(self, branchKeyId, cacheId, keyStore):
        material: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.BranchKeyMaterials.default())()
        d_907_getCacheInput_: AwsCryptographyMaterialProvidersTypes.GetCacheEntryInput
        d_907_getCacheInput_ = AwsCryptographyMaterialProvidersTypes.GetCacheEntryInput_GetCacheEntryInput(cacheId, Wrappers.Option_None())
        d_908_getCacheOutput_: Wrappers.Result
        out165_: Wrappers.Result
        out165_ = default__.getEntry((self).cache, d_907_getCacheInput_)
        d_908_getCacheOutput_ = out165_
        if (d_908_getCacheOutput_).is_Failure:
            d_909_maybeGetActiveBranchKeyOutput_: Wrappers.Result
            out166_: Wrappers.Result
            out166_ = (keyStore).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(branchKeyId))
            d_909_maybeGetActiveBranchKeyOutput_ = out166_
            d_910_getActiveBranchKeyOutput_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
            d_911_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
            def lambda77_(d_912_e_):
                return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyKeyStore(d_912_e_)

            d_911_valueOrError0_ = (d_909_maybeGetActiveBranchKeyOutput_).MapFailure(lambda77_)
            if (d_911_valueOrError0_).IsFailure():
                material = (d_911_valueOrError0_).PropagateFailure()
                return material
            d_910_getActiveBranchKeyOutput_ = (d_911_valueOrError0_).Extract()
            d_913_branchKeyMaterials_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
            d_913_branchKeyMaterials_ = (d_910_getActiveBranchKeyOutput_).branchKeyMaterials
            d_914_now_: int
            out167_: int
            out167_ = Time.default__.CurrentRelativeTime()
            d_914_now_ = out167_
            d_915_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_915_valueOrError1_ = Wrappers.default__.Need(((d_914_now_) + ((self).ttlSeconds)) < (StandardLibrary_UInt.default__.INT64__MAX__LIMIT), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("INT64 Overflow when putting cache entry.")))
            if (d_915_valueOrError1_).IsFailure():
                material = (d_915_valueOrError1_).PropagateFailure()
                return material
            d_916_putCacheEntryInput_: AwsCryptographyMaterialProvidersTypes.PutCacheEntryInput
            d_916_putCacheEntryInput_ = AwsCryptographyMaterialProvidersTypes.PutCacheEntryInput_PutCacheEntryInput(cacheId, AwsCryptographyMaterialProvidersTypes.Materials_BranchKey(d_913_branchKeyMaterials_), d_914_now_, ((self).ttlSeconds) + (d_914_now_), Wrappers.Option_None(), Wrappers.Option_None())
            d_917___v0_: tuple
            d_918_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            out168_: Wrappers.Result
            out168_ = default__.putEntry((self).cache, d_916_putCacheEntryInput_)
            d_918_valueOrError2_ = out168_
            if (d_918_valueOrError2_).IsFailure():
                material = (d_918_valueOrError2_).PropagateFailure()
                return material
            d_917___v0_ = (d_918_valueOrError2_).Extract()
            material = Wrappers.Result_Success(d_913_branchKeyMaterials_)
            return material
        elif True:
            d_919_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_919_valueOrError3_ = Wrappers.default__.Need(((((d_908_getCacheOutput_).value).materials).is_BranchKey) and ((((d_908_getCacheOutput_).value).materials) == (AwsCryptographyMaterialProvidersTypes.Materials_BranchKey((((d_908_getCacheOutput_).value).materials).BranchKey))), default__.E(_dafny.Seq("Invalid Material Type.")))
            if (d_919_valueOrError3_).IsFailure():
                material = (d_919_valueOrError3_).PropagateFailure()
                return material
            material = Wrappers.Result_Success((((d_908_getCacheOutput_).value).materials).BranchKey)
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
        d_920_providerInfo_: _dafny.Seq
        d_920_providerInfo_ = (edk).keyProviderInfo
        d_921_providerId_: _dafny.Seq
        d_921_providerId_ = (edk).keyProviderId
        if (d_921_providerId_) != (Constants.default__.PROVIDER__ID__HIERARCHY):
            res = Wrappers.Result_Success(False)
            return res
        if not(UTF8.default__.ValidUTF8Seq(d_920_providerInfo_)):
            res = Wrappers.Result_Failure(default__.E(_dafny.Seq("Invalid encoding, provider info is not UTF8.")))
            return res
        d_922_branchKeyId_: _dafny.Seq
        d_923_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_923_valueOrError0_ = (UTF8.default__.Decode(d_920_providerInfo_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_923_valueOrError0_).IsFailure():
            res = (d_923_valueOrError0_).PropagateFailure()
            return res
        d_922_branchKeyId_ = (d_923_valueOrError0_).Extract()
        res = Wrappers.Result_Success(((self).branchKeyId) == (d_922_branchKeyId_))
        return res
        return res

    @property
    def branchKeyId(self):
        return self._branchKeyId

class DecryptSingleEncryptedDataKey(Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._materials: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials = None
        self._keyStore: AwsCryptographyKeyStoreTypes.IKeyStoreClient = None
        self._cryptoPrimitives: AtomicPrimitives.AtomicPrimitivesClient = None
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
        d_924_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_924_valueOrError0_ = Wrappers.default__.Need(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received invalid EDK provider info for Hierarchical Keyring")))
        if (d_924_valueOrError0_).IsFailure():
            res = (d_924_valueOrError0_).PropagateFailure()
            return res
        d_925_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_925_suite_ = ((self).materials).algorithmSuite
        d_926_keyProviderId_: _dafny.Seq
        d_926_keyProviderId_ = (edk).keyProviderId
        d_927_branchKeyIdUtf8_: _dafny.Seq
        d_927_branchKeyIdUtf8_ = (edk).keyProviderInfo
        d_928_ciphertext_: _dafny.Seq
        d_928_ciphertext_ = (edk).ciphertext
        d_929_providerWrappedMaterial_: _dafny.Seq
        d_930_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_930_valueOrError1_ = EdkWrapping.default__.GetProviderWrappedMaterial(d_928_ciphertext_, d_925_suite_)
        if (d_930_valueOrError1_).IsFailure():
            res = (d_930_valueOrError1_).PropagateFailure()
            return res
        d_929_providerWrappedMaterial_ = (d_930_valueOrError1_).Extract()
        d_931_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_931_valueOrError2_ = Wrappers.default__.Need((len(d_929_providerWrappedMaterial_)) >= (default__.EDK__CIPHERTEXT__VERSION__INDEX), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received EDK Ciphertext of incorrect length.")))
        if (d_931_valueOrError2_).IsFailure():
            res = (d_931_valueOrError2_).PropagateFailure()
            return res
        d_932_branchKeyVersionUuid_: _dafny.Seq
        d_932_branchKeyVersionUuid_ = _dafny.Seq((d_929_providerWrappedMaterial_)[default__.EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX:default__.EDK__CIPHERTEXT__VERSION__INDEX:])
        d_933_version_: _dafny.Seq
        d_934_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_934_valueOrError3_ = (UUID.default__.FromByteArray(d_932_branchKeyVersionUuid_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_934_valueOrError3_).IsFailure():
            res = (d_934_valueOrError3_).PropagateFailure()
            return res
        d_933_version_ = (d_934_valueOrError3_).Extract()
        d_935_cacheId_: _dafny.Seq
        d_936_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out169_: Wrappers.Result
        out169_ = (self).GetVersionCacheId(d_927_branchKeyIdUtf8_, d_933_version_, (self).cryptoPrimitives)
        d_936_valueOrError4_ = out169_
        if (d_936_valueOrError4_).IsFailure():
            res = (d_936_valueOrError4_).PropagateFailure()
            return res
        d_935_cacheId_ = (d_936_valueOrError4_).Extract()
        d_937_hierarchicalMaterials_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
        d_938_valueOrError5_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.BranchKeyMaterials.default())()
        out170_: Wrappers.Result
        out170_ = (self).GetHierarchicalMaterialsVersion((self).branchKeyId, d_927_branchKeyIdUtf8_, d_933_version_, d_935_cacheId_)
        d_938_valueOrError5_ = out170_
        if (d_938_valueOrError5_).IsFailure():
            res = (d_938_valueOrError5_).PropagateFailure()
            return res
        d_937_hierarchicalMaterials_ = (d_938_valueOrError5_).Extract()
        d_939_branchKey_: _dafny.Seq
        d_939_branchKey_ = (d_937_hierarchicalMaterials_).branchKey
        d_940_branchKeyVersion_: _dafny.Seq
        d_940_branchKeyVersion_ = (d_937_hierarchicalMaterials_).branchKeyVersion
        d_941_branchKeyVersionAsString_: _dafny.Seq
        d_942_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_942_valueOrError6_ = (UTF8.default__.Decode(d_940_branchKeyVersion_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_942_valueOrError6_).IsFailure():
            res = (d_942_valueOrError6_).PropagateFailure()
            return res
        d_941_branchKeyVersionAsString_ = (d_942_valueOrError6_).Extract()
        d_943_branchKeyVersionAsBytes_: _dafny.Seq
        d_944_valueOrError7_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_944_valueOrError7_ = (UUID.default__.ToByteArray(d_941_branchKeyVersionAsString_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_944_valueOrError7_).IsFailure():
            res = (d_944_valueOrError7_).PropagateFailure()
            return res
        d_943_branchKeyVersionAsBytes_ = (d_944_valueOrError7_).Extract()
        d_945_maybeCrypto_: Wrappers.Result
        out171_: Wrappers.Result
        out171_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_945_maybeCrypto_ = out171_
        d_946_cryptoPrimitivesX_: AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient
        d_947_valueOrError8_: Wrappers.Result = None
        def lambda78_(d_948_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_948_e_)

        d_947_valueOrError8_ = (d_945_maybeCrypto_).MapFailure(lambda78_)
        if (d_947_valueOrError8_).IsFailure():
            res = (d_947_valueOrError8_).PropagateFailure()
            return res
        d_946_cryptoPrimitivesX_ = (d_947_valueOrError8_).Extract()
        d_949_cryptoPrimitives_: AtomicPrimitives.AtomicPrimitivesClient
        d_949_cryptoPrimitives_ = d_946_cryptoPrimitivesX_
        d_950_kmsHierarchyUnwrap_: KmsHierarchyUnwrapKeyMaterial
        nw37_ = KmsHierarchyUnwrapKeyMaterial()
        nw37_.ctor__(d_939_branchKey_, d_927_branchKeyIdUtf8_, d_943_branchKeyVersionAsBytes_, d_949_cryptoPrimitives_)
        d_950_kmsHierarchyUnwrap_ = nw37_
        d_951_unwrapOutputRes_: Wrappers.Result
        out172_: Wrappers.Result
        out172_ = EdkWrapping.default__.UnwrapEdkMaterial((edk).ciphertext, (self).materials, d_950_kmsHierarchyUnwrap_)
        d_951_unwrapOutputRes_ = out172_
        d_952_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_953_valueOrError9_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.UnwrapEdkMaterialOutput.default(HierarchyUnwrapInfo.default()))()
        d_953_valueOrError9_ = d_951_unwrapOutputRes_
        if (d_953_valueOrError9_).IsFailure():
            res = (d_953_valueOrError9_).PropagateFailure()
            return res
        d_952_unwrapOutput_ = (d_953_valueOrError9_).Extract()
        d_954_result_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_955_valueOrError10_: Wrappers.Result = None
        d_955_valueOrError10_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_952_unwrapOutput_).plaintextDataKey, (d_952_unwrapOutput_).symmetricSigningKey)
        if (d_955_valueOrError10_).IsFailure():
            res = (d_955_valueOrError10_).PropagateFailure()
            return res
        d_954_result_ = (d_955_valueOrError10_).Extract()
        res = Wrappers.Result_Success(d_954_result_)
        return res
        return res

    def GetVersionCacheId(self, branchKeyIdUtf8, branchKeyVersion, cryptoPrimitives):
        cacheId: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_956_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        def iife28_(_pat_let9_0):
            def iife29_(d_957_branchKeyId_):
                return (True) and (((0) <= (len(d_957_branchKeyId_))) and ((len(d_957_branchKeyId_)) < (StandardLibrary_UInt.default__.UINT32__LIMIT)))
            return iife29_(_pat_let9_0)
        d_956_valueOrError0_ = Wrappers.default__.Need((((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).is_Success) and (iife28_(((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).value)), default__.E(_dafny.Seq("Invalid Branch Key ID Length")))
        if (d_956_valueOrError0_).IsFailure():
            cacheId = (d_956_valueOrError0_).PropagateFailure()
            return cacheId
        d_958_branchKeyId_: _dafny.Seq
        d_958_branchKeyId_ = (UTF8.default__.Decode(branchKeyIdUtf8)).value
        d_959_lenBranchKey_: _dafny.Seq
        d_959_lenBranchKey_ = StandardLibrary_UInt.default__.UInt32ToSeq(len(d_958_branchKeyId_))
        d_960_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_960_valueOrError1_ = Wrappers.default__.Need(UTF8.default__.IsASCIIString(branchKeyVersion), default__.E(_dafny.Seq("Unable to represent as an ASCII string.")))
        if (d_960_valueOrError1_).IsFailure():
            cacheId = (d_960_valueOrError1_).PropagateFailure()
            return cacheId
        d_961_versionBytes_: _dafny.Seq
        d_961_versionBytes_ = UTF8.default__.EncodeAscii(branchKeyVersion)
        d_962_identifier_: _dafny.Seq
        d_962_identifier_ = (((d_959_lenBranchKey_) + (branchKeyIdUtf8)) + (_dafny.Seq([0]))) + (d_961_versionBytes_)
        d_963_identifierDigestInput_: AwsCryptographyPrimitivesTypes.DigestInput
        d_963_identifierDigestInput_ = AwsCryptographyPrimitivesTypes.DigestInput_DigestInput(AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__512(), d_962_identifier_)
        d_964_maybeCacheDigest_: Wrappers.Result
        out173_: Wrappers.Result
        out173_ = Digest.default__.Digest(d_963_identifierDigestInput_)
        d_964_maybeCacheDigest_ = out173_
        d_965_cacheDigest_: _dafny.Seq
        d_966_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda79_(d_967_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_967_e_)

        d_966_valueOrError2_ = (d_964_maybeCacheDigest_).MapFailure(lambda79_)
        if (d_966_valueOrError2_).IsFailure():
            cacheId = (d_966_valueOrError2_).PropagateFailure()
            return cacheId
        d_965_cacheDigest_ = (d_966_valueOrError2_).Extract()
        cacheId = Wrappers.Result_Success(_dafny.Seq((d_965_cacheDigest_)[0:32:]))
        return cacheId
        return cacheId

    def GetHierarchicalMaterialsVersion(self, branchKeyId, branchKeyIdUtf8, version, cacheId):
        material: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.BranchKeyMaterials.default())()
        d_968_getCacheInput_: AwsCryptographyMaterialProvidersTypes.GetCacheEntryInput
        d_968_getCacheInput_ = AwsCryptographyMaterialProvidersTypes.GetCacheEntryInput_GetCacheEntryInput(cacheId, Wrappers.Option_None())
        d_969_getCacheOutput_: Wrappers.Result
        out174_: Wrappers.Result
        out174_ = default__.getEntry((self).cache, d_968_getCacheInput_)
        d_969_getCacheOutput_ = out174_
        if (d_969_getCacheOutput_).is_Failure:
            d_970_maybeGetBranchKeyVersionOutput_: Wrappers.Result
            out175_: Wrappers.Result
            out175_ = ((self).keyStore).GetBranchKeyVersion(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput_GetBranchKeyVersionInput(branchKeyId, version))
            d_970_maybeGetBranchKeyVersionOutput_ = out175_
            d_971_getBranchKeyVersionOutput_: AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
            d_972_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
            def lambda80_(d_973_e_):
                return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyKeyStore(d_973_e_)

            d_972_valueOrError0_ = (d_970_maybeGetBranchKeyVersionOutput_).MapFailure(lambda80_)
            if (d_972_valueOrError0_).IsFailure():
                material = (d_972_valueOrError0_).PropagateFailure()
                return material
            d_971_getBranchKeyVersionOutput_ = (d_972_valueOrError0_).Extract()
            d_974_branchKeyMaterials_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
            d_974_branchKeyMaterials_ = (d_971_getBranchKeyVersionOutput_).branchKeyMaterials
            d_975_now_: int
            out176_: int
            out176_ = Time.default__.CurrentRelativeTime()
            d_975_now_ = out176_
            d_976_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_976_valueOrError1_ = Wrappers.default__.Need(((d_975_now_) + ((self).ttlSeconds)) < (StandardLibrary_UInt.default__.INT64__MAX__LIMIT), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("INT64 Overflow when putting cache entry.")))
            if (d_976_valueOrError1_).IsFailure():
                material = (d_976_valueOrError1_).PropagateFailure()
                return material
            d_977_putCacheEntryInput_: AwsCryptographyMaterialProvidersTypes.PutCacheEntryInput
            d_977_putCacheEntryInput_ = AwsCryptographyMaterialProvidersTypes.PutCacheEntryInput_PutCacheEntryInput(cacheId, AwsCryptographyMaterialProvidersTypes.Materials_BranchKey(d_974_branchKeyMaterials_), d_975_now_, ((self).ttlSeconds) + (d_975_now_), Wrappers.Option_None(), Wrappers.Option_None())
            d_978___v1_: tuple
            d_979_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            out177_: Wrappers.Result
            out177_ = default__.putEntry((self).cache, d_977_putCacheEntryInput_)
            d_979_valueOrError2_ = out177_
            if (d_979_valueOrError2_).IsFailure():
                material = (d_979_valueOrError2_).PropagateFailure()
                return material
            d_978___v1_ = (d_979_valueOrError2_).Extract()
            material = Wrappers.Result_Success(d_974_branchKeyMaterials_)
            return material
        elif True:
            d_980_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_980_valueOrError3_ = Wrappers.default__.Need(((((d_969_getCacheOutput_).value).materials).is_BranchKey) and ((((d_969_getCacheOutput_).value).materials) == (AwsCryptographyMaterialProvidersTypes.Materials_BranchKey((((d_969_getCacheOutput_).value).materials).BranchKey))), default__.E(_dafny.Seq("Invalid Material Type.")))
            if (d_980_valueOrError3_).IsFailure():
                material = (d_980_valueOrError3_).PropagateFailure()
                return material
            material = Wrappers.Result_Success((((d_969_getCacheOutput_).value).materials).BranchKey)
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
        self._crypto: AtomicPrimitives.AtomicPrimitivesClient = None
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
        d_981_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_981_suite_ = (input).algorithmSuite
        d_982_wrappedMaterial_: _dafny.Seq
        d_982_wrappedMaterial_ = (input).wrappedMaterial
        d_983_aad_: _dafny.Map
        d_983_aad_ = (input).encryptionContext
        d_984_KeyLength_: int
        d_984_KeyLength_ = AlgorithmSuites.default__.GetEncryptKeyLength(d_981_suite_)
        d_985_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_985_valueOrError0_ = Wrappers.default__.Need((len(d_982_wrappedMaterial_)) == ((default__.EXPECTED__EDK__CIPHERTEXT__OVERHEAD) + (d_984_KeyLength_)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received EDK Ciphertext of incorrect length2.")))
        if (d_985_valueOrError0_).IsFailure():
            res = (d_985_valueOrError0_).PropagateFailure()
            return res
        d_986_salt_: _dafny.Seq
        d_986_salt_ = _dafny.Seq((d_982_wrappedMaterial_)[0:default__.H__WRAP__SALT__LEN:])
        d_987_iv_: _dafny.Seq
        d_987_iv_ = _dafny.Seq((d_982_wrappedMaterial_)[default__.H__WRAP__SALT__LEN:default__.EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX:])
        d_988_branchKeyVersionUuid_: _dafny.Seq
        d_988_branchKeyVersionUuid_ = _dafny.Seq((d_982_wrappedMaterial_)[default__.EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX:default__.EDK__CIPHERTEXT__VERSION__INDEX:])
        d_989_wrappedKey_: _dafny.Seq
        d_989_wrappedKey_ = _dafny.Seq((d_982_wrappedMaterial_)[default__.EDK__CIPHERTEXT__VERSION__INDEX:(default__.EDK__CIPHERTEXT__VERSION__INDEX) + (d_984_KeyLength_):])
        d_990_authTag_: _dafny.Seq
        d_990_authTag_ = _dafny.Seq((d_982_wrappedMaterial_)[(default__.EDK__CIPHERTEXT__VERSION__INDEX) + (d_984_KeyLength_)::])
        d_991_serializedEC_: _dafny.Seq
        d_992_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_992_valueOrError1_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_992_valueOrError1_).IsFailure():
            res = (d_992_valueOrError1_).PropagateFailure()
            return res
        d_991_serializedEC_ = (d_992_valueOrError1_).Extract()
        d_993_wrappingAad_: _dafny.Seq
        d_993_wrappingAad_ = default__.WrappingAad((self).branchKeyIdUtf8, (self).branchKeyVersionAsBytes, d_991_serializedEC_)
        d_994_derivedBranchKey_: _dafny.Seq
        d_995_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out178_: Wrappers.Result
        out178_ = default__.DeriveEncryptionKeyFromBranchKey((self).branchKey, d_986_salt_, Wrappers.Option_Some(Constants.default__.PROVIDER__ID__HIERARCHY), (self).crypto)
        d_995_valueOrError2_ = out178_
        if (d_995_valueOrError2_).IsFailure():
            res = (d_995_valueOrError2_).PropagateFailure()
            return res
        d_994_derivedBranchKey_ = (d_995_valueOrError2_).Extract()
        d_996_maybeUnwrappedPdk_: Wrappers.Result
        out179_: Wrappers.Result
        out179_ = ((self).crypto).AESDecrypt(AwsCryptographyPrimitivesTypes.AESDecryptInput_AESDecryptInput(default__.AES__256__ENC__ALG, d_994_derivedBranchKey_, d_989_wrappedKey_, d_990_authTag_, d_987_iv_, d_993_wrappingAad_))
        d_996_maybeUnwrappedPdk_ = out179_
        d_997_unwrappedPdk_: _dafny.Seq
        d_998_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda81_(d_999_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_999_e_)

        d_998_valueOrError3_ = (d_996_maybeUnwrappedPdk_).MapFailure(lambda81_)
        if (d_998_valueOrError3_).IsFailure():
            res = (d_998_valueOrError3_).PropagateFailure()
            return res
        d_997_unwrappedPdk_ = (d_998_valueOrError3_).Extract()
        d_1000_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1000_valueOrError4_ = Wrappers.default__.Need((len(d_997_unwrappedPdk_)) == (AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)), default__.E(_dafny.Seq("Invalid Key Length")))
        if (d_1000_valueOrError4_).IsFailure():
            res = (d_1000_valueOrError4_).PropagateFailure()
            return res
        d_1001_output_: MaterialWrapping.UnwrapOutput
        d_1001_output_ = MaterialWrapping.UnwrapOutput_UnwrapOutput(d_997_unwrappedPdk_, HierarchyUnwrapInfo_HierarchyUnwrapInfo())
        res = Wrappers.Result_Success(d_1001_output_)
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
        self._crypto: AtomicPrimitives.AtomicPrimitivesClient = None
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
        d_1002_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_1002_suite_ = (input).algorithmSuite
        d_1003_pdkResult_: Wrappers.Result
        out180_: Wrappers.Result
        out180_ = ((self).crypto).GenerateRandomBytes(AwsCryptographyPrimitivesTypes.GenerateRandomBytesInput_GenerateRandomBytesInput(AlgorithmSuites.default__.GetEncryptKeyLength(d_1002_suite_)))
        d_1003_pdkResult_ = out180_
        d_1004_pdk_: _dafny.Seq
        d_1005_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda82_(d_1006_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1006_e_)

        d_1005_valueOrError0_ = (d_1003_pdkResult_).MapFailure(lambda82_)
        if (d_1005_valueOrError0_).IsFailure():
            res = (d_1005_valueOrError0_).PropagateFailure()
            return res
        d_1004_pdk_ = (d_1005_valueOrError0_).Extract()
        d_1007_wrap_: KmsHierarchyWrapKeyMaterial
        nw38_ = KmsHierarchyWrapKeyMaterial()
        nw38_.ctor__((self).branchKey, (self).branchKeyIdUtf8, (self).branchKeyVersionAsBytes, (self).crypto)
        d_1007_wrap_ = nw38_
        d_1008_wrapOutput_: MaterialWrapping.WrapOutput
        d_1009_valueOrError1_: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.WrapOutput.default(HierarchyWrapInfo.default()))()
        out181_: Wrappers.Result
        out181_ = (d_1007_wrap_).Invoke(MaterialWrapping.WrapInput_WrapInput(d_1004_pdk_, (input).algorithmSuite, (input).encryptionContext))
        d_1009_valueOrError1_ = out181_
        if (d_1009_valueOrError1_).IsFailure():
            res = (d_1009_valueOrError1_).PropagateFailure()
            return res
        d_1008_wrapOutput_ = (d_1009_valueOrError1_).Extract()
        d_1010_output_: MaterialWrapping.GenerateAndWrapOutput
        d_1010_output_ = MaterialWrapping.GenerateAndWrapOutput_GenerateAndWrapOutput(d_1004_pdk_, (d_1008_wrapOutput_).wrappedMaterial, HierarchyWrapInfo_HierarchyWrapInfo())
        res = Wrappers.Result_Success(d_1010_output_)
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
        self._crypto: AtomicPrimitives.AtomicPrimitivesClient = None
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
        d_1011_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_1011_suite_ = (input).algorithmSuite
        d_1012_maybeNonceSalt_: Wrappers.Result
        out182_: Wrappers.Result
        out182_ = ((self).crypto).GenerateRandomBytes(AwsCryptographyPrimitivesTypes.GenerateRandomBytesInput_GenerateRandomBytesInput((default__.H__WRAP__SALT__LEN) + (default__.H__WRAP__NONCE__LEN)))
        d_1012_maybeNonceSalt_ = out182_
        d_1013_saltAndNonce_: _dafny.Seq
        d_1014_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda83_(d_1015_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1015_e_)

        d_1014_valueOrError0_ = (d_1012_maybeNonceSalt_).MapFailure(lambda83_)
        if (d_1014_valueOrError0_).IsFailure():
            res = (d_1014_valueOrError0_).PropagateFailure()
            return res
        d_1013_saltAndNonce_ = (d_1014_valueOrError0_).Extract()
        d_1016_salt_: _dafny.Seq
        d_1016_salt_ = _dafny.Seq((d_1013_saltAndNonce_)[0:default__.H__WRAP__SALT__LEN:])
        d_1017_nonce_: _dafny.Seq
        d_1017_nonce_ = _dafny.Seq((d_1013_saltAndNonce_)[default__.H__WRAP__SALT__LEN::])
        d_1018_serializedEC_: _dafny.Seq
        d_1019_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1019_valueOrError1_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_1019_valueOrError1_).IsFailure():
            res = (d_1019_valueOrError1_).PropagateFailure()
            return res
        d_1018_serializedEC_ = (d_1019_valueOrError1_).Extract()
        d_1020_wrappingAad_: _dafny.Seq
        d_1020_wrappingAad_ = default__.WrappingAad((self).branchKeyIdUtf8, (self).branchKeyVersionAsBytes, d_1018_serializedEC_)
        d_1021_derivedBranchKey_: _dafny.Seq
        d_1022_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out183_: Wrappers.Result
        out183_ = default__.DeriveEncryptionKeyFromBranchKey((self).branchKey, d_1016_salt_, Wrappers.Option_Some(Constants.default__.PROVIDER__ID__HIERARCHY), (self).crypto)
        d_1022_valueOrError2_ = out183_
        if (d_1022_valueOrError2_).IsFailure():
            res = (d_1022_valueOrError2_).PropagateFailure()
            return res
        d_1021_derivedBranchKey_ = (d_1022_valueOrError2_).Extract()
        d_1023_maybeWrappedPdk_: Wrappers.Result
        out184_: Wrappers.Result
        out184_ = ((self).crypto).AESEncrypt(AwsCryptographyPrimitivesTypes.AESEncryptInput_AESEncryptInput(default__.AES__256__ENC__ALG, d_1017_nonce_, d_1021_derivedBranchKey_, (input).plaintextMaterial, d_1020_wrappingAad_))
        d_1023_maybeWrappedPdk_ = out184_
        d_1024_wrappedPdk_: AwsCryptographyPrimitivesTypes.AESEncryptOutput
        d_1025_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.AESEncryptOutput.default())()
        def lambda84_(d_1026_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1026_e_)

        d_1025_valueOrError3_ = (d_1023_maybeWrappedPdk_).MapFailure(lambda84_)
        if (d_1025_valueOrError3_).IsFailure():
            res = (d_1025_valueOrError3_).PropagateFailure()
            return res
        d_1024_wrappedPdk_ = (d_1025_valueOrError3_).Extract()
        d_1027_output_: MaterialWrapping.WrapOutput
        d_1027_output_ = MaterialWrapping.WrapOutput_WrapOutput(((((d_1016_salt_) + (d_1017_nonce_)) + ((self).branchKeyVersionAsBytes)) + ((d_1024_wrappedPdk_).cipherText)) + ((d_1024_wrappedPdk_).authTag), HierarchyWrapInfo_HierarchyWrapInfo())
        res = Wrappers.Result_Success(d_1027_output_)
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
