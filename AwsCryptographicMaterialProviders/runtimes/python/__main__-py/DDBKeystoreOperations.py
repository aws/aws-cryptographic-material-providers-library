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

assert "DDBKeystoreOperations" == __name__
DDBKeystoreOperations = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def WriteNewKeyToStore(versionBranchKeyItem, activeBranchKeyItem, beaconKeyItem, tableName, ddbClient):
        output: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsOutput.default())()
        d_140_items_: _dafny.Seq
        d_140_items_ = _dafny.Seq([DDBKeystoreOperations.default__.CreateTransactWritePutItem(versionBranchKeyItem, tableName, DDBKeystoreOperations.ConditionExpression_BRANCH__KEY__NOT__EXIST()), DDBKeystoreOperations.default__.CreateTransactWritePutItem(activeBranchKeyItem, tableName, DDBKeystoreOperations.ConditionExpression_BRANCH__KEY__NOT__EXIST()), DDBKeystoreOperations.default__.CreateTransactWritePutItem(beaconKeyItem, tableName, DDBKeystoreOperations.ConditionExpression_BRANCH__KEY__NOT__EXIST())])
        d_141_transactRequest_: software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsInput
        d_141_transactRequest_ = software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsInput_TransactWriteItemsInput(d_140_items_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_142_maybeTransactWriteResponse_: Wrappers.Result
        out13_: Wrappers.Result
        out13_ = (ddbClient).TransactWriteItems(d_141_transactRequest_)
        d_142_maybeTransactWriteResponse_ = out13_
        d_143_transactWriteItemsResponse_: software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsOutput
        d_144_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsOutput.default())()
        def lambda14_(d_145_e_):
            return software_amazon_cryptography_keystore_internaldafny_types.Error_ComAmazonawsDynamodb(d_145_e_)

        d_144_valueOrError0_ = (d_142_maybeTransactWriteResponse_).MapFailure(lambda14_)
        if (d_144_valueOrError0_).IsFailure():
            output = (d_144_valueOrError0_).PropagateFailure()
            return output
        d_143_transactWriteItemsResponse_ = (d_144_valueOrError0_).Extract()
        output = Wrappers.Result_Success(d_143_transactWriteItemsResponse_)
        return output

    @staticmethod
    def WriteNewBranchKeyVersionToKeystore(versionBranchKeyItem, activeBranchKeyItem, tableName, ddbClient):
        output: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsOutput.default())()
        d_146_items_: _dafny.Seq
        d_146_items_ = _dafny.Seq([DDBKeystoreOperations.default__.CreateTransactWritePutItem(versionBranchKeyItem, tableName, DDBKeystoreOperations.ConditionExpression_BRANCH__KEY__NOT__EXIST()), DDBKeystoreOperations.default__.CreateTransactWritePutItem(activeBranchKeyItem, tableName, DDBKeystoreOperations.ConditionExpression_BRANCH__KEY__EXISTS())])
        d_147_transactRequest_: software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsInput
        d_147_transactRequest_ = software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsInput_TransactWriteItemsInput(d_146_items_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_148_maybeTransactWriteResponse_: Wrappers.Result
        out14_: Wrappers.Result
        out14_ = (ddbClient).TransactWriteItems(d_147_transactRequest_)
        d_148_maybeTransactWriteResponse_ = out14_
        d_149_transactWriteItemsResponse_: software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsOutput
        d_150_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsOutput.default())()
        def lambda15_(d_151_e_):
            return software_amazon_cryptography_keystore_internaldafny_types.Error_ComAmazonawsDynamodb(d_151_e_)

        d_150_valueOrError0_ = (d_148_maybeTransactWriteResponse_).MapFailure(lambda15_)
        if (d_150_valueOrError0_).IsFailure():
            output = (d_150_valueOrError0_).PropagateFailure()
            return output
        d_149_transactWriteItemsResponse_ = (d_150_valueOrError0_).Extract()
        output = Wrappers.Result_Success(d_149_transactWriteItemsResponse_)
        return output

    @staticmethod
    def GetActiveBranchKeyItem(branchKeyIdentifier, tableName, ddbClient):
        output: Wrappers.Result = None
        d_152_dynamoDbKey_: _dafny.Map
        d_152_dynamoDbKey_ = _dafny.Map({(Structure.default__).BRANCH__KEY__IDENTIFIER__FIELD: software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S(branchKeyIdentifier), (Structure.default__).TYPE__FIELD: software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S((Structure.default__).BRANCH__KEY__ACTIVE__TYPE)})
        d_153_ItemRequest_: software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemInput
        d_153_ItemRequest_ = software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemInput_GetItemInput(tableName, d_152_dynamoDbKey_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_154_maybeGetItem_: Wrappers.Result
        out15_: Wrappers.Result
        out15_ = (ddbClient).GetItem(d_153_ItemRequest_)
        d_154_maybeGetItem_ = out15_
        d_155_getItemResponse_: software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemOutput
        d_156_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemOutput.default())()
        def lambda16_(d_157_e_):
            return software_amazon_cryptography_keystore_internaldafny_types.Error_ComAmazonawsDynamodb(d_157_e_)

        d_156_valueOrError0_ = (d_154_maybeGetItem_).MapFailure(lambda16_)
        if (d_156_valueOrError0_).IsFailure():
            output = (d_156_valueOrError0_).PropagateFailure()
            return output
        d_155_getItemResponse_ = (d_156_valueOrError0_).Extract()
        d_158_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_158_valueOrError1_ = Wrappers.default__.Need(((d_155_getItemResponse_).Item).is_Some, software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("No item found for corresponding branch key identifier.")))
        if (d_158_valueOrError1_).IsFailure():
            output = (d_158_valueOrError1_).PropagateFailure()
            return output
        d_159_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_159_valueOrError2_ = Wrappers.default__.Need((Structure.default__.ActiveBranchKeyItem_q(((d_155_getItemResponse_).Item).value)) and ((((((d_155_getItemResponse_).Item).value)[(Structure.default__).BRANCH__KEY__IDENTIFIER__FIELD]).S) == (branchKeyIdentifier)), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Item found is not a valid active branch key.")))
        if (d_159_valueOrError2_).IsFailure():
            output = (d_159_valueOrError2_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(((d_155_getItemResponse_).Item).value)
        return output

    @staticmethod
    def GetVersionBranchKeyItem(branchKeyIdentifier, branchKeyVersion, tableName, ddbClient):
        output: Wrappers.Result = None
        d_160_dynamoDbKey_: _dafny.Map
        d_160_dynamoDbKey_ = _dafny.Map({(Structure.default__).BRANCH__KEY__IDENTIFIER__FIELD: software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S(branchKeyIdentifier), (Structure.default__).TYPE__FIELD: software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S(((Structure.default__).BRANCH__KEY__TYPE__PREFIX) + (branchKeyVersion))})
        d_161_ItemRequest_: software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemInput
        d_161_ItemRequest_ = software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemInput_GetItemInput(tableName, d_160_dynamoDbKey_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_162_maybeGetItem_: Wrappers.Result
        out16_: Wrappers.Result
        out16_ = (ddbClient).GetItem(d_161_ItemRequest_)
        d_162_maybeGetItem_ = out16_
        d_163_getItemResponse_: software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemOutput
        d_164_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemOutput.default())()
        def lambda17_(d_165_e_):
            return software_amazon_cryptography_keystore_internaldafny_types.Error_ComAmazonawsDynamodb(d_165_e_)

        d_164_valueOrError0_ = (d_162_maybeGetItem_).MapFailure(lambda17_)
        if (d_164_valueOrError0_).IsFailure():
            output = (d_164_valueOrError0_).PropagateFailure()
            return output
        d_163_getItemResponse_ = (d_164_valueOrError0_).Extract()
        d_166_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_166_valueOrError1_ = Wrappers.default__.Need(((d_163_getItemResponse_).Item).is_Some, software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("No item found for corresponding branch key identifier.")))
        if (d_166_valueOrError1_).IsFailure():
            output = (d_166_valueOrError1_).PropagateFailure()
            return output
        d_167_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_167_valueOrError2_ = Wrappers.default__.Need(((Structure.default__.VersionBranchKeyItem_q(((d_163_getItemResponse_).Item).value)) and ((((((d_163_getItemResponse_).Item).value)[(Structure.default__).BRANCH__KEY__IDENTIFIER__FIELD]).S) == (branchKeyIdentifier))) and ((((((d_163_getItemResponse_).Item).value)[(Structure.default__).TYPE__FIELD]).S) == (((Structure.default__).BRANCH__KEY__TYPE__PREFIX) + (branchKeyVersion))), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Item found is not a valid branch key version.")))
        if (d_167_valueOrError2_).IsFailure():
            output = (d_167_valueOrError2_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(((d_163_getItemResponse_).Item).value)
        return output

    @staticmethod
    def GetBeaconKeyItem(branchKeyIdentifier, tableName, ddbClient):
        output: Wrappers.Result = None
        d_168_dynamoDbKey_: _dafny.Map
        d_168_dynamoDbKey_ = _dafny.Map({(Structure.default__).BRANCH__KEY__IDENTIFIER__FIELD: software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S(branchKeyIdentifier), (Structure.default__).TYPE__FIELD: software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S((Structure.default__).BEACON__KEY__TYPE__VALUE)})
        d_169_ItemRequest_: software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemInput
        d_169_ItemRequest_ = software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemInput_GetItemInput(tableName, d_168_dynamoDbKey_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_170_maybeGetItem_: Wrappers.Result
        out17_: Wrappers.Result
        out17_ = (ddbClient).GetItem(d_169_ItemRequest_)
        d_170_maybeGetItem_ = out17_
        d_171_getItemResponse_: software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemOutput
        d_172_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemOutput.default())()
        def lambda18_(d_173_e_):
            return software_amazon_cryptography_keystore_internaldafny_types.Error_ComAmazonawsDynamodb(d_173_e_)

        d_172_valueOrError0_ = (d_170_maybeGetItem_).MapFailure(lambda18_)
        if (d_172_valueOrError0_).IsFailure():
            output = (d_172_valueOrError0_).PropagateFailure()
            return output
        d_171_getItemResponse_ = (d_172_valueOrError0_).Extract()
        d_174_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_174_valueOrError1_ = Wrappers.default__.Need(((d_171_getItemResponse_).Item).is_Some, software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("No item found for corresponding branch key identifier.")))
        if (d_174_valueOrError1_).IsFailure():
            output = (d_174_valueOrError1_).PropagateFailure()
            return output
        d_175_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_175_valueOrError2_ = Wrappers.default__.Need((Structure.default__.BeaconKeyItem_q(((d_171_getItemResponse_).Item).value)) and ((((((d_171_getItemResponse_).Item).value)[(Structure.default__).BRANCH__KEY__IDENTIFIER__FIELD]).S) == (branchKeyIdentifier)), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Item found is not a valid beacon key.")))
        if (d_175_valueOrError2_).IsFailure():
            output = (d_175_valueOrError2_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(((d_171_getItemResponse_).Item).value)
        return output

    @staticmethod
    def CreateTransactWritePutItem(item, tableName, ConditionExpression):
        def lambda19_(source9_):
            if source9_.is_BRANCH__KEY__NOT__EXIST:
                return (DDBKeystoreOperations.default__).BRANCH__KEY__NOT__EXIST__CONDITION
            elif True:
                return (DDBKeystoreOperations.default__).BRANCH__KEY__EXISTS__CONDITION

        return software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItem_TransactWriteItem(Wrappers.Option_None(), Wrappers.Option_Some(software_amazon_cryptography_services_dynamodb_internaldafny_types.Put_Put(item, tableName, Wrappers.Option_Some(lambda19_(ConditionExpression)), Wrappers.Option_Some((DDBKeystoreOperations.default__).BRANCH__KEY__EXISTS__EXPRESSION__ATTRIBUTE__NAMES), Wrappers.Option_None(), Wrappers.Option_None())), Wrappers.Option_None(), Wrappers.Option_None())

    @_dafny.classproperty
    def BRANCH__KEY__EXISTS__EXPRESSION__ATTRIBUTE__NAME(instance):
        return _dafny.Seq("#BranchKeyIdentifierField")
    @_dafny.classproperty
    def BRANCH__KEY__EXISTS__EXPRESSION__ATTRIBUTE__NAMES(instance):
        return _dafny.Map({(DDBKeystoreOperations.default__).BRANCH__KEY__EXISTS__EXPRESSION__ATTRIBUTE__NAME: (Structure.default__).BRANCH__KEY__IDENTIFIER__FIELD})
    @_dafny.classproperty
    def BRANCH__KEY__NOT__EXIST__CONDITION(instance):
        return ((_dafny.Seq("attribute_not_exists(")) + ((DDBKeystoreOperations.default__).BRANCH__KEY__EXISTS__EXPRESSION__ATTRIBUTE__NAME)) + (_dafny.Seq(")"))
    @_dafny.classproperty
    def BRANCH__KEY__EXISTS__CONDITION(instance):
        return ((_dafny.Seq("attribute_exists(")) + ((DDBKeystoreOperations.default__).BRANCH__KEY__EXISTS__EXPRESSION__ATTRIBUTE__NAME)) + (_dafny.Seq(")"))

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
        return isinstance(self, DDBKeystoreOperations.ConditionExpression_BRANCH__KEY__NOT__EXIST)
    @property
    def is_BRANCH__KEY__EXISTS(self) -> bool:
        return isinstance(self, DDBKeystoreOperations.ConditionExpression_BRANCH__KEY__EXISTS)

class ConditionExpression_BRANCH__KEY__NOT__EXIST(ConditionExpression, NamedTuple('BRANCH__KEY__NOT__EXIST', [])):
    def __dafnystr__(self) -> str:
        return f'DDBKeystoreOperations.ConditionExpression.BRANCH_KEY_NOT_EXIST'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DDBKeystoreOperations.ConditionExpression_BRANCH__KEY__NOT__EXIST)
    def __hash__(self) -> int:
        return super().__hash__()

class ConditionExpression_BRANCH__KEY__EXISTS(ConditionExpression, NamedTuple('BRANCH__KEY__EXISTS', [])):
    def __dafnystr__(self) -> str:
        return f'DDBKeystoreOperations.ConditionExpression.BRANCH_KEY_EXISTS'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DDBKeystoreOperations.ConditionExpression_BRANCH__KEY__EXISTS)
    def __hash__(self) -> int:
        return super().__hash__()

