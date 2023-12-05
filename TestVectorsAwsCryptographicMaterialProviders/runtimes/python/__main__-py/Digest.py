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
import DafnyLibraries
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsArnParsing
import AwsKmsMrkAreUnique
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
import Constants
import ExternRandom
import Random
import AESEncryption
import ExternDigest

# Module: Digest

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Length(digestAlgorithm):
        source17_ = digestAlgorithm
        if source17_.is_SHA__512:
            return 64
        elif source17_.is_SHA__384:
            return 48
        elif True:
            return 32

    @staticmethod
    def Digest(input):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        let_tmp_rhs2_ = input
        d_230_digestAlgorithm_ = let_tmp_rhs2_.digestAlgorithm
        d_231_message_ = let_tmp_rhs2_.message
        d_232_value_: _dafny.Seq
        d_233_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out20_: Wrappers.Result
        out20_ = ExternDigest.default__.Digest(d_230_digestAlgorithm_, d_231_message_)
        d_233_valueOrError0_ = out20_
        if (d_233_valueOrError0_).IsFailure():
            res = (d_233_valueOrError0_).PropagateFailure()
            return res
        d_232_value_ = (d_233_valueOrError0_).Extract()
        d_234_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_234_valueOrError1_ = Wrappers.default__.Need((len(d_232_value_)) == (default__.Length(d_230_digestAlgorithm_)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Incorrect length digest from ExternDigest.")))
        if (d_234_valueOrError1_).IsFailure():
            res = (d_234_valueOrError1_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(d_232_value_)
        return res
        return res

