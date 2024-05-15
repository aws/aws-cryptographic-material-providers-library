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

# Module: aws_cryptography_primitives.internaldafny.generated.Signature

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def SignatureLength(signatureAlgorithm):
        source2_ = signatureAlgorithm
        if source2_.is_ECDSA__P384:
            return 103
        elif True:
            return 71

    @staticmethod
    def FieldSize(signatureAlgorithm):
        source3_ = signatureAlgorithm
        if source3_.is_ECDSA__P384:
            return 49
        elif True:
            return 33

    @staticmethod
    def KeyGen(input):
        res: Wrappers.Result = Wrappers.Result.default(AwsCryptographyPrimitivesTypes.GenerateECDSASignatureKeyOutput.default())()
        d_75_sigKeyPair_: SignatureKeyPair
        d_76_valueOrError0_: Wrappers.Result = Wrappers.Result.default(SignatureKeyPair.default())()
        out14_: Wrappers.Result
        out14_ = Signature.ECDSA.ExternKeyGen((input).signatureAlgorithm)
        d_76_valueOrError0_ = out14_
        if (d_76_valueOrError0_).IsFailure():
            res = (d_76_valueOrError0_).PropagateFailure()
            return res
        d_75_sigKeyPair_ = (d_76_valueOrError0_).Extract()
        d_77_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_77_valueOrError1_ = Wrappers.default__.Need((len((d_75_sigKeyPair_).verificationKey)) == (default__.FieldSize((input).signatureAlgorithm)), AwsCryptographyPrimitivesTypes.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Incorrect verification-key length from ExternKeyGen.")))
        if (d_77_valueOrError1_).IsFailure():
            res = (d_77_valueOrError1_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(AwsCryptographyPrimitivesTypes.GenerateECDSASignatureKeyOutput_GenerateECDSASignatureKeyOutput((input).signatureAlgorithm, (d_75_sigKeyPair_).verificationKey, (d_75_sigKeyPair_).signingKey))
        return res
        return res

    @staticmethod
    def CreateExternKeyGenSuccess(output):
        return Wrappers.Result_Success(output)

    @staticmethod
    def CreateExternKeyGenFailure(error):
        return Wrappers.Result_Failure(error)

    @staticmethod
    def CreateSignSuccess(bytes):
        return Wrappers.Result_Success(bytes)

    @staticmethod
    def CreateSignFailure(error):
        return Wrappers.Result_Failure(error)

    @staticmethod
    def CreateVerifySuccess(b):
        return Wrappers.Result_Success(b)

    @staticmethod
    def CreateVerifyFailure(error):
        return Wrappers.Result_Failure(error)


class SignatureKeyPair:
    @classmethod
    def default(cls, ):
        return lambda: SignatureKeyPair_SignatureKeyPair(_dafny.Seq({}), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_SignatureKeyPair(self) -> bool:
        return isinstance(self, SignatureKeyPair_SignatureKeyPair)

class SignatureKeyPair_SignatureKeyPair(SignatureKeyPair, NamedTuple('SignatureKeyPair', [('verificationKey', Any), ('signingKey', Any)])):
    def __dafnystr__(self) -> str:
        return f'Signature.SignatureKeyPair.SignatureKeyPair({_dafny.string_of(self.verificationKey)}, {_dafny.string_of(self.signingKey)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, SignatureKeyPair_SignatureKeyPair) and self.verificationKey == __o.verificationKey and self.signingKey == __o.signingKey
    def __hash__(self) -> int:
        return super().__hash__()

