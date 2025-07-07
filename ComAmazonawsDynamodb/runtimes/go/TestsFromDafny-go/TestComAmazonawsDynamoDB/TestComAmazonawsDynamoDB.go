// Package TestComAmazonawsDynamoDB
// Dafny module TestComAmazonawsDynamoDB compiled into Go

package TestComAmazonawsDynamoDB

import (
	os "os"

	m_ComAmazonawsDynamodbTypes "github.com/aws/aws-cryptographic-material-providers-library/releases/go/dynamodb/ComAmazonawsDynamodbTypes"
	m_Com_Amazonaws_Dynamodb "github.com/aws/aws-cryptographic-material-providers-library/releases/go/dynamodb/Com_Amazonaws_Dynamodb"
	m_Actions "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Actions"
	m_Base64 "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Base64"
	m_Base64Lemmas "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Base64Lemmas"
	m_BoundedInts "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/BoundedInts"
	m_DivInternals "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/DivInternals"
	m_DivInternalsNonlinear "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/DivInternalsNonlinear"
	m_DivMod "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/DivMod"
	m_FileIO "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/FileIO"
	m_FloatCompare "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/FloatCompare"
	m_Functions "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Functions"
	m_GeneralInternals "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/GeneralInternals"
	m_GetOpt "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/GetOpt"
	m_HexStrings "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/HexStrings"
	m_Logarithm "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Logarithm"
	m__Math "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Math_"
	m_ModInternals "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/ModInternals"
	m_ModInternalsNonlinear "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/ModInternalsNonlinear"
	m_Mul "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Mul"
	m_MulInternals "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/MulInternals"
	m_MulInternalsNonlinear "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/MulInternalsNonlinear"
	m_Power "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Power"
	m_Relations "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Relations"
	m_Seq "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Seq"
	m_Seq_MergeSort "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Seq_MergeSort"
	m_Sorting "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Sorting"
	m_StandardLibrary "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/StandardLibrary"
	m_StandardLibraryInterop "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/StandardLibraryInterop"
	m_StandardLibrary_MemoryMath "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/StandardLibrary_MemoryMath"
	m_StandardLibrary_Sequence "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/StandardLibrary_Sequence"
	m_StandardLibrary_String "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/StandardLibrary_String"
	m_StandardLibrary_UInt "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/StandardLibrary_UInt"
	m_Streams "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Streams"
	m_UnicodeStrings "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/UnicodeStrings"
	m__Unicode "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Unicode_"
	m_Utf16EncodingForm "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Utf16EncodingForm"
	m_Utf8EncodingForm "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Utf8EncodingForm"
	m_Wrappers "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Wrappers"
	m__System "github.com/dafny-lang/DafnyRuntimeGo/v4/System_"
	_dafny "github.com/dafny-lang/DafnyRuntimeGo/v4/dafny"
)

var _ = os.Args
var _ _dafny.Dummy__
var _ m__System.Dummy__
var _ m_Wrappers.Dummy__
var _ m_BoundedInts.Dummy__
var _ m_StandardLibrary_UInt.Dummy__
var _ m_StandardLibrary_MemoryMath.Dummy__
var _ m_StandardLibrary_Sequence.Dummy__
var _ m_StandardLibrary_String.Dummy__
var _ m_StandardLibrary.Dummy__
var _ m_ComAmazonawsDynamodbTypes.Dummy__
var _ m_Relations.Dummy__
var _ m_Seq_MergeSort.Dummy__
var _ m__Math.Dummy__
var _ m_Seq.Dummy__
var _ m__Unicode.Dummy__
var _ m_Functions.Dummy__
var _ m_Utf8EncodingForm.Dummy__
var _ m_Utf16EncodingForm.Dummy__
var _ m_UnicodeStrings.Dummy__
var _ m_FileIO.Dummy__
var _ m_GeneralInternals.Dummy__
var _ m_MulInternalsNonlinear.Dummy__
var _ m_MulInternals.Dummy__
var _ m_Mul.Dummy__
var _ m_ModInternalsNonlinear.Dummy__
var _ m_DivInternalsNonlinear.Dummy__
var _ m_ModInternals.Dummy__
var _ m_DivInternals.Dummy__
var _ m_DivMod.Dummy__
var _ m_Power.Dummy__
var _ m_Logarithm.Dummy__
var _ m_StandardLibraryInterop.Dummy__
var _ m_Streams.Dummy__
var _ m_Sorting.Dummy__
var _ m_HexStrings.Dummy__
var _ m_GetOpt.Dummy__
var _ m_FloatCompare.Dummy__
var _ m_Base64.Dummy__
var _ m_Base64Lemmas.Dummy__
var _ m_Actions.Dummy__
var _ m_Com_Amazonaws_Dynamodb.Dummy__

