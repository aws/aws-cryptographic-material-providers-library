import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_ as module_
import _dafny as _dafny
import System_ as System_
import standard_library.internaldafny.generated.Wrappers as Wrappers
import standard_library.internaldafny.generated.BoundedInts as BoundedInts
import standard_library.internaldafny.generated.StandardLibrary_UInt as StandardLibrary_UInt
import standard_library.internaldafny.generated.StandardLibrary_String as StandardLibrary_String
import standard_library.internaldafny.generated.StandardLibrary as StandardLibrary
import standard_library.internaldafny.generated.UTF8 as UTF8
import com_amazonaws_dynamodb.internaldafny.generated.ComAmazonawsDynamodbTypes as ComAmazonawsDynamodbTypes
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
import com_amazonaws_dynamodb.internaldafny.generated.Com_Amazonaws_Dynamodb as Com_Amazonaws_Dynamodb

# Module: TestComAmazonawsDynamoDB

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def BasicPutGetQuery():
        d_0_client_: ComAmazonawsDynamodbTypes.IDynamoDBClient
        d_1_valueOrError0_: Wrappers.Result = None
        out0_: Wrappers.Result
        out0_ = Com_Amazonaws_Dynamodb.default__.DynamoDBClient()
        d_1_valueOrError0_ = out0_
        if not(not((d_1_valueOrError0_).IsFailure())):
            raise _dafny.HaltException("test/TestComAmazonawsDynamodb.dfy(20,18): " + _dafny.string_of(d_1_valueOrError0_))
        d_0_client_ = (d_1_valueOrError0_).Extract()
        d_2_item_: _dafny.Map
        d_2_item_ = _dafny.Map({_dafny.Seq("branch-key-id"): ComAmazonawsDynamodbTypes.AttributeValue_S(_dafny.Seq("ddb-client-test")), _dafny.Seq("type"): ComAmazonawsDynamodbTypes.AttributeValue_S(_dafny.Seq("ddb-client-test")), _dafny.Seq("status"): ComAmazonawsDynamodbTypes.AttributeValue_S(_dafny.Seq("ACTIVE"))})
        d_3_putInput_: ComAmazonawsDynamodbTypes.PutItemInput
        d_3_putInput_ = ComAmazonawsDynamodbTypes.PutItemInput_PutItemInput(default__.tableNameTest, d_2_item_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_4_putRet_: Wrappers.Result
        out1_: Wrappers.Result
        out1_ = (d_0_client_).PutItem(d_3_putInput_)
        d_4_putRet_ = out1_
        if (d_4_putRet_).is_Failure:
            _dafny.print(_dafny.string_of((d_4_putRet_).error))
        if not((d_4_putRet_).is_Success):
            raise _dafny.HaltException("test/TestComAmazonawsDynamodb.dfy(47,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_5_Key2Get_: _dafny.Map
        d_5_Key2Get_ = _dafny.Map({_dafny.Seq("branch-key-id"): ComAmazonawsDynamodbTypes.AttributeValue_S(_dafny.Seq("ddb-client-test")), _dafny.Seq("type"): ComAmazonawsDynamodbTypes.AttributeValue_S(_dafny.Seq("ddb-client-test"))})
        d_6_getInput_: ComAmazonawsDynamodbTypes.GetItemInput
        d_6_getInput_ = ComAmazonawsDynamodbTypes.GetItemInput_GetItemInput(default__.tableNameTest, d_5_Key2Get_, Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None())
        d_7_getRet_: Wrappers.Result
        out2_: Wrappers.Result
        out2_ = (d_0_client_).GetItem(d_6_getInput_)
        d_7_getRet_ = out2_
        if (d_7_getRet_).is_Failure:
            _dafny.print(_dafny.string_of((d_7_getRet_).error))
        if not((d_7_getRet_).is_Success):
            raise _dafny.HaltException("test/TestComAmazonawsDynamodb.dfy(69,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_8_itemOutput_: ComAmazonawsDynamodbTypes.GetItemOutput
        d_8_itemOutput_ = (d_7_getRet_).value
        if not(((d_8_itemOutput_).Item).is_Some):
            raise _dafny.HaltException("test/TestComAmazonawsDynamodb.dfy(72,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_9_gotItem_: _dafny.Map
        d_9_gotItem_ = ((d_8_itemOutput_).Item).value
        if not((d_9_gotItem_) == (d_2_item_)):
            raise _dafny.HaltException("test/TestComAmazonawsDynamodb.dfy(74,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_10_attributeNameMap_: _dafny.Map
        d_10_attributeNameMap_ = _dafny.Map({_dafny.Seq("#status"): _dafny.Seq("status"), _dafny.Seq("#branchKeyId"): _dafny.Seq("branch-key-id")})
        d_11_attributeValueMap_: _dafny.Map
        d_11_attributeValueMap_ = _dafny.Map({_dafny.Seq(":status"): ComAmazonawsDynamodbTypes.AttributeValue_S(_dafny.Seq("ACTIVE")), _dafny.Seq(":branchKeyId"): ComAmazonawsDynamodbTypes.AttributeValue_S(_dafny.Seq("ddb-client-test"))})
        d_12_queryInput_: ComAmazonawsDynamodbTypes.QueryInput
        d_12_queryInput_ = ComAmazonawsDynamodbTypes.QueryInput_QueryInput(default__.tableNameTest, Wrappers.Option_Some(default__.secIndex), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(_dafny.Seq("#status = :status and #branchKeyId = :branchKeyId")), Wrappers.Option_Some(d_10_attributeNameMap_), Wrappers.Option_Some(d_11_attributeValueMap_))
        d_13_queryRet_: Wrappers.Result
        out3_: Wrappers.Result
        out3_ = (d_0_client_).Query(d_12_queryInput_)
        d_13_queryRet_ = out3_
        if (d_13_queryRet_).is_Failure:
            _dafny.print(_dafny.string_of((d_13_queryRet_).error))
        if not((d_13_queryRet_).is_Success):
            raise _dafny.HaltException("test/TestComAmazonawsDynamodb.dfy(112,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_14_queryOutput_: ComAmazonawsDynamodbTypes.QueryOutput
        d_14_queryOutput_ = (d_13_queryRet_).value
        if not(((d_14_queryOutput_).Items).is_Some):
            raise _dafny.HaltException("test/TestComAmazonawsDynamodb.dfy(115,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_15_queryItem_: _dafny.Seq
        d_15_queryItem_ = ((d_14_queryOutput_).Items).value
        if not((len(d_15_queryItem_)) == (1)):
            raise _dafny.HaltException("test/TestComAmazonawsDynamodb.dfy(117,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))
        d_16_queriedItem_: _dafny.Map
        d_16_queriedItem_ = (d_15_queryItem_)[0]
        if not((d_2_item_) == (d_16_queriedItem_)):
            raise _dafny.HaltException("test/TestComAmazonawsDynamodb.dfy(119,4): " + _dafny.string_of(_dafny.Seq("expectation violation")))

    @_dafny.classproperty
    def tableNameTest(instance):
        return _dafny.Seq("KeyStoreTestTable")
    @_dafny.classproperty
    def secIndex(instance):
        return _dafny.Seq("Active-Keys")
