// Package Sorting
// Dafny module Sorting compiled into Go

package Sorting

import (
	os "os"

	m__System "github.com/dafny-lang/DafnyRuntimeGo/v4/System_"
	_dafny "github.com/dafny-lang/DafnyRuntimeGo/v4/dafny"
	m_BoundedInts "github.com/dafny-lang/DafnyStandardLibGo/BoundedInts"
	m_DivInternals "github.com/dafny-lang/DafnyStandardLibGo/DivInternals"
	m_DivInternalsNonlinear "github.com/dafny-lang/DafnyStandardLibGo/DivInternalsNonlinear"
	m_DivMod "github.com/dafny-lang/DafnyStandardLibGo/DivMod"
	m_FileIO "github.com/dafny-lang/DafnyStandardLibGo/FileIO"
	m_Functions "github.com/dafny-lang/DafnyStandardLibGo/Functions"
	m_GeneralInternals "github.com/dafny-lang/DafnyStandardLibGo/GeneralInternals"
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
	return "Sorting.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) LexicographicByteSeqBelow(x _dafny.Sequence, y _dafny.Sequence) bool {
	return Companion_Default___.LexicographicByteSeqBelowAux(x, y, _dafny.Zero)
}
func (_static *CompanionStruct_Default___) LexicographicByteSeqBelowAux(x _dafny.Sequence, y _dafny.Sequence, n _dafny.Int) bool {
	return (((n).Cmp(_dafny.IntOfUint32((x).Cardinality())) == 0) || (((n).Cmp(_dafny.IntOfUint32((y).Cardinality())) != 0) && (((x).Select((n).Uint32()).(uint8)) < ((y).Select((n).Uint32()).(uint8))))) || ((((n).Cmp(_dafny.IntOfUint32((y).Cardinality())) != 0) && (((x).Select((n).Uint32()).(uint8)) == ((y).Select((n).Uint32()).(uint8)))) && (Companion_Default___.LexicographicByteSeqBelowAux(x, y, (n).Plus(_dafny.One))))
}
func (_static *CompanionStruct_Default___) SelectionSort(a _dafny.Array, below func(interface{}, interface{}) bool) {
	var _0_m _dafny.Int
	_ = _0_m
	_0_m = _dafny.Zero
	for (_0_m).Cmp(_dafny.ArrayLen((a), 0)) < 0 {
		var _1_mindex _dafny.Int
		_ = _1_mindex
		var _2_n _dafny.Int
		_ = _2_n
		var _rhs0 _dafny.Int = _0_m
		_ = _rhs0
		var _rhs1 _dafny.Int = (_0_m).Plus(_dafny.One)
		_ = _rhs1
		_1_mindex = _rhs0
		_2_n = _rhs1
		for (_2_n).Cmp(_dafny.ArrayLen((a), 0)) < 0 {
			if !((below)((a).ArrayGet1((_1_mindex).Int()), (a).ArrayGet1((_2_n).Int()))) {
				_1_mindex = _2_n
			}
			_2_n = (_2_n).Plus(_dafny.One)
		}
		var _rhs2 interface{} = (a).ArrayGet1((_1_mindex).Int())
		_ = _rhs2
		var _rhs3 interface{} = (a).ArrayGet1((_0_m).Int())
		_ = _rhs3
		var _lhs0 _dafny.Array = a
		_ = _lhs0
		var _lhs1 _dafny.Int = _0_m
		_ = _lhs1
		var _lhs2 _dafny.Array = a
		_ = _lhs2
		var _lhs3 _dafny.Int = _1_mindex
		_ = _lhs3
		(_lhs0).ArraySet1(_rhs2, (_lhs1).Int())
		(_lhs2).ArraySet1(_rhs3, (_lhs3).Int())
		_0_m = (_0_m).Plus(_dafny.One)
	}
}

// End of class Default__
