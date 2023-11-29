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
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
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
import software_amazon_cryptography_keystore_internaldafny
import Fixtures
import TestCreateKeyStore
import ExternRandom
import Random
import AESEncryption
import ExternDigest

# assert "Digest" == __name__
Digest = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Length(digestAlgorithm):
        source10_ = digestAlgorithm
        if source10_.is_SHA__512:
            return 64
        elif source10_.is_SHA__384:
            return 48
        elif True:
            return 32

    @staticmethod
    def Digest(input):
        res: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        let_tmp_rhs2_ = input
        d_322_digestAlgorithm_ = let_tmp_rhs2_.digestAlgorithm
        d_323_message_ = let_tmp_rhs2_.message
        d_324_value_: _dafny.Seq
        d_325_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(_dafny.Seq)()
        out61_: Wrappers.Result
        out61_ = ExternDigest.default__.Digest(d_322_digestAlgorithm_, d_323_message_)
        d_325_valueOrError0_ = out61_
        if (d_325_valueOrError0_).IsFailure():
            res = (d_325_valueOrError0_).PropagateFailure()
            return res
        d_324_value_ = (d_325_valueOrError0_).Extract()
        d_326_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_326_valueOrError1_ = Wrappers.default__.Need((len(d_324_value_)) == (Digest.default__.Length(d_322_digestAlgorithm_)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Incorrect length digest from ExternDigest.")))
        if (d_326_valueOrError1_).IsFailure():
            res = (d_326_valueOrError1_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(d_324_value_)
        return res
        return res

