import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import BoundedInts
import StandardLibrary_mUInt
import String
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
import software_amazon_cryptography_primitives_internaldafny
import Aws_mCryptography
import Aws
import AesKdfCtr
import TestAwsCryptographyPrimitivesAesKdfCtr
import TestAwsCryptographyPrimitivesHMacDigest
import TestAwsCryptographyPrimitivesDigest
import TestAwsCryptographyPrimitivesHMAC
import TestAwsCryptographyPrimitivesAES
import TestAwsCryptographyPrimitivesRSA
import TestKDF
import TestKDFK__TestVectors
import TestAwsCryptographyPrimitivesHKDF
import TestHKDF__Rfc5869TestVectors
import ConstantTime
import ConstantTimeTest

# assert "TestAwsCryptographyPrimitivesGenerateRandomBytes" == __name__
TestAwsCryptographyPrimitivesGenerateRandomBytes = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def BasicGenerateRandomBytes():
        d_129_client_: software_amazon_cryptography_primitives_internaldafny.AtomicPrimitivesClient
        d_130_valueOrError0_: Wrappers.Result = None
        out24_: Wrappers.Result
        out24_ = software_amazon_cryptography_primitives_internaldafny.default__.AtomicPrimitives(software_amazon_cryptography_primitives_internaldafny.default__.DefaultCryptoConfig())
        d_130_valueOrError0_ = out24_
        if not(not((d_130_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestGenerateRandomBytes.dfy(11,15): " + _dafny.string_of(d_130_valueOrError0_))
        d_129_client_ = (d_130_valueOrError0_).Extract()
        d_131_length_: BoundedInts.int32
        d_131_length_ = 5
        d_132_input_: software_amazon_cryptography_primitives_internaldafny_types.GenerateRandomBytesInput
        d_132_input_ = software_amazon_cryptography_primitives_internaldafny_types.GenerateRandomBytesInput_GenerateRandomBytesInput(d_131_length_)
        d_133_output_: Wrappers.Result
        out25_: Wrappers.Result
        out25_ = (d_129_client_).GenerateRandomBytes(d_132_input_)
        d_133_output_ = out25_
        d_134_value_: _dafny.Seq
        d_135_valueOrError1_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_135_valueOrError1_ = d_133_output_
        if not(not((d_135_valueOrError1_).IsFailure())):
            raise _dafny.HaltException("test/TestGenerateRandomBytes.dfy(20,14): " + _dafny.string_of(d_135_valueOrError1_))
        d_134_value_ = (d_135_valueOrError1_).Extract()
        if not((len(d_134_value_)) == (d_131_length_)):
            raise _dafny.HaltException("test/TestGenerateRandomBytes.dfy(21,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

