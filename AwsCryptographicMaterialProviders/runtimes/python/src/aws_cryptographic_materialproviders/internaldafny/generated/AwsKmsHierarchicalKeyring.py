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
        out147_: Wrappers.Result
        out147_ = (cmc).GetCacheEntry(input)
        res = out147_
        return res

    @staticmethod
    def putEntry(cmc, input):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out148_: Wrappers.Result
        out148_ = (cmc).PutCacheEntry(input)
        res = out148_
        return res

    @staticmethod
    def DeriveEncryptionKeyFromBranchKey(branchKey, salt, purpose, cryptoPrimitives):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_839_maybeDerivedBranchKey_: Wrappers.Result
        out149_: Wrappers.Result
        out149_ = (cryptoPrimitives).KdfCounterMode(AwsCryptographyPrimitivesTypes.KdfCtrInput_KdfCtrInput(AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__256(), branchKey, default__.DERIVED__BRANCH__KEY__EXPECTED__LENGTH, purpose, Wrappers.Option_Some(salt)))
        d_839_maybeDerivedBranchKey_ = out149_
        d_840_derivedBranchKey_: _dafny.Seq
        d_841_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda72_(d_842_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_842_e_)

        d_841_valueOrError0_ = (d_839_maybeDerivedBranchKey_).MapFailure(lambda72_)
        if (d_841_valueOrError0_).IsFailure():
            output = (d_841_valueOrError0_).PropagateFailure()
            return output
        d_840_derivedBranchKey_ = (d_841_valueOrError0_).Extract()
        output = Wrappers.Result_Success(d_840_derivedBranchKey_)
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
        out150_: Wrappers.Result
        out150_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnDecrypt(self, input)
        return out150_

    def OnEncrypt(self, input):
        out151_: Wrappers.Result
        out151_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnEncrypt(self, input)
        return out151_

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
            d_843_GetBranchKeyIdOut_: AwsCryptographyMaterialProvidersTypes.GetBranchKeyIdOutput
            d_844_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyMaterialProvidersTypes.GetBranchKeyIdOutput.default())()
            out152_: Wrappers.Result
            out152_ = (((self).branchKeyIdSupplier).value).GetBranchKeyId(AwsCryptographyMaterialProvidersTypes.GetBranchKeyIdInput_GetBranchKeyIdInput(context))
            d_844_valueOrError0_ = out152_
            if (d_844_valueOrError0_).IsFailure():
                ret = (d_844_valueOrError0_).PropagateFailure()
                return ret
            d_843_GetBranchKeyIdOut_ = (d_844_valueOrError0_).Extract()
            ret = Wrappers.Result_Success((d_843_GetBranchKeyIdOut_).branchKeyId)
            return ret
        return ret

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        d_845_materials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_845_materials_ = (input).materials
        d_846_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_846_suite_ = (d_845_materials_).algorithmSuite
        d_847_branchKeyIdForEncrypt_: _dafny.Seq
        d_848_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out153_: Wrappers.Result
        out153_ = (self).GetBranchKeyId((d_845_materials_).encryptionContext)
        d_848_valueOrError0_ = out153_
        if (d_848_valueOrError0_).IsFailure():
            res = (d_848_valueOrError0_).PropagateFailure()
            return res
        d_847_branchKeyIdForEncrypt_ = (d_848_valueOrError0_).Extract()
        d_849_branchKeyIdUtf8_: _dafny.Seq
        d_850_valueOrError1_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_850_valueOrError1_ = (UTF8.default__.Encode(d_847_branchKeyIdForEncrypt_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_850_valueOrError1_).IsFailure():
            res = (d_850_valueOrError1_).PropagateFailure()
            return res
        d_849_branchKeyIdUtf8_ = (d_850_valueOrError1_).Extract()
        d_851_cacheId_: _dafny.Seq
        d_852_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out154_: Wrappers.Result
        out154_ = (self).GetActiveCacheId(d_847_branchKeyIdForEncrypt_, d_849_branchKeyIdUtf8_, (self).cryptoPrimitives)
        d_852_valueOrError2_ = out154_
        if (d_852_valueOrError2_).IsFailure():
            res = (d_852_valueOrError2_).PropagateFailure()
            return res
        d_851_cacheId_ = (d_852_valueOrError2_).Extract()
        d_853_hierarchicalMaterials_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
        d_854_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.BranchKeyMaterials.default())()
        out155_: Wrappers.Result
        out155_ = (self).GetActiveHierarchicalMaterials(d_847_branchKeyIdForEncrypt_, d_851_cacheId_, (self).keyStore)
        d_854_valueOrError3_ = out155_
        if (d_854_valueOrError3_).IsFailure():
            res = (d_854_valueOrError3_).PropagateFailure()
            return res
        d_853_hierarchicalMaterials_ = (d_854_valueOrError3_).Extract()
        d_855_branchKey_: _dafny.Seq
        d_855_branchKey_ = (d_853_hierarchicalMaterials_).branchKey
        d_856_branchKeyVersion_: _dafny.Seq
        d_856_branchKeyVersion_ = (d_853_hierarchicalMaterials_).branchKeyVersion
        d_857_branchKeyVersionAsString_: _dafny.Seq
        d_858_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_858_valueOrError4_ = (UTF8.default__.Decode(d_856_branchKeyVersion_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_858_valueOrError4_).IsFailure():
            res = (d_858_valueOrError4_).PropagateFailure()
            return res
        d_857_branchKeyVersionAsString_ = (d_858_valueOrError4_).Extract()
        d_859_branchKeyVersionAsBytes_: _dafny.Seq
        d_860_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_860_valueOrError5_ = (UUID.default__.ToByteArray(d_857_branchKeyVersionAsString_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_860_valueOrError5_).IsFailure():
            res = (d_860_valueOrError5_).PropagateFailure()
            return res
        d_859_branchKeyVersionAsBytes_ = (d_860_valueOrError5_).Extract()
        d_861_kmsHierarchyGenerateAndWrap_: KmsHierarchyGenerateAndWrapKeyMaterial
        nw33_ = KmsHierarchyGenerateAndWrapKeyMaterial()
        nw33_.ctor__((d_853_hierarchicalMaterials_).branchKey, d_849_branchKeyIdUtf8_, d_859_branchKeyVersionAsBytes_, (self).cryptoPrimitives)
        d_861_kmsHierarchyGenerateAndWrap_ = nw33_
        d_862_kmsHierarchyWrap_: KmsHierarchyWrapKeyMaterial
        nw34_ = KmsHierarchyWrapKeyMaterial()
        nw34_.ctor__((d_853_hierarchicalMaterials_).branchKey, d_849_branchKeyIdUtf8_, d_859_branchKeyVersionAsBytes_, (self).cryptoPrimitives)
        d_862_kmsHierarchyWrap_ = nw34_
        d_863_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_864_valueOrError6_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.WrapEdkMaterialOutput.default(HierarchyWrapInfo.default()))()
        out156_: Wrappers.Result
        out156_ = EdkWrapping.default__.WrapEdkMaterial(d_845_materials_, d_862_kmsHierarchyWrap_, d_861_kmsHierarchyGenerateAndWrap_)
        d_864_valueOrError6_ = out156_
        if (d_864_valueOrError6_).IsFailure():
            res = (d_864_valueOrError6_).PropagateFailure()
            return res
        d_863_wrapOutput_ = (d_864_valueOrError6_).Extract()
        d_865_symmetricSigningKeyList_: Wrappers.Option
        d_865_symmetricSigningKeyList_ = (Wrappers.Option_Some(_dafny.Seq([((d_863_wrapOutput_).symmetricSigningKey).value])) if ((d_863_wrapOutput_).symmetricSigningKey).is_Some else Wrappers.Option_None())
        d_866_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_866_edk_ = AwsCryptographyMaterialProvidersTypes.EncryptedDataKey_EncryptedDataKey(Constants.default__.PROVIDER__ID__HIERARCHY, d_849_branchKeyIdUtf8_, (d_863_wrapOutput_).wrappedMaterial)
        if (d_863_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_867_result_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_868_valueOrError7_: Wrappers.Result = None
            d_868_valueOrError7_ = Materials.default__.EncryptionMaterialAddDataKey(d_845_materials_, (d_863_wrapOutput_).plaintextDataKey, _dafny.Seq([d_866_edk_]), d_865_symmetricSigningKeyList_)
            if (d_868_valueOrError7_).IsFailure():
                res = (d_868_valueOrError7_).PropagateFailure()
                return res
            d_867_result_ = (d_868_valueOrError7_).Extract()
            res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(d_867_result_))
            return res
        elif (d_863_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_869_result_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_870_valueOrError8_: Wrappers.Result = None
            d_870_valueOrError8_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys(d_845_materials_, _dafny.Seq([d_866_edk_]), d_865_symmetricSigningKeyList_)
            if (d_870_valueOrError8_).IsFailure():
                res = (d_870_valueOrError8_).PropagateFailure()
                return res
            d_869_result_ = (d_870_valueOrError8_).Extract()
            res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(d_869_result_))
            return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_871_materials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_871_materials_ = (input).materials
        d_872_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_872_suite_ = ((input).materials).algorithmSuite
        d_873_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_873_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_871_materials_), default__.E(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_873_valueOrError0_).IsFailure():
            res = (d_873_valueOrError0_).PropagateFailure()
            return res
        d_874_branchKeyIdForDecrypt_: _dafny.Seq
        d_875_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out157_: Wrappers.Result
        out157_ = (self).GetBranchKeyId((d_871_materials_).encryptionContext)
        d_875_valueOrError1_ = out157_
        if (d_875_valueOrError1_).IsFailure():
            res = (d_875_valueOrError1_).PropagateFailure()
            return res
        d_874_branchKeyIdForDecrypt_ = (d_875_valueOrError1_).Extract()
        d_876_filter_: OnDecryptHierarchyEncryptedDataKeyFilter
        nw35_ = OnDecryptHierarchyEncryptedDataKeyFilter()
        nw35_.ctor__(d_874_branchKeyIdForDecrypt_)
        d_876_filter_ = nw35_
        d_877_edksToAttempt_: _dafny.Seq
        d_878_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out158_: Wrappers.Result
        out158_ = Actions.default__.FilterWithResult(d_876_filter_, (input).encryptedDataKeys)
        d_878_valueOrError2_ = out158_
        if (d_878_valueOrError2_).IsFailure():
            res = (d_878_valueOrError2_).PropagateFailure()
            return res
        d_877_edksToAttempt_ = (d_878_valueOrError2_).Extract()
        if (0) == (len(d_877_edksToAttempt_)):
            d_879_errorMessage_: _dafny.Seq
            d_880_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            d_880_valueOrError3_ = ErrorMessages.default__.IncorrectDataKeys((input).encryptedDataKeys, ((input).materials).algorithmSuite, _dafny.Seq(""))
            if (d_880_valueOrError3_).IsFailure():
                res = (d_880_valueOrError3_).PropagateFailure()
                return res
            d_879_errorMessage_ = (d_880_valueOrError3_).Extract()
            res = Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_879_errorMessage_))
            return res
        d_881_decryptClosure_: Actions.ActionWithResult
        nw36_ = DecryptSingleEncryptedDataKey()
        nw36_.ctor__(d_871_materials_, (self).keyStore, (self).cryptoPrimitives, d_874_branchKeyIdForDecrypt_, (self).ttlSeconds, (self).cache)
        d_881_decryptClosure_ = nw36_
        d_882_outcome_: Wrappers.Result
        out159_: Wrappers.Result
        out159_ = Actions.default__.ReduceToSuccess(d_881_decryptClosure_, d_877_edksToAttempt_)
        d_882_outcome_ = out159_
        d_883_SealedDecryptionMaterials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_884_valueOrError4_: Wrappers.Result = None
        def lambda73_(d_885_errors_):
            return AwsCryptographyMaterialProvidersTypes.Error_CollectionOfErrors(d_885_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."))

        d_884_valueOrError4_ = (d_882_outcome_).MapFailure(lambda73_)
        if (d_884_valueOrError4_).IsFailure():
            res = (d_884_valueOrError4_).PropagateFailure()
            return res
        d_883_SealedDecryptionMaterials_ = (d_884_valueOrError4_).Extract()
        res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnDecryptOutput_OnDecryptOutput(d_883_SealedDecryptionMaterials_))
        return res
        return res

    def GetActiveCacheId(self, branchKeyId, branchKeyIdUtf8, cryptoPrimitives):
        cacheId: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_886_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        def iife26_(_pat_let8_0):
            def iife27_(d_887_branchKeyId_):
                return (True) and (((0) <= (len(d_887_branchKeyId_))) and ((len(d_887_branchKeyId_)) < (StandardLibrary_UInt.default__.UINT32__LIMIT)))
            return iife27_(_pat_let8_0)
        d_886_valueOrError0_ = Wrappers.default__.Need((((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).is_Success) and (iife26_(((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).value)), default__.E(_dafny.Seq("Invalid Branch Key ID Length")))
        if (d_886_valueOrError0_).IsFailure():
            cacheId = (d_886_valueOrError0_).PropagateFailure()
            return cacheId
        d_888_branchKeyId_: _dafny.Seq
        d_888_branchKeyId_ = (UTF8.default__.Decode(branchKeyIdUtf8)).value
        d_889_lenBranchKey_: _dafny.Seq
        d_889_lenBranchKey_ = StandardLibrary_UInt.default__.UInt32ToSeq(len(d_888_branchKeyId_))
        d_890_hashAlgorithm_: AwsCryptographyPrimitivesTypes.DigestAlgorithm
        d_890_hashAlgorithm_ = AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__512()
        d_891_maybeBranchKeyDigest_: Wrappers.Result
        out160_: Wrappers.Result
        out160_ = (cryptoPrimitives).Digest(AwsCryptographyPrimitivesTypes.DigestInput_DigestInput(d_890_hashAlgorithm_, branchKeyIdUtf8))
        d_891_maybeBranchKeyDigest_ = out160_
        d_892_branchKeyDigest_: _dafny.Seq
        d_893_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda74_(d_894_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_894_e_)

        d_893_valueOrError1_ = (d_891_maybeBranchKeyDigest_).MapFailure(lambda74_)
        if (d_893_valueOrError1_).IsFailure():
            cacheId = (d_893_valueOrError1_).PropagateFailure()
            return cacheId
        d_892_branchKeyDigest_ = (d_893_valueOrError1_).Extract()
        d_895_activeUtf8_: _dafny.Seq
        d_896_valueOrError2_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_896_valueOrError2_ = (UTF8.default__.Encode(default__.EXPRESSION__ATTRIBUTE__VALUE__STATUS__VALUE)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_896_valueOrError2_).IsFailure():
            cacheId = (d_896_valueOrError2_).PropagateFailure()
            return cacheId
        d_895_activeUtf8_ = (d_896_valueOrError2_).Extract()
        d_897_identifier_: _dafny.Seq
        d_897_identifier_ = (((d_889_lenBranchKey_) + (d_892_branchKeyDigest_)) + (_dafny.Seq([0]))) + (d_895_activeUtf8_)
        d_898_maybeCacheIdDigest_: Wrappers.Result
        out161_: Wrappers.Result
        out161_ = (cryptoPrimitives).Digest(AwsCryptographyPrimitivesTypes.DigestInput_DigestInput(d_890_hashAlgorithm_, d_897_identifier_))
        d_898_maybeCacheIdDigest_ = out161_
        d_899_cacheDigest_: _dafny.Seq
        d_900_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda75_(d_901_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_901_e_)

        d_900_valueOrError3_ = (d_898_maybeCacheIdDigest_).MapFailure(lambda75_)
        if (d_900_valueOrError3_).IsFailure():
            cacheId = (d_900_valueOrError3_).PropagateFailure()
            return cacheId
        d_899_cacheDigest_ = (d_900_valueOrError3_).Extract()
        d_902_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_902_valueOrError4_ = Wrappers.default__.Need((len(d_899_cacheDigest_)) == (Digest.default__.Length(d_890_hashAlgorithm_)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Digest generated a message not equal to the expected length.")))
        if (d_902_valueOrError4_).IsFailure():
            cacheId = (d_902_valueOrError4_).PropagateFailure()
            return cacheId
        cacheId = Wrappers.Result_Success(_dafny.Seq((d_899_cacheDigest_)[0:32:]))
        return cacheId
        return cacheId

    def GetActiveHierarchicalMaterials(self, branchKeyId, cacheId, keyStore):
        material: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.BranchKeyMaterials.default())()
        d_903_getCacheInput_: AwsCryptographyMaterialProvidersTypes.GetCacheEntryInput
        d_903_getCacheInput_ = AwsCryptographyMaterialProvidersTypes.GetCacheEntryInput_GetCacheEntryInput(cacheId, Wrappers.Option_None())
        d_904_getCacheOutput_: Wrappers.Result
        out162_: Wrappers.Result
        out162_ = default__.getEntry((self).cache, d_903_getCacheInput_)
        d_904_getCacheOutput_ = out162_
        if (d_904_getCacheOutput_).is_Failure:
            d_905_maybeGetActiveBranchKeyOutput_: Wrappers.Result
            out163_: Wrappers.Result
            out163_ = (keyStore).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(branchKeyId))
            d_905_maybeGetActiveBranchKeyOutput_ = out163_
            d_906_getActiveBranchKeyOutput_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
            d_907_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
            def lambda76_(d_908_e_):
                return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyKeyStore(d_908_e_)

            d_907_valueOrError0_ = (d_905_maybeGetActiveBranchKeyOutput_).MapFailure(lambda76_)
            if (d_907_valueOrError0_).IsFailure():
                material = (d_907_valueOrError0_).PropagateFailure()
                return material
            d_906_getActiveBranchKeyOutput_ = (d_907_valueOrError0_).Extract()
            d_909_branchKeyMaterials_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
            d_909_branchKeyMaterials_ = (d_906_getActiveBranchKeyOutput_).branchKeyMaterials
            d_910_now_: int
            out164_: int
            out164_ = Time.default__.CurrentRelativeTime()
            d_910_now_ = out164_
            d_911_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_911_valueOrError1_ = Wrappers.default__.Need(((d_910_now_) + ((self).ttlSeconds)) < (StandardLibrary_UInt.default__.INT64__MAX__LIMIT), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("INT64 Overflow when putting cache entry.")))
            if (d_911_valueOrError1_).IsFailure():
                material = (d_911_valueOrError1_).PropagateFailure()
                return material
            d_912_putCacheEntryInput_: AwsCryptographyMaterialProvidersTypes.PutCacheEntryInput
            d_912_putCacheEntryInput_ = AwsCryptographyMaterialProvidersTypes.PutCacheEntryInput_PutCacheEntryInput(cacheId, AwsCryptographyMaterialProvidersTypes.Materials_BranchKey(d_909_branchKeyMaterials_), d_910_now_, ((self).ttlSeconds) + (d_910_now_), Wrappers.Option_None(), Wrappers.Option_None())
            d_913___v0_: tuple
            d_914_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            out165_: Wrappers.Result
            out165_ = default__.putEntry((self).cache, d_912_putCacheEntryInput_)
            d_914_valueOrError2_ = out165_
            if (d_914_valueOrError2_).IsFailure():
                material = (d_914_valueOrError2_).PropagateFailure()
                return material
            d_913___v0_ = (d_914_valueOrError2_).Extract()
            material = Wrappers.Result_Success(d_909_branchKeyMaterials_)
            return material
        elif True:
            d_915_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_915_valueOrError3_ = Wrappers.default__.Need(((((d_904_getCacheOutput_).value).materials).is_BranchKey) and ((((d_904_getCacheOutput_).value).materials) == (AwsCryptographyMaterialProvidersTypes.Materials_BranchKey((((d_904_getCacheOutput_).value).materials).BranchKey))), default__.E(_dafny.Seq("Invalid Material Type.")))
            if (d_915_valueOrError3_).IsFailure():
                material = (d_915_valueOrError3_).PropagateFailure()
                return material
            material = Wrappers.Result_Success((((d_904_getCacheOutput_).value).materials).BranchKey)
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
        d_916_providerInfo_: _dafny.Seq
        d_916_providerInfo_ = (edk).keyProviderInfo
        d_917_providerId_: _dafny.Seq
        d_917_providerId_ = (edk).keyProviderId
        if (d_917_providerId_) != (Constants.default__.PROVIDER__ID__HIERARCHY):
            res = Wrappers.Result_Success(False)
            return res
        if not(UTF8.default__.ValidUTF8Seq(d_916_providerInfo_)):
            res = Wrappers.Result_Failure(default__.E(_dafny.Seq("Invalid encoding, provider info is not UTF8.")))
            return res
        d_918_branchKeyId_: _dafny.Seq
        d_919_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_919_valueOrError0_ = (UTF8.default__.Decode(d_916_providerInfo_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_919_valueOrError0_).IsFailure():
            res = (d_919_valueOrError0_).PropagateFailure()
            return res
        d_918_branchKeyId_ = (d_919_valueOrError0_).Extract()
        res = Wrappers.Result_Success(((self).branchKeyId) == (d_918_branchKeyId_))
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
        d_920_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_920_valueOrError0_ = Wrappers.default__.Need(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received invalid EDK provider info for Hierarchical Keyring")))
        if (d_920_valueOrError0_).IsFailure():
            res = (d_920_valueOrError0_).PropagateFailure()
            return res
        d_921_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_921_suite_ = ((self).materials).algorithmSuite
        d_922_keyProviderId_: _dafny.Seq
        d_922_keyProviderId_ = (edk).keyProviderId
        d_923_branchKeyIdUtf8_: _dafny.Seq
        d_923_branchKeyIdUtf8_ = (edk).keyProviderInfo
        d_924_ciphertext_: _dafny.Seq
        d_924_ciphertext_ = (edk).ciphertext
        d_925_providerWrappedMaterial_: _dafny.Seq
        d_926_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_926_valueOrError1_ = EdkWrapping.default__.GetProviderWrappedMaterial(d_924_ciphertext_, d_921_suite_)
        if (d_926_valueOrError1_).IsFailure():
            res = (d_926_valueOrError1_).PropagateFailure()
            return res
        d_925_providerWrappedMaterial_ = (d_926_valueOrError1_).Extract()
        d_927_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_927_valueOrError2_ = Wrappers.default__.Need((len(d_925_providerWrappedMaterial_)) >= (default__.EDK__CIPHERTEXT__VERSION__INDEX), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received EDK Ciphertext of incorrect length.")))
        if (d_927_valueOrError2_).IsFailure():
            res = (d_927_valueOrError2_).PropagateFailure()
            return res
        d_928_branchKeyVersionUuid_: _dafny.Seq
        d_928_branchKeyVersionUuid_ = _dafny.Seq((d_925_providerWrappedMaterial_)[default__.EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX:default__.EDK__CIPHERTEXT__VERSION__INDEX:])
        d_929_version_: _dafny.Seq
        d_930_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_930_valueOrError3_ = (UUID.default__.FromByteArray(d_928_branchKeyVersionUuid_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_930_valueOrError3_).IsFailure():
            res = (d_930_valueOrError3_).PropagateFailure()
            return res
        d_929_version_ = (d_930_valueOrError3_).Extract()
        d_931_cacheId_: _dafny.Seq
        d_932_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out166_: Wrappers.Result
        out166_ = (self).GetVersionCacheId(d_923_branchKeyIdUtf8_, d_929_version_, (self).cryptoPrimitives)
        d_932_valueOrError4_ = out166_
        if (d_932_valueOrError4_).IsFailure():
            res = (d_932_valueOrError4_).PropagateFailure()
            return res
        d_931_cacheId_ = (d_932_valueOrError4_).Extract()
        d_933_hierarchicalMaterials_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
        d_934_valueOrError5_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.BranchKeyMaterials.default())()
        out167_: Wrappers.Result
        out167_ = (self).GetHierarchicalMaterialsVersion((self).branchKeyId, d_923_branchKeyIdUtf8_, d_929_version_, d_931_cacheId_)
        d_934_valueOrError5_ = out167_
        if (d_934_valueOrError5_).IsFailure():
            res = (d_934_valueOrError5_).PropagateFailure()
            return res
        d_933_hierarchicalMaterials_ = (d_934_valueOrError5_).Extract()
        d_935_branchKey_: _dafny.Seq
        d_935_branchKey_ = (d_933_hierarchicalMaterials_).branchKey
        d_936_branchKeyVersion_: _dafny.Seq
        d_936_branchKeyVersion_ = (d_933_hierarchicalMaterials_).branchKeyVersion
        d_937_branchKeyVersionAsString_: _dafny.Seq
        d_938_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_938_valueOrError6_ = (UTF8.default__.Decode(d_936_branchKeyVersion_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_938_valueOrError6_).IsFailure():
            res = (d_938_valueOrError6_).PropagateFailure()
            return res
        d_937_branchKeyVersionAsString_ = (d_938_valueOrError6_).Extract()
        d_939_branchKeyVersionAsBytes_: _dafny.Seq
        d_940_valueOrError7_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_940_valueOrError7_ = (UUID.default__.ToByteArray(d_937_branchKeyVersionAsString_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_940_valueOrError7_).IsFailure():
            res = (d_940_valueOrError7_).PropagateFailure()
            return res
        d_939_branchKeyVersionAsBytes_ = (d_940_valueOrError7_).Extract()
        d_941_maybeCrypto_: Wrappers.Result
        out168_: Wrappers.Result
        out168_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_941_maybeCrypto_ = out168_
        d_942_cryptoPrimitivesX_: AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient
        d_943_valueOrError8_: Wrappers.Result = None
        def lambda77_(d_944_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_944_e_)

        d_943_valueOrError8_ = (d_941_maybeCrypto_).MapFailure(lambda77_)
        if (d_943_valueOrError8_).IsFailure():
            res = (d_943_valueOrError8_).PropagateFailure()
            return res
        d_942_cryptoPrimitivesX_ = (d_943_valueOrError8_).Extract()
        d_945_cryptoPrimitives_: AtomicPrimitives.AtomicPrimitivesClient
        d_945_cryptoPrimitives_ = d_942_cryptoPrimitivesX_
        d_946_kmsHierarchyUnwrap_: KmsHierarchyUnwrapKeyMaterial
        nw37_ = KmsHierarchyUnwrapKeyMaterial()
        nw37_.ctor__(d_935_branchKey_, d_923_branchKeyIdUtf8_, d_939_branchKeyVersionAsBytes_, d_945_cryptoPrimitives_)
        d_946_kmsHierarchyUnwrap_ = nw37_
        d_947_unwrapOutputRes_: Wrappers.Result
        out169_: Wrappers.Result
        out169_ = EdkWrapping.default__.UnwrapEdkMaterial((edk).ciphertext, (self).materials, d_946_kmsHierarchyUnwrap_)
        d_947_unwrapOutputRes_ = out169_
        d_948_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_949_valueOrError9_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.UnwrapEdkMaterialOutput.default(HierarchyUnwrapInfo.default()))()
        d_949_valueOrError9_ = d_947_unwrapOutputRes_
        if (d_949_valueOrError9_).IsFailure():
            res = (d_949_valueOrError9_).PropagateFailure()
            return res
        d_948_unwrapOutput_ = (d_949_valueOrError9_).Extract()
        d_950_result_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_951_valueOrError10_: Wrappers.Result = None
        d_951_valueOrError10_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_948_unwrapOutput_).plaintextDataKey, (d_948_unwrapOutput_).symmetricSigningKey)
        if (d_951_valueOrError10_).IsFailure():
            res = (d_951_valueOrError10_).PropagateFailure()
            return res
        d_950_result_ = (d_951_valueOrError10_).Extract()
        res = Wrappers.Result_Success(d_950_result_)
        return res
        return res

    def GetVersionCacheId(self, branchKeyIdUtf8, branchKeyVersion, cryptoPrimitives):
        cacheId: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_952_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        def iife28_(_pat_let9_0):
            def iife29_(d_953_branchKeyId_):
                return (True) and (((0) <= (len(d_953_branchKeyId_))) and ((len(d_953_branchKeyId_)) < (StandardLibrary_UInt.default__.UINT32__LIMIT)))
            return iife29_(_pat_let9_0)
        d_952_valueOrError0_ = Wrappers.default__.Need((((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).is_Success) and (iife28_(((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).value)), default__.E(_dafny.Seq("Invalid Branch Key ID Length")))
        if (d_952_valueOrError0_).IsFailure():
            cacheId = (d_952_valueOrError0_).PropagateFailure()
            return cacheId
        d_954_branchKeyId_: _dafny.Seq
        d_954_branchKeyId_ = (UTF8.default__.Decode(branchKeyIdUtf8)).value
        d_955_lenBranchKey_: _dafny.Seq
        d_955_lenBranchKey_ = StandardLibrary_UInt.default__.UInt32ToSeq(len(d_954_branchKeyId_))
        d_956_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_956_valueOrError1_ = Wrappers.default__.Need(UTF8.default__.IsASCIIString(branchKeyVersion), default__.E(_dafny.Seq("Unable to represent as an ASCII string.")))
        if (d_956_valueOrError1_).IsFailure():
            cacheId = (d_956_valueOrError1_).PropagateFailure()
            return cacheId
        d_957_versionBytes_: _dafny.Seq
        d_957_versionBytes_ = UTF8.default__.EncodeAscii(branchKeyVersion)
        d_958_identifier_: _dafny.Seq
        d_958_identifier_ = (((d_955_lenBranchKey_) + (branchKeyIdUtf8)) + (_dafny.Seq([0]))) + (d_957_versionBytes_)
        d_959_identifierDigestInput_: AwsCryptographyPrimitivesTypes.DigestInput
        d_959_identifierDigestInput_ = AwsCryptographyPrimitivesTypes.DigestInput_DigestInput(AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__512(), d_958_identifier_)
        d_960_maybeCacheDigest_: Wrappers.Result
        out170_: Wrappers.Result
        out170_ = Digest.default__.Digest(d_959_identifierDigestInput_)
        d_960_maybeCacheDigest_ = out170_
        d_961_cacheDigest_: _dafny.Seq
        d_962_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda78_(d_963_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_963_e_)

        d_962_valueOrError2_ = (d_960_maybeCacheDigest_).MapFailure(lambda78_)
        if (d_962_valueOrError2_).IsFailure():
            cacheId = (d_962_valueOrError2_).PropagateFailure()
            return cacheId
        d_961_cacheDigest_ = (d_962_valueOrError2_).Extract()
        cacheId = Wrappers.Result_Success(_dafny.Seq((d_961_cacheDigest_)[0:32:]))
        return cacheId
        return cacheId

    def GetHierarchicalMaterialsVersion(self, branchKeyId, branchKeyIdUtf8, version, cacheId):
        material: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.BranchKeyMaterials.default())()
        d_964_getCacheInput_: AwsCryptographyMaterialProvidersTypes.GetCacheEntryInput
        d_964_getCacheInput_ = AwsCryptographyMaterialProvidersTypes.GetCacheEntryInput_GetCacheEntryInput(cacheId, Wrappers.Option_None())
        d_965_getCacheOutput_: Wrappers.Result
        out171_: Wrappers.Result
        out171_ = default__.getEntry((self).cache, d_964_getCacheInput_)
        d_965_getCacheOutput_ = out171_
        if (d_965_getCacheOutput_).is_Failure:
            d_966_maybeGetBranchKeyVersionOutput_: Wrappers.Result
            out172_: Wrappers.Result
            out172_ = ((self).keyStore).GetBranchKeyVersion(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput_GetBranchKeyVersionInput(branchKeyId, version))
            d_966_maybeGetBranchKeyVersionOutput_ = out172_
            d_967_getBranchKeyVersionOutput_: AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
            d_968_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
            def lambda79_(d_969_e_):
                return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyKeyStore(d_969_e_)

            d_968_valueOrError0_ = (d_966_maybeGetBranchKeyVersionOutput_).MapFailure(lambda79_)
            if (d_968_valueOrError0_).IsFailure():
                material = (d_968_valueOrError0_).PropagateFailure()
                return material
            d_967_getBranchKeyVersionOutput_ = (d_968_valueOrError0_).Extract()
            d_970_branchKeyMaterials_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
            d_970_branchKeyMaterials_ = (d_967_getBranchKeyVersionOutput_).branchKeyMaterials
            d_971_now_: int
            out173_: int
            out173_ = Time.default__.CurrentRelativeTime()
            d_971_now_ = out173_
            d_972_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_972_valueOrError1_ = Wrappers.default__.Need(((d_971_now_) + ((self).ttlSeconds)) < (StandardLibrary_UInt.default__.INT64__MAX__LIMIT), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("INT64 Overflow when putting cache entry.")))
            if (d_972_valueOrError1_).IsFailure():
                material = (d_972_valueOrError1_).PropagateFailure()
                return material
            d_973_putCacheEntryInput_: AwsCryptographyMaterialProvidersTypes.PutCacheEntryInput
            d_973_putCacheEntryInput_ = AwsCryptographyMaterialProvidersTypes.PutCacheEntryInput_PutCacheEntryInput(cacheId, AwsCryptographyMaterialProvidersTypes.Materials_BranchKey(d_970_branchKeyMaterials_), d_971_now_, ((self).ttlSeconds) + (d_971_now_), Wrappers.Option_None(), Wrappers.Option_None())
            d_974___v1_: tuple
            d_975_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            out174_: Wrappers.Result
            out174_ = default__.putEntry((self).cache, d_973_putCacheEntryInput_)
            d_975_valueOrError2_ = out174_
            if (d_975_valueOrError2_).IsFailure():
                material = (d_975_valueOrError2_).PropagateFailure()
                return material
            d_974___v1_ = (d_975_valueOrError2_).Extract()
            material = Wrappers.Result_Success(d_970_branchKeyMaterials_)
            return material
        elif True:
            d_976_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_976_valueOrError3_ = Wrappers.default__.Need(((((d_965_getCacheOutput_).value).materials).is_BranchKey) and ((((d_965_getCacheOutput_).value).materials) == (AwsCryptographyMaterialProvidersTypes.Materials_BranchKey((((d_965_getCacheOutput_).value).materials).BranchKey))), default__.E(_dafny.Seq("Invalid Material Type.")))
            if (d_976_valueOrError3_).IsFailure():
                material = (d_976_valueOrError3_).PropagateFailure()
                return material
            material = Wrappers.Result_Success((((d_965_getCacheOutput_).value).materials).BranchKey)
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
        d_977_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_977_suite_ = (input).algorithmSuite
        d_978_wrappedMaterial_: _dafny.Seq
        d_978_wrappedMaterial_ = (input).wrappedMaterial
        d_979_aad_: _dafny.Map
        d_979_aad_ = (input).encryptionContext
        d_980_KeyLength_: int
        d_980_KeyLength_ = AlgorithmSuites.default__.GetEncryptKeyLength(d_977_suite_)
        d_981_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_981_valueOrError0_ = Wrappers.default__.Need((len(d_978_wrappedMaterial_)) == ((default__.EXPECTED__EDK__CIPHERTEXT__OVERHEAD) + (d_980_KeyLength_)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received EDK Ciphertext of incorrect length2.")))
        if (d_981_valueOrError0_).IsFailure():
            res = (d_981_valueOrError0_).PropagateFailure()
            return res
        d_982_salt_: _dafny.Seq
        d_982_salt_ = _dafny.Seq((d_978_wrappedMaterial_)[0:default__.H__WRAP__SALT__LEN:])
        d_983_iv_: _dafny.Seq
        d_983_iv_ = _dafny.Seq((d_978_wrappedMaterial_)[default__.H__WRAP__SALT__LEN:default__.EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX:])
        d_984_branchKeyVersionUuid_: _dafny.Seq
        d_984_branchKeyVersionUuid_ = _dafny.Seq((d_978_wrappedMaterial_)[default__.EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX:default__.EDK__CIPHERTEXT__VERSION__INDEX:])
        d_985_wrappedKey_: _dafny.Seq
        d_985_wrappedKey_ = _dafny.Seq((d_978_wrappedMaterial_)[default__.EDK__CIPHERTEXT__VERSION__INDEX:(default__.EDK__CIPHERTEXT__VERSION__INDEX) + (d_980_KeyLength_):])
        d_986_authTag_: _dafny.Seq
        d_986_authTag_ = _dafny.Seq((d_978_wrappedMaterial_)[(default__.EDK__CIPHERTEXT__VERSION__INDEX) + (d_980_KeyLength_)::])
        d_987_serializedEC_: _dafny.Seq
        d_988_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_988_valueOrError1_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_988_valueOrError1_).IsFailure():
            res = (d_988_valueOrError1_).PropagateFailure()
            return res
        d_987_serializedEC_ = (d_988_valueOrError1_).Extract()
        d_989_wrappingAad_: _dafny.Seq
        d_989_wrappingAad_ = default__.WrappingAad((self).branchKeyIdUtf8, (self).branchKeyVersionAsBytes, d_987_serializedEC_)
        d_990_derivedBranchKey_: _dafny.Seq
        d_991_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out175_: Wrappers.Result
        out175_ = default__.DeriveEncryptionKeyFromBranchKey((self).branchKey, d_982_salt_, Wrappers.Option_Some(Constants.default__.PROVIDER__ID__HIERARCHY), (self).crypto)
        d_991_valueOrError2_ = out175_
        if (d_991_valueOrError2_).IsFailure():
            res = (d_991_valueOrError2_).PropagateFailure()
            return res
        d_990_derivedBranchKey_ = (d_991_valueOrError2_).Extract()
        d_992_maybeUnwrappedPdk_: Wrappers.Result
        out176_: Wrappers.Result
        out176_ = ((self).crypto).AESDecrypt(AwsCryptographyPrimitivesTypes.AESDecryptInput_AESDecryptInput(default__.AES__256__ENC__ALG, d_990_derivedBranchKey_, d_985_wrappedKey_, d_986_authTag_, d_983_iv_, d_989_wrappingAad_))
        d_992_maybeUnwrappedPdk_ = out176_
        d_993_unwrappedPdk_: _dafny.Seq
        d_994_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda80_(d_995_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_995_e_)

        d_994_valueOrError3_ = (d_992_maybeUnwrappedPdk_).MapFailure(lambda80_)
        if (d_994_valueOrError3_).IsFailure():
            res = (d_994_valueOrError3_).PropagateFailure()
            return res
        d_993_unwrappedPdk_ = (d_994_valueOrError3_).Extract()
        d_996_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_996_valueOrError4_ = Wrappers.default__.Need((len(d_993_unwrappedPdk_)) == (AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)), default__.E(_dafny.Seq("Invalid Key Length")))
        if (d_996_valueOrError4_).IsFailure():
            res = (d_996_valueOrError4_).PropagateFailure()
            return res
        d_997_output_: MaterialWrapping.UnwrapOutput
        d_997_output_ = MaterialWrapping.UnwrapOutput_UnwrapOutput(d_993_unwrappedPdk_, HierarchyUnwrapInfo_HierarchyUnwrapInfo())
        res = Wrappers.Result_Success(d_997_output_)
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
        d_998_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_998_suite_ = (input).algorithmSuite
        d_999_pdkResult_: Wrappers.Result
        out177_: Wrappers.Result
        out177_ = ((self).crypto).GenerateRandomBytes(AwsCryptographyPrimitivesTypes.GenerateRandomBytesInput_GenerateRandomBytesInput(AlgorithmSuites.default__.GetEncryptKeyLength(d_998_suite_)))
        d_999_pdkResult_ = out177_
        d_1000_pdk_: _dafny.Seq
        d_1001_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda81_(d_1002_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1002_e_)

        d_1001_valueOrError0_ = (d_999_pdkResult_).MapFailure(lambda81_)
        if (d_1001_valueOrError0_).IsFailure():
            res = (d_1001_valueOrError0_).PropagateFailure()
            return res
        d_1000_pdk_ = (d_1001_valueOrError0_).Extract()
        d_1003_wrap_: KmsHierarchyWrapKeyMaterial
        nw38_ = KmsHierarchyWrapKeyMaterial()
        nw38_.ctor__((self).branchKey, (self).branchKeyIdUtf8, (self).branchKeyVersionAsBytes, (self).crypto)
        d_1003_wrap_ = nw38_
        d_1004_wrapOutput_: MaterialWrapping.WrapOutput
        d_1005_valueOrError1_: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.WrapOutput.default(HierarchyWrapInfo.default()))()
        out178_: Wrappers.Result
        out178_ = (d_1003_wrap_).Invoke(MaterialWrapping.WrapInput_WrapInput(d_1000_pdk_, (input).algorithmSuite, (input).encryptionContext))
        d_1005_valueOrError1_ = out178_
        if (d_1005_valueOrError1_).IsFailure():
            res = (d_1005_valueOrError1_).PropagateFailure()
            return res
        d_1004_wrapOutput_ = (d_1005_valueOrError1_).Extract()
        d_1006_output_: MaterialWrapping.GenerateAndWrapOutput
        d_1006_output_ = MaterialWrapping.GenerateAndWrapOutput_GenerateAndWrapOutput(d_1000_pdk_, (d_1004_wrapOutput_).wrappedMaterial, HierarchyWrapInfo_HierarchyWrapInfo())
        res = Wrappers.Result_Success(d_1006_output_)
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
        d_1007_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_1007_suite_ = (input).algorithmSuite
        d_1008_maybeNonceSalt_: Wrappers.Result
        out179_: Wrappers.Result
        out179_ = ((self).crypto).GenerateRandomBytes(AwsCryptographyPrimitivesTypes.GenerateRandomBytesInput_GenerateRandomBytesInput((default__.H__WRAP__SALT__LEN) + (default__.H__WRAP__NONCE__LEN)))
        d_1008_maybeNonceSalt_ = out179_
        d_1009_saltAndNonce_: _dafny.Seq
        d_1010_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda82_(d_1011_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1011_e_)

        d_1010_valueOrError0_ = (d_1008_maybeNonceSalt_).MapFailure(lambda82_)
        if (d_1010_valueOrError0_).IsFailure():
            res = (d_1010_valueOrError0_).PropagateFailure()
            return res
        d_1009_saltAndNonce_ = (d_1010_valueOrError0_).Extract()
        d_1012_salt_: _dafny.Seq
        d_1012_salt_ = _dafny.Seq((d_1009_saltAndNonce_)[0:default__.H__WRAP__SALT__LEN:])
        d_1013_nonce_: _dafny.Seq
        d_1013_nonce_ = _dafny.Seq((d_1009_saltAndNonce_)[default__.H__WRAP__SALT__LEN::])
        d_1014_serializedEC_: _dafny.Seq
        d_1015_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1015_valueOrError1_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_1015_valueOrError1_).IsFailure():
            res = (d_1015_valueOrError1_).PropagateFailure()
            return res
        d_1014_serializedEC_ = (d_1015_valueOrError1_).Extract()
        d_1016_wrappingAad_: _dafny.Seq
        d_1016_wrappingAad_ = default__.WrappingAad((self).branchKeyIdUtf8, (self).branchKeyVersionAsBytes, d_1014_serializedEC_)
        d_1017_derivedBranchKey_: _dafny.Seq
        d_1018_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out180_: Wrappers.Result
        out180_ = default__.DeriveEncryptionKeyFromBranchKey((self).branchKey, d_1012_salt_, Wrappers.Option_Some(Constants.default__.PROVIDER__ID__HIERARCHY), (self).crypto)
        d_1018_valueOrError2_ = out180_
        if (d_1018_valueOrError2_).IsFailure():
            res = (d_1018_valueOrError2_).PropagateFailure()
            return res
        d_1017_derivedBranchKey_ = (d_1018_valueOrError2_).Extract()
        d_1019_maybeWrappedPdk_: Wrappers.Result
        out181_: Wrappers.Result
        out181_ = ((self).crypto).AESEncrypt(AwsCryptographyPrimitivesTypes.AESEncryptInput_AESEncryptInput(default__.AES__256__ENC__ALG, d_1013_nonce_, d_1017_derivedBranchKey_, (input).plaintextMaterial, d_1016_wrappingAad_))
        d_1019_maybeWrappedPdk_ = out181_
        d_1020_wrappedPdk_: AwsCryptographyPrimitivesTypes.AESEncryptOutput
        d_1021_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.AESEncryptOutput.default())()
        def lambda83_(d_1022_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1022_e_)

        d_1021_valueOrError3_ = (d_1019_maybeWrappedPdk_).MapFailure(lambda83_)
        if (d_1021_valueOrError3_).IsFailure():
            res = (d_1021_valueOrError3_).PropagateFailure()
            return res
        d_1020_wrappedPdk_ = (d_1021_valueOrError3_).Extract()
        d_1023_output_: MaterialWrapping.WrapOutput
        d_1023_output_ = MaterialWrapping.WrapOutput_WrapOutput(((((d_1012_salt_) + (d_1013_nonce_)) + ((self).branchKeyVersionAsBytes)) + ((d_1020_wrappedPdk_).cipherText)) + ((d_1020_wrappedPdk_).authTag), HierarchyWrapInfo_HierarchyWrapInfo())
        res = Wrappers.Result_Success(d_1023_output_)
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
