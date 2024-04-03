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
import TestAwsCryptographyPrimitivesHKDF
import TestAwsCryptographyPrimitivesGenerateRandomBytes
import ConstantTime
import ConstantTimeTest
import TestHKDF__Rfc5869TestVectors
import TestKDF
import TestKDFK__TestVectors
import TestAwsCryptographyPrimitivesRSA

# Module: TestAwsCryptographyPrimitivesAES

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def AESDecryptTests():
        default__.BasicAESDecryptTest(software_amazon_cryptography_primitives_internaldafny_types.AESDecryptInput_AESDecryptInput(software_amazon_cryptography_primitives_internaldafny_types.AES__GCM_AES__GCM(32, 16, 12), _dafny.Seq([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), _dafny.Seq([102, 165, 173, 47]), _dafny.Seq([54, 200, 18, 56, 172, 194, 174, 23, 239, 151, 47, 180, 143, 232, 142, 184]), _dafny.Seq([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]), _dafny.Seq([3, 3, 3, 3])), _dafny.Seq([97, 115, 100, 102]))

    @staticmethod
    def AESEncryptTests():
        default__.BasicAESEncryptTest(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptInput_AESEncryptInput(software_amazon_cryptography_primitives_internaldafny_types.AES__GCM_AES__GCM(32, 16, 12), _dafny.Seq([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]), _dafny.Seq([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), _dafny.Seq([97, 115, 100, 102]), _dafny.Seq([3, 3, 3, 3])))

    @staticmethod
    def BasicAESDecryptTest(input, expectedOutput):
        d_113_client_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_114_valueOrError0_: Wrappers.Result = None
        out21_: Wrappers.Result
        out21_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_114_valueOrError0_ = out21_
        if not(not((d_114_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestAES.dfy(99,18): " + _dafny.string_of(d_114_valueOrError0_))
        d_113_client_ = (d_114_valueOrError0_).Extract()
        d_115_output_: _dafny.Seq
        d_116_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out22_: Wrappers.Result
        out22_ = (d_113_client_).AESDecrypt(input)
        d_116_valueOrError1_ = out22_
        if not(not((d_116_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestAES.dfy(100,18): " + _dafny.string_of(d_116_valueOrError1_))
        d_115_output_ = (d_116_valueOrError1_).Extract()
        if not((d_115_output_) == (expectedOutput)):
            raise _dafny.HaltException("test/TestAES.dfy(101,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def BasicAESEncryptTest(input):
        d_117_client_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_118_valueOrError0_: Wrappers.Result = None
        out23_: Wrappers.Result
        out23_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_118_valueOrError0_ = out23_
        if not(not((d_118_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestAES.dfy(108,18): " + _dafny.string_of(d_118_valueOrError0_))
        d_117_client_ = (d_118_valueOrError0_).Extract()
        d_119_output_: software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput
        d_120_valueOrError1_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput.default())()
        out24_: Wrappers.Result
        out24_ = (d_117_client_).AESEncrypt(input)
        d_120_valueOrError1_ = out24_
        if not(not((d_120_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestAES.dfy(109,18): " + _dafny.string_of(d_120_valueOrError1_))
        d_119_output_ = (d_120_valueOrError1_).Extract()
        d_121_decryptInput_: software_amazon_cryptography_primitives_internaldafny_types.AESDecryptInput
        d_121_decryptInput_ = software_amazon_cryptography_primitives_internaldafny_types.AESDecryptInput_AESDecryptInput((input).encAlg, (input).key, (d_119_output_).cipherText, (d_119_output_).authTag, (input).iv, (input).aad)
        default__.BasicAESDecryptTest(d_121_decryptInput_, (input).msg)

