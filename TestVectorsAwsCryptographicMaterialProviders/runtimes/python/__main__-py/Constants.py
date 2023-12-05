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

# Module: Constants

class default__:
    def  __init__(self):
        pass

    @_dafny.classproperty
    def PROVIDER__ID(instance):
        d_202_s_ = _dafny.Seq([97, 119, 115, 45, 107, 109, 115])
        return d_202_s_
    @_dafny.classproperty
    def PROVIDER__ID__HIERARCHY(instance):
        d_203_s_ = _dafny.Seq([97, 119, 115, 45, 107, 109, 115, 45, 104, 105, 101, 114, 97, 114, 99, 104, 121])
        return d_203_s_
    @_dafny.classproperty
    def RSA__PROVIDER__ID(instance):
        d_204_s_ = _dafny.Seq([97, 119, 115, 45, 107, 109, 115, 45, 114, 115, 97])
        return d_204_s_

class AwsKmsEncryptedDataKey:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey.default()()

class AwsKmsEdkHelper:
    @classmethod
    def default(cls, ):
        return lambda: AwsKmsEdkHelper_AwsKmsEdkHelper(software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey.default()(), AwsArnParsing.AwsArn.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AwsKmsEdkHelper(self) -> bool:
        return isinstance(self, AwsKmsEdkHelper_AwsKmsEdkHelper)

class AwsKmsEdkHelper_AwsKmsEdkHelper(AwsKmsEdkHelper, NamedTuple('AwsKmsEdkHelper', [('edk', Any), ('arn', Any)])):
    def __dafnystr__(self) -> str:
        return f'Constants.AwsKmsEdkHelper.AwsKmsEdkHelper({_dafny.string_of(self.edk)}, {_dafny.string_of(self.arn)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AwsKmsEdkHelper_AwsKmsEdkHelper) and self.edk == __o.edk and self.arn == __o.arn
    def __hash__(self) -> int:
        return super().__hash__()

