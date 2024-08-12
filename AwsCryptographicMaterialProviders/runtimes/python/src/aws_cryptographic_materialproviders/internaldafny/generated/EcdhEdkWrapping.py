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
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsHierarchicalKeyring as AwsKmsHierarchicalKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsRsaKeyring as AwsKmsRsaKeyring

# Module: EcdhEdkWrapping

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DeriveSharedKeyingMaterial(sharedSecret, fixedInfo, salt, crypto):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1091_maybeDerivedKeyingMaterial_: Wrappers.Result
        out196_: Wrappers.Result
        out196_ = (crypto).KdfCounterMode(AwsCryptographyPrimitivesTypes.KdfCtrInput_KdfCtrInput(AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__384(), sharedSecret, Constants.default__.KDF__EXPECTED__LEN, Wrappers.Option_Some(fixedInfo), Wrappers.Option_Some(salt)))
        d_1091_maybeDerivedKeyingMaterial_ = out196_
        d_1092_derivedKeyingMaterial_: _dafny.Seq
        d_1093_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda91_(d_1094_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1094_e_)

        d_1093_valueOrError0_ = (d_1091_maybeDerivedKeyingMaterial_).MapFailure(lambda91_)
        if (d_1093_valueOrError0_).IsFailure():
            res = (d_1093_valueOrError0_).PropagateFailure()
            return res
        d_1092_derivedKeyingMaterial_ = (d_1093_valueOrError0_).Extract()
        res = Wrappers.Result_Success(d_1092_derivedKeyingMaterial_)
        return res

    @staticmethod
    def SerializeFixedInfo(ecdhKeyDerivationUtf8, curveSpecUtf8, senderPublicKey, recipientPublicKey, canonicalizedEC, keyringVersion):
        return (((((((((((ecdhKeyDerivationUtf8) + (Constants.default__.ECDH__KDF__DELIMETER)) + (curveSpecUtf8)) + (Constants.default__.ECDH__KDF__DELIMETER)) + (Constants.default__.ECDH__KDF__PRF__NAME)) + (Constants.default__.ECDH__KDF__DELIMETER)) + (senderPublicKey)) + (recipientPublicKey)) + (Constants.default__.ECDH__KDF__DELIMETER)) + (keyringVersion)) + (Constants.default__.ECDH__KDF__DELIMETER)) + (canonicalizedEC)

    @staticmethod
    def CurveSpecTypeToString(c):
        source31_ = c
        unmatched31 = True
        if unmatched31:
            if source31_.is_ECC__NIST__P256:
                unmatched31 = False
                return _dafny.Seq("p256")
        if unmatched31:
            if source31_.is_ECC__NIST__P384:
                unmatched31 = False
                return _dafny.Seq("p384")
        if unmatched31:
            if source31_.is_ECC__NIST__P521:
                unmatched31 = False
                return _dafny.Seq("p521")
        if unmatched31:
            unmatched31 = False
            return _dafny.Seq("sm2")
        raise Exception("unexpected control point")

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
        self._crypto: Aws_Cryptography_Primitives.AtomicPrimitivesClient = None
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
        d_1095_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_1095_suite_ = (input).algorithmSuite
        d_1096_wrappedMaterial_: _dafny.Seq
        d_1096_wrappedMaterial_ = (input).wrappedMaterial
        d_1097_aad_: _dafny.Map
        d_1097_aad_ = (input).encryptionContext
        d_1098_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1098_valueOrError0_ = Wrappers.default__.Need((len(d_1096_wrappedMaterial_)) > (Constants.default__.CIPHERTEXT__WRAPPED__MATERIAL__INDEX), default__.E(_dafny.Seq("Recieved ciphertext is shorter than expected.")))
        if (d_1098_valueOrError0_).IsFailure():
            res = (d_1098_valueOrError0_).PropagateFailure()
            return res
        d_1099_KeyLength_: int
        d_1099_KeyLength_ = AlgorithmSuites.default__.GetEncryptKeyLength(d_1095_suite_)
        d_1100_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1100_valueOrError1_ = Wrappers.default__.Need((len(d_1096_wrappedMaterial_)) > ((Constants.default__.ECDH__WRAPPED__KEY__MATERIAL__INDEX) + (d_1099_KeyLength_)), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received EDK Ciphertext of incorrect length.")))
        if (d_1100_valueOrError1_).IsFailure():
            res = (d_1100_valueOrError1_).PropagateFailure()
            return res
        d_1101_kdfNonce_: _dafny.Seq
        d_1101_kdfNonce_ = _dafny.Seq((d_1096_wrappedMaterial_)[0:Constants.default__.ECDH__COMMITMENT__KEY__INDEX:])
        d_1102_iv_: _dafny.Seq
        d_1102_iv_ = _dafny.Seq([0 for d_1103___v0_ in range((Constants.default__.ECDH__AES__256__ENC__ALG).ivLength)])
        d_1104_commitmentKey_: _dafny.Seq
        d_1104_commitmentKey_ = _dafny.Seq((d_1096_wrappedMaterial_)[Constants.default__.ECDH__COMMITMENT__KEY__INDEX:Constants.default__.ECDH__WRAPPED__KEY__MATERIAL__INDEX:])
        d_1105_wrappedKey_: _dafny.Seq
        d_1105_wrappedKey_ = _dafny.Seq((d_1096_wrappedMaterial_)[Constants.default__.ECDH__WRAPPED__KEY__MATERIAL__INDEX:(Constants.default__.ECDH__WRAPPED__KEY__MATERIAL__INDEX) + (d_1099_KeyLength_):])
        d_1106_authTag_: _dafny.Seq
        d_1106_authTag_ = _dafny.Seq((d_1096_wrappedMaterial_)[(Constants.default__.ECDH__WRAPPED__KEY__MATERIAL__INDEX) + (d_1099_KeyLength_)::])
        d_1107_curveSpecUtf8_: _dafny.Seq
        d_1108_valueOrError2_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_1108_valueOrError2_ = (UTF8.default__.Encode(default__.CurveSpecTypeToString((self).curveSpec))).MapFailure(default__.E)
        if (d_1108_valueOrError2_).IsFailure():
            res = (d_1108_valueOrError2_).PropagateFailure()
            return res
        d_1107_curveSpecUtf8_ = (d_1108_valueOrError2_).Extract()
        d_1109_canonicalizedEC_: _dafny.Seq
        d_1110_valueOrError3_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1110_valueOrError3_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_1110_valueOrError3_).IsFailure():
            res = (d_1110_valueOrError3_).PropagateFailure()
            return res
        d_1109_canonicalizedEC_ = (d_1110_valueOrError3_).Extract()
        d_1111_fixedInfo_: _dafny.Seq
        d_1111_fixedInfo_ = default__.SerializeFixedInfo(Constants.default__.ECDH__KDF__UTF8, d_1107_curveSpecUtf8_, (self).senderPublicKey, (self).recipientPublicKey, d_1109_canonicalizedEC_, (self).keyringVersion)
        d_1112_derivedKeyingMaterial_: _dafny.Seq
        d_1113_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out197_: Wrappers.Result
        out197_ = default__.DeriveSharedKeyingMaterial((self).sharedSecret, d_1111_fixedInfo_, d_1101_kdfNonce_, (self).crypto)
        d_1113_valueOrError4_ = out197_
        if (d_1113_valueOrError4_).IsFailure():
            res = (d_1113_valueOrError4_).PropagateFailure()
            return res
        d_1112_derivedKeyingMaterial_ = (d_1113_valueOrError4_).Extract()
        d_1114_calculatedCommitmentKey_: _dafny.Seq
        d_1114_calculatedCommitmentKey_ = _dafny.Seq((d_1112_derivedKeyingMaterial_)[0:32:])
        d_1115_sharedKeyingMaterial_: _dafny.Seq
        d_1115_sharedKeyingMaterial_ = _dafny.Seq((d_1112_derivedKeyingMaterial_)[32::])
        d_1116_valueOrError5_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1116_valueOrError5_ = Wrappers.default__.Need((len(d_1114_calculatedCommitmentKey_)) == (len(d_1104_commitmentKey_)), default__.E(_dafny.Seq("Calculated commitment key length does NOT match expected commitment key length")))
        if (d_1116_valueOrError5_).IsFailure():
            res = (d_1116_valueOrError5_).PropagateFailure()
            return res
        d_1117_check_q_: bool
        out198_: bool
        out198_ = (self).commitmentKeyCheck(d_1114_calculatedCommitmentKey_, d_1104_commitmentKey_)
        d_1117_check_q_ = out198_
        d_1118_valueOrError6_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1118_valueOrError6_ = Wrappers.default__.Need(d_1117_check_q_, default__.E(_dafny.Seq("Commitment keys do not match")))
        if (d_1118_valueOrError6_).IsFailure():
            res = (d_1118_valueOrError6_).PropagateFailure()
            return res
        d_1119_maybeUnwrappedPdk_: Wrappers.Result
        out199_: Wrappers.Result
        out199_ = ((self).crypto).AESDecrypt(AwsCryptographyPrimitivesTypes.AESDecryptInput_AESDecryptInput(Constants.default__.ECDH__AES__256__ENC__ALG, d_1115_sharedKeyingMaterial_, d_1105_wrappedKey_, d_1106_authTag_, d_1102_iv_, d_1111_fixedInfo_))
        d_1119_maybeUnwrappedPdk_ = out199_
        d_1120_unwrappedPdk_: _dafny.Seq
        d_1121_valueOrError7_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda92_(d_1122_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1122_e_)

        d_1121_valueOrError7_ = (d_1119_maybeUnwrappedPdk_).MapFailure(lambda92_)
        if (d_1121_valueOrError7_).IsFailure():
            res = (d_1121_valueOrError7_).PropagateFailure()
            return res
        d_1120_unwrappedPdk_ = (d_1121_valueOrError7_).Extract()
        d_1123_valueOrError8_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1123_valueOrError8_ = Wrappers.default__.Need((len(d_1120_unwrappedPdk_)) == (AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)), default__.E(_dafny.Seq("Invalid Key Length")))
        if (d_1123_valueOrError8_).IsFailure():
            res = (d_1123_valueOrError8_).PropagateFailure()
            return res
        d_1124_output_: MaterialWrapping.UnwrapOutput
        d_1124_output_ = MaterialWrapping.UnwrapOutput_UnwrapOutput(d_1120_unwrappedPdk_, EcdhUnwrapInfo_EcdhUnwrapInfo())
        res = Wrappers.Result_Success(d_1124_output_)
        return res
        return res

    def commitmentKeyCheck(self, calculatedCommitmentKey, serializedCommitmentKey):
        res: bool = False
        d_1125_diff_q_: int
        d_1125_diff_q_ = 0
        hi8_ = len(serializedCommitmentKey)
        for d_1126_i_ in range(0, hi8_):
            d_1125_diff_q_ = (d_1125_diff_q_) | (((calculatedCommitmentKey)[d_1126_i_]) ^ ((serializedCommitmentKey)[d_1126_i_]))
        res = (d_1125_diff_q_) == (0)
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
        self._crypto: Aws_Cryptography_Primitives.AtomicPrimitivesClient = None
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
        d_1127_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_1127_suite_ = (input).algorithmSuite
        d_1128_pdkResult_: Wrappers.Result
        out200_: Wrappers.Result
        out200_ = ((self).crypto).GenerateRandomBytes(AwsCryptographyPrimitivesTypes.GenerateRandomBytesInput_GenerateRandomBytesInput(AlgorithmSuites.default__.GetEncryptKeyLength(d_1127_suite_)))
        d_1128_pdkResult_ = out200_
        d_1129_pdk_: _dafny.Seq
        d_1130_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda93_(d_1131_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1131_e_)

        d_1130_valueOrError0_ = (d_1128_pdkResult_).MapFailure(lambda93_)
        if (d_1130_valueOrError0_).IsFailure():
            res = (d_1130_valueOrError0_).PropagateFailure()
            return res
        d_1129_pdk_ = (d_1130_valueOrError0_).Extract()
        d_1132_wrap_: EcdhWrapKeyMaterial
        nw45_ = EcdhWrapKeyMaterial()
        nw45_.ctor__((self).sharedSecret, (self).fixedInfo, (self).crypto)
        d_1132_wrap_ = nw45_
        d_1133_wrapOutput_: MaterialWrapping.WrapOutput
        d_1134_valueOrError1_: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.WrapOutput.default(EcdhWrapInfo.default()))()
        out201_: Wrappers.Result
        out201_ = (d_1132_wrap_).Invoke(MaterialWrapping.WrapInput_WrapInput(d_1129_pdk_, (input).algorithmSuite, (input).encryptionContext))
        d_1134_valueOrError1_ = out201_
        if (d_1134_valueOrError1_).IsFailure():
            res = (d_1134_valueOrError1_).PropagateFailure()
            return res
        d_1133_wrapOutput_ = (d_1134_valueOrError1_).Extract()
        d_1135_output_: MaterialWrapping.GenerateAndWrapOutput
        d_1135_output_ = MaterialWrapping.GenerateAndWrapOutput_GenerateAndWrapOutput(d_1129_pdk_, (d_1133_wrapOutput_).wrappedMaterial, (d_1133_wrapOutput_).wrapInfo)
        res = Wrappers.Result_Success(d_1135_output_)
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
        self._crypto: Aws_Cryptography_Primitives.AtomicPrimitivesClient = None
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
        d_1136_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_1136_suite_ = (input).algorithmSuite
        d_1137_canonicalizedEC_: _dafny.Seq
        d_1138_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1138_valueOrError0_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_1138_valueOrError0_).IsFailure():
            res = (d_1138_valueOrError0_).PropagateFailure()
            return res
        d_1137_canonicalizedEC_ = (d_1138_valueOrError0_).Extract()
        d_1139_maybeSalt_: Wrappers.Result
        out202_: Wrappers.Result
        out202_ = ((self).crypto).GenerateRandomBytes(AwsCryptographyPrimitivesTypes.GenerateRandomBytesInput_GenerateRandomBytesInput(Constants.default__.KDF__SALT__LEN))
        d_1139_maybeSalt_ = out202_
        d_1140_salt_: _dafny.Seq
        d_1141_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda94_(d_1142_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1142_e_)

        d_1141_valueOrError1_ = (d_1139_maybeSalt_).MapFailure(lambda94_)
        if (d_1141_valueOrError1_).IsFailure():
            res = (d_1141_valueOrError1_).PropagateFailure()
            return res
        d_1140_salt_ = (d_1141_valueOrError1_).Extract()
        d_1143_derivedKeyingMaterial_: _dafny.Seq
        d_1144_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out203_: Wrappers.Result
        out203_ = default__.DeriveSharedKeyingMaterial((self).sharedSecret, (self).fixedInfo, d_1140_salt_, (self).crypto)
        d_1144_valueOrError2_ = out203_
        if (d_1144_valueOrError2_).IsFailure():
            res = (d_1144_valueOrError2_).PropagateFailure()
            return res
        d_1143_derivedKeyingMaterial_ = (d_1144_valueOrError2_).Extract()
        d_1145_commitmentKey_: _dafny.Seq
        d_1145_commitmentKey_ = _dafny.Seq((d_1143_derivedKeyingMaterial_)[0:32:])
        d_1146_sharedKeyingMaterial_: _dafny.Seq
        d_1146_sharedKeyingMaterial_ = _dafny.Seq((d_1143_derivedKeyingMaterial_)[32::])
        d_1147_iv_: _dafny.Seq
        d_1147_iv_ = _dafny.Seq([0 for d_1148___v3_ in range((Constants.default__.ECDH__AES__256__ENC__ALG).ivLength)])
        d_1149_maybeWrappedPdk_: Wrappers.Result
        out204_: Wrappers.Result
        out204_ = ((self).crypto).AESEncrypt(AwsCryptographyPrimitivesTypes.AESEncryptInput_AESEncryptInput(Constants.default__.ECDH__AES__256__ENC__ALG, d_1147_iv_, d_1146_sharedKeyingMaterial_, (input).plaintextMaterial, (self).fixedInfo))
        d_1149_maybeWrappedPdk_ = out204_
        d_1150_wrappedPdk_: AwsCryptographyPrimitivesTypes.AESEncryptOutput
        d_1151_valueOrError3_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.AESEncryptOutput.default())()
        def lambda95_(d_1152_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1152_e_)

        d_1151_valueOrError3_ = (d_1149_maybeWrappedPdk_).MapFailure(lambda95_)
        if (d_1151_valueOrError3_).IsFailure():
            res = (d_1151_valueOrError3_).PropagateFailure()
            return res
        d_1150_wrappedPdk_ = (d_1151_valueOrError3_).Extract()
        d_1153_output_: MaterialWrapping.WrapOutput
        d_1153_output_ = MaterialWrapping.WrapOutput_WrapOutput((((d_1140_salt_) + (d_1145_commitmentKey_)) + ((d_1150_wrappedPdk_).cipherText)) + ((d_1150_wrappedPdk_).authTag), EcdhWrapInfo_EcdhWrapInfo())
        res = Wrappers.Result_Success(d_1153_output_)
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
