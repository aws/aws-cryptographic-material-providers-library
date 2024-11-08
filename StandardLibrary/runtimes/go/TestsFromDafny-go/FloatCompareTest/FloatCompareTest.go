// Package FloatCompareTest
// Dafny module FloatCompareTest compiled into Go

package FloatCompareTest

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
	m_TestUUID "github.com/dafny-lang/DafnyStandardLibGo/test/TestUUID"
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
var _ m_TestUUID.Dummy__

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
	return "FloatCompareTest.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) TestCompareFloat(x _dafny.Sequence, y _dafny.Sequence, ret int8) {
	if (m_FloatCompare.Companion_Default___.CompareFloat(x, y)) != (ret) /* dircomp */ {
		_dafny.Print((_dafny.SeqOfString("CompareFloat(")).SetString())
		_dafny.Print((x).SetString())
		_dafny.Print((_dafny.SeqOfString(", ")).SetString())
		_dafny.Print((y).SetString())
		_dafny.Print((_dafny.SeqOfString(") was ")).SetString())
		_dafny.Print(m_FloatCompare.Companion_Default___.CompareFloat(x, y))
		_dafny.Print((_dafny.SeqOfString(" but should have been ")).SetString())
		_dafny.Print(ret)
		_dafny.Print((_dafny.SeqOfString("\n")).SetString())
	}
	if (m_FloatCompare.Companion_Default___.CompareFloat(y, x)) != ((int8(0)) - (ret)) /* dircomp */ {
		_dafny.Print((_dafny.SeqOfString("CompareFloat(")).SetString())
		_dafny.Print((y).SetString())
		_dafny.Print((_dafny.SeqOfString(", ")).SetString())
		_dafny.Print((x).SetString())
		_dafny.Print((_dafny.SeqOfString(") was ")).SetString())
		_dafny.Print(m_FloatCompare.Companion_Default___.CompareFloat(y, x))
		_dafny.Print((_dafny.SeqOfString(" but should have been ")).SetString())
		_dafny.Print((int8(0)) - (ret))
		_dafny.Print((_dafny.SeqOfString("\n")).SetString())
	}
	if !((m_FloatCompare.Companion_Default___.CompareFloat(x, y)) == (ret)) {
		panic("test/FloatCompare.dfy(165,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !((m_FloatCompare.Companion_Default___.CompareFloat(y, x)) == ((int8(0)) - (ret))) {
		panic("test/FloatCompare.dfy(166,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestOneTwoZeroMatrix() {
	var _hi0 _dafny.Int = _dafny.IntOfUint32((Companion_Default___.NEGATIVE__TWO()).Cardinality())
	_ = _hi0
	for _0_i := _dafny.Zero; _0_i.Cmp(_hi0) < 0; _0_i = _0_i.Plus(_dafny.One) {
		var _1_negativeTwo _dafny.Sequence
		_ = _1_negativeTwo
		_1_negativeTwo = (Companion_Default___.NEGATIVE__TWO()).Select((_0_i).Uint32()).(_dafny.Sequence)
		var _hi1 _dafny.Int = _dafny.IntOfUint32((Companion_Default___.NEGATIVE__TWO()).Cardinality())
		_ = _hi1
		for _2_j := _0_i; _2_j.Cmp(_hi1) < 0; _2_j = _2_j.Plus(_dafny.One) {
			Companion_Default___.TestCompareFloat((Companion_Default___.NEGATIVE__TWO()).Select((_2_j).Uint32()).(_dafny.Sequence), _1_negativeTwo, m_FloatCompare.Companion_Default___.Equal())
		}
		var _hi2 _dafny.Int = _dafny.IntOfUint32((Companion_Default___.NEGATIVE__ONE()).Cardinality())
		_ = _hi2
		for _3_j := _dafny.Zero; _3_j.Cmp(_hi2) < 0; _3_j = _3_j.Plus(_dafny.One) {
			Companion_Default___.TestCompareFloat((Companion_Default___.NEGATIVE__ONE()).Select((_3_j).Uint32()).(_dafny.Sequence), _1_negativeTwo, m_FloatCompare.Companion_Default___.Greater())
		}
		var _hi3 _dafny.Int = _dafny.IntOfUint32((Companion_Default___.ZERO()).Cardinality())
		_ = _hi3
		for _4_j := _dafny.Zero; _4_j.Cmp(_hi3) < 0; _4_j = _4_j.Plus(_dafny.One) {
			Companion_Default___.TestCompareFloat((Companion_Default___.ZERO()).Select((_4_j).Uint32()).(_dafny.Sequence), _1_negativeTwo, m_FloatCompare.Companion_Default___.Greater())
		}
		var _hi4 _dafny.Int = _dafny.IntOfUint32((Companion_Default___.ONE()).Cardinality())
		_ = _hi4
		for _5_j := _dafny.Zero; _5_j.Cmp(_hi4) < 0; _5_j = _5_j.Plus(_dafny.One) {
			Companion_Default___.TestCompareFloat((Companion_Default___.ONE()).Select((_5_j).Uint32()).(_dafny.Sequence), _1_negativeTwo, m_FloatCompare.Companion_Default___.Greater())
		}
		var _hi5 _dafny.Int = _dafny.IntOfUint32((Companion_Default___.TWO()).Cardinality())
		_ = _hi5
		for _6_j := _dafny.Zero; _6_j.Cmp(_hi5) < 0; _6_j = _6_j.Plus(_dafny.One) {
			Companion_Default___.TestCompareFloat((Companion_Default___.TWO()).Select((_6_j).Uint32()).(_dafny.Sequence), _1_negativeTwo, m_FloatCompare.Companion_Default___.Greater())
		}
	}
	var _hi6 _dafny.Int = _dafny.IntOfUint32((Companion_Default___.NEGATIVE__ONE()).Cardinality())
	_ = _hi6
	for _7_i := _dafny.Zero; _7_i.Cmp(_hi6) < 0; _7_i = _7_i.Plus(_dafny.One) {
		var _8_negativeOne _dafny.Sequence
		_ = _8_negativeOne
		_8_negativeOne = (Companion_Default___.NEGATIVE__ONE()).Select((_7_i).Uint32()).(_dafny.Sequence)
		var _hi7 _dafny.Int = _dafny.IntOfUint32((Companion_Default___.NEGATIVE__ONE()).Cardinality())
		_ = _hi7
		for _9_j := _7_i; _9_j.Cmp(_hi7) < 0; _9_j = _9_j.Plus(_dafny.One) {
			Companion_Default___.TestCompareFloat((Companion_Default___.NEGATIVE__ONE()).Select((_9_j).Uint32()).(_dafny.Sequence), _8_negativeOne, m_FloatCompare.Companion_Default___.Equal())
		}
		var _hi8 _dafny.Int = _dafny.IntOfUint32((Companion_Default___.ZERO()).Cardinality())
		_ = _hi8
		for _10_j := _dafny.Zero; _10_j.Cmp(_hi8) < 0; _10_j = _10_j.Plus(_dafny.One) {
			Companion_Default___.TestCompareFloat((Companion_Default___.ZERO()).Select((_10_j).Uint32()).(_dafny.Sequence), _8_negativeOne, m_FloatCompare.Companion_Default___.Greater())
		}
		var _hi9 _dafny.Int = _dafny.IntOfUint32((Companion_Default___.ONE()).Cardinality())
		_ = _hi9
		for _11_j := _dafny.Zero; _11_j.Cmp(_hi9) < 0; _11_j = _11_j.Plus(_dafny.One) {
			Companion_Default___.TestCompareFloat((Companion_Default___.ONE()).Select((_11_j).Uint32()).(_dafny.Sequence), _8_negativeOne, m_FloatCompare.Companion_Default___.Greater())
		}
		var _hi10 _dafny.Int = _dafny.IntOfUint32((Companion_Default___.TWO()).Cardinality())
		_ = _hi10
		for _12_j := _dafny.Zero; _12_j.Cmp(_hi10) < 0; _12_j = _12_j.Plus(_dafny.One) {
			Companion_Default___.TestCompareFloat((Companion_Default___.TWO()).Select((_12_j).Uint32()).(_dafny.Sequence), _8_negativeOne, m_FloatCompare.Companion_Default___.Greater())
		}
	}
	var _hi11 _dafny.Int = _dafny.IntOfUint32((Companion_Default___.ZERO()).Cardinality())
	_ = _hi11
	for _13_i := _dafny.Zero; _13_i.Cmp(_hi11) < 0; _13_i = _13_i.Plus(_dafny.One) {
		var _14_zero _dafny.Sequence
		_ = _14_zero
		_14_zero = (Companion_Default___.ZERO()).Select((_13_i).Uint32()).(_dafny.Sequence)
		var _hi12 _dafny.Int = _dafny.IntOfUint32((Companion_Default___.ZERO()).Cardinality())
		_ = _hi12
		for _15_j := _13_i; _15_j.Cmp(_hi12) < 0; _15_j = _15_j.Plus(_dafny.One) {
			Companion_Default___.TestCompareFloat((Companion_Default___.ZERO()).Select((_15_j).Uint32()).(_dafny.Sequence), _14_zero, m_FloatCompare.Companion_Default___.Equal())
		}
		var _hi13 _dafny.Int = _dafny.IntOfUint32((Companion_Default___.ONE()).Cardinality())
		_ = _hi13
		for _16_j := _dafny.Zero; _16_j.Cmp(_hi13) < 0; _16_j = _16_j.Plus(_dafny.One) {
			Companion_Default___.TestCompareFloat((Companion_Default___.ONE()).Select((_16_j).Uint32()).(_dafny.Sequence), _14_zero, m_FloatCompare.Companion_Default___.Greater())
		}
		var _hi14 _dafny.Int = _dafny.IntOfUint32((Companion_Default___.TWO()).Cardinality())
		_ = _hi14
		for _17_j := _dafny.Zero; _17_j.Cmp(_hi14) < 0; _17_j = _17_j.Plus(_dafny.One) {
			Companion_Default___.TestCompareFloat((Companion_Default___.TWO()).Select((_17_j).Uint32()).(_dafny.Sequence), _14_zero, m_FloatCompare.Companion_Default___.Greater())
		}
	}
	var _hi15 _dafny.Int = _dafny.IntOfUint32((Companion_Default___.ONE()).Cardinality())
	_ = _hi15
	for _18_i := _dafny.Zero; _18_i.Cmp(_hi15) < 0; _18_i = _18_i.Plus(_dafny.One) {
		var _19_one _dafny.Sequence
		_ = _19_one
		_19_one = (Companion_Default___.ONE()).Select((_18_i).Uint32()).(_dafny.Sequence)
		var _hi16 _dafny.Int = _dafny.IntOfUint32((Companion_Default___.ONE()).Cardinality())
		_ = _hi16
		for _20_j := _18_i; _20_j.Cmp(_hi16) < 0; _20_j = _20_j.Plus(_dafny.One) {
			Companion_Default___.TestCompareFloat((Companion_Default___.ONE()).Select((_20_j).Uint32()).(_dafny.Sequence), _19_one, m_FloatCompare.Companion_Default___.Equal())
		}
		var _hi17 _dafny.Int = _dafny.IntOfUint32((Companion_Default___.TWO()).Cardinality())
		_ = _hi17
		for _21_j := _dafny.Zero; _21_j.Cmp(_hi17) < 0; _21_j = _21_j.Plus(_dafny.One) {
			Companion_Default___.TestCompareFloat((Companion_Default___.TWO()).Select((_21_j).Uint32()).(_dafny.Sequence), _19_one, m_FloatCompare.Companion_Default___.Greater())
		}
	}
	var _hi18 _dafny.Int = _dafny.IntOfUint32((Companion_Default___.TWO()).Cardinality())
	_ = _hi18
	for _22_i := _dafny.Zero; _22_i.Cmp(_hi18) < 0; _22_i = _22_i.Plus(_dafny.One) {
		var _23_two _dafny.Sequence
		_ = _23_two
		_23_two = (Companion_Default___.TWO()).Select((_22_i).Uint32()).(_dafny.Sequence)
		var _hi19 _dafny.Int = _dafny.IntOfUint32((Companion_Default___.TWO()).Cardinality())
		_ = _hi19
		for _24_j := _22_i; _24_j.Cmp(_hi19) < 0; _24_j = _24_j.Plus(_dafny.One) {
			Companion_Default___.TestCompareFloat((Companion_Default___.TWO()).Select((_24_j).Uint32()).(_dafny.Sequence), _23_two, m_FloatCompare.Companion_Default___.Equal())
		}
	}
}
func (_static *CompanionStruct_Default___) SimpleTests() {
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("1"), _dafny.SeqOfString("1"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("2"), _dafny.SeqOfString("1"), m_FloatCompare.Companion_Default___.Greater())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("1.1"), _dafny.SeqOfString("1.2"), m_FloatCompare.Companion_Default___.Less())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("1.2"), _dafny.SeqOfString("1.2"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("1.35"), _dafny.SeqOfString("1.357"), m_FloatCompare.Companion_Default___.Less())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("1.35e2"), _dafny.SeqOfString("13.5e1"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("1.351e2"), _dafny.SeqOfString("13.5e1"), m_FloatCompare.Companion_Default___.Greater())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("1.35e-1"), _dafny.SeqOfString("13.5e-2"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("1"), _dafny.SeqOfString("-2"), m_FloatCompare.Companion_Default___.Greater())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("1.2e7"), _dafny.SeqOfString("2.3e2"), m_FloatCompare.Companion_Default___.Greater())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-1.2e7"), _dafny.SeqOfString("2.3e2"), m_FloatCompare.Companion_Default___.Less())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("1.2e7"), _dafny.SeqOfString("-2.3e2"), m_FloatCompare.Companion_Default___.Greater())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-1.2e7"), _dafny.SeqOfString("-2.3e2"), m_FloatCompare.Companion_Default___.Less())
}
func (_static *CompanionStruct_Default___) SignTests() {
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("+1"), _dafny.SeqOfString("1"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("+1e+0"), _dafny.SeqOfString("1"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("+1e-0"), _dafny.SeqOfString("1"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-1"), _dafny.SeqOfString("1"), m_FloatCompare.Companion_Default___.Less())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-1"), _dafny.SeqOfString("+1"), m_FloatCompare.Companion_Default___.Less())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("1"), _dafny.SeqOfString("-1"), m_FloatCompare.Companion_Default___.Greater())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("+1"), _dafny.SeqOfString("-1"), m_FloatCompare.Companion_Default___.Greater())
}
func (_static *CompanionStruct_Default___) ExponentTests() {
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("2e0"), _dafny.SeqOfString("2e0"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("1e0"), _dafny.SeqOfString("2e0"), m_FloatCompare.Companion_Default___.Less())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("3e0"), _dafny.SeqOfString("2e0"), m_FloatCompare.Companion_Default___.Greater())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("1e-5"), _dafny.SeqOfString("1e5"), m_FloatCompare.Companion_Default___.Less())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("1e5"), _dafny.SeqOfString("1e-5"), m_FloatCompare.Companion_Default___.Greater())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("1e5"), _dafny.SeqOfString("1e6"), m_FloatCompare.Companion_Default___.Less())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("1e5"), _dafny.SeqOfString("1e4"), m_FloatCompare.Companion_Default___.Greater())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("1e-5"), _dafny.SeqOfString("1e-4"), m_FloatCompare.Companion_Default___.Less())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("1e-5"), _dafny.SeqOfString("1e-6"), m_FloatCompare.Companion_Default___.Greater())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-1e5"), _dafny.SeqOfString("-1e-5"), m_FloatCompare.Companion_Default___.Less())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-1e-5"), _dafny.SeqOfString("-1e5"), m_FloatCompare.Companion_Default___.Greater())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-1e5"), _dafny.SeqOfString("-1e4"), m_FloatCompare.Companion_Default___.Less())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-1e5"), _dafny.SeqOfString("-1e6"), m_FloatCompare.Companion_Default___.Greater())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-1e-5"), _dafny.SeqOfString("-1e-6"), m_FloatCompare.Companion_Default___.Less())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-1e-5"), _dafny.SeqOfString("-1e-4"), m_FloatCompare.Companion_Default___.Greater())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("2"), _dafny.SeqOfString("2e0"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("1"), _dafny.SeqOfString("2e0"), m_FloatCompare.Companion_Default___.Less())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("3"), _dafny.SeqOfString("2e0"), m_FloatCompare.Companion_Default___.Greater())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("20"), _dafny.SeqOfString("2e1"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("19"), _dafny.SeqOfString("2e1"), m_FloatCompare.Companion_Default___.Less())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("21"), _dafny.SeqOfString("2e1"), m_FloatCompare.Companion_Default___.Greater())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-20"), _dafny.SeqOfString("-2e1"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-21"), _dafny.SeqOfString("-2e1"), m_FloatCompare.Companion_Default___.Less())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-19"), _dafny.SeqOfString("-2e1"), m_FloatCompare.Companion_Default___.Greater())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("0.2"), _dafny.SeqOfString("2e-1"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("0.02"), _dafny.SeqOfString("2e-2"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("0.02"), _dafny.SeqOfString(".2e-1"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString(".1"), _dafny.SeqOfString("2e-1"), m_FloatCompare.Companion_Default___.Less())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString(".3"), _dafny.SeqOfString("2e-1"), m_FloatCompare.Companion_Default___.Greater())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-0.2"), _dafny.SeqOfString("-2e-1"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-0.02"), _dafny.SeqOfString("-2e-2"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-0.02"), _dafny.SeqOfString("-.2e-1"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-.3"), _dafny.SeqOfString("-2e-1"), m_FloatCompare.Companion_Default___.Less())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-.1"), _dafny.SeqOfString("-2e-1"), m_FloatCompare.Companion_Default___.Greater())
}
func (_static *CompanionStruct_Default___) ZeroTests() {
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-0"), _dafny.SeqOfString("0"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("+0"), _dafny.SeqOfString("0"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("00"), _dafny.SeqOfString("0"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("0.0"), _dafny.SeqOfString("0"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("0"), _dafny.SeqOfString("000"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("0"), _dafny.SeqOfString(".000"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("0.0"), _dafny.SeqOfString("000.00000"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("0"), _dafny.SeqOfString("000.000e0"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("0"), _dafny.SeqOfString("0e+0"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("0"), _dafny.SeqOfString("0e-0"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("0"), _dafny.SeqOfString("0e99"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("0"), _dafny.SeqOfString("0e-99"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("0e+99"), _dafny.SeqOfString("0e-99"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("+0e+99"), _dafny.SeqOfString("-0e-99"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-0e+99"), _dafny.SeqOfString("-0e-99"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-0e+99"), _dafny.SeqOfString("+0e-99"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("01"), _dafny.SeqOfString("1"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("1"), _dafny.SeqOfString("001"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("1.0"), _dafny.SeqOfString("001.00000"), m_FloatCompare.Companion_Default___.Equal())
}
func (_static *CompanionStruct_Default___) ExtremeNumTest() {
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("123456789.01234567890123456789012345678"), _dafny.SeqOfString("123456789.01234567890123456789012345678"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("1234567890123456789012345678901234567800000000000000000000000000000"), _dafny.SeqOfString("1234567890123456789012345678901234567800000000000000000000000000000"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString(".000000000000000000000000012345678901234567890123456789012345678"), _dafny.SeqOfString("0.000000000000000000000000012345678901234567890123456789012345678"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("123456789.01234567890123456789012345676"), _dafny.SeqOfString("123456789.01234567890123456789012345678"), m_FloatCompare.Companion_Default___.Less())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("123456789.01234567890123456789012345675"), _dafny.SeqOfString("123456789.01234567890123456789012345676"), m_FloatCompare.Companion_Default___.Less())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("123456789.01234567890123456789012345679"), _dafny.SeqOfString("123456789.01234567890123456789012345678"), m_FloatCompare.Companion_Default___.Greater())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("123456789.01234567890123456789012345677"), _dafny.SeqOfString("123456789.01234567890123456789012345676"), m_FloatCompare.Companion_Default___.Greater())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-123456789.01234567890123456789012345678"), _dafny.SeqOfString("123456789.01234567890123456789012345678"), m_FloatCompare.Companion_Default___.Less())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("123456789.01234567890123456789012345678"), _dafny.SeqOfString("-123456789.01234567890123456789012345678"), m_FloatCompare.Companion_Default___.Greater())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("0000000000000000000000000012345.67e121"), _dafny.SeqOfString("123456700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("12345.67e121"), _dafny.SeqOfString("123456700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("0.00000001e133"), _dafny.SeqOfString("100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("0.00000001e-122"), _dafny.SeqOfString("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("1234567e-136"), _dafny.SeqOfString("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001234567"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("0000000000000000000000000012345.66e121"), _dafny.SeqOfString("123456700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), m_FloatCompare.Companion_Default___.Less())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("0000000000000000000000000012345.68e121"), _dafny.SeqOfString("123456700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), m_FloatCompare.Companion_Default___.Greater())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("12345.67e120"), _dafny.SeqOfString("12345.67e121"), m_FloatCompare.Companion_Default___.Less())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("12345.67e122"), _dafny.SeqOfString("12345.67e121"), m_FloatCompare.Companion_Default___.Greater())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-12345.67e122"), _dafny.SeqOfString("-12345.67e121"), m_FloatCompare.Companion_Default___.Less())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-12345.67e120"), _dafny.SeqOfString("-12345.67e121"), m_FloatCompare.Companion_Default___.Greater())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("12345.67e120"), _dafny.SeqOfString("123456700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), m_FloatCompare.Companion_Default___.Less())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("12345.67e122"), _dafny.SeqOfString("123456700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), m_FloatCompare.Companion_Default___.Greater())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-12345.67e122"), _dafny.SeqOfString("-123456700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), m_FloatCompare.Companion_Default___.Less())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-12345.67e120"), _dafny.SeqOfString("-123456700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), m_FloatCompare.Companion_Default___.Greater())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("0.00000001e-123"), _dafny.SeqOfString("0.00000001e-122"), m_FloatCompare.Companion_Default___.Less())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("0.00000001e-121"), _dafny.SeqOfString("0.00000001e-122"), m_FloatCompare.Companion_Default___.Greater())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-0.00000001e-121"), _dafny.SeqOfString("-0.00000001e-122"), m_FloatCompare.Companion_Default___.Less())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-0.00000001e-123"), _dafny.SeqOfString("-0.00000001e-122"), m_FloatCompare.Companion_Default___.Greater())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("0.00000001e-123"), _dafny.SeqOfString("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), m_FloatCompare.Companion_Default___.Less())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("0.00000001e-121"), _dafny.SeqOfString("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), m_FloatCompare.Companion_Default___.Greater())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-0.00000001e-121"), _dafny.SeqOfString("-0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), m_FloatCompare.Companion_Default___.Less())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-0.00000001e-123"), _dafny.SeqOfString("-0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), m_FloatCompare.Companion_Default___.Greater())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("9.9999999999999999999999999999999999999E+125"), _dafny.SeqOfString("999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString(".99999999999999999999999999999999999999E+126"), _dafny.SeqOfString("999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), _dafny.SeqOfString("999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("9.9999999999999999999999999999999999999E+124"), _dafny.SeqOfString("999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), m_FloatCompare.Companion_Default___.Less())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("9.9999999999999999999999999999999999999E+126"), _dafny.SeqOfString("999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), m_FloatCompare.Companion_Default___.Greater())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("999999999999999999999999999999999999989999999999999999999999999999999999999999999999999999999999999999999999999999999999999999"), _dafny.SeqOfString("999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), m_FloatCompare.Companion_Default___.Less())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), _dafny.SeqOfString("999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), m_FloatCompare.Companion_Default___.Greater())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("1E-130"), _dafny.SeqOfString("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("10E-131"), _dafny.SeqOfString("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), _dafny.SeqOfString("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("1E-131"), _dafny.SeqOfString("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), m_FloatCompare.Companion_Default___.Less())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("1E-129"), _dafny.SeqOfString("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), m_FloatCompare.Companion_Default___.Greater())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000009"), _dafny.SeqOfString("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), m_FloatCompare.Companion_Default___.Less())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002"), _dafny.SeqOfString("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), m_FloatCompare.Companion_Default___.Greater())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-9.9999999999999999999999999999999999999E+125"), _dafny.SeqOfString("-999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-.99999999999999999999999999999999999999E+126"), _dafny.SeqOfString("-999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), _dafny.SeqOfString("-999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-9.9999999999999999999999999999999999999E+126"), _dafny.SeqOfString("-999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), m_FloatCompare.Companion_Default___.Less())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-9.9999999999999999999999999999999999999E+124"), _dafny.SeqOfString("-999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), m_FloatCompare.Companion_Default___.Greater())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), _dafny.SeqOfString("-999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), m_FloatCompare.Companion_Default___.Less())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-99999999999999999999999999999999999998999999999999999999999999999999999999999999999999999999999999999999999999999999999999999"), _dafny.SeqOfString("-999999999999999999999999999999999999990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), m_FloatCompare.Companion_Default___.Greater())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-1E-130"), _dafny.SeqOfString("-0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-10E-131"), _dafny.SeqOfString("-0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), _dafny.SeqOfString("-0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-1E-129"), _dafny.SeqOfString("-0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), m_FloatCompare.Companion_Default___.Less())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-1E-131"), _dafny.SeqOfString("-0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), m_FloatCompare.Companion_Default___.Greater())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002"), _dafny.SeqOfString("-0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), m_FloatCompare.Companion_Default___.Less())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("-0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000009"), _dafny.SeqOfString("-0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"), m_FloatCompare.Companion_Default___.Greater())
}
func (_static *CompanionStruct_Default___) InvalidTests() {
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("a"), _dafny.SeqOfString("0"), m_FloatCompare.Companion_Default___.Equal())
	Companion_Default___.TestCompareFloat(_dafny.SeqOfString("a"), _dafny.SeqOfString("b"), m_FloatCompare.Companion_Default___.Equal())
}
func (_static *CompanionStruct_Default___) NEGATIVE__TWO() _dafny.Sequence {
	return _dafny.SeqOf(_dafny.SeqOfString("-2"), _dafny.SeqOfString("-2."), _dafny.SeqOfString("-2.0"), _dafny.SeqOfString("-2e0"), _dafny.SeqOfString("-2.e0"), _dafny.SeqOfString("-2.0e0"), _dafny.SeqOfString("-2.0e+0"), _dafny.SeqOfString("-2.0e-0"), _dafny.SeqOfString("-.2e1"), _dafny.SeqOfString("-0.2e1"), _dafny.SeqOfString("-0.2e+1"), _dafny.SeqOfString("-0.02e2"), _dafny.SeqOfString("-20e-1"), _dafny.SeqOfString("-20.e-1"), _dafny.SeqOfString("-200.0e-2"))
}
func (_static *CompanionStruct_Default___) NEGATIVE__ONE() _dafny.Sequence {
	return _dafny.SeqOf(_dafny.SeqOfString("-1"), _dafny.SeqOfString("-1."), _dafny.SeqOfString("-1.0"), _dafny.SeqOfString("-1e0"), _dafny.SeqOfString("-1.e0"), _dafny.SeqOfString("-1.0e0"), _dafny.SeqOfString("-1.0e+0"), _dafny.SeqOfString("-1.0e-0"), _dafny.SeqOfString("-.1e1"), _dafny.SeqOfString("-0.1e1"), _dafny.SeqOfString("-0.1e+1"), _dafny.SeqOfString("-0.01e2"), _dafny.SeqOfString("-10e-1"), _dafny.SeqOfString("-10.e-1"), _dafny.SeqOfString("-100.0e-2"))
}
func (_static *CompanionStruct_Default___) ZERO() _dafny.Sequence {
	return _dafny.SeqOf(_dafny.SeqOfString("0"), _dafny.SeqOfString("+0"), _dafny.SeqOfString("-0"), _dafny.SeqOfString("0."), _dafny.SeqOfString("+0."), _dafny.SeqOfString("-0."), _dafny.SeqOfString("00"), _dafny.SeqOfString("+00"), _dafny.SeqOfString("-00"), _dafny.SeqOfString("0.0"), _dafny.SeqOfString("+0.0"), _dafny.SeqOfString("-0.0"), _dafny.SeqOfString("00.00"), _dafny.SeqOfString("+00.00"), _dafny.SeqOfString("-00.00"), _dafny.SeqOfString(".0"), _dafny.SeqOfString("+.0"), _dafny.SeqOfString("-.0"), _dafny.SeqOfString("0e0"), _dafny.SeqOfString("+0e0"), _dafny.SeqOfString("+0e+0"), _dafny.SeqOfString("+0e-0"), _dafny.SeqOfString("-0e0"), _dafny.SeqOfString("-0e+0"), _dafny.SeqOfString("-0e-0"), _dafny.SeqOfString("0e-99"), _dafny.SeqOfString("+0e-99"), _dafny.SeqOfString("-0e-99"), _dafny.SeqOfString("0e99"), _dafny.SeqOfString("+0e99"), _dafny.SeqOfString("-0e99"), _dafny.SeqOfString("0e+99"), _dafny.SeqOfString("+0e+99"), _dafny.SeqOfString("-0e+99"))
}
func (_static *CompanionStruct_Default___) ONE() _dafny.Sequence {
	return _dafny.SeqOf(_dafny.SeqOfString("1"), _dafny.SeqOfString("1."), _dafny.SeqOfString("1.0"), _dafny.SeqOfString("1e0"), _dafny.SeqOfString("1.e0"), _dafny.SeqOfString("1.0e0"), _dafny.SeqOfString("1.0e+0"), _dafny.SeqOfString("1.0e-0"), _dafny.SeqOfString(".1e1"), _dafny.SeqOfString("0.1e1"), _dafny.SeqOfString("0.1e+1"), _dafny.SeqOfString("0.01e2"), _dafny.SeqOfString("10e-1"), _dafny.SeqOfString("10.e-1"), _dafny.SeqOfString("100.0e-2"), _dafny.SeqOfString("+1"), _dafny.SeqOfString("+1."), _dafny.SeqOfString("+1.0"), _dafny.SeqOfString("+1e0"), _dafny.SeqOfString("+1.e0"), _dafny.SeqOfString("+1.0e0"), _dafny.SeqOfString("+1.0e+0"), _dafny.SeqOfString("+1.0e-0"), _dafny.SeqOfString("+.1e1"), _dafny.SeqOfString("+0.1e1"), _dafny.SeqOfString("+0.1e+1"), _dafny.SeqOfString("+0.01e2"), _dafny.SeqOfString("+10e-1"), _dafny.SeqOfString("+10.e-1"), _dafny.SeqOfString("+100.0e-2"))
}
func (_static *CompanionStruct_Default___) TWO() _dafny.Sequence {
	return _dafny.SeqOf(_dafny.SeqOfString("2"), _dafny.SeqOfString("2."), _dafny.SeqOfString("2.0"), _dafny.SeqOfString("2e0"), _dafny.SeqOfString("2.e0"), _dafny.SeqOfString("2.0e0"), _dafny.SeqOfString("2.0e+0"), _dafny.SeqOfString("2.0e-0"), _dafny.SeqOfString(".2e1"), _dafny.SeqOfString("0.2e1"), _dafny.SeqOfString("0.2e+1"), _dafny.SeqOfString("0.02e2"), _dafny.SeqOfString("20e-1"), _dafny.SeqOfString("20.e-1"), _dafny.SeqOfString("200.0e-2"), _dafny.SeqOfString("+2"), _dafny.SeqOfString("+2."), _dafny.SeqOfString("+2.0"), _dafny.SeqOfString("+2e0"), _dafny.SeqOfString("+2.e0"), _dafny.SeqOfString("+2.0e0"), _dafny.SeqOfString("+2.0e+0"), _dafny.SeqOfString("+2.0e-0"), _dafny.SeqOfString("+.2e1"), _dafny.SeqOfString("+0.2e1"), _dafny.SeqOfString("+0.2e+1"), _dafny.SeqOfString("+0.02e2"), _dafny.SeqOfString("+20e-1"), _dafny.SeqOfString("+20.e-1"), _dafny.SeqOfString("+200.0e-2"))
}

// End of class Default__
