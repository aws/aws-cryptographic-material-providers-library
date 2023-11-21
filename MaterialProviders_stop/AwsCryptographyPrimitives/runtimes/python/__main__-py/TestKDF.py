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

assert "TestKDF" == __name__
TestKDF = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def KdfRawDeriveTest(ikm, info, L, expectedOKM):
        d_156_output_: Wrappers.Result
        out62_: Wrappers.Result
        out62_ = KdfCtr.default__.RawDerive(ikm, info, L, 0)
        d_156_output_ = out62_
        if (d_156_output_).is_Success:
            if not((len((d_156_output_).value)) == (L)):
                raise _dafny.HaltException("test/TestKDF.dfy(30,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            if not(((d_156_output_).value) == (expectedOKM)):
                raise _dafny.HaltException("test/TestKDF.dfy(31,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def KdfTest(input, expectedOKM):
        d_157_client_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_158_valueOrError0_: Wrappers.Result = None
        out63_: Wrappers.Result
        out63_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_158_valueOrError0_ = out63_
        if not(not((d_158_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestKDF.dfy(40,15): " + _dafny.string_of(d_158_valueOrError0_))
        d_157_client_ = (d_158_valueOrError0_).Extract()
        d_159_output_: _dafny.Seq
        d_160_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out64_: Wrappers.Result
        out64_ = (d_157_client_).KdfCounterMode(input)
        d_160_valueOrError1_ = out64_
        if not(not((d_160_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestKDF.dfy(42,15): " + _dafny.string_of(d_160_valueOrError1_))
        d_159_output_ = (d_160_valueOrError1_).Extract()
        if not((len(d_159_output_)) == ((input).expectedLength)):
            raise _dafny.HaltException("test/TestKDF.dfy(43,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_159_output_) == (expectedOKM)):
            raise _dafny.HaltException("test/TestKDF.dfy(44,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

