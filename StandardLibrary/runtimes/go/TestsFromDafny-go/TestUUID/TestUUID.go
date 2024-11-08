// Package TestUUID
// Dafny module TestUUID compiled into Go

package TestUUID

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
	m_UUID "github.com/dafny-lang/DafnyStandardLibGo/UUID"
	m_UnicodeStrings "github.com/dafny-lang/DafnyStandardLibGo/UnicodeStrings"
	m__Unicode "github.com/dafny-lang/DafnyStandardLibGo/Unicode_"
	m_Utf16EncodingForm "github.com/dafny-lang/DafnyStandardLibGo/Utf16EncodingForm"
	m_Utf8EncodingForm "github.com/dafny-lang/DafnyStandardLibGo/Utf8EncodingForm"
	m_Wrappers "github.com/dafny-lang/DafnyStandardLibGo/Wrappers"
	m_GetOptTest "github.com/dafny-lang/DafnyStandardLibGo/test/GetOptTest"
	m_Sets "github.com/dafny-lang/DafnyStandardLibGo/test/Sets"
	m_TestComputeSetToOrderedSequenceCharLess "github.com/dafny-lang/DafnyStandardLibGo/test/TestComputeSetToOrderedSequenceCharLess"
	m_TestComputeSetToOrderedSequenceUInt8Less "github.com/dafny-lang/DafnyStandardLibGo/test/TestComputeSetToOrderedSequenceUInt8Less"
	m_TestHexStrings "github.com/dafny-lang/DafnyStandardLibGo/test/TestHexStrings"
	m_TestTime "github.com/dafny-lang/DafnyStandardLibGo/test/TestTime"
	m_TestUTF8 "github.com/dafny-lang/DafnyStandardLibGo/test/TestUTF8"
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
var _ m_TestUTF8.Dummy__
var _ m_TestComputeSetToOrderedSequenceUInt8Less.Dummy__

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
	return "TestUUID.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) TestFromBytesSuccess() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _0_valueOrError0
	_0_valueOrError0 = m_UUID.FromByteArray(Companion_Default___.ByteUuid())
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("test/UUID.dfy(23,21): " + (_0_valueOrError0).String())
	}
	var _1_fromBytes _dafny.Sequence
	_ = _1_fromBytes
	_1_fromBytes = (_0_valueOrError0).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_1_fromBytes, Companion_Default___.Uuid())) {
		panic("test/UUID.dfy(24,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestFromBytesFailure() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _0_valueOrError0
	_0_valueOrError0 = m_UUID.FromByteArray(Companion_Default___.WrongByteUuid())
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("test/UUID.dfy(28,21): " + (_0_valueOrError0).String())
	}
	var _1_fromBytes _dafny.Sequence
	_ = _1_fromBytes
	_1_fromBytes = (_0_valueOrError0).Extract().(_dafny.Sequence)
	if !(!_dafny.Companion_Sequence_.Equal(_1_fromBytes, Companion_Default___.Uuid())) {
		panic("test/UUID.dfy(29,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestToBytesSuccess() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _0_valueOrError0
	_0_valueOrError0 = m_UUID.ToByteArray(Companion_Default___.Uuid())
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("test/UUID.dfy(33,19): " + (_0_valueOrError0).String())
	}
	var _1_toBytes _dafny.Sequence
	_ = _1_toBytes
	_1_toBytes = (_0_valueOrError0).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_1_toBytes, Companion_Default___.ByteUuid())) {
		panic("test/UUID.dfy(34,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestToBytesFailure() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _0_valueOrError0
	_0_valueOrError0 = m_UUID.ToByteArray(Companion_Default___.Uuid())
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("test/UUID.dfy(38,19): " + (_0_valueOrError0).String())
	}
	var _1_toBytes _dafny.Sequence
	_ = _1_toBytes
	_1_toBytes = (_0_valueOrError0).Extract().(_dafny.Sequence)
	if !(!_dafny.Companion_Sequence_.Equal(_1_toBytes, Companion_Default___.WrongByteUuid())) {
		panic("test/UUID.dfy(39,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestRoundTripStringConversion() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _0_valueOrError0
	_0_valueOrError0 = m_UUID.ToByteArray(Companion_Default___.Uuid())
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("test/UUID.dfy(43,25): " + (_0_valueOrError0).String())
	}
	var _1_stringToBytes _dafny.Sequence
	_ = _1_stringToBytes
	_1_stringToBytes = (_0_valueOrError0).Extract().(_dafny.Sequence)
	if !((_dafny.IntOfUint32((_1_stringToBytes).Cardinality())).Cmp(_dafny.IntOfInt64(16)) == 0) {
		panic("test/UUID.dfy(44,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _2_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _2_valueOrError1
	_2_valueOrError1 = m_UUID.FromByteArray(_1_stringToBytes)
	if !(!((_2_valueOrError1).IsFailure())) {
		panic("test/UUID.dfy(45,25): " + (_2_valueOrError1).String())
	}
	var _3_bytesToString _dafny.Sequence
	_ = _3_bytesToString
	_3_bytesToString = (_2_valueOrError1).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_3_bytesToString, Companion_Default___.Uuid())) {
		panic("test/UUID.dfy(46,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestRoundTripByteConversion() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _0_valueOrError0
	_0_valueOrError0 = m_UUID.FromByteArray(Companion_Default___.ByteUuid())
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("test/UUID.dfy(50,25): " + (_0_valueOrError0).String())
	}
	var _1_bytesToString _dafny.Sequence
	_ = _1_bytesToString
	_1_bytesToString = (_0_valueOrError0).Extract().(_dafny.Sequence)
	var _2_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _2_valueOrError1
	_2_valueOrError1 = m_UUID.ToByteArray(_1_bytesToString)
	if !(!((_2_valueOrError1).IsFailure())) {
		panic("test/UUID.dfy(51,25): " + (_2_valueOrError1).String())
	}
	var _3_stringToBytes _dafny.Sequence
	_ = _3_stringToBytes
	_3_stringToBytes = (_2_valueOrError1).Extract().(_dafny.Sequence)
	if !((_dafny.IntOfUint32((_3_stringToBytes).Cardinality())).Cmp(_dafny.IntOfInt64(16)) == 0) {
		panic("test/UUID.dfy(52,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(_3_stringToBytes, Companion_Default___.ByteUuid())) {
		panic("test/UUID.dfy(53,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestGenerateAndConversion() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_UUID.GenerateUUID()
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("test/UUID.dfy(57,22): " + (_0_valueOrError0).String())
	}
	var _1_uuidString _dafny.Sequence
	_ = _1_uuidString
	_1_uuidString = (_0_valueOrError0).Extract().(_dafny.Sequence)
	var _2_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _2_valueOrError1
	_2_valueOrError1 = m_UUID.ToByteArray(_1_uuidString)
	if !(!((_2_valueOrError1).IsFailure())) {
		panic("test/UUID.dfy(58,21): " + (_2_valueOrError1).String())
	}
	var _3_uuidBytes _dafny.Sequence
	_ = _3_uuidBytes
	_3_uuidBytes = (_2_valueOrError1).Extract().(_dafny.Sequence)
	var _4_valueOrError2 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _4_valueOrError2
	_4_valueOrError2 = m_UUID.FromByteArray(_3_uuidBytes)
	if !(!((_4_valueOrError2).IsFailure())) {
		panic("test/UUID.dfy(60,25): " + (_4_valueOrError2).String())
	}
	var _5_bytesToString _dafny.Sequence
	_ = _5_bytesToString
	_5_bytesToString = (_4_valueOrError2).Extract().(_dafny.Sequence)
	var _6_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _6_valueOrError3
	_6_valueOrError3 = m_UUID.ToByteArray(_5_bytesToString)
	if !(!((_6_valueOrError3).IsFailure())) {
		panic("test/UUID.dfy(61,25): " + (_6_valueOrError3).String())
	}
	var _7_stringToBytes _dafny.Sequence
	_ = _7_stringToBytes
	_7_stringToBytes = (_6_valueOrError3).Extract().(_dafny.Sequence)
	if !((_dafny.IntOfUint32((_7_stringToBytes).Cardinality())).Cmp(_dafny.IntOfInt64(16)) == 0) {
		panic("test/UUID.dfy(62,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(_7_stringToBytes, _3_uuidBytes)) {
		panic("test/UUID.dfy(63,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _8_valueOrError4 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _8_valueOrError4
	_8_valueOrError4 = m_UUID.ToByteArray(_1_uuidString)
	if !(!((_8_valueOrError4).IsFailure())) {
		panic("test/UUID.dfy(65,29): " + (_8_valueOrError4).String())
	}
	var _9_uuidStringToBytes _dafny.Sequence
	_ = _9_uuidStringToBytes
	_9_uuidStringToBytes = (_8_valueOrError4).Extract().(_dafny.Sequence)
	if !((_dafny.IntOfUint32((_9_uuidStringToBytes).Cardinality())).Cmp(_dafny.IntOfInt64(16)) == 0) {
		panic("test/UUID.dfy(66,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _10_valueOrError5 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _10_valueOrError5
	_10_valueOrError5 = m_UUID.FromByteArray(_9_uuidStringToBytes)
	if !(!((_10_valueOrError5).IsFailure())) {
		panic("test/UUID.dfy(67,29): " + (_10_valueOrError5).String())
	}
	var _11_uuidBytesToString _dafny.Sequence
	_ = _11_uuidBytesToString
	_11_uuidBytesToString = (_10_valueOrError5).Extract().(_dafny.Sequence)
	if !(_dafny.Companion_Sequence_.Equal(_11_uuidBytesToString, _1_uuidString)) {
		panic("test/UUID.dfy(68,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) ByteUuid() _dafny.Sequence {
	return _dafny.SeqOf(uint8(146), uint8(56), uint8(38), uint8(88), uint8(183), uint8(160), uint8(77), uint8(151), uint8(156), uint8(73), uint8(206), uint8(228), uint8(230), uint8(114), uint8(163), uint8(179))
}
func (_static *CompanionStruct_Default___) Uuid() _dafny.Sequence {
	return _dafny.SeqOfString("92382658-b7a0-4d97-9c49-cee4e672a3b3")
}
func (_static *CompanionStruct_Default___) WrongByteUuid() _dafny.Sequence {
	return _dafny.SeqOf(uint8(146), uint8(56), uint8(38), uint8(88), uint8(183), uint8(160), uint8(77), uint8(151), uint8(156), uint8(73), uint8(206), uint8(228), uint8(230), uint8(114), uint8(163), uint8(178))
}

// End of class Default__
