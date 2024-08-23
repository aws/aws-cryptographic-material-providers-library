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
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsHierarchicalKeyring as AwsKmsHierarchicalKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsRsaKeyring as AwsKmsRsaKeyring
import aws_cryptographic_materialproviders.internaldafny.generated.EcdhEdkWrapping as EcdhEdkWrapping

# Module: RawECDHKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def ValidPublicKeyLength(p):
        return (True) and ((((len(p)) == (Constants.default__.ECDH__PUBLIC__KEY__LEN__ECC__NIST__256)) or ((len(p)) == (Constants.default__.ECDH__PUBLIC__KEY__LEN__ECC__NIST__384))) or ((len(p)) == (Constants.default__.ECDH__PUBLIC__KEY__LEN__ECC__NIST__521)))

    @staticmethod
    def ValidCompressedPublicKeyLength(p):
        return (True) and ((((len(p)) == (Constants.default__.ECDH__PUBLIC__KEY__COMPRESSED__LEN__ECC__NIST__256)) or ((len(p)) == (Constants.default__.ECDH__PUBLIC__KEY__COMPRESSED__LEN__ECC__NIST__384))) or ((len(p)) == (Constants.default__.ECDH__PUBLIC__KEY__COMPRESSED__LEN__ECC__NIST__521)))

    @staticmethod
    def ValidProviderInfoLength(p):
        return (((len(p)) == (Constants.default__.ECDH__PROVIDER__INFO__256__LEN)) or ((len(p)) == (Constants.default__.ECDH__PROVIDER__INFO__384__LEN))) or ((len(p)) == (Constants.default__.ECDH__PROVIDER__INFO__521__LEN))

    @staticmethod
    def LocalDeriveSharedSecret(senderPrivateKey, recipientPublicKey, curveSpec, crypto):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1156_maybeSharedSecret_: Wrappers.Result
        out207_: Wrappers.Result
        out207_ = (crypto).DeriveSharedSecret(AwsCryptographyPrimitivesTypes.DeriveSharedSecretInput_DeriveSharedSecretInput(curveSpec, senderPrivateKey, recipientPublicKey))
        d_1156_maybeSharedSecret_ = out207_
        d_1157_sharedSecretOutput_: AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput
        d_1158_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput.default())()
        def lambda96_(d_1159_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1159_e_)

        d_1158_valueOrError0_ = (d_1156_maybeSharedSecret_).MapFailure(lambda96_)
        if (d_1158_valueOrError0_).IsFailure():
            res = (d_1158_valueOrError0_).PropagateFailure()
            return res
        d_1157_sharedSecretOutput_ = (d_1158_valueOrError0_).Extract()
        res = Wrappers.Result_Success((d_1157_sharedSecretOutput_).sharedSecret)
        return res
        return res

    @staticmethod
    def CompressPublicKey(publicKey, curveSpec, crypto):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1160_maybeCompressedPublicKey_: Wrappers.Result
        out208_: Wrappers.Result
        out208_ = (crypto).CompressPublicKey(AwsCryptographyPrimitivesTypes.CompressPublicKeyInput_CompressPublicKeyInput(publicKey, curveSpec))
        d_1160_maybeCompressedPublicKey_ = out208_
        d_1161_compresedPublicKey_: AwsCryptographyPrimitivesTypes.CompressPublicKeyOutput
        d_1162_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.CompressPublicKeyOutput.default())()
        def lambda97_(d_1163_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1163_e_)

        d_1162_valueOrError0_ = (d_1160_maybeCompressedPublicKey_).MapFailure(lambda97_)
        if (d_1162_valueOrError0_).IsFailure():
            res = (d_1162_valueOrError0_).PropagateFailure()
            return res
        d_1161_compresedPublicKey_ = (d_1162_valueOrError0_).Extract()
        res = Wrappers.Result_Success((d_1161_compresedPublicKey_).compressedPublicKey)
        return res
        return res

    @staticmethod
    def DecompressPublicKey(publicKey, curveSpec, crypto):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1164_maybePublicKey_: Wrappers.Result
        out209_: Wrappers.Result
        out209_ = (crypto).DecompressPublicKey(AwsCryptographyPrimitivesTypes.DecompressPublicKeyInput_DecompressPublicKeyInput(publicKey, curveSpec))
        d_1164_maybePublicKey_ = out209_
        d_1165_publicKey_: AwsCryptographyPrimitivesTypes.DecompressPublicKeyOutput
        d_1166_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.DecompressPublicKeyOutput.default())()
        def lambda98_(d_1167_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1167_e_)

        d_1166_valueOrError0_ = (d_1164_maybePublicKey_).MapFailure(lambda98_)
        if (d_1166_valueOrError0_).IsFailure():
            res = (d_1166_valueOrError0_).PropagateFailure()
            return res
        d_1165_publicKey_ = (d_1166_valueOrError0_).Extract()
        res = Wrappers.Result_Success(((d_1165_publicKey_).publicKey).der)
        return res
        return res

    @staticmethod
    def SerializeProviderInfo(senderPublicKey, recipientPublicKey):
        return ((((default__.RAW__ECDH__KEYRING__VERSION) + (StandardLibrary_UInt.default__.UInt32ToSeq(len(recipientPublicKey)))) + (recipientPublicKey)) + (StandardLibrary_UInt.default__.UInt32ToSeq(len(senderPublicKey)))) + (senderPublicKey)

    @staticmethod
    def GenerateEphemeralEccKeyPair(curveSpec, crypto):
        res: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
        d_1168_maybeKeyPair_: Wrappers.Result
        out210_: Wrappers.Result
        out210_ = (crypto).GenerateECCKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(curveSpec))
        d_1168_maybeKeyPair_ = out210_
        d_1169_keyPair_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
        d_1170_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
        def lambda99_(d_1171_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1171_e_)

        d_1170_valueOrError0_ = (d_1168_maybeKeyPair_).MapFailure(lambda99_)
        if (d_1170_valueOrError0_).IsFailure():
            res = (d_1170_valueOrError0_).PropagateFailure()
            return res
        d_1169_keyPair_ = (d_1170_valueOrError0_).Extract()
        res = Wrappers.Result_Success(d_1169_keyPair_)
        return res

    @staticmethod
    def ValidatePublicKey(crypto, curveSpec, publicKey):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        d_1172_maybeValidate_: Wrappers.Result
        out211_: Wrappers.Result
        out211_ = (crypto).ValidatePublicKey(AwsCryptographyPrimitivesTypes.ValidatePublicKeyInput_ValidatePublicKeyInput(curveSpec, publicKey))
        d_1172_maybeValidate_ = out211_
        d_1173_validate_: AwsCryptographyPrimitivesTypes.ValidatePublicKeyOutput
        d_1174_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.ValidatePublicKeyOutput.default())()
        def lambda100_(d_1175_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1175_e_)

        d_1174_valueOrError0_ = (d_1172_maybeValidate_).MapFailure(lambda100_)
        if (d_1174_valueOrError0_).IsFailure():
            res = (d_1174_valueOrError0_).PropagateFailure()
            return res
        d_1173_validate_ = (d_1174_valueOrError0_).Extract()
        res = Wrappers.Result_Success((d_1173_validate_).success)
        return res

    @staticmethod
    def CurveSpecTypeToString(c):
        source32_ = c
        unmatched32 = True
        if unmatched32:
            if source32_.is_ECC__NIST__P256:
                unmatched32 = False
                return _dafny.Seq("p256")
        if unmatched32:
            if source32_.is_ECC__NIST__P384:
                unmatched32 = False
                return _dafny.Seq("p384")
        if unmatched32:
            if source32_.is_ECC__NIST__P521:
                unmatched32 = False
                return _dafny.Seq("p521")
        if unmatched32:
            unmatched32 = False
            return _dafny.Seq("sm2")
        raise Exception("unexpected control point")

    @staticmethod
    def E(s):
        return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(s)

    @_dafny.classproperty
    def RAW__ECDH__KEYRING__VERSION(instance):
        return _dafny.Seq([1])

