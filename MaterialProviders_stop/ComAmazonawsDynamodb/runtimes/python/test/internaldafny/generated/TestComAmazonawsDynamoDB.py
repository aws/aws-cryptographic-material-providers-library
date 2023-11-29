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
import software_amazon_cryptography_services_dynamodb_internaldafny

assert "TestComAmazonawsDynamoDB" == __name__
TestComAmazonawsDynamoDB = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def BasicPutGetQuery():
        d_0_client_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_1_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_1_valueOrError0_ = out0_
        if not(not((d_1_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestComAmazonawsDynamodb.dfy(20,15): " + _dafny.string_of(d_1_valueOrError0_))
        d_0_client_ = (d_1_valueOrError0_).Extract()
        d_2_item_: _dafny.Map
        d_2_item_ = _dafny.Map({_dafny.Seq("branch-key-id"): software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S(_dafny.Seq("ddb-client-test")), _dafny.Seq("type"): software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S(_dafny.Seq("ddb-client-test")), _dafny.Seq("status"): software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S(_dafny.Seq("ACTIVE"))})
        d_3_putInput_: software_amazon_cryptography_services_dynamodb_internaldafny_types.PutItemInput
        d_3_putInput_ = software_amazon_cryptography_services_dynamodb_internaldafny_types.PutItemInput_PutItemInput((TestComAmazonawsDynamoDB.default__).tableNameTest, d_2_item_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_4_putRet_: Wrappers.Result
        out1_: Wrappers.Result
        out1_ = (d_0_client_).PutItem(d_3_putInput_)
        d_4_putRet_ = out1_
        if not((d_4_putRet_).is_Success):
            raise _dafny.HaltException("test/TestComAmazonawsDynamodb.dfy(44,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_5_Key2Get_: _dafny.Map
        d_5_Key2Get_ = _dafny.Map({_dafny.Seq("branch-key-id"): software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S(_dafny.Seq("ddb-client-test")), _dafny.Seq("type"): software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S(_dafny.Seq("ddb-client-test"))})
        d_6_getInput_: software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemInput
        d_6_getInput_ = software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemInput_GetItemInput((TestComAmazonawsDynamoDB.default__).tableNameTest, d_5_Key2Get_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_7_getRet_: Wrappers.Result
        out2_: Wrappers.Result
        out2_ = (d_0_client_).GetItem(d_6_getInput_)
        d_7_getRet_ = out2_
        if not((d_7_getRet_).is_Success):
            raise _dafny.HaltException("test/TestComAmazonawsDynamodb.dfy(63,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_8_itemOutput_: software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemOutput
        d_8_itemOutput_ = (d_7_getRet_).value
        if not(((d_8_itemOutput_).Item).is_Some):
            raise _dafny.HaltException("test/TestComAmazonawsDynamodb.dfy(66,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_9_gotItem_: _dafny.Map
        d_9_gotItem_ = ((d_8_itemOutput_).Item).value
        if not((d_9_gotItem_) == (d_2_item_)):
            raise _dafny.HaltException("test/TestComAmazonawsDynamodb.dfy(68,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_10_attributeNameMap_: _dafny.Map
        d_10_attributeNameMap_ = _dafny.Map({_dafny.Seq("#status"): _dafny.Seq("status"), _dafny.Seq("#branchKeyId"): _dafny.Seq("branch-key-id")})
        d_11_attributeValueMap_: _dafny.Map
        d_11_attributeValueMap_ = _dafny.Map({_dafny.Seq(":status"): software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S(_dafny.Seq("ACTIVE")), _dafny.Seq(":branchKeyId"): software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S(_dafny.Seq("ddb-client-test"))})
        d_12_queryInput_: software_amazon_cryptography_services_dynamodb_internaldafny_types.QueryInput
        d_12_queryInput_ = software_amazon_cryptography_services_dynamodb_internaldafny_types.QueryInput_QueryInput((TestComAmazonawsDynamoDB.default__).tableNameTest, Wrappers.Option_Some((TestComAmazonawsDynamoDB.default__).secIndex), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(_dafny.Seq("#status = :status and #branchKeyId = :branchKeyId")), Wrappers.Option_Some(d_10_attributeNameMap_), Wrappers.Option_Some(d_11_attributeValueMap_))
        d_13_queryRet_: Wrappers.Result
        out3_: Wrappers.Result
        out3_ = (d_0_client_).Query(d_12_queryInput_)
        d_13_queryRet_ = out3_
        if not((d_13_queryRet_).is_Success):
            raise _dafny.HaltException("test/TestComAmazonawsDynamodb.dfy(103,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_14_queryOutput_: software_amazon_cryptography_services_dynamodb_internaldafny_types.QueryOutput
        d_14_queryOutput_ = (d_13_queryRet_).value
        if not(((d_14_queryOutput_).Items).is_Some):
            raise _dafny.HaltException("test/TestComAmazonawsDynamodb.dfy(106,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_15_queryItem_: _dafny.Seq
        d_15_queryItem_ = ((d_14_queryOutput_).Items).value
        if not((len(d_15_queryItem_)) == (1)):
            raise _dafny.HaltException("test/TestComAmazonawsDynamodb.dfy(108,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_16_queriedItem_: _dafny.Map
        d_16_queriedItem_ = (d_15_queryItem_)[0]
        if not((d_2_item_) == (d_16_queriedItem_)):
            raise _dafny.HaltException("test/TestComAmazonawsDynamodb.dfy(110,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @_dafny.classproperty
    def tableNameTest(instance):
        return _dafny.Seq("KeyStoreTestTable")
    @_dafny.classproperty
    def secIndex(instance):
        return _dafny.Seq("Active-Keys")
