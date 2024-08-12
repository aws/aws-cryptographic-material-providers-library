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
import aws_cryptography_primitives.internaldafny.generated.Aws_Cryptography_Primitives as Aws_Cryptography_Primitives
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
import TestAwsCryptographyPrimitivesHMacDigest as TestAwsCryptographyPrimitivesHMacDigest
import TestECDH as TestECDH

# Module: TestAwsCryptographyPrimitivesAesKdfCtr

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def AesKdfCtrTests():
        d_264_key_: _dafny.Seq
        d_264_key_ = _dafny.Seq([138, 39, 30, 72, 206, 182, 214, 144, 245, 34, 28, 219, 204, 175, 198, 23, 132, 234, 125, 246, 130, 54, 251, 60, 137, 120, 166, 245, 0, 150, 79, 107])
        d_265_nonce_: _dafny.Seq
        d_265_nonce_ = _dafny.Seq([66, 32, 73, 11, 207, 79, 97, 80, 11, 22, 236, 247, 42, 6, 222, 165])
        d_266_goal_: _dafny.Seq
        d_266_goal_ = _dafny.Seq([143, 128, 174, 191, 9, 171, 140, 22, 40, 143, 11, 239, 249, 101, 61, 120, 176, 23, 233, 210, 125, 72, 114, 70, 209, 170, 206, 96, 24, 112, 215, 169, 100, 136, 162, 231, 208, 24, 135, 121, 223, 13, 239, 180])
        d_267_result_: _dafny.Seq
        d_268_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_268_valueOrError0_ = AesKdfCtr.default__.AesKdfCtrStream(d_265_nonce_, d_264_key_, 44)
        if not(not((d_268_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestAesKdfCtr.dfy(18,18): " + _dafny.string_of(d_268_valueOrError0_))
        d_267_result_ = (d_268_valueOrError0_).Extract()
        if not((len(d_267_result_)) == (44)):
            raise _dafny.HaltException("test/TestAesKdfCtr.dfy(19,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_266_goal_) == (d_267_result_)):
            raise _dafny.HaltException("test/TestAesKdfCtr.dfy(20,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_264_key_ = _dafny.Seq([212, 191, 10, 32, 13, 55, 22, 101, 189, 182, 186, 119, 202, 16, 175, 49, 103, 82, 87, 190, 13, 142, 103, 201, 98, 84, 228, 47, 142, 96, 61, 167])
        d_265_nonce_ = _dafny.Seq([135, 1, 132, 66, 198, 216, 26, 105, 47, 97, 246, 192, 186, 187, 54, 129])
        d_266_goal_ = _dafny.Seq([11, 154, 37, 42, 116, 143, 238, 68, 62, 135, 225, 71, 98, 224, 135, 18])
        d_269_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_269_valueOrError1_ = AesKdfCtr.default__.AesKdfCtrStream(d_265_nonce_, d_264_key_, 16)
        if not(not((d_269_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestAesKdfCtr.dfy(25,14): " + _dafny.string_of(d_269_valueOrError1_))
        d_267_result_ = (d_269_valueOrError1_).Extract()
        if not((len(d_267_result_)) == (16)):
            raise _dafny.HaltException("test/TestAesKdfCtr.dfy(26,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_266_goal_) == (d_267_result_)):
            raise _dafny.HaltException("test/TestAesKdfCtr.dfy(27,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_264_key_ = _dafny.Seq([106, 72, 42, 47, 58, 213, 111, 196, 126, 37, 46, 203, 150, 153, 188, 53, 32, 194, 159, 196, 221, 90, 124, 70, 45, 252, 99, 98, 42, 68, 94, 19])
        d_265_nonce_ = _dafny.Seq([13, 247, 32, 159, 220, 254, 69, 218, 42, 110, 159, 42, 209, 244, 79, 232])
        d_266_goal_ = _dafny.Seq([150, 218, 139, 126, 166, 233, 178, 123, 229, 210, 40, 218, 141, 26, 127, 208, 124, 197, 212, 69, 251, 71, 73, 90, 47, 134, 46, 7, 215, 208, 194, 180, 174, 110, 1, 57, 16, 37, 16, 235, 93, 138, 25, 180, 85, 16, 229, 165, 238, 36, 56, 131, 247, 31, 64, 23, 249, 67, 153, 94, 23, 243, 69, 11])
        d_270_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_270_valueOrError2_ = AesKdfCtr.default__.AesKdfCtrStream(d_265_nonce_, d_264_key_, 64)
        if not(not((d_270_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("test/TestAesKdfCtr.dfy(32,14): " + _dafny.string_of(d_270_valueOrError2_))
        d_267_result_ = (d_270_valueOrError2_).Extract()
        if not((len(d_267_result_)) == (64)):
            raise _dafny.HaltException("test/TestAesKdfCtr.dfy(33,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_266_goal_) == (d_267_result_)):
            raise _dafny.HaltException("test/TestAesKdfCtr.dfy(34,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

