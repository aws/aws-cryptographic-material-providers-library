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
        d_834_maybeDerivedBranchKey_: Wrappers.Result
        out149_: Wrappers.Result
        out149_ = (cryptoPrimitives).KdfCounterMode(AwsCryptographyPrimitivesTypes.KdfCtrInput_KdfCtrInput(AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__256(), branchKey, default__.DERIVED__BRANCH__KEY__EXPECTED__LENGTH, purpose, Wrappers.Option_Some(salt)))
        d_834_maybeDerivedBranchKey_ = out149_
        d_835_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda68_(d_836_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_836_e_)

        d_835_valueOrError0_ = (d_834_maybeDerivedBranchKey_).MapFailure(lambda68_)
        if (d_835_valueOrError0_).IsFailure():
            output = (d_835_valueOrError0_).PropagateFailure()
            return output
        d_837_derivedBranchKey_: _dafny.Seq
        d_837_derivedBranchKey_ = (d_835_valueOrError0_).Extract()
        output = Wrappers.Result_Success(d_837_derivedBranchKey_)
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
            d_838_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyMaterialProvidersTypes.GetBranchKeyIdOutput.default())()
            out152_: Wrappers.Result
            out152_ = (((self).branchKeyIdSupplier).value).GetBranchKeyId(AwsCryptographyMaterialProvidersTypes.GetBranchKeyIdInput_GetBranchKeyIdInput(context))
            d_838_valueOrError0_ = out152_
            if (d_838_valueOrError0_).IsFailure():
                ret = (d_838_valueOrError0_).PropagateFailure()
                return ret
            d_839_GetBranchKeyIdOut_: AwsCryptographyMaterialProvidersTypes.GetBranchKeyIdOutput
            d_839_GetBranchKeyIdOut_ = (d_838_valueOrError0_).Extract()
            ret = Wrappers.Result_Success((d_839_GetBranchKeyIdOut_).branchKeyId)
            return ret
        return ret

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        d_840_materials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_840_materials_ = (input).materials
        d_841_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_841_suite_ = (d_840_materials_).algorithmSuite
        d_842_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out153_: Wrappers.Result
        out153_ = (self).GetBranchKeyId((d_840_materials_).encryptionContext)
        d_842_valueOrError0_ = out153_
        if (d_842_valueOrError0_).IsFailure():
            res = (d_842_valueOrError0_).PropagateFailure()
            return res
        d_843_branchKeyIdForEncrypt_: _dafny.Seq
        d_843_branchKeyIdForEncrypt_ = (d_842_valueOrError0_).Extract()
        d_844_valueOrError1_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_844_valueOrError1_ = (UTF8.default__.Encode(d_843_branchKeyIdForEncrypt_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_844_valueOrError1_).IsFailure():
            res = (d_844_valueOrError1_).PropagateFailure()
            return res
        d_845_branchKeyIdUtf8_: _dafny.Seq
        d_845_branchKeyIdUtf8_ = (d_844_valueOrError1_).Extract()
        d_846_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out154_: Wrappers.Result
        out154_ = (self).GetActiveCacheId(d_843_branchKeyIdForEncrypt_, d_845_branchKeyIdUtf8_, (self).cryptoPrimitives)
        d_846_valueOrError2_ = out154_
        if (d_846_valueOrError2_).IsFailure():
            res = (d_846_valueOrError2_).PropagateFailure()
            return res
        d_847_cacheId_: _dafny.Seq
        d_847_cacheId_ = (d_846_valueOrError2_).Extract()
        d_848_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.BranchKeyMaterials.default())()
        out155_: Wrappers.Result
        out155_ = (self).GetActiveHierarchicalMaterials(d_843_branchKeyIdForEncrypt_, d_847_cacheId_, (self).keyStore)
        d_848_valueOrError3_ = out155_
        if (d_848_valueOrError3_).IsFailure():
            res = (d_848_valueOrError3_).PropagateFailure()
            return res
        d_849_hierarchicalMaterials_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
        d_849_hierarchicalMaterials_ = (d_848_valueOrError3_).Extract()
        d_850_branchKey_: _dafny.Seq
        d_850_branchKey_ = (d_849_hierarchicalMaterials_).branchKey
        d_851_branchKeyVersion_: _dafny.Seq
        d_851_branchKeyVersion_ = (d_849_hierarchicalMaterials_).branchKeyVersion
        d_852_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_852_valueOrError4_ = (UTF8.default__.Decode(d_851_branchKeyVersion_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_852_valueOrError4_).IsFailure():
            res = (d_852_valueOrError4_).PropagateFailure()
            return res
        d_853_branchKeyVersionAsString_: _dafny.Seq
        d_853_branchKeyVersionAsString_ = (d_852_valueOrError4_).Extract()
        d_854_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_854_valueOrError5_ = (UUID.default__.ToByteArray(d_853_branchKeyVersionAsString_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_854_valueOrError5_).IsFailure():
            res = (d_854_valueOrError5_).PropagateFailure()
            return res
        d_855_branchKeyVersionAsBytes_: _dafny.Seq
        d_855_branchKeyVersionAsBytes_ = (d_854_valueOrError5_).Extract()
        d_856_kmsHierarchyGenerateAndWrap_: KmsHierarchyGenerateAndWrapKeyMaterial
        nw33_ = KmsHierarchyGenerateAndWrapKeyMaterial()
        nw33_.ctor__((d_849_hierarchicalMaterials_).branchKey, d_845_branchKeyIdUtf8_, d_855_branchKeyVersionAsBytes_, (self).cryptoPrimitives)
        d_856_kmsHierarchyGenerateAndWrap_ = nw33_
        d_857_kmsHierarchyWrap_: KmsHierarchyWrapKeyMaterial
        nw34_ = KmsHierarchyWrapKeyMaterial()
        nw34_.ctor__((d_849_hierarchicalMaterials_).branchKey, d_845_branchKeyIdUtf8_, d_855_branchKeyVersionAsBytes_, (self).cryptoPrimitives)
        d_857_kmsHierarchyWrap_ = nw34_
        d_858_valueOrError6_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.WrapEdkMaterialOutput.default(HierarchyWrapInfo.default()))()
        out156_: Wrappers.Result
        out156_ = EdkWrapping.default__.WrapEdkMaterial(d_840_materials_, d_857_kmsHierarchyWrap_, d_856_kmsHierarchyGenerateAndWrap_)
        d_858_valueOrError6_ = out156_
        if (d_858_valueOrError6_).IsFailure():
            res = (d_858_valueOrError6_).PropagateFailure()
            return res
        d_859_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_859_wrapOutput_ = (d_858_valueOrError6_).Extract()
        d_860_symmetricSigningKeyList_: Wrappers.Option
        if ((d_859_wrapOutput_).symmetricSigningKey).is_Some:
            d_860_symmetricSigningKeyList_ = Wrappers.Option_Some(_dafny.Seq([((d_859_wrapOutput_).symmetricSigningKey).value]))
        elif True:
            d_860_symmetricSigningKeyList_ = Wrappers.Option_None()
        d_861_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_861_edk_ = AwsCryptographyMaterialProvidersTypes.EncryptedDataKey_EncryptedDataKey(Constants.default__.PROVIDER__ID__HIERARCHY, d_845_branchKeyIdUtf8_, (d_859_wrapOutput_).wrappedMaterial)
        if (d_859_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_862_valueOrError7_: Wrappers.Result = None
            d_862_valueOrError7_ = Materials.default__.EncryptionMaterialAddDataKey(d_840_materials_, (d_859_wrapOutput_).plaintextDataKey, _dafny.Seq([d_861_edk_]), d_860_symmetricSigningKeyList_)
            if (d_862_valueOrError7_).IsFailure():
                res = (d_862_valueOrError7_).PropagateFailure()
                return res
            d_863_result_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_863_result_ = (d_862_valueOrError7_).Extract()
            res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(d_863_result_))
            return res
        elif (d_859_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_864_valueOrError8_: Wrappers.Result = None
            d_864_valueOrError8_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys(d_840_materials_, _dafny.Seq([d_861_edk_]), d_860_symmetricSigningKeyList_)
            if (d_864_valueOrError8_).IsFailure():
                res = (d_864_valueOrError8_).PropagateFailure()
                return res
            d_865_result_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_865_result_ = (d_864_valueOrError8_).Extract()
            res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(d_865_result_))
            return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_866_materials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_866_materials_ = (input).materials
        d_867_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_867_suite_ = ((input).materials).algorithmSuite
        d_868_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_868_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_866_materials_), default__.E(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_868_valueOrError0_).IsFailure():
            res = (d_868_valueOrError0_).PropagateFailure()
            return res
        d_869_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out157_: Wrappers.Result
        out157_ = (self).GetBranchKeyId((d_866_materials_).encryptionContext)
        d_869_valueOrError1_ = out157_
        if (d_869_valueOrError1_).IsFailure():
            res = (d_869_valueOrError1_).PropagateFailure()
            return res
        d_870_branchKeyIdForDecrypt_: _dafny.Seq
        d_870_branchKeyIdForDecrypt_ = (d_869_valueOrError1_).Extract()
        d_871_filter_: OnDecryptHierarchyEncryptedDataKeyFilter
        nw35_ = OnDecryptHierarchyEncryptedDataKeyFilter()
        nw35_.ctor__(d_870_branchKeyIdForDecrypt_)
        d_871_filter_ = nw35_
        d_872_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out158_: Wrappers.Result
        out158_ = Actions.default__.FilterWithResult(d_871_filter_, (input).encryptedDataKeys)
        d_872_valueOrError2_ = out158_
        if (d_872_valueOrError2_).IsFailure():
            res = (d_872_valueOrError2_).PropagateFailure()
            return res
        d_873_edksToAttempt_: _dafny.Seq
        d_873_edksToAttempt_ = (d_872_valueOrError2_).Extract()
        if (0) == (len(d_873_edksToAttempt_)):
            d_874_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            d_874_valueOrError3_ = ErrorMessages.default__.IncorrectDataKeys((input).encryptedDataKeys, ((input).materials).algorithmSuite, _dafny.Seq(""))
            if (d_874_valueOrError3_).IsFailure():
                res = (d_874_valueOrError3_).PropagateFailure()
                return res
            d_875_errorMessage_: _dafny.Seq
            d_875_errorMessage_ = (d_874_valueOrError3_).Extract()
            res = Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_875_errorMessage_))
            return res
        d_876_decryptClosure_: Actions.ActionWithResult
        nw36_ = DecryptSingleEncryptedDataKey()
        nw36_.ctor__(d_866_materials_, (self).keyStore, (self).cryptoPrimitives, d_870_branchKeyIdForDecrypt_, (self).ttlSeconds, (self).cache)
        d_876_decryptClosure_ = nw36_
        d_877_outcome_: Wrappers.Result
        out159_: Wrappers.Result
        out159_ = Actions.default__.ReduceToSuccess(d_876_decryptClosure_, d_873_edksToAttempt_)
        d_877_outcome_ = out159_
        d_878_valueOrError4_: Wrappers.Result = None
        def lambda69_(d_879_errors_):
            return AwsCryptographyMaterialProvidersTypes.Error_CollectionOfErrors(d_879_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."))

        d_878_valueOrError4_ = (d_877_outcome_).MapFailure(lambda69_)
        if (d_878_valueOrError4_).IsFailure():
            res = (d_878_valueOrError4_).PropagateFailure()
            return res
        d_880_SealedDecryptionMaterials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_880_SealedDecryptionMaterials_ = (d_878_valueOrError4_).Extract()
        res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnDecryptOutput_OnDecryptOutput(d_880_SealedDecryptionMaterials_))
        return res
        return res

    def GetActiveCacheId(self, branchKeyId, branchKeyIdUtf8, cryptoPrimitives):
        cacheId: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_881_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        def iife22_(_pat_let6_0):
            def iife23_(d_882_branchKeyId_):
                return (True) and (((0) <= (len(d_882_branchKeyId_))) and ((len(d_882_branchKeyId_)) < (StandardLibrary_UInt.default__.UINT32__LIMIT)))
            return iife23_(_pat_let6_0)
        d_881_valueOrError0_ = Wrappers.default__.Need((((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).is_Success) and (iife22_(((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).value)), default__.E(_dafny.Seq("Invalid Branch Key ID Length")))
        if (d_881_valueOrError0_).IsFailure():
            cacheId = (d_881_valueOrError0_).PropagateFailure()
            return cacheId
        d_883_branchKeyId_: _dafny.Seq
        d_883_branchKeyId_ = (UTF8.default__.Decode(branchKeyIdUtf8)).value
        d_884_lenBranchKey_: _dafny.Seq
        d_884_lenBranchKey_ = StandardLibrary_UInt.default__.UInt32ToSeq(len(d_883_branchKeyId_))
        d_885_hashAlgorithm_: AwsCryptographyPrimitivesTypes.DigestAlgorithm
        d_885_hashAlgorithm_ = AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__512()
        d_886_maybeBranchKeyDigest_: Wrappers.Result
        out160_: Wrappers.Result
        out160_ = (cryptoPrimitives).Digest(AwsCryptographyPrimitivesTypes.DigestInput_DigestInput(d_885_hashAlgorithm_, branchKeyIdUtf8))
        d_886_maybeBranchKeyDigest_ = out160_
        d_887_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda70_(d_888_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_888_e_)

        d_887_valueOrError1_ = (d_886_maybeBranchKeyDigest_).MapFailure(lambda70_)
        if (d_887_valueOrError1_).IsFailure():
            cacheId = (d_887_valueOrError1_).PropagateFailure()
            return cacheId
        d_889_branchKeyDigest_: _dafny.Seq
        d_889_branchKeyDigest_ = (d_887_valueOrError1_).Extract()
        d_890_valueOrError2_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_890_valueOrError2_ = (UTF8.default__.Encode(default__.EXPRESSION__ATTRIBUTE__VALUE__STATUS__VALUE)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_890_valueOrError2_).IsFailure():
            cacheId = (d_890_valueOrError2_).PropagateFailure()
            return cacheId
        d_891_activeUtf8_: _dafny.Seq
        d_891_activeUtf8_ = (d_890_valueOrError2_).Extract()
        d_892_identifier_: _dafny.Seq
        d_892_identifier_ = (((d_884_lenBranchKey_) + (d_889_branchKeyDigest_)) + (_dafny.Seq([0]))) + (d_891_activeUtf8_)
        d_893_maybeCacheIdDigest_: Wrappers.Result
        out161_: Wrappers.Result
        out161_ = (cryptoPrimitives).Digest(AwsCryptographyPrimitivesTypes.DigestInput_DigestInput(d_885_hashAlgorithm_, d_892_identifier_))
        d_893_maybeCacheIdDigest_ = out161_
        d_894_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda71_(d_895_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_895_e_)

        d_894_valueOrError3_ = (d_893_maybeCacheIdDigest_).MapFailure(lambda71_)
        if (d_894_valueOrError3_).IsFailure():
            cacheId = (d_894_valueOrError3_).PropagateFailure()
            return cacheId
        d_896_cacheDigest_: _dafny.Seq
        d_896_cacheDigest_ = (d_894_valueOrError3_).Extract()
        d_897_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_897_valueOrError4_ = Wrappers.default__.Need((len(d_896_cacheDigest_)) == (Digest.default__.Length(d_885_hashAlgorithm_)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Digest generated a message not equal to the expected length.")))
        if (d_897_valueOrError4_).IsFailure():
            cacheId = (d_897_valueOrError4_).PropagateFailure()
            return cacheId
        cacheId = Wrappers.Result_Success(_dafny.Seq((d_896_cacheDigest_)[0:32:]))
        return cacheId
        return cacheId

    def GetActiveHierarchicalMaterials(self, branchKeyId, cacheId, keyStore):
        material: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.BranchKeyMaterials.default())()
        d_898_getCacheInput_: AwsCryptographyMaterialProvidersTypes.GetCacheEntryInput
        d_898_getCacheInput_ = AwsCryptographyMaterialProvidersTypes.GetCacheEntryInput_GetCacheEntryInput(cacheId, Wrappers.Option_None())
        d_899_getCacheOutput_: Wrappers.Result
        out162_: Wrappers.Result
        out162_ = default__.getEntry((self).cache, d_898_getCacheInput_)
        d_899_getCacheOutput_ = out162_
        if (d_899_getCacheOutput_).is_Failure:
            d_900_maybeGetActiveBranchKeyOutput_: Wrappers.Result
            out163_: Wrappers.Result
            out163_ = (keyStore).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(branchKeyId))
            d_900_maybeGetActiveBranchKeyOutput_ = out163_
            d_901_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
            def lambda72_(d_902_e_):
                return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyKeyStore(d_902_e_)

            d_901_valueOrError0_ = (d_900_maybeGetActiveBranchKeyOutput_).MapFailure(lambda72_)
            if (d_901_valueOrError0_).IsFailure():
                material = (d_901_valueOrError0_).PropagateFailure()
                return material
            d_903_getActiveBranchKeyOutput_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
            d_903_getActiveBranchKeyOutput_ = (d_901_valueOrError0_).Extract()
            d_904_branchKeyMaterials_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
            d_904_branchKeyMaterials_ = (d_903_getActiveBranchKeyOutput_).branchKeyMaterials
            d_905_now_: int
            out164_: int
            out164_ = Time.default__.CurrentRelativeTime()
            d_905_now_ = out164_
            d_906_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_906_valueOrError1_ = Wrappers.default__.Need(((d_905_now_) + ((self).ttlSeconds)) < (StandardLibrary_UInt.default__.INT64__MAX__LIMIT), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("INT64 Overflow when putting cache entry.")))
            if (d_906_valueOrError1_).IsFailure():
                material = (d_906_valueOrError1_).PropagateFailure()
                return material
            d_907_putCacheEntryInput_: AwsCryptographyMaterialProvidersTypes.PutCacheEntryInput
            d_907_putCacheEntryInput_ = AwsCryptographyMaterialProvidersTypes.PutCacheEntryInput_PutCacheEntryInput(cacheId, AwsCryptographyMaterialProvidersTypes.Materials_BranchKey(d_904_branchKeyMaterials_), d_905_now_, ((self).ttlSeconds) + (d_905_now_), Wrappers.Option_None(), Wrappers.Option_None())
            d_908_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            out165_: Wrappers.Result
            out165_ = default__.putEntry((self).cache, d_907_putCacheEntryInput_)
            d_908_valueOrError2_ = out165_
            if (d_908_valueOrError2_).IsFailure():
                material = (d_908_valueOrError2_).PropagateFailure()
                return material
            d_909___v0_: tuple
            d_909___v0_ = (d_908_valueOrError2_).Extract()
            material = Wrappers.Result_Success(d_904_branchKeyMaterials_)
            return material
        elif True:
            d_910_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_910_valueOrError3_ = Wrappers.default__.Need(((((d_899_getCacheOutput_).value).materials).is_BranchKey) and ((((d_899_getCacheOutput_).value).materials) == (AwsCryptographyMaterialProvidersTypes.Materials_BranchKey((((d_899_getCacheOutput_).value).materials).BranchKey))), default__.E(_dafny.Seq("Invalid Material Type.")))
            if (d_910_valueOrError3_).IsFailure():
                material = (d_910_valueOrError3_).PropagateFailure()
                return material
            material = Wrappers.Result_Success((((d_899_getCacheOutput_).value).materials).BranchKey)
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
        d_911_providerInfo_: _dafny.Seq
        d_911_providerInfo_ = (edk).keyProviderInfo
        d_912_providerId_: _dafny.Seq
        d_912_providerId_ = (edk).keyProviderId
        if (d_912_providerId_) != (Constants.default__.PROVIDER__ID__HIERARCHY):
            res = Wrappers.Result_Success(False)
            return res
        if not(UTF8.default__.ValidUTF8Seq(d_911_providerInfo_)):
            res = Wrappers.Result_Failure(default__.E(_dafny.Seq("Invalid encoding, provider info is not UTF8.")))
            return res
        d_913_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_913_valueOrError0_ = (UTF8.default__.Decode(d_911_providerInfo_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_913_valueOrError0_).IsFailure():
            res = (d_913_valueOrError0_).PropagateFailure()
            return res
        d_914_branchKeyId_: _dafny.Seq
        d_914_branchKeyId_ = (d_913_valueOrError0_).Extract()
        res = Wrappers.Result_Success(((self).branchKeyId) == (d_914_branchKeyId_))
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
        d_915_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_915_valueOrError0_ = Wrappers.default__.Need(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received invalid EDK provider info for Hierarchical Keyring")))
        if (d_915_valueOrError0_).IsFailure():
            res = (d_915_valueOrError0_).PropagateFailure()
            return res
        d_916_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_916_suite_ = ((self).materials).algorithmSuite
        d_917_keyProviderId_: _dafny.Seq
        d_917_keyProviderId_ = (edk).keyProviderId
        d_918_branchKeyIdUtf8_: _dafny.Seq
        d_918_branchKeyIdUtf8_ = (edk).keyProviderInfo
        d_919_ciphertext_: _dafny.Seq
        d_919_ciphertext_ = (edk).ciphertext
        d_920_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_920_valueOrError1_ = EdkWrapping.default__.GetProviderWrappedMaterial(d_919_ciphertext_, d_916_suite_)
        if (d_920_valueOrError1_).IsFailure():
            res = (d_920_valueOrError1_).PropagateFailure()
            return res
        d_921_providerWrappedMaterial_: _dafny.Seq
        d_921_providerWrappedMaterial_ = (d_920_valueOrError1_).Extract()
        d_922_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_922_valueOrError2_ = Wrappers.default__.Need((len(d_921_providerWrappedMaterial_)) >= (default__.EDK__CIPHERTEXT__VERSION__INDEX), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received EDK Ciphertext of incorrect length.")))
        if (d_922_valueOrError2_).IsFailure():
            res = (d_922_valueOrError2_).PropagateFailure()
            return res
        d_923_branchKeyVersionUuid_: _dafny.Seq
        d_923_branchKeyVersionUuid_ = _dafny.Seq((d_921_providerWrappedMaterial_)[default__.EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX:default__.EDK__CIPHERTEXT__VERSION__INDEX:])
        d_924_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_924_valueOrError3_ = (UUID.default__.FromByteArray(d_923_branchKeyVersionUuid_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_924_valueOrError3_).IsFailure():
            res = (d_924_valueOrError3_).PropagateFailure()
            return res
        d_925_version_: _dafny.Seq
        d_925_version_ = (d_924_valueOrError3_).Extract()
        d_926_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out166_: Wrappers.Result
        out166_ = (self).GetVersionCacheId(d_918_branchKeyIdUtf8_, d_925_version_, (self).cryptoPrimitives)
        d_926_valueOrError4_ = out166_
        if (d_926_valueOrError4_).IsFailure():
            res = (d_926_valueOrError4_).PropagateFailure()
            return res
        d_927_cacheId_: _dafny.Seq
        d_927_cacheId_ = (d_926_valueOrError4_).Extract()
        d_928_valueOrError5_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.BranchKeyMaterials.default())()
        out167_: Wrappers.Result
        out167_ = (self).GetHierarchicalMaterialsVersion((self).branchKeyId, d_918_branchKeyIdUtf8_, d_925_version_, d_927_cacheId_)
        d_928_valueOrError5_ = out167_
        if (d_928_valueOrError5_).IsFailure():
            res = (d_928_valueOrError5_).PropagateFailure()
            return res
        d_929_hierarchicalMaterials_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
        d_929_hierarchicalMaterials_ = (d_928_valueOrError5_).Extract()
        d_930_branchKey_: _dafny.Seq
        d_930_branchKey_ = (d_929_hierarchicalMaterials_).branchKey
        d_931_branchKeyVersion_: _dafny.Seq
        d_931_branchKeyVersion_ = (d_929_hierarchicalMaterials_).branchKeyVersion
        d_932_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_932_valueOrError6_ = (UTF8.default__.Decode(d_931_branchKeyVersion_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_932_valueOrError6_).IsFailure():
            res = (d_932_valueOrError6_).PropagateFailure()
            return res
        d_933_branchKeyVersionAsString_: _dafny.Seq
        d_933_branchKeyVersionAsString_ = (d_932_valueOrError6_).Extract()
        d_934_valueOrError7_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_934_valueOrError7_ = (UUID.default__.ToByteArray(d_933_branchKeyVersionAsString_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_934_valueOrError7_).IsFailure():
            res = (d_934_valueOrError7_).PropagateFailure()
            return res
        d_935_branchKeyVersionAsBytes_: _dafny.Seq
        d_935_branchKeyVersionAsBytes_ = (d_934_valueOrError7_).Extract()
        d_936_maybeCrypto_: Wrappers.Result
        out168_: Wrappers.Result
        out168_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_936_maybeCrypto_ = out168_
        d_937_valueOrError8_: Wrappers.Result = None
        def lambda73_(d_938_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_938_e_)

        d_937_valueOrError8_ = (d_936_maybeCrypto_).MapFailure(lambda73_)
        if (d_937_valueOrError8_).IsFailure():
            res = (d_937_valueOrError8_).PropagateFailure()
            return res
        d_939_cryptoPrimitivesX_: AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient
        d_939_cryptoPrimitivesX_ = (d_937_valueOrError8_).Extract()
        d_940_cryptoPrimitives_: AtomicPrimitives.AtomicPrimitivesClient
        d_940_cryptoPrimitives_ = d_939_cryptoPrimitivesX_
        d_941_kmsHierarchyUnwrap_: KmsHierarchyUnwrapKeyMaterial
        nw37_ = KmsHierarchyUnwrapKeyMaterial()
        nw37_.ctor__(d_930_branchKey_, d_918_branchKeyIdUtf8_, d_935_branchKeyVersionAsBytes_, d_940_cryptoPrimitives_)
        d_941_kmsHierarchyUnwrap_ = nw37_
        d_942_unwrapOutputRes_: Wrappers.Result
        out169_: Wrappers.Result
        out169_ = EdkWrapping.default__.UnwrapEdkMaterial((edk).ciphertext, (self).materials, d_941_kmsHierarchyUnwrap_)
        d_942_unwrapOutputRes_ = out169_
        d_943_valueOrError9_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.UnwrapEdkMaterialOutput.default(HierarchyUnwrapInfo.default()))()
        d_943_valueOrError9_ = d_942_unwrapOutputRes_
        if (d_943_valueOrError9_).IsFailure():
            res = (d_943_valueOrError9_).PropagateFailure()
            return res
        d_944_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_944_unwrapOutput_ = (d_943_valueOrError9_).Extract()
        d_945_valueOrError10_: Wrappers.Result = None
        d_945_valueOrError10_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_944_unwrapOutput_).plaintextDataKey, (d_944_unwrapOutput_).symmetricSigningKey)
        if (d_945_valueOrError10_).IsFailure():
            res = (d_945_valueOrError10_).PropagateFailure()
            return res
        d_946_result_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_946_result_ = (d_945_valueOrError10_).Extract()
        res = Wrappers.Result_Success(d_946_result_)
        return res
        return res

    def GetVersionCacheId(self, branchKeyIdUtf8, branchKeyVersion, cryptoPrimitives):
        cacheId: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_947_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        def iife24_(_pat_let7_0):
            def iife25_(d_948_branchKeyId_):
                return (True) and (((0) <= (len(d_948_branchKeyId_))) and ((len(d_948_branchKeyId_)) < (StandardLibrary_UInt.default__.UINT32__LIMIT)))
            return iife25_(_pat_let7_0)
        d_947_valueOrError0_ = Wrappers.default__.Need((((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).is_Success) and (iife24_(((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).value)), default__.E(_dafny.Seq("Invalid Branch Key ID Length")))
        if (d_947_valueOrError0_).IsFailure():
            cacheId = (d_947_valueOrError0_).PropagateFailure()
            return cacheId
        d_949_branchKeyId_: _dafny.Seq
        d_949_branchKeyId_ = (UTF8.default__.Decode(branchKeyIdUtf8)).value
        d_950_lenBranchKey_: _dafny.Seq
        d_950_lenBranchKey_ = StandardLibrary_UInt.default__.UInt32ToSeq(len(d_949_branchKeyId_))
        d_951_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_951_valueOrError1_ = Wrappers.default__.Need(UTF8.default__.IsASCIIString(branchKeyVersion), default__.E(_dafny.Seq("Unable to represent as an ASCII string.")))
        if (d_951_valueOrError1_).IsFailure():
            cacheId = (d_951_valueOrError1_).PropagateFailure()
            return cacheId
        d_952_versionBytes_: _dafny.Seq
        d_952_versionBytes_ = UTF8.default__.EncodeAscii(branchKeyVersion)
        d_953_identifier_: _dafny.Seq
        d_953_identifier_ = (((d_950_lenBranchKey_) + (branchKeyIdUtf8)) + (_dafny.Seq([0]))) + (d_952_versionBytes_)
        d_954_identifierDigestInput_: AwsCryptographyPrimitivesTypes.DigestInput
        d_954_identifierDigestInput_ = AwsCryptographyPrimitivesTypes.DigestInput_DigestInput(AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__512(), d_953_identifier_)
        d_955_maybeCacheDigest_: Wrappers.Result
        out170_: Wrappers.Result
        out170_ = Digest.default__.Digest(d_954_identifierDigestInput_)
        d_955_maybeCacheDigest_ = out170_
        d_956_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda74_(d_957_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_957_e_)

        d_956_valueOrError2_ = (d_955_maybeCacheDigest_).MapFailure(lambda74_)
        if (d_956_valueOrError2_).IsFailure():
            cacheId = (d_956_valueOrError2_).PropagateFailure()
            return cacheId
        d_958_cacheDigest_: _dafny.Seq
        d_958_cacheDigest_ = (d_956_valueOrError2_).Extract()
        cacheId = Wrappers.Result_Success(_dafny.Seq((d_958_cacheDigest_)[0:32:]))
        return cacheId
        return cacheId

    def GetHierarchicalMaterialsVersion(self, branchKeyId, branchKeyIdUtf8, version, cacheId):
        material: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.BranchKeyMaterials.default())()
        d_959_getCacheInput_: AwsCryptographyMaterialProvidersTypes.GetCacheEntryInput
        d_959_getCacheInput_ = AwsCryptographyMaterialProvidersTypes.GetCacheEntryInput_GetCacheEntryInput(cacheId, Wrappers.Option_None())
        d_960_getCacheOutput_: Wrappers.Result
        out171_: Wrappers.Result
        out171_ = default__.getEntry((self).cache, d_959_getCacheInput_)
        d_960_getCacheOutput_ = out171_
        if (d_960_getCacheOutput_).is_Failure:
            d_961_maybeGetBranchKeyVersionOutput_: Wrappers.Result
            out172_: Wrappers.Result
            out172_ = ((self).keyStore).GetBranchKeyVersion(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput_GetBranchKeyVersionInput(branchKeyId, version))
            d_961_maybeGetBranchKeyVersionOutput_ = out172_
            d_962_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
            def lambda75_(d_963_e_):
                return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyKeyStore(d_963_e_)

            d_962_valueOrError0_ = (d_961_maybeGetBranchKeyVersionOutput_).MapFailure(lambda75_)
            if (d_962_valueOrError0_).IsFailure():
                material = (d_962_valueOrError0_).PropagateFailure()
                return material
            d_964_getBranchKeyVersionOutput_: AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
            d_964_getBranchKeyVersionOutput_ = (d_962_valueOrError0_).Extract()
            d_965_branchKeyMaterials_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
            d_965_branchKeyMaterials_ = (d_964_getBranchKeyVersionOutput_).branchKeyMaterials
            d_966_now_: int
            out173_: int
            out173_ = Time.default__.CurrentRelativeTime()
            d_966_now_ = out173_
            d_967_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_967_valueOrError1_ = Wrappers.default__.Need(((d_966_now_) + ((self).ttlSeconds)) < (StandardLibrary_UInt.default__.INT64__MAX__LIMIT), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("INT64 Overflow when putting cache entry.")))
            if (d_967_valueOrError1_).IsFailure():
                material = (d_967_valueOrError1_).PropagateFailure()
                return material
            d_968_putCacheEntryInput_: AwsCryptographyMaterialProvidersTypes.PutCacheEntryInput
            d_968_putCacheEntryInput_ = AwsCryptographyMaterialProvidersTypes.PutCacheEntryInput_PutCacheEntryInput(cacheId, AwsCryptographyMaterialProvidersTypes.Materials_BranchKey(d_965_branchKeyMaterials_), d_966_now_, ((self).ttlSeconds) + (d_966_now_), Wrappers.Option_None(), Wrappers.Option_None())
            d_969_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
            out174_: Wrappers.Result
            out174_ = default__.putEntry((self).cache, d_968_putCacheEntryInput_)
            d_969_valueOrError2_ = out174_
            if (d_969_valueOrError2_).IsFailure():
                material = (d_969_valueOrError2_).PropagateFailure()
                return material
            d_970___v1_: tuple
            d_970___v1_ = (d_969_valueOrError2_).Extract()
            material = Wrappers.Result_Success(d_965_branchKeyMaterials_)
            return material
        elif True:
            d_971_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_971_valueOrError3_ = Wrappers.default__.Need(((((d_960_getCacheOutput_).value).materials).is_BranchKey) and ((((d_960_getCacheOutput_).value).materials) == (AwsCryptographyMaterialProvidersTypes.Materials_BranchKey((((d_960_getCacheOutput_).value).materials).BranchKey))), default__.E(_dafny.Seq("Invalid Material Type.")))
            if (d_971_valueOrError3_).IsFailure():
                material = (d_971_valueOrError3_).PropagateFailure()
                return material
            material = Wrappers.Result_Success((((d_960_getCacheOutput_).value).materials).BranchKey)
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
        d_972_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_972_suite_ = (input).algorithmSuite
        d_973_wrappedMaterial_: _dafny.Seq
        d_973_wrappedMaterial_ = (input).wrappedMaterial
        d_974_aad_: _dafny.Map
        d_974_aad_ = (input).encryptionContext
        d_975_KeyLength_: int
        d_975_KeyLength_ = AlgorithmSuites.default__.GetEncryptKeyLength(d_972_suite_)
        d_976_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_976_valueOrError0_ = Wrappers.default__.Need((len(d_973_wrappedMaterial_)) == ((default__.EXPECTED__EDK__CIPHERTEXT__OVERHEAD) + (d_975_KeyLength_)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received EDK Ciphertext of incorrect length2.")))
        if (d_976_valueOrError0_).IsFailure():
            res = (d_976_valueOrError0_).PropagateFailure()
            return res
        d_977_salt_: _dafny.Seq
        d_977_salt_ = _dafny.Seq((d_973_wrappedMaterial_)[0:default__.H__WRAP__SALT__LEN:])
        d_978_iv_: _dafny.Seq
        d_978_iv_ = _dafny.Seq((d_973_wrappedMaterial_)[default__.H__WRAP__SALT__LEN:default__.EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX:])
        d_979_branchKeyVersionUuid_: _dafny.Seq
        d_979_branchKeyVersionUuid_ = _dafny.Seq((d_973_wrappedMaterial_)[default__.EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX:default__.EDK__CIPHERTEXT__VERSION__INDEX:])
        d_980_wrappedKey_: _dafny.Seq
        d_980_wrappedKey_ = _dafny.Seq((d_973_wrappedMaterial_)[default__.EDK__CIPHERTEXT__VERSION__INDEX:(default__.EDK__CIPHERTEXT__VERSION__INDEX) + (d_975_KeyLength_):])
        d_981_authTag_: _dafny.Seq
        d_981_authTag_ = _dafny.Seq((d_973_wrappedMaterial_)[(default__.EDK__CIPHERTEXT__VERSION__INDEX) + (d_975_KeyLength_)::])
        d_982_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_982_valueOrError1_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_982_valueOrError1_).IsFailure():
            res = (d_982_valueOrError1_).PropagateFailure()
            return res
        d_983_serializedEC_: _dafny.Seq
        d_983_serializedEC_ = (d_982_valueOrError1_).Extract()
        d_984_wrappingAad_: _dafny.Seq
        d_984_wrappingAad_ = default__.WrappingAad((self).branchKeyIdUtf8, (self).branchKeyVersionAsBytes, d_983_serializedEC_)
        d_985_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out175_: Wrappers.Result
        out175_ = default__.DeriveEncryptionKeyFromBranchKey((self).branchKey, d_977_salt_, Wrappers.Option_Some(Constants.default__.PROVIDER__ID__HIERARCHY), (self).crypto)
        d_985_valueOrError2_ = out175_
        if (d_985_valueOrError2_).IsFailure():
            res = (d_985_valueOrError2_).PropagateFailure()
            return res
        d_986_derivedBranchKey_: _dafny.Seq
        d_986_derivedBranchKey_ = (d_985_valueOrError2_).Extract()
        d_987_maybeUnwrappedPdk_: Wrappers.Result
        out176_: Wrappers.Result
        out176_ = ((self).crypto).AESDecrypt(AwsCryptographyPrimitivesTypes.AESDecryptInput_AESDecryptInput(default__.AES__256__ENC__ALG, d_986_derivedBranchKey_, d_980_wrappedKey_, d_981_authTag_, d_978_iv_, d_984_wrappingAad_))
        d_987_maybeUnwrappedPdk_ = out176_
        d_988_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda76_(d_989_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_989_e_)

        d_988_valueOrError3_ = (d_987_maybeUnwrappedPdk_).MapFailure(lambda76_)
        if (d_988_valueOrError3_).IsFailure():
            res = (d_988_valueOrError3_).PropagateFailure()
            return res
        d_990_unwrappedPdk_: _dafny.Seq
        d_990_unwrappedPdk_ = (d_988_valueOrError3_).Extract()
        d_991_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_991_valueOrError4_ = Wrappers.default__.Need((len(d_990_unwrappedPdk_)) == (AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)), default__.E(_dafny.Seq("Invalid Key Length")))
        if (d_991_valueOrError4_).IsFailure():
            res = (d_991_valueOrError4_).PropagateFailure()
            return res
        d_992_output_: MaterialWrapping.UnwrapOutput
        d_992_output_ = MaterialWrapping.UnwrapOutput_UnwrapOutput(d_990_unwrappedPdk_, HierarchyUnwrapInfo_HierarchyUnwrapInfo())
        res = Wrappers.Result_Success(d_992_output_)
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
        d_993_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_993_suite_ = (input).algorithmSuite
        d_994_pdkResult_: Wrappers.Result
        out177_: Wrappers.Result
        out177_ = ((self).crypto).GenerateRandomBytes(AwsCryptographyPrimitivesTypes.GenerateRandomBytesInput_GenerateRandomBytesInput(AlgorithmSuites.default__.GetEncryptKeyLength(d_993_suite_)))
        d_994_pdkResult_ = out177_
        d_995_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda77_(d_996_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_996_e_)

        d_995_valueOrError0_ = (d_994_pdkResult_).MapFailure(lambda77_)
        if (d_995_valueOrError0_).IsFailure():
            res = (d_995_valueOrError0_).PropagateFailure()
            return res
        d_997_pdk_: _dafny.Seq
        d_997_pdk_ = (d_995_valueOrError0_).Extract()
        d_998_wrap_: KmsHierarchyWrapKeyMaterial
        nw38_ = KmsHierarchyWrapKeyMaterial()
        nw38_.ctor__((self).branchKey, (self).branchKeyIdUtf8, (self).branchKeyVersionAsBytes, (self).crypto)
        d_998_wrap_ = nw38_
        d_999_valueOrError1_: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.WrapOutput.default(HierarchyWrapInfo.default()))()
        out178_: Wrappers.Result
        out178_ = (d_998_wrap_).Invoke(MaterialWrapping.WrapInput_WrapInput(d_997_pdk_, (input).algorithmSuite, (input).encryptionContext))
        d_999_valueOrError1_ = out178_
        if (d_999_valueOrError1_).IsFailure():
            res = (d_999_valueOrError1_).PropagateFailure()
            return res
        d_1000_wrapOutput_: MaterialWrapping.WrapOutput
        d_1000_wrapOutput_ = (d_999_valueOrError1_).Extract()
        d_1001_output_: MaterialWrapping.GenerateAndWrapOutput
        d_1001_output_ = MaterialWrapping.GenerateAndWrapOutput_GenerateAndWrapOutput(d_997_pdk_, (d_1000_wrapOutput_).wrappedMaterial, HierarchyWrapInfo_HierarchyWrapInfo())
        res = Wrappers.Result_Success(d_1001_output_)
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
        d_1002_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_1002_suite_ = (input).algorithmSuite
        d_1003_maybeNonceSalt_: Wrappers.Result
        out179_: Wrappers.Result
        out179_ = ((self).crypto).GenerateRandomBytes(AwsCryptographyPrimitivesTypes.GenerateRandomBytesInput_GenerateRandomBytesInput((default__.H__WRAP__SALT__LEN) + (default__.H__WRAP__NONCE__LEN)))
        d_1003_maybeNonceSalt_ = out179_
        d_1004_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda78_(d_1005_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1005_e_)

        d_1004_valueOrError0_ = (d_1003_maybeNonceSalt_).MapFailure(lambda78_)
        if (d_1004_valueOrError0_).IsFailure():
            res = (d_1004_valueOrError0_).PropagateFailure()
            return res
        d_1006_saltAndNonce_: _dafny.Seq
        d_1006_saltAndNonce_ = (d_1004_valueOrError0_).Extract()
        d_1007_salt_: _dafny.Seq
        d_1007_salt_ = _dafny.Seq((d_1006_saltAndNonce_)[0:default__.H__WRAP__SALT__LEN:])
        d_1008_nonce_: _dafny.Seq
        d_1008_nonce_ = _dafny.Seq((d_1006_saltAndNonce_)[default__.H__WRAP__SALT__LEN::])
        d_1009_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1009_valueOrError1_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_1009_valueOrError1_).IsFailure():
            res = (d_1009_valueOrError1_).PropagateFailure()
            return res
        d_1010_serializedEC_: _dafny.Seq
        d_1010_serializedEC_ = (d_1009_valueOrError1_).Extract()
        d_1011_wrappingAad_: _dafny.Seq
        d_1011_wrappingAad_ = default__.WrappingAad((self).branchKeyIdUtf8, (self).branchKeyVersionAsBytes, d_1010_serializedEC_)
        d_1012_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out180_: Wrappers.Result
        out180_ = default__.DeriveEncryptionKeyFromBranchKey((self).branchKey, d_1007_salt_, Wrappers.Option_Some(Constants.default__.PROVIDER__ID__HIERARCHY), (self).crypto)
        d_1012_valueOrError2_ = out180_
        if (d_1012_valueOrError2_).IsFailure():
            res = (d_1012_valueOrError2_).PropagateFailure()
            return res
        d_1013_derivedBranchKey_: _dafny.Seq
        d_1013_derivedBranchKey_ = (d_1012_valueOrError2_).Extract()
        d_1014_maybeWrappedPdk_: Wrappers.Result
        out181_: Wrappers.Result
        out181_ = ((self).crypto).AESEncrypt(AwsCryptographyPrimitivesTypes.AESEncryptInput_AESEncryptInput(default__.AES__256__ENC__ALG, d_1008_nonce_, d_1013_derivedBranchKey_, (input).plaintextMaterial, d_1011_wrappingAad_))
        d_1014_maybeWrappedPdk_ = out181_
        d_1015_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.AESEncryptOutput.default())()
        def lambda79_(d_1016_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1016_e_)

        d_1015_valueOrError3_ = (d_1014_maybeWrappedPdk_).MapFailure(lambda79_)
        if (d_1015_valueOrError3_).IsFailure():
            res = (d_1015_valueOrError3_).PropagateFailure()
            return res
        d_1017_wrappedPdk_: AwsCryptographyPrimitivesTypes.AESEncryptOutput
        d_1017_wrappedPdk_ = (d_1015_valueOrError3_).Extract()
        d_1018_output_: MaterialWrapping.WrapOutput
        d_1018_output_ = MaterialWrapping.WrapOutput_WrapOutput(((((d_1007_salt_) + (d_1008_nonce_)) + ((self).branchKeyVersionAsBytes)) + ((d_1017_wrappedPdk_).cipherText)) + ((d_1017_wrappedPdk_).authTag), HierarchyWrapInfo_HierarchyWrapInfo())
        res = Wrappers.Result_Success(d_1018_output_)
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
