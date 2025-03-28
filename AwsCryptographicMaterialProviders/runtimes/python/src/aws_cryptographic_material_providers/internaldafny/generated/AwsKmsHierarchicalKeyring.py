import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptographic_material_providers.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import smithy_dafny_standard_library.internaldafny.generated.BoundedInts as BoundedInts
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_Sequence as StandardLibrary_Sequence
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import smithy_dafny_standard_library.internaldafny.generated.UTF8 as UTF8
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
import aws_cryptography_internal_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import aws_cryptography_internal_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
import smithy_dafny_standard_library.internaldafny.generated.Relations as Relations
import smithy_dafny_standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import smithy_dafny_standard_library.internaldafny.generated.Math as Math
import smithy_dafny_standard_library.internaldafny.generated.Seq as Seq
import smithy_dafny_standard_library.internaldafny.generated.Unicode as Unicode
import smithy_dafny_standard_library.internaldafny.generated.Functions as Functions
import smithy_dafny_standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import smithy_dafny_standard_library.internaldafny.generated.FileIO as FileIO
import smithy_dafny_standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import smithy_dafny_standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.MulInternals as MulInternals
import smithy_dafny_standard_library.internaldafny.generated.Mul as Mul
import smithy_dafny_standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.ModInternals as ModInternals
import smithy_dafny_standard_library.internaldafny.generated.DivInternals as DivInternals
import smithy_dafny_standard_library.internaldafny.generated.DivMod as DivMod
import smithy_dafny_standard_library.internaldafny.generated.Power as Power
import smithy_dafny_standard_library.internaldafny.generated.Logarithm as Logarithm
import smithy_dafny_standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import smithy_dafny_standard_library.internaldafny.generated.UUID as UUID
import smithy_dafny_standard_library.internaldafny.generated.OsLang as OsLang
import smithy_dafny_standard_library.internaldafny.generated.Time as Time
import smithy_dafny_standard_library.internaldafny.generated.Streams as Streams
import smithy_dafny_standard_library.internaldafny.generated.Sorting as Sorting
import smithy_dafny_standard_library.internaldafny.generated.SortedSets as SortedSets
import smithy_dafny_standard_library.internaldafny.generated.HexStrings as HexStrings
import smithy_dafny_standard_library.internaldafny.generated.GetOpt as GetOpt
import smithy_dafny_standard_library.internaldafny.generated.FloatCompare as FloatCompare
import smithy_dafny_standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import smithy_dafny_standard_library.internaldafny.generated.Base64 as Base64
import smithy_dafny_standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import smithy_dafny_standard_library.internaldafny.generated.Actions as Actions
import smithy_dafny_standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_material_providers.internaldafny.generated.KeyStoreErrorMessages as KeyStoreErrorMessages
import aws_cryptographic_material_providers.internaldafny.generated.KmsArn as KmsArn
import aws_cryptographic_material_providers.internaldafny.generated.Structure as Structure
import aws_cryptographic_material_providers.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_material_providers.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_material_providers.internaldafny.generated.CreateKeys as CreateKeys
import aws_cryptographic_material_providers.internaldafny.generated.CreateKeyStoreTable as CreateKeyStoreTable
import aws_cryptographic_material_providers.internaldafny.generated.GetKeys as GetKeys
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreOperations as AwsCryptographyKeyStoreOperations
import aws_cryptography_internal_kms.internaldafny.generated.Com_Amazonaws_Kms as Com_Amazonaws_Kms
import aws_cryptography_internal_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb
import aws_cryptographic_material_providers.internaldafny.generated.KeyStore as KeyStore
import aws_cryptographic_material_providers.internaldafny.generated.AlgorithmSuites as AlgorithmSuites
import aws_cryptographic_material_providers.internaldafny.generated.Materials as Materials
import aws_cryptographic_material_providers.internaldafny.generated.Keyring as Keyring
import aws_cryptographic_material_providers.internaldafny.generated.MultiKeyring as MultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkAreUnique as AwsKmsMrkAreUnique
import aws_cryptographic_material_providers.internaldafny.generated.Constants as Constants
import aws_cryptographic_material_providers.internaldafny.generated.MaterialWrapping as MaterialWrapping
import aws_cryptographic_material_providers.internaldafny.generated.CanonicalEncryptionContext as CanonicalEncryptionContext
import aws_cryptographic_material_providers.internaldafny.generated.IntermediateKeyWrapping as IntermediateKeyWrapping
import aws_cryptographic_material_providers.internaldafny.generated.EdkWrapping as EdkWrapping
import aws_cryptographic_material_providers.internaldafny.generated.ErrorMessages as ErrorMessages
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsKeyring as AwsKmsKeyring
import aws_cryptographic_material_providers.internaldafny.generated.StrictMultiKeyring as StrictMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsDiscoveryKeyring as AwsKmsDiscoveryKeyring
import aws_cryptographic_material_providers.internaldafny.generated.DiscoveryMultiKeyring as DiscoveryMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkDiscoveryKeyring as AwsKmsMrkDiscoveryKeyring
import aws_cryptographic_material_providers.internaldafny.generated.MrkAwareDiscoveryMultiKeyring as MrkAwareDiscoveryMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkKeyring as AwsKmsMrkKeyring
import aws_cryptographic_material_providers.internaldafny.generated.MrkAwareStrictMultiKeyring as MrkAwareStrictMultiKeyring
import aws_cryptographic_material_providers.internaldafny.generated.LocalCMC as LocalCMC
import aws_cryptographic_material_providers.internaldafny.generated.SynchronizedLocalCMC as SynchronizedLocalCMC
import aws_cryptographic_material_providers.internaldafny.generated.StormTracker as StormTracker
import aws_cryptographic_material_providers.internaldafny.generated.StormTrackingCMC as StormTrackingCMC
import aws_cryptographic_material_providers.internaldafny.generated.CacheConstants as CacheConstants

# Module: AwsKmsHierarchicalKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def cacheEntryWithinLimits(creationTime, now, ttlSeconds):
        return ((now) - (creationTime)) <= (ttlSeconds)

    @staticmethod
    def DeriveEncryptionKeyFromBranchKey(branchKey, salt, purpose, cryptoPrimitives):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_0_maybeDerivedBranchKey_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = (cryptoPrimitives).KdfCounterMode(AwsCryptographyPrimitivesTypes.KdfCtrInput_KdfCtrInput(AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__256(), branchKey, default__.DERIVED__BRANCH__KEY__EXPECTED__LENGTH, purpose, Wrappers.Option_Some(salt)))
        d_0_maybeDerivedBranchKey_ = out0_
        d_1_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda0_(d_2_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_2_e_)

        d_1_valueOrError0_ = (d_0_maybeDerivedBranchKey_).MapFailure(lambda0_)
        if (d_1_valueOrError0_).IsFailure():
            output = (d_1_valueOrError0_).PropagateFailure()
            return output
        d_3_derivedBranchKey_: _dafny.Seq
        d_3_derivedBranchKey_ = (d_1_valueOrError0_).Extract()
        output = Wrappers.Result_Success(d_3_derivedBranchKey_)
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
    def EXPRESSION__ATTRIBUTE__VALUE__STATUS__VALUE(instance):
        return _dafny.Seq("ACTIVE")
    @_dafny.classproperty
    def EXPRESSION__ATTRIBUTE__VALUE__BRANCH__KEY(instance):
        return _dafny.Seq(":branch_key_id")

