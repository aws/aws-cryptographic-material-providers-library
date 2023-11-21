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

assert "CleanupItems" == __name__
CleanupItems = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DeleteVersion(branchKeyIdentifier, branchKeyVersion, ddbClient):
        d_484___v0_: Wrappers.Result
        out128_: Wrappers.Result
        out128_ = (ddbClient).DeleteItem(software_amazon_cryptography_services_dynamodb_internaldafny_types.DeleteItemInput_DeleteItemInput((Fixtures.default__).branchKeyStoreName, _dafny.Map({(Structure.default__).BRANCH__KEY__IDENTIFIER__FIELD: software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S(branchKeyIdentifier), (Structure.default__).TYPE__FIELD: software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S(((Structure.default__).BRANCH__KEY__TYPE__PREFIX) + (branchKeyVersion))}), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None()))
        d_484___v0_ = out128_

    @staticmethod
    def DeleteActive(branchKeyIdentifier, ddbClient):
        d_485___v1_: Wrappers.Result
        out129_: Wrappers.Result
        out129_ = (ddbClient).DeleteItem(software_amazon_cryptography_services_dynamodb_internaldafny_types.DeleteItemInput_DeleteItemInput((Fixtures.default__).branchKeyStoreName, _dafny.Map({(Structure.default__).BRANCH__KEY__IDENTIFIER__FIELD: software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S(branchKeyIdentifier), (Structure.default__).TYPE__FIELD: software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S((Structure.default__).BRANCH__KEY__ACTIVE__TYPE)}), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None()))
        d_485___v1_ = out129_
        d_486___v2_: Wrappers.Result
        out130_: Wrappers.Result
        out130_ = (ddbClient).DeleteItem(software_amazon_cryptography_services_dynamodb_internaldafny_types.DeleteItemInput_DeleteItemInput((Fixtures.default__).branchKeyStoreName, _dafny.Map({(Structure.default__).BRANCH__KEY__IDENTIFIER__FIELD: software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S(branchKeyIdentifier), (Structure.default__).TYPE__FIELD: software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S((Structure.default__).BEACON__KEY__TYPE__VALUE)}), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None()))
        d_486___v2_ = out130_

