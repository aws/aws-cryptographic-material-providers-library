import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_MergeSort
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
import StandardLibraryInterop
import StandardLibrary_UInt
import StandardLibrary_String
import StandardLibrary
import UUID
import UTF8
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

# Module: AwsCryptographyPrimitivesOperations

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def GenerateRandomBytes(config, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out22_: Wrappers.Result
        out22_ = Random.default__.GenerateBytes((input).length)
        output = out22_
        return output

    @staticmethod
    def Digest(config, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out23_: Wrappers.Result
        out23_ = Digest.default__.Digest(input)
        output = out23_
        return output

    @staticmethod
    def HMac(config, input):
        return WrappedHMAC.default__.Digest(input)

    @staticmethod
    def HkdfExtract(config, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out24_: Wrappers.Result
        out24_ = WrappedHKDF.default__.Extract(input)
        output = out24_
        return output

    @staticmethod
    def HkdfExpand(config, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out25_: Wrappers.Result
        out25_ = WrappedHKDF.default__.Expand(input)
        output = out25_
        return output

    @staticmethod
    def Hkdf(config, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out26_: Wrappers.Result
        out26_ = WrappedHKDF.default__.Hkdf(input)
        output = out26_
        return output

    @staticmethod
    def KdfCounterMode(config, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out27_: Wrappers.Result
        out27_ = KdfCtr.default__.KdfCounterMode(input)
        output = out27_
        return output

    @staticmethod
    def AesKdfCounterMode(config, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        output = Wrappers.Result_Failure(software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Implement")))
        return output

    @staticmethod
    def AESEncrypt(config, input):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput.default())()
        out28_: Wrappers.Result
        out28_ = AESEncryption.default__.AESEncrypt(input)
        output = out28_
        return output

    @staticmethod
    def AESDecrypt(config, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out29_: Wrappers.Result
        out29_ = AESEncryption.default__.AESDecrypt(input)
        output = out29_
        return output

    @staticmethod
    def GenerateRSAKeyPair(config, input):
        output: Wrappers.Result = None
        d_107_publicKey_: software_amazon_cryptography_primitives_internaldafny_types.RSAPublicKey
        d_108_privateKey_: software_amazon_cryptography_primitives_internaldafny_types.RSAPrivateKey
        out30_: software_amazon_cryptography_primitives_internaldafny_types.RSAPublicKey
        out31_: software_amazon_cryptography_primitives_internaldafny_types.RSAPrivateKey
        out30_, out31_ = RSAEncryption.default__.GenerateKeyPair((input).lengthBits)
        d_107_publicKey_ = out30_
        d_108_privateKey_ = out31_
        output = Wrappers.Result_Success(software_amazon_cryptography_primitives_internaldafny_types.GenerateRSAKeyPairOutput_GenerateRSAKeyPairOutput(d_107_publicKey_, d_108_privateKey_))
        return output

    @staticmethod
    def GetRSAKeyModulusLength(config, input):
        d_109_valueOrError0_ = RSAEncryption.default__.GetRSAKeyModulusLength((input).publicKey)
        if (d_109_valueOrError0_).IsFailure():
            return (d_109_valueOrError0_).PropagateFailure()
        elif True:
            d_110_length_ = (d_109_valueOrError0_).Extract()
            return Wrappers.Result_Success(software_amazon_cryptography_primitives_internaldafny_types.GetRSAKeyModulusLengthOutput_GetRSAKeyModulusLengthOutput(d_110_length_))

    @staticmethod
    def RSADecrypt(config, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out32_: Wrappers.Result
        out32_ = RSAEncryption.default__.Decrypt(input)
        output = out32_
        return output

    @staticmethod
    def RSAEncrypt(config, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out33_: Wrappers.Result
        out33_ = RSAEncryption.default__.Encrypt(input)
        output = out33_
        return output

    @staticmethod
    def GenerateECDSASignatureKey(config, input):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_primitives_internaldafny_types.GenerateECDSASignatureKeyOutput.default())()
        out34_: Wrappers.Result
        out34_ = Signature.default__.KeyGen(input)
        output = out34_
        return output

    @staticmethod
    def ECDSASign(config, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out35_: Wrappers.Result
        out35_ = Signature.ECDSA.Sign((input).signatureAlgorithm, (input).signingKey, (input).message)
        output = out35_
        return output

    @staticmethod
    def ECDSAVerify(config, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        output = Signature.ECDSA_Verify((input).signatureAlgorithm, (input).verificationKey, (input).message, (input).signature)
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
        return isinstance(self, Config_Config)

class Config_Config(Config, NamedTuple('Config', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesOperations.Config.Config'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Config_Config)
    def __hash__(self) -> int:
        return super().__hash__()

