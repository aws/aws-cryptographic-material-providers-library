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
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types

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
        return (not ((True) and ((kdf).is_HKDF)) or (((((kdf).HKDF).inputKeyLength) == (((kdf).HKDF).outputKeyLength)) and (not ((((kdf).HKDF).hmac) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__512())) or ((((kdf).HKDF).inputKeyLength) == (32))))) and (not((kdf).is_None))

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
        def lambda0_(source0_):
            if source0_.is_ALG__AES__128__GCM__IV12__TAG16__NO__KDF:
                return ((((((((((a).binaryId) == (_dafny.Seq([0, 20]))) and (((a).messageVersion) == (1))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (16))) and (((a).kdf).is_IDENTITY)) and (((a).signature).is_None)) and (((a).commitment).is_None)) and (((a).symmetricSignature).is_None)) and (((a).edkWrapping).is_DIRECT__KEY__WRAPPING)
            elif source0_.is_ALG__AES__192__GCM__IV12__TAG16__NO__KDF:
                return ((((((((((a).binaryId) == (_dafny.Seq([0, 70]))) and (((a).messageVersion) == (1))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (24))) and (((a).kdf).is_IDENTITY)) and (((a).signature).is_None)) and (((a).commitment).is_None)) and (((a).symmetricSignature).is_None)) and (((a).edkWrapping).is_DIRECT__KEY__WRAPPING)
            elif source0_.is_ALG__AES__256__GCM__IV12__TAG16__NO__KDF:
                return ((((((((((a).binaryId) == (_dafny.Seq([0, 120]))) and (((a).messageVersion) == (1))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (32))) and (((a).kdf).is_IDENTITY)) and (((a).signature).is_None)) and (((a).commitment).is_None)) and (((a).symmetricSignature).is_None)) and (((a).edkWrapping).is_DIRECT__KEY__WRAPPING)
            elif source0_.is_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256:
                return (((((((((((a).binaryId) == (_dafny.Seq([1, 20]))) and (((a).messageVersion) == (1))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (16))) and (((a).kdf).is_HKDF)) and (((((a).kdf).HKDF).hmac) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__256()))) and (((a).signature).is_None)) and (((a).commitment).is_None)) and (((a).symmetricSignature).is_None)) and (((a).edkWrapping).is_DIRECT__KEY__WRAPPING)
            elif source0_.is_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256:
                return (((((((((((a).binaryId) == (_dafny.Seq([1, 70]))) and (((a).messageVersion) == (1))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (24))) and (((a).kdf).is_HKDF)) and (((((a).kdf).HKDF).hmac) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__256()))) and (((a).signature).is_None)) and (((a).commitment).is_None)) and (((a).symmetricSignature).is_None)) and (((a).edkWrapping).is_DIRECT__KEY__WRAPPING)
            elif source0_.is_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256:
                return (((((((((((a).binaryId) == (_dafny.Seq([1, 120]))) and (((a).messageVersion) == (1))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (32))) and (((a).kdf).is_HKDF)) and (((((a).kdf).HKDF).hmac) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__256()))) and (((a).signature).is_None)) and (((a).commitment).is_None)) and (((a).symmetricSignature).is_None)) and (((a).edkWrapping).is_DIRECT__KEY__WRAPPING)
            elif source0_.is_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256:
                return ((((((((((((a).binaryId) == (_dafny.Seq([2, 20]))) and (((a).messageVersion) == (1))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (16))) and (((a).kdf).is_HKDF)) and (((((a).kdf).HKDF).hmac) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__256()))) and (((a).signature).is_ECDSA)) and (((((a).signature).ECDSA).curve) == (software_amazon_cryptography_primitives_internaldafny_types.ECDSASignatureAlgorithm_ECDSA__P256()))) and (((a).commitment).is_None)) and (((a).symmetricSignature).is_None)) and (((a).edkWrapping).is_DIRECT__KEY__WRAPPING)
            elif source0_.is_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384:
                return ((((((((((((a).binaryId) == (_dafny.Seq([3, 70]))) and (((a).messageVersion) == (1))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (24))) and (((a).kdf).is_HKDF)) and (((((a).kdf).HKDF).hmac) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__384()))) and (((a).signature).is_ECDSA)) and (((((a).signature).ECDSA).curve) == (software_amazon_cryptography_primitives_internaldafny_types.ECDSASignatureAlgorithm_ECDSA__P384()))) and (((a).commitment).is_None)) and (((a).symmetricSignature).is_None)) and (((a).edkWrapping).is_DIRECT__KEY__WRAPPING)
            elif source0_.is_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384:
                return ((((((((((((a).binaryId) == (_dafny.Seq([3, 120]))) and (((a).messageVersion) == (1))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (32))) and (((a).kdf).is_HKDF)) and (((((a).kdf).HKDF).hmac) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__384()))) and (((a).signature).is_ECDSA)) and (((((a).signature).ECDSA).curve) == (software_amazon_cryptography_primitives_internaldafny_types.ECDSASignatureAlgorithm_ECDSA__P384()))) and (((a).commitment).is_None)) and (((a).symmetricSignature).is_None)) and (((a).edkWrapping).is_DIRECT__KEY__WRAPPING)
            elif source0_.is_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY:
                return (((((((((((a).binaryId) == (_dafny.Seq([4, 120]))) and (((a).messageVersion) == (2))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (32))) and (((a).kdf).is_HKDF)) and (((((a).kdf).HKDF).hmac) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__512()))) and (((a).signature).is_None)) and (((a).commitment).is_HKDF)) and (((a).symmetricSignature).is_None)) and (((a).edkWrapping).is_DIRECT__KEY__WRAPPING)
            elif True:
                return ((((((((((((a).binaryId) == (_dafny.Seq([5, 120]))) and (((a).messageVersion) == (2))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (32))) and (((a).kdf).is_HKDF)) and (((((a).kdf).HKDF).hmac) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__512()))) and (((a).signature).is_ECDSA)) and (((((a).signature).ECDSA).curve) == (software_amazon_cryptography_primitives_internaldafny_types.ECDSASignatureAlgorithm_ECDSA__P384()))) and (((a).commitment).is_HKDF)) and (((a).symmetricSignature).is_None)) and (((a).edkWrapping).is_DIRECT__KEY__WRAPPING)

        return ((default__.AlgorithmSuiteInfo_q(a)) and (default__.SupportedESDKEncrypt_q((a).encrypt))) and (lambda0_(((a).id).ESDK))

    @staticmethod
    def DBEAlgorithmSuite_q(a):
        def lambda1_(source1_):
            if source1_.is_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384:
                return ((((((((((((((a).binaryId) == (_dafny.Seq([103, 0]))) and (((a).messageVersion) == (1))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (32))) and (((a).kdf).is_HKDF)) and (((((a).kdf).HKDF).hmac) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__512()))) and (((a).signature).is_None)) and (((a).commitment).is_HKDF)) and (((a).symmetricSignature).is_HMAC)) and ((((a).symmetricSignature).HMAC) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__384()))) and (((a).edkWrapping).is_IntermediateKeyWrapping)) and (True)) and (((((((a).edkWrapping).IntermediateKeyWrapping).pdkEncryptAlgorithm).AES__GCM).keyLength) == (32))
            elif True:
                return (((((((((((((((a).binaryId) == (_dafny.Seq([103, 1]))) and (((a).messageVersion) == (1))) and (True)) and (((((a).encrypt).AES__GCM).keyLength) == (32))) and (((a).kdf).is_HKDF)) and (((((a).kdf).HKDF).hmac) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__512()))) and (((a).signature).is_ECDSA)) and (((((a).signature).ECDSA).curve) == (software_amazon_cryptography_primitives_internaldafny_types.ECDSASignatureAlgorithm_ECDSA__P384()))) and (((a).commitment).is_HKDF)) and (((a).symmetricSignature).is_HMAC)) and ((((a).symmetricSignature).HMAC) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__384()))) and (((a).edkWrapping).is_IntermediateKeyWrapping)) and (True)) and (((((((a).edkWrapping).IntermediateKeyWrapping).pdkEncryptAlgorithm).AES__GCM).keyLength) == (32))

        return (((default__.AlgorithmSuiteInfo_q(a)) and (default__.SupportedDBEEncrypt_q((a).encrypt))) and (default__.SupportedDBEEDKWrapping_q((a).edkWrapping))) and (lambda1_(((a).id).DBE))

    @staticmethod
    def AlgorithmSuite_q(a):
        source2_ = (a).id
        if source2_.is_ESDK:
            d_0___mcc_h0_ = source2_.ESDK
            return default__.ESDKAlgorithmSuite_q(a)
        elif True:
            d_1___mcc_h1_ = source2_.DBE
            return default__.DBEAlgorithmSuite_q(a)

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
        source3_ = id
        if source3_.is_ESDK:
            d_2___mcc_h0_ = source3_.ESDK
            d_3_e_ = d_2___mcc_h0_
            return default__.GetESDKSuite(d_3_e_)
        elif True:
            d_4___mcc_h1_ = source3_.DBE
            d_5_e_ = d_4___mcc_h1_
            return default__.GetDBESuite(d_5_e_)

    @staticmethod
    def GetDBESuite(id):
        return (default__.SupportedDBEAlgorithmSuites)[id]

    @staticmethod
    def GetESDKSuite(id):
        return (default__.SupportedESDKAlgorithmSuites)[id]

    @staticmethod
    def GetEncryptKeyLength(a):
        source4_ = (a).encrypt
        d_6___mcc_h0_ = source4_.AES__GCM
        d_7_e_ = d_6___mcc_h0_
        return (d_7_e_).keyLength

    @staticmethod
    def GetEncryptTagLength(a):
        source5_ = (a).encrypt
        d_8___mcc_h0_ = source5_.AES__GCM
        d_9_e_ = d_8___mcc_h0_
        return (d_9_e_).tagLength

    @staticmethod
    def GetEncryptIvLength(a):
        source6_ = (a).encrypt
        d_10___mcc_h0_ = source6_.AES__GCM
        d_11_e_ = d_10___mcc_h0_
        return (d_11_e_).ivLength

    @staticmethod
    def GetAlgorithmSuiteInfo(binaryId_q):
        d_12_valueOrError0_ = Wrappers.default__.Need((binaryId_q) in (default__.AlgorithmSuiteInfoByBinaryId), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid BinaryId")))
        if (d_12_valueOrError0_).IsFailure():
            return (d_12_valueOrError0_).PropagateFailure()
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
        return software_amazon_cryptography_materialproviders_internaldafny_types.Encrypt_AES__GCM(software_amazon_cryptography_primitives_internaldafny_types.AES__GCM_AES__GCM(default__.Bits128, default__.TagLen, default__.IvLen))
    @_dafny.classproperty
    def Bits192(instance):
        return 24
    @_dafny.classproperty
    def AES__192__GCM__IV12__TAG16(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.Encrypt_AES__GCM(software_amazon_cryptography_primitives_internaldafny_types.AES__GCM_AES__GCM(default__.Bits192, default__.TagLen, default__.IvLen))
    @_dafny.classproperty
    def Bits256(instance):
        return 32
    @_dafny.classproperty
    def AES__256__GCM__IV12__TAG16(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.Encrypt_AES__GCM(software_amazon_cryptography_primitives_internaldafny_types.AES__GCM_AES__GCM(default__.Bits256, default__.TagLen, default__.IvLen))
    @_dafny.classproperty
    def EDK__INTERMEDIATE__WRAPPING__AES__GCM__256__HKDF__SHA__512(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_IntermediateKeyWrapping(software_amazon_cryptography_materialproviders_internaldafny_types.IntermediateKeyWrapping_IntermediateKeyWrapping(default__.HKDF__SHA__512(default__.Bits256), default__.HKDF__SHA__512(default__.Bits256), default__.AES__256__GCM__IV12__TAG16))
    @_dafny.classproperty
    def DBE__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_DBE(software_amazon_cryptography_materialproviders_internaldafny_types.DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384()), _dafny.Seq([103, 0]), 1, default__.AES__256__GCM__IV12__TAG16, default__.HKDF__SHA__512(default__.Bits256), default__.HKDF__SHA__512(default__.Bits256), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_HMAC(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__384()), default__.EDK__INTERMEDIATE__WRAPPING__AES__GCM__256__HKDF__SHA__512)
    @_dafny.classproperty
    def DBE__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_DBE(software_amazon_cryptography_materialproviders_internaldafny_types.DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384()), _dafny.Seq([103, 1]), 1, default__.AES__256__GCM__IV12__TAG16, default__.HKDF__SHA__512(default__.Bits256), default__.HKDF__SHA__512(default__.Bits256), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_ECDSA(software_amazon_cryptography_materialproviders_internaldafny_types.ECDSA_ECDSA(software_amazon_cryptography_primitives_internaldafny_types.ECDSASignatureAlgorithm_ECDSA__P384())), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_HMAC(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__384()), default__.EDK__INTERMEDIATE__WRAPPING__AES__GCM__256__HKDF__SHA__512)
    @_dafny.classproperty
    def ESDK__ALG__AES__128__GCM__IV12__TAG16__NO__KDF(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__NO__KDF()), _dafny.Seq([0, 20]), 1, default__.AES__128__GCM__IV12__TAG16, software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_IDENTITY(software_amazon_cryptography_materialproviders_internaldafny_types.IDENTITY_IDENTITY()), software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(software_amazon_cryptography_materialproviders_internaldafny_types.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__192__GCM__IV12__TAG16__NO__KDF(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__NO__KDF()), _dafny.Seq([0, 70]), 1, default__.AES__192__GCM__IV12__TAG16, software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_IDENTITY(software_amazon_cryptography_materialproviders_internaldafny_types.IDENTITY_IDENTITY()), software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(software_amazon_cryptography_materialproviders_internaldafny_types.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__256__GCM__IV12__TAG16__NO__KDF(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF()), _dafny.Seq([0, 120]), 1, default__.AES__256__GCM__IV12__TAG16, software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_IDENTITY(software_amazon_cryptography_materialproviders_internaldafny_types.IDENTITY_IDENTITY()), software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(software_amazon_cryptography_materialproviders_internaldafny_types.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256()), _dafny.Seq([1, 20]), 1, default__.AES__128__GCM__IV12__TAG16, default__.HKDF__SHA__256(default__.Bits128), software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(software_amazon_cryptography_materialproviders_internaldafny_types.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256()), _dafny.Seq([1, 70]), 1, default__.AES__192__GCM__IV12__TAG16, default__.HKDF__SHA__256(default__.Bits192), software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(software_amazon_cryptography_materialproviders_internaldafny_types.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256()), _dafny.Seq([1, 120]), 1, default__.AES__256__GCM__IV12__TAG16, default__.HKDF__SHA__256(default__.Bits256), software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(software_amazon_cryptography_materialproviders_internaldafny_types.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256()), _dafny.Seq([2, 20]), 1, default__.AES__128__GCM__IV12__TAG16, default__.HKDF__SHA__256(default__.Bits128), software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_ECDSA(software_amazon_cryptography_materialproviders_internaldafny_types.ECDSA_ECDSA(software_amazon_cryptography_primitives_internaldafny_types.ECDSASignatureAlgorithm_ECDSA__P256())), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(software_amazon_cryptography_materialproviders_internaldafny_types.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384()), _dafny.Seq([3, 70]), 1, default__.AES__192__GCM__IV12__TAG16, default__.HKDF__SHA__384(default__.Bits192), software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_ECDSA(software_amazon_cryptography_materialproviders_internaldafny_types.ECDSA_ECDSA(software_amazon_cryptography_primitives_internaldafny_types.ECDSASignatureAlgorithm_ECDSA__P384())), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(software_amazon_cryptography_materialproviders_internaldafny_types.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384()), _dafny.Seq([3, 120]), 1, default__.AES__256__GCM__IV12__TAG16, default__.HKDF__SHA__384(default__.Bits256), software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_ECDSA(software_amazon_cryptography_materialproviders_internaldafny_types.ECDSA_ECDSA(software_amazon_cryptography_primitives_internaldafny_types.ECDSASignatureAlgorithm_ECDSA__P384())), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(software_amazon_cryptography_materialproviders_internaldafny_types.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY()), _dafny.Seq([4, 120]), 2, default__.AES__256__GCM__IV12__TAG16, default__.HKDF__SHA__512(default__.Bits256), default__.HKDF__SHA__512(default__.Bits256), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(software_amazon_cryptography_materialproviders_internaldafny_types.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384()), _dafny.Seq([5, 120]), 2, default__.AES__256__GCM__IV12__TAG16, default__.HKDF__SHA__512(default__.Bits256), default__.HKDF__SHA__512(default__.Bits256), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_ECDSA(software_amazon_cryptography_materialproviders_internaldafny_types.ECDSA_ECDSA(software_amazon_cryptography_primitives_internaldafny_types.ECDSASignatureAlgorithm_ECDSA__P384())), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None__None()), software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(software_amazon_cryptography_materialproviders_internaldafny_types.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def SupportedESDKAlgorithmSuites(instance):
        return _dafny.Map({software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__NO__KDF(): default__.ESDK__ALG__AES__128__GCM__IV12__TAG16__NO__KDF, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__NO__KDF(): default__.ESDK__ALG__AES__192__GCM__IV12__TAG16__NO__KDF, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF(): default__.ESDK__ALG__AES__256__GCM__IV12__TAG16__NO__KDF, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256(): default__.ESDK__ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256(): default__.ESDK__ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256(): default__.ESDK__ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256(): default__.ESDK__ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384(): default__.ESDK__ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384(): default__.ESDK__ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY(): default__.ESDK__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY, software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384(): default__.ESDK__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384})
    @_dafny.classproperty
    def SupportedDBEAlgorithmSuites(instance):
        return _dafny.Map({software_amazon_cryptography_materialproviders_internaldafny_types.DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384(): default__.DBE__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384, software_amazon_cryptography_materialproviders_internaldafny_types.DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384(): default__.DBE__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384})
    @_dafny.classproperty
    def AlgorithmSuiteInfoByBinaryId(instance):
        return _dafny.Map({_dafny.Seq([0, 20]): default__.ESDK__ALG__AES__128__GCM__IV12__TAG16__NO__KDF, _dafny.Seq([0, 70]): default__.ESDK__ALG__AES__192__GCM__IV12__TAG16__NO__KDF, _dafny.Seq([0, 120]): default__.ESDK__ALG__AES__256__GCM__IV12__TAG16__NO__KDF, _dafny.Seq([1, 20]): default__.ESDK__ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256, _dafny.Seq([1, 70]): default__.ESDK__ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256, _dafny.Seq([1, 120]): default__.ESDK__ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256, _dafny.Seq([2, 20]): default__.ESDK__ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256, _dafny.Seq([3, 70]): default__.ESDK__ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384, _dafny.Seq([3, 120]): default__.ESDK__ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384, _dafny.Seq([4, 120]): default__.ESDK__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY, _dafny.Seq([5, 120]): default__.ESDK__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384, _dafny.Seq([103, 0]): default__.DBE__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384, _dafny.Seq([103, 1]): default__.DBE__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384})

class AlgorithmSuite:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo.default()()
