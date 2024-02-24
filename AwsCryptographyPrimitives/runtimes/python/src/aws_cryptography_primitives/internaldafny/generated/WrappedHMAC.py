import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_MergeSort
import Math
import Seq
import BoundedInts
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
import StandardLibrary_UInt
import StandardLibrary_String
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
import software_amazon_cryptography_primitives_internaldafny_types
import ExternRandom
import Random
import AESEncryption
import ExternDigest
import Digest
import HMAC

# Module: WrappedHMAC

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Digest(input):
        d_30_valueOrError0_ = Wrappers.default__.Need((0) < (len((input).key)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Key MUST NOT be 0 bytes.")))
        if (d_30_valueOrError0_).IsFailure():
            return (d_30_valueOrError0_).PropagateFailure()
        elif True:
            d_31_valueOrError1_ = Wrappers.default__.Need((len((input).message)) < (StandardLibrary_UInt.default__.INT32__MAX__LIMIT), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Message over INT32_MAX_LIMIT")))
            if (d_31_valueOrError1_).IsFailure():
                return (d_31_valueOrError1_).PropagateFailure()
            elif True:
                d_32_valueOrError2_ = HMAC.default__.Digest(input)
                if (d_32_valueOrError2_).IsFailure():
                    return (d_32_valueOrError2_).PropagateFailure()
                elif True:
                    d_33_value_ = (d_32_valueOrError2_).Extract()
                    return Wrappers.Result_Success(d_33_value_)

