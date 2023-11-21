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
import TestAwsCryptographyPrimitivesAES
import TestAwsCryptographyPrimitivesHMAC
import TestAwsCryptographyPrimitivesDigest

assert "TestAwsCryptographyPrimitivesHMacDigest" == __name__
TestAwsCryptographyPrimitivesHMacDigest = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DigestTests():
        d_237_client_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_238_valueOrError0_: Wrappers.Result = None
        out79_: Wrappers.Result
        out79_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_238_valueOrError0_ = out79_
        if not(not((d_238_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestHMAC.dfy(14,15): " + _dafny.string_of(d_238_valueOrError0_))
        d_237_client_ = (d_238_valueOrError0_).Extract()
        TestAwsCryptographyPrimitivesHMacDigest.default__.HmacSHA__256(d_237_client_)
        TestAwsCryptographyPrimitivesHMacDigest.default__.HmacSHA__384(d_237_client_)
        TestAwsCryptographyPrimitivesHMacDigest.default__.HmacSHA__512(d_237_client_)

    @staticmethod
    def HmacSHA__256(client):
        d_239___v0_: tuple
        d_240_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        d_240_valueOrError0_ = TestAwsCryptographyPrimitivesHMacDigest.default__.BasicHMacTest(client, software_amazon_cryptography_primitives_internaldafny_types.HMacInput_HMacInput(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__256(), _dafny.Seq([1, 1, 1, 1]), _dafny.Seq([97, 115, 100, 102])), _dafny.Seq([93, 12, 86, 145, 123, 239, 169, 72, 195, 226, 204, 179, 103, 94, 195, 83, 134, 128, 226, 185, 184, 203, 98, 100, 115, 32, 7, 44, 172, 11, 81, 16]))
        if not(not((d_240_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestHMAC.dfy(26,10): " + _dafny.string_of(d_240_valueOrError0_))
        d_239___v0_ = (d_240_valueOrError0_).Extract()

    @staticmethod
    def HmacSHA__384(client):
        d_241___v1_: tuple
        d_242_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        d_242_valueOrError0_ = TestAwsCryptographyPrimitivesHMacDigest.default__.BasicHMacTest(client, software_amazon_cryptography_primitives_internaldafny_types.HMacInput_HMacInput(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__384(), _dafny.Seq([1, 1, 1, 1]), _dafny.Seq([97, 115, 100, 102])), _dafny.Seq([219, 44, 51, 60, 217, 57, 186, 208, 8, 69, 115, 185, 190, 136, 136, 1, 69, 143, 151, 148, 7, 66, 149, 193, 16, 225, 51, 85, 92, 176, 139, 249, 56, 93, 189, 11, 150, 21, 135, 54, 153, 37, 76, 68, 70, 77, 154, 124]))
        if not(not((d_242_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestHMAC.dfy(47,10): " + _dafny.string_of(d_242_valueOrError0_))
        d_241___v1_ = (d_242_valueOrError0_).Extract()

    @staticmethod
    def HmacSHA__512(client):
        d_243___v2_: tuple
        d_244_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.defaults.tuple())()
        d_244_valueOrError0_ = TestAwsCryptographyPrimitivesHMacDigest.default__.BasicHMacTest(client, software_amazon_cryptography_primitives_internaldafny_types.HMacInput_HMacInput(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__512(), _dafny.Seq([1, 1, 1, 1]), _dafny.Seq([97, 115, 100, 102])), _dafny.Seq([49, 213, 21, 219, 23, 169, 195, 39, 177, 1, 15, 162, 233, 182, 208, 84, 226, 3, 27, 120, 75, 78, 85, 46, 220, 5, 166, 206, 79, 47, 25, 94, 88, 119, 211, 192, 148, 23, 252, 155, 98, 218, 97, 225, 38, 93, 83, 113, 139, 95, 101, 222, 154, 98, 244, 206, 88, 229, 6, 115, 226, 188, 152, 173]))
        if not(not((d_244_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestHMAC.dfy(69,10): " + _dafny.string_of(d_244_valueOrError0_))
        d_243___v2_ = (d_244_valueOrError0_).Extract()

    @staticmethod
    def BasicHMacTest(client, input, expectedDigest):
        d_245_valueOrError0_ = (client).HMac(input)
        if (d_245_valueOrError0_).IsFailure():
            return (d_245_valueOrError0_).PropagateFailure()
        elif True:
            d_246_output_ = (d_245_valueOrError0_).Extract()
            d_247_valueOrError1_ = Wrappers.default__.Need((len(d_246_output_)) == (Digest.default__.Length((input).digestAlgorithm)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Error")))
            if (d_247_valueOrError1_).IsFailure():
                return (d_247_valueOrError1_).PropagateFailure()
            elif True:
                d_248_valueOrError2_ = Wrappers.default__.Need((d_246_output_) == (expectedDigest), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Error")))
                if (d_248_valueOrError2_).IsFailure():
                    return (d_248_valueOrError2_).PropagateFailure()
                elif True:
                    return Wrappers.Result_Success(())

