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
import Digest
import HMAC
import WrappedHMAC
import HKDF
import WrappedHKDF
import Signature
import KdfCtr
import RSAEncryption
import AwsCryptographyPrimitivesOperations
import TestConfig
import TestGetKeys
import CleanupItems
import TestCreateKeys
import TestVersionKey
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsKmsMrkAreUnique
import Constants
import software_amazon_cryptography_primitives_internaldafny
import Aws_mCryptography
import Aws

# assert "MaterialWrapping" == __name__
MaterialWrapping = sys.modules[__name__]


class GenerateAndWrapInput:
    @classmethod
    def default(cls, ):
        return lambda: GenerateAndWrapInput_GenerateAndWrapInput(software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo.default()(), _dafny.Map({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_GenerateAndWrapInput(self) -> bool:
        return isinstance(self, MaterialWrapping.GenerateAndWrapInput_GenerateAndWrapInput)

class GenerateAndWrapInput_GenerateAndWrapInput(GenerateAndWrapInput, NamedTuple('GenerateAndWrapInput', [('algorithmSuite', Any), ('encryptionContext', Any)])):
    def __dafnystr__(self) -> str:
        return f'MaterialWrapping.GenerateAndWrapInput.GenerateAndWrapInput({_dafny.string_of(self.algorithmSuite)}, {_dafny.string_of(self.encryptionContext)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, MaterialWrapping.GenerateAndWrapInput_GenerateAndWrapInput) and self.algorithmSuite == __o.algorithmSuite and self.encryptionContext == __o.encryptionContext
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
        return isinstance(self, MaterialWrapping.GenerateAndWrapOutput_GenerateAndWrapOutput)

class GenerateAndWrapOutput_GenerateAndWrapOutput(GenerateAndWrapOutput, NamedTuple('GenerateAndWrapOutput', [('plaintextMaterial', Any), ('wrappedMaterial', Any), ('wrapInfo', Any)])):
    def __dafnystr__(self) -> str:
        return f'MaterialWrapping.GenerateAndWrapOutput.GenerateAndWrapOutput({_dafny.string_of(self.plaintextMaterial)}, {_dafny.string_of(self.wrappedMaterial)}, {_dafny.string_of(self.wrapInfo)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, MaterialWrapping.GenerateAndWrapOutput_GenerateAndWrapOutput) and self.plaintextMaterial == __o.plaintextMaterial and self.wrappedMaterial == __o.wrappedMaterial and self.wrapInfo == __o.wrapInfo
    def __hash__(self) -> int:
        return super().__hash__()


class WrapInput:
    @classmethod
    def default(cls, ):
        return lambda: WrapInput_WrapInput(_dafny.Seq({}), software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo.default()(), _dafny.Map({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_WrapInput(self) -> bool:
        return isinstance(self, MaterialWrapping.WrapInput_WrapInput)

class WrapInput_WrapInput(WrapInput, NamedTuple('WrapInput', [('plaintextMaterial', Any), ('algorithmSuite', Any), ('encryptionContext', Any)])):
    def __dafnystr__(self) -> str:
        return f'MaterialWrapping.WrapInput.WrapInput({_dafny.string_of(self.plaintextMaterial)}, {_dafny.string_of(self.algorithmSuite)}, {_dafny.string_of(self.encryptionContext)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, MaterialWrapping.WrapInput_WrapInput) and self.plaintextMaterial == __o.plaintextMaterial and self.algorithmSuite == __o.algorithmSuite and self.encryptionContext == __o.encryptionContext
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
        return isinstance(self, MaterialWrapping.WrapOutput_WrapOutput)

class WrapOutput_WrapOutput(WrapOutput, NamedTuple('WrapOutput', [('wrappedMaterial', Any), ('wrapInfo', Any)])):
    def __dafnystr__(self) -> str:
        return f'MaterialWrapping.WrapOutput.WrapOutput({_dafny.string_of(self.wrappedMaterial)}, {_dafny.string_of(self.wrapInfo)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, MaterialWrapping.WrapOutput_WrapOutput) and self.wrappedMaterial == __o.wrappedMaterial and self.wrapInfo == __o.wrapInfo
    def __hash__(self) -> int:
        return super().__hash__()


class UnwrapInput:
    @classmethod
    def default(cls, ):
        return lambda: UnwrapInput_UnwrapInput(_dafny.Seq({}), software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo_AlgorithmSuiteInfo.default()(), _dafny.Map({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_UnwrapInput(self) -> bool:
        return isinstance(self, MaterialWrapping.UnwrapInput_UnwrapInput)

class UnwrapInput_UnwrapInput(UnwrapInput, NamedTuple('UnwrapInput', [('wrappedMaterial', Any), ('algorithmSuite', Any), ('encryptionContext', Any)])):
    def __dafnystr__(self) -> str:
        return f'MaterialWrapping.UnwrapInput.UnwrapInput({_dafny.string_of(self.wrappedMaterial)}, {_dafny.string_of(self.algorithmSuite)}, {_dafny.string_of(self.encryptionContext)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, MaterialWrapping.UnwrapInput_UnwrapInput) and self.wrappedMaterial == __o.wrappedMaterial and self.algorithmSuite == __o.algorithmSuite and self.encryptionContext == __o.encryptionContext
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
        return isinstance(self, MaterialWrapping.UnwrapOutput_UnwrapOutput)

class UnwrapOutput_UnwrapOutput(UnwrapOutput, NamedTuple('UnwrapOutput', [('unwrappedMaterial', Any), ('unwrapInfo', Any)])):
    def __dafnystr__(self) -> str:
        return f'MaterialWrapping.UnwrapOutput.UnwrapOutput({_dafny.string_of(self.unwrappedMaterial)}, {_dafny.string_of(self.unwrapInfo)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, MaterialWrapping.UnwrapOutput_UnwrapOutput) and self.unwrappedMaterial == __o.unwrappedMaterial and self.unwrapInfo == __o.unwrapInfo
    def __hash__(self) -> int:
        return super().__hash__()


class GenerateAndWrapMaterial:
    pass

class WrapMaterial:
    pass

class UnwrapMaterial:
    pass
