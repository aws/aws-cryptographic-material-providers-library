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
import aws_cryptography_primitives.internaldafny.generated.AtomicPrimitives as AtomicPrimitives
import com_amazonaws_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
import com_amazonaws_kms.internaldafny.generated.ComAmazonawsKmsTypes as ComAmazonawsKmsTypes
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
import aws_cryptographic_materialproviders.internaldafny.generated.KeyStoreErrorMessages as KeyStoreErrorMessages
import aws_cryptographic_materialproviders.internaldafny.generated.KmsArn as KmsArn
import aws_cryptographic_materialproviders.internaldafny.generated.Structure as Structure
import aws_cryptographic_materialproviders.internaldafny.generated.KMSKeystoreOperations as KMSKeystoreOperations

# Module: DDBKeystoreOperations

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def WriteNewKeyToStore(versionBranchKeyItem, activeBranchKeyItem, beaconKeyItem, tableName, ddbClient):
        output: Wrappers.Result = Wrappers.Result.default(ComAmazonawsDynamodbTypes.TransactWriteItemsOutput.default())()
        d_165_items_: _dafny.Seq
        d_165_items_ = _dafny.Seq([default__.CreateTransactWritePutItem(versionBranchKeyItem, tableName, ConditionExpression_BRANCH__KEY__NOT__EXIST()), default__.CreateTransactWritePutItem(activeBranchKeyItem, tableName, ConditionExpression_BRANCH__KEY__NOT__EXIST()), default__.CreateTransactWritePutItem(beaconKeyItem, tableName, ConditionExpression_BRANCH__KEY__NOT__EXIST())])
        d_166_transactRequest_: ComAmazonawsDynamodbTypes.TransactWriteItemsInput
        d_166_transactRequest_ = ComAmazonawsDynamodbTypes.TransactWriteItemsInput_TransactWriteItemsInput(d_165_items_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_167_maybeTransactWriteResponse_: Wrappers.Result
        out13_: Wrappers.Result
        out13_ = (ddbClient).TransactWriteItems(d_166_transactRequest_)
        d_167_maybeTransactWriteResponse_ = out13_
        d_168_transactWriteItemsResponse_: ComAmazonawsDynamodbTypes.TransactWriteItemsOutput
        d_169_valueOrError0_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsDynamodbTypes.TransactWriteItemsOutput.default())()
        def lambda15_(d_170_e_):
            return AwsCryptographyKeyStoreTypes.Error_ComAmazonawsDynamodb(d_170_e_)

        d_169_valueOrError0_ = (d_167_maybeTransactWriteResponse_).MapFailure(lambda15_)
        if (d_169_valueOrError0_).IsFailure():
            output = (d_169_valueOrError0_).PropagateFailure()
            return output
        d_168_transactWriteItemsResponse_ = (d_169_valueOrError0_).Extract()
        output = Wrappers.Result_Success(d_168_transactWriteItemsResponse_)
        return output

    @staticmethod
    def WriteNewBranchKeyVersionToKeystore(versionBranchKeyItem, activeBranchKeyItem, tableName, ddbClient):
        output: Wrappers.Result = Wrappers.Result.default(ComAmazonawsDynamodbTypes.TransactWriteItemsOutput.default())()
        d_171_items_: _dafny.Seq
        d_171_items_ = _dafny.Seq([default__.CreateTransactWritePutItem(versionBranchKeyItem, tableName, ConditionExpression_BRANCH__KEY__NOT__EXIST()), default__.CreateTransactWritePutItem(activeBranchKeyItem, tableName, ConditionExpression_BRANCH__KEY__EXISTS())])
        d_172_transactRequest_: ComAmazonawsDynamodbTypes.TransactWriteItemsInput
        d_172_transactRequest_ = ComAmazonawsDynamodbTypes.TransactWriteItemsInput_TransactWriteItemsInput(d_171_items_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_173_maybeTransactWriteResponse_: Wrappers.Result
        out14_: Wrappers.Result
        out14_ = (ddbClient).TransactWriteItems(d_172_transactRequest_)
        d_173_maybeTransactWriteResponse_ = out14_
        d_174_transactWriteItemsResponse_: ComAmazonawsDynamodbTypes.TransactWriteItemsOutput
        d_175_valueOrError0_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsDynamodbTypes.TransactWriteItemsOutput.default())()
        def lambda16_(d_176_e_):
            return AwsCryptographyKeyStoreTypes.Error_ComAmazonawsDynamodb(d_176_e_)

        d_175_valueOrError0_ = (d_173_maybeTransactWriteResponse_).MapFailure(lambda16_)
        if (d_175_valueOrError0_).IsFailure():
            output = (d_175_valueOrError0_).PropagateFailure()
            return output
        d_174_transactWriteItemsResponse_ = (d_175_valueOrError0_).Extract()
        output = Wrappers.Result_Success(d_174_transactWriteItemsResponse_)
        return output

    @staticmethod
    def GetActiveBranchKeyItem(branchKeyIdentifier, tableName, ddbClient):
        output: Wrappers.Result = None
        d_177_dynamoDbKey_: _dafny.Map
        d_177_dynamoDbKey_ = _dafny.Map({Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD: ComAmazonawsDynamodbTypes.AttributeValue_S(branchKeyIdentifier), Structure.default__.TYPE__FIELD: ComAmazonawsDynamodbTypes.AttributeValue_S(Structure.default__.BRANCH__KEY__ACTIVE__TYPE)})
        d_178_ItemRequest_: ComAmazonawsDynamodbTypes.GetItemInput
        d_178_ItemRequest_ = ComAmazonawsDynamodbTypes.GetItemInput_GetItemInput(tableName, d_177_dynamoDbKey_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_179_maybeGetItem_: Wrappers.Result
        out15_: Wrappers.Result
        out15_ = (ddbClient).GetItem(d_178_ItemRequest_)
        d_179_maybeGetItem_ = out15_
        d_180_getItemResponse_: ComAmazonawsDynamodbTypes.GetItemOutput
        d_181_valueOrError0_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsDynamodbTypes.GetItemOutput.default())()
        def lambda17_(d_182_e_):
            return AwsCryptographyKeyStoreTypes.Error_ComAmazonawsDynamodb(d_182_e_)

        d_181_valueOrError0_ = (d_179_maybeGetItem_).MapFailure(lambda17_)
        if (d_181_valueOrError0_).IsFailure():
            output = (d_181_valueOrError0_).PropagateFailure()
            return output
        d_180_getItemResponse_ = (d_181_valueOrError0_).Extract()
        d_183_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_183_valueOrError1_ = Wrappers.default__.Need((((d_180_getItemResponse_).Item).is_Some) and ((len(((d_180_getItemResponse_).Item).value)) >= (1)), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.NO__CORRESPONDING__BRANCH__KEY))
        if (d_183_valueOrError1_).IsFailure():
            output = (d_183_valueOrError1_).PropagateFailure()
            return output
        d_184_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_184_valueOrError2_ = Wrappers.default__.Need((Structure.default__.ActiveBranchKeyItem_q(((d_180_getItemResponse_).Item).value)) and ((((((d_180_getItemResponse_).Item).value)[Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD]).S) == (branchKeyIdentifier)), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Item found is not a valid active branch key.")))
        if (d_184_valueOrError2_).IsFailure():
            output = (d_184_valueOrError2_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(((d_180_getItemResponse_).Item).value)
        return output

    @staticmethod
    def GetVersionBranchKeyItem(branchKeyIdentifier, branchKeyVersion, tableName, ddbClient):
        output: Wrappers.Result = None
        d_185_dynamoDbKey_: _dafny.Map
        d_185_dynamoDbKey_ = _dafny.Map({Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD: ComAmazonawsDynamodbTypes.AttributeValue_S(branchKeyIdentifier), Structure.default__.TYPE__FIELD: ComAmazonawsDynamodbTypes.AttributeValue_S((Structure.default__.BRANCH__KEY__TYPE__PREFIX) + (branchKeyVersion))})
        d_186_ItemRequest_: ComAmazonawsDynamodbTypes.GetItemInput
        d_186_ItemRequest_ = ComAmazonawsDynamodbTypes.GetItemInput_GetItemInput(tableName, d_185_dynamoDbKey_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_187_maybeGetItem_: Wrappers.Result
        out16_: Wrappers.Result
        out16_ = (ddbClient).GetItem(d_186_ItemRequest_)
        d_187_maybeGetItem_ = out16_
        d_188_getItemResponse_: ComAmazonawsDynamodbTypes.GetItemOutput
        d_189_valueOrError0_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsDynamodbTypes.GetItemOutput.default())()
        def lambda18_(d_190_e_):
            return AwsCryptographyKeyStoreTypes.Error_ComAmazonawsDynamodb(d_190_e_)

        d_189_valueOrError0_ = (d_187_maybeGetItem_).MapFailure(lambda18_)
        if (d_189_valueOrError0_).IsFailure():
            output = (d_189_valueOrError0_).PropagateFailure()
            return output
        d_188_getItemResponse_ = (d_189_valueOrError0_).Extract()
        d_191_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_191_valueOrError1_ = Wrappers.default__.Need((((d_188_getItemResponse_).Item).is_Some) and ((len(((d_188_getItemResponse_).Item).value)) >= (1)), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.NO__CORRESPONDING__BRANCH__KEY))
        if (d_191_valueOrError1_).IsFailure():
            output = (d_191_valueOrError1_).PropagateFailure()
            return output
        d_192_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_192_valueOrError2_ = Wrappers.default__.Need(((Structure.default__.VersionBranchKeyItem_q(((d_188_getItemResponse_).Item).value)) and ((((((d_188_getItemResponse_).Item).value)[Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD]).S) == (branchKeyIdentifier))) and ((((((d_188_getItemResponse_).Item).value)[Structure.default__.TYPE__FIELD]).S) == ((Structure.default__.BRANCH__KEY__TYPE__PREFIX) + (branchKeyVersion))), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Item found is not a valid branch key version.")))
        if (d_192_valueOrError2_).IsFailure():
            output = (d_192_valueOrError2_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(((d_188_getItemResponse_).Item).value)
        return output

    @staticmethod
    def GetBeaconKeyItem(branchKeyIdentifier, tableName, ddbClient):
        output: Wrappers.Result = None
        d_193_dynamoDbKey_: _dafny.Map
        d_193_dynamoDbKey_ = _dafny.Map({Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD: ComAmazonawsDynamodbTypes.AttributeValue_S(branchKeyIdentifier), Structure.default__.TYPE__FIELD: ComAmazonawsDynamodbTypes.AttributeValue_S(Structure.default__.BEACON__KEY__TYPE__VALUE)})
        d_194_ItemRequest_: ComAmazonawsDynamodbTypes.GetItemInput
        d_194_ItemRequest_ = ComAmazonawsDynamodbTypes.GetItemInput_GetItemInput(tableName, d_193_dynamoDbKey_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_195_maybeGetItem_: Wrappers.Result
        out17_: Wrappers.Result
        out17_ = (ddbClient).GetItem(d_194_ItemRequest_)
        d_195_maybeGetItem_ = out17_
        d_196_getItemResponse_: ComAmazonawsDynamodbTypes.GetItemOutput
        d_197_valueOrError0_: Wrappers.Result = Wrappers.Result.default(ComAmazonawsDynamodbTypes.GetItemOutput.default())()
        def lambda19_(d_198_e_):
            return AwsCryptographyKeyStoreTypes.Error_ComAmazonawsDynamodb(d_198_e_)

        d_197_valueOrError0_ = (d_195_maybeGetItem_).MapFailure(lambda19_)
        if (d_197_valueOrError0_).IsFailure():
            output = (d_197_valueOrError0_).PropagateFailure()
            return output
        d_196_getItemResponse_ = (d_197_valueOrError0_).Extract()
        d_199_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_199_valueOrError1_ = Wrappers.default__.Need((((d_196_getItemResponse_).Item).is_Some) and ((len(((d_196_getItemResponse_).Item).value)) >= (1)), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(KeyStoreErrorMessages.default__.NO__CORRESPONDING__BRANCH__KEY))
        if (d_199_valueOrError1_).IsFailure():
            output = (d_199_valueOrError1_).PropagateFailure()
            return output
        d_200_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_200_valueOrError2_ = Wrappers.default__.Need((Structure.default__.BeaconKeyItem_q(((d_196_getItemResponse_).Item).value)) and ((((((d_196_getItemResponse_).Item).value)[Structure.default__.BRANCH__KEY__IDENTIFIER__FIELD]).S) == (branchKeyIdentifier)), AwsCryptographyKeyStoreTypes.Error_KeyStoreException(_dafny.Seq("Item found is not a valid beacon key.")))
        if (d_200_valueOrError2_).IsFailure():
            output = (d_200_valueOrError2_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(((d_196_getItemResponse_).Item).value)
        return output

    @staticmethod
    def CreateTransactWritePutItem(item, tableName, ConditionExpression):
        def lambda20_():
            source10_ = ConditionExpression
            unmatched10 = True
            if unmatched10:
                if source10_.is_BRANCH__KEY__NOT__EXIST:
                    unmatched10 = False
                    return default__.BRANCH__KEY__NOT__EXIST__CONDITION
            if unmatched10:
                unmatched10 = False
                return default__.BRANCH__KEY__EXISTS__CONDITION
            raise Exception("unexpected control point")

        return ComAmazonawsDynamodbTypes.TransactWriteItem_TransactWriteItem(Wrappers.Option_None(), Wrappers.Option_Some(ComAmazonawsDynamodbTypes.Put_Put(item, tableName, Wrappers.Option_Some(lambda20_()), Wrappers.Option_Some(default__.BRANCH__KEY__EXISTS__EXPRESSION__ATTRIBUTE__NAMES), Wrappers.Option_None(), Wrappers.Option_None())), Wrappers.Option_None(), Wrappers.Option_None())

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

