import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import BoundedInts
import StandardLibrary_UInt
import StandardLibrary_String
import StandardLibrary
import UTF8
import software.amazon.cryptography.primitives.internaldafny.types
import ExternRandom
import Random
import AESEncryption
import ExternDigest
import Digest
import HMAC
import WrappedHMAC
import HKDF
import WrappedHKDF
import Signature
import KdfCtr
import RSAEncryption
import AwsCryptographyPrimitivesOperations
import AesKdfCtr
import Relations
import Seq_MergeSort
import Math
import Seq
import Unicode
import Functions
import Utf8EncodingForm
import Utf16EncodingForm
import UnicodeStrings
import FileIO
import GeneralInternals
import MulInternalsNonlinear
import MulInternals
import Mul
import ModInternalsNonlinear
import DivInternalsNonlinear
import ModInternals
import DivInternals
import DivMod
import Power
import Logarithm
import StandardLibraryInterop
import UUID
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import GetOpt
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
import software_amazon_cryptography_primitives_internaldafny
import Aws_Cryptography
import Aws
import TestSignature
import TestAwsCryptographyPrimitivesHKDF
import TestAwsCryptographyPrimitivesGenerateRandomBytes
import ConstantTime
import ConstantTimeTest
import TestHKDF__Rfc5869TestVectors
import TestKDF

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
        if not((((len(d_60_IKM_)) == (32)) and ((d_62_L_) == (32))) and (((4) + (len(d_61_info_))) < (StandardLibrary_UInt.default__.INT32__MAX__LIMIT))):
            raise _dafny.HaltException("test/TestKDF_TestVectors.dfy(297,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        TestKDF.default__.KdfRawDeriveTest(d_60_IKM_, d_61_info_, d_62_L_, d_63_OKM_)

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
        TestKDF.default__.KdfTest(software.amazon.cryptography.primitives.internaldafny.types.KdfCtrInput_KdfCtrInput(d_65_hash_, d_66_IKM_, d_69_L_, Wrappers.Option_Some(d_68_purpose_), Wrappers.Option_Some(d_67_info_)), d_70_OKM_)

    @_dafny.classproperty
    def b1(instance):
        return InternalTestVector_InternalTestVector(_dafny.Seq("B.1  Test Case 1"), software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm_SHA__256(), _dafny.Seq([226, 4, 214, 212, 102, 170, 213, 7, 255, 175, 109, 109, 171, 10, 91, 38, 21, 44, 158, 33, 231, 100, 55, 4, 100, 227, 96, 200, 251, 199, 101, 198]), _dafny.Seq([123, 3, 185, 141, 159, 148, 184, 153, 229, 145, 243, 239, 38, 75, 113, 177, 147, 251, 167, 4, 60, 126, 149, 60, 222, 35, 188, 83, 132, 188, 26, 98, 147, 88, 1, 21, 250, 227, 73, 95, 216, 69, 218, 219, 208, 43, 214, 69, 92, 244, 141, 15, 98, 179, 62, 98, 54, 74, 58, 128]), 32, _dafny.Seq([119, 13, 250, 182, 166, 164, 164, 190, 224, 37, 127, 243, 53, 33, 63, 120, 216, 40, 123, 79, 213, 55, 213, 193, 255, 250, 149, 105, 16, 231, 199, 121]))
    @_dafny.classproperty
    def b2(instance):
        return InternalTestVector_InternalTestVector(_dafny.Seq("B.2  Test Case 2"), software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm_SHA__256(), _dafny.Seq([174, 238, 202, 96, 246, 137, 164, 65, 177, 59, 12, 188, 212, 65, 216, 45, 240, 207, 135, 218, 194, 54, 41, 13, 236, 232, 147, 29, 248, 215, 3, 23]), _dafny.Seq([88, 142, 192, 65, 229, 115, 59, 112, 49, 33, 44, 85, 56, 239, 228, 246, 170, 250, 76, 218, 139, 146, 93, 38, 31, 90, 38, 136, 240, 7, 179, 172, 36, 14, 225, 41, 145, 231, 123, 140, 184, 83, 134, 120, 97, 89, 102, 22, 74, 129, 135, 43, 209, 207, 203, 251, 57, 164, 244, 80]), 32, _dafny.Seq([62, 129, 214, 17, 60, 238, 60, 82, 158, 206, 223, 248, 154, 105, 153, 206, 37, 182, 24, 193, 94, 225, 209, 157, 69, 203, 55, 106, 28, 142, 35, 116]))
    @_dafny.classproperty
    def b3(instance):
        return InternalTestVector_InternalTestVector(_dafny.Seq("B.3  Test Case 3"), software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm_SHA__256(), _dafny.Seq([149, 200, 247, 110, 17, 54, 126, 181, 85, 38, 162, 179, 147, 174, 144, 101, 131, 209, 203, 221, 71, 150, 33, 70, 245, 6, 204, 124, 172, 18, 244, 100]), _dafny.Seq([202, 214, 14, 144, 75, 158, 156, 139, 254, 180, 168, 26, 127, 103, 211, 189, 220, 192, 94, 100, 37, 88, 112, 64, 55, 112, 243, 83, 58, 230, 221, 99, 76, 234, 165, 108, 83, 230, 136, 189, 19, 122, 230, 1, 137, 53, 243, 75, 159, 176, 132, 234, 72, 228, 198, 136, 246, 187, 179, 136]), 32, _dafny.Seq([202, 250, 92, 160, 63, 95, 190, 42, 36, 32, 4, 171, 203, 211, 222, 16, 89, 199, 64, 123, 30, 229, 121, 37, 81, 36, 175, 24, 155, 224, 181, 86]))
    @_dafny.classproperty
    def b4(instance):
        return InternalTestVector_InternalTestVector(_dafny.Seq("B.4  Test Case 4"), software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm_SHA__256(), _dafny.Seq([77, 5, 57, 31, 214, 251, 30, 41, 46, 120, 171, 150, 25, 177, 183, 42, 125, 99, 238, 89, 215, 67, 93, 215, 24, 151, 185, 255, 126, 231, 174, 112]), _dafny.Seq([240, 120, 230, 249, 183, 248, 45, 100, 85, 79, 166, 182, 4, 200, 8, 241, 155, 31, 106, 214, 114, 125, 183, 170, 111, 28, 134, 105, 78, 16, 75, 82, 86, 200, 180, 3, 153, 25, 100, 100, 129, 215, 234, 36, 82, 199, 44, 23, 163, 232, 215, 211, 145, 98, 133, 70, 10, 165, 235, 129]), 32, _dafny.Seq([107, 22, 232, 245, 59, 131, 26, 165, 232, 107, 249, 122, 92, 79, 163, 125, 8, 155, 193, 114, 218, 90, 30, 127, 102, 45, 212, 165, 149, 51, 154, 183]))
    @_dafny.classproperty
    def b5(instance):
        return InternalTestVector_InternalTestVector(_dafny.Seq("B.5  Test Case 5"), software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm_SHA__256(), _dafny.Seq([15, 104, 168, 47, 241, 103, 22, 52, 204, 145, 54, 197, 100, 169, 224, 42, 118, 118, 33, 221, 116, 161, 191, 92, 36, 18, 155, 128, 130, 20, 183, 82]), _dafny.Seq([100, 133, 153, 128, 156, 44, 78, 124, 106, 94, 108, 68, 159, 0, 49, 235, 245, 92, 54, 97, 168, 149, 180, 77, 176, 87, 46, 232, 128, 131, 177, 244, 177, 38, 2, 170, 85, 252, 29, 241, 80, 166, 90, 109, 110, 237, 160, 170, 121, 164, 52, 161, 3, 155, 145, 181, 165, 143, 199, 241]), 32, _dafny.Seq([226, 151, 100, 15, 119, 104, 72, 93, 74, 110, 124, 254, 36, 95, 139, 250, 132, 112, 13, 153, 118, 38, 146, 234, 26, 66, 92, 204, 2, 117, 232, 245]))
    @_dafny.classproperty
    def rawTestVectors(instance):
        return _dafny.Seq([default__.b1, default__.b2, default__.b3, default__.b4, default__.b5])
    @_dafny.classproperty
    def PURPOSE(instance):
        return UTF8.default__.EncodeAscii(_dafny.Seq("aws-kms-hierarchy"))
    @_dafny.classproperty
    def c1(instance):
        return TestVector_TestVector(_dafny.Seq("C.1 Test Case 1"), software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm_SHA__256(), _dafny.Seq([125, 201, 189, 252, 37, 52, 4, 124, 254, 99, 233, 235, 41, 123, 119, 82, 81, 73, 237, 125, 74, 252, 233, 198, 68, 15, 53, 14, 97, 239, 62, 208]), _dafny.Seq([119, 218, 233, 62, 104, 155, 88, 29, 62, 6, 235, 1, 200, 211, 186, 2]), default__.PURPOSE, 32, _dafny.Seq([188, 232, 152, 114, 85, 137, 174, 192, 143, 152, 52, 179, 184, 15, 220, 63, 241, 115, 144, 126, 85, 116, 231, 41, 253, 206, 18, 124, 247, 109, 183, 204]))
    @_dafny.classproperty
    def c2(instance):
        return TestVector_TestVector(_dafny.Seq("C.2 Test Case 2"), software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm_SHA__256(), _dafny.Seq([80, 22, 113, 23, 118, 68, 10, 32, 75, 169, 199, 192, 255, 220, 214, 60, 182, 1, 126, 147, 171, 233, 110, 177, 35, 145, 217, 129, 30, 9, 80, 159]), _dafny.Seq([210, 241, 192, 158, 103, 66, 27, 35, 143, 66, 168, 189, 82, 171, 211, 252]), default__.PURPOSE, 32, _dafny.Seq([54, 206, 174, 72, 237, 133, 85, 156, 93, 53, 120, 152, 118, 82, 89, 33, 114, 98, 204, 236, 138, 57, 162, 118, 85, 92, 199, 232, 240, 252, 92, 97]))
    @_dafny.classproperty
    def c3(instance):
        return TestVector_TestVector(_dafny.Seq("C.3 Test Case 3"), software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm_SHA__256(), _dafny.Seq([57, 90, 16, 46, 83, 54, 189, 241, 27, 242, 237, 236, 246, 66, 54, 226, 74, 112, 79, 156, 208, 13, 148, 71, 117, 211, 139, 57, 73, 69, 122, 236]), _dafny.Seq([51, 15, 183, 124, 82, 229, 249, 86, 117, 148, 237, 162, 27, 243, 173, 108]), default__.PURPOSE, 32, _dafny.Seq([22, 55, 236, 141, 159, 163, 250, 236, 86, 47, 225, 103, 156, 225, 228, 146, 166, 45, 244, 39, 136, 163, 205, 200, 116, 193, 20, 147, 112, 254, 210, 194]))
    @_dafny.classproperty
    def c4(instance):
        return TestVector_TestVector(_dafny.Seq("C.4 Test Case 4"), software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm_SHA__256(), _dafny.Seq([152, 192, 25, 223, 239, 154, 175, 67, 237, 250, 184, 146, 228, 243, 227, 1, 128, 247, 228, 152, 142, 131, 149, 41, 60, 70, 244, 58, 166, 234, 86, 189]), _dafny.Seq([243, 160, 102, 127, 219, 137, 115, 38, 187, 216, 48, 80, 151, 168, 148, 71]), default__.PURPOSE, 32, _dafny.Seq([191, 112, 86, 234, 220, 233, 122, 154, 100, 188, 230, 238, 239, 155, 54, 32, 97, 35, 51, 160, 121, 235, 42, 64, 145, 105, 15, 153, 162, 89, 9, 156]))
    @_dafny.classproperty
    def c5(instance):
        return TestVector_TestVector(_dafny.Seq("C.5 Test Case 5"), software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm_SHA__256(), _dafny.Seq([166, 236, 116, 51, 140, 189, 192, 175, 42, 154, 51, 26, 208, 149, 76, 159, 174, 162, 207, 4, 108, 232, 196, 240, 12, 57, 228, 155, 97, 75, 42, 66]), _dafny.Seq([236, 169, 233, 45, 43, 25, 122, 243, 152, 191, 154, 55, 45, 134, 159, 220]), default__.PURPOSE, 32, _dafny.Seq([156, 11, 20, 251, 100, 227, 163, 161, 30, 45, 242, 2, 248, 246, 44, 11, 88, 132, 189, 175, 95, 96, 61, 44, 98, 160, 212, 136, 140, 222, 57, 151]))
    @_dafny.classproperty
    def testVectors(instance):
        return _dafny.Seq([default__.c1, default__.c2, default__.c3, default__.c4, default__.c5])

class InternalTestVector:
    @classmethod
    def default(cls, ):
        return lambda: InternalTestVector_InternalTestVector(_dafny.Seq({}), software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm.default()(), _dafny.Seq({}), _dafny.Seq({}), int(0), _dafny.Seq({}))
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
        return lambda: TestVector_TestVector(_dafny.Seq({}), software.amazon.cryptography.primitives.internaldafny.types.DigestAlgorithm.default()(), _dafny.Seq({}), _dafny.Seq({}), _dafny.Seq({}), int(0), _dafny.Seq({}))
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

