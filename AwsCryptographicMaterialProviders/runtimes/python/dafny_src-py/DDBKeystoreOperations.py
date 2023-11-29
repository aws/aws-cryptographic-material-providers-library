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
        d_139_items_: _dafny.Seq
        d_139_items_ = _dafny.Seq([DDBKeystoreOperations.default__.CreateTransactWritePutItem(versionBranchKeyItem, tableName, DDBKeystoreOperations.ConditionExpression_BRANCH__KEY__NOT__EXIST()), DDBKeystoreOperations.default__.CreateTransactWritePutItem(activeBranchKeyItem, tableName, DDBKeystoreOperations.ConditionExpression_BRANCH__KEY__NOT__EXIST()), DDBKeystoreOperations.default__.CreateTransactWritePutItem(beaconKeyItem, tableName, DDBKeystoreOperations.ConditionExpression_BRANCH__KEY__NOT__EXIST())])
        d_140_transactRequest_: software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsInput
        d_140_transactRequest_ = software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsInput_TransactWriteItemsInput(d_139_items_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_141_maybeTransactWriteResponse_: Wrappers.Result
        out13_: Wrappers.Result
        out13_ = (ddbClient).TransactWriteItems(d_140_transactRequest_)
        d_141_maybeTransactWriteResponse_ = out13_
        d_142_transactWriteItemsResponse_: software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsOutput
        d_143_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsOutput.default())()
        def lambda14_(d_144_e_):
            return software_amazon_cryptography_keystore_internaldafny_types.Error_ComAmazonawsDynamodb(d_144_e_)

        d_143_valueOrError0_ = (d_141_maybeTransactWriteResponse_).MapFailure(lambda14_)
        if (d_143_valueOrError0_).IsFailure():
            output = (d_143_valueOrError0_).PropagateFailure()
            return output
        d_142_transactWriteItemsResponse_ = (d_143_valueOrError0_).Extract()
        output = Wrappers.Result_Success(d_142_transactWriteItemsResponse_)
        return output

    @staticmethod
    def WriteNewBranchKeyVersionToKeystore(versionBranchKeyItem, activeBranchKeyItem, tableName, ddbClient):
        output: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsOutput.default())()
        d_145_items_: _dafny.Seq
        d_145_items_ = _dafny.Seq([DDBKeystoreOperations.default__.CreateTransactWritePutItem(versionBranchKeyItem, tableName, DDBKeystoreOperations.ConditionExpression_BRANCH__KEY__NOT__EXIST()), DDBKeystoreOperations.default__.CreateTransactWritePutItem(activeBranchKeyItem, tableName, DDBKeystoreOperations.ConditionExpression_BRANCH__KEY__EXISTS())])
        d_146_transactRequest_: software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsInput
        d_146_transactRequest_ = software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsInput_TransactWriteItemsInput(d_145_items_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_147_maybeTransactWriteResponse_: Wrappers.Result
        out14_: Wrappers.Result
        out14_ = (ddbClient).TransactWriteItems(d_146_transactRequest_)
        d_147_maybeTransactWriteResponse_ = out14_
        d_148_transactWriteItemsResponse_: software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsOutput
        d_149_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_dynamodb_internaldafny_types.TransactWriteItemsOutput.default())()
        def lambda15_(d_150_e_):
            return software_amazon_cryptography_keystore_internaldafny_types.Error_ComAmazonawsDynamodb(d_150_e_)

        d_149_valueOrError0_ = (d_147_maybeTransactWriteResponse_).MapFailure(lambda15_)
        if (d_149_valueOrError0_).IsFailure():
            output = (d_149_valueOrError0_).PropagateFailure()
            return output
        d_148_transactWriteItemsResponse_ = (d_149_valueOrError0_).Extract()
        output = Wrappers.Result_Success(d_148_transactWriteItemsResponse_)
        return output

    @staticmethod
    def GetActiveBranchKeyItem(branchKeyIdentifier, tableName, ddbClient):
        output: Wrappers.Result = None
        d_151_dynamoDbKey_: _dafny.Map
        d_151_dynamoDbKey_ = _dafny.Map({(Structure.default__).BRANCH__KEY__IDENTIFIER__FIELD: software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S(branchKeyIdentifier), (Structure.default__).TYPE__FIELD: software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S((Structure.default__).BRANCH__KEY__ACTIVE__TYPE)})
        d_152_ItemRequest_: software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemInput
        d_152_ItemRequest_ = software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemInput_GetItemInput(tableName, d_151_dynamoDbKey_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_153_maybeGetItem_: Wrappers.Result
        out15_: Wrappers.Result
        out15_ = (ddbClient).GetItem(d_152_ItemRequest_)
        d_153_maybeGetItem_ = out15_
        d_154_getItemResponse_: software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemOutput
        d_155_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemOutput.default())()
        def lambda16_(d_156_e_):
            return software_amazon_cryptography_keystore_internaldafny_types.Error_ComAmazonawsDynamodb(d_156_e_)

        d_155_valueOrError0_ = (d_153_maybeGetItem_).MapFailure(lambda16_)
        if (d_155_valueOrError0_).IsFailure():
            output = (d_155_valueOrError0_).PropagateFailure()
            return output
        d_154_getItemResponse_ = (d_155_valueOrError0_).Extract()
        d_157_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_157_valueOrError1_ = Wrappers.default__.Need(((d_154_getItemResponse_).Item).is_Some, software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("No item found for corresponding branch key identifier.")))
        if (d_157_valueOrError1_).IsFailure():
            output = (d_157_valueOrError1_).PropagateFailure()
            return output
        d_158_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_158_valueOrError2_ = Wrappers.default__.Need((Structure.default__.ActiveBranchKeyItem_q(((d_154_getItemResponse_).Item).value)) and ((((((d_154_getItemResponse_).Item).value)[(Structure.default__).BRANCH__KEY__IDENTIFIER__FIELD]).S) == (branchKeyIdentifier)), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Item found is not a valid active branch key.")))
        if (d_158_valueOrError2_).IsFailure():
            output = (d_158_valueOrError2_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(((d_154_getItemResponse_).Item).value)
        return output

    @staticmethod
    def GetVersionBranchKeyItem(branchKeyIdentifier, branchKeyVersion, tableName, ddbClient):
        output: Wrappers.Result = None
        d_159_dynamoDbKey_: _dafny.Map
        d_159_dynamoDbKey_ = _dafny.Map({(Structure.default__).BRANCH__KEY__IDENTIFIER__FIELD: software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S(branchKeyIdentifier), (Structure.default__).TYPE__FIELD: software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S(((Structure.default__).BRANCH__KEY__TYPE__PREFIX) + (branchKeyVersion))})
        d_160_ItemRequest_: software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemInput
        d_160_ItemRequest_ = software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemInput_GetItemInput(tableName, d_159_dynamoDbKey_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_161_maybeGetItem_: Wrappers.Result
        out16_: Wrappers.Result
        out16_ = (ddbClient).GetItem(d_160_ItemRequest_)
        d_161_maybeGetItem_ = out16_
        d_162_getItemResponse_: software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemOutput
        d_163_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemOutput.default())()
        def lambda17_(d_164_e_):
            return software_amazon_cryptography_keystore_internaldafny_types.Error_ComAmazonawsDynamodb(d_164_e_)

        d_163_valueOrError0_ = (d_161_maybeGetItem_).MapFailure(lambda17_)
        if (d_163_valueOrError0_).IsFailure():
            output = (d_163_valueOrError0_).PropagateFailure()
            return output
        d_162_getItemResponse_ = (d_163_valueOrError0_).Extract()
        d_165_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_165_valueOrError1_ = Wrappers.default__.Need(((d_162_getItemResponse_).Item).is_Some, software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("No item found for corresponding branch key identifier.")))
        if (d_165_valueOrError1_).IsFailure():
            output = (d_165_valueOrError1_).PropagateFailure()
            return output
        d_166_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_166_valueOrError2_ = Wrappers.default__.Need(((Structure.default__.VersionBranchKeyItem_q(((d_162_getItemResponse_).Item).value)) and ((((((d_162_getItemResponse_).Item).value)[(Structure.default__).BRANCH__KEY__IDENTIFIER__FIELD]).S) == (branchKeyIdentifier))) and ((((((d_162_getItemResponse_).Item).value)[(Structure.default__).TYPE__FIELD]).S) == (((Structure.default__).BRANCH__KEY__TYPE__PREFIX) + (branchKeyVersion))), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Item found is not a valid branch key version.")))
        if (d_166_valueOrError2_).IsFailure():
            output = (d_166_valueOrError2_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(((d_162_getItemResponse_).Item).value)
        return output

    @staticmethod
    def GetBeaconKeyItem(branchKeyIdentifier, tableName, ddbClient):
        output: Wrappers.Result = None
        d_167_dynamoDbKey_: _dafny.Map
        d_167_dynamoDbKey_ = _dafny.Map({(Structure.default__).BRANCH__KEY__IDENTIFIER__FIELD: software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S(branchKeyIdentifier), (Structure.default__).TYPE__FIELD: software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S((Structure.default__).BEACON__KEY__TYPE__VALUE)})
        d_168_ItemRequest_: software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemInput
        d_168_ItemRequest_ = software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemInput_GetItemInput(tableName, d_167_dynamoDbKey_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_169_maybeGetItem_: Wrappers.Result
        out17_: Wrappers.Result
        out17_ = (ddbClient).GetItem(d_168_ItemRequest_)
        d_169_maybeGetItem_ = out17_
        d_170_getItemResponse_: software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemOutput
        d_171_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemOutput.default())()
        def lambda18_(d_172_e_):
            return software_amazon_cryptography_keystore_internaldafny_types.Error_ComAmazonawsDynamodb(d_172_e_)

        d_171_valueOrError0_ = (d_169_maybeGetItem_).MapFailure(lambda18_)
        if (d_171_valueOrError0_).IsFailure():
            output = (d_171_valueOrError0_).PropagateFailure()
            return output
        d_170_getItemResponse_ = (d_171_valueOrError0_).Extract()
        d_173_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_173_valueOrError1_ = Wrappers.default__.Need(((d_170_getItemResponse_).Item).is_Some, software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("No item found for corresponding branch key identifier.")))
        if (d_173_valueOrError1_).IsFailure():
            output = (d_173_valueOrError1_).PropagateFailure()
            return output
        d_174_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_174_valueOrError2_ = Wrappers.default__.Need((Structure.default__.BeaconKeyItem_q(((d_170_getItemResponse_).Item).value)) and ((((((d_170_getItemResponse_).Item).value)[(Structure.default__).BRANCH__KEY__IDENTIFIER__FIELD]).S) == (branchKeyIdentifier)), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Item found is not a valid beacon key.")))
        if (d_174_valueOrError2_).IsFailure():
            output = (d_174_valueOrError2_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(((d_170_getItemResponse_).Item).value)
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

