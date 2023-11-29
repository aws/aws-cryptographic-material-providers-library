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

# assert "TestAwsCryptographyPrimitivesAES" == __name__
TestAwsCryptographyPrimitivesAES = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def AESDecryptTests():
        TestAwsCryptographyPrimitivesAES.default__.BasicAESDecryptTest(software_amazon_cryptography_primitives_internaldafny_types.AESDecryptInput_AESDecryptInput(software_amazon_cryptography_primitives_internaldafny_types.AES__GCM_AES__GCM(32, 16, 12), _dafny.Seq([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), _dafny.Seq([102, 165, 173, 47]), _dafny.Seq([54, 200, 18, 56, 172, 194, 174, 23, 239, 151, 47, 180, 143, 232, 142, 184]), _dafny.Seq([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]), _dafny.Seq([3, 3, 3, 3])), _dafny.Seq([97, 115, 100, 102]))

    @staticmethod
    def AESEncryptTests():
        TestAwsCryptographyPrimitivesAES.default__.BasicAESEncryptTest(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptInput_AESEncryptInput(software_amazon_cryptography_primitives_internaldafny_types.AES__GCM_AES__GCM(32, 16, 12), _dafny.Seq([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]), _dafny.Seq([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), _dafny.Seq([97, 115, 100, 102]), _dafny.Seq([3, 3, 3, 3])))

    @staticmethod
    def BasicAESDecryptTest(input, expectedOutput):
        d_29_client_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_30_valueOrError0_: Wrappers.Result = None
        out4_: Wrappers.Result
        out4_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_30_valueOrError0_ = out4_
        if not(not((d_30_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestAES.dfy(99,15): " + _dafny.string_of(d_30_valueOrError0_))
        d_29_client_ = (d_30_valueOrError0_).Extract()
        d_31_output_: _dafny.Seq
        d_32_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out5_: Wrappers.Result
        out5_ = (d_29_client_).AESDecrypt(input)
        d_32_valueOrError1_ = out5_
        if not(not((d_32_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestAES.dfy(100,15): " + _dafny.string_of(d_32_valueOrError1_))
        d_31_output_ = (d_32_valueOrError1_).Extract()
        if not((d_31_output_) == (expectedOutput)):
            raise _dafny.HaltException("test/TestAES.dfy(101,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def BasicAESEncryptTest(input):
        d_33_client_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_34_valueOrError0_: Wrappers.Result = None
        out6_: Wrappers.Result
        out6_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_34_valueOrError0_ = out6_
        if not(not((d_34_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestAES.dfy(108,15): " + _dafny.string_of(d_34_valueOrError0_))
        d_33_client_ = (d_34_valueOrError0_).Extract()
        d_35_output_: software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput
        d_36_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput.default())()
        out7_: Wrappers.Result
        out7_ = (d_33_client_).AESEncrypt(input)
        d_36_valueOrError1_ = out7_
        if not(not((d_36_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestAES.dfy(109,15): " + _dafny.string_of(d_36_valueOrError1_))
        d_35_output_ = (d_36_valueOrError1_).Extract()
        d_37_decryptInput_: software_amazon_cryptography_primitives_internaldafny_types.AESDecryptInput
        d_37_decryptInput_ = software_amazon_cryptography_primitives_internaldafny_types.AESDecryptInput_AESDecryptInput((input).encAlg, (input).key, (d_35_output_).cipherText, (d_35_output_).authTag, (input).iv, (input).aad)
        TestAwsCryptographyPrimitivesAES.default__.BasicAESDecryptTest(d_37_decryptInput_, (input).msg)

