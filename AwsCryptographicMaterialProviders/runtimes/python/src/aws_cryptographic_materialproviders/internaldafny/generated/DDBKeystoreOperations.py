import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import aws_cryptographic_materialproviders.internaldafny.generated.module_ as module_
import _dafny as _dafny
import System_ as System_
import standard_library.internaldafny.generated.Wrappers as Wrappers
import standard_library.internaldafny.generated.BoundedInts as BoundedInts
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import standard_library.internaldafny.generated.UTF8 as UTF8
import com_amazonaws_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import com_amazonaws_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
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
import aws_cryptography_primitives.internaldafny.generated.AwsCryptographyPrimitivesOperations as AwsCryptographyPrimitivesOperations
import aws_cryptography_primitives.internaldafny.generated.AesKdfCtr as AesKdfCtr
import standard_library.internaldafny.generated.Relations as Relations
import standard_library.internaldafny.generated.Seq_MergeSort as Seq_MergeSort
import standard_library.internaldafny.generated.Math as Math
import standard_library.internaldafny.generated.Seq as Seq
import standard_library.internaldafny.generated.Unicode as Unicode
import standard_library.internaldafny.generated.Functions as Functions
import standard_library.internaldafny.generated.Utf8EncodingForm as Utf8EncodingForm
import standard_library.internaldafny.generated.Utf16EncodingForm as Utf16EncodingForm
import standard_library.internaldafny.generated.UnicodeStrings as UnicodeStrings
import standard_library.internaldafny.generated.FileIO as FileIO
import standard_library.internaldafny.generated.GeneralInternals as GeneralInternals
import standard_library.internaldafny.generated.MulInternalsNonlinear as MulInternalsNonlinear
import standard_library.internaldafny.generated.MulInternals as MulInternals
import standard_library.internaldafny.generated.Mul as Mul
import standard_library.internaldafny.generated.ModInternalsNonlinear as ModInternalsNonlinear
import standard_library.internaldafny.generated.DivInternalsNonlinear as DivInternalsNonlinear
import standard_library.internaldafny.generated.ModInternals as ModInternals
import standard_library.internaldafny.generated.DivInternals as DivInternals
import standard_library.internaldafny.generated.DivMod as DivMod
import standard_library.internaldafny.generated.Power as Power
import standard_library.internaldafny.generated.Logarithm as Logarithm
import standard_library.internaldafny.generated.StandardLibraryInterop as StandardLibraryInterop
import standard_library.internaldafny.generated.UUID as UUID
import standard_library.internaldafny.generated.Time as Time
import standard_library.internaldafny.generated.Streams as Streams
import standard_library.internaldafny.generated.Sorting as Sorting
import standard_library.internaldafny.generated.SortedSets as SortedSets
import standard_library.internaldafny.generated.HexStrings as HexStrings
import standard_library.internaldafny.generated.GetOpt as GetOpt
import standard_library.internaldafny.generated.FloatCompare as FloatCompare
import standard_library.internaldafny.generated.ConcurrentCall as ConcurrentCall
import standard_library.internaldafny.generated.Base64 as Base64
import standard_library.internaldafny.generated.Base64Lemmas as Base64Lemmas
import standard_library.internaldafny.generated.Actions as Actions
import standard_library.internaldafny.generated.DafnyLibraries as DafnyLibraries
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyKeyStoreTypes as AwsCryptographyKeyStoreTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsCryptographyMaterialProvidersTypes as AwsCryptographyMaterialProvidersTypes
import aws_cryptographic_materialproviders.internaldafny.generated.AwsArnParsing as AwsArnParsing
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsMrkMatchForDecrypt as AwsKmsMrkMatchForDecrypt
import aws_cryptographic_materialproviders.internaldafny.generated.AwsKmsUtils as AwsKmsUtils
import aws_cryptographic_materialproviders.internaldafny.generated.Structure as Structure
import aws_cryptographic_materialproviders.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations

