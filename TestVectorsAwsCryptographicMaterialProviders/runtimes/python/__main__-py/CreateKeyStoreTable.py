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
import Digest
import HMAC
import WrappedHMAC
import HKDF
import WrappedHKDF
import Signature
import KdfCtr
import RSAEncryption
import AwsCryptographyPrimitivesOperations
import software_amazon_cryptography_primitives_internaldafny
import Aws_Cryptography
import Aws
import MaterialWrapping
import CanonicalEncryptionContext
import IntermediateKeyWrapping
import EdkWrapping
import AwsKmsKeyring
import StrictMultiKeyring
import AwsKmsDiscoveryKeyring
import software_amazon_cryptography_services_kms_internaldafny
import DiscoveryMultiKeyring
import AwsKmsMrkDiscoveryKeyring
import MrkAwareDiscoveryMultiKeyring
import AwsKmsMrkKeyring
import MrkAwareStrictMultiKeyring
import LocalCMC
import software_amazon_cryptography_internaldafny_SynchronizedLocalCMC
import StormTracker
import software_amazon_cryptography_internaldafny_StormTrackingCMC
import AwsKmsHierarchicalKeyring
import AwsKmsRsaKeyring
import RawAESKeyring
import RawRSAKeyring
import CMM
import Defaults
import Commitment
import DefaultCMM
import DefaultClientSupplier
import RequiredEncryptionContextCMM
import AwsCryptographyMaterialProvidersOperations
import software_amazon_cryptography_materialproviders_internaldafny
import software_amazon_cryptography_materialproviders_internaldafny_wrapped
import TestVectorsUtils
import TestVectorConstants
import KeyringExpectations
import CreateAwsKmsKeyrings
import CreateAwsKmsMultiKeyrings
import CreateAwsKmsMrkKeyrings
import CreateAwsKmsMrkMultiKeyrings
import CreateRawAesKeyrings
import CreateRawRsaKeyrings
import CreateKeyrings
import software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types
import JSON_Utils_Views_Core
import JSON_Utils_Views_Writers
import JSON_Utils_Views
import JSON_Utils_Lexers_Core
import JSON_Utils_Lexers_Strings
import JSON_Utils_Lexers
import JSON_Utils_Cursors
import JSON_Utils_Parsers
import JSON_Utils_Str_CharStrConversion
import JSON_Utils_Str_CharStrEscaping
import JSON_Utils_Str
import JSON_Utils_Seq
import JSON_Utils_Vectors
import JSON_Utils
import JSON_Errors
import JSON_Values
import JSON_Spec
import JSON_Grammar
import JSON_Serializer_ByteStrConversion
import JSON_Serializer
import JSON_Deserializer_Uint16StrConversion
import JSON_Deserializer_ByteStrConversion
import JSON_Deserializer
import JSON_ConcreteSyntax_Spec
import JSON_ConcreteSyntax_SpecProperties
import JSON_ConcreteSyntax
import JSON_ZeroCopy_Serializer
import JSON_ZeroCopy_Deserializer_Core
import JSON_ZeroCopy_Deserializer_Strings
import JSON_ZeroCopy_Deserializer_Numbers
import JSON_ZeroCopy_Deserializer_ObjectParams
import JSON_ZeroCopy_Deserializer_Objects
import JSON_ZeroCopy_Deserializer_ArrayParams
import JSON_ZeroCopy_Deserializer_Arrays
import JSON_ZeroCopy_Deserializer_Constants
import JSON_ZeroCopy_Deserializer_Values
import JSON_ZeroCopy_Deserializer_API
import JSON_ZeroCopy_Deserializer
import JSON_ZeroCopy_API
import JSON_ZeroCopy
import JSON_API
import JSON
import JSONHelpers
import KeyDescription
import KeyMaterial
import CreateStaticKeyrings
import CreateStaticKeyStores
import KeyringFromKeyDescription
import KeysVectorOperations
import software_amazon_cryptography_materialproviderstestvectorkeys_internaldafny
import TestVectors
import CompleteVectors
import ParseJsonManifests
import TestManifests
import WrappedMaterialProvidersMain
import TestWrappedMaterialProvidersMain
import software_amazon_cryptography_services_dynamodb_internaldafny
import Structure
import KMSKeystoreOperations
import DDBKeystoreOperations
import CreateKeys

