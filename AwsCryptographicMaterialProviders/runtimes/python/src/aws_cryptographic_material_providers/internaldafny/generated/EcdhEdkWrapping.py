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
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsHierarchicalKeyring as AwsKmsHierarchicalKeyring
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsRsaKeyring as AwsKmsRsaKeyring

# Module: EcdhEdkWrapping

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DeriveSharedKeyingMaterial(sharedSecret, fixedInfo, salt, crypto):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_0_maybeDerivedKeyingMaterial_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = (crypto).KdfCounterMode(AwsCryptographyPrimitivesTypes.KdfCtrInput_KdfCtrInput(AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__384(), sharedSecret, Constants.default__.KDF__EXPECTED__LEN, Wrappers.Option_Some(fixedInfo), Wrappers.Option_Some(salt)))
        d_0_maybeDerivedKeyingMaterial_ = out0_
        d_1_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda0_(d_2_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_2_e_)

        d_1_valueOrError0_ = (d_0_maybeDerivedKeyingMaterial_).MapFailure(lambda0_)
        if (d_1_valueOrError0_).IsFailure():
            res = (d_1_valueOrError0_).PropagateFailure()
            return res
        d_3_derivedKeyingMaterial_: _dafny.Seq
        d_3_derivedKeyingMaterial_ = (d_1_valueOrError0_).Extract()
        res = Wrappers.Result_Success(d_3_derivedKeyingMaterial_)
        return res

    @staticmethod
    def SerializeFixedInfo(ecdhKeyDerivationUtf8, curveSpecUtf8, senderPublicKey, recipientPublicKey, canonicalizedEC, keyringVersion):
        return (((((((((((ecdhKeyDerivationUtf8) + (Constants.default__.ECDH__KDF__DELIMETER)) + (curveSpecUtf8)) + (Constants.default__.ECDH__KDF__DELIMETER)) + (Constants.default__.ECDH__KDF__PRF__NAME)) + (Constants.default__.ECDH__KDF__DELIMETER)) + (senderPublicKey)) + (recipientPublicKey)) + (Constants.default__.ECDH__KDF__DELIMETER)) + (keyringVersion)) + (Constants.default__.ECDH__KDF__DELIMETER)) + (canonicalizedEC)

    @staticmethod
    def CurveSpecTypeToString(c):
        source0_ = c
        if True:
            if source0_.is_ECC__NIST__P256:
                return _dafny.Seq("p256")
        if True:
            if source0_.is_ECC__NIST__P384:
                return _dafny.Seq("p384")
        if True:
            if source0_.is_ECC__NIST__P521:
                return _dafny.Seq("p521")
        if True:
            return _dafny.Seq("sm2")

    @staticmethod
    def E(s):
        return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(s)


class EcdhUnwrapInfo:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [EcdhUnwrapInfo_EcdhUnwrapInfo()]
    @classmethod
    def default(cls, ):
        return lambda: EcdhUnwrapInfo_EcdhUnwrapInfo()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_EcdhUnwrapInfo(self) -> bool:
        return isinstance(self, EcdhUnwrapInfo_EcdhUnwrapInfo)

class EcdhUnwrapInfo_EcdhUnwrapInfo(EcdhUnwrapInfo, NamedTuple('EcdhUnwrapInfo', [])):
    def __dafnystr__(self) -> str:
        return f'EcdhEdkWrapping.EcdhUnwrapInfo.EcdhUnwrapInfo'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, EcdhUnwrapInfo_EcdhUnwrapInfo)
    def __hash__(self) -> int:
        return super().__hash__()


class EcdhWrapInfo:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [EcdhWrapInfo_EcdhWrapInfo()]
    @classmethod
    def default(cls, ):
        return lambda: EcdhWrapInfo_EcdhWrapInfo()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_EcdhWrapInfo(self) -> bool:
        return isinstance(self, EcdhWrapInfo_EcdhWrapInfo)

class EcdhWrapInfo_EcdhWrapInfo(EcdhWrapInfo, NamedTuple('EcdhWrapInfo', [])):
    def __dafnystr__(self) -> str:
        return f'EcdhEdkWrapping.EcdhWrapInfo.EcdhWrapInfo'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, EcdhWrapInfo_EcdhWrapInfo)
    def __hash__(self) -> int:
        return super().__hash__()


