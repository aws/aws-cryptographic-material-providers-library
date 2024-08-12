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

# Module: TestKDFK__TestVectors

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def ExpectInternalTestVectors():
        hi1_ = len(default__.rawTestVectors)
        for d_56_i_ in range(0, hi1_):
            default__.ExpectRawDeriveTestVector((default__.rawTestVectors)[d_56_i_])
        hi2_ = len(default__.testVectors)
        for d_57_i_ in range(0, hi2_):
            default__.ExpectTestVector((default__.testVectors)[d_57_i_])

    @staticmethod
    def ExpectRawDeriveTestVector(vector):
        let_tmp_rhs1_ = vector
        d_58_name_ = let_tmp_rhs1_.name
        d_59_hash_ = let_tmp_rhs1_.hash
        d_60_IKM_ = let_tmp_rhs1_.IKM
        d_61_info_ = let_tmp_rhs1_.info
        d_62_L_ = let_tmp_rhs1_.L
        d_63_OKM_ = let_tmp_rhs1_.OKM
        _dafny.print(_dafny.string_of((d_58_name_) + (_dafny.Seq("\n"))))
        if not((((((len(d_60_IKM_)) == (32)) or ((len(d_60_IKM_)) == (48))) and ((d_62_L_) > (0))) and (((4) + (len(d_61_info_))) < (StandardLibrary_UInt.default__.INT32__MAX__LIMIT))) and (((d_59_hash_) == (AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__256())) or ((d_59_hash_) == (AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__384())))):
            raise _dafny.HaltException("test/TestKDF_TestVectors.dfy(364,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((((d_62_L_) + (Digest.default__.Length(AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__256()))) < ((StandardLibrary_UInt.default__.INT32__MAX__LIMIT) - (1))) and (((d_62_L_) + (Digest.default__.Length(AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__384()))) < ((StandardLibrary_UInt.default__.INT32__MAX__LIMIT) - (1)))):
            raise _dafny.HaltException("test/TestKDF_TestVectors.dfy(365,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        TestKDF.default__.KdfRawDeriveTest(d_60_IKM_, d_61_info_, d_62_L_, d_63_OKM_, d_59_hash_)

    @staticmethod
    def ExpectTestVector(vector):
        let_tmp_rhs2_ = vector
        d_64_name_ = let_tmp_rhs2_.name
        d_65_hash_ = let_tmp_rhs2_.hash
        d_66_IKM_ = let_tmp_rhs2_.IKM
        d_67_info_ = let_tmp_rhs2_.info
        d_68_purpose_ = let_tmp_rhs2_.purpose
        d_69_L_ = let_tmp_rhs2_.L
        d_70_OKM_ = let_tmp_rhs2_.OKM
        _dafny.print(_dafny.string_of((d_64_name_) + (_dafny.Seq("\n"))))
        TestKDF.default__.KdfTest(AwsCryptographyPrimitivesTypes.KdfCtrInput_KdfCtrInput(d_65_hash_, d_66_IKM_, d_69_L_, Wrappers.Option_Some(d_68_purpose_), Wrappers.Option_Some(d_67_info_)), d_70_OKM_)

    @_dafny.classproperty
    def b1(instance):
        return InternalTestVector_InternalTestVector(_dafny.Seq("B.1  Test Case 1"), AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__256(), _dafny.Seq([226, 4, 214, 212, 102, 170, 213, 7, 255, 175, 109, 109, 171, 10, 91, 38, 21, 44, 158, 33, 231, 100, 55, 4, 100, 227, 96, 200, 251, 199, 101, 198]), _dafny.Seq([123, 3, 185, 141, 159, 148, 184, 153, 229, 145, 243, 239, 38, 75, 113, 177, 147, 251, 167, 4, 60, 126, 149, 60, 222, 35, 188, 83, 132, 188, 26, 98, 147, 88, 1, 21, 250, 227, 73, 95, 216, 69, 218, 219, 208, 43, 214, 69, 92, 244, 141, 15, 98, 179, 62, 98, 54, 74, 58, 128]), 32, _dafny.Seq([119, 13, 250, 182, 166, 164, 164, 190, 224, 37, 127, 243, 53, 33, 63, 120, 216, 40, 123, 79, 213, 55, 213, 193, 255, 250, 149, 105, 16, 231, 199, 121]))
    @_dafny.classproperty
    def b2(instance):
        return InternalTestVector_InternalTestVector(_dafny.Seq("B.2  Test Case 2"), AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__256(), _dafny.Seq([174, 238, 202, 96, 246, 137, 164, 65, 177, 59, 12, 188, 212, 65, 216, 45, 240, 207, 135, 218, 194, 54, 41, 13, 236, 232, 147, 29, 248, 215, 3, 23]), _dafny.Seq([88, 142, 192, 65, 229, 115, 59, 112, 49, 33, 44, 85, 56, 239, 228, 246, 170, 250, 76, 218, 139, 146, 93, 38, 31, 90, 38, 136, 240, 7, 179, 172, 36, 14, 225, 41, 145, 231, 123, 140, 184, 83, 134, 120, 97, 89, 102, 22, 74, 129, 135, 43, 209, 207, 203, 251, 57, 164, 244, 80]), 32, _dafny.Seq([62, 129, 214, 17, 60, 238, 60, 82, 158, 206, 223, 248, 154, 105, 153, 206, 37, 182, 24, 193, 94, 225, 209, 157, 69, 203, 55, 106, 28, 142, 35, 116]))
    @_dafny.classproperty
    def b3(instance):
        return InternalTestVector_InternalTestVector(_dafny.Seq("B.3  Test Case 3"), AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__256(), _dafny.Seq([149, 200, 247, 110, 17, 54, 126, 181, 85, 38, 162, 179, 147, 174, 144, 101, 131, 209, 203, 221, 71, 150, 33, 70, 245, 6, 204, 124, 172, 18, 244, 100]), _dafny.Seq([202, 214, 14, 144, 75, 158, 156, 139, 254, 180, 168, 26, 127, 103, 211, 189, 220, 192, 94, 100, 37, 88, 112, 64, 55, 112, 243, 83, 58, 230, 221, 99, 76, 234, 165, 108, 83, 230, 136, 189, 19, 122, 230, 1, 137, 53, 243, 75, 159, 176, 132, 234, 72, 228, 198, 136, 246, 187, 179, 136]), 32, _dafny.Seq([202, 250, 92, 160, 63, 95, 190, 42, 36, 32, 4, 171, 203, 211, 222, 16, 89, 199, 64, 123, 30, 229, 121, 37, 81, 36, 175, 24, 155, 224, 181, 86]))
    @_dafny.classproperty
    def b4(instance):
        return InternalTestVector_InternalTestVector(_dafny.Seq("B.4  Test Case 4"), AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__256(), _dafny.Seq([77, 5, 57, 31, 214, 251, 30, 41, 46, 120, 171, 150, 25, 177, 183, 42, 125, 99, 238, 89, 215, 67, 93, 215, 24, 151, 185, 255, 126, 231, 174, 112]), _dafny.Seq([240, 120, 230, 249, 183, 248, 45, 100, 85, 79, 166, 182, 4, 200, 8, 241, 155, 31, 106, 214, 114, 125, 183, 170, 111, 28, 134, 105, 78, 16, 75, 82, 86, 200, 180, 3, 153, 25, 100, 100, 129, 215, 234, 36, 82, 199, 44, 23, 163, 232, 215, 211, 145, 98, 133, 70, 10, 165, 235, 129]), 32, _dafny.Seq([107, 22, 232, 245, 59, 131, 26, 165, 232, 107, 249, 122, 92, 79, 163, 125, 8, 155, 193, 114, 218, 90, 30, 127, 102, 45, 212, 165, 149, 51, 154, 183]))
    @_dafny.classproperty
    def b5(instance):
        return InternalTestVector_InternalTestVector(_dafny.Seq("B.5  Test Case 5"), AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__256(), _dafny.Seq([15, 104, 168, 47, 241, 103, 22, 52, 204, 145, 54, 197, 100, 169, 224, 42, 118, 118, 33, 221, 116, 161, 191, 92, 36, 18, 155, 128, 130, 20, 183, 82]), _dafny.Seq([100, 133, 153, 128, 156, 44, 78, 124, 106, 94, 108, 68, 159, 0, 49, 235, 245, 92, 54, 97, 168, 149, 180, 77, 176, 87, 46, 232, 128, 131, 177, 244, 177, 38, 2, 170, 85, 252, 29, 241, 80, 166, 90, 109, 110, 237, 160, 170, 121, 164, 52, 161, 3, 155, 145, 181, 165, 143, 199, 241]), 32, _dafny.Seq([226, 151, 100, 15, 119, 104, 72, 93, 74, 110, 124, 254, 36, 95, 139, 250, 132, 112, 13, 153, 118, 38, 146, 234, 26, 66, 92, 204, 2, 117, 232, 245]))
    @_dafny.classproperty
    def b6(instance):
        return InternalTestVector_InternalTestVector(_dafny.Seq("B.6 Test Case 6"), AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__384(), _dafny.Seq([130, 44, 118, 74, 27, 17, 112, 133, 193, 15, 14, 104, 152, 20, 210, 191, 189, 155, 67, 40, 127, 26, 140, 117, 215, 149, 169, 131, 26, 40, 97, 132, 200, 88, 111, 53, 119, 182, 229, 187, 206, 22, 55, 146, 94, 4, 252, 71]), _dafny.Seq([175, 52, 97, 16, 185, 65, 177, 29, 33, 137, 49, 108, 159, 194, 185, 244, 33, 55, 117, 165, 215, 54, 141, 53, 65, 38, 120, 162, 143, 205, 3, 176, 127, 5, 73, 102, 110, 253, 243, 12, 128, 240, 171, 85, 99, 114, 10, 86, 239, 97, 106, 19, 187, 143, 119, 128, 3, 111, 192, 142]), 32, _dafny.Seq([224, 174, 35, 92, 184, 35, 128, 82, 123, 231, 105, 52, 166, 150, 34, 57, 109, 144, 231, 191, 167, 226, 210, 149, 228, 55, 91, 206, 224, 209, 177, 1]))
    @_dafny.classproperty
    def b7(instance):
        return InternalTestVector_InternalTestVector(_dafny.Seq("B.7 Test Case 7"), AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__384(), _dafny.Seq([52, 14, 33, 45, 117, 142, 131, 204, 91, 137, 228, 181, 106, 134, 238, 140, 150, 49, 174, 78, 75, 186, 236, 21, 172, 9, 94, 164, 64, 123, 199, 182, 52, 173, 99, 13, 208, 190, 133, 169, 28, 8, 168, 199, 225, 225, 3, 11]), _dafny.Seq([60, 213, 86, 26, 209, 47, 173, 252, 228, 8, 224, 65, 128, 175, 206, 227, 139, 131, 21, 107, 158, 75, 224, 119, 156, 79, 13, 185, 226, 107, 254, 92, 205, 67, 225, 89, 33, 151, 124, 210, 107, 29, 184, 40, 139, 128, 8, 158, 183, 209, 187, 215, 245, 158, 16, 17, 179, 225, 139, 81]), 32, _dafny.Seq([5, 250, 87, 123, 112, 129, 33, 14, 124, 157, 230, 157, 176, 61, 124, 32, 38, 207, 68, 105, 169, 11, 250, 41, 241, 194, 193, 8, 24, 212, 99, 224]))
    @_dafny.classproperty
    def b8(instance):
        return InternalTestVector_InternalTestVector(_dafny.Seq("B.8 Test Case 8"), AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__384(), _dafny.Seq([0, 161, 45, 60, 228, 255, 117, 166, 227, 15, 65, 243, 85, 124, 130, 106, 241, 50, 107, 99, 2, 244, 206, 136, 123, 173, 61, 51, 23, 165, 72, 200, 192, 58, 5, 114, 132, 220, 195, 141, 139, 198, 144, 189, 74, 86, 95, 71]), _dafny.Seq([36, 197, 192, 178, 200, 16, 223, 160, 142, 53, 215, 254, 235, 184, 199, 142, 12, 215, 38, 201, 46, 205, 66, 217, 23, 16, 19, 115, 140, 162, 83, 26, 148, 127, 82, 60, 55, 246, 76, 219, 4, 48, 91, 217, 105, 209, 214, 249, 236, 212, 100, 5, 210, 130, 128, 249, 104, 80, 11, 167]), 32, _dafny.Seq([174, 243, 213, 124, 141, 167, 217, 88, 44, 93, 28, 98, 214, 182, 72, 150, 218, 155, 27, 14, 64, 18, 164, 76, 220, 61, 207, 75, 112, 173, 108, 102]))
    @_dafny.classproperty
    def b9(instance):
        return InternalTestVector_InternalTestVector(_dafny.Seq("B.9 Test Case 9"), AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__384(), _dafny.Seq([0, 0, 217, 183, 236, 111, 190, 253, 242, 86, 253, 104, 34, 11, 82, 5, 172, 101, 162, 0, 17, 69, 17, 140, 80, 186, 107, 101, 112, 50, 25, 139, 139, 124, 227, 178, 247, 6, 138, 120, 13, 193, 124, 34, 69, 154, 242, 183]), _dafny.Seq([216, 87, 84, 28, 98, 184, 87, 86, 220, 115, 222, 125, 194, 216, 111, 93, 94, 139, 40, 51, 139, 176, 169, 69, 181, 196, 253, 124, 129, 247, 25, 97, 185, 112, 93, 61, 21, 59, 25, 25, 93, 0, 59, 116, 33, 32, 104, 237, 16, 249, 108, 83, 67, 134, 83, 8, 122, 1, 82, 207]), 20, _dafny.Seq([121, 62, 241, 19, 249, 99, 151, 171, 0, 49, 234, 160, 250, 167, 119, 193, 7, 231, 208, 60]))
    @_dafny.classproperty
    def b10(instance):
        return InternalTestVector_InternalTestVector(_dafny.Seq("B.10 Test Case 10"), AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__384(), _dafny.Seq([79, 61, 116, 77, 62, 68, 158, 6, 39, 191, 68, 152, 116, 56, 40, 248, 110, 99, 143, 96, 98, 10, 126, 212, 167, 201, 181, 176, 115, 105, 28, 158, 201, 71, 40, 197, 136, 34, 232, 39, 240, 246, 204, 248, 109, 188, 28, 174]), _dafny.Seq([48, 31, 238, 178, 94, 108, 168, 80, 62, 205, 130, 31, 29, 55, 135, 174, 191, 179, 208, 236, 81, 139, 179, 17, 116, 245, 32, 155, 42, 193, 242, 142, 211, 230, 152, 115, 107, 173, 16, 161, 142, 60, 189, 181, 220, 39, 187, 209, 45, 5, 139, 54, 219, 8, 146, 249, 207, 208, 131, 0]), 20, _dafny.Seq([133, 239, 149, 5, 178, 48, 86, 94, 204, 242, 166, 74, 179, 222, 83, 229, 169, 28, 123, 81]))
    @_dafny.classproperty
    def rawTestVectors(instance):
        return _dafny.Seq([default__.b1, default__.b2, default__.b3, default__.b4, default__.b5, default__.b6, default__.b7, default__.b8, default__.b9, default__.b10])
    @_dafny.classproperty
    def PURPOSE(instance):
        return UTF8.default__.EncodeAscii(_dafny.Seq("aws-kms-hierarchy"))
    @_dafny.classproperty
    def c1(instance):
        return TestVector_TestVector(_dafny.Seq("C.1 Test Case 1"), AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__256(), _dafny.Seq([125, 201, 189, 252, 37, 52, 4, 124, 254, 99, 233, 235, 41, 123, 119, 82, 81, 73, 237, 125, 74, 252, 233, 198, 68, 15, 53, 14, 97, 239, 62, 208]), _dafny.Seq([119, 218, 233, 62, 104, 155, 88, 29, 62, 6, 235, 1, 200, 211, 186, 2]), default__.PURPOSE, 32, _dafny.Seq([188, 232, 152, 114, 85, 137, 174, 192, 143, 152, 52, 179, 184, 15, 220, 63, 241, 115, 144, 126, 85, 116, 231, 41, 253, 206, 18, 124, 247, 109, 183, 204]))
    @_dafny.classproperty
    def c2(instance):
        return TestVector_TestVector(_dafny.Seq("C.2 Test Case 2"), AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__256(), _dafny.Seq([80, 22, 113, 23, 118, 68, 10, 32, 75, 169, 199, 192, 255, 220, 214, 60, 182, 1, 126, 147, 171, 233, 110, 177, 35, 145, 217, 129, 30, 9, 80, 159]), _dafny.Seq([210, 241, 192, 158, 103, 66, 27, 35, 143, 66, 168, 189, 82, 171, 211, 252]), default__.PURPOSE, 32, _dafny.Seq([54, 206, 174, 72, 237, 133, 85, 156, 93, 53, 120, 152, 118, 82, 89, 33, 114, 98, 204, 236, 138, 57, 162, 118, 85, 92, 199, 232, 240, 252, 92, 97]))
    @_dafny.classproperty
    def c3(instance):
        return TestVector_TestVector(_dafny.Seq("C.3 Test Case 3"), AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__256(), _dafny.Seq([57, 90, 16, 46, 83, 54, 189, 241, 27, 242, 237, 236, 246, 66, 54, 226, 74, 112, 79, 156, 208, 13, 148, 71, 117, 211, 139, 57, 73, 69, 122, 236]), _dafny.Seq([51, 15, 183, 124, 82, 229, 249, 86, 117, 148, 237, 162, 27, 243, 173, 108]), default__.PURPOSE, 32, _dafny.Seq([22, 55, 236, 141, 159, 163, 250, 236, 86, 47, 225, 103, 156, 225, 228, 146, 166, 45, 244, 39, 136, 163, 205, 200, 116, 193, 20, 147, 112, 254, 210, 194]))
    @_dafny.classproperty
    def c4(instance):
        return TestVector_TestVector(_dafny.Seq("C.4 Test Case 4"), AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__256(), _dafny.Seq([152, 192, 25, 223, 239, 154, 175, 67, 237, 250, 184, 146, 228, 243, 227, 1, 128, 247, 228, 152, 142, 131, 149, 41, 60, 70, 244, 58, 166, 234, 86, 189]), _dafny.Seq([243, 160, 102, 127, 219, 137, 115, 38, 187, 216, 48, 80, 151, 168, 148, 71]), default__.PURPOSE, 32, _dafny.Seq([191, 112, 86, 234, 220, 233, 122, 154, 100, 188, 230, 238, 239, 155, 54, 32, 97, 35, 51, 160, 121, 235, 42, 64, 145, 105, 15, 153, 162, 89, 9, 156]))
    @_dafny.classproperty
    def c5(instance):
        return TestVector_TestVector(_dafny.Seq("C.5 Test Case 5"), AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__256(), _dafny.Seq([166, 236, 116, 51, 140, 189, 192, 175, 42, 154, 51, 26, 208, 149, 76, 159, 174, 162, 207, 4, 108, 232, 196, 240, 12, 57, 228, 155, 97, 75, 42, 66]), _dafny.Seq([236, 169, 233, 45, 43, 25, 122, 243, 152, 191, 154, 55, 45, 134, 159, 220]), default__.PURPOSE, 32, _dafny.Seq([156, 11, 20, 251, 100, 227, 163, 161, 30, 45, 242, 2, 248, 246, 44, 11, 88, 132, 189, 175, 95, 96, 61, 44, 98, 160, 212, 136, 140, 222, 57, 151]))
    @_dafny.classproperty
    def testVectors(instance):
        return _dafny.Seq([default__.c1, default__.c2, default__.c3, default__.c4, default__.c5])

class InternalTestVector:
    @classmethod
    def default(cls, ):
        return lambda: InternalTestVector_InternalTestVector(_dafny.Seq(""), AwsCryptographyPrimitivesTypes.DigestAlgorithm.default()(), _dafny.Seq({}), _dafny.Seq({}), int(0), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_InternalTestVector(self) -> bool:
        return isinstance(self, InternalTestVector_InternalTestVector)

class InternalTestVector_InternalTestVector(InternalTestVector, NamedTuple('InternalTestVector', [('name', Any), ('hash', Any), ('IKM', Any), ('info', Any), ('L', Any), ('OKM', Any)])):
    def __dafnystr__(self) -> str:
        return f'TestKDFK_TestVectors.InternalTestVector.InternalTestVector({_dafny.string_of(self.name)}, {_dafny.string_of(self.hash)}, {_dafny.string_of(self.IKM)}, {_dafny.string_of(self.info)}, {_dafny.string_of(self.L)}, {_dafny.string_of(self.OKM)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, InternalTestVector_InternalTestVector) and self.name == __o.name and self.hash == __o.hash and self.IKM == __o.IKM and self.info == __o.info and self.L == __o.L and self.OKM == __o.OKM
    def __hash__(self) -> int:
        return super().__hash__()


class TestVector:
    @classmethod
    def default(cls, ):
        return lambda: TestVector_TestVector(_dafny.Seq(""), AwsCryptographyPrimitivesTypes.DigestAlgorithm.default()(), _dafny.Seq({}), _dafny.Seq({}), _dafny.Seq({}), int(0), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_TestVector(self) -> bool:
        return isinstance(self, TestVector_TestVector)

class TestVector_TestVector(TestVector, NamedTuple('TestVector', [('name', Any), ('hash', Any), ('IKM', Any), ('info', Any), ('purpose', Any), ('L', Any), ('OKM', Any)])):
    def __dafnystr__(self) -> str:
        return f'TestKDFK_TestVectors.TestVector.TestVector({_dafny.string_of(self.name)}, {_dafny.string_of(self.hash)}, {_dafny.string_of(self.IKM)}, {_dafny.string_of(self.info)}, {_dafny.string_of(self.purpose)}, {_dafny.string_of(self.L)}, {_dafny.string_of(self.OKM)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TestVector_TestVector) and self.name == __o.name and self.hash == __o.hash and self.IKM == __o.IKM and self.info == __o.info and self.purpose == __o.purpose and self.L == __o.L and self.OKM == __o.OKM
    def __hash__(self) -> int:
        return super().__hash__()

