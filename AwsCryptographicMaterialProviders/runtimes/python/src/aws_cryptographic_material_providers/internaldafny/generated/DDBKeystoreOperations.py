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

# Module: DDBKeystoreOperations

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def WriteNewKeyToStore(versionBranchKeyItem, activeBranchKeyItem, beaconKeyItem, tableName, ddbClient):
        output: Wrappers.Result = Wrappers.Result.default(ComAmazonawsDynamodbTypes.TransactWriteItemsOutput.default())()
        d_0_items_: _dafny.Seq
        d_0_items_ = _dafny.Seq([default__.CreateTransactWritePutItem(versionBranchKeyItem, tableName, ConditionExpression_BRANCH__KEY__NOT__EXIST()), default__.CreateTransactWritePutItem(activeBranchKeyItem, tableName, ConditionExpression_BRANCH__KEY__NOT__EXIST()), default__.CreateTransactWritePutItem(beaconKeyItem, tableName, ConditionExpression_BRANCH__KEY__NOT__EXIST())])
        d_1_transactRequest_: ComAmazonawsDynamodbTypes.TransactWriteItemsInput
        d_1_transactRequest_ = ComAmazonawsDynamodbTypes.TransactWriteItemsInput_TransactWriteItemsInput(d_0_items_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_2_maybeTransactWriteResponse_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = (ddbClient).TransactWriteItems(d_1_transactRequest_)
        d_2_maybeTransactWriteResponse_ = out0_
        d_3_valueOrError0_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsDynamodbTypes.TransactWriteItemsOutput.default())()
        def lambda0_(d_4_e_):
            return AwsCryptographyKeyStoreTypes.Error_ComAmazonawsDynamodb(d_4_e_)

        d_3_valueOrError0_ = (d_2_maybeTransactWriteResponse_).MapFailure(lambda0_)
        if (d_3_valueOrError0_).IsFailure():
            output = (d_3_valueOrError0_).PropagateFailure()
            return output
        d_5_transactWriteItemsResponse_: ComAmazonawsDynamodbTypes.TransactWriteItemsOutput
        d_5_transactWriteItemsResponse_ = (d_3_valueOrError0_).Extract()
        output = Wrappers.Result_Success(d_5_transactWriteItemsResponse_)
        return output

    @staticmethod
    def WriteNewBranchKeyVersionToKeystore(versionBranchKeyItem, activeBranchKeyItem, tableName, ddbClient):
        output: Wrappers.Result = Wrappers.Result.default(ComAmazonawsDynamodbTypes.TransactWriteItemsOutput.default())()
        d_0_items_: _dafny.Seq
        d_0_items_ = _dafny.Seq([default__.CreateTransactWritePutItem(versionBranchKeyItem, tableName, ConditionExpression_BRANCH__KEY__NOT__EXIST()), default__.CreateTransactWritePutItem(activeBranchKeyItem, tableName, ConditionExpression_BRANCH__KEY__EXISTS())])
        d_1_transactRequest_: ComAmazonawsDynamodbTypes.TransactWriteItemsInput
        d_1_transactRequest_ = ComAmazonawsDynamodbTypes.TransactWriteItemsInput_TransactWriteItemsInput(d_0_items_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_2_maybeTransactWriteResponse_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = (ddbClient).TransactWriteItems(d_1_transactRequest_)
        d_2_maybeTransactWriteResponse_ = out0_
        d_3_valueOrError0_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsDynamodbTypes.TransactWriteItemsOutput.default())()
        def lambda0_(d_4_e_):
            return AwsCryptographyKeyStoreTypes.Error_ComAmazonawsDynamodb(d_4_e_)

        d_3_valueOrError0_ = (d_2_maybeTransactWriteResponse_).MapFailure(lambda0_)
        if (d_3_valueOrError0_).IsFailure():
            output = (d_3_valueOrError0_).PropagateFailure()
            return output
        d_5_transactWriteItemsResponse_: ComAmazonawsDynamodbTypes.TransactWriteItemsOutput
        d_5_transactWriteItemsResponse_ = (d_3_valueOrError0_).Extract()
        output = Wrappers.Result_Success(d_5_transactWriteItemsResponse_)
        return output

    @staticmethod
    def GetActiveBranchKeyItem(branchKeyIdentifier, tableName, ddbClient):
        output: Wrappers.Result = None
        d_0_dynamoDbKey_: _dafny.Map
        d_0_dynamoDbKey_ = _dafny.Map({Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD: ComAmazonawsDynamodbTypes.AttributeValue_S(branchKeyIdentifier), Structure.default__.TYPE__FIELD: ComAmazonawsDynamodbTypes.AttributeValue_S(Structure.default__.BRANCH__KEY__ACTIVE__TYPE)})
        d_1_ItemRequest_: ComAmazonawsDynamodbTypes.GetItemInput
        d_1_ItemRequest_ = ComAmazonawsDynamodbTypes.GetItemInput_GetItemInput(tableName, d_0_dynamoDbKey_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_2_maybeGetItem_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = (ddbClient).GetItem(d_1_ItemRequest_)
        d_2_maybeGetItem_ = out0_
        d_3_valueOrError0_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsDynamodbTypes.GetItemOutput.default())()
        def lambda0_(d_4_e_):
            return AwsCryptographyKeyStoreTypes.Error_ComAmazonawsDynamodb(d_4_e_)

        d_3_valueOrError0_ = (d_2_maybeGetItem_).MapFailure(lambda0_)
        if (d_3_valueOrError0_).IsFailure():
            output = (d_3_valueOrError0_).PropagateFailure()
            return output
        d_5_getItemResponse_: ComAmazonawsDynamodbTypes.GetItemOutput
        d_5_getItemResponse_ = (d_3_valueOrError0_).Extract()
        d_6_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_6_valueOrError1_ = Wrappers.default__.Need((((d_5_getItemResponse_).Item).is_Some) and ((len(((d_5_getItemResponse_).Item).value)) >= (1)), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.NO__CORRESPONDING__BRANCH__KEY))
        if (d_6_valueOrError1_).IsFailure():
            output = (d_6_valueOrError1_).PropagateFailure()
            return output
        d_7_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_7_valueOrError2_ = Wrappers.default__.Need((Structure.default__.ActiveBranchKeyItem_q(((d_5_getItemResponse_).Item).value)) and ((((((d_5_getItemResponse_).Item).value)[Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD]).S) == (branchKeyIdentifier)), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Item found is not a valid active branch key.")))
        if (d_7_valueOrError2_).IsFailure():
            output = (d_7_valueOrError2_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(((d_5_getItemResponse_).Item).value)
        return output

    @staticmethod
    def GetVersionBranchKeyItem(branchKeyIdentifier, branchKeyVersion, tableName, ddbClient):
        output: Wrappers.Result = None
        d_0_dynamoDbKey_: _dafny.Map
        d_0_dynamoDbKey_ = _dafny.Map({Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD: ComAmazonawsDynamodbTypes.AttributeValue_S(branchKeyIdentifier), Structure.default__.TYPE__FIELD: ComAmazonawsDynamodbTypes.AttributeValue_S((Structure.default__.BRANCH__KEY__TYPE__PREFIX) + (branchKeyVersion))})
        d_1_ItemRequest_: ComAmazonawsDynamodbTypes.GetItemInput
        d_1_ItemRequest_ = ComAmazonawsDynamodbTypes.GetItemInput_GetItemInput(tableName, d_0_dynamoDbKey_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_2_maybeGetItem_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = (ddbClient).GetItem(d_1_ItemRequest_)
        d_2_maybeGetItem_ = out0_
        d_3_valueOrError0_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsDynamodbTypes.GetItemOutput.default())()
        def lambda0_(d_4_e_):
            return AwsCryptographyKeyStoreTypes.Error_ComAmazonawsDynamodb(d_4_e_)

        d_3_valueOrError0_ = (d_2_maybeGetItem_).MapFailure(lambda0_)
        if (d_3_valueOrError0_).IsFailure():
            output = (d_3_valueOrError0_).PropagateFailure()
            return output
        d_5_getItemResponse_: ComAmazonawsDynamodbTypes.GetItemOutput
        d_5_getItemResponse_ = (d_3_valueOrError0_).Extract()
        d_6_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_6_valueOrError1_ = Wrappers.default__.Need((((d_5_getItemResponse_).Item).is_Some) and ((len(((d_5_getItemResponse_).Item).value)) >= (1)), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.NO__CORRESPONDING__BRANCH__KEY))
        if (d_6_valueOrError1_).IsFailure():
            output = (d_6_valueOrError1_).PropagateFailure()
            return output
        d_7_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_7_valueOrError2_ = Wrappers.default__.Need(((Structure.default__.VersionBranchKeyItem_q(((d_5_getItemResponse_).Item).value)) and ((((((d_5_getItemResponse_).Item).value)[Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD]).S) == (branchKeyIdentifier))) and ((((((d_5_getItemResponse_).Item).value)[Structure.default__.TYPE__FIELD]).S) == ((Structure.default__.BRANCH__KEY__TYPE__PREFIX) + (branchKeyVersion))), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Item found is not a valid branch key version.")))
        if (d_7_valueOrError2_).IsFailure():
            output = (d_7_valueOrError2_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(((d_5_getItemResponse_).Item).value)
        return output

    @staticmethod
    def GetBeaconKeyItem(branchKeyIdentifier, tableName, ddbClient):
        output: Wrappers.Result = None
        d_0_dynamoDbKey_: _dafny.Map
        d_0_dynamoDbKey_ = _dafny.Map({Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD: ComAmazonawsDynamodbTypes.AttributeValue_S(branchKeyIdentifier), Structure.default__.TYPE__FIELD: ComAmazonawsDynamodbTypes.AttributeValue_S(Structure.default__.BEACON__KEY__TYPE__VALUE)})
        d_1_ItemRequest_: ComAmazonawsDynamodbTypes.GetItemInput
        d_1_ItemRequest_ = ComAmazonawsDynamodbTypes.GetItemInput_GetItemInput(tableName, d_0_dynamoDbKey_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_2_maybeGetItem_: Wrappers.Result
        out0_: Wrappers.Result
        out0_ = (ddbClient).GetItem(d_1_ItemRequest_)
        d_2_maybeGetItem_ = out0_
        d_3_valueOrError0_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsDynamodbTypes.GetItemOutput.default())()
        def lambda0_(d_4_e_):
            return AwsCryptographyKeyStoreTypes.Error_ComAmazonawsDynamodb(d_4_e_)

        d_3_valueOrError0_ = (d_2_maybeGetItem_).MapFailure(lambda0_)
        if (d_3_valueOrError0_).IsFailure():
            output = (d_3_valueOrError0_).PropagateFailure()
            return output
        d_5_getItemResponse_: ComAmazonawsDynamodbTypes.GetItemOutput
        d_5_getItemResponse_ = (d_3_valueOrError0_).Extract()
        d_6_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_6_valueOrError1_ = Wrappers.default__.Need((((d_5_getItemResponse_).Item).is_Some) and ((len(((d_5_getItemResponse_).Item).value)) >= (1)), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.NO__CORRESPONDING__BRANCH__KEY))
        if (d_6_valueOrError1_).IsFailure():
            output = (d_6_valueOrError1_).PropagateFailure()
            return output
        d_7_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_7_valueOrError2_ = Wrappers.default__.Need((Structure.default__.BeaconKeyItem_q(((d_5_getItemResponse_).Item).value)) and ((((((d_5_getItemResponse_).Item).value)[Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD]).S) == (branchKeyIdentifier)), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Item found is not a valid beacon key.")))
        if (d_7_valueOrError2_).IsFailure():
            output = (d_7_valueOrError2_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(((d_5_getItemResponse_).Item).value)
        return output

    @staticmethod
    def CreateTransactWritePutItem(item, tableName, conditionExpression):
        def lambda0_():
            source0_ = conditionExpression
            if True:
                if source0_.is_BRANCH__KEY__NOT__EXIST:
                    return default__.BRANCH__KEY__NOT__EXIST__CONDITION
            if True:
                return default__.BRANCH__KEY__EXISTS__CONDITION

        return ComAmazonawsDynamodbTypes.TransactWriteItem_TransactWriteItem(Wrappers.Option_None(), Wrappers.Option_Some(ComAmazonawsDynamodbTypes.Put_Put(item, tableName, Wrappers.Option_Some(lambda0_()), Wrappers.Option_Some(default__.BRANCH__KEY__EXISTS__EXPRESSION__ATTRIBUTE__NAMES), Wrappers.Option_None(), Wrappers.Option_None())), Wrappers.Option_None(), Wrappers.Option_None())

    @_dafny.classproperty
    def BRANCH__KEY__EXISTS__EXPRESSION__ATTRIBUTE__NAME(instance):
        return _dafny.Seq("#BranchKeyIdentifierField")
    @_dafny.classproperty
    def BRANCH__KEY__EXISTS__EXPRESSION__ATTRIBUTE__NAMES(instance):
        return _dafny.Map({default__.BRANCH__KEY__EXISTS__EXPRESSION__ATTRIBUTE__NAME: Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD})
    @_dafny.classproperty
    def BRANCH__KEY__NOT__EXIST__CONDITION(instance):
        return ((_dafny.Seq("attribute_not_exists(")) + (default__.BRANCH__KEY__EXISTS__EXPRESSION__ATTRIBUTE__NAME)) + (_dafny.Seq(")"))
    @_dafny.classproperty
    def BRANCH__KEY__EXISTS__CONDITION(instance):
        return ((_dafny.Seq("attribute_exists(")) + (default__.BRANCH__KEY__EXISTS__EXPRESSION__ATTRIBUTE__NAME)) + (_dafny.Seq(")"))

class ConditionExpression:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [ConditionExpression_BRANCH__KEY__NOT__EXIST(), ConditionExpression_BRANCH__KEY__EXISTS()]
    @classmethod
    def default(cls, ):
        return lambda: ConditionExpression_BRANCH__KEY__NOT__EXIST()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_BRANCH__KEY__NOT__EXIST(self) -> bool:
        return isinstance(self, ConditionExpression_BRANCH__KEY__NOT__EXIST)
    @property
    def is_BRANCH__KEY__EXISTS(self) -> bool:
        return isinstance(self, ConditionExpression_BRANCH__KEY__EXISTS)

class ConditionExpression_BRANCH__KEY__NOT__EXIST(ConditionExpression, NamedTuple('BRANCH__KEY__NOT__EXIST', [])):
    def __dafnystr__(self) -> str:
        return f'DDBKeystoreOperations.ConditionExpression.BRANCH_KEY_NOT_EXIST'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ConditionExpression_BRANCH__KEY__NOT__EXIST)
    def __hash__(self) -> int:
        return super().__hash__()

class ConditionExpression_BRANCH__KEY__EXISTS(ConditionExpression, NamedTuple('BRANCH__KEY__EXISTS', [])):
    def __dafnystr__(self) -> str:
        return f'DDBKeystoreOperations.ConditionExpression.BRANCH_KEY_EXISTS'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ConditionExpression_BRANCH__KEY__EXISTS)
    def __hash__(self) -> int:
        return super().__hash__()