# Module: aws_cryptographic_materialproviders.internaldafny.generated.DDBKeystoreOperations

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def WriteNewKeyToStore(versionBranchKeyItem, activeBranchKeyItem, beaconKeyItem, tableName, ddbClient):
        output: Wrappers.Result = Wrappers.Result.default(ComAmazonawsDynamodbTypes.TransactWriteItemsOutput.default())()
        d_154_items_: _dafny.Seq
        d_154_items_ = _dafny.Seq([default__.CreateTransactWritePutItem(versionBranchKeyItem, tableName, ConditionExpression_BRANCH__KEY__NOT__EXIST()), default__.CreateTransactWritePutItem(activeBranchKeyItem, tableName, ConditionExpression_BRANCH__KEY__NOT__EXIST()), default__.CreateTransactWritePutItem(beaconKeyItem, tableName, ConditionExpression_BRANCH__KEY__NOT__EXIST())])
        d_155_transactRequest_: ComAmazonawsDynamodbTypes.TransactWriteItemsInput
        d_155_transactRequest_ = ComAmazonawsDynamodbTypes.TransactWriteItemsInput_TransactWriteItemsInput(d_154_items_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_156_maybeTransactWriteResponse_: Wrappers.Result
        out13_: Wrappers.Result
        out13_ = (ddbClient).TransactWriteItems(d_155_transactRequest_)
        d_156_maybeTransactWriteResponse_ = out13_
        d_157_transactWriteItemsResponse_: ComAmazonawsDynamodbTypes.TransactWriteItemsOutput
        d_158_valueOrError0_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsDynamodbTypes.TransactWriteItemsOutput.default())()
        def lambda14_(d_159_e_):
            return AwsCryptographyKeyStoreTypes.Error_ComAmazonawsDynamodb(d_159_e_)

        d_158_valueOrError0_ = (d_156_maybeTransactWriteResponse_).MapFailure(lambda14_)
        if (d_158_valueOrError0_).IsFailure():
            output = (d_158_valueOrError0_).PropagateFailure()
            return output
        d_157_transactWriteItemsResponse_ = (d_158_valueOrError0_).Extract()
        output = Wrappers.Result_Success(d_157_transactWriteItemsResponse_)
        return output

    @staticmethod
    def WriteNewBranchKeyVersionToKeystore(versionBranchKeyItem, activeBranchKeyItem, tableName, ddbClient):
        output: Wrappers.Result = Wrappers.Result.default(ComAmazonawsDynamodbTypes.TransactWriteItemsOutput.default())()
        d_160_items_: _dafny.Seq
        d_160_items_ = _dafny.Seq([default__.CreateTransactWritePutItem(versionBranchKeyItem, tableName, ConditionExpression_BRANCH__KEY__NOT__EXIST()), default__.CreateTransactWritePutItem(activeBranchKeyItem, tableName, ConditionExpression_BRANCH__KEY__EXISTS())])
        d_161_transactRequest_: ComAmazonawsDynamodbTypes.TransactWriteItemsInput
        d_161_transactRequest_ = ComAmazonawsDynamodbTypes.TransactWriteItemsInput_TransactWriteItemsInput(d_160_items_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_162_maybeTransactWriteResponse_: Wrappers.Result
        out14_: Wrappers.Result
        out14_ = (ddbClient).TransactWriteItems(d_161_transactRequest_)
        d_162_maybeTransactWriteResponse_ = out14_
        d_163_transactWriteItemsResponse_: ComAmazonawsDynamodbTypes.TransactWriteItemsOutput
        d_164_valueOrError0_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsDynamodbTypes.TransactWriteItemsOutput.default())()
        def lambda15_(d_165_e_):
            return AwsCryptographyKeyStoreTypes.Error_ComAmazonawsDynamodb(d_165_e_)

        d_164_valueOrError0_ = (d_162_maybeTransactWriteResponse_).MapFailure(lambda15_)
        if (d_164_valueOrError0_).IsFailure():
            output = (d_164_valueOrError0_).PropagateFailure()
            return output
        d_163_transactWriteItemsResponse_ = (d_164_valueOrError0_).Extract()
        output = Wrappers.Result_Success(d_163_transactWriteItemsResponse_)
        return output

    @staticmethod
    def GetActiveBranchKeyItem(branchKeyIdentifier, tableName, ddbClient):
        output: Wrappers.Result = None
        d_166_dynamoDbKey_: _dafny.Map
        d_166_dynamoDbKey_ = _dafny.Map({Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD: ComAmazonawsDynamodbTypes.AttributeValue_S(branchKeyIdentifier), Structure.default__.TYPE__FIELD: ComAmazonawsDynamodbTypes.AttributeValue_S(Structure.default__.BRANCH__KEY__ACTIVE__TYPE)})
        d_167_ItemRequest_: ComAmazonawsDynamodbTypes.GetItemInput
        d_167_ItemRequest_ = ComAmazonawsDynamodbTypes.GetItemInput_GetItemInput(tableName, d_166_dynamoDbKey_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_168_maybeGetItem_: Wrappers.Result
        out15_: Wrappers.Result
        out15_ = (ddbClient).GetItem(d_167_ItemRequest_)
        d_168_maybeGetItem_ = out15_
        d_169_getItemResponse_: ComAmazonawsDynamodbTypes.GetItemOutput
        d_170_valueOrError0_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsDynamodbTypes.GetItemOutput.default())()
        def lambda16_(d_171_e_):
            return AwsCryptographyKeyStoreTypes.Error_ComAmazonawsDynamodb(d_171_e_)

        d_170_valueOrError0_ = (d_168_maybeGetItem_).MapFailure(lambda16_)
        if (d_170_valueOrError0_).IsFailure():
            output = (d_170_valueOrError0_).PropagateFailure()
            return output
        d_169_getItemResponse_ = (d_170_valueOrError0_).Extract()
        d_172_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_172_valueOrError1_ = Wrappers.default__.Need(((d_169_getItemResponse_).Item).is_Some, AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("No item found for corresponding branch key identifier.")))
        if (d_172_valueOrError1_).IsFailure():
            output = (d_172_valueOrError1_).PropagateFailure()
            return output
        d_173_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_173_valueOrError2_ = Wrappers.default__.Need((Structure.default__.ActiveBranchKeyItem_q(((d_169_getItemResponse_).Item).value)) and ((((((d_169_getItemResponse_).Item).value)[Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD]).S) == (branchKeyIdentifier)), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Item found is not a valid active branch key.")))
        if (d_173_valueOrError2_).IsFailure():
            output = (d_173_valueOrError2_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(((d_169_getItemResponse_).Item).value)
        return output

    @staticmethod
    def GetVersionBranchKeyItem(branchKeyIdentifier, branchKeyVersion, tableName, ddbClient):
        output: Wrappers.Result = None
        d_174_dynamoDbKey_: _dafny.Map
        d_174_dynamoDbKey_ = _dafny.Map({Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD: ComAmazonawsDynamodbTypes.AttributeValue_S(branchKeyIdentifier), Structure.default__.TYPE__FIELD: ComAmazonawsDynamodbTypes.AttributeValue_S((Structure.default__.BRANCH__KEY__TYPE__PREFIX) + (branchKeyVersion))})
        d_175_ItemRequest_: ComAmazonawsDynamodbTypes.GetItemInput
        d_175_ItemRequest_ = ComAmazonawsDynamodbTypes.GetItemInput_GetItemInput(tableName, d_174_dynamoDbKey_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_176_maybeGetItem_: Wrappers.Result
        out16_: Wrappers.Result
        out16_ = (ddbClient).GetItem(d_175_ItemRequest_)
        d_176_maybeGetItem_ = out16_
        d_177_getItemResponse_: ComAmazonawsDynamodbTypes.GetItemOutput
        d_178_valueOrError0_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsDynamodbTypes.GetItemOutput.default())()
        def lambda17_(d_179_e_):
            return AwsCryptographyKeyStoreTypes.Error_ComAmazonawsDynamodb(d_179_e_)

        d_178_valueOrError0_ = (d_176_maybeGetItem_).MapFailure(lambda17_)
        if (d_178_valueOrError0_).IsFailure():
            output = (d_178_valueOrError0_).PropagateFailure()
            return output
        d_177_getItemResponse_ = (d_178_valueOrError0_).Extract()
        d_180_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_180_valueOrError1_ = Wrappers.default__.Need(((d_177_getItemResponse_).Item).is_Some, AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("No item found for corresponding branch key identifier.")))
        if (d_180_valueOrError1_).IsFailure():
            output = (d_180_valueOrError1_).PropagateFailure()
            return output
        d_181_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_181_valueOrError2_ = Wrappers.default__.Need(((Structure.default__.VersionBranchKeyItem_q(((d_177_getItemResponse_).Item).value)) and ((((((d_177_getItemResponse_).Item).value)[Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD]).S) == (branchKeyIdentifier))) and ((((((d_177_getItemResponse_).Item).value)[Structure.default__.TYPE__FIELD]).S) == ((Structure.default__.BRANCH__KEY__TYPE__PREFIX) + (branchKeyVersion))), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Item found is not a valid branch key version.")))
        if (d_181_valueOrError2_).IsFailure():
            output = (d_181_valueOrError2_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(((d_177_getItemResponse_).Item).value)
        return output

    @staticmethod
    def GetBeaconKeyItem(branchKeyIdentifier, tableName, ddbClient):
        output: Wrappers.Result = None
        d_182_dynamoDbKey_: _dafny.Map
        d_182_dynamoDbKey_ = _dafny.Map({Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD: ComAmazonawsDynamodbTypes.AttributeValue_S(branchKeyIdentifier), Structure.default__.TYPE__FIELD: ComAmazonawsDynamodbTypes.AttributeValue_S(Structure.default__.BEACON__KEY__TYPE__VALUE)})
        d_183_ItemRequest_: ComAmazonawsDynamodbTypes.GetItemInput
        d_183_ItemRequest_ = ComAmazonawsDynamodbTypes.GetItemInput_GetItemInput(tableName, d_182_dynamoDbKey_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_184_maybeGetItem_: Wrappers.Result
        out17_: Wrappers.Result
        out17_ = (ddbClient).GetItem(d_183_ItemRequest_)
        d_184_maybeGetItem_ = out17_
        d_185_getItemResponse_: ComAmazonawsDynamodbTypes.GetItemOutput
        d_186_valueOrError0_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsDynamodbTypes.GetItemOutput.default())()
        def lambda18_(d_187_e_):
            return AwsCryptographyKeyStoreTypes.Error_ComAmazonawsDynamodb(d_187_e_)

        d_186_valueOrError0_ = (d_184_maybeGetItem_).MapFailure(lambda18_)
        if (d_186_valueOrError0_).IsFailure():
            output = (d_186_valueOrError0_).PropagateFailure()
            return output
        d_185_getItemResponse_ = (d_186_valueOrError0_).Extract()
        d_188_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_188_valueOrError1_ = Wrappers.default__.Need(((d_185_getItemResponse_).Item).is_Some, AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("No item found for corresponding branch key identifier.")))
        if (d_188_valueOrError1_).IsFailure():
            output = (d_188_valueOrError1_).PropagateFailure()
            return output
        d_189_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_189_valueOrError2_ = Wrappers.default__.Need((Structure.default__.BeaconKeyItem_q(((d_185_getItemResponse_).Item).value)) and ((((((d_185_getItemResponse_).Item).value)[Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD]).S) == (branchKeyIdentifier)), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Item found is not a valid beacon key.")))
        if (d_189_valueOrError2_).IsFailure():
            output = (d_189_valueOrError2_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(((d_185_getItemResponse_).Item).value)
        return output

    @staticmethod
    def CreateTransactWritePutItem(item, tableName, ConditionExpression):
        def lambda19_(source9_):
            if source9_.is_BRANCH__KEY__NOT__EXIST:
                return default__.BRANCH__KEY__NOT__EXIST__CONDITION
            elif True:
                return default__.BRANCH__KEY__EXISTS__CONDITION

        return ComAmazonawsDynamodbTypes.TransactWriteItem_TransactWriteItem(Wrappers.Option_None(), Wrappers.Option_Some(ComAmazonawsDynamodbTypes.Put_Put(item, tableName, Wrappers.Option_Some(lambda19_(ConditionExpression)), Wrappers.Option_Some(default__.BRANCH__KEY__EXISTS__EXPRESSION__ATTRIBUTE__NAMES), Wrappers.Option_None(), Wrappers.Option_None())), Wrappers.Option_None(), Wrappers.Option_None())

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

