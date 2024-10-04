import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptography_primitives.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import smithy_dafny_standard_library.internaldafny.generated.Relations as Relations
import smithy_dafny_standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import smithy_dafny_standard_library.internaldafny.generated.Math as Math
import smithy_dafny_standard_library.internaldafny.generated.Seq as Seq
import smithy_dafny_standard_library.internaldafny.generated.BoundedInts as BoundedInts
import smithy_dafny_standard_library.internaldafny.generated.Unicode as Unicode
import smithy_dafny_standard_library.internaldafny.generated.Functions as Functions
import smithy_dafny_standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import smithy_dafny_standard_library.internaldafny.generated.FileIO as FileIO
import smithy_dafny_standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import smithy_dafny_standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.MulInternals as MulInternals
import smithy_dafny_standard_library.internaldafny.generated.Mul as Mul
import smithy_dafny_standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.ModInternals as ModInternals
import smithy_dafny_standard_library.internaldafny.generated.DivInternals as DivInternals
import smithy_dafny_standard_library.internaldafny.generated.DivMod as DivMod
import smithy_dafny_standard_library.internaldafny.generated.Power as Power
import smithy_dafny_standard_library.internaldafny.generated.Logarithm as Logarithm
import smithy_dafny_standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import smithy_dafny_standard_library.internaldafny.generated.UUID as UUID
import smithy_dafny_standard_library.internaldafny.generated.UTF8 as UTF8
import smithy_dafny_standard_library.internaldafny.generated.Time as Time
import smithy_dafny_standard_library.internaldafny.generated.Streams as Streams
import smithy_dafny_standard_library.internaldafny.generated.Sorting as Sorting
import smithy_dafny_standard_library.internaldafny.generated.SortedSets as SortedSets
import smithy_dafny_standard_library.internaldafny.generated.HexStrings as HexStrings
import smithy_dafny_standard_library.internaldafny.generated.GetOpt as GetOpt
import smithy_dafny_standard_library.internaldafny.generated.FloatCompare as FloatCompare
import smithy_dafny_standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import smithy_dafny_standard_library.internaldafny.generated.Base64 as Base64
import smithy_dafny_standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import smithy_dafny_standard_library.internaldafny.generated.Actions as Actions
import smithy_dafny_standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
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

