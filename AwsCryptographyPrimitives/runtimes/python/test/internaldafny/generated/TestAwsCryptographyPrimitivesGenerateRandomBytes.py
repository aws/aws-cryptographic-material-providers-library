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

# Module: TestAwsCryptographyPrimitivesGenerateRandomBytes

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def BasicGenerateRandomBytes():
        d_34_client_: software_amazon_cryptography_primitives_internaldafny_types.IAwsCryptographicPrimitivesClient
        d_35_valueOrError0_: Wrappers.Result = None
        out9_: Wrappers.Result
        out9_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_35_valueOrError0_ = out9_
        if not(not((d_35_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestGenerateRandomBytes.dfy(11,15): " + _dafny.string_of(d_35_valueOrError0_))
        d_34_client_ = (d_35_valueOrError0_).Extract()
        d_36_length_: int
        d_36_length_ = 5
        d_37_input_: software_amazon_cryptography_primitives_internaldafny_types.GenerateRandomBytesInput
        d_37_input_ = software_amazon_cryptography_primitives_internaldafny_types.GenerateRandomBytesInput_GenerateRandomBytesInput(d_36_length_)
        d_38_output_: Wrappers.Result
        out10_: Wrappers.Result
        out10_ = (d_34_client_).GenerateRandomBytes(d_37_input_)
        d_38_output_ = out10_
        d_39_value_: _dafny.Seq
        d_40_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_40_valueOrError1_ = d_38_output_
        if not(not((d_40_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestGenerateRandomBytes.dfy(20,14): " + _dafny.string_of(d_40_valueOrError1_))
        d_39_value_ = (d_40_valueOrError1_).Extract()
        if not((len(d_39_value_)) == (d_36_length_)):
            raise _dafny.HaltException("test/TestGenerateRandomBytes.dfy(21,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

