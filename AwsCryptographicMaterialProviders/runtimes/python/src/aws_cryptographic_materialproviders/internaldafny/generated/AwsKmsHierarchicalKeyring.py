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
import com_amazonaws_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import com_amazonaws_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
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
import aws_cryptography_primitives.internaldafny.generated.Aws_Cryptography_Primitives as Aws_Cryptography_Primitives
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
        out148_: Wrappers.Result
        out148_ = (cmc).GetCacheEntry(input)
        res = out148_
        return res

    @staticmethod
    def putEntry(cmc, input):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        out149_: Wrappers.Result
        out149_ = (cmc).PutCacheEntry(input)
        res = out149_
        return res

    @staticmethod
    def DeriveEncryptionKeyFromBranchKey(branchKey, salt, purpose, cryptoPrimitives):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_841_maybeDerivedBranchKey_: Wrappers.Result
        out150_: Wrappers.Result
        out150_ = (cryptoPrimitives).KdfCounterMode(AwsCryptographyPrimitivesTypes.KdfCtrInput_KdfCtrInput(AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__256(), branchKey, default__.DERIVED__BRANCH__KEY__EXPECTED__LENGTH, purpose, Wrappers.Option_Some(salt)))
        d_841_maybeDerivedBranchKey_ = out150_
        d_842_derivedBranchKey_: _dafny.Seq
        d_843_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda73_(d_844_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_844_e_)

        d_843_valueOrError0_ = (d_841_maybeDerivedBranchKey_).MapFailure(lambda73_)
        if (d_843_valueOrError0_).IsFailure():
            output = (d_843_valueOrError0_).PropagateFailure()
            return output
        d_842_derivedBranchKey_ = (d_843_valueOrError0_).Extract()
        output = Wrappers.Result_Success(d_842_derivedBranchKey_)
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
        self._cryptoPrimitives: Aws_Cryptography_Primitives.AtomicPrimitivesClient = None
        self._branchKeyIdSupplier: Wrappers.Option = Wrappers.Option.default()()
        self._branchKeyId: Wrappers.Option = Wrappers.Option.default()()
        self._ttlSeconds: int = None
        self._cache: AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsCache = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsHierarchicalKeyring.AwsKmsHierarchicalKeyring"
    def OnDecrypt(self, input):
        out151_: Wrappers.Result
        out151_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnDecrypt(self, input)
        return out151_

    def OnEncrypt(self, input):
        out152_: Wrappers.Result
        out152_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnEncrypt(self, input)
        return out152_

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
            d_845_GetBranchKeyIdOut_: AwsCryptographyMaterialProvidersTypes.GetBranchKeyIdOutput
            d_846_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyMaterialProvidersTypes.GetBranchKeyIdOutput.default())()
            out153_: Wrappers.Result
            out153_ = (((self).branchKeyIdSupplier).value).GetBranchKeyId(AwsCryptographyMaterialProvidersTypes.GetBranchKeyIdInput_GetBranchKeyIdInput(context))
            d_846_valueOrError0_ = out153_
            if (d_846_valueOrError0_).IsFailure():
                ret = (d_846_valueOrError0_).PropagateFailure()
                return ret
            d_845_GetBranchKeyIdOut_ = (d_846_valueOrError0_).Extract()
            ret = Wrappers.Result_Success((d_845_GetBranchKeyIdOut_).branchKeyId)
            return ret
        return ret

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        d_847_materials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_847_materials_ = (input).materials
        d_848_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_848_suite_ = (d_847_materials_).algorithmSuite
        d_849_branchKeyIdForEncrypt_: _dafny.Seq
        d_850_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out154_: Wrappers.Result
        out154_ = (self).GetBranchKeyId((d_847_materials_).encryptionContext)
        d_850_valueOrError0_ = out154_
        if (d_850_valueOrError0_).IsFailure():
            res = (d_850_valueOrError0_).PropagateFailure()
            return res
        d_849_branchKeyIdForEncrypt_ = (d_850_valueOrError0_).Extract()
        d_851_branchKeyIdUtf8_: _dafny.Seq
        d_852_valueOrError1_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_852_valueOrError1_ = (UTF8.default__.Encode(d_849_branchKeyIdForEncrypt_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_852_valueOrError1_).IsFailure():
            res = (d_852_valueOrError1_).PropagateFailure()
            return res
        d_851_branchKeyIdUtf8_ = (d_852_valueOrError1_).Extract()
        d_853_cacheId_: _dafny.Seq
        d_854_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out155_: Wrappers.Result
        out155_ = (self).GetActiveCacheId(d_849_branchKeyIdForEncrypt_, d_851_branchKeyIdUtf8_, (self).cryptoPrimitives)
        d_854_valueOrError2_ = out155_
        if (d_854_valueOrError2_).IsFailure():
            res = (d_854_valueOrError2_).PropagateFailure()
            return res
        d_853_cacheId_ = (d_854_valueOrError2_).Extract()
        d_855_hierarchicalMaterials_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
        d_856_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.BranchKeyMaterials.default())()
        out156_: Wrappers.Result
        out156_ = (self).GetActiveHierarchicalMaterials(d_849_branchKeyIdForEncrypt_, d_853_cacheId_, (self).keyStore)
        d_856_valueOrError3_ = out156_
        if (d_856_valueOrError3_).IsFailure():
            res = (d_856_valueOrError3_).PropagateFailure()
            return res
        d_855_hierarchicalMaterials_ = (d_856_valueOrError3_).Extract()
        d_857_branchKey_: _dafny.Seq
        d_857_branchKey_ = (d_855_hierarchicalMaterials_).branchKey
        d_858_branchKeyVersion_: _dafny.Seq
        d_858_branchKeyVersion_ = (d_855_hierarchicalMaterials_).branchKeyVersion
        d_859_branchKeyVersionAsString_: _dafny.Seq
        d_860_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_860_valueOrError4_ = (UTF8.default__.Decode(d_858_branchKeyVersion_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_860_valueOrError4_).IsFailure():
            res = (d_860_valueOrError4_).PropagateFailure()
            return res
        d_859_branchKeyVersionAsString_ = (d_860_valueOrError4_).Extract()
        d_861_branchKeyVersionAsBytes_: _dafny.Seq
        d_862_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_862_valueOrError5_ = (UUID.default__.ToByteArray(d_859_branchKeyVersionAsString_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_862_valueOrError5_).IsFailure():
            res = (d_862_valueOrError5_).PropagateFailure()
            return res
        d_861_branchKeyVersionAsBytes_ = (d_862_valueOrError5_).Extract()
        d_863_kmsHierarchyGenerateAndWrap_: KmsHierarchyGenerateAndWrapKeyMaterial
        nw33_ = KmsHierarchyGenerateAndWrapKeyMaterial()
        nw33_.ctor__((d_855_hierarchicalMaterials_).branchKey, d_851_branchKeyIdUtf8_, d_861_branchKeyVersionAsBytes_, (self).cryptoPrimitives)
        d_863_kmsHierarchyGenerateAndWrap_ = nw33_
        d_864_kmsHierarchyWrap_: KmsHierarchyWrapKeyMaterial
        nw34_ = KmsHierarchyWrapKeyMaterial()
        nw34_.ctor__((d_855_hierarchicalMaterials_).branchKey, d_851_branchKeyIdUtf8_, d_861_branchKeyVersionAsBytes_, (self).cryptoPrimitives)
        d_864_kmsHierarchyWrap_ = nw34_
        d_865_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_866_valueOrError6_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.WrapEdkMaterialOutput.default(HierarchyWrapInfo.default()))()
        out157_: Wrappers.Result
        out157_ = EdkWrapping.default__.WrapEdkMaterial(d_847_materials_, d_864_kmsHierarchyWrap_, d_863_kmsHierarchyGenerateAndWrap_)
        d_866_valueOrError6_ = out157_
        if (d_866_valueOrError6_).IsFailure():
            res = (d_866_valueOrError6_).PropagateFailure()
            return res
        d_865_wrapOutput_ = (d_866_valueOrError6_).Extract()
        d_867_symmetricSigningKeyList_: Wrappers.Option
        d_867_symmetricSigningKeyList_ = (Wrappers.Option_Some(_dafny.Seq([((d_865_wrapOutput_).symmetricSigningKey).value])) if ((d_865_wrapOutput_).symmetricSigningKey).is_Some else Wrappers.Option_None())
        d_868_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_868_edk_ = AwsCryptographyMaterialProvidersTypes.EncryptedDataKey_EncryptedDataKey(Constants.default__.PROVIDER__ID__HIERARCHY, d_851_branchKeyIdUtf8_, (d_865_wrapOutput_).wrappedMaterial)
        if (d_865_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_869_result_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_870_valueOrError7_: Wrappers.Result = None
            d_870_valueOrError7_ = Materials.default__.EncryptionMaterialAddDataKey(d_847_materials_, (d_865_wrapOutput_).plaintextDataKey, _dafny.Seq([d_868_edk_]), d_867_symmetricSigningKeyList_)
            if (d_870_valueOrError7_).IsFailure():
                res = (d_870_valueOrError7_).PropagateFailure()
                return res
            d_869_result_ = (d_870_valueOrError7_).Extract()
            res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(d_869_result_))
            return res
        elif (d_865_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_871_result_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_872_valueOrError8_: Wrappers.Result = None
            d_872_valueOrError8_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys(d_847_materials_, _dafny.Seq([d_868_edk_]), d_867_symmetricSigningKeyList_)
            if (d_872_valueOrError8_).IsFailure():
                res = (d_872_valueOrError8_).PropagateFailure()
                return res
            d_871_result_ = (d_872_valueOrError8_).Extract()
            res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(d_871_result_))
            return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_873_materials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_873_materials_ = (input).materials
        d_874_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_874_suite_ = ((input).materials).algorithmSuite
        d_875_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_875_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_873_materials_), default__.E(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_875_valueOrError0_).IsFailure():
            res = (d_875_valueOrError0_).PropagateFailure()
            return res
        d_876_branchKeyIdForDecrypt_: _dafny.Seq
        d_877_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out158_: Wrappers.Result
        out158_ = (self).GetBranchKeyId((d_873_materials_).encryptionContext)
        d_877_valueOrError1_ = out158_
        if (d_877_valueOrError1_).IsFailure():
            res = (d_877_valueOrError1_).PropagateFailure()
            return res
        d_876_branchKeyIdForDecrypt_ = (d_877_valueOrError1_).Extract()
        d_878_filter_: OnDecryptHierarchyEncryptedDataKeyFilter
        nw35_ = OnDecryptHierarchyEncryptedDataKeyFilter()
        nw35_.ctor__(d_876_branchKeyIdForDecrypt_)
        d_878_filter_ = nw35_
        d_879_edksToAttempt_: _dafny.Seq
        d_880_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out159_: Wrappers.Result
        out159_ = Actions.default__.FilterWithResult(d_878_filter_, (input).encryptedDataKeys)
        d_880_valueOrError2_ = out159_
        if (d_880_valueOrError2_).IsFailure():
            res = (d_880_valueOrError2_).PropagateFailure()
            return res
        d_879_edksToAttempt_ = (d_880_valueOrError2_).Extract()
        if (0) == (len(d_879_edksToAttempt_)):
            d_881_errorMessage_: _dafny.Seq
            d_882_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            d_882_valueOrError3_ = ErrorMessages.default__.IncorrectDataKeys((input).encryptedDataKeys, ((input).materials).algorithmSuite, _dafny.Seq(""))
            if (d_882_valueOrError3_).IsFailure():
                res = (d_882_valueOrError3_).PropagateFailure()
                return res
            d_881_errorMessage_ = (d_882_valueOrError3_).Extract()
            res = Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_881_errorMessage_))
            return res
        d_883_decryptClosure_: Actions.ActionWithResult
        nw36_ = DecryptSingleEncryptedDataKey()
        nw36_.ctor__(d_873_materials_, (self).keyStore, (self).cryptoPrimitives, d_876_branchKeyIdForDecrypt_, (self).ttlSeconds, (self).cache)
        d_883_decryptClosure_ = nw36_
        d_884_outcome_: Wrappers.Result
        out160_: Wrappers.Result
        out160_ = Actions.default__.ReduceToSuccess(d_883_decryptClosure_, d_879_edksToAttempt_)
        d_884_outcome_ = out160_
        d_885_SealedDecryptionMaterials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_886_valueOrError4_: Wrappers.Result = None
        def lambda74_(d_887_errors_):
            return AwsCryptographyMaterialProvidersTypes.Error_CollectionOfErrors(d_887_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."))

        d_886_valueOrError4_ = (d_884_outcome_).MapFailure(lambda74_)
        if (d_886_valueOrError4_).IsFailure():
            res = (d_886_valueOrError4_).PropagateFailure()
            return res
        d_885_SealedDecryptionMaterials_ = (d_886_valueOrError4_).Extract()
        res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnDecryptOutput_OnDecryptOutput(d_885_SealedDecryptionMaterials_))
        return res
        return res

    def GetActiveCacheId(self, branchKeyId, branchKeyIdUtf8, cryptoPrimitives):
        cacheId: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_888_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        def iife26_(_pat_let8_0):
            def iife27_(d_889_branchKeyId_):
                return (True) and (((0) <= (len(d_889_branchKeyId_))) and ((len(d_889_branchKeyId_)) < (StandardLibrary_UInt.default__.UINT32__LIMIT)))
            return iife27_(_pat_let8_0)
        d_888_valueOrError0_ = Wrappers.default__.Need((((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).is_Success) and (iife26_(((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).value)), default__.E(_dafny.Seq("Invalid Branch Key ID Length")))
        if (d_888_valueOrError0_).IsFailure():
            cacheId = (d_888_valueOrError0_).PropagateFailure()
            return cacheId
        d_890_branchKeyId_: _dafny.Seq
        d_890_branchKeyId_ = (UTF8.default__.Decode(branchKeyIdUtf8)).value
        d_891_lenBranchKey_: _dafny.Seq
        d_891_lenBranchKey_ = StandardLibrary_UInt.default__.UInt32ToSeq(len(d_890_branchKeyId_))
        d_892_hashAlgorithm_: AwsCryptographyPrimitivesTypes.DigestAlgorithm
        d_892_hashAlgorithm_ = AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__512()
        d_893_maybeBranchKeyDigest_: Wrappers.Result
        out161_: Wrappers.Result
        out161_ = (cryptoPrimitives).Digest(AwsCryptographyPrimitivesTypes.DigestInput_DigestInput(d_892_hashAlgorithm_, branchKeyIdUtf8))
        d_893_maybeBranchKeyDigest_ = out161_
        d_894_branchKeyDigest_: _dafny.Seq
        d_895_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda75_(d_896_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_896_e_)

        d_895_valueOrError1_ = (d_893_maybeBranchKeyDigest_).MapFailure(lambda75_)
        if (d_895_valueOrError1_).IsFailure():
            cacheId = (d_895_valueOrError1_).PropagateFailure()
            return cacheId
        d_894_branchKeyDigest_ = (d_895_valueOrError1_).Extract()
        d_897_activeUtf8_: _dafny.Seq
        d_898_valueOrError2_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_898_valueOrError2_ = (UTF8.default__.Encode(default__.EXPRESSION__ATTRIBUTE__VALUE__STATUS__VALUE)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_898_valueOrError2_).IsFailure():
            cacheId = (d_898_valueOrError2_).PropagateFailure()
            return cacheId
        d_897_activeUtf8_ = (d_898_valueOrError2_).Extract()
        d_899_identifier_: _dafny.Seq
        d_899_identifier_ = (((d_891_lenBranchKey_) + (d_894_branchKeyDigest_)) + (_dafny.Seq([0]))) + (d_897_activeUtf8_)
        d_900_maybeCacheIdDigest_: Wrappers.Result
        out162_: Wrappers.Result
        out162_ = (cryptoPrimitives).Digest(AwsCryptographyPrimitivesTypes.DigestInput_DigestInput(d_892_hashAlgorithm_, d_899_identifier_))
        d_900_maybeCacheIdDigest_ = out162_
        d_901_cacheDigest_: _dafny.Seq
        d_902_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda76_(d_903_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_903_e_)

        d_902_valueOrError3_ = (d_900_maybeCacheIdDigest_).MapFailure(lambda76_)
        if (d_902_valueOrError3_).IsFailure():
            cacheId = (d_902_valueOrError3_).PropagateFailure()
            return cacheId
        d_901_cacheDigest_ = (d_902_valueOrError3_).Extract()
        d_904_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_904_valueOrError4_ = Wrappers.default__.Need((len(d_901_cacheDigest_)) == (Digest.default__.Length(d_892_hashAlgorithm_)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Digest generated a message not equal to the expected length.")))
        if (d_904_valueOrError4_).IsFailure():
            cacheId = (d_904_valueOrError4_).PropagateFailure()
            return cacheId
        cacheId = Wrappers.Result_Success(_dafny.Seq((d_901_cacheDigest_)[0:32:]))
        return cacheId
        return cacheId

    def GetActiveHierarchicalMaterials(self, branchKeyId, cacheId, keyStore):
        material: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.BranchKeyMaterials.default())()
        d_905_getCacheInput_: AwsCryptographyMaterialProvidersTypes.GetCacheEntryInput
        d_905_getCacheInput_ = AwsCryptographyMaterialProvidersTypes.GetCacheEntryInput_GetCacheEntryInput(cacheId, Wrappers.Option_None())
        d_906_getCacheOutput_: Wrappers.Result
        out163_: Wrappers.Result
        out163_ = default__.getEntry((self).cache, d_905_getCacheInput_)
        d_906_getCacheOutput_ = out163_
        if (d_906_getCacheOutput_).is_Failure:
            d_907_maybeGetActiveBranchKeyOutput_: Wrappers.Result
            out164_: Wrappers.Result
            out164_ = (keyStore).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(branchKeyId))
            d_907_maybeGetActiveBranchKeyOutput_ = out164_
            d_908_getActiveBranchKeyOutput_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
            d_909_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
            def lambda77_(d_910_e_):
                return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyKeyStore(d_910_e_)

            d_909_valueOrError0_ = (d_907_maybeGetActiveBranchKeyOutput_).MapFailure(lambda77_)
            if (d_909_valueOrError0_).IsFailure():
                material = (d_909_valueOrError0_).PropagateFailure()
                return material
            d_908_getActiveBranchKeyOutput_ = (d_909_valueOrError0_).Extract()
            d_911_branchKeyMaterials_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
            d_911_branchKeyMaterials_ = (d_908_getActiveBranchKeyOutput_).branchKeyMaterials
            d_912_now_: int
            out165_: int
            out165_ = Time.default__.CurrentRelativeTime()
            d_912_now_ = out165_
            d_913_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_913_valueOrError1_ = Wrappers.default__.Need(((d_912_now_) + ((self).ttlSeconds)) < (StandardLibrary_UInt.default__.INT64__MAX__LIMIT), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("INT64 Overflow when putting cache entry.")))
            if (d_913_valueOrError1_).IsFailure():
                material = (d_913_valueOrError1_).PropagateFailure()
                return material
            d_914_putCacheEntryInput_: AwsCryptographyMaterialProvidersTypes.PutCacheEntryInput
            d_914_putCacheEntryInput_ = AwsCryptographyMaterialProvidersTypes.PutCacheEntryInput_PutCacheEntryInput(cacheId, AwsCryptographyMaterialProvidersTypes.Materials_BranchKey(d_911_branchKeyMaterials_), d_912_now_, ((self).ttlSeconds) + (d_912_now_), Wrappers.Option_None(), Wrappers.Option_None())
            d_915___v0_: tuple
            d_916_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            out166_: Wrappers.Result
            out166_ = default__.putEntry((self).cache, d_914_putCacheEntryInput_)
            d_916_valueOrError2_ = out166_
            if (d_916_valueOrError2_).IsFailure():
                material = (d_916_valueOrError2_).PropagateFailure()
                return material
            d_915___v0_ = (d_916_valueOrError2_).Extract()
            material = Wrappers.Result_Success(d_911_branchKeyMaterials_)
            return material
        elif True:
            d_917_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_917_valueOrError3_ = Wrappers.default__.Need(((((d_906_getCacheOutput_).value).materials).is_BranchKey) and ((((d_906_getCacheOutput_).value).materials) == (AwsCryptographyMaterialProvidersTypes.Materials_BranchKey((((d_906_getCacheOutput_).value).materials).BranchKey))), default__.E(_dafny.Seq("Invalid Material Type.")))
            if (d_917_valueOrError3_).IsFailure():
                material = (d_917_valueOrError3_).PropagateFailure()
                return material
            material = Wrappers.Result_Success((((d_906_getCacheOutput_).value).materials).BranchKey)
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
        d_918_providerInfo_: _dafny.Seq
        d_918_providerInfo_ = (edk).keyProviderInfo
        d_919_providerId_: _dafny.Seq
        d_919_providerId_ = (edk).keyProviderId
        if (d_919_providerId_) != (Constants.default__.PROVIDER__ID__HIERARCHY):
            res = Wrappers.Result_Success(False)
            return res
        if not(UTF8.default__.ValidUTF8Seq(d_918_providerInfo_)):
            res = Wrappers.Result_Failure(default__.E(_dafny.Seq("Invalid encoding, provider info is not UTF8.")))
            return res
        d_920_branchKeyId_: _dafny.Seq
        d_921_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_921_valueOrError0_ = (UTF8.default__.Decode(d_918_providerInfo_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_921_valueOrError0_).IsFailure():
            res = (d_921_valueOrError0_).PropagateFailure()
            return res
        d_920_branchKeyId_ = (d_921_valueOrError0_).Extract()
        res = Wrappers.Result_Success(((self).branchKeyId) == (d_920_branchKeyId_))
        return res
        return res

    @property
    def branchKeyId(self):
        return self._branchKeyId

class DecryptSingleEncryptedDataKey(Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._materials: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials = None
        self._keyStore: AwsCryptographyKeyStoreTypes.IKeyStoreClient = None
        self._cryptoPrimitives: Aws_Cryptography_Primitives.AtomicPrimitivesClient = None
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
        d_922_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_922_valueOrError0_ = Wrappers.default__.Need(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received invalid EDK provider info for Hierarchical Keyring")))
        if (d_922_valueOrError0_).IsFailure():
            res = (d_922_valueOrError0_).PropagateFailure()
            return res
        d_923_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_923_suite_ = ((self).materials).algorithmSuite
        d_924_keyProviderId_: _dafny.Seq
        d_924_keyProviderId_ = (edk).keyProviderId
        d_925_branchKeyIdUtf8_: _dafny.Seq
        d_925_branchKeyIdUtf8_ = (edk).keyProviderInfo
        d_926_ciphertext_: _dafny.Seq
        d_926_ciphertext_ = (edk).ciphertext
        d_927_providerWrappedMaterial_: _dafny.Seq
        d_928_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_928_valueOrError1_ = EdkWrapping.default__.GetProviderWrappedMaterial(d_926_ciphertext_, d_923_suite_)
        if (d_928_valueOrError1_).IsFailure():
            res = (d_928_valueOrError1_).PropagateFailure()
            return res
        d_927_providerWrappedMaterial_ = (d_928_valueOrError1_).Extract()
        d_929_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_929_valueOrError2_ = Wrappers.default__.Need((len(d_927_providerWrappedMaterial_)) >= (default__.EDK__CIPHERTEXT__VERSION__INDEX), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received EDK Ciphertext of incorrect length.")))
        if (d_929_valueOrError2_).IsFailure():
            res = (d_929_valueOrError2_).PropagateFailure()
            return res
        d_930_branchKeyVersionUuid_: _dafny.Seq
        d_930_branchKeyVersionUuid_ = _dafny.Seq((d_927_providerWrappedMaterial_)[default__.EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX:default__.EDK__CIPHERTEXT__VERSION__INDEX:])
        d_931_version_: _dafny.Seq
        d_932_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_932_valueOrError3_ = (UUID.default__.FromByteArray(d_930_branchKeyVersionUuid_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_932_valueOrError3_).IsFailure():
            res = (d_932_valueOrError3_).PropagateFailure()
            return res
        d_931_version_ = (d_932_valueOrError3_).Extract()
        d_933_cacheId_: _dafny.Seq
        d_934_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out167_: Wrappers.Result
        out167_ = (self).GetVersionCacheId(d_925_branchKeyIdUtf8_, d_931_version_, (self).cryptoPrimitives)
        d_934_valueOrError4_ = out167_
        if (d_934_valueOrError4_).IsFailure():
            res = (d_934_valueOrError4_).PropagateFailure()
            return res
        d_933_cacheId_ = (d_934_valueOrError4_).Extract()
        d_935_hierarchicalMaterials_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
        d_936_valueOrError5_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.BranchKeyMaterials.default())()
        out168_: Wrappers.Result
        out168_ = (self).GetHierarchicalMaterialsVersion((self).branchKeyId, d_925_branchKeyIdUtf8_, d_931_version_, d_933_cacheId_)
        d_936_valueOrError5_ = out168_
        if (d_936_valueOrError5_).IsFailure():
            res = (d_936_valueOrError5_).PropagateFailure()
            return res
        d_935_hierarchicalMaterials_ = (d_936_valueOrError5_).Extract()
        d_937_branchKey_: _dafny.Seq
        d_937_branchKey_ = (d_935_hierarchicalMaterials_).branchKey
        d_938_branchKeyVersion_: _dafny.Seq
        d_938_branchKeyVersion_ = (d_935_hierarchicalMaterials_).branchKeyVersion
        d_939_branchKeyVersionAsString_: _dafny.Seq
        d_940_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_940_valueOrError6_ = (UTF8.default__.Decode(d_938_branchKeyVersion_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_940_valueOrError6_).IsFailure():
            res = (d_940_valueOrError6_).PropagateFailure()
            return res
        d_939_branchKeyVersionAsString_ = (d_940_valueOrError6_).Extract()
        d_941_branchKeyVersionAsBytes_: _dafny.Seq
        d_942_valueOrError7_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_942_valueOrError7_ = (UUID.default__.ToByteArray(d_939_branchKeyVersionAsString_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_942_valueOrError7_).IsFailure():
            res = (d_942_valueOrError7_).PropagateFailure()
            return res
        d_941_branchKeyVersionAsBytes_ = (d_942_valueOrError7_).Extract()
        d_943_maybeCrypto_: Wrappers.Result
        out169_: Wrappers.Result
        out169_ = Aws_Cryptography_Primitives.default__.AtomicPrimitives(Aws_Cryptography_Primitives.default__.DefaultCryptoConfig())
        d_943_maybeCrypto_ = out169_
        d_944_cryptoPrimitivesX_: AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient
        d_945_valueOrError8_: Wrappers.Result = None
        def lambda78_(d_946_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_946_e_)

        d_945_valueOrError8_ = (d_943_maybeCrypto_).MapFailure(lambda78_)
        if (d_945_valueOrError8_).IsFailure():
            res = (d_945_valueOrError8_).PropagateFailure()
            return res
        d_944_cryptoPrimitivesX_ = (d_945_valueOrError8_).Extract()
        d_947_cryptoPrimitives_: Aws_Cryptography_Primitives.AtomicPrimitivesClient
        d_947_cryptoPrimitives_ = d_944_cryptoPrimitivesX_
        d_948_kmsHierarchyUnwrap_: KmsHierarchyUnwrapKeyMaterial
        nw37_ = KmsHierarchyUnwrapKeyMaterial()
        nw37_.ctor__(d_937_branchKey_, d_925_branchKeyIdUtf8_, d_941_branchKeyVersionAsBytes_, d_947_cryptoPrimitives_)
        d_948_kmsHierarchyUnwrap_ = nw37_
        d_949_unwrapOutputRes_: Wrappers.Result
        out170_: Wrappers.Result
        out170_ = EdkWrapping.default__.UnwrapEdkMaterial((edk).ciphertext, (self).materials, d_948_kmsHierarchyUnwrap_)
        d_949_unwrapOutputRes_ = out170_
        d_950_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_951_valueOrError9_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.UnwrapEdkMaterialOutput.default(HierarchyUnwrapInfo.default()))()
        d_951_valueOrError9_ = d_949_unwrapOutputRes_
        if (d_951_valueOrError9_).IsFailure():
            res = (d_951_valueOrError9_).PropagateFailure()
            return res
        d_950_unwrapOutput_ = (d_951_valueOrError9_).Extract()
        d_952_result_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_953_valueOrError10_: Wrappers.Result = None
        d_953_valueOrError10_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_950_unwrapOutput_).plaintextDataKey, (d_950_unwrapOutput_).symmetricSigningKey)
        if (d_953_valueOrError10_).IsFailure():
            res = (d_953_valueOrError10_).PropagateFailure()
            return res
        d_952_result_ = (d_953_valueOrError10_).Extract()
        res = Wrappers.Result_Success(d_952_result_)
        return res
        return res

    def GetVersionCacheId(self, branchKeyIdUtf8, branchKeyVersion, cryptoPrimitives):
        cacheId: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_954_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        def iife28_(_pat_let9_0):
            def iife29_(d_955_branchKeyId_):
                return (True) and (((0) <= (len(d_955_branchKeyId_))) and ((len(d_955_branchKeyId_)) < (StandardLibrary_UInt.default__.UINT32__LIMIT)))
            return iife29_(_pat_let9_0)
        d_954_valueOrError0_ = Wrappers.default__.Need((((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).is_Success) and (iife28_(((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).value)), default__.E(_dafny.Seq("Invalid Branch Key ID Length")))
        if (d_954_valueOrError0_).IsFailure():
            cacheId = (d_954_valueOrError0_).PropagateFailure()
            return cacheId
        d_956_branchKeyId_: _dafny.Seq
        d_956_branchKeyId_ = (UTF8.default__.Decode(branchKeyIdUtf8)).value
        d_957_lenBranchKey_: _dafny.Seq
        d_957_lenBranchKey_ = StandardLibrary_UInt.default__.UInt32ToSeq(len(d_956_branchKeyId_))
        d_958_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_958_valueOrError1_ = Wrappers.default__.Need(UTF8.default__.IsASCIIString(branchKeyVersion), default__.E(_dafny.Seq("Unable to represent as an ASCII string.")))
        if (d_958_valueOrError1_).IsFailure():
            cacheId = (d_958_valueOrError1_).PropagateFailure()
            return cacheId
        d_959_versionBytes_: _dafny.Seq
        d_959_versionBytes_ = UTF8.default__.EncodeAscii(branchKeyVersion)
        d_960_identifier_: _dafny.Seq
        d_960_identifier_ = (((d_957_lenBranchKey_) + (branchKeyIdUtf8)) + (_dafny.Seq([0]))) + (d_959_versionBytes_)
        d_961_identifierDigestInput_: AwsCryptographyPrimitivesTypes.DigestInput
        d_961_identifierDigestInput_ = AwsCryptographyPrimitivesTypes.DigestInput_DigestInput(AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__512(), d_960_identifier_)
        d_962_maybeCacheDigest_: Wrappers.Result
        out171_: Wrappers.Result
        out171_ = Digest.default__.Digest(d_961_identifierDigestInput_)
        d_962_maybeCacheDigest_ = out171_
        d_963_cacheDigest_: _dafny.Seq
        d_964_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda79_(d_965_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_965_e_)

        d_964_valueOrError2_ = (d_962_maybeCacheDigest_).MapFailure(lambda79_)
        if (d_964_valueOrError2_).IsFailure():
            cacheId = (d_964_valueOrError2_).PropagateFailure()
            return cacheId
        d_963_cacheDigest_ = (d_964_valueOrError2_).Extract()
        cacheId = Wrappers.Result_Success(_dafny.Seq((d_963_cacheDigest_)[0:32:]))
        return cacheId
        return cacheId

    def GetHierarchicalMaterialsVersion(self, branchKeyId, branchKeyIdUtf8, version, cacheId):
        material: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.BranchKeyMaterials.default())()
        d_966_getCacheInput_: AwsCryptographyMaterialProvidersTypes.GetCacheEntryInput
        d_966_getCacheInput_ = AwsCryptographyMaterialProvidersTypes.GetCacheEntryInput_GetCacheEntryInput(cacheId, Wrappers.Option_None())
        d_967_getCacheOutput_: Wrappers.Result
        out172_: Wrappers.Result
        out172_ = default__.getEntry((self).cache, d_966_getCacheInput_)
        d_967_getCacheOutput_ = out172_
        if (d_967_getCacheOutput_).is_Failure:
            d_968_maybeGetBranchKeyVersionOutput_: Wrappers.Result
            out173_: Wrappers.Result
            out173_ = ((self).keyStore).GetBranchKeyVersion(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput_GetBranchKeyVersionInput(branchKeyId, version))
            d_968_maybeGetBranchKeyVersionOutput_ = out173_
            d_969_getBranchKeyVersionOutput_: AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
            d_970_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
            def lambda80_(d_971_e_):
                return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyKeyStore(d_971_e_)

            d_970_valueOrError0_ = (d_968_maybeGetBranchKeyVersionOutput_).MapFailure(lambda80_)
            if (d_970_valueOrError0_).IsFailure():
                material = (d_970_valueOrError0_).PropagateFailure()
                return material
            d_969_getBranchKeyVersionOutput_ = (d_970_valueOrError0_).Extract()
            d_972_branchKeyMaterials_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
            d_972_branchKeyMaterials_ = (d_969_getBranchKeyVersionOutput_).branchKeyMaterials
            d_973_now_: int
            out174_: int
            out174_ = Time.default__.CurrentRelativeTime()
            d_973_now_ = out174_
            d_974_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_974_valueOrError1_ = Wrappers.default__.Need(((d_973_now_) + ((self).ttlSeconds)) < (StandardLibrary_UInt.default__.INT64__MAX__LIMIT), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("INT64 Overflow when putting cache entry.")))
            if (d_974_valueOrError1_).IsFailure():
                material = (d_974_valueOrError1_).PropagateFailure()
                return material
            d_975_putCacheEntryInput_: AwsCryptographyMaterialProvidersTypes.PutCacheEntryInput
            d_975_putCacheEntryInput_ = AwsCryptographyMaterialProvidersTypes.PutCacheEntryInput_PutCacheEntryInput(cacheId, AwsCryptographyMaterialProvidersTypes.Materials_BranchKey(d_972_branchKeyMaterials_), d_973_now_, ((self).ttlSeconds) + (d_973_now_), Wrappers.Option_None(), Wrappers.Option_None())
            d_976___v1_: tuple
            d_977_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            out175_: Wrappers.Result
            out175_ = default__.putEntry((self).cache, d_975_putCacheEntryInput_)
            d_977_valueOrError2_ = out175_
            if (d_977_valueOrError2_).IsFailure():
                material = (d_977_valueOrError2_).PropagateFailure()
                return material
            d_976___v1_ = (d_977_valueOrError2_).Extract()
            material = Wrappers.Result_Success(d_972_branchKeyMaterials_)
            return material
        elif True:
            d_978_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_978_valueOrError3_ = Wrappers.default__.Need(((((d_967_getCacheOutput_).value).materials).is_BranchKey) and ((((d_967_getCacheOutput_).value).materials) == (AwsCryptographyMaterialProvidersTypes.Materials_BranchKey((((d_967_getCacheOutput_).value).materials).BranchKey))), default__.E(_dafny.Seq("Invalid Material Type.")))
            if (d_978_valueOrError3_).IsFailure():
                material = (d_978_valueOrError3_).PropagateFailure()
                return material
            material = Wrappers.Result_Success((((d_967_getCacheOutput_).value).materials).BranchKey)
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
        self._crypto: Aws_Cryptography_Primitives.AtomicPrimitivesClient = None
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
        d_979_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_979_suite_ = (input).algorithmSuite
        d_980_wrappedMaterial_: _dafny.Seq
        d_980_wrappedMaterial_ = (input).wrappedMaterial
        d_981_aad_: _dafny.Map
        d_981_aad_ = (input).encryptionContext
        d_982_KeyLength_: int
        d_982_KeyLength_ = AlgorithmSuites.default__.GetEncryptKeyLength(d_979_suite_)
        d_983_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_983_valueOrError0_ = Wrappers.default__.Need((len(d_980_wrappedMaterial_)) == ((default__.EXPECTED__EDK__CIPHERTEXT__OVERHEAD) + (d_982_KeyLength_)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received EDK Ciphertext of incorrect length2.")))
        if (d_983_valueOrError0_).IsFailure():
            res = (d_983_valueOrError0_).PropagateFailure()
            return res
        d_984_salt_: _dafny.Seq
        d_984_salt_ = _dafny.Seq((d_980_wrappedMaterial_)[0:default__.H__WRAP__SALT__LEN:])
        d_985_iv_: _dafny.Seq
        d_985_iv_ = _dafny.Seq((d_980_wrappedMaterial_)[default__.H__WRAP__SALT__LEN:default__.EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX:])
        d_986_branchKeyVersionUuid_: _dafny.Seq
        d_986_branchKeyVersionUuid_ = _dafny.Seq((d_980_wrappedMaterial_)[default__.EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX:default__.EDK__CIPHERTEXT__VERSION__INDEX:])
        d_987_wrappedKey_: _dafny.Seq
        d_987_wrappedKey_ = _dafny.Seq((d_980_wrappedMaterial_)[default__.EDK__CIPHERTEXT__VERSION__INDEX:(default__.EDK__CIPHERTEXT__VERSION__INDEX) + (d_982_KeyLength_):])
        d_988_authTag_: _dafny.Seq
        d_988_authTag_ = _dafny.Seq((d_980_wrappedMaterial_)[(default__.EDK__CIPHERTEXT__VERSION__INDEX) + (d_982_KeyLength_)::])
        d_989_serializedEC_: _dafny.Seq
        d_990_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_990_valueOrError1_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_990_valueOrError1_).IsFailure():
            res = (d_990_valueOrError1_).PropagateFailure()
            return res
        d_989_serializedEC_ = (d_990_valueOrError1_).Extract()
        d_991_wrappingAad_: _dafny.Seq
        d_991_wrappingAad_ = default__.WrappingAad((self).branchKeyIdUtf8, (self).branchKeyVersionAsBytes, d_989_serializedEC_)
        d_992_derivedBranchKey_: _dafny.Seq
        d_993_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out176_: Wrappers.Result
        out176_ = default__.DeriveEncryptionKeyFromBranchKey((self).branchKey, d_984_salt_, Wrappers.Option_Some(Constants.default__.PROVIDER__ID__HIERARCHY), (self).crypto)
        d_993_valueOrError2_ = out176_
        if (d_993_valueOrError2_).IsFailure():
            res = (d_993_valueOrError2_).PropagateFailure()
            return res
        d_992_derivedBranchKey_ = (d_993_valueOrError2_).Extract()
        d_994_maybeUnwrappedPdk_: Wrappers.Result
        out177_: Wrappers.Result
        out177_ = ((self).crypto).AESDecrypt(AwsCryptographyPrimitivesTypes.AESDecryptInput_AESDecryptInput(default__.AES__256__ENC__ALG, d_992_derivedBranchKey_, d_987_wrappedKey_, d_988_authTag_, d_985_iv_, d_991_wrappingAad_))
        d_994_maybeUnwrappedPdk_ = out177_
        d_995_unwrappedPdk_: _dafny.Seq
        d_996_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda81_(d_997_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_997_e_)

        d_996_valueOrError3_ = (d_994_maybeUnwrappedPdk_).MapFailure(lambda81_)
        if (d_996_valueOrError3_).IsFailure():
            res = (d_996_valueOrError3_).PropagateFailure()
            return res
        d_995_unwrappedPdk_ = (d_996_valueOrError3_).Extract()
        d_998_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_998_valueOrError4_ = Wrappers.default__.Need((len(d_995_unwrappedPdk_)) == (AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)), default__.E(_dafny.Seq("Invalid Key Length")))
        if (d_998_valueOrError4_).IsFailure():
            res = (d_998_valueOrError4_).PropagateFailure()
            return res
        d_999_output_: MaterialWrapping.UnwrapOutput
        d_999_output_ = MaterialWrapping.UnwrapOutput_UnwrapOutput(d_995_unwrappedPdk_, HierarchyUnwrapInfo_HierarchyUnwrapInfo())
        res = Wrappers.Result_Success(d_999_output_)
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
        self._crypto: Aws_Cryptography_Primitives.AtomicPrimitivesClient = None
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
        d_1000_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_1000_suite_ = (input).algorithmSuite
        d_1001_pdkResult_: Wrappers.Result
        out178_: Wrappers.Result
        out178_ = ((self).crypto).GenerateRandomBytes(AwsCryptographyPrimitivesTypes.GenerateRandomBytesInput_GenerateRandomBytesInput(AlgorithmSuites.default__.GetEncryptKeyLength(d_1000_suite_)))
        d_1001_pdkResult_ = out178_
        d_1002_pdk_: _dafny.Seq
        d_1003_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda82_(d_1004_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1004_e_)

        d_1003_valueOrError0_ = (d_1001_pdkResult_).MapFailure(lambda82_)
        if (d_1003_valueOrError0_).IsFailure():
            res = (d_1003_valueOrError0_).PropagateFailure()
            return res
        d_1002_pdk_ = (d_1003_valueOrError0_).Extract()
        d_1005_wrap_: KmsHierarchyWrapKeyMaterial
        nw38_ = KmsHierarchyWrapKeyMaterial()
        nw38_.ctor__((self).branchKey, (self).branchKeyIdUtf8, (self).branchKeyVersionAsBytes, (self).crypto)
        d_1005_wrap_ = nw38_
        d_1006_wrapOutput_: MaterialWrapping.WrapOutput
        d_1007_valueOrError1_: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.WrapOutput.default(HierarchyWrapInfo.default()))()
        out179_: Wrappers.Result
        out179_ = (d_1005_wrap_).Invoke(MaterialWrapping.WrapInput_WrapInput(d_1002_pdk_, (input).algorithmSuite, (input).encryptionContext))
        d_1007_valueOrError1_ = out179_
        if (d_1007_valueOrError1_).IsFailure():
            res = (d_1007_valueOrError1_).PropagateFailure()
            return res
        d_1006_wrapOutput_ = (d_1007_valueOrError1_).Extract()
        d_1008_output_: MaterialWrapping.GenerateAndWrapOutput
        d_1008_output_ = MaterialWrapping.GenerateAndWrapOutput_GenerateAndWrapOutput(d_1002_pdk_, (d_1006_wrapOutput_).wrappedMaterial, HierarchyWrapInfo_HierarchyWrapInfo())
        res = Wrappers.Result_Success(d_1008_output_)
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
        self._crypto: Aws_Cryptography_Primitives.AtomicPrimitivesClient = None
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
        d_1009_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_1009_suite_ = (input).algorithmSuite
        d_1010_maybeNonceSalt_: Wrappers.Result
        out180_: Wrappers.Result
        out180_ = ((self).crypto).GenerateRandomBytes(AwsCryptographyPrimitivesTypes.GenerateRandomBytesInput_GenerateRandomBytesInput((default__.H__WRAP__SALT__LEN) + (default__.H__WRAP__NONCE__LEN)))
        d_1010_maybeNonceSalt_ = out180_
        d_1011_saltAndNonce_: _dafny.Seq
        d_1012_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda83_(d_1013_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1013_e_)

        d_1012_valueOrError0_ = (d_1010_maybeNonceSalt_).MapFailure(lambda83_)
        if (d_1012_valueOrError0_).IsFailure():
            res = (d_1012_valueOrError0_).PropagateFailure()
            return res
        d_1011_saltAndNonce_ = (d_1012_valueOrError0_).Extract()
        d_1014_salt_: _dafny.Seq
        d_1014_salt_ = _dafny.Seq((d_1011_saltAndNonce_)[0:default__.H__WRAP__SALT__LEN:])
        d_1015_nonce_: _dafny.Seq
        d_1015_nonce_ = _dafny.Seq((d_1011_saltAndNonce_)[default__.H__WRAP__SALT__LEN::])
        d_1016_serializedEC_: _dafny.Seq
        d_1017_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1017_valueOrError1_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_1017_valueOrError1_).IsFailure():
            res = (d_1017_valueOrError1_).PropagateFailure()
            return res
        d_1016_serializedEC_ = (d_1017_valueOrError1_).Extract()
        d_1018_wrappingAad_: _dafny.Seq
        d_1018_wrappingAad_ = default__.WrappingAad((self).branchKeyIdUtf8, (self).branchKeyVersionAsBytes, d_1016_serializedEC_)
        d_1019_derivedBranchKey_: _dafny.Seq
        d_1020_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out181_: Wrappers.Result
        out181_ = default__.DeriveEncryptionKeyFromBranchKey((self).branchKey, d_1014_salt_, Wrappers.Option_Some(Constants.default__.PROVIDER__ID__HIERARCHY), (self).crypto)
        d_1020_valueOrError2_ = out181_
        if (d_1020_valueOrError2_).IsFailure():
            res = (d_1020_valueOrError2_).PropagateFailure()
            return res
        d_1019_derivedBranchKey_ = (d_1020_valueOrError2_).Extract()
        d_1021_maybeWrappedPdk_: Wrappers.Result
        out182_: Wrappers.Result
        out182_ = ((self).crypto).AESEncrypt(AwsCryptographyPrimitivesTypes.AESEncryptInput_AESEncryptInput(default__.AES__256__ENC__ALG, d_1015_nonce_, d_1019_derivedBranchKey_, (input).plaintextMaterial, d_1018_wrappingAad_))
        d_1021_maybeWrappedPdk_ = out182_
        d_1022_wrappedPdk_: AwsCryptographyPrimitivesTypes.AESEncryptOutput
        d_1023_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.AESEncryptOutput.default())()
        def lambda84_(d_1024_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1024_e_)

        d_1023_valueOrError3_ = (d_1021_maybeWrappedPdk_).MapFailure(lambda84_)
        if (d_1023_valueOrError3_).IsFailure():
            res = (d_1023_valueOrError3_).PropagateFailure()
            return res
        d_1022_wrappedPdk_ = (d_1023_valueOrError3_).Extract()
        d_1025_output_: MaterialWrapping.WrapOutput
        d_1025_output_ = MaterialWrapping.WrapOutput_WrapOutput(((((d_1014_salt_) + (d_1015_nonce_)) + ((self).branchKeyVersionAsBytes)) + ((d_1022_wrappedPdk_).cipherText)) + ((d_1022_wrappedPdk_).authTag), HierarchyWrapInfo_HierarchyWrapInfo())
        res = Wrappers.Result_Success(d_1025_output_)
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
