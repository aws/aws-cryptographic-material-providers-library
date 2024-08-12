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

# Module: RSAEncryption

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def GenerateKeyPair(lengthBits):
        publicKey: AwsCryptographyPrimitivesTypes.RSAPublicKey = None
        privateKey: AwsCryptographyPrimitivesTypes.RSAPrivateKey = None
        d_99_pemPublic_: _dafny.Seq
        d_100_pemPrivate_: _dafny.Seq
        out18_: _dafny.Seq
        out19_: _dafny.Seq
        out18_, out19_ = RSAEncryption.RSA.GenerateKeyPairExtern(lengthBits)
        d_99_pemPublic_ = out18_
        d_100_pemPrivate_ = out19_
        privateKey = AwsCryptographyPrimitivesTypes.RSAPrivateKey_RSAPrivateKey(lengthBits, d_100_pemPrivate_)
        publicKey = AwsCryptographyPrimitivesTypes.RSAPublicKey_RSAPublicKey(lengthBits, d_99_pemPublic_)
        return publicKey, privateKey

    @staticmethod
    def GetRSAKeyModulusLength(publicKey):
        d_101_valueOrError0_ = RSAEncryption.RSA_GetRSAKeyModulusLengthExtern(publicKey)
        if (d_101_valueOrError0_).IsFailure():
            return (d_101_valueOrError0_).PropagateFailure()
        elif True:
            d_102_length_ = (d_101_valueOrError0_).Extract()
            d_103_valueOrError1_ = Wrappers.default__.Need(((81) <= (d_102_length_)) and ((d_102_length_) < (StandardLibrary_UInt.default__.INT32__MAX__LIMIT)), AwsCryptographyPrimitivesTypes.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Unsupported length for RSA modulus.")))
            if (d_103_valueOrError1_).IsFailure():
                return (d_103_valueOrError1_).PropagateFailure()
            elif True:
                return Wrappers.Result_Success(d_102_length_)

    @staticmethod
    def Decrypt(input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_104_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_104_valueOrError0_ = Wrappers.default__.Need(((0) < (len((input).privateKey))) and ((0) < (len((input).cipherText))), AwsCryptographyPrimitivesTypes.Error_AwsCryptographicPrimitivesError(_dafny.Seq("")))
        if (d_104_valueOrError0_).IsFailure():
            output = (d_104_valueOrError0_).PropagateFailure()
            return output
        out20_: Wrappers.Result
        out20_ = RSAEncryption.RSA.DecryptExtern((input).padding, (input).privateKey, (input).cipherText)
        output = out20_
        return output

    @staticmethod
    def Encrypt(input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_105_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_105_valueOrError0_ = Wrappers.default__.Need(((0) < (len((input).publicKey))) and ((0) < (len((input).plaintext))), AwsCryptographyPrimitivesTypes.Error_AwsCryptographicPrimitivesError(_dafny.Seq("")))
        if (d_105_valueOrError0_).IsFailure():
            output = (d_105_valueOrError0_).PropagateFailure()
            return output
        out21_: Wrappers.Result
        out21_ = RSAEncryption.RSA.EncryptExtern((input).padding, (input).publicKey, (input).plaintext)
        output = out21_
        return output

    @staticmethod
    def CreateGetRSAKeyModulusLengthExternSuccess(output):
        return Wrappers.Result_Success(output)

    @staticmethod
    def CreateGetRSAKeyModulusLengthExternFailure(error):
        return Wrappers.Result_Failure(error)

    @staticmethod
    def CreateBytesSuccess(bytes):
        return Wrappers.Result_Success(bytes)

    @staticmethod
    def CreateBytesFailure(error):
        return Wrappers.Result_Failure(error)

