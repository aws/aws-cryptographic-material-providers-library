// Package StandardLibrary_String
// Dafny module StandardLibrary_String compiled into Go

package StandardLibrary_String

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
	m_StandardLibraryInterop "github.com/dafny-lang/DafnyStandardLibGo/StandardLibraryInterop"
	m_StandardLibrary_UInt "github.com/dafny-lang/DafnyStandardLibGo/StandardLibrary_UInt"
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
	return "StandardLibrary_String.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) Int2Digits(n _dafny.Int, base _dafny.Int) _dafny.Sequence {
	var _0___accumulator _dafny.Sequence = _dafny.SeqOf()
	_ = _0___accumulator
	goto TAIL_CALL_START
TAIL_CALL_START:
	if (n).Sign() == 0 {
		return _dafny.Companion_Sequence_.Concatenate(_dafny.SeqOf(), _0___accumulator)
	} else {
		_0___accumulator = _dafny.Companion_Sequence_.Concatenate(_dafny.SeqOf((n).Modulo(base)), _0___accumulator)
		var _in0 _dafny.Int = (n).DivBy(base)
		_ = _in0
		var _in1 _dafny.Int = base
		_ = _in1
		n = _in0
		base = _in1
		goto TAIL_CALL_START
	}
}
func (_static *CompanionStruct_Default___) Digits2String(digits _dafny.Sequence, chars _dafny.Sequence) _dafny.Sequence {
	var _0___accumulator _dafny.Sequence = _dafny.SeqOfChars()
	_ = _0___accumulator
	goto TAIL_CALL_START
TAIL_CALL_START:
	if _dafny.Companion_Sequence_.Equal(digits, _dafny.SeqOf()) {
		return _dafny.Companion_Sequence_.Concatenate(_0___accumulator, _dafny.SeqOfString(""))
	} else {
		_0___accumulator = _dafny.Companion_Sequence_.Concatenate(_0___accumulator, _dafny.SeqOfChars((chars).Select(((digits).Select(0).(_dafny.Int)).Uint32()).(_dafny.Char)))
		var _in0 _dafny.Sequence = (digits).Drop(1)
		_ = _in0
		var _in1 _dafny.Sequence = chars
		_ = _in1
		digits = _in0
		chars = _in1
		goto TAIL_CALL_START
	}
}
func (_static *CompanionStruct_Default___) Int2String(n _dafny.Int, chars _dafny.Sequence) _dafny.Sequence {
	var _0_base _dafny.Int = _dafny.IntOfUint32((chars).Cardinality())
	_ = _0_base
	if (n).Sign() == 0 {
		return _dafny.SeqOfString("0")
	} else if (n).Sign() == 1 {
		return Companion_Default___.Digits2String(Companion_Default___.Int2Digits(n, _0_base), chars)
	} else {
		return _dafny.Companion_Sequence_.Concatenate(_dafny.SeqOfString("-"), Companion_Default___.Digits2String(Companion_Default___.Int2Digits((_dafny.Zero).Minus(n), _0_base), chars))
	}
}
func (_static *CompanionStruct_Default___) Base10Int2String(n _dafny.Int) _dafny.Sequence {
	return Companion_Default___.Int2String(n, Companion_Default___.Base10())
}
func (_static *CompanionStruct_Default___) Base10() _dafny.Sequence {
	return _dafny.SeqOfChars(_dafny.Char('0'), _dafny.Char('1'), _dafny.Char('2'), _dafny.Char('3'), _dafny.Char('4'), _dafny.Char('5'), _dafny.Char('6'), _dafny.Char('7'), _dafny.Char('8'), _dafny.Char('9'))
}

// End of class Default__
