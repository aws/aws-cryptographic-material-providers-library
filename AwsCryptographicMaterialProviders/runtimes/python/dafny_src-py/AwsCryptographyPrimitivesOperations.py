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
import software_amazon_cryptography_keystore_internaldafny
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

assert "AwsCryptographyPrimitivesOperations" == __name__
AwsCryptographyPrimitivesOperations = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def GenerateRandomBytes(config, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out76_: Wrappers.Result
        out76_ = Random.default__.GenerateBytes((input).length)
        output = out76_
        return output

    @staticmethod
    def Digest(config, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out77_: Wrappers.Result
        out77_ = Digest.default__.Digest(input)
        output = out77_
        return output

    @staticmethod
    def HMac(config, input):
        return WrappedHMAC.default__.Digest(input)

    @staticmethod
    def HkdfExtract(config, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out78_: Wrappers.Result
        out78_ = WrappedHKDF.default__.Extract(input)
        output = out78_
        return output

    @staticmethod
    def HkdfExpand(config, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out79_: Wrappers.Result
        out79_ = WrappedHKDF.default__.Expand(input)
        output = out79_
        return output

    @staticmethod
    def Hkdf(config, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out80_: Wrappers.Result
        out80_ = WrappedHKDF.default__.Hkdf(input)
        output = out80_
        return output

    @staticmethod
    def KdfCounterMode(config, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out81_: Wrappers.Result
        out81_ = KdfCtr.default__.KdfCounterMode(input)
        output = out81_
        return output

    @staticmethod
    def AesKdfCounterMode(config, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        output = Wrappers.Result_Failure(software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Implement")))
        return output

    @staticmethod
    def AESEncrypt(config, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput.default())()
        out82_: Wrappers.Result
        out82_ = AESEncryption.default__.AESEncrypt(input)
        output = out82_
        return output

    @staticmethod
    def AESDecrypt(config, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out83_: Wrappers.Result
        out83_ = AESEncryption.default__.AESDecrypt(input)
        output = out83_
        return output

    @staticmethod
    def GenerateRSAKeyPair(config, input):
        output: Wrappers.Result = None
        d_387_publicKey_: software_amazon_cryptography_primitives_internaldafny_types.RSAPublicKey
        d_388_privateKey_: software_amazon_cryptography_primitives_internaldafny_types.RSAPrivateKey
        out84_: software_amazon_cryptography_primitives_internaldafny_types.RSAPublicKey
        out85_: software_amazon_cryptography_primitives_internaldafny_types.RSAPrivateKey
        out84_, out85_ = RSAEncryption.default__.GenerateKeyPair((input).lengthBits)
        d_387_publicKey_ = out84_
        d_388_privateKey_ = out85_
        output = Wrappers.Result_Success(software_amazon_cryptography_primitives_internaldafny_types.GenerateRSAKeyPairOutput_GenerateRSAKeyPairOutput(d_387_publicKey_, d_388_privateKey_))
        return output

    @staticmethod
    def GetRSAKeyModulusLength(config, input):
        d_389_valueOrError0_ = RSAEncryption.default__.GetRSAKeyModulusLength((input).publicKey)
        if (d_389_valueOrError0_).IsFailure():
            return (d_389_valueOrError0_).PropagateFailure()
        elif True:
            d_390_length_ = (d_389_valueOrError0_).Extract()
            return Wrappers.Result_Success(software_amazon_cryptography_primitives_internaldafny_types.GetRSAKeyModulusLengthOutput_GetRSAKeyModulusLengthOutput(d_390_length_))

    @staticmethod
    def RSADecrypt(config, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out86_: Wrappers.Result
        out86_ = RSAEncryption.default__.Decrypt(input)
        output = out86_
        return output

    @staticmethod
    def RSAEncrypt(config, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out87_: Wrappers.Result
        out87_ = RSAEncryption.default__.Encrypt(input)
        output = out87_
        return output

    @staticmethod
    def GenerateECDSASignatureKey(config, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_primitives_internaldafny_types.GenerateECDSASignatureKeyOutput.default())()
        out88_: Wrappers.Result
        out88_ = Signature.default__.KeyGen(input)
        output = out88_
        return output

    @staticmethod
    def ECDSASign(config, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out89_: Wrappers.Result
        out89_ = Signature.ECDSA.Sign((input).signatureAlgorithm, (input).signingKey, (input).message)
        output = out89_
        return output

    @staticmethod
    def ECDSAVerify(config, input):
        output: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.bool)()
        output = Signature.ECDSA.Verify((input).signatureAlgorithm, (input).verificationKey, (input).message, (input).signature)
        return output


class Config:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [Config_Config()]
    @classmethod
    def default(cls, ):
        return lambda: Config_Config()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Config(self) -> bool:
        return isinstance(self, AwsCryptographyPrimitivesOperations.Config_Config)

class Config_Config(Config, NamedTuple('Config', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesOperations.Config.Config'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AwsCryptographyPrimitivesOperations.Config_Config)
    def __hash__(self) -> int:
        return super().__hash__()

