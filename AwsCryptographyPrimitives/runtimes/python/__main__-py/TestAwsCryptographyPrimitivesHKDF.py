import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_mMergeSort
import Math
import Seq
import BoundedInts
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
import StandardLibrary_mUInt
import String
import StandardLibrary
import UUID
import UTF8
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
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
import software_amazon_cryptography_primitives_internaldafny
import Aws_mCryptography
import Aws
import TestSignature

assert "TestAwsCryptographyPrimitivesHKDF" == __name__
TestAwsCryptographyPrimitivesHKDF = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestCase1():
        d_120_hash_: software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm
        d_120_hash_ = software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__256()
        d_121_IKM_: _dafny.Seq
        d_121_IKM_ = _dafny.Seq([11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11])
        d_122_salt_: _dafny.Seq
        d_122_salt_ = _dafny.Seq([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        d_123_info_: _dafny.Seq
        d_123_info_ = _dafny.Seq([240, 241, 242, 243, 244, 245, 246, 247, 248, 249])
        d_124_L_: BoundedInts.int32
        d_124_L_ = 42
        d_125_PRK_: _dafny.Seq
        d_125_PRK_ = _dafny.Seq([7, 119, 9, 54, 44, 46, 50, 223, 13, 220, 63, 13, 196, 123, 186, 99, 144, 182, 199, 59, 181, 15, 156, 49, 34, 236, 132, 74, 215, 194, 179, 229])
        d_126_OKM_: _dafny.Seq
        d_126_OKM_ = _dafny.Seq([60, 178, 95, 37, 250, 172, 213, 122, 144, 67, 79, 100, 208, 54, 47, 42, 45, 45, 10, 144, 207, 26, 90, 76, 93, 176, 45, 86, 236, 196, 197, 191, 52, 0, 114, 8, 213, 184, 135, 24, 88, 101])
        TestAwsCryptographyPrimitivesHKDF.default__.BasicExtractTest(software_amazon_cryptography_primitives_internaldafny_types.HkdfExtractInput_HkdfExtractInput(d_120_hash_, Wrappers.Option_Some(d_122_salt_), d_121_IKM_), d_125_PRK_)
        TestAwsCryptographyPrimitivesHKDF.default__.BasicExpandTest(software_amazon_cryptography_primitives_internaldafny_types.HkdfExpandInput_HkdfExpandInput(d_120_hash_, d_125_PRK_, d_123_info_, d_124_L_), d_126_OKM_)
        TestAwsCryptographyPrimitivesHKDF.default__.BasicHkdfTest(software_amazon_cryptography_primitives_internaldafny_types.HkdfInput_HkdfInput(d_120_hash_, Wrappers.Option_Some(d_122_salt_), d_121_IKM_, d_123_info_, d_124_L_), d_126_OKM_)

    @staticmethod
    def BasicExtractTest(input, expectedPRK):
        d_127_client_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_128_valueOrError0_: Wrappers.Result = None
        out54_: Wrappers.Result
        out54_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_128_valueOrError0_ = out54_
        if not(not((d_128_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(86,15): " + _dafny.string_of(d_128_valueOrError0_))
        d_127_client_ = (d_128_valueOrError0_).Extract()
        d_129_output_: _dafny.Seq
        d_130_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out55_: Wrappers.Result
        out55_ = (d_127_client_).HkdfExtract(input)
        d_130_valueOrError1_ = out55_
        if not(not((d_130_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(88,15): " + _dafny.string_of(d_130_valueOrError1_))
        d_129_output_ = (d_130_valueOrError1_).Extract()
        if not((len(d_129_output_)) == (Digest.default__.Length((input).digestAlgorithm))):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(89,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_129_output_) == (expectedPRK)):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(90,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def BasicExpandTest(input, expectedOKM):
        d_131_client_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_132_valueOrError0_: Wrappers.Result = None
        out56_: Wrappers.Result
        out56_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_132_valueOrError0_ = out56_
        if not(not((d_132_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(98,15): " + _dafny.string_of(d_132_valueOrError0_))
        d_131_client_ = (d_132_valueOrError0_).Extract()
        d_133_output_: _dafny.Seq
        d_134_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out57_: Wrappers.Result
        out57_ = (d_131_client_).HkdfExpand(input)
        d_134_valueOrError1_ = out57_
        if not(not((d_134_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(100,15): " + _dafny.string_of(d_134_valueOrError1_))
        d_133_output_ = (d_134_valueOrError1_).Extract()
        if not((len(d_133_output_)) == ((input).expectedLength)):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(101,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_133_output_) == (expectedOKM)):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(102,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def BasicHkdfTest(input, expectedOKM):
        d_135_client_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_136_valueOrError0_: Wrappers.Result = None
        out58_: Wrappers.Result
        out58_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_136_valueOrError0_ = out58_
        if not(not((d_136_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(110,15): " + _dafny.string_of(d_136_valueOrError0_))
        d_135_client_ = (d_136_valueOrError0_).Extract()
        d_137_output_: _dafny.Seq
        d_138_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out59_: Wrappers.Result
        out59_ = (d_135_client_).Hkdf(input)
        d_138_valueOrError1_ = out59_
        if not(not((d_138_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(112,15): " + _dafny.string_of(d_138_valueOrError1_))
        d_137_output_ = (d_138_valueOrError1_).Extract()
        if not((len(d_137_output_)) == ((input).expectedLength)):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(113,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_137_output_) == (expectedOKM)):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(114,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

