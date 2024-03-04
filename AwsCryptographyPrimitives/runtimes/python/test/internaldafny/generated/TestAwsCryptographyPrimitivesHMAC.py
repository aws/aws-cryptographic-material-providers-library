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
import TestAwsCryptographyPrimitivesAES

# Module: TestAwsCryptographyPrimitivesHMAC

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def HMACTests():
        default__.BasicHMACTest(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__256(), _dafny.Seq([1, 2, 3, 4]), _dafny.Seq([97, 115, 100, 102]), _dafny.Seq([55, 107, 186, 241, 51, 255, 154, 169, 106, 133, 2, 248, 54, 230, 193, 147, 212, 179, 154, 66, 43, 52, 108, 181, 144, 152, 19, 101, 117, 99, 204, 134]))
        default__.BasicHMACTest(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__384(), _dafny.Seq([1, 2, 3, 4]), _dafny.Seq([97, 115, 100, 102]), _dafny.Seq([90, 206, 234, 81, 173, 76, 235, 148, 203, 139, 195, 46, 251, 14, 97, 110, 146, 49, 147, 24, 240, 1, 17, 231, 58, 104, 146, 53, 144, 167, 11, 112, 7, 39, 122, 15, 58, 53, 144, 91, 16, 223, 51, 98, 30, 88, 23, 166]))
        default__.BasicHMACTest(software_amazon_cryptography_primitives_internaldafny_types.DigestAlgorithm_SHA__512(), _dafny.Seq([1, 2, 3, 4]), _dafny.Seq([97, 115, 100, 102]), _dafny.Seq([100, 23, 173, 215, 39, 67, 51, 165, 149, 53, 87, 84, 145, 58, 221, 155, 239, 182, 249, 134, 147, 191, 143, 224, 140, 165, 190, 221, 183, 15, 6, 102, 203, 77, 238, 64, 10, 138, 61, 64, 219, 79, 248, 249, 90, 102, 217, 188, 13, 2, 101, 96, 217, 242, 73, 254, 190, 217, 134, 33, 163, 137, 151, 183]))

    @staticmethod
    def BasicHMACTest(digestAlgorithm, key, message, expectedDigest):
        d_122_client_: software_amazon_cryptography_primitives_internaldafny_types.IAwsCryptographicPrimitivesClient
        d_123_valueOrError0_: Wrappers.Result = None
        out25_: Wrappers.Result
        out25_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_123_valueOrError0_ = out25_
        if not(not((d_123_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHMAC.dfy(66,15): " + _dafny.string_of(d_123_valueOrError0_))
        d_122_client_ = (d_123_valueOrError0_).Extract()
        d_124_input_: software_amazon_cryptography_primitives_internaldafny_types.HMacInput
        d_124_input_ = software_amazon_cryptography_primitives_internaldafny_types.HMacInput_HMacInput(digestAlgorithm, key, message)
        d_125_output_: _dafny.Seq
        d_126_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_126_valueOrError1_ = (d_122_client_).HMac(d_124_input_)
        if not(not((d_126_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHMAC.dfy(74,15): " + _dafny.string_of(d_126_valueOrError1_))
        d_125_output_ = (d_126_valueOrError1_).Extract()
        if not((len(d_125_output_)) == (Digest.default__.Length(digestAlgorithm))):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHMAC.dfy(75,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_125_output_) == (expectedDigest)):
            raise _dafny.HaltException("test/TestAwsCryptographyPrimitivesHMAC.dfy(76,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

