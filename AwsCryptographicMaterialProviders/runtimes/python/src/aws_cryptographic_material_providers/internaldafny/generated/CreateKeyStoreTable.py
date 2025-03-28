import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptographic_material_providers.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import smithy_dafny_standard_library.internaldafny.generated.Wrappers as Wrappers
import smithy_dafny_standard_library.internaldafny.generated.BoundedInts as BoundedInts
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_Sequence as StandardLibrary_Sequence
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import smithy_dafny_standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import smithy_dafny_standard_library.internaldafny.generated.UTF8 as UTF8
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesTypes as AwsCryptographyPrimitivesTypes
import aws_cryptography_primitives.internaldafny.generated.ExternRandom as ExternRandom
import aws_cryptography_primitives.internaldafny.generated.Random as Random
import aws_cryptography_primitives.internaldafny.generated.AESEncryption as AESEncryption
import aws_cryptography_primitives.internaldafny.generated.ExternDigest as ExternDigest
import aws_cryptography_primitives.internaldafny.generated.Digest as Digest
import aws_cryptography_primitives.internaldafny.generated.HMAC as HMAC
import aws_cryptography_primitives.internaldafny.generated.WrappedHMAC as WrappedHMAC
import aws_cryptography_primitives.internaldafny.generated.HKDF as HKDF
import aws_cryptography_primitives.internaldafny.generated.WrappedHKDF as WrappedHKDF
import aws_cryptography_primitives.internaldafny.generated.Signature as Signature
import aws_cryptography_primitives.internaldafny.generated.KdfCtr as KdfCtr
import aws_cryptography_primitives.internaldafny.generated.RSAEncryption as RSAEncryption
import aws_cryptography_primitives.internaldafny.generated.ECDH as ECDH
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesOperations as AwsCryptographyPrimitivesOperations
import aws_cryptography_primitives.internaldafny.generated.AtomicPrimitives as AtomicPrimitives
import aws_cryptography_internal_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import aws_cryptography_internal_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
import smithy_dafny_standard_library.internaldafny.generated.Relations as Relations
import smithy_dafny_standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import smithy_dafny_standard_library.internaldafny.generated.Math as Math
import smithy_dafny_standard_library.internaldafny.generated.Seq as Seq
import smithy_dafny_standard_library.internaldafny.generated.Unicode as Unicode
import smithy_dafny_standard_library.internaldafny.generated.Functions as Functions
import smithy_dafny_standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import smithy_dafny_standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import smithy_dafny_standard_library.internaldafny.generated.FileIO as FileIO
import smithy_dafny_standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import smithy_dafny_standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.MulInternals as MulInternals
import smithy_dafny_standard_library.internaldafny.generated.Mul as Mul
import smithy_dafny_standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import smithy_dafny_standard_library.internaldafny.generated.ModInternals as ModInternals
import smithy_dafny_standard_library.internaldafny.generated.DivInternals as DivInternals
import smithy_dafny_standard_library.internaldafny.generated.DivMod as DivMod
import smithy_dafny_standard_library.internaldafny.generated.Power as Power
import smithy_dafny_standard_library.internaldafny.generated.Logarithm as Logarithm
import smithy_dafny_standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import smithy_dafny_standard_library.internaldafny.generated.UUID as UUID
import smithy_dafny_standard_library.internaldafny.generated.OsLang as OsLang
import smithy_dafny_standard_library.internaldafny.generated.Time as Time
import smithy_dafny_standard_library.internaldafny.generated.Streams as Streams
import smithy_dafny_standard_library.internaldafny.generated.Sorting as Sorting
import smithy_dafny_standard_library.internaldafny.generated.SortedSets as SortedSets
import smithy_dafny_standard_library.internaldafny.generated.HexStrings as HexStrings
import smithy_dafny_standard_library.internaldafny.generated.GetOpt as GetOpt
import smithy_dafny_standard_library.internaldafny.generated.FloatCompare as FloatCompare
import smithy_dafny_standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import smithy_dafny_standard_library.internaldafny.generated.Base64 as Base64
import smithy_dafny_standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import smithy_dafny_standard_library.internaldafny.generated.Actions as Actions
import smithy_dafny_standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import aws_cryptographic_material_providers.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_material_providers.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_material_providers.internaldafny.generated.KeyStoreErrorMessages as KeyStoreErrorMessages
import aws_cryptographic_material_providers.internaldafny.generated.KmsArn as KmsArn
import aws_cryptographic_material_providers.internaldafny.generated.Structure as Structure
import aws_cryptographic_material_providers.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations
import aws_cryptographic_material_providers.internaldafny.generated.DDBKeystoreOperations as DDBKeystoreOperations
import aws_cryptographic_material_providers.internaldafny.generated.CreateKeys as CreateKeys

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
        d_0_maybeDescribeTableResponse_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = (ddbClient).DescribeTable(ComAmazonawsDynamodbTypes.DescribeTableInput_DescribeTableInput(tableName))
        d_0_maybeDescribeTableResponse_ = out0_
        if (d_0_maybeDescribeTableResponse_).is_Failure:
            d_1_error_: ComAmazonawsDynamodbTypes.Error
            d_1_error_ = (d_0_maybeDescribeTableResponse_).error
            if (d_1_error_).is_ResourceNotFoundException:
                d_2_maybeCreateTableResponse_: Wrappers.Result
                out1_: Wrappers.Result
                out1_ = (ddbClient).CreateTable(ComAmazonawsDynamodbTypes.CreateTableInput_CreateTableInput(default__.ATTRIBUTE__DEFINITIONS, tableName, default__.KEY__SCHEMA, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(ComAmazonawsDynamodbTypes.BillingMode_PAY__PER__REQUEST()), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None()))
                d_2_maybeCreateTableResponse_ = out1_
                if (d_2_maybeCreateTableResponse_).is_Failure:
                    res = Wrappers.Result_Failure(AwsCryptographyKeyStoreTypes.Error_ComAmazonawsDynamodb((d_2_maybeCreateTableResponse_).error))
                elif True:
                    d_3_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
                    d_3_valueOrError0_ = Wrappers.default__.Need((((((d_2_maybeCreateTableResponse_).value).TableDescription).is_Some) and (default__.keyStoreHasExpectedConstruction_q((((d_2_maybeCreateTableResponse_).value).TableDescription).value))) and (ComAmazonawsDynamodbTypes.default__.IsValid__TableArn((((((d_2_maybeCreateTableResponse_).value).TableDescription).value).TableArn).value)), default__.E(_dafny.Seq("Configured table name does not conform to expected Key Store construction.")))
                    if (d_3_valueOrError0_).IsFailure():
                        res = (d_3_valueOrError0_).PropagateFailure()
                        return res
                    res = Wrappers.Result_Success((((((d_2_maybeCreateTableResponse_).value).TableDescription).value).TableArn).value)
            elif True:
                res = Wrappers.Result_Failure(AwsCryptographyKeyStoreTypes.Error_ComAmazonawsDynamodb(d_1_error_))
        elif True:
            d_4_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
            d_4_valueOrError1_ = Wrappers.default__.Need((((((d_0_maybeDescribeTableResponse_).value).Table).is_Some) and (default__.keyStoreHasExpectedConstruction_q((((d_0_maybeDescribeTableResponse_).value).Table).value))) and (ComAmazonawsDynamodbTypes.default__.IsValid__TableArn((((((d_0_maybeDescribeTableResponse_).value).Table).value).TableArn).value)), default__.E(_dafny.Seq("Configured table name does not conform to expected Key Store construction.")))
            if (d_4_valueOrError1_).IsFailure():
                res = (d_4_valueOrError1_).PropagateFailure()
                return res
            res = Wrappers.Result_Success((((((d_0_maybeDescribeTableResponse_).value).Table).value).TableArn).value)
        return res

    @staticmethod
    def E(s):
        return AwsCryptographyKeyStoreTypes.Error_KeyStoreException(s)

    @_dafny.classproperty
    def ATTRIBUTE__DEFINITIONS(instance):
        return _dafny.Seq([ComAmazonawsDynamodbTypes.AttributeDefinition_AttributeDefinition(Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD, ComAmazonawsDynamodbTypes.ScalarAttributeType_S()), ComAmazonawsDynamodbTypes.AttributeDefinition_AttributeDefinition(Structure.default__.TYPE__FIELD, ComAmazonawsDynamodbTypes.ScalarAttributeType_S())])
    @_dafny.classproperty
    def KEY__SCHEMA(instance):
        return _dafny.Seq([ComAmazonawsDynamodbTypes.KeySchemaElement_KeySchemaElement(Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD, ComAmazonawsDynamodbTypes.KeyType_HASH()), ComAmazonawsDynamodbTypes.KeySchemaElement_KeySchemaElement(Structure.default__.TYPE__FIELD, ComAmazonawsDynamodbTypes.KeyType_RANGE())])

class keyStoreDescription:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return ComAmazonawsDynamodbTypes.TableDescription.default()()
    def _Is(source__):
        d_0_t_: ComAmazonawsDynamodbTypes.TableDescription = source__
        return default__.keyStoreHasExpectedConstruction_q(d_0_t_)
