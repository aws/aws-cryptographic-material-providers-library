import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import StandardLibrary_mUInt
import StandardLibrary
import UTF8
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_dynamodb_internaldafny

assert "TestDDBv2" == __name__
TestDDBv2 = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def BasicQueryTests():
        d_0_attributeNameMap_: _dafny.Map
        d_0_attributeNameMap_ = _dafny.Map({_dafny.Seq("#bkid"): _dafny.Seq("branch-key-id"), _dafny.Seq("#status"): _dafny.Seq("status")})
        d_1_attributeValueMap_: _dafny.Map
        d_1_attributeValueMap_ = _dafny.Map({_dafny.Seq(":bkid"): software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S(_dafny.Seq("aws-kms-h")), _dafny.Seq(":status"): software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S(_dafny.Seq("ACTIVE"))})
        d_2_queryInput_: software_amazon_cryptography_services_dynamodb_internaldafny_types.QueryInput
        d_2_queryInput_ = software_amazon_cryptography_services_dynamodb_internaldafny_types.QueryInput_QueryInput((TestDDBv2.default__).tableNameTest, Wrappers.Option_Some((TestDDBv2.default__).secIndex), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(_dafny.Seq("#status = :status and #bkid = :bkid")), Wrappers.Option_Some(d_0_attributeNameMap_), Wrappers.Option_Some(d_1_attributeValueMap_))
        TestDDBv2.default__.BasicQueryTest(d_2_queryInput_)

    @staticmethod
    def BasicGetTests():
        d_3_Key2Get_: _dafny.Map
        d_3_Key2Get_ = _dafny.Map({_dafny.Seq("branch-key-id"): software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S(_dafny.Seq("aws-kms-h")), _dafny.Seq("version"): software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S(_dafny.Seq("1"))})
        d_4_getInput_: software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemInput
        d_4_getInput_ = software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemInput_GetItemInput((TestDDBv2.default__).tableNameTest, d_3_Key2Get_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        TestDDBv2.default__.BasicGetTest(d_4_getInput_)

    @staticmethod
    def BasicPutTests():
        d_5_attributeValueMap_: _dafny.Map
        d_5_attributeValueMap_ = _dafny.Map({_dafny.Seq("branch-key-id"): software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S(_dafny.Seq("aws-kms-put-item")), _dafny.Seq("status"): software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S(_dafny.Seq("ACTIVE")), _dafny.Seq("version"): software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S(_dafny.Seq("version-1"))})
        d_6_putInput_: software_amazon_cryptography_services_dynamodb_internaldafny_types.PutItemInput
        d_6_putInput_ = software_amazon_cryptography_services_dynamodb_internaldafny_types.PutItemInput_PutItemInput((TestDDBv2.default__).tableNameTest, d_5_attributeValueMap_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        TestDDBv2.default__.BasicPutTest(d_6_putInput_)

    @staticmethod
    def BatGetItemTests():
        d_7_attributeNameBranchKey_: _dafny.Seq
        d_7_attributeNameBranchKey_ = _dafny.Seq("branch-key-id")
        d_8_attributeValueBranchKey_: software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue
        d_8_attributeValueBranchKey_ = software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S(_dafny.Seq("aws-kms-put-item"))
        d_9_attributeNameVersion_: _dafny.Seq
        d_9_attributeNameVersion_ = _dafny.Seq("version")
        d_10_attributeValueVersion_: software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue
        d_10_attributeValueVersion_ = software_amazon_cryptography_services_dynamodb_internaldafny_types.AttributeValue_S(_dafny.Seq("version-1"))
        d_11_key_: _dafny.Map
        d_11_key_ = _dafny.Map({d_7_attributeNameBranchKey_: d_8_attributeValueBranchKey_, d_9_attributeNameVersion_: d_10_attributeValueVersion_})
        d_12_keys_: _dafny.Seq
        d_12_keys_ = _dafny.Seq([d_11_key_])
        d_13_keyAndAttributes_: software_amazon_cryptography_services_dynamodb_internaldafny_types.KeysAndAttributes
        d_13_keyAndAttributes_ = software_amazon_cryptography_services_dynamodb_internaldafny_types.KeysAndAttributes_KeysAndAttributes(d_12_keys_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_14_batchGetRequestMap_: _dafny.Map
        d_14_batchGetRequestMap_ = _dafny.Map({(TestDDBv2.default__).tableNameTest: d_13_keyAndAttributes_})
        d_15_batchGetInput_: software_amazon_cryptography_services_dynamodb_internaldafny_types.BatchGetItemInput
        d_15_batchGetInput_ = software_amazon_cryptography_services_dynamodb_internaldafny_types.BatchGetItemInput_BatchGetItemInput(d_14_batchGetRequestMap_, Wrappers.Option_None())
        TestDDBv2.default__.BatchGetItemTest(d_15_batchGetInput_)

    @staticmethod
    def BasicQueryTest(input):
        d_16_client_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_17_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_17_valueOrError0_ = out0_
        if not(not((d_17_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestDDBv2.dfy(130,19): " + _dafny.string_of(d_17_valueOrError0_))
        d_16_client_ = (d_17_valueOrError0_).Extract()
        d_18_ret_: Wrappers.Result
        out1_: Wrappers.Result
        out1_ = (d_16_client_).Query(input)
        d_18_ret_ = out1_
        if not((d_18_ret_).is_Success):
            raise _dafny.HaltException("test/TestDDBv2.dfy(136,8): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_19_queryOutput_: software_amazon_cryptography_services_dynamodb_internaldafny_types.QueryOutput
        d_19_queryOutput_ = (d_18_ret_).value
        if not(((d_19_queryOutput_).Items).is_Some):
            raise _dafny.HaltException("test/TestDDBv2.dfy(140,8): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_20_queryItem_: _dafny.Seq
        d_20_queryItem_ = ((d_19_queryOutput_).Items).value
        if not((len(d_20_queryItem_)) > (0)):
            raise _dafny.HaltException("test/TestDDBv2.dfy(143,8): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_21_item_: _dafny.Map
        d_21_item_ = (d_20_queryItem_)[0]
        if not(((d_21_item_).keys) == (_dafny.Set({_dafny.Seq("branch-key-id"), _dafny.Seq("version"), _dafny.Seq("create-time"), _dafny.Seq("enc"), _dafny.Seq("hierarchy-version"), _dafny.Seq("status")}))):
            raise _dafny.HaltException("test/TestDDBv2.dfy(148,8): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len((d_21_item_).keys)) == (len((d_21_item_).values))):
            raise _dafny.HaltException("test/TestDDBv2.dfy(150,8): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def BasicGetTest(input):
        d_22_client_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_23_valueOrError0_: Wrappers.Result = None
        out2_: Wrappers.Result
        out2_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_23_valueOrError0_ = out2_
        if not(not((d_23_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestDDBv2.dfy(158,19): " + _dafny.string_of(d_23_valueOrError0_))
        d_22_client_ = (d_23_valueOrError0_).Extract()
        d_24_ret_: Wrappers.Result
        out3_: Wrappers.Result
        out3_ = (d_22_client_).GetItem(input)
        d_24_ret_ = out3_
        if not((d_24_ret_).is_Success):
            raise _dafny.HaltException("test/TestDDBv2.dfy(164,8): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_25_itemOutput_: software_amazon_cryptography_services_dynamodb_internaldafny_types.GetItemOutput
        d_25_itemOutput_ = (d_24_ret_).value
        if not(((d_25_itemOutput_).Item).is_Some):
            raise _dafny.HaltException("test/TestDDBv2.dfy(167,8): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_26_item_: _dafny.Map
        d_26_item_ = ((d_25_itemOutput_).Item).value
        if not(((d_26_item_).keys) == (_dafny.Set({_dafny.Seq("branch-key-id"), _dafny.Seq("version"), _dafny.Seq("create-time"), _dafny.Seq("enc"), _dafny.Seq("hierarchy-version"), _dafny.Seq("status")}))):
            raise _dafny.HaltException("test/TestDDBv2.dfy(170,8): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        if not((len((d_26_item_).keys)) == (len((d_26_item_).values))):
            raise _dafny.HaltException("test/TestDDBv2.dfy(171,8): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def BasicPutTest(input):
        d_27_client_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_28_valueOrError0_: Wrappers.Result = None
        out4_: Wrappers.Result
        out4_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_28_valueOrError0_ = out4_
        if not(not((d_28_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestDDBv2.dfy(178,19): " + _dafny.string_of(d_28_valueOrError0_))
        d_27_client_ = (d_28_valueOrError0_).Extract()
        d_29_ret_: Wrappers.Result
        out5_: Wrappers.Result
        out5_ = (d_27_client_).PutItem(input)
        d_29_ret_ = out5_
        if not((d_29_ret_).is_Success):
            raise _dafny.HaltException("test/TestDDBv2.dfy(184,8): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @staticmethod
    def BatchGetItemTest(input):
        d_30_client_: software_amazon_cryptography_services_dynamodb_internaldafny_types.IDynamoDBClient
        d_31_valueOrError0_: Wrappers.Result = None
        out6_: Wrappers.Result
        out6_ = software_amazon_cryptography_services_dynamodb_internaldafny.default__.DynamoDBClient()
        d_31_valueOrError0_ = out6_
        if not(not((d_31_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestDDBv2.dfy(191,19): " + _dafny.string_of(d_31_valueOrError0_))
        d_30_client_ = (d_31_valueOrError0_).Extract()
        d_32_ret_: Wrappers.Result
        out7_: Wrappers.Result
        out7_ = (d_30_client_).BatchGetItem(input)
        d_32_ret_ = out7_
        if (d_32_ret_).is_Failure:
            _dafny.print(_dafny.string_of(_dafny.Seq("\n\t BatchGetItemTest Failed")))
            _dafny.print(_dafny.string_of(_dafny.Seq("\n\t")))
            _dafny.print(_dafny.string_of(d_32_ret_))
            _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
        if not((d_32_ret_).is_Success):
            raise _dafny.HaltException("test/TestDDBv2.dfy(202,8): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @_dafny.classproperty
    def tableNameTest(instance):
        return _dafny.Seq("TestTable")
    @_dafny.classproperty
    def secIndex(instance):
        return _dafny.Seq("Active-Keys")
