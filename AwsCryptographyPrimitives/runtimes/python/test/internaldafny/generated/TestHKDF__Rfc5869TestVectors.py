import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_ as module_
import _dafny as _dafny
import System_ as System_
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import smithy_dafny_standard_library.internaldafny.generated.BoundedInts as BoundedInts
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import smithy_dafny_standard_library.internaldafny.generated.UTF8 as UTF8
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
import smithy_dafny_standard_library.internaldafny.generated.Relations as Relations
import smithy_dafny_standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import smithy_dafny_standard_library.internaldafny.generated.Math as Math
import smithy_dafny_standard_library.internaldafny.generated.Seq as Seq
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
import smithy_dafny_standard_library.internaldafny.generated.UUID as UUID
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
import TestSignature as TestSignature
import TestAwsCryptographyPrimitivesHKDF as TestAwsCryptographyPrimitivesHKDF
import TestAwsCryptographyPrimitivesGenerateRandomBytes as TestAwsCryptographyPrimitivesGenerateRandomBytes
import ConstantTime as ConstantTime
import ConstantTimeTest as ConstantTimeTest

# Module: TestHKDF__Rfc5869TestVectors

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def ExpectRFCTestVectors():
        hi0_ = len(default__.testVectors)
        for d_0_i_ in range(0, hi0_):
            default__.ExpectTestVector((default__.testVectors)[d_0_i_])

    @staticmethod
    def ExpectTestVector(vector):
        let_tmp_rhs0_ = vector
        d_0_name_ = let_tmp_rhs0_.name
        d_1_hash_ = let_tmp_rhs0_.hash
        d_2_IKM_ = let_tmp_rhs0_.IKM
        d_3_salt_ = let_tmp_rhs0_.salt
        d_4_info_ = let_tmp_rhs0_.info
        d_5_L_ = let_tmp_rhs0_.L
        d_6_PRK_ = let_tmp_rhs0_.PRK
        d_7_OKM_ = let_tmp_rhs0_.OKM
        _dafny.print(_dafny.string_of((d_0_name_) + (_dafny.Seq("\n"))))
        TestAwsCryptographyPrimitivesHKDF.default__.BasicExtractTest(AwsCryptographyPrimitivesTypes.HkdfExtractInput_HkdfExtractInput(d_1_hash_, (Wrappers.Option_Some(d_3_salt_) if (len(d_3_salt_)) > (0) else Wrappers.Option_None()), d_2_IKM_), d_6_PRK_)
        TestAwsCryptographyPrimitivesHKDF.default__.BasicExpandTest(AwsCryptographyPrimitivesTypes.HkdfExpandInput_HkdfExpandInput(d_1_hash_, d_6_PRK_, d_4_info_, d_5_L_), d_7_OKM_)
        TestAwsCryptographyPrimitivesHKDF.default__.BasicHkdfTest(AwsCryptographyPrimitivesTypes.HkdfInput_HkdfInput(d_1_hash_, (Wrappers.Option_Some(d_3_salt_) if (len(d_3_salt_)) > (0) else Wrappers.Option_None()), d_2_IKM_, d_4_info_, d_5_L_), d_7_OKM_)

    @_dafny.classproperty
    def a1(instance):
        return RFCTestVector_RFCTestVector(_dafny.Seq("A.1.  Test Case 1"), AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__256(), _dafny.Seq([11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11]), _dafny.Seq([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), _dafny.Seq([240, 241, 242, 243, 244, 245, 246, 247, 248, 249]), 42, _dafny.Seq([7, 119, 9, 54, 44, 46, 50, 223, 13, 220, 63, 13, 196, 123, 186, 99, 144, 182, 199, 59, 181, 15, 156, 49, 34, 236, 132, 74, 215, 194, 179, 229]), _dafny.Seq([60, 178, 95, 37, 250, 172, 213, 122, 144, 67, 79, 100, 208, 54, 47, 42, 45, 45, 10, 144, 207, 26, 90, 76, 93, 176, 45, 86, 236, 196, 197, 191, 52, 0, 114, 8, 213, 184, 135, 24, 88, 101]))
    @_dafny.classproperty
    def a2(instance):
        return RFCTestVector_RFCTestVector(_dafny.Seq("A.2.  Test Case 2"), AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__256(), _dafny.Seq([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), _dafny.Seq([96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175]), _dafny.Seq([176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255]), 82, _dafny.Seq([6, 166, 184, 140, 88, 83, 54, 26, 6, 16, 76, 156, 235, 53, 180, 92, 239, 118, 0, 20, 144, 70, 113, 1, 74, 25, 63, 64, 193, 95, 194, 68]), _dafny.Seq([177, 30, 57, 141, 200, 3, 39, 161, 200, 231, 247, 140, 89, 106, 73, 52, 79, 1, 46, 218, 45, 78, 250, 216, 160, 80, 204, 76, 25, 175, 169, 124, 89, 4, 90, 153, 202, 199, 130, 114, 113, 203, 65, 198, 94, 89, 14, 9, 218, 50, 117, 96, 12, 47, 9, 184, 54, 119, 147, 169, 172, 163, 219, 113, 204, 48, 197, 129, 121, 236, 62, 135, 193, 76, 1, 213, 193, 243, 67, 79, 29, 135]))
    @_dafny.classproperty
    def a3(instance):
        return RFCTestVector_RFCTestVector(_dafny.Seq("A.3.  Test Case 3"), AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__256(), _dafny.Seq([11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11]), _dafny.Seq([]), _dafny.Seq([]), 42, _dafny.Seq([25, 239, 36, 163, 44, 113, 123, 22, 127, 51, 169, 29, 111, 100, 139, 223, 150, 89, 103, 118, 175, 219, 99, 119, 172, 67, 76, 28, 41, 60, 203, 4]), _dafny.Seq([141, 164, 231, 117, 165, 99, 193, 143, 113, 95, 128, 42, 6, 60, 90, 49, 184, 161, 31, 92, 94, 225, 135, 158, 195, 69, 78, 95, 60, 115, 141, 45, 157, 32, 19, 149, 250, 164, 182, 26, 150, 200]))
    @_dafny.classproperty
    def testVectors(instance):
        return _dafny.Seq([default__.a1, default__.a2, default__.a3])

class RFCTestVector:
    @classmethod
    def default(cls, ):
        return lambda: RFCTestVector_RFCTestVector(_dafny.Seq(""), AwsCryptographyPrimitivesTypes.DigestAlgorithm.default()(), _dafny.Seq({}), _dafny.Seq({}), _dafny.Seq({}), int(0), _dafny.Seq({}), _dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_RFCTestVector(self) -> bool:
        return isinstance(self, RFCTestVector_RFCTestVector)

class RFCTestVector_RFCTestVector(RFCTestVector, NamedTuple('RFCTestVector', [('name', Any), ('hash', Any), ('IKM', Any), ('salt', Any), ('info', Any), ('L', Any), ('PRK', Any), ('OKM', Any)])):
    def __dafnystr__(self) -> str:
        return f'TestHKDF_Rfc5869TestVectors.RFCTestVector.RFCTestVector({_dafny.string_of(self.name)}, {_dafny.string_of(self.hash)}, {_dafny.string_of(self.IKM)}, {_dafny.string_of(self.salt)}, {_dafny.string_of(self.info)}, {_dafny.string_of(self.L)}, {_dafny.string_of(self.PRK)}, {_dafny.string_of(self.OKM)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, RFCTestVector_RFCTestVector) and self.name == __o.name and self.hash == __o.hash and self.IKM == __o.IKM and self.salt == __o.salt and self.info == __o.info and self.L == __o.L and self.PRK == __o.PRK and self.OKM == __o.OKM
    def __hash__(self) -> int:
        return super().__hash__()