class RawEcdhKeyring(Keyring.VerifiableInterface, AwsCryptographyMaterialProvidersTypes.IKeyring):
    def  __init__(self):
        self._cryptoPrimitives: AtomicPrimitives.AtomicPrimitivesClient = None
        self._keyAgreementScheme: AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations = AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations.default()()
        self._curveSpec: AwsCryptographyPrimitivesTypes.ECDHCurveSpec = AwsCryptographyPrimitivesTypes.ECDHCurveSpec.default()()
        self._recipientPublicKey: AwsCryptographyPrimitivesTypes.ECCPublicKey = AwsCryptographyPrimitivesTypes.ECCPublicKey.default()()
        self._compressedRecipientPublicKey: _dafny.Seq = _dafny.Seq({})
        self._senderPublicKey: AwsCryptographyPrimitivesTypes.ECCPublicKey = AwsCryptographyPrimitivesTypes.ECCPublicKey.default()()
        self._senderPrivateKey: AwsCryptographyPrimitivesTypes.ECCPrivateKey = AwsCryptographyPrimitivesTypes.ECCPrivateKey.default()()
        self._compressedSenderPublicKey: _dafny.Seq = _dafny.Seq({})
        pass

    def __dafnystr__(self) -> str:
        return "RawECDHKeyring.RawEcdhKeyring"
    def OnDecrypt(self, input):
        out212_: Wrappers.Result
        out212_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnDecrypt(self, input)
        return out212_

    def OnEncrypt(self, input):
        out213_: Wrappers.Result
        out213_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnEncrypt(self, input)
        return out213_

    def ctor__(self, keyAgreementScheme, curveSpec, senderPrivateKey, senderPublicKey, recipientPublicKey, compressedSenderPublicKey, compressedRecipientPublicKey, cryptoPrimitives):
        (self)._keyAgreementScheme = keyAgreementScheme
        (self)._curveSpec = curveSpec
        (self)._cryptoPrimitives = cryptoPrimitives
        (self)._recipientPublicKey = AwsCryptographyPrimitivesTypes.ECCPublicKey_ECCPublicKey(recipientPublicKey)
        (self)._compressedRecipientPublicKey = compressedRecipientPublicKey
        if (((senderPublicKey).is_Some) and ((senderPrivateKey).is_Some)) and ((compressedSenderPublicKey).is_Some):
            (self)._senderPublicKey = AwsCryptographyPrimitivesTypes.ECCPublicKey_ECCPublicKey((senderPublicKey).value)
            (self)._senderPrivateKey = AwsCryptographyPrimitivesTypes.ECCPrivateKey_ECCPrivateKey((senderPrivateKey).value)
            (self)._compressedSenderPublicKey = (compressedSenderPublicKey).value
        elif True:
            (self)._senderPublicKey = AwsCryptographyPrimitivesTypes.ECCPublicKey_ECCPublicKey(_dafny.Seq([]))
            (self)._senderPrivateKey = AwsCryptographyPrimitivesTypes.ECCPrivateKey_ECCPrivateKey(_dafny.Seq([]))
            (self)._compressedSenderPublicKey = _dafny.Seq([])

    def OnEncrypt_k(self, input):
        res: Wrappers.Result = None
        if ((self).keyAgreementScheme).is_PublicKeyDiscovery:
            res = Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("PublicKeyDiscovery Key Agreement Scheme is forbidden on encrypt.")))
            return res
        d_1176_operationSenderPrivateKey_: AwsCryptographyPrimitivesTypes.ECCPrivateKey = AwsCryptographyPrimitivesTypes.ECCPrivateKey.default()()
        d_1177_operationSenderPublicKey_: AwsCryptographyPrimitivesTypes.ECCPublicKey = AwsCryptographyPrimitivesTypes.ECCPublicKey.default()()
        d_1178_operationCompressedSenderPublicKey_: _dafny.Seq = _dafny.Seq({})
        if ((self).keyAgreementScheme).is_EphemeralPrivateKeyToStaticPublicKey:
            d_1179_ephemeralKeyPair_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
            d_1180_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
            out214_: Wrappers.Result
            out214_ = default__.GenerateEphemeralEccKeyPair((self).curveSpec, (self).cryptoPrimitives)
            d_1180_valueOrError0_ = out214_
            if (d_1180_valueOrError0_).IsFailure():
                res = (d_1180_valueOrError0_).PropagateFailure()
                return res
            d_1179_ephemeralKeyPair_ = (d_1180_valueOrError0_).Extract()
            d_1176_operationSenderPrivateKey_ = (d_1179_ephemeralKeyPair_).privateKey
            d_1177_operationSenderPublicKey_ = (d_1179_ephemeralKeyPair_).publicKey
            d_1181_operationCompressedSenderPublicKey_q_: _dafny.Seq
            d_1182_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            out215_: Wrappers.Result
            out215_ = default__.CompressPublicKey(AwsCryptographyPrimitivesTypes.ECCPublicKey_ECCPublicKey((d_1177_operationSenderPublicKey_).der), (self).curveSpec, (self).cryptoPrimitives)
            d_1182_valueOrError1_ = out215_
            if (d_1182_valueOrError1_).IsFailure():
                res = (d_1182_valueOrError1_).PropagateFailure()
                return res
            d_1181_operationCompressedSenderPublicKey_q_ = (d_1182_valueOrError1_).Extract()
            d_1178_operationCompressedSenderPublicKey_ = d_1181_operationCompressedSenderPublicKey_q_
        elif True:
            d_1176_operationSenderPrivateKey_ = (self).senderPrivateKey
            d_1177_operationSenderPublicKey_ = (self).senderPublicKey
            d_1178_operationCompressedSenderPublicKey_ = (self).compressedSenderPublicKey
        d_1183_materials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_1183_materials_ = (input).materials
        d_1184_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_1184_suite_ = ((input).materials).algorithmSuite
        d_1185_sharedSecret_: _dafny.Seq
        d_1186_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out216_: Wrappers.Result
        out216_ = default__.LocalDeriveSharedSecret(d_1176_operationSenderPrivateKey_, (self).recipientPublicKey, (self).curveSpec, (self).cryptoPrimitives)
        d_1186_valueOrError2_ = out216_
        if (d_1186_valueOrError2_).IsFailure():
            res = (d_1186_valueOrError2_).PropagateFailure()
            return res
        d_1185_sharedSecret_ = (d_1186_valueOrError2_).Extract()
        d_1187_curveSpecUtf8_: _dafny.Seq
        d_1188_valueOrError3_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_1188_valueOrError3_ = (UTF8.default__.Encode(default__.CurveSpecTypeToString((self).curveSpec))).MapFailure(default__.E)
        if (d_1188_valueOrError3_).IsFailure():
            res = (d_1188_valueOrError3_).PropagateFailure()
            return res
        d_1187_curveSpecUtf8_ = (d_1188_valueOrError3_).Extract()
        d_1189_canonicalizedEC_: _dafny.Seq
        d_1190_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1190_valueOrError4_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD(((input).materials).encryptionContext)
        if (d_1190_valueOrError4_).IsFailure():
            res = (d_1190_valueOrError4_).PropagateFailure()
            return res
        d_1189_canonicalizedEC_ = (d_1190_valueOrError4_).Extract()
        d_1191_fixedInfo_: _dafny.Seq
        d_1191_fixedInfo_ = EcdhEdkWrapping.default__.SerializeFixedInfo(Constants.default__.ECDH__KDF__UTF8, d_1187_curveSpecUtf8_, d_1178_operationCompressedSenderPublicKey_, (self).compressedRecipientPublicKey, d_1189_canonicalizedEC_, default__.RAW__ECDH__KEYRING__VERSION)
        d_1192_ecdhGenerateAndWrap_: EcdhEdkWrapping.EcdhGenerateAndWrapKeyMaterial
        nw46_ = EcdhEdkWrapping.EcdhGenerateAndWrapKeyMaterial()
        nw46_.ctor__(d_1185_sharedSecret_, d_1191_fixedInfo_, (self).cryptoPrimitives)
        d_1192_ecdhGenerateAndWrap_ = nw46_
        d_1193_ecdhWrap_: EcdhEdkWrapping.EcdhWrapKeyMaterial
        nw47_ = EcdhEdkWrapping.EcdhWrapKeyMaterial()
        nw47_.ctor__(d_1185_sharedSecret_, d_1191_fixedInfo_, (self).cryptoPrimitives)
        d_1193_ecdhWrap_ = nw47_
        d_1194_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_1195_valueOrError5_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.WrapEdkMaterialOutput.default(EcdhEdkWrapping.EcdhWrapInfo.default()))()
        out217_: Wrappers.Result
        out217_ = EdkWrapping.default__.WrapEdkMaterial(d_1183_materials_, d_1193_ecdhWrap_, d_1192_ecdhGenerateAndWrap_)
        d_1195_valueOrError5_ = out217_
        if (d_1195_valueOrError5_).IsFailure():
            res = (d_1195_valueOrError5_).PropagateFailure()
            return res
        d_1194_wrapOutput_ = (d_1195_valueOrError5_).Extract()
        d_1196_symmetricSigningKeyList_: Wrappers.Option
        d_1196_symmetricSigningKeyList_ = (Wrappers.Option_Some(_dafny.Seq([((d_1194_wrapOutput_).symmetricSigningKey).value])) if ((d_1194_wrapOutput_).symmetricSigningKey).is_Some else Wrappers.Option_None())
        d_1197_valueOrError6_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1197_valueOrError6_ = Wrappers.default__.Need((default__.ValidCompressedPublicKeyLength(d_1178_operationCompressedSenderPublicKey_)) and (default__.ValidCompressedPublicKeyLength((self).compressedRecipientPublicKey)), default__.E(_dafny.Seq("Invalid compressed public key length.")))
        if (d_1197_valueOrError6_).IsFailure():
            res = (d_1197_valueOrError6_).PropagateFailure()
            return res
        d_1198_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_1198_edk_ = AwsCryptographyMaterialProvidersTypes.EncryptedDataKey_EncryptedDataKey(Constants.default__.RAW__ECDH__PROVIDER__ID, default__.SerializeProviderInfo(d_1178_operationCompressedSenderPublicKey_, (self).compressedRecipientPublicKey), (d_1194_wrapOutput_).wrappedMaterial)
        if (d_1194_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_1199_result_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_1200_valueOrError7_: Wrappers.Result = None
            d_1200_valueOrError7_ = Materials.default__.EncryptionMaterialAddDataKey(d_1183_materials_, (d_1194_wrapOutput_).plaintextDataKey, _dafny.Seq([d_1198_edk_]), d_1196_symmetricSigningKeyList_)
            if (d_1200_valueOrError7_).IsFailure():
                res = (d_1200_valueOrError7_).PropagateFailure()
                return res
            d_1199_result_ = (d_1200_valueOrError7_).Extract()
            res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(d_1199_result_))
            return res
        elif (d_1194_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_1201_result_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_1202_valueOrError8_: Wrappers.Result = None
            d_1202_valueOrError8_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys(d_1183_materials_, _dafny.Seq([d_1198_edk_]), d_1196_symmetricSigningKeyList_)
            if (d_1202_valueOrError8_).IsFailure():
                res = (d_1202_valueOrError8_).PropagateFailure()
                return res
            d_1201_result_ = (d_1202_valueOrError8_).Extract()
            res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(d_1201_result_))
            return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        if ((self).keyAgreementScheme).is_EphemeralPrivateKeyToStaticPublicKey:
            res = Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("EphemeralPrivateKeyToStaticPublicKey Key Agreement Scheme is forbidden on decrypt.")))
            return res
        d_1203_materials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_1203_materials_ = (input).materials
        d_1204_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_1204_suite_ = ((input).materials).algorithmSuite
        d_1205_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1205_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_1203_materials_), default__.E(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_1205_valueOrError0_).IsFailure():
            res = (d_1205_valueOrError0_).PropagateFailure()
            return res
        d_1206_operationCompressedSenderPublicKey_: Wrappers.Option
        d_1206_operationCompressedSenderPublicKey_ = (Wrappers.Option_None() if ((self).compressedSenderPublicKey) == (_dafny.Seq([])) else Wrappers.Option_Some((self).compressedSenderPublicKey))
        d_1207_filter_: OnDecryptEcdhDataKeyFilter
        nw48_ = OnDecryptEcdhDataKeyFilter()
        nw48_.ctor__((self).keyAgreementScheme, (self).compressedRecipientPublicKey, d_1206_operationCompressedSenderPublicKey_)
        d_1207_filter_ = nw48_
        d_1208_edksToAttempt_: _dafny.Seq
        d_1209_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out218_: Wrappers.Result
        out218_ = Actions.default__.FilterWithResult(d_1207_filter_, (input).encryptedDataKeys)
        d_1209_valueOrError1_ = out218_
        if (d_1209_valueOrError1_).IsFailure():
            res = (d_1209_valueOrError1_).PropagateFailure()
            return res
        d_1208_edksToAttempt_ = (d_1209_valueOrError1_).Extract()
        if (0) == (len(d_1208_edksToAttempt_)):
            d_1210_errorMessage_: _dafny.Seq
            d_1211_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            d_1211_valueOrError2_ = ErrorMessages.default__.IncorrectDataKeys((input).encryptedDataKeys, ((input).materials).algorithmSuite, _dafny.Seq(""))
            if (d_1211_valueOrError2_).IsFailure():
                res = (d_1211_valueOrError2_).PropagateFailure()
                return res
            d_1210_errorMessage_ = (d_1211_valueOrError2_).Extract()
            res = Wrappers.Result_Failure(default__.E(d_1210_errorMessage_))
            return res
        d_1212_decryptClosure_: Actions.ActionWithResult
        nw49_ = DecryptSingleEncryptedDataKey()
        nw49_.ctor__(d_1203_materials_, (self).cryptoPrimitives, (self).compressedSenderPublicKey, (self).compressedRecipientPublicKey, (self).keyAgreementScheme, (self).curveSpec)
        d_1212_decryptClosure_ = nw49_
        d_1213_outcome_: Wrappers.Result
        out219_: Wrappers.Result
        out219_ = Actions.default__.ReduceToSuccess(d_1212_decryptClosure_, d_1208_edksToAttempt_)
        d_1213_outcome_ = out219_
        d_1214_SealedDecryptionMaterials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_1215_valueOrError3_: Wrappers.Result = None
        def lambda101_(d_1216_errors_):
            return AwsCryptographyMaterialProvidersTypes.Error_CollectionOfErrors(d_1216_errors_, _dafny.Seq("No Configured Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."))

        d_1215_valueOrError3_ = (d_1213_outcome_).MapFailure(lambda101_)
        if (d_1215_valueOrError3_).IsFailure():
            res = (d_1215_valueOrError3_).PropagateFailure()
            return res
        d_1214_SealedDecryptionMaterials_ = (d_1215_valueOrError3_).Extract()
        res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnDecryptOutput_OnDecryptOutput(d_1214_SealedDecryptionMaterials_))
        return res
        return res

    @property
    def cryptoPrimitives(self):
        return self._cryptoPrimitives
    @property
    def keyAgreementScheme(self):
        return self._keyAgreementScheme
    @property
    def curveSpec(self):
        return self._curveSpec
    @property
    def recipientPublicKey(self):
        return self._recipientPublicKey
    @property
    def compressedRecipientPublicKey(self):
        return self._compressedRecipientPublicKey
    @property
    def senderPublicKey(self):
        return self._senderPublicKey
    @property
    def senderPrivateKey(self):
        return self._senderPrivateKey
    @property
    def compressedSenderPublicKey(self):
        return self._compressedSenderPublicKey