class EcdhUnwrap(MaterialWrapping.UnwrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._senderPublicKey: _dafny.Seq = _dafny.Seq({})
        self._recipientPublicKey: _dafny.Seq = _dafny.Seq({})
        self._sharedSecret: _dafny.Seq = _dafny.Seq({})
        self._keyringVersion: _dafny.Seq = _dafny.Seq({})
        self._curveSpec: AwsCryptographyPrimitivesTypes.ECDHCurveSpec = AwsCryptographyPrimitivesTypes.ECDHCurveSpec.default()()
        self._crypto: AtomicPrimitives.AtomicPrimitivesClient = None
        pass

    def __dafnystr__(self) -> str:
        return "EcdhEdkWrapping.EcdhUnwrap"
    def ctor__(self, senderPublicKey, recipientPublicKey, sharedSecret, keyringVersion, curveSpec, crypto):
        (self)._senderPublicKey = senderPublicKey
        (self)._recipientPublicKey = recipientPublicKey
        (self)._sharedSecret = sharedSecret
        (self)._keyringVersion = keyringVersion
        (self)._curveSpec = curveSpec
        (self)._crypto = crypto

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.UnwrapOutput.default(EcdhUnwrapInfo.default()))()
        d_0_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_0_suite_ = (input).algorithmSuite
        d_1_wrappedMaterial_: _dafny.Seq
        d_1_wrappedMaterial_ = (input).wrappedMaterial
        d_2_aad_: _dafny.Map
        d_2_aad_ = (input).encryptionContext
        d_3_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_3_valueOrError0_ = Wrappers.default__.Need((len(d_1_wrappedMaterial_)) > (Constants.default__.CIPHERTEXT__WRAPPED__MATERIAL__INDEX), default__.E(_dafny.Seq("Recieved ciphertext is shorter than expected.")))
        if (d_3_valueOrError0_).IsFailure():
            res = (d_3_valueOrError0_).PropagateFailure()
            return res
        d_4_KeyLength_: int
        d_4_KeyLength_ = AlgorithmSuites.default__.GetEncryptKeyLength(d_0_suite_)
        d_5_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_5_valueOrError1_ = Wrappers.default__.Need((len(d_1_wrappedMaterial_)) > ((Constants.default__.ECDH__WRAPPED__KEY__MATERIAL__INDEX) + (d_4_KeyLength_)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received EDK Ciphertext of incorrect length.")))
        if (d_5_valueOrError1_).IsFailure():
            res = (d_5_valueOrError1_).PropagateFailure()
            return res
        d_6_kdfNonce_: _dafny.Seq
        d_6_kdfNonce_ = _dafny.Seq((d_1_wrappedMaterial_)[0:Constants.default__.ECDH__COMMITMENT__KEY__INDEX:])
        d_7_iv_: _dafny.Seq
        d_7_iv_ = _dafny.Seq([0 for d_8___v0_ in range((Constants.default__.ECDH__AES__256__ENC__ALG).ivLength)])
        d_9_commitmentKey_: _dafny.Seq
        d_9_commitmentKey_ = _dafny.Seq((d_1_wrappedMaterial_)[Constants.default__.ECDH__COMMITMENT__KEY__INDEX:Constants.default__.ECDH__WRAPPED__KEY__MATERIAL__INDEX:])
        d_10_wrappedKey_: _dafny.Seq
        d_10_wrappedKey_ = _dafny.Seq((d_1_wrappedMaterial_)[Constants.default__.ECDH__WRAPPED__KEY__MATERIAL__INDEX:(Constants.default__.ECDH__WRAPPED__KEY__MATERIAL__INDEX) + (d_4_KeyLength_):])
        d_11_authTag_: _dafny.Seq
        d_11_authTag_ = _dafny.Seq((d_1_wrappedMaterial_)[(Constants.default__.ECDH__WRAPPED__KEY__MATERIAL__INDEX) + (d_4_KeyLength_)::])
        d_12_valueOrError2_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_12_valueOrError2_ = (UTF8.default__.Encode(default__.CurveSpecTypeToString((self).curveSpec))).MapFailure(default__.E)
        if (d_12_valueOrError2_).IsFailure():
            res = (d_12_valueOrError2_).PropagateFailure()
            return res
        d_13_curveSpecUtf8_: _dafny.Seq
        d_13_curveSpecUtf8_ = (d_12_valueOrError2_).Extract()
        d_14_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_14_valueOrError3_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_14_valueOrError3_).IsFailure():
            res = (d_14_valueOrError3_).PropagateFailure()
            return res
        d_15_canonicalizedEC_: _dafny.Seq
        d_15_canonicalizedEC_ = (d_14_valueOrError3_).Extract()
        d_16_fixedInfo_: _dafny.Seq
        d_16_fixedInfo_ = default__.SerializeFixedInfo(Constants.default__.ECDH__KDF__UTF8, d_13_curveSpecUtf8_, (self).senderPublicKey, (self).recipientPublicKey, d_15_canonicalizedEC_, (self).keyringVersion)
        d_17_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out0_: Wrappers.Result
        out0_ = default__.DeriveSharedKeyingMaterial((self).sharedSecret, d_16_fixedInfo_, d_6_kdfNonce_, (self).crypto)
        d_17_valueOrError4_ = out0_
        if (d_17_valueOrError4_).IsFailure():
            res = (d_17_valueOrError4_).PropagateFailure()
            return res
        d_18_derivedKeyingMaterial_: _dafny.Seq
        d_18_derivedKeyingMaterial_ = (d_17_valueOrError4_).Extract()
        d_19_calculatedCommitmentKey_: _dafny.Seq
        d_19_calculatedCommitmentKey_ = _dafny.Seq((d_18_derivedKeyingMaterial_)[0:32:])
        d_20_sharedKeyingMaterial_: _dafny.Seq
        d_20_sharedKeyingMaterial_ = _dafny.Seq((d_18_derivedKeyingMaterial_)[32::])
        d_21_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_21_valueOrError5_ = Wrappers.default__.Need((len(d_19_calculatedCommitmentKey_)) == (len(d_9_commitmentKey_)), default__.E(_dafny.Seq("Calculated commitment key length does NOT match expected commitment key length")))
        if (d_21_valueOrError5_).IsFailure():
            res = (d_21_valueOrError5_).PropagateFailure()
            return res
        d_22_check_q_: bool
        out1_: bool
        out1_ = (self).commitmentKeyCheck(d_19_calculatedCommitmentKey_, d_9_commitmentKey_)
        d_22_check_q_ = out1_
        d_23_valueOrError6_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_23_valueOrError6_ = Wrappers.default__.Need(d_22_check_q_, default__.E(_dafny.Seq("Commitment keys do not match")))
        if (d_23_valueOrError6_).IsFailure():
            res = (d_23_valueOrError6_).PropagateFailure()
            return res
        d_24_maybeUnwrappedPdk_: Wrappers.Result
        out2_: Wrappers.Result
        out2_ = ((self).crypto).AESDecrypt(AwsCryptographyPrimitivesTypes.AESDecryptInput_AESDecryptInput(Constants.default__.ECDH__AES__256__ENC__ALG, d_20_sharedKeyingMaterial_, d_10_wrappedKey_, d_11_authTag_, d_7_iv_, d_16_fixedInfo_))
        d_24_maybeUnwrappedPdk_ = out2_
        d_25_valueOrError7_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda0_(d_26_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_26_e_)

        d_25_valueOrError7_ = (d_24_maybeUnwrappedPdk_).MapFailure(lambda0_)
        if (d_25_valueOrError7_).IsFailure():
            res = (d_25_valueOrError7_).PropagateFailure()
            return res
        d_27_unwrappedPdk_: _dafny.Seq
        d_27_unwrappedPdk_ = (d_25_valueOrError7_).Extract()
        d_28_valueOrError8_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_28_valueOrError8_ = Wrappers.default__.Need((len(d_27_unwrappedPdk_)) == (AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)), default__.E(_dafny.Seq("Invalid Key Length")))
        if (d_28_valueOrError8_).IsFailure():
            res = (d_28_valueOrError8_).PropagateFailure()
            return res
        d_29_output_: MaterialWrapping.UnwrapOutput
        d_29_output_ = MaterialWrapping.UnwrapOutput_UnwrapOutput(d_27_unwrappedPdk_, EcdhUnwrapInfo_EcdhUnwrapInfo())
        res = Wrappers.Result_Success(d_29_output_)
        return res
        return res

    def commitmentKeyCheck(self, calculatedCommitmentKey, serializedCommitmentKey):
        res: bool = False
        d_0_diff_q_: int
        d_0_diff_q_ = 0
        hi0_ = len(serializedCommitmentKey)
        for d_1_i_ in range(0, hi0_):
            d_0_diff_q_ = (d_0_diff_q_) | (((calculatedCommitmentKey)[d_1_i_]) ^ ((serializedCommitmentKey)[d_1_i_]))
        res = (d_0_diff_q_) == (0)
        return res

    @property
    def senderPublicKey(self):
        return self._senderPublicKey
    @property
    def recipientPublicKey(self):
        return self._recipientPublicKey
    @property
    def sharedSecret(self):
        return self._sharedSecret
    @property
    def keyringVersion(self):
        return self._keyringVersion
    @property
    def curveSpec(self):
        return self._curveSpec
    @property
    def crypto(self):
        return self._crypto