# Module: CreateKeyStoreTable

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def keyStoreHasExpectedConstruction_q(t):
        return (((((((t).AttributeDefinitions).is_Some) and (((t).KeySchema).is_Some)) and (((t).TableName).is_Some)) and (((t).TableArn).is_Some)) and ((Seq.default__.ToSet(default__.ATTRIBUTE__DEFINITIONS)).issubset(Seq.default__.ToSet(((t).AttributeDefinitions).value)))) and ((Seq.default__.ToSet(default__.KEY__SCHEMA)).issubset(Seq.default__.ToSet(((t).KeySchema).value)))

    @staticmethod
    def CreateKeyStoreTable(tableName, ddbClient):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_2057_maybeDescribeTableResponse_: Wrappers.Result
        out366_: Wrappers.Result
        out366_ = (ddbClient).DescribeTable(software_amazon_cryptography_services_dynamodb_internaldafny_types.DescribeTableInput_DescribeTableInput(tableName))
        d_2057_maybeDescribeTableResponse_ = out366_
        if (d_2057_maybeDescribeTableResponse_).is_Failure:
            d_2058_error_: software_amazon_cryptography_services_dynamodb_internaldafny_types.Error
            d_2058_error_ = (d_2057_maybeDescribeTableResponse_).error
            if (d_2058_error_).is_ResourceNotFoundException:
                d_2059_maybeCreateTableResponse_: Wrappers.Result
                out367_: Wrappers.Result
                out367_ = (ddbClient).CreateTable(software_amazon_cryptography_services_dynamodb_internaldafny_types.CreateTableInput_CreateTableInput(default__.ATTRIBUTE__DEFINITIONS, tableName, default__.KEY__SCHEMA, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(software_amazon_cryptography_services_dynamodb_internaldafny_types.BillingMode_PAY__PER__REQUEST()), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None()))
                d_2059_maybeCreateTableResponse_ = out367_
                if (d_2059_maybeCreateTableResponse_).is_Failure:
                    res = Wrappers.Result_Failure(software_amazon_cryptography_keystore_internaldafny_types.Error_ComAmazonawsDynamodb((d_2059_maybeCreateTableResponse_).error))
                elif True:
                    d_2060_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
                    d_2060_valueOrError0_ = Wrappers.default__.Need(((((d_2059_maybeCreateTableResponse_).value).TableDescription).is_Some) and (default__.keyStoreHasExpectedConstruction_q((((d_2059_maybeCreateTableResponse_).value).TableDescription).value)), default__.E(_dafny.Seq("Configured table name does not conform to expected Key Store construction.")))
                    if (d_2060_valueOrError0_).IsFailure():
                        res = (d_2060_valueOrError0_).PropagateFailure()
                        return res
                    res = Wrappers.Result_Success((((((d_2059_maybeCreateTableResponse_).value).TableDescription).value).TableArn).value)
            elif True:
                res = Wrappers.Result_Failure(software_amazon_cryptography_keystore_internaldafny_types.Error_ComAmazonawsDynamodb(d_2058_error_))
        elif True:
            d_2061_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_2061_valueOrError1_ = Wrappers.default__.Need(((((d_2057_maybeDescribeTableResponse_).value).Table).is_Some) and (default__.keyStoreHasExpectedConstruction_q((((d_2057_maybeDescribeTableResponse_).value).Table).value)), default__.E(_dafny.Seq("Configured table name does not conform to expected Key Store construction.")))
            if (d_2061_valueOrError1_).IsFailure():
                res = (d_2061_valueOrError1_).PropagateFailure()
                return res
            res = Wrappers.Result_Success((((((d_2057_maybeDescribeTableResponse_).value).Table).value).TableArn).value)
        return res

    @staticmethod
    def E(s):
        return software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(s)

    @_dafny.classproperty
    def ATTRIBUTE__DEFINITIONS(instance):
        return _dafny.Seq([software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeDefinition_AttributeDefinition(Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD, software_amazon_cryptography_services_dynamodb_internaldafny_types.ScalarAttributeType_S()), software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeDefinition_AttributeDefinition(Structure.default__.TYPE__FIELD, software_amazon_cryptography_services_dynamodb_internaldafny_types.ScalarAttributeType_S())])
    @_dafny.classproperty
    def KEY__SCHEMA(instance):
        return _dafny.Seq([software_amazon_cryptography_services_dynamodb_internaldafny_types.KeySchemaElement_KeySchemaElement(Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD, software_amazon_cryptography_services_dynamodb_internaldafny_types.KeyType_HASH()), software_amazon_cryptography_services_dynamodb_internaldafny_types.KeySchemaElement_KeySchemaElement(Structure.default__.TYPE__FIELD, software_amazon_cryptography_services_dynamodb_internaldafny_types.KeyType_RANGE())])

class keyStoreDescription:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return software_amazon_cryptography_services_dynamodb_internaldafny_types.TableDescription.default()()