class OnDecryptEcdhDataKeyFilter(Actions.DeterministicActionWithResult, Actions.DeterministicAction):
    def  __init__(self):
        self._keyAgreementScheme: AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations = AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations.default()()
        self._compressedRecipientPublicKey: _dafny.Seq = _dafny.Seq({})
        self._compressedSenderPublicKey: _dafny.Seq = _dafny.Seq({})
        pass

    def __dafnystr__(self) -> str:
        return "RawECDHKeyring.OnDecryptEcdhDataKeyFilter"
    def ctor__(self, keyAgreementScheme, compressedRecipientPublicKey, compressedSenderPublicKey):
        (self)._keyAgreementScheme = keyAgreementScheme
        (self)._compressedRecipientPublicKey = compressedRecipientPublicKey
        if (compressedSenderPublicKey).is_Some:
            (self)._compressedSenderPublicKey = (compressedSenderPublicKey).value
        elif True:
            (self)._compressedSenderPublicKey = _dafny.Seq([])

    def Invoke(self, edk):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        d_1217_providerInfo_: _dafny.Seq
        d_1217_providerInfo_ = (edk).keyProviderInfo
        d_1218_providerId_: _dafny.Seq
        d_1218_providerId_ = (edk).keyProviderId
        if ((d_1218_providerId_) != (Constants.default__.RAW__ECDH__PROVIDER__ID)) and ((d_1218_providerId_) != (Constants.default__.KMS__ECDH__PROVIDER__ID)):
            res = Wrappers.Result_Success(False)
            return res
        d_1219_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1219_valueOrError0_ = Wrappers.default__.Need(((len(d_1217_providerInfo_)) <= (Constants.default__.ECDH__PROVIDER__INFO__521__LEN)) and (default__.ValidProviderInfoLength(d_1217_providerInfo_)), default__.E(_dafny.Seq("EDK ProviderInfo longer than expected")))
        if (d_1219_valueOrError0_).IsFailure():
            res = (d_1219_valueOrError0_).PropagateFailure()
            return res
        d_1220_keyringVersion_: int
        d_1220_keyringVersion_ = (d_1217_providerInfo_)[0]
        d_1221_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1221_valueOrError1_ = Wrappers.default__.Need((_dafny.Seq([d_1220_keyringVersion_])) == (default__.RAW__ECDH__KEYRING__VERSION), default__.E(_dafny.Seq("Incorrect Keyring version found in provider info.")))
        if (d_1221_valueOrError1_).IsFailure():
            res = (d_1221_valueOrError1_).PropagateFailure()
            return res
        d_1222_recipientPublicKeyLength_: int
        d_1222_recipientPublicKeyLength_ = StandardLibrary_UInt.default__.SeqToUInt32(_dafny.Seq((d_1217_providerInfo_)[Constants.default__.ECDH__PROVIDER__INFO__RPL__INDEX:Constants.default__.ECDH__PROVIDER__INFO__RPK__INDEX:]))
        d_1223_recipientPublicKeyLengthIndex_: int
        d_1223_recipientPublicKeyLengthIndex_ = (Constants.default__.ECDH__PROVIDER__INFO__RPK__INDEX) + (d_1222_recipientPublicKeyLength_)
        d_1224_senderPublicKeyIndex_: int
        d_1224_senderPublicKeyIndex_ = (d_1223_recipientPublicKeyLengthIndex_) + (Constants.default__.ECDH__PROVIDER__INFO__PUBLIC__KEY__LEN)
        d_1225_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1225_valueOrError2_ = Wrappers.default__.Need(((d_1223_recipientPublicKeyLengthIndex_) + (4)) < (len(d_1217_providerInfo_)), default__.E(_dafny.Seq("Key Provider Info Serialization Error. Serialized length less than expected.")))
        if (d_1225_valueOrError2_).IsFailure():
            res = (d_1225_valueOrError2_).PropagateFailure()
            return res
        d_1226_providerInfoRecipientPublicKey_: _dafny.Seq
        d_1226_providerInfoRecipientPublicKey_ = _dafny.Seq((d_1217_providerInfo_)[Constants.default__.ECDH__PROVIDER__INFO__RPK__INDEX:d_1223_recipientPublicKeyLengthIndex_:])
        d_1227_providerInfoSenderPublicKey_: _dafny.Seq
        d_1227_providerInfoSenderPublicKey_ = _dafny.Seq((d_1217_providerInfo_)[d_1224_senderPublicKeyIndex_::])
        if ((self).keyAgreementScheme).is_PublicKeyDiscovery:
            res = Wrappers.Result_Success(((self).compressedRecipientPublicKey) == (d_1226_providerInfoRecipientPublicKey_))
            return res
        elif True:
            res = Wrappers.Result_Success(((((self).compressedSenderPublicKey) == (d_1227_providerInfoSenderPublicKey_)) and (((self).compressedRecipientPublicKey) == (d_1226_providerInfoRecipientPublicKey_))) or ((((self).compressedSenderPublicKey) == (d_1226_providerInfoRecipientPublicKey_)) and (((self).compressedRecipientPublicKey) == (d_1227_providerInfoSenderPublicKey_))))
            return res
        return res

    @property
    def keyAgreementScheme(self):
        return self._keyAgreementScheme
    @property
    def compressedRecipientPublicKey(self):
        return self._compressedRecipientPublicKey
    @property
    def compressedSenderPublicKey(self):
        return self._compressedSenderPublicKey