class EcdhGenerateAndWrapKeyMaterial(MaterialWrapping.GenerateAndWrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._crypto: AtomicPrimitives.AtomicPrimitivesClient = None
        self._sharedSecret: _dafny.Seq = _dafny.Seq({})
        self._fixedInfo: _dafny.Seq = _dafny.Seq({})
        pass

    def __dafnystr__(self) -> str:
        return "EcdhEdkWrapping.EcdhGenerateAndWrapKeyMaterial"
    def ctor__(self, sharedSecret, fixedInfo, crypto):
        (self)._sharedSecret = sharedSecret
        (self)._fixedInfo = fixedInfo
        (self)._crypto = crypto

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.GenerateAndWrapOutput.default(EcdhWrapInfo.default()))()
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
        d_5_wrap_: EcdhWrapKeyMaterial
        nw0_ = EcdhWrapKeyMaterial()
        nw0_.ctor__((self).sharedSecret, (self).fixedInfo, (self).crypto)
        d_5_wrap_ = nw0_
        d_6_valueOrError1_: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.WrapOutput.default(EcdhWrapInfo.default()))()
        out1_: Wrappers.Result
        out1_ = (d_5_wrap_).Invoke(MaterialWrapping.WrapInput_WrapInput(d_4_pdk_, (input).algorithmSuite, (input).encryptionContext))
        d_6_valueOrError1_ = out1_
        if (d_6_valueOrError1_).IsFailure():
            res = (d_6_valueOrError1_).PropagateFailure()
            return res
        d_7_wrapOutput_: MaterialWrapping.WrapOutput
        d_7_wrapOutput_ = (d_6_valueOrError1_).Extract()
        d_8_output_: MaterialWrapping.GenerateAndWrapOutput
        d_8_output_ = MaterialWrapping.GenerateAndWrapOutput_GenerateAndWrapOutput(d_4_pdk_, (d_7_wrapOutput_).wrappedMaterial, (d_7_wrapOutput_).wrapInfo)
        res = Wrappers.Result_Success(d_8_output_)
        return res
        return res

    @property
    def crypto(self):
        return self._crypto
    @property
    def sharedSecret(self):
        return self._sharedSecret
    @property
    def fixedInfo(self):
        return self._fixedInfo

