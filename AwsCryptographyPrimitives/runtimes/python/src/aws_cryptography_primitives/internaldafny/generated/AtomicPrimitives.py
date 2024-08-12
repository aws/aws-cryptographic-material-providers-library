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
import aws_cryptography_primitives.internaldafny.generated.ECDH as ECDH
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesOperations as AwsCryptographyPrimitivesOperations

# Module: AtomicPrimitives

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DefaultCryptoConfig():
        return AwsCryptographyPrimitivesTypes.CryptoConfig_CryptoConfig()

    @staticmethod
    def AtomicPrimitives(config):
        res: Wrappers.Result = None
        d_124_client_: AtomicPrimitivesClient
        nw0_ = AtomicPrimitivesClient()
        nw0_.ctor__(AwsCryptographyPrimitivesOperations.Config_Config())
        d_124_client_ = nw0_
        res = Wrappers.Result_Success(d_124_client_)
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
        out50_: Wrappers.Result
        out50_ = AwsCryptographyPrimitivesOperations.default__.GenerateRandomBytes((self).config, input)
        output = out50_
        return output

    def Digest(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out51_: Wrappers.Result
        out51_ = AwsCryptographyPrimitivesOperations.default__.Digest((self).config, input)
        output = out51_
        return output

    def HMac(self, input):
        return AwsCryptographyPrimitivesOperations.default__.HMac((self).config, input)

    def HkdfExtract(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out52_: Wrappers.Result
        out52_ = AwsCryptographyPrimitivesOperations.default__.HkdfExtract((self).config, input)
        output = out52_
        return output

    def HkdfExpand(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out53_: Wrappers.Result
        out53_ = AwsCryptographyPrimitivesOperations.default__.HkdfExpand((self).config, input)
        output = out53_
        return output

    def Hkdf(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out54_: Wrappers.Result
        out54_ = AwsCryptographyPrimitivesOperations.default__.Hkdf((self).config, input)
        output = out54_
        return output

    def KdfCounterMode(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out55_: Wrappers.Result
        out55_ = AwsCryptographyPrimitivesOperations.default__.KdfCounterMode((self).config, input)
        output = out55_
        return output

    def AesKdfCounterMode(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out56_: Wrappers.Result
        out56_ = AwsCryptographyPrimitivesOperations.default__.AesKdfCounterMode((self).config, input)
        output = out56_
        return output

    def AESEncrypt(self, input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.AESEncryptOutput.default())()
        out57_: Wrappers.Result
        out57_ = AwsCryptographyPrimitivesOperations.default__.AESEncrypt((self).config, input)
        output = out57_
        return output

    def AESDecrypt(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out58_: Wrappers.Result
        out58_ = AwsCryptographyPrimitivesOperations.default__.AESDecrypt((self).config, input)
        output = out58_
        return output

    def GenerateRSAKeyPair(self, input):
        output: Wrappers.Result = None
        out59_: Wrappers.Result
        out59_ = AwsCryptographyPrimitivesOperations.default__.GenerateRSAKeyPair((self).config, input)
        output = out59_
        return output

    def GetRSAKeyModulusLength(self, input):
        return AwsCryptographyPrimitivesOperations.default__.GetRSAKeyModulusLength((self).config, input)

    def RSADecrypt(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out60_: Wrappers.Result
        out60_ = AwsCryptographyPrimitivesOperations.default__.RSADecrypt((self).config, input)
        output = out60_
        return output

    def RSAEncrypt(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out61_: Wrappers.Result
        out61_ = AwsCryptographyPrimitivesOperations.default__.RSAEncrypt((self).config, input)
        output = out61_
        return output

    def GenerateECDSASignatureKey(self, input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECDSASignatureKeyOutput.default())()
        out62_: Wrappers.Result
        out62_ = AwsCryptographyPrimitivesOperations.default__.GenerateECDSASignatureKey((self).config, input)
        output = out62_
        return output

    def ECDSASign(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out63_: Wrappers.Result
        out63_ = AwsCryptographyPrimitivesOperations.default__.ECDSASign((self).config, input)
        output = out63_
        return output

    def ECDSAVerify(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        out64_: Wrappers.Result
        out64_ = AwsCryptographyPrimitivesOperations.default__.ECDSAVerify((self).config, input)
        output = out64_
        return output

    def GenerateECCKeyPair(self, input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
        out65_: Wrappers.Result
        out65_ = AwsCryptographyPrimitivesOperations.default__.GenerateECCKeyPair((self).config, input)
        output = out65_
        return output

    def GetPublicKeyFromPrivateKey(self, input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GetPublicKeyFromPrivateKeyOutput.default())()
        out66_: Wrappers.Result
        out66_ = AwsCryptographyPrimitivesOperations.default__.GetPublicKeyFromPrivateKey((self).config, input)
        output = out66_
        return output

    def ValidatePublicKey(self, input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.ValidatePublicKeyOutput.default())()
        out67_: Wrappers.Result
        out67_ = AwsCryptographyPrimitivesOperations.default__.ValidatePublicKey((self).config, input)
        output = out67_
        return output

    def DeriveSharedSecret(self, input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput.default())()
        out68_: Wrappers.Result
        out68_ = AwsCryptographyPrimitivesOperations.default__.DeriveSharedSecret((self).config, input)
        output = out68_
        return output

    def CompressPublicKey(self, input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.CompressPublicKeyOutput.default())()
        out69_: Wrappers.Result
        out69_ = AwsCryptographyPrimitivesOperations.default__.CompressPublicKey((self).config, input)
        output = out69_
        return output

    def DecompressPublicKey(self, input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.DecompressPublicKeyOutput.default())()
        out70_: Wrappers.Result
        out70_ = AwsCryptographyPrimitivesOperations.default__.DecompressPublicKey((self).config, input)
        output = out70_
        return output

    def ParsePublicKey(self, input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.ParsePublicKeyOutput.default())()
        out71_: Wrappers.Result
        out71_ = AwsCryptographyPrimitivesOperations.default__.ParsePublicKey((self).config, input)
        output = out71_
        return output

    @property
    def config(self):
        return self._config
