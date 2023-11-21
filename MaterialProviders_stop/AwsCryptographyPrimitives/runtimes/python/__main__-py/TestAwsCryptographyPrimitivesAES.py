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
import TestAwsCryptographyPrimitivesHKDF
import TestAwsCryptographyPrimitivesGenerateRandomBytes
import ConstantTime
import ConstantTimeTest
import TestHKDF__Rfc5869TestVectors
import TestKDF
import TestKDFK__TestVectors
import TestAwsCryptographyPrimitivesRSA

assert "TestAwsCryptographyPrimitivesAES" == __name__
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
        d_218_client_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_219_valueOrError0_: Wrappers.Result = None
        out72_: Wrappers.Result
        out72_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_219_valueOrError0_ = out72_
        if not(not((d_219_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestAES.dfy(99,15): " + _dafny.string_of(d_219_valueOrError0_))
        d_218_client_ = (d_219_valueOrError0_).Extract()
        d_220_output_: _dafny.Seq
        d_221_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out73_: Wrappers.Result
        out73_ = (d_218_client_).AESDecrypt(input)
        d_221_valueOrError1_ = out73_
        if not(not((d_221_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestAES.dfy(100,15): " + _dafny.string_of(d_221_valueOrError1_))
        d_220_output_ = (d_221_valueOrError1_).Extract()
        if not((d_220_output_) == (expectedOutput)):
            raise _dafny.HaltException("test/TestAES.dfy(101,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def BasicAESEncryptTest(input):
        d_222_client_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_223_valueOrError0_: Wrappers.Result = None
        out74_: Wrappers.Result
        out74_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_223_valueOrError0_ = out74_
        if not(not((d_223_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestAES.dfy(108,15): " + _dafny.string_of(d_223_valueOrError0_))
        d_222_client_ = (d_223_valueOrError0_).Extract()
        d_224_output_: software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput
        d_225_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput.default())()
        out75_: Wrappers.Result
        out75_ = (d_222_client_).AESEncrypt(input)
        d_225_valueOrError1_ = out75_
        if not(not((d_225_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestAES.dfy(109,15): " + _dafny.string_of(d_225_valueOrError1_))
        d_224_output_ = (d_225_valueOrError1_).Extract()
        d_226_decryptInput_: software_amazon_cryptography_primitives_internaldafny_types.AESDecryptInput
        d_226_decryptInput_ = software_amazon_cryptography_primitives_internaldafny_types.AESDecryptInput_AESDecryptInput((input).encAlg, (input).key, (d_224_output_).cipherText, (d_224_output_).authTag, (input).iv, (input).aad)
        TestAwsCryptographyPrimitivesAES.default__.BasicAESDecryptTest(d_226_decryptInput_, (input).msg)