class AwsKmsHierarchicalKeyring(Keyring.VerifiableInterface, AwsCryptographyMaterialProvidersTypes.IKeyring):
    def  __init__(self):
        self._keyStore: AwsCryptographyKeyStoreTypes.IKeyStoreClient = None
        self._cryptoPrimitives: AtomicPrimitives.AtomicPrimitivesClient = None
        self._cache: AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsCache = None
        self._branchKeyIdSupplier: Wrappers.Option = Wrappers.Option.default()()
        self._branchKeyId: Wrappers.Option = Wrappers.Option.default()()
        self._ttlSeconds: int = None
        self._partitionIdBytes: _dafny.Seq = _dafny.Seq({})
        self._logicalKeyStoreNameBytes: _dafny.Seq = _dafny.Seq({})
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsHierarchicalKeyring.AwsKmsHierarchicalKeyring"
    def OnDecrypt(self, input):
        out6_: Wrappers.Result
        out6_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnDecrypt(self, input)
        return out6_

    def OnEncrypt(self, input):
        out6_: Wrappers.Result
        out6_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnEncrypt(self, input)
        return out6_

    def ctor__(self, keyStore, branchKeyId, branchKeyIdSupplier, ttlSeconds, cmc, partitionIdBytes, logicalKeyStoreNameBytes, cryptoPrimitives):
        (self)._keyStore = keyStore
        (self)._branchKeyId = branchKeyId
        (self)._branchKeyIdSupplier = branchKeyIdSupplier
        (self)._ttlSeconds = ttlSeconds
        (self)._cryptoPrimitives = cryptoPrimitives
        (self)._cache = cmc
        (self)._partitionIdBytes = partitionIdBytes
        (self)._logicalKeyStoreNameBytes = logicalKeyStoreNameBytes

    def GetBranchKeyId(self, context):
        ret: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        if ((self).branchKeyId).is_Some:
            ret = Wrappers.Result_Success(((self).branchKeyId).value)
            return ret
        elif True:
            d_0_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyMaterialProvidersTypes.GetBranchKeyIdOutput.default())()
            out0_: Wrappers.Result
            out0_ = (((self).branchKeyIdSupplier).value).GetBranchKeyId(AwsCryptographyMaterialProvidersTypes.GetBranchKeyIdInput_GetBranchKeyIdInput(context))
            d_0_valueOrError0_ = out0_
            if (d_0_valueOrError0_).IsFailure():
                ret = (d_0_valueOrError0_).PropagateFailure()
                return ret
            d_1_GetBranchKeyIdOut_: AwsCryptographyMaterialProvidersTypes.GetBranchKeyIdOutput
            d_1_GetBranchKeyIdOut_ = (d_0_valueOrError0_).Extract()
            ret = Wrappers.Result_Success((d_1_GetBranchKeyIdOut_).branchKeyId)
            return ret
        return ret

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        d_0_materials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_0_materials_ = (input).materials
        d_1_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_1_suite_ = (d_0_materials_).algorithmSuite
        d_2_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out0_: Wrappers.Result
        out0_ = (self).GetBranchKeyId((d_0_materials_).encryptionContext)
        d_2_valueOrError0_ = out0_
        if (d_2_valueOrError0_).IsFailure():
            res = (d_2_valueOrError0_).PropagateFailure()
            return res
        d_3_branchKeyIdForEncrypt_: _dafny.Seq
        d_3_branchKeyIdForEncrypt_ = (d_2_valueOrError0_).Extract()
        d_4_valueOrError1_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_4_valueOrError1_ = (UTF8.default__.Encode(d_3_branchKeyIdForEncrypt_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_4_valueOrError1_).IsFailure():
            res = (d_4_valueOrError1_).PropagateFailure()
            return res
        d_5_branchKeyIdUtf8_: _dafny.Seq
        d_5_branchKeyIdUtf8_ = (d_4_valueOrError1_).Extract()
        d_6_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out1_: Wrappers.Result
        out1_ = (self).GetActiveCacheId(d_3_branchKeyIdForEncrypt_, d_5_branchKeyIdUtf8_, (self).cryptoPrimitives)
        d_6_valueOrError2_ = out1_
        if (d_6_valueOrError2_).IsFailure():
            res = (d_6_valueOrError2_).PropagateFailure()
            return res
        d_7_cacheId_: _dafny.Seq
        d_7_cacheId_ = (d_6_valueOrError2_).Extract()
        d_8_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.BranchKeyMaterials.default())()
        out2_: Wrappers.Result
        out2_ = (self).GetActiveHierarchicalMaterials(d_3_branchKeyIdForEncrypt_, d_7_cacheId_, (self).keyStore)
        d_8_valueOrError3_ = out2_
        if (d_8_valueOrError3_).IsFailure():
            res = (d_8_valueOrError3_).PropagateFailure()
            return res
        d_9_hierarchicalMaterials_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
        d_9_hierarchicalMaterials_ = (d_8_valueOrError3_).Extract()
        d_10_branchKey_: _dafny.Seq
        d_10_branchKey_ = (d_9_hierarchicalMaterials_).branchKey
        d_11_branchKeyVersion_: _dafny.Seq
        d_11_branchKeyVersion_ = (d_9_hierarchicalMaterials_).branchKeyVersion
        d_12_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_12_valueOrError4_ = (UTF8.default__.Decode(d_11_branchKeyVersion_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_12_valueOrError4_).IsFailure():
            res = (d_12_valueOrError4_).PropagateFailure()
            return res
        d_13_branchKeyVersionAsString_: _dafny.Seq
        d_13_branchKeyVersionAsString_ = (d_12_valueOrError4_).Extract()
        d_14_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_14_valueOrError5_ = (UUID.default__.ToByteArray(d_13_branchKeyVersionAsString_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_14_valueOrError5_).IsFailure():
            res = (d_14_valueOrError5_).PropagateFailure()
            return res
        d_15_branchKeyVersionAsBytes_: _dafny.Seq
        d_15_branchKeyVersionAsBytes_ = (d_14_valueOrError5_).Extract()
        d_16_kmsHierarchyGenerateAndWrap_: KmsHierarchyGenerateAndWrapKeyMaterial
        nw0_ = KmsHierarchyGenerateAndWrapKeyMaterial()
        nw0_.ctor__((d_9_hierarchicalMaterials_).branchKey, d_5_branchKeyIdUtf8_, d_15_branchKeyVersionAsBytes_, (self).cryptoPrimitives)
        d_16_kmsHierarchyGenerateAndWrap_ = nw0_
        d_17_kmsHierarchyWrap_: KmsHierarchyWrapKeyMaterial
        nw1_ = KmsHierarchyWrapKeyMaterial()
        nw1_.ctor__((d_9_hierarchicalMaterials_).branchKey, d_5_branchKeyIdUtf8_, d_15_branchKeyVersionAsBytes_, (self).cryptoPrimitives)
        d_17_kmsHierarchyWrap_ = nw1_
        d_18_valueOrError6_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.WrapEdkMaterialOutput.default(HierarchyWrapInfo.default()))()
        out3_: Wrappers.Result
        out3_ = EdkWrapping.default__.WrapEdkMaterial(d_0_materials_, d_17_kmsHierarchyWrap_, d_16_kmsHierarchyGenerateAndWrap_)
        d_18_valueOrError6_ = out3_
        if (d_18_valueOrError6_).IsFailure():
            res = (d_18_valueOrError6_).PropagateFailure()
            return res
        d_19_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_19_wrapOutput_ = (d_18_valueOrError6_).Extract()
        d_20_symmetricSigningKeyList_: Wrappers.Option
        if ((d_19_wrapOutput_).symmetricSigningKey).is_Some:
            d_20_symmetricSigningKeyList_ = Wrappers.Option_Some(_dafny.Seq([((d_19_wrapOutput_).symmetricSigningKey).value]))
        elif True:
            d_20_symmetricSigningKeyList_ = Wrappers.Option_None()
        d_21_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_21_edk_ = AwsCryptographyMaterialProvidersTypes.EncryptedDataKey_EncryptedDataKey(Constants.default__.PROVIDER__ID__HIERARCHY, d_5_branchKeyIdUtf8_, (d_19_wrapOutput_).wrappedMaterial)
        if (d_19_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_22_valueOrError7_: Wrappers.Result = None
            d_22_valueOrError7_ = Materials.default__.EncryptionMaterialAddDataKey(d_0_materials_, (d_19_wrapOutput_).plaintextDataKey, _dafny.Seq([d_21_edk_]), d_20_symmetricSigningKeyList_)
            if (d_22_valueOrError7_).IsFailure():
                res = (d_22_valueOrError7_).PropagateFailure()
                return res
            d_23_result_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_23_result_ = (d_22_valueOrError7_).Extract()
            res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(d_23_result_))
            return res
        elif (d_19_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_24_valueOrError8_: Wrappers.Result = None
            d_24_valueOrError8_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys(d_0_materials_, _dafny.Seq([d_21_edk_]), d_20_symmetricSigningKeyList_)
            if (d_24_valueOrError8_).IsFailure():
                res = (d_24_valueOrError8_).PropagateFailure()
                return res
            d_25_result_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_25_result_ = (d_24_valueOrError8_).Extract()
            res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(d_25_result_))
            return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        d_0_materials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_0_materials_ = (input).materials
        d_1_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_1_suite_ = ((input).materials).algorithmSuite
        d_2_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_2_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_0_materials_), default__.E(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_2_valueOrError0_).IsFailure():
            res = (d_2_valueOrError0_).PropagateFailure()
            return res
        d_3_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out0_: Wrappers.Result
        out0_ = (self).GetBranchKeyId((d_0_materials_).encryptionContext)
        d_3_valueOrError1_ = out0_
        if (d_3_valueOrError1_).IsFailure():
            res = (d_3_valueOrError1_).PropagateFailure()
            return res
        d_4_branchKeyIdForDecrypt_: _dafny.Seq
        d_4_branchKeyIdForDecrypt_ = (d_3_valueOrError1_).Extract()
        d_5_filter_: OnDecryptHierarchyEncryptedDataKeyFilter
        nw0_ = OnDecryptHierarchyEncryptedDataKeyFilter()
        nw0_.ctor__(d_4_branchKeyIdForDecrypt_)
        d_5_filter_ = nw0_
        d_6_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out1_: Wrappers.Result
        out1_ = Actions.default__.FilterWithResult(d_5_filter_, (input).encryptedDataKeys)
        d_6_valueOrError2_ = out1_
        if (d_6_valueOrError2_).IsFailure():
            res = (d_6_valueOrError2_).PropagateFailure()
            return res
        d_7_edksToAttempt_: _dafny.Seq
        d_7_edksToAttempt_ = (d_6_valueOrError2_).Extract()
        if (0) == (len(d_7_edksToAttempt_)):
            d_8_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            d_8_valueOrError3_ = ErrorMessages.default__.IncorrectDataKeys((input).encryptedDataKeys, ((input).materials).algorithmSuite, _dafny.Seq(""))
            if (d_8_valueOrError3_).IsFailure():
                res = (d_8_valueOrError3_).PropagateFailure()
                return res
            d_9_errorMessage_: _dafny.Seq
            d_9_errorMessage_ = (d_8_valueOrError3_).Extract()
            res = Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(d_9_errorMessage_))
            return res
        d_10_decryptClosure_: Actions.ActionWithResult
        nw1_ = DecryptSingleEncryptedDataKey()
        nw1_.ctor__(d_0_materials_, (self).keyStore, (self).cryptoPrimitives, d_4_branchKeyIdForDecrypt_, (self).ttlSeconds, (self).cache, (self).partitionIdBytes, (self).logicalKeyStoreNameBytes)
        d_10_decryptClosure_ = nw1_
        d_11_outcome_: Wrappers.Result
        out2_: Wrappers.Result
        out2_ = Actions.default__.ReduceToSuccess(d_10_decryptClosure_, d_7_edksToAttempt_)
        d_11_outcome_ = out2_
        d_12_valueOrError4_: Wrappers.Result = None
        def lambda0_(d_13_errors_):
            return AwsCryptographyMaterialProvidersTypes.Error_CollectionOfErrors(d_13_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."))

        d_12_valueOrError4_ = (d_11_outcome_).MapFailure(lambda0_)
        if (d_12_valueOrError4_).IsFailure():
            res = (d_12_valueOrError4_).PropagateFailure()
            return res
        d_14_SealedDecryptionMaterials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_14_SealedDecryptionMaterials_ = (d_12_valueOrError4_).Extract()
        res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnDecryptOutput_OnDecryptOutput(d_14_SealedDecryptionMaterials_))
        return res
        return res

    def GetActiveCacheId(self, branchKeyId, branchKeyIdUtf8, cryptoPrimitives):
        cacheId: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_0_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        def iife0_(_pat_let6_0):
            def iife1_(d_1_branchKeyId_):
                return (True) and (((0) <= (len(d_1_branchKeyId_))) and ((len(d_1_branchKeyId_)) < (StandardLibrary_UInt.default__.UINT32__LIMIT)))
            return iife1_(_pat_let6_0)
        d_0_valueOrError0_ = Wrappers.default__.Need((((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).is_Success) and (iife0_(((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).value)), default__.E(_dafny.Seq("Invalid Branch Key ID Length")))
        if (d_0_valueOrError0_).IsFailure():
            cacheId = (d_0_valueOrError0_).PropagateFailure()
            return cacheId
        d_2_hashAlgorithm_: AwsCryptographyPrimitivesTypes.DigestAlgorithm
        d_2_hashAlgorithm_ = AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__384()
        d_3_resourceId_: _dafny.Seq
        d_3_resourceId_ = CacheConstants.default__.RESOURCE__ID__HIERARCHICAL__KEYRING
        d_4_scopeId_: _dafny.Seq
        d_4_scopeId_ = CacheConstants.default__.SCOPE__ID__ENCRYPT
        d_5_suffix_: _dafny.Seq
        d_5_suffix_ = (((self).logicalKeyStoreNameBytes) + (CacheConstants.default__.NULL__BYTE)) + (branchKeyIdUtf8)
        d_6_identifier_: _dafny.Seq
        d_6_identifier_ = ((((((d_3_resourceId_) + (CacheConstants.default__.NULL__BYTE)) + (d_4_scopeId_)) + (CacheConstants.default__.NULL__BYTE)) + ((self).partitionIdBytes)) + (CacheConstants.default__.NULL__BYTE)) + (d_5_suffix_)
        d_7_maybeCacheIdDigest_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = (cryptoPrimitives).Digest(AwsCryptographyPrimitivesTypes.DigestInput_DigestInput(d_2_hashAlgorithm_, d_6_identifier_))
        d_7_maybeCacheIdDigest_ = out0_
        d_8_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda0_(d_9_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_9_e_)

        d_8_valueOrError1_ = (d_7_maybeCacheIdDigest_).MapFailure(lambda0_)
        if (d_8_valueOrError1_).IsFailure():
            cacheId = (d_8_valueOrError1_).PropagateFailure()
            return cacheId
        d_10_cacheDigest_: _dafny.Seq
        d_10_cacheDigest_ = (d_8_valueOrError1_).Extract()
        d_11_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_11_valueOrError2_ = Wrappers.default__.Need((len(d_10_cacheDigest_)) == (Digest.default__.Length(d_2_hashAlgorithm_)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Digest generated a message not equal to the expected length.")))
        if (d_11_valueOrError2_).IsFailure():
            cacheId = (d_11_valueOrError2_).PropagateFailure()
            return cacheId
        cacheId = Wrappers.Result_Success(d_10_cacheDigest_)
        return cacheId
        return cacheId

    def GetActiveHierarchicalMaterials(self, branchKeyId, cacheId, keyStore):
        material: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.BranchKeyMaterials.default())()
        d_0_getCacheInput_: AwsCryptographyMaterialProvidersTypes.GetCacheEntryInput
        d_0_getCacheInput_ = AwsCryptographyMaterialProvidersTypes.GetCacheEntryInput_GetCacheEntryInput(cacheId, Wrappers.Option_None())
        d_1_getCacheOutput_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = ((self).cache).GetCacheEntry(d_0_getCacheInput_)
        d_1_getCacheOutput_ = out0_
        if ((d_1_getCacheOutput_).is_Failure) and (not(((d_1_getCacheOutput_).error).is_EntryDoesNotExist)):
            material = Wrappers.Result_Failure((d_1_getCacheOutput_).error)
            return material
        d_2_now_: int
        out1_: int
        out1_ = Time.default__.CurrentRelativeTime()
        d_2_now_ = out1_
        if ((d_1_getCacheOutput_).is_Failure) or (not(default__.cacheEntryWithinLimits(((d_1_getCacheOutput_).value).creationTime, d_2_now_, (self).ttlSeconds))):
            d_3_maybeGetActiveBranchKeyOutput_: Wrappers.Result
            out2_: Wrappers.Result
            out2_ = (keyStore).GetActiveBranchKey(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyInput_GetActiveBranchKeyInput(branchKeyId))
            d_3_maybeGetActiveBranchKeyOutput_ = out2_
            d_4_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput.default())()
            def lambda0_(d_5_e_):
                return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyKeyStore(d_5_e_)

            d_4_valueOrError0_ = (d_3_maybeGetActiveBranchKeyOutput_).MapFailure(lambda0_)
            if (d_4_valueOrError0_).IsFailure():
                material = (d_4_valueOrError0_).PropagateFailure()
                return material
            d_6_getActiveBranchKeyOutput_: AwsCryptographyKeyStoreTypes.GetActiveBranchKeyOutput
            d_6_getActiveBranchKeyOutput_ = (d_4_valueOrError0_).Extract()
            d_7_branchKeyMaterials_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
            d_7_branchKeyMaterials_ = (d_6_getActiveBranchKeyOutput_).branchKeyMaterials
            d_8_now_: int
            out3_: int
            out3_ = Time.default__.CurrentRelativeTime()
            d_8_now_ = out3_
            d_9_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_9_valueOrError1_ = Wrappers.default__.Need(((d_8_now_) + ((self).ttlSeconds)) < (StandardLibrary_UInt.default__.INT64__MAX__LIMIT), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("INT64 Overflow when putting cache entry.")))
            if (d_9_valueOrError1_).IsFailure():
                material = (d_9_valueOrError1_).PropagateFailure()
                return material
            d_10_putCacheEntryInput_: AwsCryptographyMaterialProvidersTypes.PutCacheEntryInput
            d_10_putCacheEntryInput_ = AwsCryptographyMaterialProvidersTypes.PutCacheEntryInput_PutCacheEntryInput(cacheId, AwsCryptographyMaterialProvidersTypes.Materials_BranchKey(d_7_branchKeyMaterials_), d_8_now_, ((self).ttlSeconds) + (d_8_now_), Wrappers.Option_None(), Wrappers.Option_None())
            d_11_putResult_: Wrappers.Result
            out4_: Wrappers.Result
            out4_ = ((self).cache).PutCacheEntry(d_10_putCacheEntryInput_)
            d_11_putResult_ = out4_
            if ((d_11_putResult_).is_Failure) and (not(((d_11_putResult_).error).is_EntryAlreadyExists)):
                material = Wrappers.Result_Failure((d_11_putResult_).error)
                return material
            material = Wrappers.Result_Success(d_7_branchKeyMaterials_)
            return material
        elif True:
            d_12_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_12_valueOrError2_ = Wrappers.default__.Need(((((d_1_getCacheOutput_).value).materials).is_BranchKey) and ((((d_1_getCacheOutput_).value).materials) == (AwsCryptographyMaterialProvidersTypes.Materials_BranchKey((((d_1_getCacheOutput_).value).materials).BranchKey))), default__.E(_dafny.Seq("Invalid Material Type.")))
            if (d_12_valueOrError2_).IsFailure():
                material = (d_12_valueOrError2_).PropagateFailure()
                return material
            material = Wrappers.Result_Success((((d_1_getCacheOutput_).value).materials).BranchKey)
            return material
        return material

    @property
    def keyStore(self):
        return self._keyStore
    @property
    def cryptoPrimitives(self):
        return self._cryptoPrimitives
    @property
    def cache(self):
        return self._cache
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
    def partitionIdBytes(self):
        return self._partitionIdBytes
    @property
    def logicalKeyStoreNameBytes(self):
        return self._logicalKeyStoreNameBytes

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
        d_0_providerInfo_: _dafny.Seq
        d_0_providerInfo_ = (edk).keyProviderInfo
        d_1_providerId_: _dafny.Seq
        d_1_providerId_ = (edk).keyProviderId
        if (d_1_providerId_) != (Constants.default__.PROVIDER__ID__HIERARCHY):
            res = Wrappers.Result_Success(False)
            return res
        if not(UTF8.default__.ValidUTF8Seq(d_0_providerInfo_)):
            res = Wrappers.Result_Failure(default__.E(_dafny.Seq("Invalid encoding, provider info is not UTF8.")))
            return res
        d_2_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_2_valueOrError0_ = (UTF8.default__.Decode(d_0_providerInfo_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_2_valueOrError0_).IsFailure():
            res = (d_2_valueOrError0_).PropagateFailure()
            return res
        d_3_branchKeyId_: _dafny.Seq
        d_3_branchKeyId_ = (d_2_valueOrError0_).Extract()
        res = Wrappers.Result_Success(((self).branchKeyId) == (d_3_branchKeyId_))
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
        self._partitionIdBytes: _dafny.Seq = _dafny.Seq({})
        self._logicalKeyStoreNameBytes: _dafny.Seq = _dafny.Seq({})
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsHierarchicalKeyring.DecryptSingleEncryptedDataKey"
    def ctor__(self, materials, keyStore, cryptoPrimitives, branchKeyId, ttlSeconds, cache, partitionIdBytes, logicalKeyStoreNameBytes):
        (self)._materials = materials
        (self)._keyStore = keyStore
        (self)._cryptoPrimitives = cryptoPrimitives
        (self)._branchKeyId = branchKeyId
        (self)._ttlSeconds = ttlSeconds
        (self)._cache = cache
        (self)._partitionIdBytes = partitionIdBytes
        (self)._logicalKeyStoreNameBytes = logicalKeyStoreNameBytes

    def Invoke(self, edk):
        res: Wrappers.Result = None
        d_0_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_0_valueOrError0_ = Wrappers.default__.Need(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received invalid EDK provider info for Hierarchical Keyring")))
        if (d_0_valueOrError0_).IsFailure():
            res = (d_0_valueOrError0_).PropagateFailure()
            return res
        d_1_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_1_suite_ = ((self).materials).algorithmSuite
        d_2_keyProviderId_: _dafny.Seq
        d_2_keyProviderId_ = (edk).keyProviderId
        d_3_branchKeyIdUtf8_: _dafny.Seq
        d_3_branchKeyIdUtf8_ = (edk).keyProviderInfo
        d_4_ciphertext_: _dafny.Seq
        d_4_ciphertext_ = (edk).ciphertext
        d_5_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_5_valueOrError1_ = EdkWrapping.default__.GetProviderWrappedMaterial(d_4_ciphertext_, d_1_suite_)
        if (d_5_valueOrError1_).IsFailure():
            res = (d_5_valueOrError1_).PropagateFailure()
            return res
        d_6_providerWrappedMaterial_: _dafny.Seq
        d_6_providerWrappedMaterial_ = (d_5_valueOrError1_).Extract()
        d_7_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_7_valueOrError2_ = Wrappers.default__.Need((len(d_6_providerWrappedMaterial_)) >= (default__.EDK__CIPHERTEXT__VERSION__INDEX), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received EDK Ciphertext of incorrect length.")))
        if (d_7_valueOrError2_).IsFailure():
            res = (d_7_valueOrError2_).PropagateFailure()
            return res
        d_8_branchKeyVersionUuid_: _dafny.Seq
        d_8_branchKeyVersionUuid_ = _dafny.Seq((d_6_providerWrappedMaterial_)[default__.EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX:default__.EDK__CIPHERTEXT__VERSION__INDEX:])
        d_9_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_9_valueOrError3_ = (UUID.default__.FromByteArray(d_8_branchKeyVersionUuid_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_9_valueOrError3_).IsFailure():
            res = (d_9_valueOrError3_).PropagateFailure()
            return res
        d_10_version_: _dafny.Seq
        d_10_version_ = (d_9_valueOrError3_).Extract()
        d_11_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out0_: Wrappers.Result
        out0_ = (self).GetVersionCacheId(d_3_branchKeyIdUtf8_, d_10_version_, (self).cryptoPrimitives)
        d_11_valueOrError4_ = out0_
        if (d_11_valueOrError4_).IsFailure():
            res = (d_11_valueOrError4_).PropagateFailure()
            return res
        d_12_cacheId_: _dafny.Seq
        d_12_cacheId_ = (d_11_valueOrError4_).Extract()
        d_13_valueOrError5_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.BranchKeyMaterials.default())()
        out1_: Wrappers.Result
        out1_ = (self).GetHierarchicalMaterialsVersion((self).branchKeyId, d_3_branchKeyIdUtf8_, d_10_version_, d_12_cacheId_)
        d_13_valueOrError5_ = out1_
        if (d_13_valueOrError5_).IsFailure():
            res = (d_13_valueOrError5_).PropagateFailure()
            return res
        d_14_hierarchicalMaterials_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
        d_14_hierarchicalMaterials_ = (d_13_valueOrError5_).Extract()
        d_15_branchKey_: _dafny.Seq
        d_15_branchKey_ = (d_14_hierarchicalMaterials_).branchKey
        d_16_branchKeyVersion_: _dafny.Seq
        d_16_branchKeyVersion_ = (d_14_hierarchicalMaterials_).branchKeyVersion
        d_17_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_17_valueOrError6_ = (UTF8.default__.Decode(d_16_branchKeyVersion_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_17_valueOrError6_).IsFailure():
            res = (d_17_valueOrError6_).PropagateFailure()
            return res
        d_18_branchKeyVersionAsString_: _dafny.Seq
        d_18_branchKeyVersionAsString_ = (d_17_valueOrError6_).Extract()
        d_19_valueOrError7_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_19_valueOrError7_ = (UUID.default__.ToByteArray(d_18_branchKeyVersionAsString_)).MapFailure(AwsKmsUtils.default__.WrapStringToError)
        if (d_19_valueOrError7_).IsFailure():
            res = (d_19_valueOrError7_).PropagateFailure()
            return res
        d_20_branchKeyVersionAsBytes_: _dafny.Seq
        d_20_branchKeyVersionAsBytes_ = (d_19_valueOrError7_).Extract()
        d_21_maybeCrypto_: Wrappers.Result
        out2_: Wrappers.Result
        out2_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_21_maybeCrypto_ = out2_
        d_22_valueOrError8_: Wrappers.Result = None
        def lambda0_(d_23_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_23_e_)

        d_22_valueOrError8_ = (d_21_maybeCrypto_).MapFailure(lambda0_)
        if (d_22_valueOrError8_).IsFailure():
            res = (d_22_valueOrError8_).PropagateFailure()
            return res
        d_24_cryptoPrimitivesX_: AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient
        d_24_cryptoPrimitivesX_ = (d_22_valueOrError8_).Extract()
        d_25_cryptoPrimitives_: AtomicPrimitives.AtomicPrimitivesClient
        d_25_cryptoPrimitives_ = d_24_cryptoPrimitivesX_
        d_26_kmsHierarchyUnwrap_: KmsHierarchyUnwrapKeyMaterial
        nw0_ = KmsHierarchyUnwrapKeyMaterial()
        nw0_.ctor__(d_15_branchKey_, d_3_branchKeyIdUtf8_, d_20_branchKeyVersionAsBytes_, d_25_cryptoPrimitives_)
        d_26_kmsHierarchyUnwrap_ = nw0_
        d_27_unwrapOutputRes_: Wrappers.Result
        out3_: Wrappers.Result
        out3_ = EdkWrapping.default__.UnwrapEdkMaterial((edk).ciphertext, (self).materials, d_26_kmsHierarchyUnwrap_)
        d_27_unwrapOutputRes_ = out3_
        d_28_valueOrError9_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.UnwrapEdkMaterialOutput.default(HierarchyUnwrapInfo.default()))()
        d_28_valueOrError9_ = d_27_unwrapOutputRes_
        if (d_28_valueOrError9_).IsFailure():
            res = (d_28_valueOrError9_).PropagateFailure()
            return res
        d_29_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_29_unwrapOutput_ = (d_28_valueOrError9_).Extract()
        d_30_valueOrError10_: Wrappers.Result = None
        d_30_valueOrError10_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_29_unwrapOutput_).plaintextDataKey, (d_29_unwrapOutput_).symmetricSigningKey)
        if (d_30_valueOrError10_).IsFailure():
            res = (d_30_valueOrError10_).PropagateFailure()
            return res
        d_31_result_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_31_result_ = (d_30_valueOrError10_).Extract()
        res = Wrappers.Result_Success(d_31_result_)
        return res
        return res

    def GetVersionCacheId(self, branchKeyIdUtf8, branchKeyVersion, cryptoPrimitives):
        cacheId: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_0_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        def iife0_(_pat_let7_0):
            def iife1_(d_1_branchKeyId_):
                return (True) and (((0) <= (len(d_1_branchKeyId_))) and ((len(d_1_branchKeyId_)) < (StandardLibrary_UInt.default__.UINT32__LIMIT)))
            return iife1_(_pat_let7_0)
        d_0_valueOrError0_ = Wrappers.default__.Need((((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).is_Success) and (iife0_(((UTF8.default__.Decode(branchKeyIdUtf8)).MapFailure(AwsKmsUtils.default__.WrapStringToError)).value)), default__.E(_dafny.Seq("Invalid Branch Key ID Length")))
        if (d_0_valueOrError0_).IsFailure():
            cacheId = (d_0_valueOrError0_).PropagateFailure()
            return cacheId
        d_2_hashAlgorithm_: AwsCryptographyPrimitivesTypes.DigestAlgorithm
        d_2_hashAlgorithm_ = AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__384()
        d_3_resourceId_: _dafny.Seq
        d_3_resourceId_ = CacheConstants.default__.RESOURCE__ID__HIERARCHICAL__KEYRING
        d_4_scopeId_: _dafny.Seq
        d_4_scopeId_ = CacheConstants.default__.SCOPE__ID__DECRYPT
        d_5_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_5_valueOrError1_ = Wrappers.default__.Need(UTF8.default__.IsASCIIString(branchKeyVersion), default__.E(_dafny.Seq("Unable to represent as an ASCII string.")))
        if (d_5_valueOrError1_).IsFailure():
            cacheId = (d_5_valueOrError1_).PropagateFailure()
            return cacheId
        d_6_versionBytes_: _dafny.Seq
        d_6_versionBytes_ = UTF8.default__.EncodeAscii(branchKeyVersion)
        d_7_suffix_: _dafny.Seq
        d_7_suffix_ = (((((self).logicalKeyStoreNameBytes) + (CacheConstants.default__.NULL__BYTE)) + (branchKeyIdUtf8)) + (CacheConstants.default__.NULL__BYTE)) + (d_6_versionBytes_)
        d_8_identifier_: _dafny.Seq
        d_8_identifier_ = ((((((d_3_resourceId_) + (CacheConstants.default__.NULL__BYTE)) + (d_4_scopeId_)) + (CacheConstants.default__.NULL__BYTE)) + ((self).partitionIdBytes)) + (CacheConstants.default__.NULL__BYTE)) + (d_7_suffix_)
        d_9_identifierDigestInput_: AwsCryptographyPrimitivesTypes.DigestInput
        d_9_identifierDigestInput_ = AwsCryptographyPrimitivesTypes.DigestInput_DigestInput(d_2_hashAlgorithm_, d_8_identifier_)
        d_10_maybeCacheDigest_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = Digest.default__.Digest(d_9_identifierDigestInput_)
        d_10_maybeCacheDigest_ = out0_
        d_11_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda0_(d_12_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_12_e_)

        d_11_valueOrError2_ = (d_10_maybeCacheDigest_).MapFailure(lambda0_)
        if (d_11_valueOrError2_).IsFailure():
            cacheId = (d_11_valueOrError2_).PropagateFailure()
            return cacheId
        d_13_cacheDigest_: _dafny.Seq
        d_13_cacheDigest_ = (d_11_valueOrError2_).Extract()
        d_14_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_14_valueOrError3_ = Wrappers.default__.Need((len(d_13_cacheDigest_)) == (Digest.default__.Length(d_2_hashAlgorithm_)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Digest generated a message not equal to the expected length.")))
        if (d_14_valueOrError3_).IsFailure():
            cacheId = (d_14_valueOrError3_).PropagateFailure()
            return cacheId
        cacheId = Wrappers.Result_Success(d_13_cacheDigest_)
        return cacheId
        return cacheId

    def GetHierarchicalMaterialsVersion(self, branchKeyId, branchKeyIdUtf8, version, cacheId):
        material: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.BranchKeyMaterials.default())()
        d_0_getCacheInput_: AwsCryptographyMaterialProvidersTypes.GetCacheEntryInput
        d_0_getCacheInput_ = AwsCryptographyMaterialProvidersTypes.GetCacheEntryInput_GetCacheEntryInput(cacheId, Wrappers.Option_None())
        d_1_getCacheOutput_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = ((self).cache).GetCacheEntry(d_0_getCacheInput_)
        d_1_getCacheOutput_ = out0_
        if ((d_1_getCacheOutput_).is_Failure) and (not(((d_1_getCacheOutput_).error).is_EntryDoesNotExist)):
            material = Wrappers.Result_Failure((d_1_getCacheOutput_).error)
            return material
        d_2_now_: int
        out1_: int
        out1_ = Time.default__.CurrentRelativeTime()
        d_2_now_ = out1_
        if ((d_1_getCacheOutput_).is_Failure) or (not(default__.cacheEntryWithinLimits(((d_1_getCacheOutput_).value).creationTime, d_2_now_, (self).ttlSeconds))):
            d_3_maybeGetBranchKeyVersionOutput_: Wrappers.Result
            out2_: Wrappers.Result
            out2_ = ((self).keyStore).GetBranchKeyVersion(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionInput_GetBranchKeyVersionInput(branchKeyId, version))
            d_3_maybeGetBranchKeyVersionOutput_ = out2_
            d_4_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput.default())()
            def lambda0_(d_5_e_):
                return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyKeyStore(d_5_e_)

            d_4_valueOrError0_ = (d_3_maybeGetBranchKeyVersionOutput_).MapFailure(lambda0_)
            if (d_4_valueOrError0_).IsFailure():
                material = (d_4_valueOrError0_).PropagateFailure()
                return material
            d_6_getBranchKeyVersionOutput_: AwsCryptographyKeyStoreTypes.GetBranchKeyVersionOutput
            d_6_getBranchKeyVersionOutput_ = (d_4_valueOrError0_).Extract()
            d_7_branchKeyMaterials_: AwsCryptographyKeyStoreTypes.BranchKeyMaterials
            d_7_branchKeyMaterials_ = (d_6_getBranchKeyVersionOutput_).branchKeyMaterials
            d_8_now_: int
            out3_: int
            out3_ = Time.default__.CurrentRelativeTime()
            d_8_now_ = out3_
            d_9_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_9_valueOrError1_ = Wrappers.default__.Need(((d_8_now_) + ((self).ttlSeconds)) < (StandardLibrary_UInt.default__.INT64__MAX__LIMIT), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("INT64 Overflow when putting cache entry.")))
            if (d_9_valueOrError1_).IsFailure():
                material = (d_9_valueOrError1_).PropagateFailure()
                return material
            d_10_putCacheEntryInput_: AwsCryptographyMaterialProvidersTypes.PutCacheEntryInput
            d_10_putCacheEntryInput_ = AwsCryptographyMaterialProvidersTypes.PutCacheEntryInput_PutCacheEntryInput(cacheId, AwsCryptographyMaterialProvidersTypes.Materials_BranchKey(d_7_branchKeyMaterials_), d_8_now_, ((self).ttlSeconds) + (d_8_now_), Wrappers.Option_None(), Wrappers.Option_None())
            d_11_putResult_: Wrappers.Result
            out4_: Wrappers.Result
            out4_ = ((self).cache).PutCacheEntry(d_10_putCacheEntryInput_)
            d_11_putResult_ = out4_
            if ((d_11_putResult_).is_Failure) and (not(((d_11_putResult_).error).is_EntryAlreadyExists)):
                material = Wrappers.Result_Failure((d_11_putResult_).error)
                return material
            material = Wrappers.Result_Success(d_7_branchKeyMaterials_)
            return material
        elif True:
            d_12_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_12_valueOrError2_ = Wrappers.default__.Need(((((d_1_getCacheOutput_).value).materials).is_BranchKey) and ((((d_1_getCacheOutput_).value).materials) == (AwsCryptographyMaterialProvidersTypes.Materials_BranchKey((((d_1_getCacheOutput_).value).materials).BranchKey))), default__.E(_dafny.Seq("Invalid Material Type.")))
            if (d_12_valueOrError2_).IsFailure():
                material = (d_12_valueOrError2_).PropagateFailure()
                return material
            material = Wrappers.Result_Success((((d_1_getCacheOutput_).value).materials).BranchKey)
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
    @property
    def partitionIdBytes(self):
        return self._partitionIdBytes
    @property
    def logicalKeyStoreNameBytes(self):
        return self._logicalKeyStoreNameBytes

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
        d_0_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_0_suite_ = (input).algorithmSuite
        d_1_wrappedMaterial_: _dafny.Seq
        d_1_wrappedMaterial_ = (input).wrappedMaterial
        d_2_aad_: _dafny.Map
        d_2_aad_ = (input).encryptionContext
        d_3_KeyLength_: int
        d_3_KeyLength_ = AlgorithmSuites.default__.GetEncryptKeyLength(d_0_suite_)
        d_4_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_4_valueOrError0_ = Wrappers.default__.Need((len(d_1_wrappedMaterial_)) == ((default__.EXPECTED__EDK__CIPHERTEXT__OVERHEAD) + (d_3_KeyLength_)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received EDK Ciphertext of incorrect length2.")))
        if (d_4_valueOrError0_).IsFailure():
            res = (d_4_valueOrError0_).PropagateFailure()
            return res
        d_5_salt_: _dafny.Seq
        d_5_salt_ = _dafny.Seq((d_1_wrappedMaterial_)[0:default__.H__WRAP__SALT__LEN:])
        d_6_iv_: _dafny.Seq
        d_6_iv_ = _dafny.Seq((d_1_wrappedMaterial_)[default__.H__WRAP__SALT__LEN:default__.EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX:])
        d_7_branchKeyVersionUuid_: _dafny.Seq
        d_7_branchKeyVersionUuid_ = _dafny.Seq((d_1_wrappedMaterial_)[default__.EDK__CIPHERTEXT__BRANCH__KEY__VERSION__INDEX:default__.EDK__CIPHERTEXT__VERSION__INDEX:])
        d_8_wrappedKey_: _dafny.Seq
        d_8_wrappedKey_ = _dafny.Seq((d_1_wrappedMaterial_)[default__.EDK__CIPHERTEXT__VERSION__INDEX:(default__.EDK__CIPHERTEXT__VERSION__INDEX) + (d_3_KeyLength_):])
        d_9_authTag_: _dafny.Seq
        d_9_authTag_ = _dafny.Seq((d_1_wrappedMaterial_)[(default__.EDK__CIPHERTEXT__VERSION__INDEX) + (d_3_KeyLength_)::])
        d_10_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_10_valueOrError1_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_10_valueOrError1_).IsFailure():
            res = (d_10_valueOrError1_).PropagateFailure()
            return res
        d_11_serializedEC_: _dafny.Seq
        d_11_serializedEC_ = (d_10_valueOrError1_).Extract()
        d_12_wrappingAad_: _dafny.Seq
        d_12_wrappingAad_ = default__.WrappingAad((self).branchKeyIdUtf8, (self).branchKeyVersionAsBytes, d_11_serializedEC_)
        d_13_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out0_: Wrappers.Result
        out0_ = default__.DeriveEncryptionKeyFromBranchKey((self).branchKey, d_5_salt_, Wrappers.Option_Some(Constants.default__.PROVIDER__ID__HIERARCHY), (self).crypto)
        d_13_valueOrError2_ = out0_
        if (d_13_valueOrError2_).IsFailure():
            res = (d_13_valueOrError2_).PropagateFailure()
            return res
        d_14_derivedBranchKey_: _dafny.Seq
        d_14_derivedBranchKey_ = (d_13_valueOrError2_).Extract()
        d_15_maybeUnwrappedPdk_: Wrappers.Result
        out1_: Wrappers.Result
        out1_ = ((self).crypto).AESDecrypt(AwsCryptographyPrimitivesTypes.AESDecryptInput_AESDecryptInput(default__.AES__256__ENC__ALG, d_14_derivedBranchKey_, d_8_wrappedKey_, d_9_authTag_, d_6_iv_, d_12_wrappingAad_))
        d_15_maybeUnwrappedPdk_ = out1_
        d_16_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda0_(d_17_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_17_e_)

        d_16_valueOrError3_ = (d_15_maybeUnwrappedPdk_).MapFailure(lambda0_)
        if (d_16_valueOrError3_).IsFailure():
            res = (d_16_valueOrError3_).PropagateFailure()
            return res
        d_18_unwrappedPdk_: _dafny.Seq
        d_18_unwrappedPdk_ = (d_16_valueOrError3_).Extract()
        d_19_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_19_valueOrError4_ = Wrappers.default__.Need((len(d_18_unwrappedPdk_)) == (AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)), default__.E(_dafny.Seq("Invalid Key Length")))
        if (d_19_valueOrError4_).IsFailure():
            res = (d_19_valueOrError4_).PropagateFailure()
            return res
        d_20_output_: MaterialWrapping.UnwrapOutput
        d_20_output_ = MaterialWrapping.UnwrapOutput_UnwrapOutput(d_18_unwrappedPdk_, HierarchyUnwrapInfo_HierarchyUnwrapInfo())
        res = Wrappers.Result_Success(d_20_output_)
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
        d_0_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_0_suite_ = (input).algorithmSuite
        d_1_pdkResult_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = ((self).crypto).GenerateRandomBytes(AwsCryptographyPrimitivesTypes.GenerateRandomBytesInput_GenerateRandomBytesInput(AlgorithmSuites.default__.GetEncryptKeyLength(d_0_suite_)))
        d_1_pdkResult_ = out0_
        d_2_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda0_(d_3_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_3_e_)

        d_2_valueOrError0_ = (d_1_pdkResult_).MapFailure(lambda0_)
        if (d_2_valueOrError0_).IsFailure():
            res = (d_2_valueOrError0_).PropagateFailure()
            return res
        d_4_pdk_: _dafny.Seq
        d_4_pdk_ = (d_2_valueOrError0_).Extract()
        d_5_wrap_: KmsHierarchyWrapKeyMaterial
        nw0_ = KmsHierarchyWrapKeyMaterial()
        nw0_.ctor__((self).branchKey, (self).branchKeyIdUtf8, (self).branchKeyVersionAsBytes, (self).crypto)
        d_5_wrap_ = nw0_
        d_6_valueOrError1_: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.WrapOutput.default(HierarchyWrapInfo.default()))()
        out1_: Wrappers.Result
        out1_ = (d_5_wrap_).Invoke(MaterialWrapping.WrapInput_WrapInput(d_4_pdk_, (input).algorithmSuite, (input).encryptionContext))
        d_6_valueOrError1_ = out1_
        if (d_6_valueOrError1_).IsFailure():
            res = (d_6_valueOrError1_).PropagateFailure()
            return res
        d_7_wrapOutput_: MaterialWrapping.WrapOutput
        d_7_wrapOutput_ = (d_6_valueOrError1_).Extract()
        d_8_output_: MaterialWrapping.GenerateAndWrapOutput
        d_8_output_ = MaterialWrapping.GenerateAndWrapOutput_GenerateAndWrapOutput(d_4_pdk_, (d_7_wrapOutput_).wrappedMaterial, HierarchyWrapInfo_HierarchyWrapInfo())
        res = Wrappers.Result_Success(d_8_output_)
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
        d_0_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_0_suite_ = (input).algorithmSuite
        d_1_maybeNonceSalt_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = ((self).crypto).GenerateRandomBytes(AwsCryptographyPrimitivesTypes.GenerateRandomBytesInput_GenerateRandomBytesInput((default__.H__WRAP__SALT__LEN) + (default__.H__WRAP__NONCE__LEN)))
        d_1_maybeNonceSalt_ = out0_
        d_2_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda0_(d_3_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_3_e_)

        d_2_valueOrError0_ = (d_1_maybeNonceSalt_).MapFailure(lambda0_)
        if (d_2_valueOrError0_).IsFailure():
            res = (d_2_valueOrError0_).PropagateFailure()
            return res
        d_4_saltAndNonce_: _dafny.Seq
        d_4_saltAndNonce_ = (d_2_valueOrError0_).Extract()
        d_5_salt_: _dafny.Seq
        d_5_salt_ = _dafny.Seq((d_4_saltAndNonce_)[0:default__.H__WRAP__SALT__LEN:])
        d_6_nonce_: _dafny.Seq
        d_6_nonce_ = _dafny.Seq((d_4_saltAndNonce_)[default__.H__WRAP__SALT__LEN::])
        d_7_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_7_valueOrError1_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_7_valueOrError1_).IsFailure():
            res = (d_7_valueOrError1_).PropagateFailure()
            return res
        d_8_serializedEC_: _dafny.Seq
        d_8_serializedEC_ = (d_7_valueOrError1_).Extract()
        d_9_wrappingAad_: _dafny.Seq
        d_9_wrappingAad_ = default__.WrappingAad((self).branchKeyIdUtf8, (self).branchKeyVersionAsBytes, d_8_serializedEC_)
        d_10_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out1_: Wrappers.Result
        out1_ = default__.DeriveEncryptionKeyFromBranchKey((self).branchKey, d_5_salt_, Wrappers.Option_Some(Constants.default__.PROVIDER__ID__HIERARCHY), (self).crypto)
        d_10_valueOrError2_ = out1_
        if (d_10_valueOrError2_).IsFailure():
            res = (d_10_valueOrError2_).PropagateFailure()
            return res
        d_11_derivedBranchKey_: _dafny.Seq
        d_11_derivedBranchKey_ = (d_10_valueOrError2_).Extract()
        d_12_maybeWrappedPdk_: Wrappers.Result
        out2_: Wrappers.Result
        out2_ = ((self).crypto).AESEncrypt(AwsCryptographyPrimitivesTypes.AESEncryptInput_AESEncryptInput(default__.AES__256__ENC__ALG, d_6_nonce_, d_11_derivedBranchKey_, (input).plaintextMaterial, d_9_wrappingAad_))
        d_12_maybeWrappedPdk_ = out2_
        d_13_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.AESEncryptOutput.default())()
        def lambda1_(d_14_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_14_e_)

        d_13_valueOrError3_ = (d_12_maybeWrappedPdk_).MapFailure(lambda1_)
        if (d_13_valueOrError3_).IsFailure():
            res = (d_13_valueOrError3_).PropagateFailure()
            return res
        d_15_wrappedPdk_: AwsCryptographyPrimitivesTypes.AESEncryptOutput
        d_15_wrappedPdk_ = (d_13_valueOrError3_).Extract()
        d_16_output_: MaterialWrapping.WrapOutput
        d_16_output_ = MaterialWrapping.WrapOutput_WrapOutput(((((d_5_salt_) + (d_6_nonce_)) + ((self).branchKeyVersionAsBytes)) + ((d_15_wrappedPdk_).cipherText)) + ((d_15_wrappedPdk_).authTag), HierarchyWrapInfo_HierarchyWrapInfo())
        res = Wrappers.Result_Success(d_16_output_)
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
