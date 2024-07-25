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
import aws_cryptography_primitives.internaldafny.generated.ECDH as ECDH
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

# Module: TestAwsCryptographyPrimitivesHMAC

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def HMACTests():
        default__.BasicHMACTest(AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__256(), _dafny.Seq([1, 2, 3, 4]), _dafny.Seq([97, 115, 100, 102]), _dafny.Seq([55, 107, 186, 241, 51, 255, 154, 169, 106, 133, 2, 248, 54, 230, 193, 147, 212, 179, 154, 66, 43, 52, 108, 181, 144, 152, 19, 101, 117, 99, 204, 134]))
        default__.BasicHMACTest(AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__384(), _dafny.Seq([1, 2, 3, 4]), _dafny.Seq([97, 115, 100, 102]), _dafny.Seq([90, 206, 234, 81, 173, 76, 235, 148, 203, 139, 195, 46, 251, 14, 97, 110, 146, 49, 147, 24, 240, 1, 17, 231, 58, 104, 146, 53, 144, 167, 11, 112, 7, 39, 122, 15, 58, 53, 144, 91, 16, 223, 51, 98, 30, 88, 23, 166]))
        default__.BasicHMACTest(AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__512(), _dafny.Seq([1, 2, 3, 4]), _dafny.Seq([97, 115, 100, 102]), _dafny.Seq([100, 23, 173, 215, 39, 67, 51, 165, 149, 53, 87, 84, 145, 58, 221, 155, 239, 182, 249, 134, 147, 191, 143, 224, 140, 165, 190, 221, 183, 15, 6, 102, 203, 77, 238, 64, 10, 138, 61, 64, 219, 79, 248, 249, 90, 102, 217, 188, 13, 2, 101, 96, 217, 242, 73, 254, 190, 217, 134, 33, 163, 137, 151, 183]))

    @staticmethod
    def BasicHMACTest(digestAlgorithm, key, message, expectedDigest):
        d_122_client_: AtomicPrimitives.AtomicPrimitivesClient
        d_123_valueOrError0_: Wrappers.Result = None
        out25_: Wrappers.Result
        out25_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_123_valueOrError0_ = out25_
        if not(not((d_123_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHMAC.dfy(66,18): " + _dafny.string_of(d_123_valueOrError0_))
        d_122_client_ = (d_123_valueOrError0_).Extract()
        d_124_input_: AwsCryptographyPrimitivesTypes.HMacInput
        d_124_input_ = AwsCryptographyPrimitivesTypes.HMacInput_HMacInput(digestAlgorithm, key, message)
        d_125_output_: _dafny.Seq
        d_126_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_126_valueOrError1_ = (d_122_client_).HMac(d_124_input_)
        if not(not((d_126_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHMAC.dfy(74,18): " + _dafny.string_of(d_126_valueOrError1_))
        d_125_output_ = (d_126_valueOrError1_).Extract()
        if not((len(d_125_output_)) == (Digest.default__.Length(digestAlgorithm))):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHMAC.dfy(75,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_125_output_) == (expectedDigest)):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHMAC.dfy(76,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

