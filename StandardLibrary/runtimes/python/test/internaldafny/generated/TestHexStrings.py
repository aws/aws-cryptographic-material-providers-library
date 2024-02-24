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
import TestUTF8
import TestTime
import TestComputeSetToOrderedSequenceCharLess
import Sets

# Module: TestHexStrings

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def BasicTests():
        if not((HexStrings.default__.ToHexString(_dafny.Seq([1, 2, 255]))) == (_dafny.Seq("0102ff"))):
            raise _dafny.HaltException("test/HexStrings.dfy(11,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((HexStrings.default__.FromHexString(_dafny.Seq("0102ff"))) == (_dafny.Seq([1, 2, 255]))):
            raise _dafny.HaltException("test/HexStrings.dfy(12,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

