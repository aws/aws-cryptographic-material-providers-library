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
import software_amazon_cryptography_primitives_internaldafny_types
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

# Module: TestAwsCryptographyPrimitivesHKDF

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestCase1():
        d_15_hash_: software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm
        d_15_hash_ = software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__256()
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
        default__.BasicExtractTest(software_amazon_cryptography_primitives_internaldafny_types.HkdfExtractInput_HkdfExtractInput(d_15_hash_, Wrappers.Option_Some(d_17_salt_), d_16_IKM_), d_20_PRK_)
        default__.BasicExpandTest(software_amazon_cryptography_primitives_internaldafny_types.HkdfExpandInput_HkdfExpandInput(d_15_hash_, d_20_PRK_, d_18_info_, d_19_L_), d_21_OKM_)
        default__.BasicHkdfTest(software_amazon_cryptography_primitives_internaldafny_types.HkdfInput_HkdfInput(d_15_hash_, Wrappers.Option_Some(d_17_salt_), d_16_IKM_, d_18_info_, d_19_L_), d_21_OKM_)

    @staticmethod
    def BasicExtractTest(input, expectedPRK):
        d_22_client_: software_amazon_cryptography_primitives_internaldafny_types.IAwsCryptographicPrimitivesClient
        d_23_valueOrError0_: Wrappers.Result = None
        out3_: Wrappers.Result
        out3_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_23_valueOrError0_ = out3_
        if not(not((d_23_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(86,15): " + _dafny.string_of(d_23_valueOrError0_))
        d_22_client_ = (d_23_valueOrError0_).Extract()
        d_24_output_: _dafny.Seq
        d_25_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out4_: Wrappers.Result
        out4_ = (d_22_client_).HkdfExtract(input)
        d_25_valueOrError1_ = out4_
        if not(not((d_25_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(88,15): " + _dafny.string_of(d_25_valueOrError1_))
        d_24_output_ = (d_25_valueOrError1_).Extract()
        if not((len(d_24_output_)) == (Digest.default__.Length((input).digestAlgorithm))):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(89,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_24_output_) == (expectedPRK)):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(90,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def BasicExpandTest(input, expectedOKM):
        d_26_client_: software_amazon_cryptography_primitives_internaldafny_types.IAwsCryptographicPrimitivesClient
        d_27_valueOrError0_: Wrappers.Result = None
        out5_: Wrappers.Result
        out5_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_27_valueOrError0_ = out5_
        if not(not((d_27_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(98,15): " + _dafny.string_of(d_27_valueOrError0_))
        d_26_client_ = (d_27_valueOrError0_).Extract()
        d_28_output_: _dafny.Seq
        d_29_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out6_: Wrappers.Result
        out6_ = (d_26_client_).HkdfExpand(input)
        d_29_valueOrError1_ = out6_
        if not(not((d_29_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(100,15): " + _dafny.string_of(d_29_valueOrError1_))
        d_28_output_ = (d_29_valueOrError1_).Extract()
        if not((len(d_28_output_)) == ((input).expectedLength)):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(101,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_28_output_) == (expectedOKM)):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(102,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def BasicHkdfTest(input, expectedOKM):
        d_30_client_: software_amazon_cryptography_primitives_internaldafny_types.IAwsCryptographicPrimitivesClient
        d_31_valueOrError0_: Wrappers.Result = None
        out7_: Wrappers.Result
        out7_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_31_valueOrError0_ = out7_
        if not(not((d_31_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(110,15): " + _dafny.string_of(d_31_valueOrError0_))
        d_30_client_ = (d_31_valueOrError0_).Extract()
        d_32_output_: _dafny.Seq
        d_33_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out8_: Wrappers.Result
        out8_ = (d_30_client_).Hkdf(input)
        d_33_valueOrError1_ = out8_
        if not(not((d_33_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(112,15): " + _dafny.string_of(d_33_valueOrError1_))
        d_32_output_ = (d_33_valueOrError1_).Extract()
        if not((len(d_32_output_)) == ((input).expectedLength)):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(113,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_32_output_) == (expectedOKM)):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(114,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

