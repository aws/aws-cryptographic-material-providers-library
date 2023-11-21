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

assert "TestAwsCryptographyPrimitivesAesKdfCtr" == __name__
TestAwsCryptographyPrimitivesAesKdfCtr = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def AesKdfCtrTests():
        d_0_key_: _dafny.Seq
        d_0_key_ = _dafny.Seq([138, 39, 30, 72, 206, 182, 214, 144, 245, 34, 28, 219, 204, 175, 198, 23, 132, 234, 125, 246, 130, 54, 251, 60, 137, 120, 166, 245, 0, 150, 79, 107])
        d_1_nonce_: _dafny.Seq
        d_1_nonce_ = _dafny.Seq([66, 32, 73, 11, 207, 79, 97, 80, 11, 22, 236, 247, 42, 6, 222, 165])
        d_2_goal_: _dafny.Seq
        d_2_goal_ = _dafny.Seq([143, 128, 174, 191, 9, 171, 140, 22, 40, 143, 11, 239, 249, 101, 61, 120, 176, 23, 233, 210, 125, 72, 114, 70, 209, 170, 206, 96, 24, 112, 215, 169, 100, 136, 162, 231, 208, 24, 135, 121, 223, 13, 239, 180])
        d_3_result_: _dafny.Seq
        d_4_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_4_valueOrError0_ = AesKdfCtr.default__.AesKdfCtrStream(d_1_nonce_, d_0_key_, 44)
        if not(not((d_4_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestAesKdfCtr.dfy(18,15): " + _dafny.string_of(d_4_valueOrError0_))
        d_3_result_ = (d_4_valueOrError0_).Extract()
        if not((len(d_3_result_)) == (44)):
            raise _dafny.HaltException("test/TestAesKdfCtr.dfy(19,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_2_goal_) == (d_3_result_)):
            raise _dafny.HaltException("test/TestAesKdfCtr.dfy(20,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_0_key_ = _dafny.Seq([212, 191, 10, 32, 13, 55, 22, 101, 189, 182, 186, 119, 202, 16, 175, 49, 103, 82, 87, 190, 13, 142, 103, 201, 98, 84, 228, 47, 142, 96, 61, 167])
        d_1_nonce_ = _dafny.Seq([135, 1, 132, 66, 198, 216, 26, 105, 47, 97, 246, 192, 186, 187, 54, 129])
        d_2_goal_ = _dafny.Seq([11, 154, 37, 42, 116, 143, 238, 68, 62, 135, 225, 71, 98, 224, 135, 18])
        d_5_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_5_valueOrError1_ = AesKdfCtr.default__.AesKdfCtrStream(d_1_nonce_, d_0_key_, 16)
        if not(not((d_5_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestAesKdfCtr.dfy(25,11): " + _dafny.string_of(d_5_valueOrError1_))
        d_3_result_ = (d_5_valueOrError1_).Extract()
        if not((len(d_3_result_)) == (16)):
            raise _dafny.HaltException("test/TestAesKdfCtr.dfy(26,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_2_goal_) == (d_3_result_)):
            raise _dafny.HaltException("test/TestAesKdfCtr.dfy(27,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_0_key_ = _dafny.Seq([106, 72, 42, 47, 58, 213, 111, 196, 126, 37, 46, 203, 150, 153, 188, 53, 32, 194, 159, 196, 221, 90, 124, 70, 45, 252, 99, 98, 42, 68, 94, 19])
        d_1_nonce_ = _dafny.Seq([13, 247, 32, 159, 220, 254, 69, 218, 42, 110, 159, 42, 209, 244, 79, 232])
        d_2_goal_ = _dafny.Seq([150, 218, 139, 126, 166, 233, 178, 123, 229, 210, 40, 218, 141, 26, 127, 208, 124, 197, 212, 69, 251, 71, 73, 90, 47, 134, 46, 7, 215, 208, 194, 180, 174, 110, 1, 57, 16, 37, 16, 235, 93, 138, 25, 180, 85, 16, 229, 165, 238, 36, 56, 131, 247, 31, 64, 23, 249, 67, 153, 94, 23, 243, 69, 11])
        d_6_valueOrError2_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_6_valueOrError2_ = AesKdfCtr.default__.AesKdfCtrStream(d_1_nonce_, d_0_key_, 64)
        if not(not((d_6_valueOrError2_).IsFailure())):
            raise _dafny.HaltException("test/TestAesKdfCtr.dfy(32,11): " + _dafny.string_of(d_6_valueOrError2_))
        d_3_result_ = (d_6_valueOrError2_).Extract()
        if not((len(d_3_result_)) == (64)):
            raise _dafny.HaltException("test/TestAesKdfCtr.dfy(33,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_2_goal_) == (d_3_result_)):
            raise _dafny.HaltException("test/TestAesKdfCtr.dfy(34,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

