import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_ as module_
import _dafny as _dafny
import System_ as System_
import standard_library.internaldafny.generated.Wrappers as Wrappers
import standard_library.internaldafny.generated.BoundedInts as BoundedInts
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import standard_library.internaldafny.generated.UTF8 as UTF8
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
import aws_cryptography_primitives.internaldafny.generated.AtomicPrimitives as AtomicPrimitives
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
import TestSignature as TestSignature
import TestAwsCryptographyPrimitivesHKDF as TestAwsCryptographyPrimitivesHKDF
import TestAwsCryptographyPrimitivesGenerateRandomBytes as TestAwsCryptographyPrimitivesGenerateRandomBytes
import ConstantTime as ConstantTime
import ConstantTimeTest as ConstantTimeTest
import TestHKDF__Rfc5869TestVectors as TestHKDF__Rfc5869TestVectors
import TestKDF as TestKDF
import TestKDFK__TestVectors as TestKDFK__TestVectors
import TestAwsCryptographyPrimitivesRSA as TestAwsCryptographyPrimitivesRSA
import TestAwsCryptographyPrimitivesAES as TestAwsCryptographyPrimitivesAES
import TestAwsCryptographyPrimitivesHMAC as TestAwsCryptographyPrimitivesHMAC
import TestAwsCryptographyPrimitivesDigest as TestAwsCryptographyPrimitivesDigest

# Module: TestAwsCryptographyPrimitivesHMacDigest

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DigestTests():
        d_132_client_: AtomicPrimitives.AtomicPrimitivesClient
        d_133_valueOrError0_: Wrappers.Result = None
        out28_: Wrappers.Result
        out28_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_133_valueOrError0_ = out28_
        if not(not((d_133_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestHMAC.dfy(14,18): " + _dafny.string_of(d_133_valueOrError0_))
        d_132_client_ = (d_133_valueOrError0_).Extract()
        default__.HmacSHA__256(d_132_client_)
        default__.HmacSHA__384(d_132_client_)
        default__.HmacSHA__512(d_132_client_)

    @staticmethod
    def HmacSHA__256(client):
        d_134___v0_: tuple
        d_135_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_135_valueOrError0_ = default__.BasicHMacTest(client, AwsCryptographyPrimitivesTypes.HMacInput_HMacInput(AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__256(), _dafny.Seq([1, 1, 1, 1]), _dafny.Seq([97, 115, 100, 102])), _dafny.Seq([93, 12, 86, 145, 123, 239, 169, 72, 195, 226, 204, 179, 103, 94, 195, 83, 134, 128, 226, 185, 184, 203, 98, 100, 115, 32, 7, 44, 172, 11, 81, 16]))
        if not(not((d_135_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestHMAC.dfy(26,13): " + _dafny.string_of(d_135_valueOrError0_))
        d_134___v0_ = (d_135_valueOrError0_).Extract()

    @staticmethod
    def HmacSHA__384(client):
        d_136___v1_: tuple
        d_137_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_137_valueOrError0_ = default__.BasicHMacTest(client, AwsCryptographyPrimitivesTypes.HMacInput_HMacInput(AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__384(), _dafny.Seq([1, 1, 1, 1]), _dafny.Seq([97, 115, 100, 102])), _dafny.Seq([219, 44, 51, 60, 217, 57, 186, 208, 8, 69, 115, 185, 190, 136, 136, 1, 69, 143, 151, 148, 7, 66, 149, 193, 16, 225, 51, 85, 92, 176, 139, 249, 56, 93, 189, 11, 150, 21, 135, 54, 153, 37, 76, 68, 70, 77, 154, 124]))
        if not(not((d_137_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestHMAC.dfy(47,13): " + _dafny.string_of(d_137_valueOrError0_))
        d_136___v1_ = (d_137_valueOrError0_).Extract()

    @staticmethod
    def HmacSHA__512(client):
        d_138___v2_: tuple
        d_139_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_139_valueOrError0_ = default__.BasicHMacTest(client, AwsCryptographyPrimitivesTypes.HMacInput_HMacInput(AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__512(), _dafny.Seq([1, 1, 1, 1]), _dafny.Seq([97, 115, 100, 102])), _dafny.Seq([49, 213, 21, 219, 23, 169, 195, 39, 177, 1, 15, 162, 233, 182, 208, 84, 226, 3, 27, 120, 75, 78, 85, 46, 220, 5, 166, 206, 79, 47, 25, 94, 88, 119, 211, 192, 148, 23, 252, 155, 98, 218, 97, 225, 38, 93, 83, 113, 139, 95, 101, 222, 154, 98, 244, 206, 88, 229, 6, 115, 226, 188, 152, 173]))
        if not(not((d_139_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestHMAC.dfy(69,13): " + _dafny.string_of(d_139_valueOrError0_))
        d_138___v2_ = (d_139_valueOrError0_).Extract()

    @staticmethod
    def BasicHMacTest(client, input, expectedDigest):
        d_140_valueOrError0_ = (client).HMac(input)
        if (d_140_valueOrError0_).IsFailure():
            return (d_140_valueOrError0_).PropagateFailure()
        elif True:
            d_141_output_ = (d_140_valueOrError0_).Extract()
            d_142_valueOrError1_ = Wrappers.default__.Need((len(d_141_output_)) == (Digest.default__.Length((input).digestAlgorithm)), AwsCryptographyPrimitivesTypes.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Error")))
            if (d_142_valueOrError1_).IsFailure():
                return (d_142_valueOrError1_).PropagateFailure()
            elif True:
                d_143_valueOrError2_ = Wrappers.default__.Need((d_141_output_) == (expectedDigest), AwsCryptographyPrimitivesTypes.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Error")))
                if (d_143_valueOrError2_).IsFailure():
                    return (d_143_valueOrError2_).PropagateFailure()
                elif True:
                    return Wrappers.Result_Success(())

