// Package JSON_Utils_Lexers_Strings
// Dafny module JSON_Utils_Lexers_Strings compiled into Go

package JSON_Utils_Lexers_Strings

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
	m_JSON_Utils_Lexers_Core "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Lexers_Core"
	m_JSON_Utils_Views_Core "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Views_Core"
	m_JSON_Utils_Views_Writers "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Views_Writers"
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
var _ m_JSON_Utils_Views_Core.Dummy__
var _ m_JSON_Utils_Views_Writers.Dummy__
var _ m_JSON_Utils_Lexers_Core.Dummy__

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
	return "JSON_Utils_Lexers_Strings.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) StringBody(escaped bool, byte_ int16) m_JSON_Utils_Lexers_Core.LexerResult {
	if (byte_) == (int16(_dafny.Char('\\'))) {
		return m_JSON_Utils_Lexers_Core.Companion_LexerResult_.Create_Partial_(!(escaped))
	} else if ((byte_) == (int16(_dafny.Char('"')))) && (!(escaped)) {
		return m_JSON_Utils_Lexers_Core.Companion_LexerResult_.Create_Accept_()
	} else {
		return m_JSON_Utils_Lexers_Core.Companion_LexerResult_.Create_Partial_(false)
	}
}
func (_static *CompanionStruct_Default___) String(st StringLexerState, byte_ int16) m_JSON_Utils_Lexers_Core.LexerResult {
	var _source0 StringLexerState = st
	_ = _source0
	{
		if _source0.Is_Start() {
			if (byte_) == (int16(_dafny.Char('"'))) {
				return m_JSON_Utils_Lexers_Core.Companion_LexerResult_.Create_Partial_(Companion_StringLexerState_.Create_Body_(false))
			} else {
				return m_JSON_Utils_Lexers_Core.Companion_LexerResult_.Create_Reject_(_dafny.SeqOfString("String must start with double quote"))
			}
		}
	}
	{
		if _source0.Is_End() {
			return m_JSON_Utils_Lexers_Core.Companion_LexerResult_.Create_Accept_()
		}
	}
	{
		var _0_escaped bool = _source0.Get_().(StringLexerState_Body).Escaped
		_ = _0_escaped
		if (byte_) == (int16(_dafny.Char('\\'))) {
			return m_JSON_Utils_Lexers_Core.Companion_LexerResult_.Create_Partial_(Companion_StringLexerState_.Create_Body_(!(_0_escaped)))
		} else if ((byte_) == (int16(_dafny.Char('"')))) && (!(_0_escaped)) {
			return m_JSON_Utils_Lexers_Core.Companion_LexerResult_.Create_Partial_(Companion_StringLexerState_.Create_End_())
		} else {
			return m_JSON_Utils_Lexers_Core.Companion_LexerResult_.Create_Partial_(Companion_StringLexerState_.Create_Body_(false))
		}
	}
}
func (_static *CompanionStruct_Default___) StringBodyLexerStart() bool {
	return false
}
func (_static *CompanionStruct_Default___) StringLexerStart() StringLexerState {
	return Companion_StringLexerState_.Create_Start_()
}

// End of class Default__

// Definition of datatype StringLexerState
type StringLexerState struct {
	Data_StringLexerState_
}

func (_this StringLexerState) Get_() Data_StringLexerState_ {
	return _this.Data_StringLexerState_
}

type Data_StringLexerState_ interface {
	isStringLexerState()
}

type CompanionStruct_StringLexerState_ struct {
}

var Companion_StringLexerState_ = CompanionStruct_StringLexerState_{}

type StringLexerState_Start struct {
}

func (StringLexerState_Start) isStringLexerState() {}

func (CompanionStruct_StringLexerState_) Create_Start_() StringLexerState {
	return StringLexerState{StringLexerState_Start{}}
}

func (_this StringLexerState) Is_Start() bool {
	_, ok := _this.Get_().(StringLexerState_Start)
	return ok
}

type StringLexerState_Body struct {
	Escaped bool
}

func (StringLexerState_Body) isStringLexerState() {}

func (CompanionStruct_StringLexerState_) Create_Body_(Escaped bool) StringLexerState {
	return StringLexerState{StringLexerState_Body{Escaped}}
}

func (_this StringLexerState) Is_Body() bool {
	_, ok := _this.Get_().(StringLexerState_Body)
	return ok
}

type StringLexerState_End struct {
}

func (StringLexerState_End) isStringLexerState() {}

func (CompanionStruct_StringLexerState_) Create_End_() StringLexerState {
	return StringLexerState{StringLexerState_End{}}
}

func (_this StringLexerState) Is_End() bool {
	_, ok := _this.Get_().(StringLexerState_End)
	return ok
}

func (CompanionStruct_StringLexerState_) Default() StringLexerState {
	return Companion_StringLexerState_.Create_Start_()
}

func (_this StringLexerState) Dtor_escaped() bool {
	return _this.Get_().(StringLexerState_Body).Escaped
}

func (_this StringLexerState) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case StringLexerState_Start:
		{
			return "Strings.StringLexerState.Start"
		}
	case StringLexerState_Body:
		{
			return "Strings.StringLexerState.Body" + "(" + _dafny.String(data.Escaped) + ")"
		}
	case StringLexerState_End:
		{
			return "Strings.StringLexerState.End"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this StringLexerState) Equals(other StringLexerState) bool {
	switch data1 := _this.Get_().(type) {
	case StringLexerState_Start:
		{
			_, ok := other.Get_().(StringLexerState_Start)
			return ok
		}
	case StringLexerState_Body:
		{
			data2, ok := other.Get_().(StringLexerState_Body)
			return ok && data1.Escaped == data2.Escaped
		}
	case StringLexerState_End:
		{
			_, ok := other.Get_().(StringLexerState_End)
			return ok
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this StringLexerState) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(StringLexerState)
	return ok && _this.Equals(typed)
}

func Type_StringLexerState_() _dafny.TypeDescriptor {
	return type_StringLexerState_{}
}

type type_StringLexerState_ struct {
}

func (_this type_StringLexerState_) Default() interface{} {
	return Companion_StringLexerState_.Default()
}

func (_this type_StringLexerState_) String() string {
	return "JSON_Utils_Lexers_Strings.StringLexerState"
}
func (_this StringLexerState) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = StringLexerState{}

// End of datatype StringLexerState
