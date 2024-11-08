// Package TestTime
// Dafny module TestTime compiled into Go

package TestTime

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
	m__Time "github.com/dafny-lang/DafnyStandardLibGo/Time_"
	m_UnicodeStrings "github.com/dafny-lang/DafnyStandardLibGo/UnicodeStrings"
	m__Unicode "github.com/dafny-lang/DafnyStandardLibGo/Unicode_"
	m_Utf16EncodingForm "github.com/dafny-lang/DafnyStandardLibGo/Utf16EncodingForm"
	m_Utf8EncodingForm "github.com/dafny-lang/DafnyStandardLibGo/Utf8EncodingForm"
	m_Wrappers "github.com/dafny-lang/DafnyStandardLibGo/Wrappers"
	m_GetOptTest "github.com/dafny-lang/DafnyStandardLibGo/test/GetOptTest"
	m_Sets "github.com/dafny-lang/DafnyStandardLibGo/test/Sets"
	m_TestComputeSetToOrderedSequenceCharLess "github.com/dafny-lang/DafnyStandardLibGo/test/TestComputeSetToOrderedSequenceCharLess"
	m_TestHexStrings "github.com/dafny-lang/DafnyStandardLibGo/test/TestHexStrings"
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
	return "TestTime.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) TestFormat() {
	if !(_dafny.Companion_Sequence_.Equal(m__Time.Companion_Default___.FormatMilliDiff(int64(123456), int64(123456)), _dafny.SeqOfString("0.000"))) {
		panic("test/Time.dfy(11,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(m__Time.Companion_Default___.FormatMilliDiff(int64(123456), int64(123457)), _dafny.SeqOfString("0.001"))) {
		panic("test/Time.dfy(12,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(m__Time.Companion_Default___.FormatMilliDiff(int64(123456), int64(123467)), _dafny.SeqOfString("0.011"))) {
		panic("test/Time.dfy(13,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(m__Time.Companion_Default___.FormatMilliDiff(int64(123456), int64(123567)), _dafny.SeqOfString("0.111"))) {
		panic("test/Time.dfy(14,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(m__Time.Companion_Default___.FormatMilliDiff(int64(123456), int64(124567)), _dafny.SeqOfString("1.111"))) {
		panic("test/Time.dfy(15,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(m__Time.Companion_Default___.FormatMilliDiff(int64(123456), int64(134567)), _dafny.SeqOfString("11.111"))) {
		panic("test/Time.dfy(16,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(m__Time.Companion_Default___.FormatMilliDiff(int64(123456), int64(234567)), _dafny.SeqOfString("111.111"))) {
		panic("test/Time.dfy(17,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestNonDecreasing() {
	var _0_t1 int64
	_ = _0_t1
	var _out0 int64
	_ = _out0
	_out0 = m__Time.CurrentRelativeTime()
	_0_t1 = _out0
	var _1_t2 int64
	_ = _1_t2
	var _out1 int64
	_ = _out1
	_out1 = m__Time.CurrentRelativeTime()
	_1_t2 = _out1
	if !((_1_t2) >= (_0_t1)) {
		panic("test/Time.dfy(23,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestNonDecreasingMilli() {
	var _0_t1 int64
	_ = _0_t1
	var _out0 int64
	_ = _out0
	_out0 = m__Time.CurrentRelativeTimeMilli()
	_0_t1 = _out0
	var _1_t2 int64
	_ = _1_t2
	var _out1 int64
	_ = _out1
	_out1 = m__Time.CurrentRelativeTimeMilli()
	_1_t2 = _out1
	if !((_1_t2) >= (_0_t1)) {
		panic("test/Time.dfy(29,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestPositiveValues() {
	var _0_t1 int64
	_ = _0_t1
	var _out0 int64
	_ = _out0
	_out0 = m__Time.CurrentRelativeTime()
	_0_t1 = _out0
	var _1_t2 int64
	_ = _1_t2
	var _out1 int64
	_ = _out1
	_out1 = m__Time.CurrentRelativeTime()
	_1_t2 = _out1
	if !(((_1_t2) - (_0_t1)) >= (int64(0))) {
		panic("test/Time.dfy(35,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestGetCurrentTimeStamp() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq.SetString())
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m__Time.GetCurrentTimeStamp()
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("test/Time.dfy(40,23): " + (_0_valueOrError0).String())
	}
	var _1_CurrentTime _dafny.Sequence
	_ = _1_CurrentTime
	_1_CurrentTime = (_0_valueOrError0).Extract().(_dafny.Sequence)
	if !(Companion_Default___.ISO8601_q(_1_CurrentTime)) {
		panic("test/Time.dfy(41,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) ISO8601_q(CreateTime _dafny.Sequence) bool {
	return ((((((((_dafny.IntOfUint32((CreateTime).Cardinality())).Cmp(_dafny.IntOfInt64(27)) == 0) && (((CreateTime).Select(4).(_dafny.Char)) == (_dafny.Char('-')))) && (((CreateTime).Select(7).(_dafny.Char)) == (_dafny.Char('-')))) && (((CreateTime).Select(10).(_dafny.Char)) == (_dafny.Char('T')))) && (((CreateTime).Select(13).(_dafny.Char)) == (_dafny.Char(':')))) && (((CreateTime).Select(16).(_dafny.Char)) == (_dafny.Char(':')))) && (((CreateTime).Select(19).(_dafny.Char)) == (_dafny.Char('.')))) && (((CreateTime).Select(26).(_dafny.Char)) == (_dafny.Char('Z')))
}

// End of class Default__
