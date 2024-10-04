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

# Module: TestAwsCryptographyPrimitivesHKDF

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestCase1():
        d_0_hash_: AwsCryptographyPrimitivesTypes.DigestAlgorithm
        d_0_hash_ = AwsCryptographyPrimitivesTypes.DigestAlgorithm_SHA__256()
        d_1_IKM_: _dafny.Seq
        d_1_IKM_ = _dafny.Seq([11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11])
        d_2_salt_: _dafny.Seq
        d_2_salt_ = _dafny.Seq([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        d_3_info_: _dafny.Seq
        d_3_info_ = _dafny.Seq([240, 241, 242, 243, 244, 245, 246, 247, 248, 249])
        d_4_L_: int
        d_4_L_ = 42
        d_5_PRK_: _dafny.Seq
        d_5_PRK_ = _dafny.Seq([7, 119, 9, 54, 44, 46, 50, 223, 13, 220, 63, 13, 196, 123, 186, 99, 144, 182, 199, 59, 181, 15, 156, 49, 34, 236, 132, 74, 215, 194, 179, 229])
        d_6_OKM_: _dafny.Seq
        d_6_OKM_ = _dafny.Seq([60, 178, 95, 37, 250, 172, 213, 122, 144, 67, 79, 100, 208, 54, 47, 42, 45, 45, 10, 144, 207, 26, 90, 76, 93, 176, 45, 86, 236, 196, 197, 191, 52, 0, 114, 8, 213, 184, 135, 24, 88, 101])
        default__.BasicExtractTest(AwsCryptographyPrimitivesTypes.HkdfExtractInput_HkdfExtractInput(d_0_hash_, Wrappers.Option_Some(d_2_salt_), d_1_IKM_), d_5_PRK_)
        default__.BasicExpandTest(AwsCryptographyPrimitivesTypes.HkdfExpandInput_HkdfExpandInput(d_0_hash_, d_5_PRK_, d_3_info_, d_4_L_), d_6_OKM_)
        default__.BasicHkdfTest(AwsCryptographyPrimitivesTypes.HkdfInput_HkdfInput(d_0_hash_, Wrappers.Option_Some(d_2_salt_), d_1_IKM_, d_3_info_, d_4_L_), d_6_OKM_)

    @staticmethod
    def BasicExtractTest(input, expectedPRK):
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(86,18): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_client_: AtomicPrimitives.AtomicPrimitivesClient
        d_1_client_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out1_: Wrappers.Result
        out1_ = (d_1_client_).HkdfExtract(input)
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(88,18): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_output_: _dafny.Seq
        d_3_output_ = (d_2_valueOrError1_).Extract()
        if not((len(d_3_output_)) == (Digest.default__.Length((input).digestAlgorithm))):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(89,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_3_output_) == (expectedPRK)):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(90,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def BasicExpandTest(input, expectedOKM):
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(98,18): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_client_: AtomicPrimitives.AtomicPrimitivesClient
        d_1_client_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out1_: Wrappers.Result
        out1_ = (d_1_client_).HkdfExpand(input)
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(100,18): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_output_: _dafny.Seq
        d_3_output_ = (d_2_valueOrError1_).Extract()
        if not((len(d_3_output_)) == ((input).expectedLength)):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(101,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_3_output_) == (expectedOKM)):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(102,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def BasicHkdfTest(input, expectedOKM):
        d_0_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = AtomicPrimitives.default__.AtomicPrimitives(AtomicPrimitives.default__.DefaultCryptoConfig())
        d_0_valueOrError0_ = out0_
        if not(not((d_0_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(110,18): " + _dafny.string_of(d_0_valueOrError0_))
        d_1_client_: AtomicPrimitives.AtomicPrimitivesClient
        d_1_client_ = (d_0_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out1_: Wrappers.Result
        out1_ = (d_1_client_).Hkdf(input)
        d_2_valueOrError1_ = out1_
        if not(not((d_2_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(112,18): " + _dafny.string_of(d_2_valueOrError1_))
        d_3_output_: _dafny.Seq
        d_3_output_ = (d_2_valueOrError1_).Extract()
        if not((len(d_3_output_)) == ((input).expectedLength)):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(113,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_3_output_) == (expectedOKM)):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(114,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

