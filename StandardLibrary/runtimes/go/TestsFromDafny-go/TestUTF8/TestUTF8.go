// Package TestUTF8
// Dafny module TestUTF8 compiled into Go

package TestUTF8

import (
	os "os"

	m__System "github.com/dafny-lang/DafnyRuntimeGo/v4/System_"
	_dafny "github.com/dafny-lang/DafnyRuntimeGo/v4/dafny"
	m_Actions "github.com/dafny-lang/DafnyStandardLibGo/Actions"
	m_Base64 "github.com/dafny-lang/DafnyStandardLibGo/Base64"
	m_Base64Lemmas "github.com/dafny-lang/DafnyStandardLibGo/Base64Lemmas"
	m_BoundedInts "github.com/dafny-lang/DafnyStandardLibGo/BoundedInts"
	m_DivInternals "github.com/dafny-lang/DafnyStandardLibGo/DivInternals"
	m_DivInternalsNonlinear "github.com/dafny-lang/DafnyStandardLibGo/DivInternalsNonlinear"
	m_DivMod "github.com/dafny-lang/DafnyStandardLibGo/DivMod"
	m_FileIO "github.com/dafny-lang/DafnyStandardLibGo/FileIO"
	m_FloatCompare "github.com/dafny-lang/DafnyStandardLibGo/FloatCompare"
	m_Functions "github.com/dafny-lang/DafnyStandardLibGo/Functions"
	m_GeneralInternals "github.com/dafny-lang/DafnyStandardLibGo/GeneralInternals"
	m_GetOpt "github.com/dafny-lang/DafnyStandardLibGo/GetOpt"
	m_HexStrings "github.com/dafny-lang/DafnyStandardLibGo/HexStrings"
	m_Logarithm "github.com/dafny-lang/DafnyStandardLibGo/Logarithm"
	m__Math "github.com/dafny-lang/DafnyStandardLibGo/Math_"
	m_ModInternals "github.com/dafny-lang/DafnyStandardLibGo/ModInternals"
	m_ModInternalsNonlinear "github.com/dafny-lang/DafnyStandardLibGo/ModInternalsNonlinear"
	m_Mul "github.com/dafny-lang/DafnyStandardLibGo/Mul"
	m_MulInternals "github.com/dafny-lang/DafnyStandardLibGo/MulInternals"
	m_MulInternalsNonlinear "github.com/dafny-lang/DafnyStandardLibGo/MulInternalsNonlinear"
	m_Power "github.com/dafny-lang/DafnyStandardLibGo/Power"
	m_Relations "github.com/dafny-lang/DafnyStandardLibGo/Relations"
	m_Seq "github.com/dafny-lang/DafnyStandardLibGo/Seq"
	m_Seq_MergeSort "github.com/dafny-lang/DafnyStandardLibGo/Seq_MergeSort"
	m_Sorting "github.com/dafny-lang/DafnyStandardLibGo/Sorting"
	m_StandardLibrary "github.com/dafny-lang/DafnyStandardLibGo/StandardLibrary"
	m_StandardLibraryInterop "github.com/dafny-lang/DafnyStandardLibGo/StandardLibraryInterop"
	m_StandardLibrary_String "github.com/dafny-lang/DafnyStandardLibGo/StandardLibrary_String"
	m_StandardLibrary_UInt "github.com/dafny-lang/DafnyStandardLibGo/StandardLibrary_UInt"
	m_Streams "github.com/dafny-lang/DafnyStandardLibGo/Streams"
	m_UTF8 "github.com/dafny-lang/DafnyStandardLibGo/UTF8"
	m_UnicodeStrings "github.com/dafny-lang/DafnyStandardLibGo/UnicodeStrings"
	m__Unicode "github.com/dafny-lang/DafnyStandardLibGo/Unicode_"
	m_Utf16EncodingForm "github.com/dafny-lang/DafnyStandardLibGo/Utf16EncodingForm"
	m_Utf8EncodingForm "github.com/dafny-lang/DafnyStandardLibGo/Utf8EncodingForm"
	m_Wrappers "github.com/dafny-lang/DafnyStandardLibGo/Wrappers"
	m_GetOptTest "github.com/dafny-lang/DafnyStandardLibGo/test/GetOptTest"
	m_Sets "github.com/dafny-lang/DafnyStandardLibGo/test/Sets"
	m_TestComputeSetToOrderedSequenceCharLess "github.com/dafny-lang/DafnyStandardLibGo/test/TestComputeSetToOrderedSequenceCharLess"
	m_TestHexStrings "github.com/dafny-lang/DafnyStandardLibGo/test/TestHexStrings"
	m_TestTime "github.com/dafny-lang/DafnyStandardLibGo/test/TestTime"
)

