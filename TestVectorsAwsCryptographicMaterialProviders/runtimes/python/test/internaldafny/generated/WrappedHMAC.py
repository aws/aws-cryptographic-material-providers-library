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
import Digest
import HMAC

# Module: WrappedHMAC

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Digest(input):
        d_235_valueOrError0_ = Wrappers.default__.Need((0) < (len((input).key)), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Key MUST NOT be 0 bytes.")))
        if (d_235_valueOrError0_).IsFailure():
            return (d_235_valueOrError0_).PropagateFailure()
        elif True:
            d_236_valueOrError1_ = Wrappers.default__.Need((len((input).message)) < (StandardLibrary_mUInt.default__.INT32__MAX__LIMIT), software_amazon_cryptography_primitives_internaldafny_types.Error_AwsCryptographicPrimitivesError(_dafny.Seq("Message over INT32_MAX_LIMIT")))
            if (d_236_valueOrError1_).IsFailure():
                return (d_236_valueOrError1_).PropagateFailure()
            elif True:
                d_237_valueOrError2_ = HMAC.default__.Digest(input)
                if (d_237_valueOrError2_).IsFailure():
                    return (d_237_valueOrError2_).PropagateFailure()
                elif True:
                    d_238_value_ = (d_237_valueOrError2_).Extract()
                    return Wrappers.Result_Success(d_238_value_)

