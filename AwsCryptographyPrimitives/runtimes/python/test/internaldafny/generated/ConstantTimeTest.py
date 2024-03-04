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
import software.amazon.cryptography.primitives.internaldafny.types
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

# Module: ConstantTimeTest

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

