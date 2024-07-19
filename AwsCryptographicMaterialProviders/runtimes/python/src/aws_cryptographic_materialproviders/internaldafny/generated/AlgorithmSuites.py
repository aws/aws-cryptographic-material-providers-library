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

# Module: AlgorithmSuites

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def SupportedESDKEncrypt_q(e):
        return (((True) and ((((((e).AES__GCM).keyLength) == (32)) or ((((e).AES__GCM).keyLength) == (24))) or ((((e).AES__GCM).keyLength) == (16)))) and ((((e).AES__GCM).tagLength) == (16))) and ((((e).AES__GCM).ivLength) == (12))

    @staticmethod
    def SupportedDBEEncrypt_q(e):
        return (((True) and ((((e).AES__GCM).keyLength) == (32))) and ((((e).AES__GCM).tagLength) == (16))) and ((((e).AES__GCM).ivLength) == (12))

    @staticmethod
    def SupportedDBEEDKWrapping_q(p):
        return (((((((p).is_IntermediateKeyWrapping) and (True)) and ((((((p).IntermediateKeyWrapping).pdkEncryptAlgorithm).AES__GCM).keyLength) == (32))) and ((((((p).IntermediateKeyWrapping).pdkEncryptAlgorithm).AES__GCM).tagLength) == (16))) and ((((((p).IntermediateKeyWrapping).pdkEncryptAlgorithm).AES__GCM).ivLength) == (12))) and ((((p).IntermediateKeyWrapping).macKeyKdf).is_HKDF)) and ((((p).IntermediateKeyWrapping).keyEncryptionKeyKdf).is_HKDF)

    @staticmethod
    def KeyDerivationAlgorithm_q(kdf):
        return (not ((True) and ((kdf).is_HKDF)) or (((((kdf).HKDF).inputKeyLength) == (((kdf).HKDF).outputKeyLength)) and (not ((((kdf).HKDF).hmac) == (AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__512())) or ((((kdf).HKDF).inputKeyLength) == (32))))) and (not((kdf).is_None))

    @staticmethod
    def CommitmentDerivationAlgorithm_q(kdf):
        return (not ((True) and ((kdf).is_HKDF)) or (((((((kdf).HKDF).hmac).is_SHA__512) and ((((kdf).HKDF).saltLength) == (32))) and ((((kdf).HKDF).inputKeyLength) == (32))) and ((((kdf).HKDF).outputKeyLength) == (32)))) and (not((kdf).is_IDENTITY))

    @staticmethod
    def EdkWrappingAlgorithm_q(alg):
        return ((((((alg).is_IntermediateKeyWrapping) and ((((alg).IntermediateKeyWrapping).keyEncryptionKeyKdf).is_HKDF)) and ((((alg).IntermediateKeyWrapping).macKeyKdf).is_HKDF)) and (True)) and ((((((alg).IntermediateKeyWrapping).pdkEncryptAlgorithm).AES__GCM).keyLength) == (32))) or ((alg).is_DIRECT__KEY__WRAPPING)

    @staticmethod
    def AlgorithmSuiteInfo_q(a):
        return ((((((((default__.KeyDerivationAlgorithm_q((a).kdf)) and (default__.CommitmentDerivationAlgorithm_q((a).commitment))) and (default__.EdkWrappingAlgorithm_q((a).edkWrapping))) and (not (((a).kdf).is_HKDF) or ((True) and (((((a).kdf).HKDF).outputKeyLength) == ((((a).encrypt).AES__GCM).keyLength))))) and (not (((a).signature).is_ECDSA) or (((a).kdf).is_HKDF))) and (not (((a).commitment).is_HKDF) or ((((((a).commitment).HKDF).saltLength) == (32)) and (((a).commitment) == ((a).kdf))))) and (not (((a).edkWrapping).is_IntermediateKeyWrapping) or (((((a).kdf).is_HKDF) and (((((a).edkWrapping).IntermediateKeyWrapping).keyEncryptionKeyKdf) == ((a).kdf))) and (((((a).edkWrapping).IntermediateKeyWrapping).macKeyKdf) == ((a).kdf))))) and (not ((((a).kdf).is_HKDF) and (((a).commitment).is_None)) or (((((a).kdf).HKDF).saltLength) == (0)))) and (not (not(((a).symmetricSignature).is_None)) or ((True) and (((a).edkWrapping).is_IntermediateKeyWrapping)))

    @staticmethod
    def ESDKAlgorithmSuite_q(a):
        def lambda32_():
            source11_ = ((a).id).ESDK
            if True:
                if source11_.is_ALG__AES__128__GCM__IV12__TAG16__NO__KDF:
                    return ((((((((((a).binaryId) == (_dafny.Seq([0, 20]))) and (((a).messageVersion) == (1))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (16))) and (((a).kdf).is_IDENTITY)) and (((a).signature).is_None)) and (((a).commitment).is_None)) and (((a).symmetricSignature).is_None)) and (((a).edkWrapping).is_DIRECT__KEY__WRAPPING)
            if True:
                if source11_.is_ALG__AES__192__GCM__IV12__TAG16__NO__KDF:
                    return ((((((((((a).binaryId) == (_dafny.Seq([0, 70]))) and (((a).messageVersion) == (1))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (24))) and (((a).kdf).is_IDENTITY)) and (((a).signature).is_None)) and (((a).commitment).is_None)) and (((a).symmetricSignature).is_None)) and (((a).edkWrapping).is_DIRECT__KEY__WRAPPING)
            if True:
                if source11_.is_ALG__AES__256__GCM__IV12__TAG16__NO__KDF:
                    return ((((((((((a).binaryId) == (_dafny.Seq([0, 120]))) and (((a).messageVersion) == (1))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (32))) and (((a).kdf).is_IDENTITY)) and (((a).signature).is_None)) and (((a).commitment).is_None)) and (((a).symmetricSignature).is_None)) and (((a).edkWrapping).is_DIRECT__KEY__WRAPPING)
            if True:
                if source11_.is_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256:
                    return (((((((((((a).binaryId) == (_dafny.Seq([1, 20]))) and (((a).messageVersion) == (1))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (16))) and (((a).kdf).is_HKDF)) and (((((a).kdf).HKDF).hmac) == (AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__256()))) and (((a).signature).is_None)) and (((a).commitment).is_None)) and (((a).symmetricSignature).is_None)) and (((a).edkWrapping).is_DIRECT__KEY__WRAPPING)
            if True:
                if source11_.is_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256:
                    return (((((((((((a).binaryId) == (_dafny.Seq([1, 70]))) and (((a).messageVersion) == (1))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (24))) and (((a).kdf).is_HKDF)) and (((((a).kdf).HKDF).hmac) == (AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__256()))) and (((a).signature).is_None)) and (((a).commitment).is_None)) and (((a).symmetricSignature).is_None)) and (((a).edkWrapping).is_DIRECT__KEY__WRAPPING)
            if True:
                if source11_.is_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256:
                    return (((((((((((a).binaryId) == (_dafny.Seq([1, 120]))) and (((a).messageVersion) == (1))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (32))) and (((a).kdf).is_HKDF)) and (((((a).kdf).HKDF).hmac) == (AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__256()))) and (((a).signature).is_None)) and (((a).commitment).is_None)) and (((a).symmetricSignature).is_None)) and (((a).edkWrapping).is_DIRECT__KEY__WRAPPING)
            if True:
                if source11_.is_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256:
                    return ((((((((((((a).binaryId) == (_dafny.Seq([2, 20]))) and (((a).messageVersion) == (1))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (16))) and (((a).kdf).is_HKDF)) and (((((a).kdf).HKDF).hmac) == (AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__256()))) and (((a).signature).is_ECDSA)) and (((((a).signature).ECDSA).curve) == (AwsCryptographyPrimitivesTypes.ECDSASignatureAlgorithm_ECDSA__P256()))) and (((a).commitment).is_None)) and (((a).symmetricSignature).is_None)) and (((a).edkWrapping).is_DIRECT__KEY__WRAPPING)
            if True:
                if source11_.is_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384:
                    return ((((((((((((a).binaryId) == (_dafny.Seq([3, 70]))) and (((a).messageVersion) == (1))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (24))) and (((a).kdf).is_HKDF)) and (((((a).kdf).HKDF).hmac) == (AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__384()))) and (((a).signature).is_ECDSA)) and (((((a).signature).ECDSA).curve) == (AwsCryptographyPrimitivesTypes.ECDSASignatureAlgorithm_ECDSA__P384()))) and (((a).commitment).is_None)) and (((a).symmetricSignature).is_None)) and (((a).edkWrapping).is_DIRECT__KEY__WRAPPING)
            if True:
                if source11_.is_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384:
                    return ((((((((((((a).binaryId) == (_dafny.Seq([3, 120]))) and (((a).messageVersion) == (1))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (32))) and (((a).kdf).is_HKDF)) and (((((a).kdf).HKDF).hmac) == (AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__384()))) and (((a).signature).is_ECDSA)) and (((((a).signature).ECDSA).curve) == (AwsCryptographyPrimitivesTypes.ECDSASignatureAlgorithm_ECDSA__P384()))) and (((a).commitment).is_None)) and (((a).symmetricSignature).is_None)) and (((a).edkWrapping).is_DIRECT__KEY__WRAPPING)
            if True:
                if source11_.is_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY:
                    return (((((((((((a).binaryId) == (_dafny.Seq([4, 120]))) and (((a).messageVersion) == (2))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (32))) and (((a).kdf).is_HKDF)) and (((((a).kdf).HKDF).hmac) == (AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__512()))) and (((a).signature).is_None)) and (((a).commitment).is_HKDF)) and (((a).symmetricSignature).is_None)) and (((a).edkWrapping).is_DIRECT__KEY__WRAPPING)
            if True:
                return ((((((((((((a).binaryId) == (_dafny.Seq([5, 120]))) and (((a).messageVersion) == (2))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (32))) and (((a).kdf).is_HKDF)) and (((((a).kdf).HKDF).hmac) == (AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__512()))) and (((a).signature).is_ECDSA)) and (((((a).signature).ECDSA).curve) == (AwsCryptographyPrimitivesTypes.ECDSASignatureAlgorithm_ECDSA__P384()))) and (((a).commitment).is_HKDF)) and (((a).symmetricSignature).is_None)) and (((a).edkWrapping).is_DIRECT__KEY__WRAPPING)

        return ((default__.AlgorithmSuiteInfo_q(a)) and (default__.SupportedESDKEncrypt_q((a).encrypt))) and (lambda32_())

    @staticmethod
    def DBEAlgorithmSuite_q(a):
        def lambda33_():
            source12_ = ((a).id).DBE
            if True:
                if source12_.is_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384:
                    return ((((((((((((((a).binaryId) == (_dafny.Seq([103, 0]))) and (((a).messageVersion) == (1))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (32))) and (((a).kdf).is_HKDF)) and (((((a).kdf).HKDF).hmac) == (AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__512()))) and (((a).signature).is_None)) and (((a).commitment).is_HKDF)) and (((a).symmetricSignature).is_HMAC)) and ((((a).symmetricSignature).HMAC) == (AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__384()))) and (((a).edkWrapping).is_IntermediateKeyWrapping)) and (True)) and (((((((a).edkWrapping).IntermediateKeyWrapping).pdkEncryptAlgorithm).AES__GCM).keyLength) == (32))
            if True:
                return (((((((((((((((a).binaryId) == (_dafny.Seq([103, 1]))) and (((a).messageVersion) == (1))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (32))) and (((a).kdf).is_HKDF)) and (((((a).kdf).HKDF).hmac) == (AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__512()))) and (((a).signature).is_ECDSA)) and (((((a).signature).ECDSA).curve) == (AwsCryptographyPrimitivesTypes.ECDSASignatureAlgorithm_ECDSA__P384()))) and (((a).commitment).is_HKDF)) and (((a).symmetricSignature).is_HMAC)) and ((((a).symmetricSignature).HMAC) == (AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__384()))) and (((a).edkWrapping).is_IntermediateKeyWrapping)) and (True)) and (((((((a).edkWrapping).IntermediateKeyWrapping).pdkEncryptAlgorithm).AES__GCM).keyLength) == (32))

        return (((default__.AlgorithmSuiteInfo_q(a)) and (default__.SupportedDBEEncrypt_q((a).encrypt))) and (default__.SupportedDBEEDKWrapping_q((a).edkWrapping))) and (lambda33_())

    @staticmethod
    def AlgorithmSuite_q(a):
        source13_ = (a).id
        if True:
            if source13_.is_ESDK:
                return default__.ESDKAlgorithmSuite_q(a)
        if True:
            return default__.DBEAlgorithmSuite_q(a)

    @staticmethod
    def HKDF__SHA__256(keyLength):
        return AwsCryptographyMaterialProvidersTypes.DerivationAlgorithm_HKDF(AwsCryptographyMaterialProvidersTypes.HKDF_HKDF(AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__256(), 0, keyLength, keyLength))

    @staticmethod
    def HKDF__SHA__384(keyLength):
        return AwsCryptographyMaterialProvidersTypes.DerivationAlgorithm_HKDF(AwsCryptographyMaterialProvidersTypes.HKDF_HKDF(AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__384(), 0, keyLength, keyLength))

    @staticmethod
    def HKDF__SHA__512(keyLength):
        return AwsCryptographyMaterialProvidersTypes.DerivationAlgorithm_HKDF(AwsCryptographyMaterialProvidersTypes.HKDF_HKDF(AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__512(), 32, keyLength, keyLength))

    @staticmethod
    def GetSuite(id):
        source14_ = id
        if True:
            if source14_.is_ESDK:
                d_324_e_ = source14_.ESDK
                return default__.GetESDKSuite(d_324_e_)
        if True:
            d_325_e_ = source14_.DBE
            return default__.GetDBESuite(d_325_e_)

    @staticmethod
    def GetDBESuite(id):
        return (default__.SupportedDBEAlgorithmSuites)[id]

    @staticmethod
    def GetESDKSuite(id):
        return (default__.SupportedESDKAlgorithmSuites)[id]

    @staticmethod
    def GetEncryptKeyLength(a):
        source15_ = (a).encrypt
        if True:
            d_326_e_ = source15_.AES__GCM
            return (d_326_e_).keyLength

    @staticmethod
    def GetEncryptTagLength(a):
        source16_ = (a).encrypt
        if True:
            d_327_e_ = source16_.AES__GCM
            return (d_327_e_).tagLength

    @staticmethod
    def GetEncryptIvLength(a):
        source17_ = (a).encrypt
        if True:
            d_328_e_ = source17_.AES__GCM
            return (d_328_e_).ivLength

    @staticmethod
    def GetAlgorithmSuiteInfo(binaryId_q):
        d_329_valueOrError0_ = Wrappers.default__.Need((binaryId_q) in (default__.AlgorithmSuiteInfoByBinaryId), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid BinaryId")))
        if (d_329_valueOrError0_).IsFailure():
            return (d_329_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success((default__.AlgorithmSuiteInfoByBinaryId)[binaryId_q])

    @_dafny.classproperty
    def Bits128(instance):
        return 16
    @_dafny.classproperty
    def TagLen(instance):
        return 16
    @_dafny.classproperty
    def IvLen(instance):
        return 12
    @_dafny.classproperty
    def AES__128__GCM__IV12__TAG16(instance):
        return AwsCryptographyMaterialProvidersTypes.Encrypt_AES__GCM(AwsCryptographyPrimitivesTypes.AES__GCM_AES__GCM(default__.Bits128, default__.TagLen, default__.IvLen))
    @_dafny.classproperty
    def Bits192(instance):
        return 24
    @_dafny.classproperty
    def AES__192__GCM__IV12__TAG16(instance):
        return AwsCryptographyMaterialProvidersTypes.Encrypt_AES__GCM(AwsCryptographyPrimitivesTypes.AES__GCM_AES__GCM(default__.Bits192, default__.TagLen, default__.IvLen))
    @_dafny.classproperty
    def Bits256(instance):
        return 32
    @_dafny.classproperty
    def AES__256__GCM__IV12__TAG16(instance):
        return AwsCryptographyMaterialProvidersTypes.Encrypt_AES__GCM(AwsCryptographyPrimitivesTypes.AES__GCM_AES__GCM(default__.Bits256, default__.TagLen, default__.IvLen))
    @_dafny.classproperty
    def EDK__INTERMEDIATE__WRAPPING__AES__GCM__256__HKDF__SHA__512(instance):
        return AwsCryptographyMaterialProvidersTypes.EdkWrappingAlgorithm_IntermediateKeyWrapping(AwsCryptographyMaterialProvidersTypes.IntermediateKeyWrapping_IntermediateKeyWrapping(default__.HKDF__SHA__512(default__.Bits256), default__.HKDF__SHA__512(default__.Bits256), default__.AES__256__GCM__IV12__TAG16))
    @_dafny.classproperty
    def DBE__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384(instance):
        return AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo_AlgorithmSuiteInfo(AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_DBE(AwsCryptographyMaterialProvidersTypes.DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384()), _dafny.Seq([103, 0]), 1, default__.AES__256__GCM__IV12__TAG16, default__.HKDF__SHA__512(default__.Bits256), default__.HKDF__SHA__512(default__.Bits256), AwsCryptographyMaterialProvidersTypes.SignatureAlgorithm_None(AwsCryptographyMaterialProvidersTypes.None__None()), AwsCryptographyMaterialProvidersTypes.SymmetricSignatureAlgorithm_HMAC(AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__384()), default__.EDK__INTERMEDIATE__WRAPPING__AES__GCM__256__HKDF__SHA__512)
    @_dafny.classproperty
    def DBE__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384(instance):
        return AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo_AlgorithmSuiteInfo(AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_DBE(AwsCryptographyMaterialProvidersTypes.DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384()), _dafny.Seq([103, 1]), 1, default__.AES__256__GCM__IV12__TAG16, default__.HKDF__SHA__512(default__.Bits256), default__.HKDF__SHA__512(default__.Bits256), AwsCryptographyMaterialProvidersTypes.SignatureAlgorithm_ECDSA(AwsCryptographyMaterialProvidersTypes.ECDSA_ECDSA(AwsCryptographyPrimitivesTypes.ECDSASignatureAlgorithm_ECDSA__P384())), AwsCryptographyMaterialProvidersTypes.SymmetricSignatureAlgorithm_HMAC(AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__384()), default__.EDK__INTERMEDIATE__WRAPPING__AES__GCM__256__HKDF__SHA__512)
    @_dafny.classproperty
    def ESDK__ALG__AES__128__GCM__IV12__TAG16__NO__KDF(instance):
        return AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo_AlgorithmSuiteInfo(AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__NO__KDF()), _dafny.Seq([0, 20]), 1, default__.AES__128__GCM__IV12__TAG16, AwsCryptographyMaterialProvidersTypes.DerivationAlgorithm_IDENTITY(AwsCryptographyMaterialProvidersTypes.IDENTITY_IDENTITY()), AwsCryptographyMaterialProvidersTypes.DerivationAlgorithm_None(AwsCryptographyMaterialProvidersTypes.None__None()), AwsCryptographyMaterialProvidersTypes.SignatureAlgorithm_None(AwsCryptographyMaterialProvidersTypes.None__None()), AwsCryptographyMaterialProvidersTypes.SymmetricSignatureAlgorithm_None(AwsCryptographyMaterialProvidersTypes.None__None()), AwsCryptographyMaterialProvidersTypes.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(AwsCryptographyMaterialProvidersTypes.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__192__GCM__IV12__TAG16__NO__KDF(instance):
        return AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo_AlgorithmSuiteInfo(AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__NO__KDF()), _dafny.Seq([0, 70]), 1, default__.AES__192__GCM__IV12__TAG16, AwsCryptographyMaterialProvidersTypes.DerivationAlgorithm_IDENTITY(AwsCryptographyMaterialProvidersTypes.IDENTITY_IDENTITY()), AwsCryptographyMaterialProvidersTypes.DerivationAlgorithm_None(AwsCryptographyMaterialProvidersTypes.None__None()), AwsCryptographyMaterialProvidersTypes.SignatureAlgorithm_None(AwsCryptographyMaterialProvidersTypes.None__None()), AwsCryptographyMaterialProvidersTypes.SymmetricSignatureAlgorithm_None(AwsCryptographyMaterialProvidersTypes.None__None()), AwsCryptographyMaterialProvidersTypes.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(AwsCryptographyMaterialProvidersTypes.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__256__GCM__IV12__TAG16__NO__KDF(instance):
        return AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo_AlgorithmSuiteInfo(AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF()), _dafny.Seq([0, 120]), 1, default__.AES__256__GCM__IV12__TAG16, AwsCryptographyMaterialProvidersTypes.DerivationAlgorithm_IDENTITY(AwsCryptographyMaterialProvidersTypes.IDENTITY_IDENTITY()), AwsCryptographyMaterialProvidersTypes.DerivationAlgorithm_None(AwsCryptographyMaterialProvidersTypes.None__None()), AwsCryptographyMaterialProvidersTypes.SignatureAlgorithm_None(AwsCryptographyMaterialProvidersTypes.None__None()), AwsCryptographyMaterialProvidersTypes.SymmetricSignatureAlgorithm_None(AwsCryptographyMaterialProvidersTypes.None__None()), AwsCryptographyMaterialProvidersTypes.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(AwsCryptographyMaterialProvidersTypes.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256(instance):
        return AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo_AlgorithmSuiteInfo(AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256()), _dafny.Seq([1, 20]), 1, default__.AES__128__GCM__IV12__TAG16, default__.HKDF__SHA__256(default__.Bits128), AwsCryptographyMaterialProvidersTypes.DerivationAlgorithm_None(AwsCryptographyMaterialProvidersTypes.None__None()), AwsCryptographyMaterialProvidersTypes.SignatureAlgorithm_None(AwsCryptographyMaterialProvidersTypes.None__None()), AwsCryptographyMaterialProvidersTypes.SymmetricSignatureAlgorithm_None(AwsCryptographyMaterialProvidersTypes.None__None()), AwsCryptographyMaterialProvidersTypes.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(AwsCryptographyMaterialProvidersTypes.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256(instance):
        return AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo_AlgorithmSuiteInfo(AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256()), _dafny.Seq([1, 70]), 1, default__.AES__192__GCM__IV12__TAG16, default__.HKDF__SHA__256(default__.Bits192), AwsCryptographyMaterialProvidersTypes.DerivationAlgorithm_None(AwsCryptographyMaterialProvidersTypes.None__None()), AwsCryptographyMaterialProvidersTypes.SignatureAlgorithm_None(AwsCryptographyMaterialProvidersTypes.None__None()), AwsCryptographyMaterialProvidersTypes.SymmetricSignatureAlgorithm_None(AwsCryptographyMaterialProvidersTypes.None__None()), AwsCryptographyMaterialProvidersTypes.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(AwsCryptographyMaterialProvidersTypes.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256(instance):
        return AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo_AlgorithmSuiteInfo(AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256()), _dafny.Seq([1, 120]), 1, default__.AES__256__GCM__IV12__TAG16, default__.HKDF__SHA__256(default__.Bits256), AwsCryptographyMaterialProvidersTypes.DerivationAlgorithm_None(AwsCryptographyMaterialProvidersTypes.None__None()), AwsCryptographyMaterialProvidersTypes.SignatureAlgorithm_None(AwsCryptographyMaterialProvidersTypes.None__None()), AwsCryptographyMaterialProvidersTypes.SymmetricSignatureAlgorithm_None(AwsCryptographyMaterialProvidersTypes.None__None()), AwsCryptographyMaterialProvidersTypes.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(AwsCryptographyMaterialProvidersTypes.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256(instance):
        return AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo_AlgorithmSuiteInfo(AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256()), _dafny.Seq([2, 20]), 1, default__.AES__128__GCM__IV12__TAG16, default__.HKDF__SHA__256(default__.Bits128), AwsCryptographyMaterialProvidersTypes.DerivationAlgorithm_None(AwsCryptographyMaterialProvidersTypes.None__None()), AwsCryptographyMaterialProvidersTypes.SignatureAlgorithm_ECDSA(AwsCryptographyMaterialProvidersTypes.ECDSA_ECDSA(AwsCryptographyPrimitivesTypes.ECDSASignatureAlgorithm_ECDSA__P256())), AwsCryptographyMaterialProvidersTypes.SymmetricSignatureAlgorithm_None(AwsCryptographyMaterialProvidersTypes.None__None()), AwsCryptographyMaterialProvidersTypes.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(AwsCryptographyMaterialProvidersTypes.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384(instance):
        return AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo_AlgorithmSuiteInfo(AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384()), _dafny.Seq([3, 70]), 1, default__.AES__192__GCM__IV12__TAG16, default__.HKDF__SHA__384(default__.Bits192), AwsCryptographyMaterialProvidersTypes.DerivationAlgorithm_None(AwsCryptographyMaterialProvidersTypes.None__None()), AwsCryptographyMaterialProvidersTypes.SignatureAlgorithm_ECDSA(AwsCryptographyMaterialProvidersTypes.ECDSA_ECDSA(AwsCryptographyPrimitivesTypes.ECDSASignatureAlgorithm_ECDSA__P384())), AwsCryptographyMaterialProvidersTypes.SymmetricSignatureAlgorithm_None(AwsCryptographyMaterialProvidersTypes.None__None()), AwsCryptographyMaterialProvidersTypes.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(AwsCryptographyMaterialProvidersTypes.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384(instance):
        return AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo_AlgorithmSuiteInfo(AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384()), _dafny.Seq([3, 120]), 1, default__.AES__256__GCM__IV12__TAG16, default__.HKDF__SHA__384(default__.Bits256), AwsCryptographyMaterialProvidersTypes.DerivationAlgorithm_None(AwsCryptographyMaterialProvidersTypes.None__None()), AwsCryptographyMaterialProvidersTypes.SignatureAlgorithm_ECDSA(AwsCryptographyMaterialProvidersTypes.ECDSA_ECDSA(AwsCryptographyPrimitivesTypes.ECDSASignatureAlgorithm_ECDSA__P384())), AwsCryptographyMaterialProvidersTypes.SymmetricSignatureAlgorithm_None(AwsCryptographyMaterialProvidersTypes.None__None()), AwsCryptographyMaterialProvidersTypes.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(AwsCryptographyMaterialProvidersTypes.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY(instance):
        return AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo_AlgorithmSuiteInfo(AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY()), _dafny.Seq([4, 120]), 2, default__.AES__256__GCM__IV12__TAG16, default__.HKDF__SHA__512(default__.Bits256), default__.HKDF__SHA__512(default__.Bits256), AwsCryptographyMaterialProvidersTypes.SignatureAlgorithm_None(AwsCryptographyMaterialProvidersTypes.None__None()), AwsCryptographyMaterialProvidersTypes.SymmetricSignatureAlgorithm_None(AwsCryptographyMaterialProvidersTypes.None__None()), AwsCryptographyMaterialProvidersTypes.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(AwsCryptographyMaterialProvidersTypes.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384(instance):
        return AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo_AlgorithmSuiteInfo(AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteId_ESDK(AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384()), _dafny.Seq([5, 120]), 2, default__.AES__256__GCM__IV12__TAG16, default__.HKDF__SHA__512(default__.Bits256), default__.HKDF__SHA__512(default__.Bits256), AwsCryptographyMaterialProvidersTypes.SignatureAlgorithm_ECDSA(AwsCryptographyMaterialProvidersTypes.ECDSA_ECDSA(AwsCryptographyPrimitivesTypes.ECDSASignatureAlgorithm_ECDSA__P384())), AwsCryptographyMaterialProvidersTypes.SymmetricSignatureAlgorithm_None(AwsCryptographyMaterialProvidersTypes.None__None()), AwsCryptographyMaterialProvidersTypes.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(AwsCryptographyMaterialProvidersTypes.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def SupportedESDKAlgorithmSuites(instance):
        return _dafny.Map({AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__NO__KDF(): default__.ESDK__ALG__AES__128__GCM__IV12__TAG16__NO__KDF, AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__NO__KDF(): default__.ESDK__ALG__AES__192__GCM__IV12__TAG16__NO__KDF, AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF(): default__.ESDK__ALG__AES__256__GCM__IV12__TAG16__NO__KDF, AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256(): default__.ESDK__ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256, AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256(): default__.ESDK__ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256, AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256(): default__.ESDK__ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256, AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256(): default__.ESDK__ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256, AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384(): default__.ESDK__ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384, AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384(): default__.ESDK__ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384, AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY(): default__.ESDK__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY, AwsCryptographyMaterialProvidersTypes.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384(): default__.ESDK__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384})
    @_dafny.classproperty
    def SupportedDBEAlgorithmSuites(instance):
        return _dafny.Map({AwsCryptographyMaterialProvidersTypes.DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384(): default__.DBE__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384, AwsCryptographyMaterialProvidersTypes.DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384(): default__.DBE__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384})
    @_dafny.classproperty
    def AlgorithmSuiteInfoByBinaryId(instance):
        return _dafny.Map({_dafny.Seq([0, 20]): default__.ESDK__ALG__AES__128__GCM__IV12__TAG16__NO__KDF, _dafny.Seq([0, 70]): default__.ESDK__ALG__AES__192__GCM__IV12__TAG16__NO__KDF, _dafny.Seq([0, 120]): default__.ESDK__ALG__AES__256__GCM__IV12__TAG16__NO__KDF, _dafny.Seq([1, 20]): default__.ESDK__ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256, _dafny.Seq([1, 70]): default__.ESDK__ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256, _dafny.Seq([1, 120]): default__.ESDK__ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256, _dafny.Seq([2, 20]): default__.ESDK__ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256, _dafny.Seq([3, 70]): default__.ESDK__ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384, _dafny.Seq([3, 120]): default__.ESDK__ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384, _dafny.Seq([4, 120]): default__.ESDK__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY, _dafny.Seq([5, 120]): default__.ESDK__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384, _dafny.Seq([103, 0]): default__.DBE__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384, _dafny.Seq([103, 1]): default__.DBE__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384})

class AlgorithmSuite:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo.default()()
    def _Is(source__):
        d_330_a_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo = source__
        return default__.AlgorithmSuite_q(d_330_a_)
