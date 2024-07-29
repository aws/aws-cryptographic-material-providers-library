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
        d_1154_maybeSharedSecret_: Wrappers.Result
        out205_: Wrappers.Result
        out205_ = (crypto).DeriveSharedSecret(AwsCryptographyPrimitivesTypes.DeriveSharedSecretInput_DeriveSharedSecretInput(curveSpec, senderPrivateKey, recipientPublicKey))
        d_1154_maybeSharedSecret_ = out205_
        d_1155_sharedSecretOutput_: AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput
        d_1156_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput.default())()
        def lambda96_(d_1157_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1157_e_)

        d_1156_valueOrError0_ = (d_1154_maybeSharedSecret_).MapFailure(lambda96_)
        if (d_1156_valueOrError0_).IsFailure():
            res = (d_1156_valueOrError0_).PropagateFailure()
            return res
        d_1155_sharedSecretOutput_ = (d_1156_valueOrError0_).Extract()
        res = Wrappers.Result_Success((d_1155_sharedSecretOutput_).sharedSecret)
        return res
        return res

    @staticmethod
    def CompressPublicKey(publicKey, curveSpec, crypto):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1158_maybeCompressedPublicKey_: Wrappers.Result
        out206_: Wrappers.Result
        out206_ = (crypto).CompressPublicKey(AwsCryptographyPrimitivesTypes.CompressPublicKeyInput_CompressPublicKeyInput(publicKey, curveSpec))
        d_1158_maybeCompressedPublicKey_ = out206_
        d_1159_compresedPublicKey_: AwsCryptographyPrimitivesTypes.CompressPublicKeyOutput
        d_1160_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.CompressPublicKeyOutput.default())()
        def lambda97_(d_1161_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1161_e_)

        d_1160_valueOrError0_ = (d_1158_maybeCompressedPublicKey_).MapFailure(lambda97_)
        if (d_1160_valueOrError0_).IsFailure():
            res = (d_1160_valueOrError0_).PropagateFailure()
            return res
        d_1159_compresedPublicKey_ = (d_1160_valueOrError0_).Extract()
        res = Wrappers.Result_Success((d_1159_compresedPublicKey_).compressedPublicKey)
        return res
        return res

    @staticmethod
    def DecompressPublicKey(publicKey, curveSpec, crypto):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1162_maybePublicKey_: Wrappers.Result
        out207_: Wrappers.Result
        out207_ = (crypto).DecompressPublicKey(AwsCryptographyPrimitivesTypes.DecompressPublicKeyInput_DecompressPublicKeyInput(publicKey, curveSpec))
        d_1162_maybePublicKey_ = out207_
        d_1163_publicKey_: AwsCryptographyPrimitivesTypes.DecompressPublicKeyOutput
        d_1164_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.DecompressPublicKeyOutput.default())()
        def lambda98_(d_1165_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1165_e_)

        d_1164_valueOrError0_ = (d_1162_maybePublicKey_).MapFailure(lambda98_)
        if (d_1164_valueOrError0_).IsFailure():
            res = (d_1164_valueOrError0_).PropagateFailure()
            return res
        d_1163_publicKey_ = (d_1164_valueOrError0_).Extract()
        res = Wrappers.Result_Success(((d_1163_publicKey_).publicKey).der)
        return res
        return res

    @staticmethod
    def SerializeProviderInfo(senderPublicKey, recipientPublicKey):
        return ((((default__.RAW__ECDH__KEYRING__VERSION) + (StandardLibrary_UInt.default__.UInt32ToSeq(len(recipientPublicKey)))) + (recipientPublicKey)) + (StandardLibrary_UInt.default__.UInt32ToSeq(len(senderPublicKey)))) + (senderPublicKey)

    @staticmethod
    def GenerateEphemeralEccKeyPair(curveSpec, crypto):
        res: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
        d_1166_maybeKeyPair_: Wrappers.Result
        out208_: Wrappers.Result
        out208_ = (crypto).GenerateECCKeyPair(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairInput_GenerateECCKeyPairInput(curveSpec))
        d_1166_maybeKeyPair_ = out208_
        d_1167_keyPair_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
        d_1168_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
        def lambda99_(d_1169_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1169_e_)

        d_1168_valueOrError0_ = (d_1166_maybeKeyPair_).MapFailure(lambda99_)
        if (d_1168_valueOrError0_).IsFailure():
            res = (d_1168_valueOrError0_).PropagateFailure()
            return res
        d_1167_keyPair_ = (d_1168_valueOrError0_).Extract()
        res = Wrappers.Result_Success(d_1167_keyPair_)
        return res

    @staticmethod
    def ValidatePublicKey(crypto, curveSpec, publicKey):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        d_1170_maybeValidate_: Wrappers.Result
        out209_: Wrappers.Result
        out209_ = (crypto).ValidatePublicKey(AwsCryptographyPrimitivesTypes.ValidatePublicKeyInput_ValidatePublicKeyInput(curveSpec, publicKey))
        d_1170_maybeValidate_ = out209_
        d_1171_validate_: AwsCryptographyPrimitivesTypes.ValidatePublicKeyOutput
        d_1172_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.ValidatePublicKeyOutput.default())()
        def lambda100_(d_1173_e_):
            return AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographyPrimitives(d_1173_e_)

        d_1172_valueOrError0_ = (d_1170_maybeValidate_).MapFailure(lambda100_)
        if (d_1172_valueOrError0_).IsFailure():
            res = (d_1172_valueOrError0_).PropagateFailure()
            return res
        d_1171_validate_ = (d_1172_valueOrError0_).Extract()
        res = Wrappers.Result_Success((d_1171_validate_).success)
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
        out210_: Wrappers.Result
        out210_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnDecrypt(self, input)
        return out210_

    def OnEncrypt(self, input):
        out211_: Wrappers.Result
        out211_ = AwsCryptographyMaterialProvidersTypes.IKeyring.OnEncrypt(self, input)
        return out211_

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
        d_1174_operationSenderPrivateKey_: AwsCryptographyPrimitivesTypes.ECCPrivateKey = AwsCryptographyPrimitivesTypes.ECCPrivateKey.default()()
        d_1175_operationSenderPublicKey_: AwsCryptographyPrimitivesTypes.ECCPublicKey = AwsCryptographyPrimitivesTypes.ECCPublicKey.default()()
        d_1176_operationCompressedSenderPublicKey_: _dafny.Seq = _dafny.Seq({})
        if ((self).keyAgreementScheme).is_EphemeralPrivateKeyToStaticPublicKey:
            d_1177_ephemeralKeyPair_: AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput
            d_1178_valueOrError0_: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
            out212_: Wrappers.Result
            out212_ = default__.GenerateEphemeralEccKeyPair((self).curveSpec, (self).cryptoPrimitives)
            d_1178_valueOrError0_ = out212_
            if (d_1178_valueOrError0_).IsFailure():
                res = (d_1178_valueOrError0_).PropagateFailure()
                return res
            d_1177_ephemeralKeyPair_ = (d_1178_valueOrError0_).Extract()
            d_1174_operationSenderPrivateKey_ = (d_1177_ephemeralKeyPair_).privateKey
            d_1175_operationSenderPublicKey_ = (d_1177_ephemeralKeyPair_).publicKey
            d_1179_operationCompressedSenderPublicKey_q_: _dafny.Seq
            d_1180_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            out213_: Wrappers.Result
            out213_ = default__.CompressPublicKey(AwsCryptographyPrimitivesTypes.ECCPublicKey_ECCPublicKey((d_1175_operationSenderPublicKey_).der), (self).curveSpec, (self).cryptoPrimitives)
            d_1180_valueOrError1_ = out213_
            if (d_1180_valueOrError1_).IsFailure():
                res = (d_1180_valueOrError1_).PropagateFailure()
                return res
            d_1179_operationCompressedSenderPublicKey_q_ = (d_1180_valueOrError1_).Extract()
            d_1176_operationCompressedSenderPublicKey_ = d_1179_operationCompressedSenderPublicKey_q_
        elif True:
            d_1174_operationSenderPrivateKey_ = (self).senderPrivateKey
            d_1175_operationSenderPublicKey_ = (self).senderPublicKey
            d_1176_operationCompressedSenderPublicKey_ = (self).compressedSenderPublicKey
        d_1181_materials_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
        d_1181_materials_ = (input).materials
        d_1182_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_1182_suite_ = ((input).materials).algorithmSuite
        d_1183_sharedSecret_: _dafny.Seq
        d_1184_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out214_: Wrappers.Result
        out214_ = default__.LocalDeriveSharedSecret(d_1174_operationSenderPrivateKey_, (self).recipientPublicKey, (self).curveSpec, (self).cryptoPrimitives)
        d_1184_valueOrError2_ = out214_
        if (d_1184_valueOrError2_).IsFailure():
            res = (d_1184_valueOrError2_).PropagateFailure()
            return res
        d_1183_sharedSecret_ = (d_1184_valueOrError2_).Extract()
        d_1185_curveSpecUtf8_: _dafny.Seq
        d_1186_valueOrError3_: Wrappers.Result = Wrappers.Result.default(UTF8.ValidUTF8Bytes.default)()
        d_1186_valueOrError3_ = (UTF8.default__.Encode(default__.CurveSpecTypeToString((self).curveSpec))).MapFailure(default__.E)
        if (d_1186_valueOrError3_).IsFailure():
            res = (d_1186_valueOrError3_).PropagateFailure()
            return res
        d_1185_curveSpecUtf8_ = (d_1186_valueOrError3_).Extract()
        d_1187_canonicalizedEC_: _dafny.Seq
        d_1188_valueOrError4_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1188_valueOrError4_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD(((input).materials).encryptionContext)
        if (d_1188_valueOrError4_).IsFailure():
            res = (d_1188_valueOrError4_).PropagateFailure()
            return res
        d_1187_canonicalizedEC_ = (d_1188_valueOrError4_).Extract()
        d_1189_fixedInfo_: _dafny.Seq
        d_1189_fixedInfo_ = EcdhEdkWrapping.default__.SerializeFixedInfo(Constants.default__.ECDH__KDF__UTF8, d_1185_curveSpecUtf8_, d_1176_operationCompressedSenderPublicKey_, (self).compressedRecipientPublicKey, d_1187_canonicalizedEC_, default__.RAW__ECDH__KEYRING__VERSION)
        d_1190_ecdhGenerateAndWrap_: EcdhEdkWrapping.EcdhGenerateAndWrapKeyMaterial
        nw46_ = EcdhEdkWrapping.EcdhGenerateAndWrapKeyMaterial()
        nw46_.ctor__(d_1183_sharedSecret_, d_1189_fixedInfo_, (self).cryptoPrimitives)
        d_1190_ecdhGenerateAndWrap_ = nw46_
        d_1191_ecdhWrap_: EcdhEdkWrapping.EcdhWrapKeyMaterial
        nw47_ = EcdhEdkWrapping.EcdhWrapKeyMaterial()
        nw47_.ctor__(d_1183_sharedSecret_, d_1189_fixedInfo_, (self).cryptoPrimitives)
        d_1191_ecdhWrap_ = nw47_
        d_1192_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_1193_valueOrError5_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.WrapEdkMaterialOutput.default(EcdhEdkWrapping.EcdhWrapInfo.default()))()
        out215_: Wrappers.Result
        out215_ = EdkWrapping.default__.WrapEdkMaterial(d_1181_materials_, d_1191_ecdhWrap_, d_1190_ecdhGenerateAndWrap_)
        d_1193_valueOrError5_ = out215_
        if (d_1193_valueOrError5_).IsFailure():
            res = (d_1193_valueOrError5_).PropagateFailure()
            return res
        d_1192_wrapOutput_ = (d_1193_valueOrError5_).Extract()
        d_1194_symmetricSigningKeyList_: Wrappers.Option
        d_1194_symmetricSigningKeyList_ = (Wrappers.Option_Some(_dafny.Seq([((d_1192_wrapOutput_).symmetricSigningKey).value])) if ((d_1192_wrapOutput_).symmetricSigningKey).is_Some else Wrappers.Option_None())
        d_1195_valueOrError6_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1195_valueOrError6_ = Wrappers.default__.Need((default__.ValidCompressedPublicKeyLength(d_1176_operationCompressedSenderPublicKey_)) and (default__.ValidCompressedPublicKeyLength((self).compressedRecipientPublicKey)), default__.E(_dafny.Seq("Invalid compressed public key length.")))
        if (d_1195_valueOrError6_).IsFailure():
            res = (d_1195_valueOrError6_).PropagateFailure()
            return res
        d_1196_edk_: AwsCryptographyMaterialProvidersTypes.EncryptedDataKey
        d_1196_edk_ = AwsCryptographyMaterialProvidersTypes.EncryptedDataKey_EncryptedDataKey(Constants.default__.RAW__ECDH__PROVIDER__ID, default__.SerializeProviderInfo(d_1176_operationCompressedSenderPublicKey_, (self).compressedRecipientPublicKey), (d_1192_wrapOutput_).wrappedMaterial)
        if (d_1192_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_1197_result_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_1198_valueOrError7_: Wrappers.Result = None
            d_1198_valueOrError7_ = Materials.default__.EncryptionMaterialAddDataKey(d_1181_materials_, (d_1192_wrapOutput_).plaintextDataKey, _dafny.Seq([d_1196_edk_]), d_1194_symmetricSigningKeyList_)
            if (d_1198_valueOrError7_).IsFailure():
                res = (d_1198_valueOrError7_).PropagateFailure()
                return res
            d_1197_result_ = (d_1198_valueOrError7_).Extract()
            res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(d_1197_result_))
            return res
        elif (d_1192_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_1199_result_: AwsCryptographyMaterialProvidersTypes.EncryptionMaterials
            d_1200_valueOrError8_: Wrappers.Result = None
            d_1200_valueOrError8_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys(d_1181_materials_, _dafny.Seq([d_1196_edk_]), d_1194_symmetricSigningKeyList_)
            if (d_1200_valueOrError8_).IsFailure():
                res = (d_1200_valueOrError8_).PropagateFailure()
                return res
            d_1199_result_ = (d_1200_valueOrError8_).Extract()
            res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnEncryptOutput_OnEncryptOutput(d_1199_result_))
            return res
        return res

    def OnDecrypt_k(self, input):
        res: Wrappers.Result = None
        if ((self).keyAgreementScheme).is_EphemeralPrivateKeyToStaticPublicKey:
            res = Wrappers.Result_Failure(AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("EphemeralPrivateKeyToStaticPublicKey Key Agreement Scheme is forbidden on decrypt.")))
            return res
        d_1201_materials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_1201_materials_ = (input).materials
        d_1202_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_1202_suite_ = ((input).materials).algorithmSuite
        d_1203_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1203_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_1201_materials_), default__.E(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_1203_valueOrError0_).IsFailure():
            res = (d_1203_valueOrError0_).PropagateFailure()
            return res
        d_1204_operationCompressedSenderPublicKey_: Wrappers.Option
        d_1204_operationCompressedSenderPublicKey_ = (Wrappers.Option_None() if ((self).compressedSenderPublicKey) == (_dafny.Seq([])) else Wrappers.Option_Some((self).compressedSenderPublicKey))
        d_1205_filter_: OnDecryptEcdhDataKeyFilter
        nw48_ = OnDecryptEcdhDataKeyFilter()
        nw48_.ctor__((self).keyAgreementScheme, (self).compressedRecipientPublicKey, d_1204_operationCompressedSenderPublicKey_)
        d_1205_filter_ = nw48_
        d_1206_edksToAttempt_: _dafny.Seq
        d_1207_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out216_: Wrappers.Result
        out216_ = Actions.default__.FilterWithResult(d_1205_filter_, (input).encryptedDataKeys)
        d_1207_valueOrError1_ = out216_
        if (d_1207_valueOrError1_).IsFailure():
            res = (d_1207_valueOrError1_).PropagateFailure()
            return res
        d_1206_edksToAttempt_ = (d_1207_valueOrError1_).Extract()
        if (0) == (len(d_1206_edksToAttempt_)):
            d_1208_errorMessage_: _dafny.Seq
            d_1209_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            d_1209_valueOrError2_ = ErrorMessages.default__.IncorrectDataKeys((input).encryptedDataKeys, ((input).materials).algorithmSuite, _dafny.Seq(""))
            if (d_1209_valueOrError2_).IsFailure():
                res = (d_1209_valueOrError2_).PropagateFailure()
                return res
            d_1208_errorMessage_ = (d_1209_valueOrError2_).Extract()
            res = Wrappers.Result_Failure(default__.E(d_1208_errorMessage_))
            return res
        d_1210_decryptClosure_: Actions.ActionWithResult
        nw49_ = DecryptSingleEncryptedDataKey()
        nw49_.ctor__(d_1201_materials_, (self).cryptoPrimitives, (self).compressedSenderPublicKey, (self).compressedRecipientPublicKey, (self).keyAgreementScheme, (self).curveSpec)
        d_1210_decryptClosure_ = nw49_
        d_1211_outcome_: Wrappers.Result
        out217_: Wrappers.Result
        out217_ = Actions.default__.ReduceToSuccess(d_1210_decryptClosure_, d_1206_edksToAttempt_)
        d_1211_outcome_ = out217_
        d_1212_SealedDecryptionMaterials_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_1213_valueOrError3_: Wrappers.Result = None
        def lambda101_(d_1214_errors_):
            return AwsCryptographyMaterialProvidersTypes.Error_CollectionOfErrors(d_1214_errors_, _dafny.Seq("No Configured Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`."))

        d_1213_valueOrError3_ = (d_1211_outcome_).MapFailure(lambda101_)
        if (d_1213_valueOrError3_).IsFailure():
            res = (d_1213_valueOrError3_).PropagateFailure()
            return res
        d_1212_SealedDecryptionMaterials_ = (d_1213_valueOrError3_).Extract()
        res = Wrappers.Result_Success(AwsCryptographyMaterialProvidersTypes.OnDecryptOutput_OnDecryptOutput(d_1212_SealedDecryptionMaterials_))
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
        d_1215_providerInfo_: _dafny.Seq
        d_1215_providerInfo_ = (edk).keyProviderInfo
        d_1216_providerId_: _dafny.Seq
        d_1216_providerId_ = (edk).keyProviderId
        if ((d_1216_providerId_) != (Constants.default__.RAW__ECDH__PROVIDER__ID)) and ((d_1216_providerId_) != (Constants.default__.KMS__ECDH__PROVIDER__ID)):
            res = Wrappers.Result_Success(False)
            return res
        d_1217_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1217_valueOrError0_ = Wrappers.default__.Need(((len(d_1215_providerInfo_)) <= (Constants.default__.ECDH__PROVIDER__INFO__521__LEN)) and (default__.ValidProviderInfoLength(d_1215_providerInfo_)), default__.E(_dafny.Seq("EDK ProviderInfo longer than expected")))
        if (d_1217_valueOrError0_).IsFailure():
            res = (d_1217_valueOrError0_).PropagateFailure()
            return res
        d_1218_keyringVersion_: int
        d_1218_keyringVersion_ = (d_1215_providerInfo_)[0]
        d_1219_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1219_valueOrError1_ = Wrappers.default__.Need((_dafny.Seq([d_1218_keyringVersion_])) == (default__.RAW__ECDH__KEYRING__VERSION), default__.E(_dafny.Seq("Incorrect Keyring version found in provider info.")))
        if (d_1219_valueOrError1_).IsFailure():
            res = (d_1219_valueOrError1_).PropagateFailure()
            return res
        d_1220_recipientPublicKeyLength_: int
        d_1220_recipientPublicKeyLength_ = StandardLibrary_UInt.default__.SeqToUInt32(_dafny.Seq((d_1215_providerInfo_)[Constants.default__.ECDH__PROVIDER__INFO__RPL__INDEX:Constants.default__.ECDH__PROVIDER__INFO__RPK__INDEX:]))
        d_1221_recipientPublicKeyLengthIndex_: int
        d_1221_recipientPublicKeyLengthIndex_ = (Constants.default__.ECDH__PROVIDER__INFO__RPK__INDEX) + (d_1220_recipientPublicKeyLength_)
        d_1222_senderPublicKeyIndex_: int
        d_1222_senderPublicKeyIndex_ = (d_1221_recipientPublicKeyLengthIndex_) + (Constants.default__.ECDH__PROVIDER__INFO__PUBLIC__KEY__LEN)
        d_1223_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1223_valueOrError2_ = Wrappers.default__.Need(((d_1221_recipientPublicKeyLengthIndex_) + (4)) < (len(d_1215_providerInfo_)), default__.E(_dafny.Seq("Key Provider Info Serialization Error. Serialized length less than expected.")))
        if (d_1223_valueOrError2_).IsFailure():
            res = (d_1223_valueOrError2_).PropagateFailure()
            return res
        d_1224_providerInfoRecipientPublicKey_: _dafny.Seq
        d_1224_providerInfoRecipientPublicKey_ = _dafny.Seq((d_1215_providerInfo_)[Constants.default__.ECDH__PROVIDER__INFO__RPK__INDEX:d_1221_recipientPublicKeyLengthIndex_:])
        d_1225_providerInfoSenderPublicKey_: _dafny.Seq
        d_1225_providerInfoSenderPublicKey_ = _dafny.Seq((d_1215_providerInfo_)[d_1222_senderPublicKeyIndex_::])
        if ((self).keyAgreementScheme).is_PublicKeyDiscovery:
            res = Wrappers.Result_Success(((self).compressedRecipientPublicKey) == (d_1224_providerInfoRecipientPublicKey_))
            return res
        elif True:
            res = Wrappers.Result_Success(((((self).compressedSenderPublicKey) == (d_1225_providerInfoSenderPublicKey_)) and (((self).compressedRecipientPublicKey) == (d_1224_providerInfoRecipientPublicKey_))) or ((((self).compressedSenderPublicKey) == (d_1224_providerInfoRecipientPublicKey_)) and (((self).compressedRecipientPublicKey) == (d_1225_providerInfoSenderPublicKey_))))
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
        d_1226_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1226_valueOrError0_ = Wrappers.default__.Need(UTF8.default__.ValidUTF8Seq((edk).keyProviderId), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Received invalid EDK provider id for AWS KMS ECDH Keyring")))
        if (d_1226_valueOrError0_).IsFailure():
            res = (d_1226_valueOrError0_).PropagateFailure()
            return res
        d_1227_suite_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo
        d_1227_suite_ = ((self).materials).algorithmSuite
        d_1228_keyProviderId_: _dafny.Seq
        d_1228_keyProviderId_ = (edk).keyProviderId
        d_1229_providerInfo_: _dafny.Seq
        d_1229_providerInfo_ = (edk).keyProviderInfo
        d_1230_ciphertext_: _dafny.Seq
        d_1230_ciphertext_ = (edk).ciphertext
        d_1231_providerWrappedMaterial_: _dafny.Seq
        d_1232_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1232_valueOrError1_ = EdkWrapping.default__.GetProviderWrappedMaterial(d_1230_ciphertext_, d_1227_suite_)
        if (d_1232_valueOrError1_).IsFailure():
            res = (d_1232_valueOrError1_).PropagateFailure()
            return res
        d_1231_providerWrappedMaterial_ = (d_1232_valueOrError1_).Extract()
        d_1233_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1233_valueOrError2_ = Wrappers.default__.Need(((len(d_1229_providerInfo_)) <= (Constants.default__.ECDH__PROVIDER__INFO__521__LEN)) and (default__.ValidProviderInfoLength(d_1229_providerInfo_)), default__.E(_dafny.Seq("EDK ProviderInfo longer than expected")))
        if (d_1233_valueOrError2_).IsFailure():
            res = (d_1233_valueOrError2_).PropagateFailure()
            return res
        d_1234_keyringVersion_: int
        d_1234_keyringVersion_ = (d_1229_providerInfo_)[0]
        d_1235_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1235_valueOrError3_ = Wrappers.default__.Need((_dafny.Seq([d_1234_keyringVersion_])) == (default__.RAW__ECDH__KEYRING__VERSION), default__.E(_dafny.Seq("Incorrect Keyring version found in provider info.")))
        if (d_1235_valueOrError3_).IsFailure():
            res = (d_1235_valueOrError3_).PropagateFailure()
            return res
        d_1236_recipientPublicKeyLength_: int
        d_1236_recipientPublicKeyLength_ = StandardLibrary_UInt.default__.SeqToUInt32(_dafny.Seq((d_1229_providerInfo_)[Constants.default__.ECDH__PROVIDER__INFO__RPL__INDEX:Constants.default__.ECDH__PROVIDER__INFO__RPK__INDEX:]))
        d_1237_recipientPublicKeyLengthIndex_: int
        d_1237_recipientPublicKeyLengthIndex_ = (Constants.default__.ECDH__PROVIDER__INFO__RPK__INDEX) + (d_1236_recipientPublicKeyLength_)
        d_1238_senderPublicKeyIndex_: int
        d_1238_senderPublicKeyIndex_ = (d_1237_recipientPublicKeyLengthIndex_) + (Constants.default__.ECDH__PROVIDER__INFO__PUBLIC__KEY__LEN)
        d_1239_valueOrError4_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1239_valueOrError4_ = Wrappers.default__.Need(((d_1237_recipientPublicKeyLengthIndex_) + (4)) < (len(d_1229_providerInfo_)), default__.E(_dafny.Seq("Key Provider Info Serialization Error. Serialized length less than expected.")))
        if (d_1239_valueOrError4_).IsFailure():
            res = (d_1239_valueOrError4_).PropagateFailure()
            return res
        d_1240_providerInfoRecipientPublicKey_: _dafny.Seq
        d_1240_providerInfoRecipientPublicKey_ = _dafny.Seq((d_1229_providerInfo_)[Constants.default__.ECDH__PROVIDER__INFO__RPK__INDEX:d_1237_recipientPublicKeyLengthIndex_:])
        d_1241_providerInfoSenderPublicKey_: _dafny.Seq
        d_1241_providerInfoSenderPublicKey_ = _dafny.Seq((d_1229_providerInfo_)[d_1238_senderPublicKeyIndex_::])
        d_1242_senderPublicKey_: _dafny.Seq
        d_1243_valueOrError5_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out218_: Wrappers.Result
        out218_ = default__.DecompressPublicKey(d_1241_providerInfoSenderPublicKey_, (self).curveSpec, (self).cryptoPrimitives)
        d_1243_valueOrError5_ = out218_
        if (d_1243_valueOrError5_).IsFailure():
            res = (d_1243_valueOrError5_).PropagateFailure()
            return res
        d_1242_senderPublicKey_ = (d_1243_valueOrError5_).Extract()
        d_1244_recipientPublicKey_: _dafny.Seq
        d_1245_valueOrError6_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out219_: Wrappers.Result
        out219_ = default__.DecompressPublicKey(d_1240_providerInfoRecipientPublicKey_, (self).curveSpec, (self).cryptoPrimitives)
        d_1245_valueOrError6_ = out219_
        if (d_1245_valueOrError6_).IsFailure():
            res = (d_1245_valueOrError6_).PropagateFailure()
            return res
        d_1244_recipientPublicKey_ = (d_1245_valueOrError6_).Extract()
        d_1246___v0_: bool
        d_1247_valueOrError7_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        out220_: Wrappers.Result
        out220_ = default__.ValidatePublicKey((self).cryptoPrimitives, (self).curveSpec, d_1242_senderPublicKey_)
        d_1247_valueOrError7_ = out220_
        if (d_1247_valueOrError7_).IsFailure():
            res = (d_1247_valueOrError7_).PropagateFailure()
            return res
        d_1246___v0_ = (d_1247_valueOrError7_).Extract()
        d_1248___v1_: bool
        d_1249_valueOrError8_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        out221_: Wrappers.Result
        out221_ = default__.ValidatePublicKey((self).cryptoPrimitives, (self).curveSpec, d_1244_recipientPublicKey_)
        d_1249_valueOrError8_ = out221_
        if (d_1249_valueOrError8_).IsFailure():
            res = (d_1249_valueOrError8_).PropagateFailure()
            return res
        d_1248___v1_ = (d_1249_valueOrError8_).Extract()
        d_1250_sharedSecretPublicKey_: _dafny.Seq = _dafny.Seq({})
        d_1251_sharedSecretPrivateKey_: _dafny.Seq = _dafny.Seq({})
        if ((self).keyAgreementScheme).is_PublicKeyDiscovery:
            d_1250_sharedSecretPublicKey_ = d_1242_senderPublicKey_
            d_1251_sharedSecretPrivateKey_ = (((self).keyAgreementScheme).PublicKeyDiscovery).recipientStaticPrivateKey
        elif ((self).keyAgreementScheme).is_RawPrivateKeyToStaticPublicKey:
            d_1251_sharedSecretPrivateKey_ = (((self).keyAgreementScheme).RawPrivateKeyToStaticPublicKey).senderStaticPrivateKey
            if ((((self).keyAgreementScheme).RawPrivateKeyToStaticPublicKey).recipientPublicKey) == (d_1244_recipientPublicKey_):
                d_1250_sharedSecretPublicKey_ = d_1244_recipientPublicKey_
            elif True:
                d_1250_sharedSecretPublicKey_ = d_1242_senderPublicKey_
        elif ((self).keyAgreementScheme).is_EphemeralPrivateKeyToStaticPublicKey:
            res = Wrappers.Result_Failure(default__.E(_dafny.Seq("EphemeralPrivateKeyToStaticPublicKey Not allowed on decrypt")))
            return res
        elif True:
            raise Exception("unreachable alternative")
        d_1252___v2_: bool
        d_1253_valueOrError9_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        out222_: Wrappers.Result
        out222_ = default__.ValidatePublicKey((self).cryptoPrimitives, (self).curveSpec, d_1250_sharedSecretPublicKey_)
        d_1253_valueOrError9_ = out222_
        if (d_1253_valueOrError9_).IsFailure():
            res = (d_1253_valueOrError9_).PropagateFailure()
            return res
        d_1252___v2_ = (d_1253_valueOrError9_).Extract()
        d_1254_sharedSecret_: _dafny.Seq
        d_1255_valueOrError10_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out223_: Wrappers.Result
        out223_ = default__.LocalDeriveSharedSecret(AwsCryptographyPrimitivesTypes.ECCPrivateKey_ECCPrivateKey(d_1251_sharedSecretPrivateKey_), AwsCryptographyPrimitivesTypes.ECCPublicKey_ECCPublicKey(d_1250_sharedSecretPublicKey_), (self).curveSpec, (self).cryptoPrimitives)
        d_1255_valueOrError10_ = out223_
        if (d_1255_valueOrError10_).IsFailure():
            res = (d_1255_valueOrError10_).PropagateFailure()
            return res
        d_1254_sharedSecret_ = (d_1255_valueOrError10_).Extract()
        d_1256_ecdhUnwrap_: EcdhEdkWrapping.EcdhUnwrap
        nw50_ = EcdhEdkWrapping.EcdhUnwrap()
        nw50_.ctor__(d_1241_providerInfoSenderPublicKey_, d_1240_providerInfoRecipientPublicKey_, d_1254_sharedSecret_, default__.RAW__ECDH__KEYRING__VERSION, (self).curveSpec, (self).cryptoPrimitives)
        d_1256_ecdhUnwrap_ = nw50_
        d_1257_unwrapOutputRes_: Wrappers.Result
        out224_: Wrappers.Result
        out224_ = EdkWrapping.default__.UnwrapEdkMaterial((edk).ciphertext, (self).materials, d_1256_ecdhUnwrap_)
        d_1257_unwrapOutputRes_ = out224_
        d_1258_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_1259_valueOrError11_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.UnwrapEdkMaterialOutput.default(EcdhEdkWrapping.EcdhUnwrapInfo.default()))()
        d_1259_valueOrError11_ = d_1257_unwrapOutputRes_
        if (d_1259_valueOrError11_).IsFailure():
            res = (d_1259_valueOrError11_).PropagateFailure()
            return res
        d_1258_unwrapOutput_ = (d_1259_valueOrError11_).Extract()
        d_1260_result_: AwsCryptographyMaterialProvidersTypes.DecryptionMaterials
        d_1261_valueOrError12_: Wrappers.Result = None
        d_1261_valueOrError12_ = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_1258_unwrapOutput_).plaintextDataKey, (d_1258_unwrapOutput_).symmetricSigningKey)
        if (d_1261_valueOrError12_).IsFailure():
            res = (d_1261_valueOrError12_).PropagateFailure()
            return res
        d_1260_result_ = (d_1261_valueOrError12_).Extract()
        res = Wrappers.Result_Success(d_1260_result_)
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
