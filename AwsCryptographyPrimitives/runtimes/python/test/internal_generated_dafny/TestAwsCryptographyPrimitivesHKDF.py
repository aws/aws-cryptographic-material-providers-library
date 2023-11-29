import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import BoundedInts
import StandardLibrary_mUInt
import String
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
import software_amazon_cryptography_primitives_internaldafny
import Aws_mCryptography
import Aws
import AesKdfCtr
import TestAwsCryptographyPrimitivesAesKdfCtr
import TestAwsCryptographyPrimitivesHMacDigest
import TestAwsCryptographyPrimitivesDigest
import TestAwsCryptographyPrimitivesHMAC
import TestAwsCryptographyPrimitivesAES
import TestAwsCryptographyPrimitivesRSA
import TestKDF
import TestKDFK__TestVectors

# assert "TestAwsCryptographyPrimitivesHKDF" == __name__
TestAwsCryptographyPrimitivesHKDF = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def TestCase1():
        d_100_hash_: software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm
        d_100_hash_ = software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__256()
        d_101_IKM_: _dafny.Seq
        d_101_IKM_ = _dafny.Seq([11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11])
        d_102_salt_: _dafny.Seq
        d_102_salt_ = _dafny.Seq([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        d_103_info_: _dafny.Seq
        d_103_info_ = _dafny.Seq([240, 241, 242, 243, 244, 245, 246, 247, 248, 249])
        d_104_L_: BoundedInts.int32
        d_104_L_ = 42
        d_105_PRK_: _dafny.Seq
        d_105_PRK_ = _dafny.Seq([7, 119, 9, 54, 44, 46, 50, 223, 13, 220, 63, 13, 196, 123, 186, 99, 144, 182, 199, 59, 181, 15, 156, 49, 34, 236, 132, 74, 215, 194, 179, 229])
        d_106_OKM_: _dafny.Seq
        d_106_OKM_ = _dafny.Seq([60, 178, 95, 37, 250, 172, 213, 122, 144, 67, 79, 100, 208, 54, 47, 42, 45, 45, 10, 144, 207, 26, 90, 76, 93, 176, 45, 86, 236, 196, 197, 191, 52, 0, 114, 8, 213, 184, 135, 24, 88, 101])
        TestAwsCryptographyPrimitivesHKDF.default__.BasicExtractTest(software_amazon_cryptography_primitives_internaldafny_types.HkdfExtractInput_HkdfExtractInput(d_100_hash_, Wrappers.Option_Some(d_102_salt_), d_101_IKM_), d_105_PRK_)
        TestAwsCryptographyPrimitivesHKDF.default__.BasicExpandTest(software_amazon_cryptography_primitives_internaldafny_types.HkdfExpandInput_HkdfExpandInput(d_100_hash_, d_105_PRK_, d_103_info_, d_104_L_), d_106_OKM_)
        TestAwsCryptographyPrimitivesHKDF.default__.BasicHkdfTest(software_amazon_cryptography_primitives_internaldafny_types.HkdfInput_HkdfInput(d_100_hash_, Wrappers.Option_Some(d_102_salt_), d_101_IKM_, d_103_info_, d_104_L_), d_106_OKM_)

    @staticmethod
    def BasicExtractTest(input, expectedPRK):
        d_107_client_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_108_valueOrError0_: Wrappers.Result = None
        out18_: Wrappers.Result
        out18_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_108_valueOrError0_ = out18_
        if not(not((d_108_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(86,15): " + _dafny.string_of(d_108_valueOrError0_))
        d_107_client_ = (d_108_valueOrError0_).Extract()
        d_109_output_: _dafny.Seq
        d_110_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out19_: Wrappers.Result
        out19_ = (d_107_client_).HkdfExtract(input)
        d_110_valueOrError1_ = out19_
        if not(not((d_110_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(88,15): " + _dafny.string_of(d_110_valueOrError1_))
        d_109_output_ = (d_110_valueOrError1_).Extract()
        if not((len(d_109_output_)) == (Digest.default__.Length((input).digestAlgorithm))):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(89,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_109_output_) == (expectedPRK)):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(90,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def BasicExpandTest(input, expectedOKM):
        d_111_client_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_112_valueOrError0_: Wrappers.Result = None
        out20_: Wrappers.Result
        out20_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_112_valueOrError0_ = out20_
        if not(not((d_112_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(98,15): " + _dafny.string_of(d_112_valueOrError0_))
        d_111_client_ = (d_112_valueOrError0_).Extract()
        d_113_output_: _dafny.Seq
        d_114_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out21_: Wrappers.Result
        out21_ = (d_111_client_).HkdfExpand(input)
        d_114_valueOrError1_ = out21_
        if not(not((d_114_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(100,15): " + _dafny.string_of(d_114_valueOrError1_))
        d_113_output_ = (d_114_valueOrError1_).Extract()
        if not((len(d_113_output_)) == ((input).expectedLength)):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(101,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_113_output_) == (expectedOKM)):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(102,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def BasicHkdfTest(input, expectedOKM):
        d_115_client_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_116_valueOrError0_: Wrappers.Result = None
        out22_: Wrappers.Result
        out22_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_116_valueOrError0_ = out22_
        if not(not((d_116_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(110,15): " + _dafny.string_of(d_116_valueOrError0_))
        d_115_client_ = (d_116_valueOrError0_).Extract()
        d_117_output_: _dafny.Seq
        d_118_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out23_: Wrappers.Result
        out23_ = (d_115_client_).Hkdf(input)
        d_118_valueOrError1_ = out23_
        if not(not((d_118_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(112,15): " + _dafny.string_of(d_118_valueOrError1_))
        d_117_output_ = (d_118_valueOrError1_).Extract()
        if not((len(d_117_output_)) == ((input).expectedLength)):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(113,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_117_output_) == (expectedOKM)):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHKDF.dfy(114,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

