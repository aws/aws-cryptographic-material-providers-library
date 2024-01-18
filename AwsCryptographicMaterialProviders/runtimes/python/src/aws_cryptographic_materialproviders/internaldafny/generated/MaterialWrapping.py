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
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_primitives_internaldafny_types
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
import Relations
import Seq_MergeSort
import Math
import Seq
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
import UUID
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
import software_amazon_cryptography_keystore_internaldafny_types
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
import Com_Amazonaws
import Com
import software_amazon_cryptography_keystore_internaldafny
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsKmsMrkAreUnique
import Constants
import software_amazon_cryptography_primitives_internaldafny
import Aws_Cryptography
import Aws

# Module: MaterialWrapping


class GenerateAndWrapInput:
    @classmethod
    def default(cls, ):
        return lambda: GenerateAndWrapInput_GenerateAndWrapInput(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo.default()(), _dafny.Map({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GenerateAndWrapInput(self) -> bool:
        return isinstance(self, GenerateAndWrapInput_GenerateAndWrapInput)

class GenerateAndWrapInput_GenerateAndWrapInput(GenerateAndWrapInput, NamedTuple('GenerateAndWrapInput', [('algorithmSuite', Any), ('encryptionContext', Any)])):
    def __dafnystr__(self) -> str:
        return f'MaterialWrapping.GenerateAndWrapInput.GenerateAndWrapInput({_dafny.string_of(self.algorithmSuite)}, {_dafny.string_of(self.encryptionContext)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GenerateAndWrapInput_GenerateAndWrapInput) and self.algorithmSuite == __o.algorithmSuite and self.encryptionContext == __o.encryptionContext
    def __hash__(self) -> int:
        return super().__hash__()


class GenerateAndWrapOutput:
    @classmethod
    def default(cls, default_T):
        return lambda: GenerateAndWrapOutput_GenerateAndWrapOutput(_dafny.Seq({}), _dafny.Seq({}), default_T())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GenerateAndWrapOutput(self) -> bool:
        return isinstance(self, GenerateAndWrapOutput_GenerateAndWrapOutput)

class GenerateAndWrapOutput_GenerateAndWrapOutput(GenerateAndWrapOutput, NamedTuple('GenerateAndWrapOutput', [('plaintextMaterial', Any), ('wrappedMaterial', Any), ('wrapInfo', Any)])):
    def __dafnystr__(self) -> str:
        return f'MaterialWrapping.GenerateAndWrapOutput.GenerateAndWrapOutput({_dafny.string_of(self.plaintextMaterial)}, {_dafny.string_of(self.wrappedMaterial)}, {_dafny.string_of(self.wrapInfo)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, GenerateAndWrapOutput_GenerateAndWrapOutput) and self.plaintextMaterial == __o.plaintextMaterial and self.wrappedMaterial == __o.wrappedMaterial and self.wrapInfo == __o.wrapInfo
    def __hash__(self) -> int:
        return super().__hash__()


class WrapInput:
    @classmethod
    def default(cls, ):
        return lambda: WrapInput_WrapInput(_dafny.Seq({}), software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo.default()(), _dafny.Map({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_WrapInput(self) -> bool:
        return isinstance(self, WrapInput_WrapInput)

class WrapInput_WrapInput(WrapInput, NamedTuple('WrapInput', [('plaintextMaterial', Any), ('algorithmSuite', Any), ('encryptionContext', Any)])):
    def __dafnystr__(self) -> str:
        return f'MaterialWrapping.WrapInput.WrapInput({_dafny.string_of(self.plaintextMaterial)}, {_dafny.string_of(self.algorithmSuite)}, {_dafny.string_of(self.encryptionContext)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, WrapInput_WrapInput) and self.plaintextMaterial == __o.plaintextMaterial and self.algorithmSuite == __o.algorithmSuite and self.encryptionContext == __o.encryptionContext
    def __hash__(self) -> int:
        return super().__hash__()


class WrapOutput:
    @classmethod
    def default(cls, default_T):
        return lambda: WrapOutput_WrapOutput(_dafny.Seq({}), default_T())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_WrapOutput(self) -> bool:
        return isinstance(self, WrapOutput_WrapOutput)

class WrapOutput_WrapOutput(WrapOutput, NamedTuple('WrapOutput', [('wrappedMaterial', Any), ('wrapInfo', Any)])):
    def __dafnystr__(self) -> str:
        return f'MaterialWrapping.WrapOutput.WrapOutput({_dafny.string_of(self.wrappedMaterial)}, {_dafny.string_of(self.wrapInfo)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, WrapOutput_WrapOutput) and self.wrappedMaterial == __o.wrappedMaterial and self.wrapInfo == __o.wrapInfo
    def __hash__(self) -> int:
        return super().__hash__()


class UnwrapInput:
    @classmethod
    def default(cls, ):
        return lambda: UnwrapInput_UnwrapInput(_dafny.Seq({}), software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo.default()(), _dafny.Map({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_UnwrapInput(self) -> bool:
        return isinstance(self, UnwrapInput_UnwrapInput)

class UnwrapInput_UnwrapInput(UnwrapInput, NamedTuple('UnwrapInput', [('wrappedMaterial', Any), ('algorithmSuite', Any), ('encryptionContext', Any)])):
    def __dafnystr__(self) -> str:
        return f'MaterialWrapping.UnwrapInput.UnwrapInput({_dafny.string_of(self.wrappedMaterial)}, {_dafny.string_of(self.algorithmSuite)}, {_dafny.string_of(self.encryptionContext)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, UnwrapInput_UnwrapInput) and self.wrappedMaterial == __o.wrappedMaterial and self.algorithmSuite == __o.algorithmSuite and self.encryptionContext == __o.encryptionContext
    def __hash__(self) -> int:
        return super().__hash__()


class UnwrapOutput:
    @classmethod
    def default(cls, default_T):
        return lambda: UnwrapOutput_UnwrapOutput(_dafny.Seq({}), default_T())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_UnwrapOutput(self) -> bool:
        return isinstance(self, UnwrapOutput_UnwrapOutput)

class UnwrapOutput_UnwrapOutput(UnwrapOutput, NamedTuple('UnwrapOutput', [('unwrappedMaterial', Any), ('unwrapInfo', Any)])):
    def __dafnystr__(self) -> str:
        return f'MaterialWrapping.UnwrapOutput.UnwrapOutput({_dafny.string_of(self.unwrappedMaterial)}, {_dafny.string_of(self.unwrapInfo)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, UnwrapOutput_UnwrapOutput) and self.unwrappedMaterial == __o.unwrappedMaterial and self.unwrapInfo == __o.unwrapInfo
    def __hash__(self) -> int:
        return super().__hash__()


class GenerateAndWrapMaterial:
    pass

class WrapMaterial:
    pass

class UnwrapMaterial:
    pass
