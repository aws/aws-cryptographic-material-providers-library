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
import software_amazon_cryptography_primitives_internaldafny_types
import ExternRandom

# Module: Random

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def GenerateBytes(i):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_0_value_: _dafny.Seq
        d_1_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out0_: Wrappers.Result
        out0_ = ExternRandom.default__.GenerateBytes(i)
        d_1_valueOrError0_ = out0_
        if (d_1_valueOrError0_).IsFailure():
            res = (d_1_valueOrError0_).PropagateFailure()
            return res
        d_0_value_ = (d_1_valueOrError0_).Extract()
        d_2_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_2_valueOrError1_ = Wrappers.default__.Need((len(d_0_value_)) == (i), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Incorrect length from ExternRandom.")))
        if (d_2_valueOrError1_).IsFailure():
            res = (d_2_valueOrError1_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(d_0_value_)
        return res
        return res

