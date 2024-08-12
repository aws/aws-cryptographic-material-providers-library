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
        pat_let_tv100_ = a
        pat_let_tv101_ = a
        pat_let_tv102_ = a
        pat_let_tv103_ = a
        pat_let_tv104_ = a
        pat_let_tv105_ = a
        pat_let_tv106_ = a
        pat_let_tv107_ = a
        def lambda33_():
            source11_ = ((a).id).ESDK
            unmatched11 = True
            if unmatched11:
                if source11_.is_ALG__AES__128__GCM__IV12__TAG16__NO__KDF:
                    unmatched11 = False
                    return ((((((((((pat_let_tv8_).binaryId) == (_dafny.Seq([0, 20]))) and (((pat_let_tv9_).messageVersion) == (1))) and (True)) and (((((pat_let_tv10_).encrypt).AES__GCM).keyLength) == (16))) and (((pat_let_tv11_).kdf).is_IDENTITY)) and (((pat_let_tv12_).signature).is_None)) and (((pat_let_tv13_).commitment).is_None)) and (((pat_let_tv14_).symmetricSignature).is_None)) and (((pat_let_tv15_).edkWrapping).is_DIRECT__KEY__WRAPPING)
            if unmatched11:
                if source11_.is_ALG__AES__192__GCM__IV12__TAG16__NO__KDF:
                    unmatched11 = False
                    return ((((((((((pat_let_tv16_).binaryId) == (_dafny.Seq([0, 70]))) and (((pat_let_tv17_).messageVersion) == (1))) and (True)) and (((((pat_let_tv18_).encrypt).AES__GCM).keyLength) == (24))) and (((pat_let_tv19_).kdf).is_IDENTITY)) and (((pat_let_tv20_).signature).is_None)) and (((pat_let_tv21_).commitment).is_None)) and (((pat_let_tv22_).symmetricSignature).is_None)) and (((pat_let_tv23_).edkWrapping).is_DIRECT__KEY__WRAPPING)
            if unmatched11:
                if source11_.is_ALG__AES__256__GCM__IV12__TAG16__NO__KDF:
                    unmatched11 = False
                    return ((((((((((pat_let_tv24_).binaryId) == (_dafny.Seq([0, 120]))) and (((pat_let_tv25_).messageVersion) == (1))) and (True)) and (((((pat_let_tv26_).encrypt).AES__GCM).keyLength) == (32))) and (((pat_let_tv27_).kdf).is_IDENTITY)) and (((pat_let_tv28_).signature).is_None)) and (((pat_let_tv29_).commitment).is_None)) and (((pat_let_tv30_).symmetricSignature).is_None)) and (((pat_let_tv31_).edkWrapping).is_DIRECT__KEY__WRAPPING)
            if unmatched11:
                if source11_.is_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256:
                    unmatched11 = False
                    return (((((((((((pat_let_tv32_).binaryId) == (_dafny.Seq([1, 20]))) and (((pat_let_tv33_).messageVersion) == (1))) and (True)) and (((((pat_let_tv34_).encrypt).AES__GCM).keyLength) == (16))) and (((pat_let_tv35_).kdf).is_HKDF)) and (((((pat_let_tv36_).kdf).HKDF).hmac) == (AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__256()))) and (((pat_let_tv37_).signature).is_None)) and (((pat_let_tv38_).commitment).is_None)) and (((pat_let_tv39_).symmetricSignature).is_None)) and (((pat_let_tv40_).edkWrapping).is_DIRECT__KEY__WRAPPING)
            if unmatched11:
                if source11_.is_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA256:
                    unmatched11 = False
                    return (((((((((((pat_let_tv41_).binaryId) == (_dafny.Seq([1, 70]))) and (((pat_let_tv42_).messageVersion) == (1))) and (True)) and (((((pat_let_tv43_).encrypt).AES__GCM).keyLength) == (24))) and (((pat_let_tv44_).kdf).is_HKDF)) and (((((pat_let_tv45_).kdf).HKDF).hmac) == (AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__256()))) and (((pat_let_tv46_).signature).is_None)) and (((pat_let_tv47_).commitment).is_None)) and (((pat_let_tv48_).symmetricSignature).is_None)) and (((pat_let_tv49_).edkWrapping).is_DIRECT__KEY__WRAPPING)
            if unmatched11:
                if source11_.is_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA256:
                    unmatched11 = False
                    return (((((((((((pat_let_tv50_).binaryId) == (_dafny.Seq([1, 120]))) and (((pat_let_tv51_).messageVersion) == (1))) and (True)) and (((((pat_let_tv52_).encrypt).AES__GCM).keyLength) == (32))) and (((pat_let_tv53_).kdf).is_HKDF)) and (((((pat_let_tv54_).kdf).HKDF).hmac) == (AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__256()))) and (((pat_let_tv55_).signature).is_None)) and (((pat_let_tv56_).commitment).is_None)) and (((pat_let_tv57_).symmetricSignature).is_None)) and (((pat_let_tv58_).edkWrapping).is_DIRECT__KEY__WRAPPING)
            if unmatched11:
                if source11_.is_ALG__AES__128__GCM__IV12__TAG16__HKDF__SHA256__ECDSA__P256:
                    unmatched11 = False
                    return ((((((((((((pat_let_tv59_).binaryId) == (_dafny.Seq([2, 20]))) and (((pat_let_tv60_).messageVersion) == (1))) and (True)) and (((((pat_let_tv61_).encrypt).AES__GCM).keyLength) == (16))) and (((pat_let_tv62_).kdf).is_HKDF)) and (((((pat_let_tv63_).kdf).HKDF).hmac) == (AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__256()))) and (((pat_let_tv64_).signature).is_ECDSA)) and (((((pat_let_tv65_).signature).ECDSA).curve) == (AwsCryptographyPrimitivesTypes.ECDSASignatureAlgorithm_ECDSA__P256()))) and (((pat_let_tv66_).commitment).is_None)) and (((pat_let_tv67_).symmetricSignature).is_None)) and (((pat_let_tv68_).edkWrapping).is_DIRECT__KEY__WRAPPING)
            if unmatched11:
                if source11_.is_ALG__AES__192__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384:
                    unmatched11 = False
                    return ((((((((((((pat_let_tv69_).binaryId) == (_dafny.Seq([3, 70]))) and (((pat_let_tv70_).messageVersion) == (1))) and (True)) and (((((pat_let_tv71_).encrypt).AES__GCM).keyLength) == (24))) and (((pat_let_tv72_).kdf).is_HKDF)) and (((((pat_let_tv73_).kdf).HKDF).hmac) == (AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__384()))) and (((pat_let_tv74_).signature).is_ECDSA)) and (((((pat_let_tv75_).signature).ECDSA).curve) == (AwsCryptographyPrimitivesTypes.ECDSASignatureAlgorithm_ECDSA__P384()))) and (((pat_let_tv76_).commitment).is_None)) and (((pat_let_tv77_).symmetricSignature).is_None)) and (((pat_let_tv78_).edkWrapping).is_DIRECT__KEY__WRAPPING)
            if unmatched11:
                if source11_.is_ALG__AES__256__GCM__IV12__TAG16__HKDF__SHA384__ECDSA__P384:
                    unmatched11 = False
                    return ((((((((((((pat_let_tv79_).binaryId) == (_dafny.Seq([3, 120]))) and (((pat_let_tv80_).messageVersion) == (1))) and (True)) and (((((pat_let_tv81_).encrypt).AES__GCM).keyLength) == (32))) and (((pat_let_tv82_).kdf).is_HKDF)) and (((((pat_let_tv83_).kdf).HKDF).hmac) == (AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__384()))) and (((pat_let_tv84_).signature).is_ECDSA)) and (((((pat_let_tv85_).signature).ECDSA).curve) == (AwsCryptographyPrimitivesTypes.ECDSASignatureAlgorithm_ECDSA__P384()))) and (((pat_let_tv86_).commitment).is_None)) and (((pat_let_tv87_).symmetricSignature).is_None)) and (((pat_let_tv88_).edkWrapping).is_DIRECT__KEY__WRAPPING)
            if unmatched11:
                if source11_.is_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY:
                    unmatched11 = False
                    return (((((((((((pat_let_tv89_).binaryId) == (_dafny.Seq([4, 120]))) and (((pat_let_tv90_).messageVersion) == (2))) and (True)) and (((((pat_let_tv91_).encrypt).AES__GCM).keyLength) == (32))) and (((pat_let_tv92_).kdf).is_HKDF)) and (((((pat_let_tv93_).kdf).HKDF).hmac) == (AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__512()))) and (((pat_let_tv94_).signature).is_None)) and (((pat_let_tv95_).commitment).is_HKDF)) and (((pat_let_tv96_).symmetricSignature).is_None)) and (((pat_let_tv97_).edkWrapping).is_DIRECT__KEY__WRAPPING)
            if unmatched11:
                unmatched11 = False
                return ((((((((((((pat_let_tv98_).binaryId) == (_dafny.Seq([5, 120]))) and (((pat_let_tv99_).messageVersion) == (2))) and (True)) and (((((pat_let_tv100_).encrypt).AES__GCM).keyLength) == (32))) and (((pat_let_tv101_).kdf).is_HKDF)) and (((((pat_let_tv102_).kdf).HKDF).hmac) == (AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__512()))) and (((pat_let_tv103_).signature).is_ECDSA)) and (((((pat_let_tv104_).signature).ECDSA).curve) == (AwsCryptographyPrimitivesTypes.ECDSASignatureAlgorithm_ECDSA__P384()))) and (((pat_let_tv105_).commitment).is_HKDF)) and (((pat_let_tv106_).symmetricSignature).is_None)) and (((pat_let_tv107_).edkWrapping).is_DIRECT__KEY__WRAPPING)
            raise Exception("unexpected control point")

        return ((default__.AlgorithmSuiteInfo_q(a)) and (default__.SupportedESDKEncrypt_q((a).encrypt))) and (lambda33_())

    @staticmethod
    def DBEAlgorithmSuite_q(a):
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
        pat_let_tv123_ = a
        pat_let_tv124_ = a
        pat_let_tv125_ = a
        pat_let_tv126_ = a
        pat_let_tv127_ = a
        pat_let_tv128_ = a
        pat_let_tv129_ = a
        pat_let_tv130_ = a
        def lambda34_():
            source12_ = ((a).id).DBE
            unmatched12 = True
            if unmatched12:
                if source12_.is_ALG__AES__256__GCM__HKDF__SHA512__COMMIT__KEY__SYMSIG__HMAC__SHA384:
                    unmatched12 = False
                    return ((((((((((((((pat_let_tv108_).binaryId) == (_dafny.Seq([103, 0]))) and (((pat_let_tv109_).messageVersion) == (1))) and (True)) and (((((pat_let_tv110_).encrypt).AES__GCM).keyLength) == (32))) and (((pat_let_tv111_).kdf).is_HKDF)) and (((((pat_let_tv112_).kdf).HKDF).hmac) == (AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__512()))) and (((pat_let_tv113_).signature).is_None)) and (((pat_let_tv114_).commitment).is_HKDF)) and (((pat_let_tv115_).symmetricSignature).is_HMAC)) and ((((pat_let_tv116_).symmetricSignature).HMAC) == (AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__384()))) and (((pat_let_tv117_).edkWrapping).is_IntermediateKeyWrapping)) and (True)) and (((((((pat_let_tv118_).edkWrapping).IntermediateKeyWrapping).pdkEncryptAlgorithm).AES__GCM).keyLength) == (32))
            if unmatched12:
                unmatched12 = False
                return (((((((((((((((pat_let_tv119_).binaryId) == (_dafny.Seq([103, 1]))) and (((pat_let_tv120_).messageVersion) == (1))) and (True)) and (((((pat_let_tv121_).encrypt).AES__GCM).keyLength) == (32))) and (((pat_let_tv122_).kdf).is_HKDF)) and (((((pat_let_tv123_).kdf).HKDF).hmac) == (AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__512()))) and (((pat_let_tv124_).signature).is_ECDSA)) and (((((pat_let_tv125_).signature).ECDSA).curve) == (AwsCryptographyPrimitivesTypes.ECDSASignatureAlgorithm_ECDSA__P384()))) and (((pat_let_tv126_).commitment).is_HKDF)) and (((pat_let_tv127_).symmetricSignature).is_HMAC)) and ((((pat_let_tv128_).symmetricSignature).HMAC) == (AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__384()))) and (((pat_let_tv129_).edkWrapping).is_IntermediateKeyWrapping)) and (True)) and (((((((pat_let_tv130_).edkWrapping).IntermediateKeyWrapping).pdkEncryptAlgorithm).AES__GCM).keyLength) == (32))
            raise Exception("unexpected control point")

        return (((default__.AlgorithmSuiteInfo_q(a)) and (default__.SupportedDBEEncrypt_q((a).encrypt))) and (default__.SupportedDBEEDKWrapping_q((a).edkWrapping))) and (lambda34_())

    @staticmethod
    def AlgorithmSuite_q(a):
        pat_let_tv131_ = a
        pat_let_tv132_ = a
        source13_ = (a).id
        unmatched13 = True
        if unmatched13:
            if source13_.is_ESDK:
                unmatched13 = False
                return default__.ESDKAlgorithmSuite_q(pat_let_tv131_)
        if unmatched13:
            unmatched13 = False
            return default__.DBEAlgorithmSuite_q(pat_let_tv132_)
        raise Exception("unexpected control point")

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
        unmatched14 = True
        if unmatched14:
            if source14_.is_ESDK:
                d_330_e_ = source14_.ESDK
                unmatched14 = False
                return default__.GetESDKSuite(d_330_e_)
        if unmatched14:
            d_331_e_ = source14_.DBE
            unmatched14 = False
            return default__.GetDBESuite(d_331_e_)
        raise Exception("unexpected control point")

    @staticmethod
    def GetDBESuite(id):
        return (default__.SupportedDBEAlgorithmSuites)[id]

    @staticmethod
    def GetESDKSuite(id):
        return (default__.SupportedESDKAlgorithmSuites)[id]

    @staticmethod
    def GetEncryptKeyLength(a):
        source15_ = (a).encrypt
        unmatched15 = True
        if unmatched15:
            d_332_e_ = source15_.AES__GCM
            unmatched15 = False
            return (d_332_e_).keyLength
        raise Exception("unexpected control point")

    @staticmethod
    def GetEncryptTagLength(a):
        source16_ = (a).encrypt
        unmatched16 = True
        if unmatched16:
            d_333_e_ = source16_.AES__GCM
            unmatched16 = False
            return (d_333_e_).tagLength
        raise Exception("unexpected control point")

    @staticmethod
    def GetEncryptIvLength(a):
        source17_ = (a).encrypt
        unmatched17 = True
        if unmatched17:
            d_334_e_ = source17_.AES__GCM
            unmatched17 = False
            return (d_334_e_).ivLength
        raise Exception("unexpected control point")

    @staticmethod
    def GetAlgorithmSuiteInfo(binaryId_q):
        d_335_valueOrError0_ = Wrappers.default__.Need((binaryId_q) in (default__.AlgorithmSuiteInfoByBinaryId), AwsCryptographyMaterialProvidersTypes.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid BinaryId")))
        if (d_335_valueOrError0_).IsFailure():
            return (d_335_valueOrError0_).PropagateFailure()
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
        d_336_a_: AwsCryptographyMaterialProvidersTypes.AlgorithmSuiteInfo = source__
        return default__.AlgorithmSuite_q(d_336_a_)
