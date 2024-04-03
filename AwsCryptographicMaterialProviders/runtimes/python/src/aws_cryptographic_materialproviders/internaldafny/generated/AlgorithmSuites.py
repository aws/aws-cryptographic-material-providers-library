import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import BoundedInts
import StandardLibrary_UInt
import StandardLibrary_String
import StandardLibrary
import UTF8
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_primitives_internaldafny_types
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
import AesKdfCtr
import Relations
import Seq_MergeSort
import Math
import Seq
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
import StandardLibraryInterop
import UUID
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import GetOpt
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
import software_amazon_cryptography_keystore_internaldafny_types
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
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import Com_Amazonaws
import Com
import software_amazon_cryptography_keystore_internaldafny

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
        pat_let_tv0_ = a
        pat_let_tv1_ = a
        pat_let_tv2_ = a
        pat_let_tv3_ = a
        pat_let_tv4_ = a
        pat_let_tv5_ = a
        pat_let_tv6_ = a
        pat_let_tv7_ = a
        pat_let_tv8_ = a
        pat_let_tv9_ = a
        pat_let_tv10_ = a
        pat_let_tv11_ = a
        pat_let_tv12_ = a
        pat_let_tv13_ = a
        pat_let_tv14_ = a
        pat_let_tv15_ = a
        pat_let_tv16_ = a
        pat_let_tv17_ = a
        pat_let_tv18_ = a
        pat_let_tv19_ = a
        pat_let_tv20_ = a
        pat_let_tv21_ = a
        pat_let_tv22_ = a
        pat_let_tv23_ = a
        pat_let_tv24_ = a
        pat_let_tv25_ = a
        pat_let_tv26_ = a
        pat_let_tv27_ = a
        pat_let_tv28_ = a
        pat_let_tv29_ = a
        pat_let_tv30_ = a
        pat_let_tv31_ = a
        pat_let_tv32_ = a
        pat_let_tv33_ = a
        pat_let_tv34_ = a
        pat_let_tv35_ = a
        pat_let_tv36_ = a
        pat_let_tv37_ = a
        pat_let_tv38_ = a
        pat_let_tv39_ = a
        pat_let_tv40_ = a
        pat_let_tv41_ = a
        pat_let_tv42_ = a
        pat_let_tv43_ = a
        pat_let_tv44_ = a
        pat_let_tv45_ = a
        pat_let_tv46_ = a
        pat_let_tv47_ = a
        pat_let_tv48_ = a
        pat_let_tv49_ = a
        pat_let_tv50_ = a
        pat_let_tv51_ = a
        pat_let_tv52_ = a
        pat_let_tv53_ = a
        pat_let_tv54_ = a
        pat_let_tv55_ = a
        pat_let_tv56_ = a
        pat_let_tv57_ = a
        pat_let_tv58_ = a
        pat_let_tv59_ = a
        pat_let_tv60_ = a
        pat_let_tv61_ = a
        pat_let_tv62_ = a
        pat_let_tv63_ = a
        pat_let_tv64_ = a
        pat_let_tv65_ = a
        pat_let_tv66_ = a
        pat_let_tv67_ = a
        pat_let_tv68_ = a
        pat_let_tv69_ = a
        pat_let_tv70_ = a
        pat_let_tv71_ = a
        pat_let_tv72_ = a
        pat_let_tv73_ = a
        pat_let_tv74_ = a
        pat_let_tv75_ = a
        pat_let_tv76_ = a
        pat_let_tv77_ = a
        pat_let_tv78_ = a
        pat_let_tv79_ = a
        pat_let_tv80_ = a
        pat_let_tv81_ = a
        pat_let_tv82_ = a
        pat_let_tv83_ = a
        pat_let_tv84_ = a
        pat_let_tv85_ = a
        pat_let_tv86_ = a
        pat_let_tv87_ = a
        pat_let_tv88_ = a
        pat_let_tv89_ = a
        pat_let_tv90_ = a
        pat_let_tv91_ = a
        pat_let_tv92_ = a
        pat_let_tv93_ = a
        pat_let_tv94_ = a
        pat_let_tv95_ = a
        pat_let_tv96_ = a
        pat_let_tv97_ = a
        pat_let_tv98_ = a
        pat_let_tv99_ = a
        def lambda29_(source10_):
            if source10_.is_ALG__AES__128__GCM__IV12__TAG16__NO__KDF:
                return ((((((((((pat_let_tv0_).binaryId) == (_dafny.Seq([0, 20]))) and (((pat_let_tv1_).messageVersion) == (1))) and (True)) and (((((pat_let_tv2_).encrypt).AES__GCM).keyLength) == (16))) and (((pat_let_tv3_).kdf).is_IDENTITY)) and (((pat_let_tv4_).signature).is_None)) and (((pat_let_tv5_).commitment).is_None)) and (((pat_let_tv6_).symmetricSignature).is_None)) and (((pat_let_tv7_).edkWrapping).is_DIRECT__KEY__WRAPPING)
            elif source10_.is_ALG__AES__192__GCM__IV12__TAG16__NO__KDF:
                return ((((((((((pat_let_tv8_).binaryId) == (_dafny.Seq([0, 70]))) and (((pat_let_tv9_).messageVersion) == (1))) and (True)) and (((((pat_let_tv10_).encrypt).AES__GCM).keyLength) == (24))) and (((pat_let_tv11_).kdf).is_IDENTITY)) and (((pat_let_tv12_).signature).is_None)) and (((pat_let_tv13_).commitment).is_None)) and (((pat_let_tv14_).symmetricSignature).is_None)) and (((pat_let_tv15_).edkWrapping).is_DIRECT__KEY__WRAPPING)
            elif source10_.is_ALG__AES__256__GCM__IV12__TAG16__NO__KDF:
                return ((((((((((pat_let_tv16_).binaryId) == (_dafny.Seq([0, 120]))) and (((pat_let_tv17_).messageVersion) == (1))) and (True)) and (((((pat_let_tv18_).encrypt).AES__GCM).keyLength) == (32))) and (((pat_let_tv19_).kdf).is_IDENTITY)) and (((pat_let_tv20_).signature).is_None)) and (((pat_let_tv21_).commitment).is_None)) and (((pat_let_tv22_).symmetricSignature).is_None)) and (((pat_let_tv23_).edkWrapping).is_DIRECT__KEY__WRAPPING)
            elif source10_.is_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256:
                return (((((((((((pat_let_tv24_).binaryId) == (_dafny.Seq([1, 20]))) and (((pat_let_tv25_).messageVersion) == (1))) and (True)) and (((((pat_let_tv26_).encrypt).AES__GCM).keyLength) == (16))) and (((pat_let_tv27_).kdf).is_HKDF)) and (((((pat_let_tv28_).kdf).HKDF).hmac) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__256()))) and (((pat_let_tv29_).signature).is_None)) and (((pat_let_tv30_).commitment).is_None)) and (((pat_let_tv31_).symmetricSignature).is_None)) and (((pat_let_tv32_).edkWrapping).is_DIRECT__KEY__WRAPPING)
            elif source10_.is_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256:
                return (((((((((((pat_let_tv33_).binaryId) == (_dafny.Seq([1, 70]))) and (((pat_let_tv34_).messageVersion) == (1))) and (True)) and (((((pat_let_tv35_).encrypt).AES__GCM).keyLength) == (24))) and (((pat_let_tv36_).kdf).is_HKDF)) and (((((pat_let_tv37_).kdf).HKDF).hmac) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__256()))) and (((pat_let_tv38_).signature).is_None)) and (((pat_let_tv39_).commitment).is_None)) and (((pat_let_tv40_).symmetricSignature).is_None)) and (((pat_let_tv41_).edkWrapping).is_DIRECT__KEY__WRAPPING)
            elif source10_.is_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256:
                return (((((((((((pat_let_tv42_).binaryId) == (_dafny.Seq([1, 120]))) and (((pat_let_tv43_).messageVersion) == (1))) and (True)) and (((((pat_let_tv44_).encrypt).AES__GCM).keyLength) == (32))) and (((pat_let_tv45_).kdf).is_HKDF)) and (((((pat_let_tv46_).kdf).HKDF).hmac) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__256()))) and (((pat_let_tv47_).signature).is_None)) and (((pat_let_tv48_).commitment).is_None)) and (((pat_let_tv49_).symmetricSignature).is_None)) and (((pat_let_tv50_).edkWrapping).is_DIRECT__KEY__WRAPPING)
            elif source10_.is_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256:
                return ((((((((((((pat_let_tv51_).binaryId) == (_dafny.Seq([2, 20]))) and (((pat_let_tv52_).messageVersion) == (1))) and (True)) and (((((pat_let_tv53_).encrypt).AES__GCM).keyLength) == (16))) and (((pat_let_tv54_).kdf).is_HKDF)) and (((((pat_let_tv55_).kdf).HKDF).hmac) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__256()))) and (((pat_let_tv56_).signature).is_ECDSA)) and (((((pat_let_tv57_).signature).ECDSA).curve) == (software_amazon_cryptography_primitives_internaldafny_types.ECDSASignatureAlgorithm_ECDSA__P256()))) and (((pat_let_tv58_).commitment).is_None)) and (((pat_let_tv59_).symmetricSignature).is_None)) and (((pat_let_tv60_).edkWrapping).is_DIRECT__KEY__WRAPPING)
            elif source10_.is_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384:
                return ((((((((((((pat_let_tv61_).binaryId) == (_dafny.Seq([3, 70]))) and (((pat_let_tv62_).messageVersion) == (1))) and (True)) and (((((pat_let_tv63_).encrypt).AES__GCM).keyLength) == (24))) and (((pat_let_tv64_).kdf).is_HKDF)) and (((((pat_let_tv65_).kdf).HKDF).hmac) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__384()))) and (((pat_let_tv66_).signature).is_ECDSA)) and (((((pat_let_tv67_).signature).ECDSA).curve) == (software_amazon_cryptography_primitives_internaldafny_types.ECDSASignatureAlgorithm_ECDSA__P384()))) and (((pat_let_tv68_).commitment).is_None)) and (((pat_let_tv69_).symmetricSignature).is_None)) and (((pat_let_tv70_).edkWrapping).is_DIRECT__KEY__WRAPPING)
            elif source10_.is_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384:
                return ((((((((((((pat_let_tv71_).binaryId) == (_dafny.Seq([3, 120]))) and (((pat_let_tv72_).messageVersion) == (1))) and (True)) and (((((pat_let_tv73_).encrypt).AES__GCM).keyLength) == (32))) and (((pat_let_tv74_).kdf).is_HKDF)) and (((((pat_let_tv75_).kdf).HKDF).hmac) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__384()))) and (((pat_let_tv76_).signature).is_ECDSA)) and (((((pat_let_tv77_).signature).ECDSA).curve) == (software_amazon_cryptography_primitives_internaldafny_types.ECDSASignatureAlgorithm_ECDSA__P384()))) and (((pat_let_tv78_).commitment).is_None)) and (((pat_let_tv79_).symmetricSignature).is_None)) and (((pat_let_tv80_).edkWrapping).is_DIRECT__KEY__WRAPPING)
            elif source10_.is_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY:
                return (((((((((((pat_let_tv81_).binaryId) == (_dafny.Seq([4, 120]))) and (((pat_let_tv82_).messageVersion) == (2))) and (True)) and (((((pat_let_tv83_).encrypt).AES__GCM).keyLength) == (32))) and (((pat_let_tv84_).kdf).is_HKDF)) and (((((pat_let_tv85_).kdf).HKDF).hmac) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__512()))) and (((pat_let_tv86_).signature).is_None)) and (((pat_let_tv87_).commitment).is_HKDF)) and (((pat_let_tv88_).symmetricSignature).is_None)) and (((pat_let_tv89_).edkWrapping).is_DIRECT__KEY__WRAPPING)
            elif True:
                return ((((((((((((pat_let_tv90_).binaryId) == (_dafny.Seq([5, 120]))) and (((pat_let_tv91_).messageVersion) == (2))) and (True)) and (((((pat_let_tv92_).encrypt).AES__GCM).keyLength) == (32))) and (((pat_let_tv93_).kdf).is_HKDF)) and (((((pat_let_tv94_).kdf).HKDF).hmac) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__512()))) and (((pat_let_tv95_).signature).is_ECDSA)) and (((((pat_let_tv96_).signature).ECDSA).curve) == (software_amazon_cryptography_primitives_internaldafny_types.ECDSASignatureAlgorithm_ECDSA__P384()))) and (((pat_let_tv97_).commitment).is_HKDF)) and (((pat_let_tv98_).symmetricSignature).is_None)) and (((pat_let_tv99_).edkWrapping).is_DIRECT__KEY__WRAPPING)

        return ((default__.AlgorithmSuiteInfo_q(a)) and (default__.SupportedESDKEncrypt_q((a).encrypt))) and (lambda29_(((a).id).ESDK))

    @staticmethod
    def DBEAlgorithmSuite_q(a):
        pat_let_tv100_ = a
        pat_let_tv101_ = a
        pat_let_tv102_ = a
        pat_let_tv103_ = a
        pat_let_tv104_ = a
        pat_let_tv105_ = a
        pat_let_tv106_ = a
        pat_let_tv107_ = a
        pat_let_tv108_ = a
        pat_let_tv109_ = a
        pat_let_tv110_ = a
        pat_let_tv111_ = a
        pat_let_tv112_ = a
        pat_let_tv113_ = a
        pat_let_tv114_ = a
        pat_let_tv115_ = a
        pat_let_tv116_ = a
        pat_let_tv117_ = a
        pat_let_tv118_ = a
        pat_let_tv119_ = a
        pat_let_tv120_ = a
        pat_let_tv121_ = a
        pat_let_tv122_ = a
        def lambda30_(source11_):
            if source11_.is_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384:
                return ((((((((((((((pat_let_tv100_).binaryId) == (_dafny.Seq([103, 0]))) and (((pat_let_tv101_).messageVersion) == (1))) and (True)) and (((((pat_let_tv102_).encrypt).AES__GCM).keyLength) == (32))) and (((pat_let_tv103_).kdf).is_HKDF)) and (((((pat_let_tv104_).kdf).HKDF).hmac) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__512()))) and (((pat_let_tv105_).signature).is_None)) and (((pat_let_tv106_).commitment).is_HKDF)) and (((pat_let_tv107_).symmetricSignature).is_HMAC)) and ((((pat_let_tv108_).symmetricSignature).HMAC) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__384()))) and (((pat_let_tv109_).edkWrapping).is_IntermediateKeyWrapping)) and (True)) and (((((((pat_let_tv110_).edkWrapping).IntermediateKeyWrapping).pdkEncryptAlgorithm).AES__GCM).keyLength) == (32))
            elif True:
                return (((((((((((((((pat_let_tv111_).binaryId) == (_dafny.Seq([103, 1]))) and (((pat_let_tv112_).messageVersion) == (1))) and (True)) and (((((pat_let_tv113_).encrypt).AES__GCM).keyLength) == (32))) and (((pat_let_tv114_).kdf).is_HKDF)) and (((((pat_let_tv115_).kdf).HKDF).hmac) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__512()))) and (((pat_let_tv116_).signature).is_ECDSA)) and (((((pat_let_tv117_).signature).ECDSA).curve) == (software_amazon_cryptography_primitives_internaldafny_types.ECDSASignatureAlgorithm_ECDSA__P384()))) and (((pat_let_tv118_).commitment).is_HKDF)) and (((pat_let_tv119_).symmetricSignature).is_HMAC)) and ((((pat_let_tv120_).symmetricSignature).HMAC) == (software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__384()))) and (((pat_let_tv121_).edkWrapping).is_IntermediateKeyWrapping)) and (True)) and (((((((pat_let_tv122_).edkWrapping).IntermediateKeyWrapping).pdkEncryptAlgorithm).AES__GCM).keyLength) == (32))

        return (((default__.AlgorithmSuiteInfo_q(a)) and (default__.SupportedDBEEncrypt_q((a).encrypt))) and (default__.SupportedDBEEDKWrapping_q((a).edkWrapping))) and (lambda30_(((a).id).DBE))

    @staticmethod
    def AlgorithmSuite_q(a):
        source12_ = (a).id
        if source12_.is_ESDK:
            d_302___mcc_h0_ = source12_.ESDK
            return default__.ESDKAlgorithmSuite_q(a)
        elif True:
            d_303___mcc_h1_ = source12_.DBE
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
        source13_ = id
        if source13_.is_ESDK:
            d_304___mcc_h0_ = source13_.ESDK
            d_305_e_ = d_304___mcc_h0_
            return default__.GetESDKSuite(d_305_e_)
        elif True:
            d_306___mcc_h1_ = source13_.DBE
            d_307_e_ = d_306___mcc_h1_
            return default__.GetDBESuite(d_307_e_)

    @staticmethod
    def GetDBESuite(id):
        return (default__.SupportedDBEAlgorithmSuites)[id]

    @staticmethod
    def GetESDKSuite(id):
        return (default__.SupportedESDKAlgorithmSuites)[id]

    @staticmethod
    def GetEncryptKeyLength(a):
        source14_ = (a).encrypt
        d_308___mcc_h0_ = source14_.AES__GCM
        d_309_e_ = d_308___mcc_h0_
        return (d_309_e_).keyLength

    @staticmethod
    def GetEncryptTagLength(a):
        source15_ = (a).encrypt
        d_310___mcc_h0_ = source15_.AES__GCM
        d_311_e_ = d_310___mcc_h0_
        return (d_311_e_).tagLength

    @staticmethod
    def GetEncryptIvLength(a):
        source16_ = (a).encrypt
        d_312___mcc_h0_ = source16_.AES__GCM
        d_313_e_ = d_312___mcc_h0_
        return (d_313_e_).ivLength

    @staticmethod
    def GetAlgorithmSuiteInfo(binaryId_q):
        d_314_valueOrError0_ = Wrappers.default__.Need((binaryId_q) in (default__.AlgorithmSuiteInfoByBinaryId), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid BinaryId")))
        if (d_314_valueOrError0_).IsFailure():
            return (d_314_valueOrError0_).PropagateFailure()
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
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_DBE(software_amazon_cryptography_materialproviders_internaldafny_types.DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384()), _dafny.Seq([103, 0]), 1, default__.AES__256__GCM__IV12__TAG16, default__.HKDF__SHA__512(default__.Bits256), default__.HKDF__SHA__512(default__.Bits256), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None_None()), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_HMAC(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__384()), default__.EDK__INTERMEDIATE__WRAPPING__AES__GCM__256__HKDF__SHA__512)
    @_dafny.classproperty
    def DBE__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_DBE(software_amazon_cryptography_materialproviders_internaldafny_types.DBEAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384__SYMSIG__HMAC__SHA384()), _dafny.Seq([103, 1]), 1, default__.AES__256__GCM__IV12__TAG16, default__.HKDF__SHA__512(default__.Bits256), default__.HKDF__SHA__512(default__.Bits256), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_ECDSA(software_amazon_cryptography_materialproviders_internaldafny_types.ECDSA_ECDSA(software_amazon_cryptography_primitives_internaldafny_types.ECDSASignatureAlgorithm_ECDSA__P384())), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_HMAC(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__384()), default__.EDK__INTERMEDIATE__WRAPPING__AES__GCM__256__HKDF__SHA__512)
    @_dafny.classproperty
    def ESDK__ALG__AES__128__GCM__IV12__TAG16__NO__KDF(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__NO__KDF()), _dafny.Seq([0, 20]), 1, default__.AES__128__GCM__IV12__TAG16, software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_IDENTITY(software_amazon_cryptography_materialproviders_internaldafny_types.IDENTITY_IDENTITY()), software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None_None()), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None_None()), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None_None()), software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(software_amazon_cryptography_materialproviders_internaldafny_types.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__192__GCM__IV12__TAG16__NO__KDF(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__NO__KDF()), _dafny.Seq([0, 70]), 1, default__.AES__192__GCM__IV12__TAG16, software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_IDENTITY(software_amazon_cryptography_materialproviders_internaldafny_types.IDENTITY_IDENTITY()), software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None_None()), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None_None()), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None_None()), software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(software_amazon_cryptography_materialproviders_internaldafny_types.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__256__GCM__IV12__TAG16__NO__KDF(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__NO__KDF()), _dafny.Seq([0, 120]), 1, default__.AES__256__GCM__IV12__TAG16, software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_IDENTITY(software_amazon_cryptography_materialproviders_internaldafny_types.IDENTITY_IDENTITY()), software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None_None()), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None_None()), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None_None()), software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(software_amazon_cryptography_materialproviders_internaldafny_types.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256()), _dafny.Seq([1, 20]), 1, default__.AES__128__GCM__IV12__TAG16, default__.HKDF__SHA__256(default__.Bits128), software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None_None()), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None_None()), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None_None()), software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(software_amazon_cryptography_materialproviders_internaldafny_types.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256()), _dafny.Seq([1, 70]), 1, default__.AES__192__GCM__IV12__TAG16, default__.HKDF__SHA__256(default__.Bits192), software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None_None()), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None_None()), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None_None()), software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(software_amazon_cryptography_materialproviders_internaldafny_types.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256()), _dafny.Seq([1, 120]), 1, default__.AES__256__GCM__IV12__TAG16, default__.HKDF__SHA__256(default__.Bits256), software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None_None()), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None_None()), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None_None()), software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(software_amazon_cryptography_materialproviders_internaldafny_types.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256()), _dafny.Seq([2, 20]), 1, default__.AES__128__GCM__IV12__TAG16, default__.HKDF__SHA__256(default__.Bits128), software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None_None()), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_ECDSA(software_amazon_cryptography_materialproviders_internaldafny_types.ECDSA_ECDSA(software_amazon_cryptography_primitives_internaldafny_types.ECDSASignatureAlgorithm_ECDSA__P256())), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None_None()), software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(software_amazon_cryptography_materialproviders_internaldafny_types.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384()), _dafny.Seq([3, 70]), 1, default__.AES__192__GCM__IV12__TAG16, default__.HKDF__SHA__384(default__.Bits192), software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None_None()), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_ECDSA(software_amazon_cryptography_materialproviders_internaldafny_types.ECDSA_ECDSA(software_amazon_cryptography_primitives_internaldafny_types.ECDSASignatureAlgorithm_ECDSA__P384())), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None_None()), software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(software_amazon_cryptography_materialproviders_internaldafny_types.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384()), _dafny.Seq([3, 120]), 1, default__.AES__256__GCM__IV12__TAG16, default__.HKDF__SHA__384(default__.Bits256), software_amazon_cryptography_materialproviders_internaldafny_types.DerivationAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None_None()), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_ECDSA(software_amazon_cryptography_materialproviders_internaldafny_types.ECDSA_ECDSA(software_amazon_cryptography_primitives_internaldafny_types.ECDSASignatureAlgorithm_ECDSA__P384())), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None_None()), software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(software_amazon_cryptography_materialproviders_internaldafny_types.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY()), _dafny.Seq([4, 120]), 2, default__.AES__256__GCM__IV12__TAG16, default__.HKDF__SHA__512(default__.Bits256), default__.HKDF__SHA__512(default__.Bits256), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None_None()), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None_None()), software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(software_amazon_cryptography_materialproviders_internaldafny_types.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
    @_dafny.classproperty
    def ESDK__ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384(instance):
        return software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteId_ESDK(software_amazon_cryptography_materialproviders_internaldafny_types.ESDKAlgorithmSuiteId_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__ECDSA__P384()), _dafny.Seq([5, 120]), 2, default__.AES__256__GCM__IV12__TAG16, default__.HKDF__SHA__512(default__.Bits256), default__.HKDF__SHA__512(default__.Bits256), software_amazon_cryptography_materialproviders_internaldafny_types.SignatureAlgorithm_ECDSA(software_amazon_cryptography_materialproviders_internaldafny_types.ECDSA_ECDSA(software_amazon_cryptography_primitives_internaldafny_types.ECDSASignatureAlgorithm_ECDSA__P384())), software_amazon_cryptography_materialproviders_internaldafny_types.SymmetricSignatureAlgorithm_None(software_amazon_cryptography_materialproviders_internaldafny_types.None_None()), software_amazon_cryptography_materialproviders_internaldafny_types.EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(software_amazon_cryptography_materialproviders_internaldafny_types.DIRECT__KEY__WRAPPING_DIRECT__KEY__WRAPPING()))
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
    def _Is(source__):
        d_315_a_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo = source__
        return default__.AlgorithmSuite_q(d_315_a_)
