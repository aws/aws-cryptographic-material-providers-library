// Package TestComputeSetToOrderedSequenceUInt8Less
// Dafny module TestComputeSetToOrderedSequenceUInt8Less compiled into Go

package TestComputeSetToOrderedSequenceUInt8Less

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
	m_SortedSets "github.com/dafny-lang/DafnyStandardLibGo/SortedSets"
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
	return "TestComputeSetToOrderedSequenceUInt8Less.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) UInt8Greater(x uint8, y uint8) bool {
	return (y) < (x)
}
func (_static *CompanionStruct_Default___) TestSetToOrderedSequenceEmpty() {
	var _0_output _dafny.Sequence
	_ = _0_output
	var _out0 _dafny.Sequence
	_ = _out0
	_out0 = m_SortedSets.SetToOrderedSequence(_dafny.SetOf(), func(coer14 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
		return func(arg28 interface{}, arg29 interface{}) bool {
			return coer14(arg28.(uint8), arg29.(uint8))
		}
	}(m_StandardLibrary_UInt.Companion_Default___.UInt8Less))
	_0_output = _out0
	var _1_output2 _dafny.Sequence
	_ = _1_output2
	_1_output2 = m_SortedSets.SetToOrderedSequence2(_dafny.SetOf(), func(coer15 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
		return func(arg30 interface{}, arg31 interface{}) bool {
			return coer15(arg30.(uint8), arg31.(uint8))
		}
	}(m_StandardLibrary_UInt.Companion_Default___.UInt8Less))
	var _2_expected _dafny.Sequence
	_ = _2_expected
	_2_expected = _dafny.SeqOf()
	if !(_dafny.Companion_Sequence_.Equal(_0_output, _2_expected)) {
		panic("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(29,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(_1_output2, _2_expected)) {
		panic("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(30,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestSetToOrderedSequenceOneItem() {
	var _0_a _dafny.Set
	_ = _0_a
	_0_a = _dafny.SetOf(_dafny.SeqOf(uint8(0)))
	var _1_output _dafny.Sequence
	_ = _1_output
	var _out0 _dafny.Sequence
	_ = _out0
	_out0 = m_SortedSets.SetToOrderedSequence(_0_a, func(coer16 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
		return func(arg32 interface{}, arg33 interface{}) bool {
			return coer16(arg32.(uint8), arg33.(uint8))
		}
	}(m_StandardLibrary_UInt.Companion_Default___.UInt8Less))
	_1_output = _out0
	var _2_output2 _dafny.Sequence
	_ = _2_output2
	_2_output2 = m_SortedSets.SetToOrderedSequence2(_0_a, func(coer17 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
		return func(arg34 interface{}, arg35 interface{}) bool {
			return coer17(arg34.(uint8), arg35.(uint8))
		}
	}(m_StandardLibrary_UInt.Companion_Default___.UInt8Less))
	var _3_expected _dafny.Sequence
	_ = _3_expected
	_3_expected = _dafny.SeqOf(_dafny.SeqOf(uint8(0)))
	if !(_dafny.Companion_Sequence_.Equal(_1_output, _3_expected)) {
		panic("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(38,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(_2_output2, _3_expected)) {
		panic("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(39,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestSetToOrderedSequenceSimple() {
	var _0_a _dafny.Set
	_ = _0_a
	_0_a = _dafny.SetOf(_dafny.SeqOf(uint8(0), uint8(2)), _dafny.SeqOf(uint8(0), uint8(1)))
	var _1_output _dafny.Sequence
	_ = _1_output
	var _out0 _dafny.Sequence
	_ = _out0
	_out0 = m_SortedSets.SetToOrderedSequence(_0_a, func(coer18 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
		return func(arg36 interface{}, arg37 interface{}) bool {
			return coer18(arg36.(uint8), arg37.(uint8))
		}
	}(m_StandardLibrary_UInt.Companion_Default___.UInt8Less))
	_1_output = _out0
	var _2_output2 _dafny.Sequence
	_ = _2_output2
	_2_output2 = m_SortedSets.SetToOrderedSequence2(_0_a, func(coer19 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
		return func(arg38 interface{}, arg39 interface{}) bool {
			return coer19(arg38.(uint8), arg39.(uint8))
		}
	}(m_StandardLibrary_UInt.Companion_Default___.UInt8Less))
	var _3_expected _dafny.Sequence
	_ = _3_expected
	_3_expected = _dafny.SeqOf(_dafny.SeqOf(uint8(0), uint8(1)), _dafny.SeqOf(uint8(0), uint8(2)))
	if !(_dafny.Companion_Sequence_.Equal(_1_output, _3_expected)) {
		panic("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(47,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(_2_output2, _3_expected)) {
		panic("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(48,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestSetToOrderedSequencePrefix() {
	var _0_a _dafny.Set
	_ = _0_a
	_0_a = _dafny.SetOf(_dafny.SeqOf(uint8(0), uint8(1), uint8(2)), _dafny.SeqOf(uint8(0), uint8(1)))
	var _1_output _dafny.Sequence
	_ = _1_output
	var _out0 _dafny.Sequence
	_ = _out0
	_out0 = m_SortedSets.SetToOrderedSequence(_0_a, func(coer20 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
		return func(arg40 interface{}, arg41 interface{}) bool {
			return coer20(arg40.(uint8), arg41.(uint8))
		}
	}(m_StandardLibrary_UInt.Companion_Default___.UInt8Less))
	_1_output = _out0
	var _2_output2 _dafny.Sequence
	_ = _2_output2
	_2_output2 = m_SortedSets.SetToOrderedSequence2(_0_a, func(coer21 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
		return func(arg42 interface{}, arg43 interface{}) bool {
			return coer21(arg42.(uint8), arg43.(uint8))
		}
	}(m_StandardLibrary_UInt.Companion_Default___.UInt8Less))
	var _3_expected _dafny.Sequence
	_ = _3_expected
	_3_expected = _dafny.SeqOf(_dafny.SeqOf(uint8(0), uint8(1)), _dafny.SeqOf(uint8(0), uint8(1), uint8(2)))
	if !(_dafny.Companion_Sequence_.Equal(_1_output, _3_expected)) {
		panic("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(56,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(_2_output2, _3_expected)) {
		panic("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(57,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestSetToOrderedSequenceComplex() {
	var _0_a _dafny.Set
	_ = _0_a
	_0_a = _dafny.SetOf(_dafny.SeqOf(uint8(0), uint8(1), uint8(2)), _dafny.SeqOf(uint8(1), uint8(1), uint8(2)), _dafny.SeqOf(uint8(0), uint8(1)))
	var _1_output _dafny.Sequence
	_ = _1_output
	var _out0 _dafny.Sequence
	_ = _out0
	_out0 = m_SortedSets.SetToOrderedSequence(_0_a, func(coer22 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
		return func(arg44 interface{}, arg45 interface{}) bool {
			return coer22(arg44.(uint8), arg45.(uint8))
		}
	}(m_StandardLibrary_UInt.Companion_Default___.UInt8Less))
	_1_output = _out0
	var _2_output2 _dafny.Sequence
	_ = _2_output2
	_2_output2 = m_SortedSets.SetToOrderedSequence2(_0_a, func(coer23 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
		return func(arg46 interface{}, arg47 interface{}) bool {
			return coer23(arg46.(uint8), arg47.(uint8))
		}
	}(m_StandardLibrary_UInt.Companion_Default___.UInt8Less))
	var _3_expected _dafny.Sequence
	_ = _3_expected
	_3_expected = _dafny.SeqOf(_dafny.SeqOf(uint8(0), uint8(1)), _dafny.SeqOf(uint8(0), uint8(1), uint8(2)), _dafny.SeqOf(uint8(1), uint8(1), uint8(2)))
	if !(_dafny.Companion_Sequence_.Equal(_1_output, _3_expected)) {
		panic("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(65,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(_2_output2, _3_expected)) {
		panic("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(66,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestSetToOrderedSequenceComplexReverse() {
	var _0_a _dafny.Set
	_ = _0_a
	_0_a = _dafny.SetOf(_dafny.SeqOf(uint8(0), uint8(1), uint8(2)), _dafny.SeqOf(uint8(1), uint8(1), uint8(2)), _dafny.SeqOf(uint8(0), uint8(1)))
	var _1_output _dafny.Sequence
	_ = _1_output
	var _out0 _dafny.Sequence
	_ = _out0
	_out0 = m_SortedSets.SetToOrderedSequence(_0_a, func(coer24 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
		return func(arg48 interface{}, arg49 interface{}) bool {
			return coer24(arg48.(uint8), arg49.(uint8))
		}
	}(Companion_Default___.UInt8Greater))
	_1_output = _out0
	var _2_output2 _dafny.Sequence
	_ = _2_output2
	_2_output2 = m_SortedSets.SetToOrderedSequence2(_0_a, func(coer25 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
		return func(arg50 interface{}, arg51 interface{}) bool {
			return coer25(arg50.(uint8), arg51.(uint8))
		}
	}(Companion_Default___.UInt8Greater))
	var _3_expected _dafny.Sequence
	_ = _3_expected
	_3_expected = _dafny.SeqOf(_dafny.SeqOf(uint8(1), uint8(1), uint8(2)), _dafny.SeqOf(uint8(0), uint8(1)), _dafny.SeqOf(uint8(0), uint8(1), uint8(2)))
	if !(_dafny.Companion_Sequence_.Equal(_1_output, _3_expected)) {
		panic("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(74,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(_2_output2, _3_expected)) {
		panic("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(75,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestSetSequence() {
	var _0_a _dafny.Set
	_ = _0_a
	_0_a = _dafny.SetOf(_dafny.SeqOf(_dafny.Zero, _dafny.One, _dafny.IntOfInt64(2)), _dafny.SeqOf(_dafny.One, _dafny.One, _dafny.IntOfInt64(2)), _dafny.SeqOf(_dafny.Zero, _dafny.One))
	var _1_output _dafny.Sequence
	_ = _1_output
	_1_output = m_SortedSets.SetToSequence(_0_a)
	if !((_dafny.MultiSetFromSeq(_1_output)).Equals(_dafny.MultiSetFromSet(_0_a))) {
		panic("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(81,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestSetToOrderedSequenceManyItems() {
	var _0_a _dafny.Set
	_ = _0_a
	_0_a = func() _dafny.Set {
		var _coll0 = _dafny.NewBuilder()
		_ = _coll0
		for _iter3 := _dafny.Iterate(m_BoundedInts.Companion_Uint16_.IntegerRange(_dafny.Zero, m_BoundedInts.Companion_Default___.TWO__TO__THE__16())); ; {
			_compr_0, _ok3 := _iter3()
			if !_ok3 {
				break
			}
			var _1_x uint16
			_1_x = interface{}(_compr_0).(uint16)
			if true {
				if ((uint16(0)) <= (_1_x)) && ((_1_x) < (uint16(65535))) {
					_coll0.Add(m_StandardLibrary_UInt.Companion_Default___.UInt16ToSeq(_1_x))
				}
			}
		}
		return _coll0.ToSet()
	}()
	var _2_output _dafny.Sequence
	_ = _2_output
	var _out0 _dafny.Sequence
	_ = _out0
	_out0 = m_SortedSets.SetToOrderedSequence(_0_a, func(coer26 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
		return func(arg52 interface{}, arg53 interface{}) bool {
			return coer26(arg52.(uint8), arg53.(uint8))
		}
	}(m_StandardLibrary_UInt.Companion_Default___.UInt8Less))
	_2_output = _out0
	var _3_output2 _dafny.Sequence
	_ = _3_output2
	_3_output2 = m_SortedSets.SetToOrderedSequence2(_0_a, func(coer27 func(uint8, uint8) bool) func(interface{}, interface{}) bool {
		return func(arg54 interface{}, arg55 interface{}) bool {
			return coer27(arg54.(uint8), arg55.(uint8))
		}
	}(m_StandardLibrary_UInt.Companion_Default___.UInt8Less))
	var _4_expected _dafny.Sequence
	_ = _4_expected
	_4_expected = _dafny.SeqCreate(65535, func(coer28 func(_dafny.Int) _dafny.Sequence) func(_dafny.Int) interface{} {
		return func(arg56 _dafny.Int) interface{} {
			return coer28(arg56)
		}
	}(func(_5_i _dafny.Int) _dafny.Sequence {
		return m_StandardLibrary_UInt.Companion_Default___.UInt16ToSeq((_5_i).Uint16())
	}))
	if !(_dafny.Companion_Sequence_.Equal(_2_output, _4_expected)) {
		panic("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(89,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(_3_output2, _4_expected)) {
		panic("test/TestComputeSetToOrderedSequenceUInt8Less.dfy(90,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}

// End of class Default__
