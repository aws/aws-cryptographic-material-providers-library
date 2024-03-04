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

# Module: ConstantTime

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
                    d_41_x_ = ((a)[0]) ^ ((b)[0])
                    in0_ = _dafny.Seq((a)[1::])
                    in1_ = _dafny.Seq((b)[1::])
                    in2_ = (d_41_x_) | (acc)
                    a = in0_
                    b = in1_
                    acc = in2_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def Equals(a, b):
        return (default__.Compare(a, b, 0)) == (0)

