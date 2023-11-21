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

assert "TestAwsCryptographyPrimitivesDigest" == __name__
TestAwsCryptographyPrimitivesDigest = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DigestTests():
        TestAwsCryptographyPrimitivesDigest.default__.BasicDigestTest(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__256(), _dafny.Seq([97, 115, 100, 102]), _dafny.Seq([240, 228, 194, 247, 108, 88, 145, 110, 194, 88, 242, 70, 133, 27, 234, 9, 29, 20, 212, 36, 122, 47, 195, 225, 134, 148, 70, 27, 24, 22, 225, 59]))
        TestAwsCryptographyPrimitivesDigest.default__.BasicDigestTest(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__384(), _dafny.Seq([97, 115, 100, 102]), _dafny.Seq([166, 158, 125, 243, 11, 36, 192, 66, 236, 84, 12, 203, 189, 191, 177, 86, 44, 133, 120, 112, 56, 200, 133, 116, 156, 30, 64, 142, 45, 98, 250, 54, 100, 44, 208, 7, 95, 163, 81, 232, 34, 226, 184, 165, 145, 57, 205, 157]))
        TestAwsCryptographyPrimitivesDigest.default__.BasicDigestTest(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__512(), _dafny.Seq([97, 115, 100, 102]), _dafny.Seq([64, 27, 9, 234, 179, 192, 19, 212, 202, 84, 146, 43, 184, 2, 190, 200, 253, 83, 24, 25, 43, 10, 117, 242, 1, 216, 179, 114, 116, 41, 8, 15, 179, 55, 89, 26, 189, 62, 68, 69, 59, 149, 69, 85, 183, 160, 129, 46, 16, 129, 195, 155, 116, 2, 147, 247, 101, 234, 231, 49, 245, 166, 94, 209]))

    @staticmethod
    def BasicDigestTest(digestAlgorithm, message, expectedDigest):
        d_232_client_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_233_valueOrError0_: Wrappers.Result = None
        out77_: Wrappers.Result
        out77_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_233_valueOrError0_ = out77_
        if not(not((d_233_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestDigest.dfy(61,15): " + _dafny.string_of(d_233_valueOrError0_))
        d_232_client_ = (d_233_valueOrError0_).Extract()
        d_234_input_: software_amazon_cryptography_primitives_internaldafny_types.DigestInput
        d_234_input_ = software_amazon_cryptography_primitives_internaldafny_types.DigestInput_DigestInput(digestAlgorithm, message)
        d_235_output_: _dafny.Seq
        d_236_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out78_: Wrappers.Result
        out78_ = (d_232_client_).Digest(d_234_input_)
        d_236_valueOrError1_ = out78_
        if not(not((d_236_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestDigest.dfy(68,15): " + _dafny.string_of(d_236_valueOrError1_))
        d_235_output_ = (d_236_valueOrError1_).Extract()
        if not((len(d_235_output_)) == (Digest.default__.Length(digestAlgorithm))):
            raise _dafny.HaltException("test/TestDigest.dfy(69,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_235_output_) == (expectedDigest)):
            raise _dafny.HaltException("test/TestDigest.dfy(70,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