type Dummy__ struct{}

// Definition of class Default__
type Default__ struct {
	dummy byte
}

func New_Default___() *Default__ {
	_this := Default__{}

	return &_this
}

type CompanionStruct_Default___ struct {
}

var Companion_Default___ = CompanionStruct_Default___{}

func (_this *Default__) Equals(other *Default__) bool {
	return _this == other
}

func (_this *Default__) EqualsGeneric(x interface{}) bool {
	other, ok := x.(*Default__)
	return ok && _this.Equals(other)
}

func (*Default__) String() string {
	return "TestComAmazonawsDynamoDB.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) BasicPutGetQuery() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_Com_Amazonaws_Dynamodb.Companion_Default___.DynamoDBClient()
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("test/TestComAmazonawsDynamodb.dfy(20,18): " + (_0_valueOrError0).String())
	}
	var _1_client m_ComAmazonawsDynamodbTypes.IDynamoDBClient
	_ = _1_client
	_1_client = m_ComAmazonawsDynamodbTypes.Companion_IDynamoDBClient_.CastTo_((_0_valueOrError0).Extract())
	var _2_item _dafny.Map
	_ = _2_item
	_2_item = _dafny.NewMapBuilder().ToMap().UpdateUnsafe(_dafny.SeqOfString("branch-key-id"), m_ComAmazonawsDynamodbTypes.Companion_AttributeValue_.Create_S_(_dafny.SeqOfString("ddb-client-test"))).UpdateUnsafe(_dafny.SeqOfString("type"), m_ComAmazonawsDynamodbTypes.Companion_AttributeValue_.Create_S_(_dafny.SeqOfString("ddb-client-test"))).UpdateUnsafe(_dafny.SeqOfString("status"), m_ComAmazonawsDynamodbTypes.Companion_AttributeValue_.Create_S_(_dafny.SeqOfString("ACTIVE")))
	var _3_putInput m_ComAmazonawsDynamodbTypes.PutItemInput
	_ = _3_putInput
	_3_putInput = m_ComAmazonawsDynamodbTypes.Companion_PutItemInput_.Create_PutItemInput_(Companion_Default___.TableNameTest(), _2_item, m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_())
	var _4_putRet m_Wrappers.Result
	_ = _4_putRet
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = (_1_client).PutItem(_3_putInput)
	_4_putRet = _out1
	if (_4_putRet).Is_Failure() {
		_dafny.Print((_4_putRet).Dtor_error().(m_ComAmazonawsDynamodbTypes.Error))
	}
	if !((_4_putRet).Is_Success()) {
		panic("test/TestComAmazonawsDynamodb.dfy(47,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _5_Key2Get _dafny.Map
	_ = _5_Key2Get
	_5_Key2Get = _dafny.NewMapBuilder().ToMap().UpdateUnsafe(_dafny.SeqOfString("branch-key-id"), m_ComAmazonawsDynamodbTypes.Companion_AttributeValue_.Create_S_(_dafny.SeqOfString("ddb-client-test"))).UpdateUnsafe(_dafny.SeqOfString("type"), m_ComAmazonawsDynamodbTypes.Companion_AttributeValue_.Create_S_(_dafny.SeqOfString("ddb-client-test")))
	var _6_getInput m_ComAmazonawsDynamodbTypes.GetItemInput
	_ = _6_getInput
	_6_getInput = m_ComAmazonawsDynamodbTypes.Companion_GetItemInput_.Create_GetItemInput_(Companion_Default___.TableNameTest(), _5_Key2Get, m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_())
	var _7_getRet m_Wrappers.Result
	_ = _7_getRet
	var _out2 m_Wrappers.Result
	_ = _out2
	_out2 = (_1_client).GetItem(_6_getInput)
	_7_getRet = _out2
	if (_7_getRet).Is_Failure() {
		_dafny.Print((_7_getRet).Dtor_error().(m_ComAmazonawsDynamodbTypes.Error))
	}
	if !((_7_getRet).Is_Success()) {
		panic("test/TestComAmazonawsDynamodb.dfy(69,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _8_itemOutput m_ComAmazonawsDynamodbTypes.GetItemOutput
	_ = _8_itemOutput
	_8_itemOutput = (_7_getRet).Dtor_value().(m_ComAmazonawsDynamodbTypes.GetItemOutput)
	if !(((_8_itemOutput).Dtor_Item()).Is_Some()) {
		panic("test/TestComAmazonawsDynamodb.dfy(72,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _9_gotItem _dafny.Map
	_ = _9_gotItem
	_9_gotItem = ((_8_itemOutput).Dtor_Item()).Dtor_value().(_dafny.Map)
	if !((_9_gotItem).Equals(_2_item)) {
		panic("test/TestComAmazonawsDynamodb.dfy(74,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _10_attributeNameMap _dafny.Map
	_ = _10_attributeNameMap
	_10_attributeNameMap = _dafny.NewMapBuilder().ToMap().UpdateUnsafe(_dafny.SeqOfString("#status"), _dafny.SeqOfString("status")).UpdateUnsafe(_dafny.SeqOfString("#branchKeyId"), _dafny.SeqOfString("branch-key-id"))
	var _11_attributeValueMap _dafny.Map
	_ = _11_attributeValueMap
	_11_attributeValueMap = _dafny.NewMapBuilder().ToMap().UpdateUnsafe(_dafny.SeqOfString(":status"), m_ComAmazonawsDynamodbTypes.Companion_AttributeValue_.Create_S_(_dafny.SeqOfString("ACTIVE"))).UpdateUnsafe(_dafny.SeqOfString(":branchKeyId"), m_ComAmazonawsDynamodbTypes.Companion_AttributeValue_.Create_S_(_dafny.SeqOfString("ddb-client-test")))
	var _12_queryInput m_ComAmazonawsDynamodbTypes.QueryInput
	_ = _12_queryInput
	_12_queryInput = m_ComAmazonawsDynamodbTypes.Companion_QueryInput_.Create_QueryInput_(Companion_Default___.TableNameTest(), m_Wrappers.Companion_Option_.Create_Some_(Companion_Default___.SecIndex()), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_None_(), m_Wrappers.Companion_Option_.Create_Some_(_dafny.SeqOfString("#status = :status and #branchKeyId = :branchKeyId")), m_Wrappers.Companion_Option_.Create_Some_(_10_attributeNameMap), m_Wrappers.Companion_Option_.Create_Some_(_11_attributeValueMap))
	var _13_queryRet m_Wrappers.Result
	_ = _13_queryRet
	var _out3 m_Wrappers.Result
	_ = _out3
	_out3 = (_1_client).Query(_12_queryInput)
	_13_queryRet = _out3
	if (_13_queryRet).Is_Failure() {
		_dafny.Print((_13_queryRet).Dtor_error().(m_ComAmazonawsDynamodbTypes.Error))
	}
	if !((_13_queryRet).Is_Success()) {
		panic("test/TestComAmazonawsDynamodb.dfy(112,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _14_queryOutput m_ComAmazonawsDynamodbTypes.QueryOutput
	_ = _14_queryOutput
	_14_queryOutput = (_13_queryRet).Dtor_value().(m_ComAmazonawsDynamodbTypes.QueryOutput)
	if !(((_14_queryOutput).Dtor_Items()).Is_Some()) {
		panic("test/TestComAmazonawsDynamodb.dfy(115,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _15_queryItem _dafny.Sequence
	_ = _15_queryItem
	_15_queryItem = ((_14_queryOutput).Dtor_Items()).Dtor_value().(_dafny.Sequence)
	if !((_dafny.IntOfUint32((_15_queryItem).Cardinality())).Cmp(_dafny.One) == 0) {
		panic("test/TestComAmazonawsDynamodb.dfy(117,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _16_queriedItem _dafny.Map
	_ = _16_queriedItem
	_16_queriedItem = (_15_queryItem).Select(0).(_dafny.Map)
	if !((_2_item).Equals(_16_queriedItem)) {
		panic("test/TestComAmazonawsDynamodb.dfy(119,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TableNameTest() _dafny.Sequence {
	return _dafny.SeqOfString("KeyStoreTestTable")
}
func (_static *CompanionStruct_Default___) SecIndex() _dafny.Sequence {
	return _dafny.SeqOfString("Active-Keys")
}

// End of class Default__
