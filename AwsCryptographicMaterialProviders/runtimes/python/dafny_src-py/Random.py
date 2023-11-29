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
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import AwsArnParsing
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
import Structure
import KMSKeystoreOperations
import DDBKeystoreOperations
import CreateKeys
import CreateKeyStoreTable
import GetKeys
import AwsCryptographyKeyStoreOperations
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import software_amazon_cryptography_keystore_internaldafny
import ExternRandom

assert "Random" == __name__
Random = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def GenerateBytes(i):
        res: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        d_287_value_: _dafny.Seq
        d_288_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out54_: Wrappers.Result
        out54_ = ExternRandom.default__.GenerateBytes(i)
        d_288_valueOrError0_ = out54_
        if (d_288_valueOrError0_).IsFailure():
            res = (d_288_valueOrError0_).PropagateFailure()
            return res
        d_287_value_ = (d_288_valueOrError0_).Extract()
        d_289_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_289_valueOrError1_ = Wrappers.default__.Need((len(d_287_value_)) == (i), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Incorrect length from ExternRandom.")))
        if (d_289_valueOrError1_).IsFailure():
            res = (d_289_valueOrError1_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(d_287_value_)
        return res
        return res

