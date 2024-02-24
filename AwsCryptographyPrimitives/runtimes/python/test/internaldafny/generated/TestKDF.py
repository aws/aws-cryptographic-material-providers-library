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

# Module: TestKDF

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def KdfRawDeriveTest(ikm, info, L, expectedOKM):
        d_51_output_: Wrappers.Result
        out11_: Wrappers.Result
        out11_ = KdfCtr.default__.RawDerive(ikm, info, L, 0)
        d_51_output_ = out11_
        if (d_51_output_).is_Success:
            if not((len((d_51_output_).value)) == (L)):
                raise _dafny.HaltException("test/TestKDF.dfy(30,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))
            if not(((d_51_output_).value) == (expectedOKM)):
                raise _dafny.HaltException("test/TestKDF.dfy(31,6): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def KdfTest(input, expectedOKM):
        d_52_client_: software_amazon_cryptography_primitives_internaldafny_types.IAwsCryptographicPrimitivesClient
        d_53_valueOrError0_: Wrappers.Result = None
        out12_: Wrappers.Result
        out12_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_53_valueOrError0_ = out12_
        if not(not((d_53_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestKDF.dfy(40,15): " + _dafny.string_of(d_53_valueOrError0_))
        d_52_client_ = (d_53_valueOrError0_).Extract()
        d_54_output_: _dafny.Seq
        d_55_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out13_: Wrappers.Result
        out13_ = (d_52_client_).KdfCounterMode(input)
        d_55_valueOrError1_ = out13_
        if not(not((d_55_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestKDF.dfy(42,15): " + _dafny.string_of(d_55_valueOrError1_))
        d_54_output_ = (d_55_valueOrError1_).Extract()
        if not((len(d_54_output_)) == ((input).expectedLength)):
            raise _dafny.HaltException("test/TestKDF.dfy(43,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((d_54_output_) == (expectedOKM)):
            raise _dafny.HaltException("test/TestKDF.dfy(44,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