class DecryptSingleEncryptedDataKey(Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._materials: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials = None
        self._cryptoPrimitives: AtomicPrimitives.AtomicPrimitivesClient = None
        self._recipientPublicKey: _dafny.Seq = _dafny.Seq({})
        self._senderPublicKey: _dafny.Seq = _dafny.Seq({})
        self._keyAgreementScheme: AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations = AwsCryptographyMaterialProvidersTypes.RawEcdhStaticConfigurations.default()()
        self._curveSpec: AwsCryptographyPrimitivesTypes.ECDHCurveSpec = AwsCryptographyPrimitivesTypes.ECDHCurveSpec.default()()
        pass

    def __dafnystr__(self) -> str:
        return "RawECDHKeyring.DecryptSingleEncryptedDataKey"
    def ctor__(self, materials, cryptoPrimitives, senderPublicKey, recipientPublicKey, keyAgreementScheme, curveSpec):
        (self)._materials = materials
        (self)._cryptoPrimitives = cryptoPrimitives
        (self)._recipientPublicKey = recipientPublicKey
        (self)._senderPublicKey = senderPublicKey
        (self)._keyAgreementScheme = keyAgreementScheme
        (self)._curveSpec = curveSpec

    def Invoke(self, edk):
        res: Wrappers.Result = None
        d_1228_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1228_valueOrError0_ = Wrappers.default__.Need(UTF8.default__.ValidUTF8Seq((edk).keyProviderId), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received invalid EDK provider id for AWS KMS ECDH Keyring")))
        if (d_1228_valueOrError0_).IsFailure():
            res = (d_1228_valueOrError0_).PropagateFailure()
            return res
        d_1229_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_1229_suite_ = ((self).materials).algorithmSuite
        d_1230_keyProviderId_: _dafny.Seq
        d_1230_keyProviderId_ = (edk).keyProviderId
        d_1231_providerInfo_: _dafny.Seq
        d_1231_providerInfo_ = (edk).keyProviderInfo
        d_1232_ciphertext_: _dafny.Seq
        d_1232_ciphertext_ = (edk).ciphertext
        d_1233_providerWrappedMaterial_: _dafny.Seq
        d_1234_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1234_valueOrError1_ = EdkWrapping.default__.GetProviderWrappedMaterial(d_1232_ciphertext_, d_1229_suite_)
        if (d_1234_valueOrError1_).IsFailure():
            res = (d_1234_valueOrError1_).PropagateFailure()
            return res
        d_1233_providerWrappedMaterial_ = (d_1234_valueOrError1_).Extract()
        d_1235_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1235_valueOrError2_ = Wrappers.default__.Need(((len(d_1231_providerInfo_)) <= (Constants.default__.ECDH__PROVIDER__INFO__521__LEN)) and (default__.ValidProviderInfoLength(d_1231_providerInfo_)), default__.E(_dafny.Seq("EDK ProviderInfo longer than expected")))
        if (d_1235_valueOrError2_).IsFailure():
            res = (d_1235_valueOrError2_).PropagateFailure()
            return res
        d_1236_keyringVersion_: int
        d_1236_keyringVersion_ = (d_1231_providerInfo_)[0]
        d_1237_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1237_valueOrError3_ = Wrappers.default__.Need((_dafny.Seq([d_1236_keyringVersion_])) == (default__.RAW__ECDH__KEYRING__VERSION), default__.E(_dafny.Seq("Incorrect Keyring version found in provider info.")))
        if (d_1237_valueOrError3_).IsFailure():
            res = (d_1237_valueOrError3_).PropagateFailure()
            return res
        d_1238_recipientPublicKeyLength_: int
        d_1238_recipientPublicKeyLength_ = StandardLibrary_UInt.default__.SeqToUInt32(_dafny.Seq((d_1231_providerInfo_)[Constants.default__.ECDH__PROVIDER__INFO__RPL__INDEX:Constants.default__.ECDH__PROVIDER__INFO__RPK__INDEX:]))
        d_1239_recipientPublicKeyLengthIndex_: int
        d_1239_recipientPublicKeyLengthIndex_ = (Constants.default__.ECDH__PROVIDER__INFO__RPK__INDEX) + (d_1238_recipientPublicKeyLength_)
        d_1240_senderPublicKeyIndex_: int
        d_1240_senderPublicKeyIndex_ = (d_1239_recipientPublicKeyLengthIndex_) + (Constants.default__.ECDH__PROVIDER__INFO__PUBLIC__KEY__LEN)
        d_1241_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1241_valueOrError4_ = Wrappers.default__.Need(((d_1239_recipientPublicKeyLengthIndex_) + (4)) < (len(d_1231_providerInfo_)), default__.E(_dafny.Seq("Key Provider Info Serialization Error. Serialized length less than expected.")))
        if (d_1241_valueOrError4_).IsFailure():
            res = (d_1241_valueOrError4_).PropagateFailure()
            return res
        d_1242_providerInfoRecipientPublicKey_: _dafny.Seq
        d_1242_providerInfoRecipientPublicKey_ = _dafny.Seq((d_1231_providerInfo_)[Constants.default__.ECDH__PROVIDER__INFO__RPK__INDEX:d_1239_recipientPublicKeyLengthIndex_:])
        d_1243_providerInfoSenderPublicKey_: _dafny.Seq
        d_1243_providerInfoSenderPublicKey_ = _dafny.Seq((d_1231_providerInfo_)[d_1240_senderPublicKeyIndex_::])
        d_1244_senderPublicKey_: _dafny.Seq
        d_1245_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out220_: Wrappers.Result
        out220_ = default__.DecompressPublicKey(d_1243_providerInfoSenderPublicKey_, (self).curveSpec, (self).cryptoPrimitives)
        d_1245_valueOrError5_ = out220_
        if (d_1245_valueOrError5_).IsFailure():
            res = (d_1245_valueOrError5_).PropagateFailure()
            return res
        d_1244_senderPublicKey_ = (d_1245_valueOrError5_).Extract()
        d_1246_recipientPublicKey_: _dafny.Seq
        d_1247_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out221_: Wrappers.Result
        out221_ = default__.DecompressPublicKey(d_1242_providerInfoRecipientPublicKey_, (self).curveSpec, (self).cryptoPrimitives)
        d_1247_valueOrError6_ = out221_
        if (d_1247_valueOrError6_).IsFailure():
            res = (d_1247_valueOrError6_).PropagateFailure()
            return res
        d_1246_recipientPublicKey_ = (d_1247_valueOrError6_).Extract()
        d_1248___v0_: bool
        d_1249_valueOrError7_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        out222_: Wrappers.Result
        out222_ = default__.ValidatePublicKey((self).cryptoPrimitives, (self).curveSpec, d_1244_senderPublicKey_)
        d_1249_valueOrError7_ = out222_
        if (d_1249_valueOrError7_).IsFailure():
            res = (d_1249_valueOrError7_).PropagateFailure()
            return res
        d_1248___v0_ = (d_1249_valueOrError7_).Extract()
        d_1250___v1_: bool
        d_1251_valueOrError8_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        out223_: Wrappers.Result
        out223_ = default__.ValidatePublicKey((self).cryptoPrimitives, (self).curveSpec, d_1246_recipientPublicKey_)
        d_1251_valueOrError8_ = out223_
        if (d_1251_valueOrError8_).IsFailure():
            res = (d_1251_valueOrError8_).PropagateFailure()
            return res
        d_1250___v1_ = (d_1251_valueOrError8_).Extract()
        d_1252_sharedSecretPublicKey_: _dafny.Seq = _dafny.Seq({})
        d_1253_sharedSecretPrivateKey_: _dafny.Seq = _dafny.Seq({})
        if ((self).keyAgreementScheme).is_PublicKeyDiscovery:
            d_1252_sharedSecretPublicKey_ = d_1244_senderPublicKey_
            d_1253_sharedSecretPrivateKey_ = (((self).keyAgreementScheme).PublicKeyDiscovery).recipientStaticPrivateKey
        elif ((self).keyAgreementScheme).is_RawPrivateKeyToStaticPublicKey:
            d_1253_sharedSecretPrivateKey_ = (((self).keyAgreementScheme).RawPrivateKeyToStaticPublicKey).senderStaticPrivateKey
            if ((((self).keyAgreementScheme).RawPrivateKeyToStaticPublicKey).recipientPublicKey) == (d_1246_recipientPublicKey_):
                d_1252_sharedSecretPublicKey_ = d_1246_recipientPublicKey_
            elif True:
                d_1252_sharedSecretPublicKey_ = d_1244_senderPublicKey_
        elif ((self).keyAgreementScheme).is_EphemeralPrivateKeyToStaticPublicKey:
            res = Wrappers.Result_Failure(default__.E(_dafny.Seq("EphemeralPrivateKeyToStaticPublicKey Not allowed on decrypt")))
            return res
        elif True:
            raise Exception("unreachable alternative")
        d_1254___v2_: bool
        d_1255_valueOrError9_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        out224_: Wrappers.Result
        out224_ = default__.ValidatePublicKey((self).cryptoPrimitives, (self).curveSpec, d_1252_sharedSecretPublicKey_)
        d_1255_valueOrError9_ = out224_
        if (d_1255_valueOrError9_).IsFailure():
            res = (d_1255_valueOrError9_).PropagateFailure()
            return res
        d_1254___v2_ = (d_1255_valueOrError9_).Extract()
        d_1256_sharedSecret_: _dafny.Seq
        d_1257_valueOrError10_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out225_: Wrappers.Result
        out225_ = default__.LocalDeriveSharedSecret(AwsCryptographyPrimitivesTypes.ECCPrivateKey_ECCPrivateKey(d_1253_sharedSecretPrivateKey_), AwsCryptographyPrimitivesTypes.ECCPublicKey_ECCPublicKey(d_1252_sharedSecretPublicKey_), (self).curveSpec, (self).cryptoPrimitives)
        d_1257_valueOrError10_ = out225_
        if (d_1257_valueOrError10_).IsFailure():
            res = (d_1257_valueOrError10_).PropagateFailure()
            return res
        d_1256_sharedSecret_ = (d_1257_valueOrError10_).Extract()
        d_1258_ecdhUnwrap_: EcdhEdkWrapping.EcdhUnwrap
        nw50_ = EcdhEdkWrapping.EcdhUnwrap()
        nw50_.ctor__(d_1243_providerInfoSenderPublicKey_, d_1242_providerInfoRecipientPublicKey_, d_1256_sharedSecret_, default__.RAW__ECDH__KEYRING__VERSION, (self).curveSpec, (self).cryptoPrimitives)
        d_1258_ecdhUnwrap_ = nw50_
        d_1259_unwrapOutputRes_: Wrappers.Result
        out226_: Wrappers.Result
        out226_ = EdkWrapping.default__.UnwrapEdkMaterial((edk).ciphertext, (self).materials, d_1258_ecdhUnwrap_)
        d_1259_unwrapOutputRes_ = out226_
        d_1260_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_1261_valueOrError11_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.UnwrapEdkMaterialOutput.default(EcdhEdkWrapping.EcdhUnwrapInfo.default()))()
        d_1261_valueOrError11_ = d_1259_unwrapOutputRes_
        if (d_1261_valueOrError11_).IsFailure():
            res = (d_1261_valueOrError11_).PropagateFailure()
            return res
        d_1260_unwrapOutput_ = (d_1261_valueOrError11_).Extract()
        d_1262_result_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_1263_valueOrError12_: Wrappers.Result = None
        d_1263_valueOrError12_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_1260_unwrapOutput_).plaintextDataKey, (d_1260_unwrapOutput_).symmetricSigningKey)
        if (d_1263_valueOrError12_).IsFailure():
            res = (d_1263_valueOrError12_).PropagateFailure()
            return res
        d_1262_result_ = (d_1263_valueOrError12_).Extract()
        res = Wrappers.Result_Success(d_1262_result_)
        return res
        return res

    @property
    def materials(self):
        return self._materials
    @property
    def cryptoPrimitives(self):
        return self._cryptoPrimitives
    @property
    def recipientPublicKey(self):
        return self._recipientPublicKey
    @property
    def senderPublicKey(self):
        return self._senderPublicKey
    @property
    def keyAgreementScheme(self):
        return self._keyAgreementScheme
    @property
    def curveSpec(self):
        return self._curveSpec
