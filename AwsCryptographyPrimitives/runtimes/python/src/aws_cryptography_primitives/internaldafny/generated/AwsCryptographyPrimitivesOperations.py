import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptography_primitives.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import standard_library.internaldafny.generated.Wrappers as Wrappers
import standard_library.internaldafny.generated.Relations as Relations
import standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import standard_library.internaldafny.generated.Math as Math
import standard_library.internaldafny.generated.Seq as Seq
import standard_library.internaldafny.generated.BoundedInts as BoundedInts
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
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import standard_library.internaldafny.generated.UUID as UUID
import standard_library.internaldafny.generated.UTF8 as UTF8
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

# Module: aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesOperations

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
        output = Wrappers.Result_Failure(AwsCryptographyPrimitivesTypes.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Implement")))
        return output

    @staticmethod
    def AESEncrypt(config, input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.AESEncryptOutput.default())()
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
        d_107_publicKey_: AwsCryptographyPrimitivesTypes.RSAPublicKey
        d_108_privateKey_: AwsCryptographyPrimitivesTypes.RSAPrivateKey
        out30_: AwsCryptographyPrimitivesTypes.RSAPublicKey
        out31_: AwsCryptographyPrimitivesTypes.RSAPrivateKey
        out30_, out31_ = RSAEncryption.default__.GenerateKeyPair((input).lengthBits)
        d_107_publicKey_ = out30_
        d_108_privateKey_ = out31_
        output = Wrappers.Result_Success(AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput_GenerateRSAKeyPairOutput(d_107_publicKey_, d_108_privateKey_))
        return output

    @staticmethod
    def GetRSAKeyModulusLength(config, input):
        d_109_valueOrError0_ = RSAEncryption.default__.GetRSAKeyModulusLength((input).publicKey)
        if (d_109_valueOrError0_).IsFailure():
            return (d_109_valueOrError0_).PropagateFailure()
        elif True:
            d_110_length_ = (d_109_valueOrError0_).Extract()
            return Wrappers.Result_Success(AwsCryptographyPrimitivesTypes.GetRSAKeyModulusLengthOutput_GetRSAKeyModulusLengthOutput(d_110_length_))

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
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECDSASignatureKeyOutput.default())()
        out34_: Wrappers.Result
        out34_ = Signature.default__.KeyGen(input)
        output = out34_
        return output

    @staticmethod
    def ECDSASign(config, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out35_: Wrappers.Result
        out35_ = ECDSA.Sign((input).signatureAlgorithm, (input).signingKey, (input).message)
        output = out35_
        return output

    @staticmethod
    def ECDSAVerify(config, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        output = ECDSA_Verify((input).signatureAlgorithm, (input).verificationKey, (input).message, (input).signature)
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

