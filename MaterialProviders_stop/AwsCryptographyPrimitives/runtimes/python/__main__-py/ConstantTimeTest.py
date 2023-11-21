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

assert "ConstantTimeTest" == __name__
ConstantTimeTest = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def ConstantTimeTest():
        if not(ConstantTime.default__.Equals(_dafny.Seq([]), _dafny.Seq([]))):
            raise _dafny.HaltException("test/ConstantTime.dfy(10,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(ConstantTime.default__.Equals(_dafny.Seq([1]), _dafny.Seq([1]))):
            raise _dafny.HaltException("test/ConstantTime.dfy(11,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(not(ConstantTime.default__.Equals(_dafny.Seq([1]), _dafny.Seq([2])))):
            raise _dafny.HaltException("test/ConstantTime.dfy(12,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(ConstantTime.default__.Equals(_dafny.Seq([1, 2, 3]), _dafny.Seq([1, 2, 3]))):
            raise _dafny.HaltException("test/ConstantTime.dfy(13,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(not(ConstantTime.default__.Equals(_dafny.Seq([2, 2, 3]), _dafny.Seq([1, 2, 3])))):
            raise _dafny.HaltException("test/ConstantTime.dfy(14,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not(not(ConstantTime.default__.Equals(_dafny.Seq([1, 2, 3]), _dafny.Seq([1, 2, 4])))):
            raise _dafny.HaltException("test/ConstantTime.dfy(15,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