class EcdhWrapKeyMaterial(MaterialWrapping.WrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._crypto: AtomicPrimitives.AtomicPrimitivesClient = None
        self._fixedInfo: _dafny.Seq = _dafny.Seq({})
        self._sharedSecret: _dafny.Seq = _dafny.Seq({})
        pass

    def __dafnystr__(self) -> str:
        return "EcdhEdkWrapping.EcdhWrapKeyMaterial"
    def ctor__(self, sharedSecret, fixedInfo, crypto):
        (self)._sharedSecret = sharedSecret
        (self)._fixedInfo = fixedInfo
        (self)._crypto = crypto

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.WrapOutput.default(EcdhWrapInfo.default()))()
        d_0_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_0_suite_ = (input).algorithmSuite
        d_1_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1_valueOrError0_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_1_valueOrError0_).IsFailure():
            res = (d_1_valueOrError0_).PropagateFailure()
            return res
        d_2_canonicalizedEC_: _dafny.Seq
        d_2_canonicalizedEC_ = (d_1_valueOrError0_).Extract()
        d_3_maybeSalt_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = ((self).crypto).GenerateRandomBytes(AwsCryptographyPrimitivesTypes.GenerateRandomBytesInput_GenerateRandomBytesInput(Constants.default__.KDF__SALT__LEN))
        d_3_maybeSalt_ = out0_
        d_4_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda0_(d_5_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_5_e_)

        d_4_valueOrError1_ = (d_3_maybeSalt_).MapFailure(lambda0_)
        if (d_4_valueOrError1_).IsFailure():
            res = (d_4_valueOrError1_).PropagateFailure()
            return res
        d_6_salt_: _dafny.Seq
        d_6_salt_ = (d_4_valueOrError1_).Extract()
        d_7_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out1_: Wrappers.Result
        out1_ = default__.DeriveSharedKeyingMaterial((self).sharedSecret, (self).fixedInfo, d_6_salt_, (self).crypto)
        d_7_valueOrError2_ = out1_
        if (d_7_valueOrError2_).IsFailure():
            res = (d_7_valueOrError2_).PropagateFailure()
            return res
        d_8_derivedKeyingMaterial_: _dafny.Seq
        d_8_derivedKeyingMaterial_ = (d_7_valueOrError2_).Extract()
        d_9_commitmentKey_: _dafny.Seq
        d_9_commitmentKey_ = _dafny.Seq((d_8_derivedKeyingMaterial_)[0:32:])
        d_10_sharedKeyingMaterial_: _dafny.Seq
        d_10_sharedKeyingMaterial_ = _dafny.Seq((d_8_derivedKeyingMaterial_)[32::])
        d_11_iv_: _dafny.Seq
        d_11_iv_ = _dafny.Seq([0 for d_12___v3_ in range((Constants.default__.ECDH__AES__256__ENC__ALG).ivLength)])
        d_13_maybeWrappedPdk_: Wrappers.Result
        out2_: Wrappers.Result
        out2_ = ((self).crypto).AESEncrypt(AwsCryptographyPrimitivesTypes.AESEncryptInput_AESEncryptInput(Constants.default__.ECDH__AES__256__ENC__ALG, d_11_iv_, d_10_sharedKeyingMaterial_, (input).plaintextMaterial, (self).fixedInfo))
        d_13_maybeWrappedPdk_ = out2_
        d_14_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.AESEncryptOutput.default())()
        def lambda1_(d_15_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_15_e_)

        d_14_valueOrError3_ = (d_13_maybeWrappedPdk_).MapFailure(lambda1_)
        if (d_14_valueOrError3_).IsFailure():
            res = (d_14_valueOrError3_).PropagateFailure()
            return res
        d_16_wrappedPdk_: AwsCryptographyPrimitivesTypes.AESEncryptOutput
        d_16_wrappedPdk_ = (d_14_valueOrError3_).Extract()
        d_17_output_: MaterialWrapping.WrapOutput
        d_17_output_ = MaterialWrapping.WrapOutput_WrapOutput((((d_6_salt_) + (d_9_commitmentKey_)) + ((d_16_wrappedPdk_).cipherText)) + ((d_16_wrappedPdk_).authTag), EcdhWrapInfo_EcdhWrapInfo())
        res = Wrappers.Result_Success(d_17_output_)
        return res
        return res

    @property
    def crypto(self):
        return self._crypto
    @property
    def fixedInfo(self):
        return self._fixedInfo
    @property
    def sharedSecret(self):
        return self._sharedSecret
