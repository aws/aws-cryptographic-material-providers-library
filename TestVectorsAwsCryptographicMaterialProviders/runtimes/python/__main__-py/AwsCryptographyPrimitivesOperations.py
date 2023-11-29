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
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsArnParsing
import AwsKmsMrkAreUnique
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
import Constants
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
        out39_: Wrappers.Result
        out39_ = Random.default__.GenerateBytes((input).length)
        output = out39_
        return output

    @staticmethod
    def Digest(config, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out40_: Wrappers.Result
        out40_ = Digest.default__.Digest(input)
        output = out40_
        return output

    @staticmethod
    def HMac(config, input):
        return WrappedHMAC.default__.Digest(input)

    @staticmethod
    def HkdfExtract(config, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out41_: Wrappers.Result
        out41_ = WrappedHKDF.default__.Extract(input)
        output = out41_
        return output

    @staticmethod
    def HkdfExpand(config, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out42_: Wrappers.Result
        out42_ = WrappedHKDF.default__.Expand(input)
        output = out42_
        return output

    @staticmethod
    def Hkdf(config, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out43_: Wrappers.Result
        out43_ = WrappedHKDF.default__.Hkdf(input)
        output = out43_
        return output

    @staticmethod
    def KdfCounterMode(config, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out44_: Wrappers.Result
        out44_ = KdfCtr.default__.KdfCounterMode(input)
        output = out44_
        return output

    @staticmethod
    def AesKdfCounterMode(config, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        output = Wrappers.Result_Failure(software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Implement")))
        return output

    @staticmethod
    def AESEncrypt(config, input):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput.default())()
        out45_: Wrappers.Result
        out45_ = AESEncryption.default__.AESEncrypt(input)
        output = out45_
        return output

    @staticmethod
    def AESDecrypt(config, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out46_: Wrappers.Result
        out46_ = AESEncryption.default__.AESDecrypt(input)
        output = out46_
        return output

    @staticmethod
    def GenerateRSAKeyPair(config, input):
        output: Wrappers.Result = None
        d_305_publicKey_: software_amazon_cryptography_primitives_internaldafny_types.RSAPublicKey
        d_306_privateKey_: software_amazon_cryptography_primitives_internaldafny_types.RSAPrivateKey
        out47_: software_amazon_cryptography_primitives_internaldafny_types.RSAPublicKey
        out48_: software_amazon_cryptography_primitives_internaldafny_types.RSAPrivateKey
        out47_, out48_ = RSAEncryption.default__.GenerateKeyPair((input).lengthBits)
        d_305_publicKey_ = out47_
        d_306_privateKey_ = out48_
        output = Wrappers.Result_Success(software_amazon_cryptography_primitives_internaldafny_types.GenerateRSAKeyPairOutput_GenerateRSAKeyPairOutput(d_305_publicKey_, d_306_privateKey_))
        return output

    @staticmethod
    def GetRSAKeyModulusLength(config, input):
        d_307_valueOrError0_ = RSAEncryption.default__.GetRSAKeyModulusLength((input).publicKey)
        if (d_307_valueOrError0_).IsFailure():
            return (d_307_valueOrError0_).PropagateFailure()
        elif True:
            d_308_length_ = (d_307_valueOrError0_).Extract()
            return Wrappers.Result_Success(software_amazon_cryptography_primitives_internaldafny_types.GetRSAKeyModulusLengthOutput_GetRSAKeyModulusLengthOutput(d_308_length_))

    @staticmethod
    def RSADecrypt(config, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out49_: Wrappers.Result
        out49_ = RSAEncryption.default__.Decrypt(input)
        output = out49_
        return output

    @staticmethod
    def RSAEncrypt(config, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out50_: Wrappers.Result
        out50_ = RSAEncryption.default__.Encrypt(input)
        output = out50_
        return output

    @staticmethod
    def GenerateECDSASignatureKey(config, input):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_primitives_internaldafny_types.GenerateECDSASignatureKeyOutput.default())()
        out51_: Wrappers.Result
        out51_ = Signature.default__.KeyGen(input)
        output = out51_
        return output

    @staticmethod
    def ECDSASign(config, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out52_: Wrappers.Result
        out52_ = Signature.ECDSA.Sign((input).signatureAlgorithm, (input).signingKey, (input).message)
        output = out52_
        return output

    @staticmethod
    def ECDSAVerify(config, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
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
        return isinstance(self, Config_Config)

class Config_Config(Config, NamedTuple('Config', [])):
    def __dafnystr__(self) -> str:
        return f'AwsCryptographyPrimitivesOperations.Config.Config'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Config_Config)
    def __hash__(self) -> int:
        return super().__hash__()