# Module: ECDH

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def GenerateEccKeyPair(input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput.default())()
        d_0_valueOrError0_: Wrappers.Result = Wrappers.Result.default(EccKeyPair.default())()
        out0_: Wrappers.Result
        out0_ = ECDH.KeyGeneration.GenerateKeyPair((input).eccCurve)
        d_0_valueOrError0_ = out0_
        if (d_0_valueOrError0_).IsFailure():
            output = (d_0_valueOrError0_).PropagateFailure()
            return output
        d_1_keyPair_: EccKeyPair
        d_1_keyPair_ = (d_0_valueOrError0_).Extract()
        output = Wrappers.Result_Success(AwsCryptographyPrimitivesTypes.GenerateECCKeyPairOutput_GenerateECCKeyPairOutput((input).eccCurve, AwsCryptographyPrimitivesTypes.ECCPrivateKey_ECCPrivateKey((d_1_keyPair_).privateKey), AwsCryptographyPrimitivesTypes.ECCPublicKey_ECCPublicKey((d_1_keyPair_).publicKey)))
        return output
        return output

    @staticmethod
    def GetPublicKeyFromPrivate(input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GetPublicKeyFromPrivateKeyOutput.default())()
        d_0_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out0_: Wrappers.Result
        out0_ = ECDH.ECCUtils.GetPublicKey((input).eccCurve, (input).privateKey)
        d_0_valueOrError0_ = out0_
        if (d_0_valueOrError0_).IsFailure():
            output = (d_0_valueOrError0_).PropagateFailure()
            return output
        d_1_publicKey_: _dafny.Seq
        d_1_publicKey_ = (d_0_valueOrError0_).Extract()
        output = Wrappers.Result_Success(AwsCryptographyPrimitivesTypes.GetPublicKeyFromPrivateKeyOutput_GetPublicKeyFromPrivateKeyOutput((input).eccCurve, (input).privateKey, d_1_publicKey_))
        return output
        return output

    @staticmethod
    def ValidatePublicKey(input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.ValidatePublicKeyOutput.default())()
        d_0_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        out0_: Wrappers.Result
        out0_ = ECDH.ECCUtils.ValidatePublicKey((input).eccCurve, (input).publicKey)
        d_0_valueOrError0_ = out0_
        if (d_0_valueOrError0_).IsFailure():
            output = (d_0_valueOrError0_).PropagateFailure()
            return output
        d_1_result_: bool
        d_1_result_ = (d_0_valueOrError0_).Extract()
        output = Wrappers.Result_Success(AwsCryptographyPrimitivesTypes.ValidatePublicKeyOutput_ValidatePublicKeyOutput(d_1_result_))
        return output
        return output

    @staticmethod
    def DeriveSharedSecret(input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput.default())()
        d_0_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out0_: Wrappers.Result
        out0_ = ECDH.DeriveSharedSecret.CalculateSharedSecret((input).eccCurve, (input).privateKey, (input).publicKey)
        d_0_valueOrError0_ = out0_
        if (d_0_valueOrError0_).IsFailure():
            output = (d_0_valueOrError0_).PropagateFailure()
            return output
        d_1_derivedSharedSecret_: _dafny.Seq
        d_1_derivedSharedSecret_ = (d_0_valueOrError0_).Extract()
        output = Wrappers.Result_Success(AwsCryptographyPrimitivesTypes.DeriveSharedSecretOutput_DeriveSharedSecretOutput(d_1_derivedSharedSecret_))
        return output
        return output

    @staticmethod
    def CompressPublicKey(input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.CompressPublicKeyOutput.default())()
        d_0_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out0_: Wrappers.Result
        out0_ = ECDH.ECCUtils.CompressPublicKey(((input).publicKey).der, (input).eccCurve)
        d_0_valueOrError0_ = out0_
        if (d_0_valueOrError0_).IsFailure():
            output = (d_0_valueOrError0_).PropagateFailure()
            return output
        d_1_compressedPublicKey_: _dafny.Seq
        d_1_compressedPublicKey_ = (d_0_valueOrError0_).Extract()
        output = Wrappers.Result_Success(AwsCryptographyPrimitivesTypes.CompressPublicKeyOutput_CompressPublicKeyOutput(d_1_compressedPublicKey_))
        return output
        return output

    @staticmethod
    def DecompressPublicKey(input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.DecompressPublicKeyOutput.default())()
        d_0_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out0_: Wrappers.Result
        out0_ = ECDH.ECCUtils.DecompressPublicKey((input).compressedPublicKey, (input).eccCurve)
        d_0_valueOrError0_ = out0_
        if (d_0_valueOrError0_).IsFailure():
            output = (d_0_valueOrError0_).PropagateFailure()
            return output
        d_1_decompressedPublicKey_: _dafny.Seq
        d_1_decompressedPublicKey_ = (d_0_valueOrError0_).Extract()
        output = Wrappers.Result_Success(AwsCryptographyPrimitivesTypes.DecompressPublicKeyOutput_DecompressPublicKeyOutput(AwsCryptographyPrimitivesTypes.ECCPublicKey_ECCPublicKey(d_1_decompressedPublicKey_)))
        return output
        return output

    @staticmethod
    def ParsePublicKey(input):
        output: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.ParsePublicKeyOutput.default())()
        d_0_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out0_: Wrappers.Result
        out0_ = ECDH.ECCUtils.ParsePublicKey((input).publicKey)
        d_0_valueOrError0_ = out0_
        if (d_0_valueOrError0_).IsFailure():
            output = (d_0_valueOrError0_).PropagateFailure()
            return output
        d_1_derPublicKey_: _dafny.Seq
        d_1_derPublicKey_ = (d_0_valueOrError0_).Extract()
        output = Wrappers.Result_Success(AwsCryptographyPrimitivesTypes.ParsePublicKeyOutput_ParsePublicKeyOutput(AwsCryptographyPrimitivesTypes.ECCPublicKey_ECCPublicKey(d_1_derPublicKey_)))
        return output
        return output

    @staticmethod
    def CreateExternEccKeyGenSuccess(output):
        return Wrappers.Result_Success(output)

    @staticmethod
    def CreateExternEccKeyGenFailure(error):
        return Wrappers.Result_Failure(error)

    @staticmethod
    def CreateExternGetPublicKeyFromPrivateSuccess(output):
        return Wrappers.Result_Success(output)

    @staticmethod
    def CreateExternGetPublicKeyFromPrivateError(error):
        return Wrappers.Result_Failure(error)

    @staticmethod
    def CreateExternValidatePublicKeySuccess(output):
        return Wrappers.Result_Success(output)

    @staticmethod
    def CreateExternValidatePublicKeyError(error):
        return Wrappers.Result_Failure(error)

    @staticmethod
    def CreateExternDerivesharedSecretSuccess(output):
        return Wrappers.Result_Success(output)

    @staticmethod
    def CreateExternDerivesharedSecretError(error):
        return Wrappers.Result_Failure(error)

    @staticmethod
    def CreateExternCompressPublicKeyError(error):
        return Wrappers.Result_Failure(error)

    @staticmethod
    def CreateExternCompressPublicKeySuccess(output):
        return Wrappers.Result_Success(output)

    @staticmethod
    def CreateExternDecompressPublicKeyError(error):
        return Wrappers.Result_Failure(error)

    @staticmethod
    def CreateExternDecompressPublicKeySuccess(output):
        return Wrappers.Result_Success(output)

    @staticmethod
    def CreateExternParsePublicKeyError(error):
        return Wrappers.Result_Failure(error)

    @staticmethod
    def CreateExternParsePublicKeySuccess(output):
        return Wrappers.Result_Success(output)

    @staticmethod
    def CreateGetInfinityPublicKeyError(error):
        return Wrappers.Result_Failure(error)

    @staticmethod
    def CreateGetInfinityPublicKeySuccess(output):
        return Wrappers.Result_Success(output)

    @staticmethod
    def CreateGetOutOfBoundsPublicKeyError(error):
        return Wrappers.Result_Failure(error)

    @staticmethod
    def CreateGetOutOfBoundsPublicKeySuccess(output):
        return Wrappers.Result_Success(output)


class EccKeyPair:
    @classmethod
    def default(cls, ):
        return lambda: EccKeyPair_EccKeyPair(_dafny.Seq({}), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_EccKeyPair(self) -> bool:
        return isinstance(self, EccKeyPair_EccKeyPair)

class EccKeyPair_EccKeyPair(EccKeyPair, NamedTuple('EccKeyPair', [('privateKey', Any), ('publicKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'ECDH.EccKeyPair.EccKeyPair({_dafny.string_of(self.privateKey)}, {_dafny.string_of(self.publicKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, EccKeyPair_EccKeyPair) and self.privateKey == __o.privateKey and self.publicKey == __o.publicKey
    def __hash__(self) -> int:
        return super().__hash__()

