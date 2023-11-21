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

assert "TestAwsCryptographyPrimitivesHMAC" == __name__
TestAwsCryptographyPrimitivesHMAC = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def HMACTests():
        TestAwsCryptographyPrimitivesHMAC.default__.BasicHMACTest(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__256(), _dafny.Seq([1, 2, 3, 4]), _dafny.Seq([97, 115, 100, 102]), _dafny.Seq([55, 107, 186, 241, 51, 255, 154, 169, 106, 133, 2, 248, 54, 230, 193, 147, 212, 179, 154, 66, 43, 52, 108, 181, 144, 152, 19, 101, 117, 99, 204, 134]))
        TestAwsCryptographyPrimitivesHMAC.default__.BasicHMACTest(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__384(), _dafny.Seq([1, 2, 3, 4]), _dafny.Seq([97, 115, 100, 102]), _dafny.Seq([90, 206, 234, 81, 173, 76, 235, 148, 203, 139, 195, 46, 251, 14, 97, 110, 146, 49, 147, 24, 240, 1, 17, 231, 58, 104, 146, 53, 144, 167, 11, 112, 7, 39, 122, 15, 58, 53, 144, 91, 16, 223, 51, 98, 30, 88, 23, 166]))
        TestAwsCryptographyPrimitivesHMAC.default__.BasicHMACTest(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__512(), _dafny.Seq([1, 2, 3, 4]), _dafny.Seq([97, 115, 100, 102]), _dafny.Seq([100, 23, 173, 215, 39, 67, 51, 165, 149, 53, 87, 84, 145, 58, 221, 155, 239, 182, 249, 134, 147, 191, 143, 224, 140, 165, 190, 221, 183, 15, 6, 102, 203, 77, 238, 64, 10, 138, 61, 64, 219, 79, 248, 249, 90, 102, 217, 188, 13, 2, 101, 96, 217, 242, 73, 254, 190, 217, 134, 33, 163, 137, 151, 183]))

    @staticmethod
    def BasicHMACTest(digestAlgorithm, key, message, expectedDigest):
        d_227_client_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_228_valueOrError0_: Wrappers.Result = None
        out76_: Wrappers.Result
        out76_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_228_valueOrError0_ = out76_
        if not(not((d_228_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHMAC.dfy(66,15): " + _dafny.string_of(d_228_valueOrError0_))
        d_227_client_ = (d_228_valueOrError0_).Extract()
        d_229_input_: software_amazon_cryptography_primitives_internaldafny_types.HMacInput
        d_229_input_ = software_amazon_cryptography_primitives_internaldafny_types.HMacInput_HMacInput(digestAlgorithm, key, message)
        d_230_output_: _dafny.Seq
        d_231_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_231_valueOrError1_ = (d_227_client_).HMac(d_229_input_)
        if not(not((d_231_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHMAC.dfy(74,15): " + _dafny.string_of(d_231_valueOrError1_))
        d_230_output_ = (d_231_valueOrError1_).Extract()
        if not((len(d_230_output_)) == (Digest.default__.Length(digestAlgorithm))):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHMAC.dfy(75,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_230_output_) == (expectedDigest)):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHMAC.dfy(76,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

