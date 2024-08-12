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

# Module: TestAwsCryptographyPrimitivesHKDF

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestCase1():
        d_15_hash_: AwsCryptographyPrimitivesTypes.DigestAlgorithm
        d_15_hash_ = AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__256()
        d_16_IKM_: _dafny.Seq
        d_16_IKM_ = _dafny.Seq([11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11])
        d_17_salt_: _dafny.Seq
        d_17_salt_ = _dafny.Seq([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        d_18_info_: _dafny.Seq
        d_18_info_ = _dafny.Seq([240, 241, 242, 243, 244, 245, 246, 247, 248, 249])
        d_19_L_: int
        d_19_L_ = 42
        d_20_PRK_: _dafny.Seq
        d_20_PRK_ = _dafny.Seq([7, 119, 9, 54, 44, 46, 50, 223, 13, 220, 63, 13, 196, 123, 186, 99, 144, 182, 199, 59, 181, 15, 156, 49, 34, 236, 132, 74, 215, 194, 179, 229])
        d_21_OKM_: _dafny.Seq
        d_21_OKM_ = _dafny.Seq([60, 178, 95, 37, 250, 172, 213, 122, 144, 67, 79, 100, 208, 54, 47, 42, 45, 45, 10, 144, 207, 26, 90, 76, 93, 176, 45, 86, 236, 196, 197, 191, 52, 0, 114, 8, 213, 184, 135, 24, 88, 101])
        default__.BasicExtractTest(AwsCryptographyPrimitivesTypes.HkdfExtractInput_HkdfExtractInput(d_15_hash_, Wrappers.Option_Some(d_17_salt_), d_16_IKM_), d_20_PRK_)
        default__.BasicExpandTest(AwsCryptographyPrimitivesTypes.HkdfExpandInput_HkdfExpandInput(d_15_hash_, d_20_PRK_, d_18_info_, d_19_L_), d_21_OKM_)
        default__.BasicHkdfTest(AwsCryptographyPrimitivesTypes.HkdfInput_HkdfInput(d_15_hash_, Wrappers.Option_Some(d_17_salt_), d_16_IKM_, d_18_info_, d_19_L_), d_21_OKM_)

    @staticmethod
    def BasicExtractTest(input, expectedPRK):
        d_22_client_: Aws_Cryptography_Primitives.AtomicPrimitivesClient
        d_23_valueOrError0_: Wrappers.Result = None
        out3_: Wrappers.Result
        out3_ = Aws_Cryptography_Primitives.default__.AtomicPrimitives(Aws_Cryptography_Primitives.default__.DefaultCryptoConfig())
        d_23_valueOrError0_ = out3_
        if not(not((d_23_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(86,18): " + _dafny.string_of(d_23_valueOrError0_))
        d_22_client_ = (d_23_valueOrError0_).Extract()
        d_24_output_: _dafny.Seq
        d_25_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out4_: Wrappers.Result
        out4_ = (d_22_client_).HkdfExtract(input)
        d_25_valueOrError1_ = out4_
        if not(not((d_25_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(88,18): " + _dafny.string_of(d_25_valueOrError1_))
        d_24_output_ = (d_25_valueOrError1_).Extract()
        if not((len(d_24_output_)) == (Digest.default__.Length((input).digestAlgorithm))):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(89,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_24_output_) == (expectedPRK)):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(90,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def BasicExpandTest(input, expectedOKM):
        d_26_client_: Aws_Cryptography_Primitives.AtomicPrimitivesClient
        d_27_valueOrError0_: Wrappers.Result = None
        out5_: Wrappers.Result
        out5_ = Aws_Cryptography_Primitives.default__.AtomicPrimitives(Aws_Cryptography_Primitives.default__.DefaultCryptoConfig())
        d_27_valueOrError0_ = out5_
        if not(not((d_27_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(98,18): " + _dafny.string_of(d_27_valueOrError0_))
        d_26_client_ = (d_27_valueOrError0_).Extract()
        d_28_output_: _dafny.Seq
        d_29_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out6_: Wrappers.Result
        out6_ = (d_26_client_).HkdfExpand(input)
        d_29_valueOrError1_ = out6_
        if not(not((d_29_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(100,18): " + _dafny.string_of(d_29_valueOrError1_))
        d_28_output_ = (d_29_valueOrError1_).Extract()
        if not((len(d_28_output_)) == ((input).expectedLength)):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(101,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_28_output_) == (expectedOKM)):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(102,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def BasicHkdfTest(input, expectedOKM):
        d_30_client_: Aws_Cryptography_Primitives.AtomicPrimitivesClient
        d_31_valueOrError0_: Wrappers.Result = None
        out7_: Wrappers.Result
        out7_ = Aws_Cryptography_Primitives.default__.AtomicPrimitives(Aws_Cryptography_Primitives.default__.DefaultCryptoConfig())
        d_31_valueOrError0_ = out7_
        if not(not((d_31_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(110,18): " + _dafny.string_of(d_31_valueOrError0_))
        d_30_client_ = (d_31_valueOrError0_).Extract()
        d_32_output_: _dafny.Seq
        d_33_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out8_: Wrappers.Result
        out8_ = (d_30_client_).Hkdf(input)
        d_33_valueOrError1_ = out8_
        if not(not((d_33_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(112,18): " + _dafny.string_of(d_33_valueOrError1_))
        d_32_output_ = (d_33_valueOrError1_).Extract()
        if not((len(d_32_output_)) == ((input).expectedLength)):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(113,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_32_output_) == (expectedOKM)):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(114,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

