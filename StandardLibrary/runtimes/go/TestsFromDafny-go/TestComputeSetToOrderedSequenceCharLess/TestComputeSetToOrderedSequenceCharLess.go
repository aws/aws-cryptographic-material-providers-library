// Package TestComputeSetToOrderedSequenceCharLess
// Dafny module TestComputeSetToOrderedSequenceCharLess compiled into Go

package TestComputeSetToOrderedSequenceCharLess

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
	return "TestComputeSetToOrderedSequenceCharLess.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) CharLess(x _dafny.Char, y _dafny.Char) bool {
	return (x) < (y)
}
func (_static *CompanionStruct_Default___) CharGreater(x _dafny.Char, y _dafny.Char) bool {
	return (y) < (x)
}
func (_static *CompanionStruct_Default___) TestSetToOrderedSequenceEmpty() {
	var _0_output _dafny.Sequence
	_ = _0_output
	var _out0 _dafny.Sequence
	_ = _out0
	_out0 = m_SortedSets.SetToOrderedSequence(_dafny.SetOf(), func(coer0 func(_dafny.Char, _dafny.Char) bool) func(interface{}, interface{}) bool {
		return func(arg0 interface{}, arg1 interface{}) bool {
			return coer0(arg0.(_dafny.Char), arg1.(_dafny.Char))
		}
	}(Companion_Default___.CharLess))
	_0_output = _out0
	var _1_output2 _dafny.Sequence
	_ = _1_output2
	_1_output2 = m_SortedSets.SetToOrderedSequence2(_dafny.SetOf(), func(coer1 func(_dafny.Char, _dafny.Char) bool) func(interface{}, interface{}) bool {
		return func(arg2 interface{}, arg3 interface{}) bool {
			return coer1(arg2.(_dafny.Char), arg3.(_dafny.Char))
		}
	}(Companion_Default___.CharLess))
	var _2_expected _dafny.Sequence
	_ = _2_expected
	_2_expected = _dafny.SeqOf()
	if !(_dafny.Companion_Sequence_.Equal(_0_output, _2_expected)) {
		panic("test/TestComputeSetToOrderedSequenceCharLess.dfy(35,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(_1_output2, _2_expected)) {
		panic("test/TestComputeSetToOrderedSequenceCharLess.dfy(36,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestSetToOrderedSequenceOneItem() {
	var _0_a _dafny.Set
	_ = _0_a
	_0_a = _dafny.SetOf(_dafny.SeqOfString("a"))
	var _1_output _dafny.Sequence
	_ = _1_output
	var _out0 _dafny.Sequence
	_ = _out0
	_out0 = m_SortedSets.SetToOrderedSequence(_0_a, func(coer2 func(_dafny.Char, _dafny.Char) bool) func(interface{}, interface{}) bool {
		return func(arg4 interface{}, arg5 interface{}) bool {
			return coer2(arg4.(_dafny.Char), arg5.(_dafny.Char))
		}
	}(Companion_Default___.CharLess))
	_1_output = _out0
	var _2_output2 _dafny.Sequence
	_ = _2_output2
	_2_output2 = m_SortedSets.SetToOrderedSequence2(_0_a, func(coer3 func(_dafny.Char, _dafny.Char) bool) func(interface{}, interface{}) bool {
		return func(arg6 interface{}, arg7 interface{}) bool {
			return coer3(arg6.(_dafny.Char), arg7.(_dafny.Char))
		}
	}(Companion_Default___.CharLess))
	var _3_expected _dafny.Sequence
	_ = _3_expected
	_3_expected = _dafny.SeqOf(_dafny.SeqOfString("a"))
	if !(_dafny.Companion_Sequence_.Equal(_1_output, _3_expected)) {
		panic("test/TestComputeSetToOrderedSequenceCharLess.dfy(44,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(_2_output2, _3_expected)) {
		panic("test/TestComputeSetToOrderedSequenceCharLess.dfy(45,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestSetToOrderedSequenceSimple() {
	var _0_a _dafny.Set
	_ = _0_a
	_0_a = _dafny.SetOf(_dafny.SeqOfString("ac"), _dafny.SeqOfString("ab"))
	var _1_output _dafny.Sequence
	_ = _1_output
	var _out0 _dafny.Sequence
	_ = _out0
	_out0 = m_SortedSets.SetToOrderedSequence(_0_a, func(coer4 func(_dafny.Char, _dafny.Char) bool) func(interface{}, interface{}) bool {
		return func(arg8 interface{}, arg9 interface{}) bool {
			return coer4(arg8.(_dafny.Char), arg9.(_dafny.Char))
		}
	}(Companion_Default___.CharLess))
	_1_output = _out0
	var _2_output2 _dafny.Sequence
	_ = _2_output2
	_2_output2 = m_SortedSets.SetToOrderedSequence2(_0_a, func(coer5 func(_dafny.Char, _dafny.Char) bool) func(interface{}, interface{}) bool {
		return func(arg10 interface{}, arg11 interface{}) bool {
			return coer5(arg10.(_dafny.Char), arg11.(_dafny.Char))
		}
	}(Companion_Default___.CharLess))
	var _3_expected _dafny.Sequence
	_ = _3_expected
	_3_expected = _dafny.SeqOf(_dafny.SeqOfString("ab"), _dafny.SeqOfString("ac"))
	if !(_dafny.Companion_Sequence_.Equal(_1_output, _3_expected)) {
		panic("test/TestComputeSetToOrderedSequenceCharLess.dfy(53,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(_2_output2, _3_expected)) {
		panic("test/TestComputeSetToOrderedSequenceCharLess.dfy(54,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestSetToOrderedSequencePrefix() {
	var _0_a _dafny.Set
	_ = _0_a
	_0_a = _dafny.SetOf(_dafny.SeqOfString("abc"), _dafny.SeqOfString("ab"))
	var _1_output _dafny.Sequence
	_ = _1_output
	var _out0 _dafny.Sequence
	_ = _out0
	_out0 = m_SortedSets.SetToOrderedSequence(_0_a, func(coer6 func(_dafny.Char, _dafny.Char) bool) func(interface{}, interface{}) bool {
		return func(arg12 interface{}, arg13 interface{}) bool {
			return coer6(arg12.(_dafny.Char), arg13.(_dafny.Char))
		}
	}(Companion_Default___.CharLess))
	_1_output = _out0
	var _2_output2 _dafny.Sequence
	_ = _2_output2
	_2_output2 = m_SortedSets.SetToOrderedSequence2(_0_a, func(coer7 func(_dafny.Char, _dafny.Char) bool) func(interface{}, interface{}) bool {
		return func(arg14 interface{}, arg15 interface{}) bool {
			return coer7(arg14.(_dafny.Char), arg15.(_dafny.Char))
		}
	}(Companion_Default___.CharLess))
	var _3_expected _dafny.Sequence
	_ = _3_expected
	_3_expected = _dafny.SeqOf(_dafny.SeqOfString("ab"), _dafny.SeqOfString("abc"))
	if !(_dafny.Companion_Sequence_.Equal(_1_output, _3_expected)) {
		panic("test/TestComputeSetToOrderedSequenceCharLess.dfy(62,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(_2_output2, _3_expected)) {
		panic("test/TestComputeSetToOrderedSequenceCharLess.dfy(63,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestSetToOrderedSequenceComplex() {
	var _0_a _dafny.Set
	_ = _0_a
	_0_a = _dafny.SetOf(_dafny.SeqOfString("abc"), _dafny.SeqOfString("bbc"), _dafny.SeqOfString("ab"))
	var _1_output _dafny.Sequence
	_ = _1_output
	var _out0 _dafny.Sequence
	_ = _out0
	_out0 = m_SortedSets.SetToOrderedSequence(_0_a, func(coer8 func(_dafny.Char, _dafny.Char) bool) func(interface{}, interface{}) bool {
		return func(arg16 interface{}, arg17 interface{}) bool {
			return coer8(arg16.(_dafny.Char), arg17.(_dafny.Char))
		}
	}(Companion_Default___.CharLess))
	_1_output = _out0
	var _2_output2 _dafny.Sequence
	_ = _2_output2
	_2_output2 = m_SortedSets.SetToOrderedSequence2(_0_a, func(coer9 func(_dafny.Char, _dafny.Char) bool) func(interface{}, interface{}) bool {
		return func(arg18 interface{}, arg19 interface{}) bool {
			return coer9(arg18.(_dafny.Char), arg19.(_dafny.Char))
		}
	}(Companion_Default___.CharLess))
	var _3_expected _dafny.Sequence
	_ = _3_expected
	_3_expected = _dafny.SeqOf(_dafny.SeqOfString("ab"), _dafny.SeqOfString("abc"), _dafny.SeqOfString("bbc"))
	if !(_dafny.Companion_Sequence_.Equal(_1_output, _3_expected)) {
		panic("test/TestComputeSetToOrderedSequenceCharLess.dfy(71,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(_2_output2, _3_expected)) {
		panic("test/TestComputeSetToOrderedSequenceCharLess.dfy(72,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestSetToOrderedSequenceComplexReverse() {
	var _0_a _dafny.Set
	_ = _0_a
	_0_a = _dafny.SetOf(_dafny.SeqOfString("abc"), _dafny.SeqOfString("bbc"), _dafny.SeqOfString("ab"))
	var _1_output _dafny.Sequence
	_ = _1_output
	var _out0 _dafny.Sequence
	_ = _out0
	_out0 = m_SortedSets.SetToOrderedSequence(_0_a, func(coer10 func(_dafny.Char, _dafny.Char) bool) func(interface{}, interface{}) bool {
		return func(arg20 interface{}, arg21 interface{}) bool {
			return coer10(arg20.(_dafny.Char), arg21.(_dafny.Char))
		}
	}(Companion_Default___.CharGreater))
	_1_output = _out0
	var _2_output2 _dafny.Sequence
	_ = _2_output2
	_2_output2 = m_SortedSets.SetToOrderedSequence2(_0_a, func(coer11 func(_dafny.Char, _dafny.Char) bool) func(interface{}, interface{}) bool {
		return func(arg22 interface{}, arg23 interface{}) bool {
			return coer11(arg22.(_dafny.Char), arg23.(_dafny.Char))
		}
	}(Companion_Default___.CharGreater))
	var _3_expected _dafny.Sequence
	_ = _3_expected
	_3_expected = _dafny.SeqOf(_dafny.SeqOfString("bbc"), _dafny.SeqOfString("ab"), _dafny.SeqOfString("abc"))
	if !(_dafny.Companion_Sequence_.Equal(_1_output, _3_expected)) {
		panic("test/TestComputeSetToOrderedSequenceCharLess.dfy(80,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(_2_output2, _3_expected)) {
		panic("test/TestComputeSetToOrderedSequenceCharLess.dfy(81,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestSetSequence() {
	var _0_a _dafny.Set
	_ = _0_a
	_0_a = _dafny.SetOf(_dafny.SeqOfString("abc"), _dafny.SeqOfString("bbc"), _dafny.SeqOfString("ab"))
	var _1_output _dafny.Sequence
	_ = _1_output
	_1_output = m_SortedSets.SetToSequence(_0_a)
	if !((_dafny.MultiSetFromSeq(_1_output)).Equals(_dafny.MultiSetFromSet(_0_a))) {
		panic("test/TestComputeSetToOrderedSequenceCharLess.dfy(87,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestSetToOrderedComplexUnicode() {
	var _0_a _dafny.Set
	_ = _0_a
	_0_a = _dafny.SetOf(_dafny.SeqOfChars(55297, 56375), _dafny.SeqOfString("&"), _dafny.SeqOfChars(1033), _dafny.SeqOfChars(5952), _dafny.SeqOfChars(55356, 56481), _dafny.SeqOfChars(65377), _dafny.SeqOfChars(55296, 56322))
	var _1_output _dafny.Sequence
	_ = _1_output
	var _out0 _dafny.Sequence
	_ = _out0
	_out0 = m_SortedSets.SetToOrderedSequence(_0_a, func(coer12 func(_dafny.Char, _dafny.Char) bool) func(interface{}, interface{}) bool {
		return func(arg24 interface{}, arg25 interface{}) bool {
			return coer12(arg24.(_dafny.Char), arg25.(_dafny.Char))
		}
	}(Companion_Default___.CharLess))
	_1_output = _out0
	var _2_output2 _dafny.Sequence
	_ = _2_output2
	_2_output2 = m_SortedSets.SetToOrderedSequence2(_0_a, func(coer13 func(_dafny.Char, _dafny.Char) bool) func(interface{}, interface{}) bool {
		return func(arg26 interface{}, arg27 interface{}) bool {
			return coer13(arg26.(_dafny.Char), arg27.(_dafny.Char))
		}
	}(Companion_Default___.CharLess))
	var _3_expected _dafny.Sequence
	_ = _3_expected
	_3_expected = _dafny.SeqOf(_dafny.SeqOfString("&"), _dafny.SeqOfChars(1033), _dafny.SeqOfChars(5952), _dafny.SeqOfChars(55296, 56322), _dafny.SeqOfChars(55297, 56375), _dafny.SeqOfChars(55356, 56481), _dafny.SeqOfChars(65377))
	if !(_dafny.Companion_Sequence_.Equal(_1_output, _3_expected)) {
		panic("test/TestComputeSetToOrderedSequenceCharLess.dfy(124,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(_2_output2, _3_expected)) {
		panic("test/TestComputeSetToOrderedSequenceCharLess.dfy(125,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}

// End of class Default__
