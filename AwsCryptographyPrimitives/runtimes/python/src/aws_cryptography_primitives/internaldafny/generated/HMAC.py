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
import GetOpt
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
import software.amazon.cryptography.primitives.internaldafny.types
import ExternRandom
import Random
import AESEncryption
import ExternDigest
import Digest

# Module: HMAC

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def CreateDigestSuccess(bytes):
        return Wrappers.Result_Success(bytes)

    @staticmethod
    def CreateDigestFailure(error):
        return Wrappers.Result_Failure(error)


class HMac:
    def  __init__(self):
        pass

    def __dafnystr__(self) -> str:
        return "HMAC.HMac"
    @staticmethod
    def CreateHMacSuccess(hmac):
        return Wrappers.Result_Success(hmac)

    @staticmethod
    def CreateHMacFailure(error):
        return Wrappers.Result_Failure(error)

