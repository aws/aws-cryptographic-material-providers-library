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
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesOperations as AwsCryptographyPrimitivesOperations

# Module: aws_cryptography_primitives.internaldafny.generated.AtomicPrimitives

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DefaultCryptoConfig():
        return AwsCryptographyPrimitivesTypes.CryptoConfig_CryptoConfig()

    @staticmethod
    def AtomicPrimitives(config):
        res: Wrappers.Result = None
        d_111_client_: AtomicPrimitivesClient
        nw0_ = AtomicPrimitivesClient()
        nw0_.ctor__(AwsCryptographyPrimitivesOperations.Config_Config())
        d_111_client_ = nw0_
        res = Wrappers.Result_Success(d_111_client_)
        return res
        return res

    @staticmethod
    def CreateSuccessOfClient(client):
        return Wrappers.Result_Success(client)

    @staticmethod
    def CreateFailureOfError(error):
        return Wrappers.Result_Failure(error)


class AtomicPrimitivesClient(AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient):
    def  __init__(self):
        self._config: AwsCryptographyPrimitivesOperations.Config = AwsCryptographyPrimitivesOperations.Config.default()()
        pass

    def __dafnystr__(self) -> str:
        return "AtomicPrimitives.AtomicPrimitivesClient"
    def ctor__(self, config):
        (self)._config = config

    def GenerateRandomBytes(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out36_: Wrappers.Result
        out36_ = AwsCryptographyPrimitivesOperations.default__.GenerateRandomBytes((self).config, input)
        output = out36_
        return output

    def Digest(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out37_: Wrappers.Result
        out37_ = AwsCryptographyPrimitivesOperations.default__.Digest((self).config, input)
        output = out37_
        return output

    def HMac(self, input):
        return AwsCryptographyPrimitivesOperations.default__.HMac((self).config, input)

    def HkdfExtract(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out38_: Wrappers.Result
        out38_ = AwsCryptographyPrimitivesOperations.default__.HkdfExtract((self).config, input)
        output = out38_
        return output

    def HkdfExpand(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out39_: Wrappers.Result
        out39_ = AwsCryptographyPrimitivesOperations.default__.HkdfExpand((self).config, input)
        output = out39_
        return output

    def Hkdf(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out40_: Wrappers.Result
        out40_ = AwsCryptographyPrimitivesOperations.default__.Hkdf((self).config, input)
        output = out40_
        return output

    def KdfCounterMode(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out41_: Wrappers.Result
        out41_ = AwsCryptographyPrimitivesOperations.default__.KdfCounterMode((self).config, input)
        output = out41_
        return output

    def AesKdfCounterMode(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out42_: Wrappers.Result
        out42_ = AwsCryptographyPrimitivesOperations.default__.AesKdfCounterMode((self).config, input)
        output = out42_
        return output

    def AESEncrypt(self, input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.AESEncryptOutput.default())()
        out43_: Wrappers.Result
        out43_ = AwsCryptographyPrimitivesOperations.default__.AESEncrypt((self).config, input)
        output = out43_
        return output

    def AESDecrypt(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out44_: Wrappers.Result
        out44_ = AwsCryptographyPrimitivesOperations.default__.AESDecrypt((self).config, input)
        output = out44_
        return output

    def GenerateRSAKeyPair(self, input):
        output: Wrappers.Result = None
        out45_: Wrappers.Result
        out45_ = AwsCryptographyPrimitivesOperations.default__.GenerateRSAKeyPair((self).config, input)
        output = out45_
        return output

    def GetRSAKeyModulusLength(self, input):
        return AwsCryptographyPrimitivesOperations.default__.GetRSAKeyModulusLength((self).config, input)

    def RSADecrypt(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out46_: Wrappers.Result
        out46_ = AwsCryptographyPrimitivesOperations.default__.RSADecrypt((self).config, input)
        output = out46_
        return output

    def RSAEncrypt(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out47_: Wrappers.Result
        out47_ = AwsCryptographyPrimitivesOperations.default__.RSAEncrypt((self).config, input)
        output = out47_
        return output

    def GenerateECDSASignatureKey(self, input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECDSASignatureKeyOutput.default())()
        out48_: Wrappers.Result
        out48_ = AwsCryptographyPrimitivesOperations.default__.GenerateECDSASignatureKey((self).config, input)
        output = out48_
        return output

    def ECDSASign(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out49_: Wrappers.Result
        out49_ = AwsCryptographyPrimitivesOperations.default__.ECDSASign((self).config, input)
        output = out49_
        return output

    def ECDSAVerify(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        out50_: Wrappers.Result
        out50_ = AwsCryptographyPrimitivesOperations.default__.ECDSAVerify((self).config, input)
        output = out50_
        return output

    @property
    def config(self):
        return self._config
