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

# assert "TestKDF" == __name__
TestKDF = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def KdfRawDeriveTest(ikm, info, L, expectedOKM):
        d_80_output_: Wrappers.Result
        out15_: Wrappers.Result
        out15_ = KdfCtr.default__.RawDerive(ikm, info, L, 0)
        d_80_output_ = out15_
        if (d_80_output_).is_Success:
            if not((len((d_80_output_).value)) == (L)):
                raise _dafny.HaltException("test/TestKDF.dfy(30,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            if not(((d_80_output_).value) == (expectedOKM)):
                raise _dafny.HaltException("test/TestKDF.dfy(31,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def KdfTest(input, expectedOKM):
        d_81_client_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_82_valueOrError0_: Wrappers.Result = None
        out16_: Wrappers.Result
        out16_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_82_valueOrError0_ = out16_
        if not(not((d_82_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestKDF.dfy(40,15): " + _dafny.string_of(d_82_valueOrError0_))
        d_81_client_ = (d_82_valueOrError0_).Extract()
        d_83_output_: _dafny.Seq
        d_84_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out17_: Wrappers.Result
        out17_ = (d_81_client_).KdfCounterMode(input)
        d_84_valueOrError1_ = out17_
        if not(not((d_84_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestKDF.dfy(42,15): " + _dafny.string_of(d_84_valueOrError1_))
        d_83_output_ = (d_84_valueOrError1_).Extract()
        if not((len(d_83_output_)) == ((input).expectedLength)):
            raise _dafny.HaltException("test/TestKDF.dfy(43,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_83_output_) == (expectedOKM)):
            raise _dafny.HaltException("test/TestKDF.dfy(44,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

