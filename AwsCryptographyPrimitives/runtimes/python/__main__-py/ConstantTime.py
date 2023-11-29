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

assert "ConstantTime" == __name__
ConstantTime = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Compare(a, b, acc):
        while True:
            with _dafny.label():
                if (len(a)) == (0):
                    return acc
                elif True:
                    d_146_x_ = ((a)[0]) ^ ((b)[0])
                    in0_ = _dafny.Seq((a)[1::])
                    in1_ = _dafny.Seq((b)[1::])
                    in2_ = (d_146_x_) | (acc)
                    a = in0_
                    b = in1_
                    acc = in2_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def Equals(a, b):
        return (ConstantTime.default__.Compare(a, b, 0)) == (0)

