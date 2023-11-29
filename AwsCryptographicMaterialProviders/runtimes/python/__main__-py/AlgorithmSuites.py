import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_mMergeSort
import Math
import Seq
import BoundedInts
import Unicode
import Functions
import Utf8EncodingForm
import Utf16EncodingForm
import UnicodeStrings
import FileIO
import GeneralInternals
import MulInternalsNonlinear
import MulInternals
import Mul
import ModInternalsNonlinear
import DivInternalsNonlinear
import ModInternals
import DivInternals
import DivMod
import Power
import Logarithm
import StandardLibrary_mUInt
import String
import StandardLibrary
import UUID
import UTF8
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import AwsArnParsing
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
import Structure
import KMSKeystoreOperations
import DDBKeystoreOperations
import CreateKeys
import CreateKeyStoreTable
import GetKeys
import AwsCryptographyKeyStoreOperations
import software_amazon_cryptography_keystore_internaldafny
import Fixtures
import TestCreateKeyStore
import ExternRandom
import Random
import AESEncryption
import ExternDigest
import Digest
import HMAC
import WrappedHMAC
import HKDF
import WrappedHKDF
import Signature
import KdfCtr
import RSAEncryption
import AwsCryptographyPrimitivesOperations
import TestConfig
import TestGetKeys
import CleanupItems
import TestCreateKeys
import TestVersionKey

