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

assert "TestAwsCryptographyPrimitivesGenerateRandomBytes" == __name__
TestAwsCryptographyPrimitivesGenerateRandomBytes = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def BasicGenerateRandomBytes():
        d_139_client_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_140_valueOrError0_: Wrappers.Result = None
        out60_: Wrappers.Result
        out60_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_140_valueOrError0_ = out60_
        if not(not((d_140_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestGenerateRandomBytes.dfy(11,15): " + _dafny.string_of(d_140_valueOrError0_))
        d_139_client_ = (d_140_valueOrError0_).Extract()
        d_141_length_: BoundedInts.int32
        d_141_length_ = 5
        d_142_input_: software_amazon_cryptography_primitives_internaldafny_types.GenerateRandomBytesInput
        d_142_input_ = software_amazon_cryptography_primitives_internaldafny_types.GenerateRandomBytesInput_GenerateRandomBytesInput(d_141_length_)
        d_143_output_: Wrappers.Result
        out61_: Wrappers.Result
        out61_ = (d_139_client_).GenerateRandomBytes(d_142_input_)
        d_143_output_ = out61_
        d_144_value_: _dafny.Seq
        d_145_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_145_valueOrError1_ = d_143_output_
        if not(not((d_145_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestGenerateRandomBytes.dfy(20,14): " + _dafny.string_of(d_145_valueOrError1_))
        d_144_value_ = (d_145_valueOrError1_).Extract()
        if not((len(d_144_value_)) == (d_141_length_)):
            raise _dafny.HaltException("test/TestGenerateRandomBytes.dfy(21,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