var _ = os.Args
var _ _dafny.Dummy__
var _ m__System.Dummy__
var _ m_Wrappers.Dummy__
var _ m_Relations.Dummy__
var _ m_Seq_MergeSort.Dummy__
var _ m__Math.Dummy__
var _ m_Seq.Dummy__
var _ m_BoundedInts.Dummy__
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
var _ m_StandardLibrary_UInt.Dummy__
var _ m_StandardLibrary_String.Dummy__
var _ m_StandardLibrary.Dummy__
var _ m_Streams.Dummy__
var _ m_Sorting.Dummy__
var _ m_HexStrings.Dummy__
var _ m_GetOpt.Dummy__
var _ m_FloatCompare.Dummy__
var _ m_Base64.Dummy__
var _ m_Base64Lemmas.Dummy__
var _ m_Actions.Dummy__
var _ m_GetOptTest.Dummy__
var _ m_TestComputeSetToOrderedSequenceCharLess.Dummy__
var _ m_Sets.Dummy__
var _ m_TestHexStrings.Dummy__
var _ m_TestTime.Dummy__

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
	return "TestUTF8.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) TestEncodeHappyCase() {
	var _0_unicodeString _dafny.Sequence
	_ = _0_unicodeString
	_0_unicodeString = _dafny.SeqOfChars(97, 98, 99, 774, 509, 946)
	var _1_expectedBytes _dafny.Sequence
	_ = _1_expectedBytes
	_1_expectedBytes = _dafny.SeqOf(uint8(97), uint8(98), uint8(99), uint8(204), uint8(134), uint8(199), uint8(189), uint8(206), uint8(178))
	var _2_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _2_valueOrError0
	_2_valueOrError0 = m_UTF8.Encode(_0_unicodeString)
	if !(!((_2_valueOrError0).IsFailure())) {
		panic("test/UTF8.dfy(14,19): " + (_2_valueOrError0).String())
	}
	var _3_encoded _dafny.Sequence
	_ = _3_encoded
	_3_encoded = (_2_valueOrError0).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_1_expectedBytes, _3_encoded)) {
		panic("test/UTF8.dfy(15,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestEncodeInvalidUnicode() {
	var _0_invalidUnicode _dafny.Sequence
	_ = _0_invalidUnicode
	_0_invalidUnicode = _dafny.SeqOfChars(97, 98, 99, 55296)
	var _1_encoded m_Wrappers.Result
	_ = _1_encoded
	_1_encoded = m_UTF8.Encode(_0_invalidUnicode)
	if !((_1_encoded).Is_Failure()) {
		panic("test/UTF8.dfy(22,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestDecodeHappyCase() {
	var _0_unicodeBytes _dafny.Sequence
	_ = _0_unicodeBytes
	_0_unicodeBytes = _dafny.SeqOf(uint8(97), uint8(98), uint8(99), uint8(204), uint8(134), uint8(199), uint8(189), uint8(206), uint8(178))
	var _1_expectedString _dafny.Sequence
	_ = _1_expectedString
	_1_expectedString = _dafny.SeqOfChars(97, 98, 99, 774, 509, 946)
	var _2_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _2_valueOrError0
	_2_valueOrError0 = m_UTF8.Decode(_0_unicodeBytes)
	if !(!((_2_valueOrError0).IsFailure())) {
		panic("test/UTF8.dfy(32,19): " + (_2_valueOrError0).String())
	}
	var _3_decoded _dafny.Sequence
	_ = _3_decoded
	_3_decoded = (_2_valueOrError0).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_1_expectedString, _3_decoded)) {
		panic("test/UTF8.dfy(33,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestDecodeInvalidUnicode() {
	var _0_invalidUnicode _dafny.Sequence
	_ = _0_invalidUnicode
	_0_invalidUnicode = _dafny.SeqOf(uint8(97), uint8(98), uint8(99), uint8(237), uint8(160), uint8(128))
	if !(!(m_UTF8.Companion_Default___.ValidUTF8Seq(_0_invalidUnicode))) {
		panic("test/UTF8.dfy(39,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !((m_UTF8.Decode(_0_invalidUnicode)).Is_Failure()) {
		panic("test/UTF8.dfy(40,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) Test1Byte() {
	var _0_decoded _dafny.Sequence
	_ = _0_decoded
	_0_decoded = _dafny.SeqOfChars(0)
	var _1_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _1_valueOrError0
	_1_valueOrError0 = m_UTF8.Encode(_0_decoded)
	if !(!((_1_valueOrError0).IsFailure())) {
		panic("test/UTF8.dfy(46,19): " + (_1_valueOrError0).String())
	}
	var _2_encoded _dafny.Sequence
	_ = _2_encoded
	_2_encoded = (_1_valueOrError0).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_dafny.SeqOf(uint8(0)), _2_encoded)) {
		panic("test/UTF8.dfy(47,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(m_UTF8.Companion_Default___.Uses1Byte(_2_encoded)) {
		panic("test/UTF8.dfy(48,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _3_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _3_valueOrError1
	_3_valueOrError1 = m_UTF8.Decode(_2_encoded)
	if !(!((_3_valueOrError1).IsFailure())) {
		panic("test/UTF8.dfy(49,21): " + (_3_valueOrError1).String())
	}
	var _4_redecoded _dafny.Sequence
	_ = _4_redecoded
	_4_redecoded = (_3_valueOrError1).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_0_decoded, _4_redecoded)) {
		panic("test/UTF8.dfy(50,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	_0_decoded = _dafny.SeqOfChars(32)
	var _5_valueOrError2 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _5_valueOrError2
	_5_valueOrError2 = m_UTF8.Encode(_0_decoded)
	if !(!((_5_valueOrError2).IsFailure())) {
		panic("test/UTF8.dfy(54,15): " + (_5_valueOrError2).String())
	}
	_2_encoded = (_5_valueOrError2).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_dafny.SeqOf(uint8(32)), _2_encoded)) {
		panic("test/UTF8.dfy(55,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(m_UTF8.Companion_Default___.Uses1Byte(_2_encoded)) {
		panic("test/UTF8.dfy(56,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _6_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _6_valueOrError3
	_6_valueOrError3 = m_UTF8.Decode(_2_encoded)
	if !(!((_6_valueOrError3).IsFailure())) {
		panic("test/UTF8.dfy(57,17): " + (_6_valueOrError3).String())
	}
	_4_redecoded = (_6_valueOrError3).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_0_decoded, _4_redecoded)) {
		panic("test/UTF8.dfy(58,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	_0_decoded = _dafny.SeqOfString("$")
	var _7_valueOrError4 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _7_valueOrError4
	_7_valueOrError4 = m_UTF8.Encode(_0_decoded)
	if !(!((_7_valueOrError4).IsFailure())) {
		panic("test/UTF8.dfy(61,15): " + (_7_valueOrError4).String())
	}
	_2_encoded = (_7_valueOrError4).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_dafny.SeqOf(uint8(36)), _2_encoded)) {
		panic("test/UTF8.dfy(62,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(m_UTF8.Companion_Default___.Uses1Byte(_2_encoded)) {
		panic("test/UTF8.dfy(63,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _8_valueOrError5 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _8_valueOrError5
	_8_valueOrError5 = m_UTF8.Decode(_2_encoded)
	if !(!((_8_valueOrError5).IsFailure())) {
		panic("test/UTF8.dfy(64,17): " + (_8_valueOrError5).String())
	}
	_4_redecoded = (_8_valueOrError5).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_0_decoded, _4_redecoded)) {
		panic("test/UTF8.dfy(65,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	_0_decoded = _dafny.SeqOfString("0")
	var _9_valueOrError6 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _9_valueOrError6
	_9_valueOrError6 = m_UTF8.Encode(_0_decoded)
	if !(!((_9_valueOrError6).IsFailure())) {
		panic("test/UTF8.dfy(68,15): " + (_9_valueOrError6).String())
	}
	_2_encoded = (_9_valueOrError6).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_dafny.SeqOf(uint8(48)), _2_encoded)) {
		panic("test/UTF8.dfy(69,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(m_UTF8.Companion_Default___.Uses1Byte(_2_encoded)) {
		panic("test/UTF8.dfy(70,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _10_valueOrError7 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _10_valueOrError7
	_10_valueOrError7 = m_UTF8.Decode(_2_encoded)
	if !(!((_10_valueOrError7).IsFailure())) {
		panic("test/UTF8.dfy(71,17): " + (_10_valueOrError7).String())
	}
	_4_redecoded = (_10_valueOrError7).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_0_decoded, _4_redecoded)) {
		panic("test/UTF8.dfy(72,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	_0_decoded = _dafny.SeqOfString("A")
	var _11_valueOrError8 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _11_valueOrError8
	_11_valueOrError8 = m_UTF8.Encode(_0_decoded)
	if !(!((_11_valueOrError8).IsFailure())) {
		panic("test/UTF8.dfy(75,15): " + (_11_valueOrError8).String())
	}
	_2_encoded = (_11_valueOrError8).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_dafny.SeqOf(uint8(65)), _2_encoded)) {
		panic("test/UTF8.dfy(76,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(m_UTF8.Companion_Default___.Uses1Byte(_2_encoded)) {
		panic("test/UTF8.dfy(77,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _12_valueOrError9 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _12_valueOrError9
	_12_valueOrError9 = m_UTF8.Decode(_2_encoded)
	if !(!((_12_valueOrError9).IsFailure())) {
		panic("test/UTF8.dfy(78,17): " + (_12_valueOrError9).String())
	}
	_4_redecoded = (_12_valueOrError9).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_0_decoded, _4_redecoded)) {
		panic("test/UTF8.dfy(79,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	_0_decoded = _dafny.SeqOfString("a")
	var _13_valueOrError10 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _13_valueOrError10
	_13_valueOrError10 = m_UTF8.Encode(_0_decoded)
	if !(!((_13_valueOrError10).IsFailure())) {
		panic("test/UTF8.dfy(82,15): " + (_13_valueOrError10).String())
	}
	_2_encoded = (_13_valueOrError10).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_dafny.SeqOf(uint8(97)), _2_encoded)) {
		panic("test/UTF8.dfy(83,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(m_UTF8.Companion_Default___.Uses1Byte(_2_encoded)) {
		panic("test/UTF8.dfy(84,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _14_valueOrError11 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _14_valueOrError11
	_14_valueOrError11 = m_UTF8.Decode(_2_encoded)
	if !(!((_14_valueOrError11).IsFailure())) {
		panic("test/UTF8.dfy(85,17): " + (_14_valueOrError11).String())
	}
	_4_redecoded = (_14_valueOrError11).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_0_decoded, _4_redecoded)) {
		panic("test/UTF8.dfy(86,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) Test2Bytes() {
	var _0_decoded _dafny.Sequence
	_ = _0_decoded
	_0_decoded = _dafny.SeqOfChars(163)
	var _1_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _1_valueOrError0
	_1_valueOrError0 = m_UTF8.Encode(_0_decoded)
	if !(!((_1_valueOrError0).IsFailure())) {
		panic("test/UTF8.dfy(92,19): " + (_1_valueOrError0).String())
	}
	var _2_encoded _dafny.Sequence
	_ = _2_encoded
	_2_encoded = (_1_valueOrError0).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_dafny.SeqOf(uint8(194), uint8(163)), _2_encoded)) {
		panic("test/UTF8.dfy(93,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(m_UTF8.Companion_Default___.Uses2Bytes(_2_encoded)) {
		panic("test/UTF8.dfy(94,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _3_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _3_valueOrError1
	_3_valueOrError1 = m_UTF8.Decode(_2_encoded)
	if !(!((_3_valueOrError1).IsFailure())) {
		panic("test/UTF8.dfy(95,21): " + (_3_valueOrError1).String())
	}
	var _4_redecoded _dafny.Sequence
	_ = _4_redecoded
	_4_redecoded = (_3_valueOrError1).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_0_decoded, _4_redecoded)) {
		panic("test/UTF8.dfy(96,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	_0_decoded = _dafny.SeqOfChars(169)
	var _5_valueOrError2 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _5_valueOrError2
	_5_valueOrError2 = m_UTF8.Encode(_0_decoded)
	if !(!((_5_valueOrError2).IsFailure())) {
		panic("test/UTF8.dfy(100,15): " + (_5_valueOrError2).String())
	}
	_2_encoded = (_5_valueOrError2).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_dafny.SeqOf(uint8(194), uint8(169)), _2_encoded)) {
		panic("test/UTF8.dfy(101,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(m_UTF8.Companion_Default___.Uses2Bytes(_2_encoded)) {
		panic("test/UTF8.dfy(102,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _6_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _6_valueOrError3
	_6_valueOrError3 = m_UTF8.Decode(_2_encoded)
	if !(!((_6_valueOrError3).IsFailure())) {
		panic("test/UTF8.dfy(103,17): " + (_6_valueOrError3).String())
	}
	_4_redecoded = (_6_valueOrError3).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_0_decoded, _4_redecoded)) {
		panic("test/UTF8.dfy(104,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	_0_decoded = _dafny.SeqOfChars(174)
	var _7_valueOrError4 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _7_valueOrError4
	_7_valueOrError4 = m_UTF8.Encode(_0_decoded)
	if !(!((_7_valueOrError4).IsFailure())) {
		panic("test/UTF8.dfy(108,15): " + (_7_valueOrError4).String())
	}
	_2_encoded = (_7_valueOrError4).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_dafny.SeqOf(uint8(194), uint8(174)), _2_encoded)) {
		panic("test/UTF8.dfy(109,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(m_UTF8.Companion_Default___.Uses2Bytes(_2_encoded)) {
		panic("test/UTF8.dfy(110,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _8_valueOrError5 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _8_valueOrError5
	_8_valueOrError5 = m_UTF8.Decode(_2_encoded)
	if !(!((_8_valueOrError5).IsFailure())) {
		panic("test/UTF8.dfy(111,17): " + (_8_valueOrError5).String())
	}
	_4_redecoded = (_8_valueOrError5).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_0_decoded, _4_redecoded)) {
		panic("test/UTF8.dfy(112,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	_0_decoded = _dafny.SeqOfChars(960)
	var _9_valueOrError6 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _9_valueOrError6
	_9_valueOrError6 = m_UTF8.Encode(_0_decoded)
	if !(!((_9_valueOrError6).IsFailure())) {
		panic("test/UTF8.dfy(116,15): " + (_9_valueOrError6).String())
	}
	_2_encoded = (_9_valueOrError6).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_dafny.SeqOf(uint8(207), uint8(128)), _2_encoded)) {
		panic("test/UTF8.dfy(117,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(m_UTF8.Companion_Default___.Uses2Bytes(_2_encoded)) {
		panic("test/UTF8.dfy(118,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _10_valueOrError7 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _10_valueOrError7
	_10_valueOrError7 = m_UTF8.Decode(_2_encoded)
	if !(!((_10_valueOrError7).IsFailure())) {
		panic("test/UTF8.dfy(119,17): " + (_10_valueOrError7).String())
	}
	_4_redecoded = (_10_valueOrError7).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_0_decoded, _4_redecoded)) {
		panic("test/UTF8.dfy(120,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) Test3Bytes() {
	var _0_decoded _dafny.Sequence
	_ = _0_decoded
	_0_decoded = _dafny.SeqOfChars(9094)
	var _1_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _1_valueOrError0
	_1_valueOrError0 = m_UTF8.Encode(_0_decoded)
	if !(!((_1_valueOrError0).IsFailure())) {
		panic("test/UTF8.dfy(126,19): " + (_1_valueOrError0).String())
	}
	var _2_encoded _dafny.Sequence
	_ = _2_encoded
	_2_encoded = (_1_valueOrError0).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_dafny.SeqOf(uint8(226), uint8(142), uint8(134)), _2_encoded)) {
		panic("test/UTF8.dfy(127,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(m_UTF8.Companion_Default___.Uses3Bytes(_2_encoded)) {
		panic("test/UTF8.dfy(128,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _3_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _3_valueOrError1
	_3_valueOrError1 = m_UTF8.Decode(_2_encoded)
	if !(!((_3_valueOrError1).IsFailure())) {
		panic("test/UTF8.dfy(129,21): " + (_3_valueOrError1).String())
	}
	var _4_redecoded _dafny.Sequence
	_ = _4_redecoded
	_4_redecoded = (_3_valueOrError1).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_0_decoded, _4_redecoded)) {
		panic("test/UTF8.dfy(130,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	_0_decoded = _dafny.SeqOfChars(9095)
	var _5_valueOrError2 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _5_valueOrError2
	_5_valueOrError2 = m_UTF8.Encode(_0_decoded)
	if !(!((_5_valueOrError2).IsFailure())) {
		panic("test/UTF8.dfy(134,15): " + (_5_valueOrError2).String())
	}
	_2_encoded = (_5_valueOrError2).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_dafny.SeqOf(uint8(226), uint8(142), uint8(135)), _2_encoded)) {
		panic("test/UTF8.dfy(135,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(m_UTF8.Companion_Default___.Uses3Bytes(_2_encoded)) {
		panic("test/UTF8.dfy(136,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _6_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _6_valueOrError3
	_6_valueOrError3 = m_UTF8.Decode(_2_encoded)
	if !(!((_6_valueOrError3).IsFailure())) {
		panic("test/UTF8.dfy(137,17): " + (_6_valueOrError3).String())
	}
	_4_redecoded = (_6_valueOrError3).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_0_decoded, _4_redecoded)) {
		panic("test/UTF8.dfy(138,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	_0_decoded = _dafny.SeqOfChars(8987)
	var _7_valueOrError4 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _7_valueOrError4
	_7_valueOrError4 = m_UTF8.Encode(_0_decoded)
	if !(!((_7_valueOrError4).IsFailure())) {
		panic("test/UTF8.dfy(142,15): " + (_7_valueOrError4).String())
	}
	_2_encoded = (_7_valueOrError4).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_dafny.SeqOf(uint8(226), uint8(140), uint8(155)), _2_encoded)) {
		panic("test/UTF8.dfy(143,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(m_UTF8.Companion_Default___.Uses3Bytes(_2_encoded)) {
		panic("test/UTF8.dfy(144,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _8_valueOrError5 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _8_valueOrError5
	_8_valueOrError5 = m_UTF8.Decode(_2_encoded)
	if !(!((_8_valueOrError5).IsFailure())) {
		panic("test/UTF8.dfy(145,17): " + (_8_valueOrError5).String())
	}
	_4_redecoded = (_8_valueOrError5).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_0_decoded, _4_redecoded)) {
		panic("test/UTF8.dfy(146,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	_0_decoded = _dafny.SeqOfChars(7544)
	var _9_valueOrError6 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _9_valueOrError6
	_9_valueOrError6 = m_UTF8.Encode(_0_decoded)
	if !(!((_9_valueOrError6).IsFailure())) {
		panic("test/UTF8.dfy(150,15): " + (_9_valueOrError6).String())
	}
	_2_encoded = (_9_valueOrError6).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_dafny.SeqOf(uint8(225), uint8(181), uint8(184)), _2_encoded)) {
		panic("test/UTF8.dfy(151,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(m_UTF8.Companion_Default___.Uses3Bytes(_2_encoded)) {
		panic("test/UTF8.dfy(152,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _10_valueOrError7 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _10_valueOrError7
	_10_valueOrError7 = m_UTF8.Decode(_2_encoded)
	if !(!((_10_valueOrError7).IsFailure())) {
		panic("test/UTF8.dfy(153,17): " + (_10_valueOrError7).String())
	}
	_4_redecoded = (_10_valueOrError7).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_0_decoded, _4_redecoded)) {
		panic("test/UTF8.dfy(154,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	_0_decoded = _dafny.SeqOfChars(29483)
	var _11_valueOrError8 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _11_valueOrError8
	_11_valueOrError8 = m_UTF8.Encode(_0_decoded)
	if !(!((_11_valueOrError8).IsFailure())) {
		panic("test/UTF8.dfy(158,15): " + (_11_valueOrError8).String())
	}
	_2_encoded = (_11_valueOrError8).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_dafny.SeqOf(uint8(231), uint8(140), uint8(171)), _2_encoded)) {
		panic("test/UTF8.dfy(159,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(m_UTF8.Companion_Default___.Uses3Bytes(_2_encoded)) {
		panic("test/UTF8.dfy(160,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _12_valueOrError9 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _12_valueOrError9
	_12_valueOrError9 = m_UTF8.Decode(_2_encoded)
	if !(!((_12_valueOrError9).IsFailure())) {
		panic("test/UTF8.dfy(161,17): " + (_12_valueOrError9).String())
	}
	_4_redecoded = (_12_valueOrError9).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_0_decoded, _4_redecoded)) {
		panic("test/UTF8.dfy(162,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) Test4Bytes() {
	var _0_decoded _dafny.Sequence
	_ = _0_decoded
	_0_decoded = _dafny.SeqOfChars(55304, 56320)
	var _1_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _1_valueOrError0
	_1_valueOrError0 = m_UTF8.Encode(_0_decoded)
	if !(!((_1_valueOrError0).IsFailure())) {
		panic("test/UTF8.dfy(168,19): " + (_1_valueOrError0).String())
	}
	var _2_encoded _dafny.Sequence
	_ = _2_encoded
	_2_encoded = (_1_valueOrError0).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_dafny.SeqOf(uint8(240), uint8(146), uint8(128), uint8(128)), _2_encoded)) {
		panic("test/UTF8.dfy(169,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(m_UTF8.Companion_Default___.Uses4Bytes(_2_encoded)) {
		panic("test/UTF8.dfy(170,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _3_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _3_valueOrError1
	_3_valueOrError1 = m_UTF8.Decode(_2_encoded)
	if !(!((_3_valueOrError1).IsFailure())) {
		panic("test/UTF8.dfy(171,21): " + (_3_valueOrError1).String())
	}
	var _4_redecoded _dafny.Sequence
	_ = _4_redecoded
	_4_redecoded = (_3_valueOrError1).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_0_decoded, _4_redecoded)) {
		panic("test/UTF8.dfy(172,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	_0_decoded = _dafny.SeqOfChars(55349, 57281)
	var _5_valueOrError2 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_UTF8.Companion_ValidUTF8Bytes_.Witness())
	_ = _5_valueOrError2
	_5_valueOrError2 = m_UTF8.Encode(_0_decoded)
	if !(!((_5_valueOrError2).IsFailure())) {
		panic("test/UTF8.dfy(176,15): " + (_5_valueOrError2).String())
	}
	_2_encoded = (_5_valueOrError2).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_dafny.SeqOf(uint8(240), uint8(157), uint8(159), uint8(129)), _2_encoded)) {
		panic("test/UTF8.dfy(177,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(m_UTF8.Companion_Default___.Uses4Bytes(_2_encoded)) {
		panic("test/UTF8.dfy(178,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _6_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _6_valueOrError3
	_6_valueOrError3 = m_UTF8.Decode(_2_encoded)
	if !(!((_6_valueOrError3).IsFailure())) {
		panic("test/UTF8.dfy(179,17): " + (_6_valueOrError3).String())
	}
	_4_redecoded = (_6_valueOrError3).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_0_decoded, _4_redecoded)) {
		panic("test/UTF8.dfy(180,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}

// End of class Default__