assert "AlgorithmSuites" == __name__
AlgorithmSuites = sys.modules[__name__]

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
        return (not ((True) and ((kdf).is_HKDF)) or (((((kdf).HKDF).inputKeyLength) == (((kdf).HKDF).outputKeyLength)) and (not ((((kdf).HKDF).hmac) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__512())) or ((((kdf).HKDF).inputKeyLength) == (32))))) and (not((kdf).is_None))

    @staticmethod
    def CommitmentDerivationAlgorithm_q(kdf):
        return (not ((True) and ((kdf).is_HKDF)) or (((((((kdf).HKDF).hmac).is_SHA__512) and ((((kdf).HKDF).saltLength) == (32))) and ((((kdf).HKDF).inputKeyLength) == (32))) and ((((kdf).HKDF).outputKeyLength) == (32)))) and (not((kdf).is_IDENTITY))

    @staticmethod
    def EdkWrappingAlgorithm_q(alg):
        return ((((((alg).is_IntermediateKeyWrapping) and ((((alg).IntermediateKeyWrapping).keyEncryptionKeyKdf).is_HKDF)) and ((((alg).IntermediateKeyWrapping).macKeyKdf).is_HKDF)) and (True)) and ((((((alg).IntermediateKeyWrapping).pdkEncryptAlgorithm).AES__GCM).keyLength) == (32))) or ((alg).is_DIRECT__KEY__WRAPPING)

    @staticmethod
    def AlgorithmSuiteInfo_q(a):
        return ((((((((AlgorithmSuites.default__.KeyDerivationAlgorithm_q((a).kdf)) and (AlgorithmSuites.default__.CommitmentDerivationAlgorithm_q((a).commitment))) and (AlgorithmSuites.default__.EdkWrappingAlgorithm_q((a).edkWrapping))) and (not (((a).kdf).is_HKDF) or ((True) and (((((a).kdf).HKDF).outputKeyLength) == ((((a).encrypt).AES__GCM).keyLength))))) and (not (((a).signature).is_ECDSA) or (((a).kdf).is_HKDF))) and (not (((a).commitment).is_HKDF) or ((((((a).commitment).HKDF).saltLength) == (32)) and (((a).commitment) == ((a).kdf))))) and (not (((a).edkWrapping).is_IntermediateKeyWrapping) or (((((a).kdf).is_HKDF) and (((((a).edkWrapping).IntermediateKeyWrapping).keyEncryptionKeyKdf) == ((a).kdf))) and (((((a).edkWrapping).IntermediateKeyWrapping).macKeyKdf) == ((a).kdf))))) and (not ((((a).kdf).is_HKDF) and (((a).commitment).is_None)) or (((((a).kdf).HKDF).saltLength) == (0)))) and (not (not(((a).symmetricSignature).is_None)) or ((True) and (((a).edkWrapping).is_IntermediateKeyWrapping)))

    @staticmethod
    def ESDKAlgorithmSuite_q(a):
        def lambda30_(source14_):
            if source14_.is_ALG__AES__128__GCM__IV12__TAG16__NO__KDF:
                return ((((((((((a).binaryId) == (_dafny.Seq([0, 20]))) and (((a).messageVersion) == (1))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (16))) and (((a).kdf).is_IDENTITY)) and (((a).signature).is_None)) and (((a).commitment).is_None)) and (((a).symmetricSignature).is_None)) and (((a).edkWrapping).is_DIRECT__KEY__WRAPPING)
            elif source14_.is_ALG__AES__192__GCM__IV12__TAG16__NO__KDF:
                return ((((((((((a).binaryId) == (_dafny.Seq([0, 70]))) and (((a).messageVersion) == (1))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (24))) and (((a).kdf).is_IDENTITY)) and (((a).signature).is_None)) and (((a).commitment).is_None)) and (((a).symmetricSignature).is_None)) and (((a).edkWrapping).is_DIRECT__KEY__WRAPPING)
            elif source14_.is_ALG__AES__256__GCM__IV12__TAG16__NO__KDF:
                return ((((((((((a).binaryId) == (_dafny.Seq([0, 120]))) and (((a).messageVersion) == (1))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (32))) and (((a).kdf).is_IDENTITY)) and (((a).signature).is_None)) and (((a).commitment).is_None)) and (((a).symmetricSignature).is_None)) and (((a).edkWrapping).is_DIRECT__KEY__WRAPPING)
            elif source14_.is_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256:
                return (((((((((((a).binaryId) == (_dafny.Seq([1, 20]))) and (((a).messageVersion) == (1))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (16))) and (((a).kdf).is_HKDF)) and (((((a).kdf).HKDF).hmac) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__256()))) and (((a).signature).is_None)) and (((a).commitment).is_None)) and (((a).symmetricSignature).is_None)) and (((a).edkWrapping).is_DIRECT__KEY__WRAPPING)
            elif source14_.is_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256:
                return (((((((((((a).binaryId) == (_dafny.Seq([1, 70]))) and (((a).messageVersion) == (1))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (24))) and (((a).kdf).is_HKDF)) and (((((a).kdf).HKDF).hmac) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__256()))) and (((a).signature).is_None)) and (((a).commitment).is_None)) and (((a).symmetricSignature).is_None)) and (((a).edkWrapping).is_DIRECT__KEY__WRAPPING)
            elif source14_.is_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256:
                return (((((((((((a).binaryId) == (_dafny.Seq([1, 120]))) and (((a).messageVersion) == (1))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (32))) and (((a).kdf).is_HKDF)) and (((((a).kdf).HKDF).hmac) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__256()))) and (((a).signature).is_None)) and (((a).commitment).is_None)) and (((a).symmetricSignature).is_None)) and (((a).edkWrapping).is_DIRECT__KEY__WRAPPING)
            elif source14_.is_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256:
                return ((((((((((((a).binaryId) == (_dafny.Seq([2, 20]))) and (((a).messageVersion) == (1))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (16))) and (((a).kdf).is_HKDF)) and (((((a).kdf).HKDF).hmac) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__256()))) and (((a).signature).is_ECDSA)) and (((((a).signature).ECDSA).curve) == (software_amazon_cryptography_primitives_internaldafny_types.ECDSASignatureAlgorithm_ECDSA__P256()))) and (((a).commitment).is_None)) and (((a).symmetricSignature).is_None)) and (((a).edkWrapping).is_DIRECT__KEY__WRAPPING)
            elif source14_.is_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384:
                return ((((((((((((a).binaryId) == (_dafny.Seq([3, 70]))) and (((a).messageVersion) == (1))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (24))) and (((a).kdf).is_HKDF)) and (((((a).kdf).HKDF).hmac) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__384()))) and (((a).signature).is_ECDSA)) and (((((a).signature).ECDSA).curve) == (software_amazon_cryptography_primitives_internaldafny_types.ECDSASignatureAlgorithm_ECDSA__P384()))) and (((a).commitment).is_None)) and (((a).symmetricSignature).is_None)) and (((a).edkWrapping).is_DIRECT__KEY__WRAPPING)
            elif source14_.is_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384:
                return ((((((((((((a).binaryId) == (_dafny.Seq([3, 120]))) and (((a).messageVersion) == (1))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (32))) and (((a).kdf).is_HKDF)) and (((((a).kdf).HKDF).hmac) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__384()))) and (((a).signature).is_ECDSA)) and (((((a).signature).ECDSA).curve) == (software_amazon_cryptography_primitives_internaldafny_types.ECDSASignatureAlgorithm_ECDSA__P384()))) and (((a).commitment).is_None)) and (((a).symmetricSignature).is_None)) and (((a).edkWrapping).is_DIRECT__KEY__WRAPPING)
            elif source14_.is_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY:
                return (((((((((((a).binaryId) == (_dafny.Seq([4, 120]))) and (((a).messageVersion) == (2))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (32))) and (((a).kdf).is_HKDF)) and (((((a).kdf).HKDF).hmac) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__512()))) and (((a).signature).is_None)) and (((a).commitment).is_HKDF)) and (((a).symmetricSignature).is_None)) and (((a).edkWrapping).is_DIRECT__KEY__WRAPPING)
            elif True:
                return ((((((((((((a).binaryId) == (_dafny.Seq([5, 120]))) and (((a).messageVersion) == (2))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (32))) and (((a).kdf).is_HKDF)) and (((((a).kdf).HKDF).hmac) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__512()))) and (((a).signature).is_ECDSA)) and (((((a).signature).ECDSA).curve) == (software_amazon_cryptography_primitives_internaldafny_types.ECDSASignatureAlgorithm_ECDSA__P384()))) and (((a).commitment).is_HKDF)) and (((a).symmetricSignature).is_None)) and (((a).edkWrapping).is_DIRECT__KEY__WRAPPING)

        return ((AlgorithmSuites.default__.AlgorithmSuiteInfo_q(a)) and (AlgorithmSuites.default__.SupportedESDKEncrypt_q((a).encrypt))) and (lambda30_(((a).id).ESDK))

    @staticmethod
    def DBEAlgorithmSuite_q(a):
        def lambda31_(source15_):
            if source15_.is_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384:
                return ((((((((((((((a).binaryId) == (_dafny.Seq([103, 0]))) and (((a).messageVersion) == (1))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (32))) and (((a).kdf).is_HKDF)) and (((((a).kdf).HKDF).hmac) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__512()))) and (((a).signature).is_None)) and (((a).commitment).is_HKDF)) and (((a).symmetricSignature).is_HMAC)) and ((((a).symmetricSignature).HMAC) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__384()))) and (((a).edkWrapping).is_IntermediateKeyWrapping)) and (True)) and (((((((a).edkWrapping).IntermediateKeyWrapping).pdkEncryptAlgorithm).AES__GCM).keyLength) == (32))
            elif True:
                return (((((((((((((((a).binaryId) == (_dafny.Seq([103, 1]))) and (((a).messageVersion) == (1))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (32))) and (((a).kdf).is_HKDF)) and (((((a).kdf).HKDF).hmac) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__512()))) and (((a).signature).is_ECDSA)) and (((((a).signature).ECDSA).curve) == (software_amazon_cryptography_primitives_internaldafny_types.ECDSASignatureAlgorithm_ECDSA__P384()))) and (((a).commitment).is_HKDF)) and (((a).symmetricSignature).is_HMAC)) and ((((a).symmetricSignature).HMAC) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__384()))) and (((a).edkWrapping).is_IntermediateKeyWrapping)) and (True)) and (((((((a).edkWrapping).IntermediateKeyWrapping).pdkEncryptAlgorithm).AES__GCM).keyLength) == (32))

        return (((AlgorithmSuites.default__.AlgorithmSuiteInfo_q(a)) and (AlgorithmSuites.default__.SupportedDBEEncrypt_q((a).encrypt))) and (AlgorithmSuites.default__.SupportedDBEEDKWrapping_q((a).edkWrapping))) and (lambda31_(((a).id).DBE))

    @staticmethod
    def AlgorithmSuite_q(a):
        source16_ = (a).id
        if source16_.is_ESDK:
            d_590___mcc_h0_ = source16_.ESDK
            return AlgorithmSuites.default__.ESDKAlgorithmSuite_q(a)
        elif True:
            d_591___mcc_h1_ = source16_.DBE
            return AlgorithmSuites.default__.DBEAlgorithmSuite_q(a)

    @staticmethod
    def HKDF__SHA__256(keyLength):
        return software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_HKDF(software_amazon_cryptography_materialproviders_internaldafny_types.HKDF_HKDF(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__256(), 0, keyLength, keyLength))

    @staticmethod
    def HKDF__SHA__384(keyLength):
        return software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_HKDF(software_amazon_cryptography_materialproviders_internaldafny_types.HKDF_HKDF(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__384(), 0, keyLength, keyLength))

    @staticmethod
    def HKDF__SHA__512(keyLength):
        return software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_HKDF(software_amazon_cryptography_materialproviders_internaldafny_types.HKDF_HKDF(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__512(), 32, keyLength, keyLength))

    @staticmethod
    def GetSuite(id):
        source17_ = id
        if source17_.is_ESDK:
            d_592___mcc_h0_ = source17_.ESDK
            d_593_e_ = d_592___mcc_h0_
            return AlgorithmSuites.default__.GetESDKSuite(d_593_e_)
        elif True:
            d_594___mcc_h1_ = source17_.DBE
            d_595_e_ = d_594___mcc_h1_
            return AlgorithmSuites.default__.GetDBESuite(d_595_e_)

    @staticmethod
    def GetDBESuite(id):
        return ((AlgorithmSuites.default__).SupportedDBEAlgorithmSuites)[id]

    @staticmethod
    def GetESDKSuite(id):
        return ((AlgorithmSuites.default__).SupportedESDKAlgorithmSuites)[id]

    @staticmethod
    def GetEncryptKeyLength(a):
        source18_ = (a).encrypt
        if True:
            d_596___mcc_h0_ = source18_.AES__GCM
            d_597_e_ = d_596___mcc_h0_
            return (d_597_e_).keyLength

    @staticmethod
    def GetEncryptTagLength(a):
        source19_ = (a).encrypt
        if True:
            d_598___mcc_h0_ = source19_.AES__GCM
            d_599_e_ = d_598___mcc_h0_
            return (d_599_e_).tagLength

    @staticmethod
    def GetEncryptIvLength(a):
        source20_ = (a).encrypt
        if True:
            d_600___mcc_h0_ = source20_.AES__GCM
            d_601_e_ = d_600___mcc_h0_
            return (d_601_e_).ivLength

    @staticmethod
    def GetAlgorithmSuiteInfo(binaryId_q):
        d_602_valueOrError0_ = Wrappers.default__.Need((binaryId_q) in ((AlgorithmSuites.default__).AlgorithmSuiteInfoByBinaryId), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid BinaryId")))
        if (d_602_valueOrError0_).IsFailure():
            return (d_602_valueOrError0_).PropagateFailure()
        elif True:
            return Wrappers.Result_Success(((AlgorithmSuites.default__).AlgorithmSuiteInfoByBinaryId)[binaryId_q])

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
        return software_amazon_cryptography_materialproviders_internaldafny_types.Encrypt_AES__GCM(software_amazon_cryptography_primitives_internaldafny_types.AES__GCM_AES__GCM((AlgorithmSuites.default__).Bits128, (AlgorithmSuites.default__).TagLen, (AlgorithmSuites.default__).IvLen))
    @_dafny.classproperty
    def Bits192(instance):
        return 24
    @_dafny.classproperty
    def AES__192__GCM__IV12__TAG16(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.Encrypt_AES__GCM(software_amazon_cryptography_primitives_internaldafny_types.AES__GCM_AES__GCM((AlgorithmSuites.default__).Bits192, (AlgorithmSuites.default__).TagLen, (AlgorithmSuites.default__).IvLen))
    @_dafny.classproperty
    def Bits256(instance):
        return 32
    @_dafny.classproperty
    def AES__256__GCM__IV12__TAG16(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.Encrypt_AES__GCM(software_amazon_cryptography_primitives_internaldafny_types.AES__GCM_AES__GCM((AlgorithmSuites.default__).Bits256, (AlgorithmSuites.default__).TagLen, (AlgorithmSuites.default__).IvLen))
    @_dafny.classproperty
    def EDK__INTERMEDIATE__WRAPPING__AES__GCM__256__HKDF__SHA__512(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_IntermediateKeyWrapping(software_amazon_cryptography_materialproviders_internaldafny_types.IntermediateKeyWrapping_IntermediateKeyWrapping(AlgorithmSuites.default__.HKDF__SHA__512((AlgorithmSuites.default__).Bits256), AlgorithmSuites.default__.HKDF__SHA__512((AlgorithmSuites.default__).Bits256), (AlgorithmSuites.default__).AES__256__GCM__IV12__TAG16))
    @_dafny.classproperty
    def DBE__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_DBE(software_amazon_cryptography_materialproviders_internaldafny_types.DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384()), _dafny.Seq([103, 0]), 1, (AlgorithmSuites.default__).AES__256__GCM__IV12__TAG16, AlgorithmSuites.default__.HKDF__SHA__512((AlgorithmSuites.default__).Bits256), AlgorithmSuites.default__.HKDF__SHA__512((AlgorithmSuites.default__).Bits256), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_HMAC(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__384()), (AlgorithmSuites.default__).EDK__INTERMEDIATE__WRAPPING__AES__GCM__256__HKDF__SHA__512)
    @_dafny.classproperty
    def DBE__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_DBE(software_amazon_cryptography_materialproviders_internaldafny_types.DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384()), _dafny.Seq([103, 1]), 1, (AlgorithmSuites.default__).AES__256__GCM__IV12__TAG16, AlgorithmSuites.default__.HKDF__SHA__512((AlgorithmSuites.default__).Bits256), AlgorithmSuites.default__.HKDF__SHA__512((AlgorithmSuites.default__).Bits256), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_ECDSA(software_amazon_cryptography_materialproviders_internaldafny_types.ECDSA_ECDSA(software_amazon_cryptography_primitives_internaldafny_types.ECDSASignatureAlgorithm_ECDSA__P384())), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_HMAC(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__384()), (AlgorithmSuites.default__).EDK__INTERMEDIATE__WRAPPING__AES__GCM__256__HKDF__SHA__512)
    @_dafny.classproperty
    def ESDK__ALG__AES__128__GCM__IV12__TAG16__NO__KDF(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__NO__KDF()), _dafny.Seq([0, 20]), 1, (AlgorithmSuites.default__).AES__128__GCM__IV12__TAG16, software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_IDENTITY(software_amazon_cryptography_materialproviders_internaldafny_types.IDENTITY_IDENTITY()), software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(software_amazon_cryptography_materialproviders_internaldafny_types.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__192__GCM__IV12__TAG16__NO__KDF(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__NO__KDF()), _dafny.Seq([0, 70]), 1, (AlgorithmSuites.default__).AES__192__GCM__IV12__TAG16, software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_IDENTITY(software_amazon_cryptography_materialproviders_internaldafny_types.IDENTITY_IDENTITY()), software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(software_amazon_cryptography_materialproviders_internaldafny_types.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__256__GCM__IV12__TAG16__NO__KDF(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF()), _dafny.Seq([0, 120]), 1, (AlgorithmSuites.default__).AES__256__GCM__IV12__TAG16, software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_IDENTITY(software_amazon_cryptography_materialproviders_internaldafny_types.IDENTITY_IDENTITY()), software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(software_amazon_cryptography_materialproviders_internaldafny_types.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256()), _dafny.Seq([1, 20]), 1, (AlgorithmSuites.default__).AES__128__GCM__IV12__TAG16, AlgorithmSuites.default__.HKDF__SHA__256((AlgorithmSuites.default__).Bits128), software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(software_amazon_cryptography_materialproviders_internaldafny_types.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256()), _dafny.Seq([1, 70]), 1, (AlgorithmSuites.default__).AES__192__GCM__IV12__TAG16, AlgorithmSuites.default__.HKDF__SHA__256((AlgorithmSuites.default__).Bits192), software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(software_amazon_cryptography_materialproviders_internaldafny_types.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256()), _dafny.Seq([1, 120]), 1, (AlgorithmSuites.default__).AES__256__GCM__IV12__TAG16, AlgorithmSuites.default__.HKDF__SHA__256((AlgorithmSuites.default__).Bits256), software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(software_amazon_cryptography_materialproviders_internaldafny_types.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256()), _dafny.Seq([2, 20]), 1, (AlgorithmSuites.default__).AES__128__GCM__IV12__TAG16, AlgorithmSuites.default__.HKDF__SHA__256((AlgorithmSuites.default__).Bits128), software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_ECDSA(software_amazon_cryptography_materialproviders_internaldafny_types.ECDSA_ECDSA(software_amazon_cryptography_primitives_internaldafny_types.ECDSASignatureAlgorithm_ECDSA__P256())), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(software_amazon_cryptography_materialproviders_internaldafny_types.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384()), _dafny.Seq([3, 70]), 1, (AlgorithmSuites.default__).AES__192__GCM__IV12__TAG16, AlgorithmSuites.default__.HKDF__SHA__384((AlgorithmSuites.default__).Bits192), software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_ECDSA(software_amazon_cryptography_materialproviders_internaldafny_types.ECDSA_ECDSA(software_amazon_cryptography_primitives_internaldafny_types.ECDSASignatureAlgorithm_ECDSA__P384())), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(software_amazon_cryptography_materialproviders_internaldafny_types.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384()), _dafny.Seq([3, 120]), 1, (AlgorithmSuites.default__).AES__256__GCM__IV12__TAG16, AlgorithmSuites.default__.HKDF__SHA__384((AlgorithmSuites.default__).Bits256), software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_ECDSA(software_amazon_cryptography_materialproviders_internaldafny_types.ECDSA_ECDSA(software_amazon_cryptography_primitives_internaldafny_types.ECDSASignatureAlgorithm_ECDSA__P384())), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(software_amazon_cryptography_materialproviders_internaldafny_types.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY()), _dafny.Seq([4, 120]), 2, (AlgorithmSuites.default__).AES__256__GCM__IV12__TAG16, AlgorithmSuites.default__.HKDF__SHA__512((AlgorithmSuites.default__).Bits256), AlgorithmSuites.default__.HKDF__SHA__512((AlgorithmSuites.default__).Bits256), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(software_amazon_cryptography_materialproviders_internaldafny_types.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384()), _dafny.Seq([5, 120]), 2, (AlgorithmSuites.default__).AES__256__GCM__IV12__TAG16, AlgorithmSuites.default__.HKDF__SHA__512((AlgorithmSuites.default__).Bits256), AlgorithmSuites.default__.HKDF__SHA__512((AlgorithmSuites.default__).Bits256), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_ECDSA(software_amazon_cryptography_materialproviders_internaldafny_types.ECDSA_ECDSA(software_amazon_cryptography_primitives_internaldafny_types.ECDSASignatureAlgorithm_ECDSA__P384())), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(software_amazon_cryptography_materialproviders_internaldafny_types.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def SupportedESDKAlgorithmSuites(instance):
        return _dafny.Map({software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__NO__KDF(): (AlgorithmSuites.default__).ESDK__ALG__AES__128__GCM__IV12__TAG16__NO__KDF, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__NO__KDF(): (AlgorithmSuites.default__).ESDK__ALG__AES__192__GCM__IV12__TAG16__NO__KDF, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF(): (AlgorithmSuites.default__).ESDK__ALG__AES__256__GCM__IV12__TAG16__NO__KDF, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256(): (AlgorithmSuites.default__).ESDK__ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256(): (AlgorithmSuites.default__).ESDK__ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256(): (AlgorithmSuites.default__).ESDK__ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256(): (AlgorithmSuites.default__).ESDK__ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384(): (AlgorithmSuites.default__).ESDK__ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384(): (AlgorithmSuites.default__).ESDK__ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY(): (AlgorithmSuites.default__).ESDK__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384(): (AlgorithmSuites.default__).ESDK__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384})
    @_dafny.classproperty
    def SupportedDBEAlgorithmSuites(instance):
        return _dafny.Map({software_amazon_cryptography_materialproviders_internaldafny_types.DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384(): (AlgorithmSuites.default__).DBE__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384, software_amazon_cryptography_materialproviders_internaldafny_types.DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384(): (AlgorithmSuites.default__).DBE__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384})
    @_dafny.classproperty
    def AlgorithmSuiteInfoByBinaryId(instance):
        return _dafny.Map({_dafny.Seq([0, 20]): (AlgorithmSuites.default__).ESDK__ALG__AES__128__GCM__IV12__TAG16__NO__KDF, _dafny.Seq([0, 70]): (AlgorithmSuites.default__).ESDK__ALG__AES__192__GCM__IV12__TAG16__NO__KDF, _dafny.Seq([0, 120]): (AlgorithmSuites.default__).ESDK__ALG__AES__256__GCM__IV12__TAG16__NO__KDF, _dafny.Seq([1, 20]): (AlgorithmSuites.default__).ESDK__ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256, _dafny.Seq([1, 70]): (AlgorithmSuites.default__).ESDK__ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256, _dafny.Seq([1, 120]): (AlgorithmSuites.default__).ESDK__ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256, _dafny.Seq([2, 20]): (AlgorithmSuites.default__).ESDK__ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256, _dafny.Seq([3, 70]): (AlgorithmSuites.default__).ESDK__ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384, _dafny.Seq([3, 120]): (AlgorithmSuites.default__).ESDK__ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384, _dafny.Seq([4, 120]): (AlgorithmSuites.default__).ESDK__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY, _dafny.Seq([5, 120]): (AlgorithmSuites.default__).ESDK__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384, _dafny.Seq([103, 0]): (AlgorithmSuites.default__).DBE__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384, _dafny.Seq([103, 1]): (AlgorithmSuites.default__).DBE__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384})

class AlgorithmSuite:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo.default()()
