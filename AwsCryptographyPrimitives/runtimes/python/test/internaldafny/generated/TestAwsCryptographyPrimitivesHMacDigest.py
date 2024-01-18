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
import Relations
import Seq_MergeSort
import Math
import Seq
import Unicode
import Functions
import Utf8EncodingForm
import Utf16EncodingForm
import UnicodeStrings
import DafnyLibraries
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
import UUID
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
import TestAwsCryptographyPrimitivesAES
import TestAwsCryptographyPrimitivesHMAC
import TestAwsCryptographyPrimitivesDigest

# Module: TestAwsCryptographyPrimitivesHMacDigest

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DigestTests():
        d_132_client_: software_amazon_cryptography_primitives_internaldafny_types.IAwsCryptographicPrimitivesClient
        d_133_valueOrError0_: Wrappers.Result = None
        out28_: Wrappers.Result
        out28_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_133_valueOrError0_ = out28_
        if not(not((d_133_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestHMAC.dfy(14,15): " + _dafny.string_of(d_133_valueOrError0_))
        d_132_client_ = (d_133_valueOrError0_).Extract()
        default__.HmacSHA__256(d_132_client_)
        default__.HmacSHA__384(d_132_client_)
        default__.HmacSHA__512(d_132_client_)

    @staticmethod
    def HmacSHA__256(client):
        d_134___v0_: tuple
        d_135_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_135_valueOrError0_ = default__.BasicHMacTest(client, software_amazon_cryptography_primitives_internaldafny_types.HMacInput_HMacInput(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__256(), _dafny.Seq([1, 1, 1, 1]), _dafny.Seq([97, 115, 100, 102])), _dafny.Seq([93, 12, 86, 145, 123, 239, 169, 72, 195, 226, 204, 179, 103, 94, 195, 83, 134, 128, 226, 185, 184, 203, 98, 100, 115, 32, 7, 44, 172, 11, 81, 16]))
        if not(not((d_135_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestHMAC.dfy(26,10): " + _dafny.string_of(d_135_valueOrError0_))
        d_134___v0_ = (d_135_valueOrError0_).Extract()

    @staticmethod
    def HmacSHA__384(client):
        d_136___v1_: tuple
        d_137_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_137_valueOrError0_ = default__.BasicHMacTest(client, software_amazon_cryptography_primitives_internaldafny_types.HMacInput_HMacInput(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__384(), _dafny.Seq([1, 1, 1, 1]), _dafny.Seq([97, 115, 100, 102])), _dafny.Seq([219, 44, 51, 60, 217, 57, 186, 208, 8, 69, 115, 185, 190, 136, 136, 1, 69, 143, 151, 148, 7, 66, 149, 193, 16, 225, 51, 85, 92, 176, 139, 249, 56, 93, 189, 11, 150, 21, 135, 54, 153, 37, 76, 68, 70, 77, 154, 124]))
        if not(not((d_137_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestHMAC.dfy(47,10): " + _dafny.string_of(d_137_valueOrError0_))
        d_136___v1_ = (d_137_valueOrError0_).Extract()

    @staticmethod
    def HmacSHA__512(client):
        d_138___v2_: tuple
        d_139_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_139_valueOrError0_ = default__.BasicHMacTest(client, software_amazon_cryptography_primitives_internaldafny_types.HMacInput_HMacInput(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__512(), _dafny.Seq([1, 1, 1, 1]), _dafny.Seq([97, 115, 100, 102])), _dafny.Seq([49, 213, 21, 219, 23, 169, 195, 39, 177, 1, 15, 162, 233, 182, 208, 84, 226, 3, 27, 120, 75, 78, 85, 46, 220, 5, 166, 206, 79, 47, 25, 94, 88, 119, 211, 192, 148, 23, 252, 155, 98, 218, 97, 225, 38, 93, 83, 113, 139, 95, 101, 222, 154, 98, 244, 206, 88, 229, 6, 115, 226, 188, 152, 173]))
        if not(not((d_139_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestHMAC.dfy(69,10): " + _dafny.string_of(d_139_valueOrError0_))
        d_138___v2_ = (d_139_valueOrError0_).Extract()

    @staticmethod
    def BasicHMacTest(client, input, expectedDigest):
        d_140_valueOrError0_ = (client).HMac(input)
        if (d_140_valueOrError0_).IsFailure():
            return (d_140_valueOrError0_).PropagateFailure()
        elif True:
            d_141_output_ = (d_140_valueOrError0_).Extract()
            d_142_valueOrError1_ = Wrappers.default__.Need((len(d_141_output_)) == (Digest.default__.Length((input).digestAlgorithm)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Error")))
            if (d_142_valueOrError1_).IsFailure():
                return (d_142_valueOrError1_).PropagateFailure()
            elif True:
                d_143_valueOrError2_ = Wrappers.default__.Need((d_141_output_) == (expectedDigest), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Error")))
                if (d_143_valueOrError2_).IsFailure():
                    return (d_143_valueOrError2_).PropagateFailure()
                elif True:
                    return Wrappers.Result_Success(())

