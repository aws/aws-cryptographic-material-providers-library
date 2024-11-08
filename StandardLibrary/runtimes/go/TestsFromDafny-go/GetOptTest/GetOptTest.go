// Package GetOptTest
// Dafny module GetOptTest compiled into Go

package GetOptTest

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
	return "GetOptTest.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) TestEmpty() {
	var _0_MyOptions m_GetOpt.Options
	_ = _0_MyOptions
	_0_MyOptions = m_GetOpt.Companion_Options_.Create_Options_(_dafny.SeqOfString("MyProg"), _dafny.SeqOfString("does stuff"), _dafny.SeqOf(m_GetOpt.Companion_Param_.Create_Flag_(_dafny.SeqOfString("foo"), _dafny.SeqOfString("helpText"), m_GetOpt.Companion_Default___.NullChar(), false, false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf()), m_GetOpt.Companion_Param_.Create_Opt_(_dafny.SeqOfString("bar"), _dafny.SeqOfString("helpText"), _dafny.SeqOfString("arg"), m_GetOpt.Companion_Default___.NullChar(), m_GetOpt.Companion_Unused_.Create_UnusedOk_(), false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf(), m_GetOpt.Companion_Tri_.Create_No_()), m_GetOpt.Companion_Param_.Create_Opt_(_dafny.SeqOfString("two"), _dafny.SeqOfString("helpText"), _dafny.SeqOfString("arg"), _dafny.Char('t'), m_GetOpt.Companion_Unused_.Create_UnusedOk_(), false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf(), m_GetOpt.Companion_Tri_.Create_No_()), m_GetOpt.Companion_Param_.Create_Flag_(_dafny.SeqOfString("six"), _dafny.SeqOfString("helpText"), _dafny.Char('s'), false, false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf())))
	var _1_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_GetOpt.Companion_Parsed_.Default())
	_ = _1_valueOrError0
	_1_valueOrError0 = m_GetOpt.Companion_Default___.GetOptions(_0_MyOptions, _dafny.SeqOf(_dafny.SeqOfString("cmd")))
	if !(!((_1_valueOrError0).IsFailure())) {
		panic("test/GetOpt.dfy(20,13): " + (_1_valueOrError0).String())
	}
	var _2_x m_GetOpt.Parsed
	_ = _2_x
	_2_x = (_1_valueOrError0).Extract().(m_GetOpt.Parsed)
	if !(_dafny.Companion_Sequence_.Equal((_2_x).Dtor_params(), _dafny.SeqOf())) {
		panic("test/GetOpt.dfy(21,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal((_2_x).Dtor_files(), _dafny.SeqOf())) {
		panic("test/GetOpt.dfy(22,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestShort() {
	var _0_MyOptions m_GetOpt.Options
	_ = _0_MyOptions
	_0_MyOptions = m_GetOpt.Companion_Options_.Create_Options_(_dafny.SeqOfString("MyProg"), _dafny.SeqOfString("does stuff"), _dafny.SeqOf(m_GetOpt.Companion_Param_.Create_Flag_(_dafny.SeqOfString("foo"), _dafny.SeqOfString("helpText"), m_GetOpt.Companion_Default___.NullChar(), false, false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf()), m_GetOpt.Companion_Param_.Create_Opt_(_dafny.SeqOfString("bar"), _dafny.SeqOfString("helpText"), _dafny.SeqOfString("arg"), m_GetOpt.Companion_Default___.NullChar(), m_GetOpt.Companion_Unused_.Create_UnusedOk_(), false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf(), m_GetOpt.Companion_Tri_.Create_No_()), m_GetOpt.Companion_Param_.Create_Opt_(_dafny.SeqOfString("two"), _dafny.SeqOfString("helpText"), _dafny.SeqOfString("arg"), _dafny.Char('t'), m_GetOpt.Companion_Unused_.Create_UnusedOk_(), false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf(), m_GetOpt.Companion_Tri_.Create_No_()), m_GetOpt.Companion_Param_.Create_Flag_(_dafny.SeqOfString("six"), _dafny.SeqOfString("helpText"), _dafny.Char('s'), false, false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf()), m_GetOpt.Companion_Param_.Create_Flag_(_dafny.SeqOfString("seven"), _dafny.SeqOfString("helpText"), _dafny.Char('v'), false, false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf())))
	var _1_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_GetOpt.Companion_Parsed_.Default())
	_ = _1_valueOrError0
	_1_valueOrError0 = m_GetOpt.Companion_Default___.GetOptions(_0_MyOptions, _dafny.SeqOf(_dafny.SeqOfString("cmd"), _dafny.SeqOfString("-svsttt"), _dafny.SeqOfString("-t"), _dafny.SeqOfString("stuff"), _dafny.SeqOfString("-v")))
	if !(!((_1_valueOrError0).IsFailure())) {
		panic("test/GetOpt.dfy(34,13): " + (_1_valueOrError0).String())
	}
	var _2_x m_GetOpt.Parsed
	_ = _2_x
	_2_x = (_1_valueOrError0).Extract().(m_GetOpt.Parsed)
	if !(_dafny.Companion_Sequence_.Equal((_2_x).Dtor_params(), _dafny.SeqOf(m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("six"), m_Wrappers.Companion_Option_.Create_None_()), m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("seven"), m_Wrappers.Companion_Option_.Create_None_()), m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("six"), m_Wrappers.Companion_Option_.Create_None_()), m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("two"), m_Wrappers.Companion_Option_.Create_Some_(_dafny.SeqOfString("tt"))), m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("two"), m_Wrappers.Companion_Option_.Create_Some_(_dafny.SeqOfString("stuff"))), m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("seven"), m_Wrappers.Companion_Option_.Create_None_())))) {
		panic("test/GetOpt.dfy(35,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal((_2_x).Dtor_files(), _dafny.SeqOf())) {
		panic("test/GetOpt.dfy(37,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestLong() {
	var _0_MyOptions m_GetOpt.Options
	_ = _0_MyOptions
	_0_MyOptions = m_GetOpt.Companion_Options_.Create_Options_(_dafny.SeqOfString("MyProg"), _dafny.SeqOfString("does stuff"), _dafny.SeqOf(m_GetOpt.Companion_Param_.Create_Flag_(_dafny.SeqOfString("foo"), _dafny.SeqOfString("helpText"), m_GetOpt.Companion_Default___.NullChar(), false, false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf()), m_GetOpt.Companion_Param_.Create_Opt_(_dafny.SeqOfString("bar"), _dafny.SeqOfString("helpText"), _dafny.SeqOfString("arg"), m_GetOpt.Companion_Default___.NullChar(), m_GetOpt.Companion_Unused_.Create_UnusedOk_(), false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf(), m_GetOpt.Companion_Tri_.Create_No_()), m_GetOpt.Companion_Param_.Create_Opt_(_dafny.SeqOfString("two"), _dafny.SeqOfString("helpText"), _dafny.SeqOfString("arg"), _dafny.Char('t'), m_GetOpt.Companion_Unused_.Create_UnusedOk_(), false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf(), m_GetOpt.Companion_Tri_.Create_No_()), m_GetOpt.Companion_Param_.Create_Flag_(_dafny.SeqOfString("six"), _dafny.SeqOfString("helpText"), _dafny.Char('s'), false, false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf()), m_GetOpt.Companion_Param_.Create_Flag_(_dafny.SeqOfString("seven"), _dafny.SeqOfString("helpText"), _dafny.Char('v'), false, false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf())))
	var _1_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_GetOpt.Companion_Parsed_.Default())
	_ = _1_valueOrError0
	_1_valueOrError0 = m_GetOpt.Companion_Default___.GetOptions(_0_MyOptions, _dafny.SeqOf(_dafny.SeqOfString("cmd"), _dafny.SeqOfString("--foo"), _dafny.SeqOfString("file1"), _dafny.SeqOfString("--bar"), _dafny.SeqOfString("bar1"), _dafny.SeqOfString("-"), _dafny.SeqOfString("--bar=bar2=bar3"), _dafny.SeqOfString("file3"), _dafny.SeqOfString("--"), _dafny.SeqOfString("--this"), _dafny.SeqOfString("-that")))
	if !(!((_1_valueOrError0).IsFailure())) {
		panic("test/GetOpt.dfy(49,13): " + (_1_valueOrError0).String())
	}
	var _2_x m_GetOpt.Parsed
	_ = _2_x
	_2_x = (_1_valueOrError0).Extract().(m_GetOpt.Parsed)
	if !(_dafny.Companion_Sequence_.Equal((_2_x).Dtor_params(), _dafny.SeqOf(m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("foo"), m_Wrappers.Companion_Option_.Create_None_()), m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("bar"), m_Wrappers.Companion_Option_.Create_Some_(_dafny.SeqOfString("bar1"))), m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("bar"), m_Wrappers.Companion_Option_.Create_Some_(_dafny.SeqOfString("bar2=bar3")))))) {
		panic("test/GetOpt.dfy(50,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal((_2_x).Dtor_files(), _dafny.SeqOf(_dafny.SeqOfString("file1"), _dafny.SeqOfString("-"), _dafny.SeqOfString("file3"), _dafny.SeqOfString("--this"), _dafny.SeqOfString("-that")))) {
		panic("test/GetOpt.dfy(51,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestRequired() {
	var _0_MyOptions m_GetOpt.Options
	_ = _0_MyOptions
	_0_MyOptions = m_GetOpt.Companion_Options_.Create_Options_(_dafny.SeqOfString("MyProg"), _dafny.SeqOfString("does stuff"), _dafny.SeqOf(m_GetOpt.Companion_Param_.Create_Flag_(_dafny.SeqOfString("foo"), _dafny.SeqOfString("helpText"), m_GetOpt.Companion_Default___.NullChar(), false, false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf()), m_GetOpt.Companion_Param_.Create_Opt_(_dafny.SeqOfString("bar"), _dafny.SeqOfString("helpText"), _dafny.SeqOfString("arg"), m_GetOpt.Companion_Default___.NullChar(), m_GetOpt.Companion_Unused_.Create_Required_(), false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf(), m_GetOpt.Companion_Tri_.Create_No_()), m_GetOpt.Companion_Param_.Create_Opt_(_dafny.SeqOfString("two"), _dafny.SeqOfString("helpText"), _dafny.SeqOfString("arg"), _dafny.Char('t'), m_GetOpt.Companion_Unused_.Create_UnusedOk_(), false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf(), m_GetOpt.Companion_Tri_.Create_No_()), m_GetOpt.Companion_Param_.Create_Flag_(_dafny.SeqOfString("six"), _dafny.SeqOfString("helpText"), _dafny.Char('s'), false, false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf()), m_GetOpt.Companion_Param_.Create_Flag_(_dafny.SeqOfString("seven"), _dafny.SeqOfString("helpText"), _dafny.Char('v'), false, false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf())))
	var _1_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_GetOpt.Companion_Parsed_.Default())
	_ = _1_valueOrError0
	_1_valueOrError0 = m_GetOpt.Companion_Default___.GetOptions(_0_MyOptions, _dafny.SeqOf(_dafny.SeqOfString("cmd"), _dafny.SeqOfString("--foo"), _dafny.SeqOfString("file1"), _dafny.SeqOfString("--bar"), _dafny.SeqOfString("bar1"), _dafny.SeqOfString("-"), _dafny.SeqOfString("--bar=bar2=bar3"), _dafny.SeqOfString("file3"), _dafny.SeqOfString("--"), _dafny.SeqOfString("--this"), _dafny.SeqOfString("-that")))
	if !(!((_1_valueOrError0).IsFailure())) {
		panic("test/GetOpt.dfy(63,13): " + (_1_valueOrError0).String())
	}
	var _2_x m_GetOpt.Parsed
	_ = _2_x
	_2_x = (_1_valueOrError0).Extract().(m_GetOpt.Parsed)
	if !(_dafny.Companion_Sequence_.Equal((_2_x).Dtor_params(), _dafny.SeqOf(m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("foo"), m_Wrappers.Companion_Option_.Create_None_()), m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("bar"), m_Wrappers.Companion_Option_.Create_Some_(_dafny.SeqOfString("bar1"))), m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("bar"), m_Wrappers.Companion_Option_.Create_Some_(_dafny.SeqOfString("bar2=bar3")))))) {
		panic("test/GetOpt.dfy(64,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal((_2_x).Dtor_files(), _dafny.SeqOf(_dafny.SeqOfString("file1"), _dafny.SeqOfString("-"), _dafny.SeqOfString("file3"), _dafny.SeqOfString("--this"), _dafny.SeqOfString("-that")))) {
		panic("test/GetOpt.dfy(65,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _3_y m_Wrappers.Result
	_ = _3_y
	_3_y = m_GetOpt.Companion_Default___.GetOptions(_0_MyOptions, _dafny.SeqOf(_dafny.SeqOfString("cmd"), _dafny.SeqOfString("--foo"), _dafny.SeqOfString("file1"), _dafny.SeqOfString("file3"), _dafny.SeqOfString("--"), _dafny.SeqOfString("--this"), _dafny.SeqOfString("-that")))
	if !((_3_y).Is_Failure()) {
		panic("test/GetOpt.dfy(68,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal((_3_y).Dtor_error().(_dafny.Sequence), _dafny.SeqOfString("Option 'bar' is required, but was not used."))) {
		panic("test/GetOpt.dfy(69,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestDeprecated() {
	var _0_MyOptions m_GetOpt.Options
	_ = _0_MyOptions
	_0_MyOptions = m_GetOpt.Companion_Options_.Create_Options_(_dafny.SeqOfString("MyProg"), _dafny.SeqOfString("does stuff"), _dafny.SeqOf(m_GetOpt.Companion_Param_.Create_Flag_(_dafny.SeqOfString("foo"), _dafny.SeqOfString("helpText"), m_GetOpt.Companion_Default___.NullChar(), false, false, m_GetOpt.Companion_Visibility_.Create_Deprecated_(), _dafny.SeqOfChars(), _dafny.SeqOf()), m_GetOpt.Companion_Param_.Create_Opt_(_dafny.SeqOfString("bar"), _dafny.SeqOfString("helpText"), _dafny.SeqOfString("arg"), m_GetOpt.Companion_Default___.NullChar(), m_GetOpt.Companion_Unused_.Create_UnusedOk_(), false, m_GetOpt.Companion_Visibility_.Create_Deprecated_(), _dafny.SeqOfChars(), _dafny.SeqOf(), m_GetOpt.Companion_Tri_.Create_No_()), m_GetOpt.Companion_Param_.Create_Opt_(_dafny.SeqOfString("two"), _dafny.SeqOfString("helpText"), _dafny.SeqOfString("arg"), _dafny.Char('t'), m_GetOpt.Companion_Unused_.Create_UnusedOk_(), false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf(), m_GetOpt.Companion_Tri_.Create_No_()), m_GetOpt.Companion_Param_.Create_Flag_(_dafny.SeqOfString("six"), _dafny.SeqOfString("helpText"), _dafny.Char('s'), false, false, m_GetOpt.Companion_Visibility_.Create_Deprecated_(), _dafny.SeqOfChars(), _dafny.SeqOf()), m_GetOpt.Companion_Param_.Create_Flag_(_dafny.SeqOfString("seven"), _dafny.SeqOfString("helpText"), _dafny.Char('v'), false, false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf())))
	var _1_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_GetOpt.Companion_Parsed_.Default())
	_ = _1_valueOrError0
	_1_valueOrError0 = m_GetOpt.Companion_Default___.GetOptions(_0_MyOptions, _dafny.SeqOf(_dafny.SeqOfString("cmd"), _dafny.SeqOfString("--foo"), _dafny.SeqOfString("--bar=baz"), _dafny.SeqOfString("-svtstuff")))
	if !(!((_1_valueOrError0).IsFailure())) {
		panic("test/GetOpt.dfy(81,13): " + (_1_valueOrError0).String())
	}
	var _2_x m_GetOpt.Parsed
	_ = _2_x
	_2_x = (_1_valueOrError0).Extract().(m_GetOpt.Parsed)
	if !(_dafny.Companion_Sequence_.Equal((_2_x).Dtor_params(), _dafny.SeqOf(m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("seven"), m_Wrappers.Companion_Option_.Create_None_()), m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("two"), m_Wrappers.Companion_Option_.Create_Some_(_dafny.SeqOfString("stuff")))))) {
		panic("test/GetOpt.dfy(82,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal((_2_x).Dtor_files(), _dafny.SeqOf())) {
		panic("test/GetOpt.dfy(83,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestAlias() {
	var _0_MyOptions m_GetOpt.Options
	_ = _0_MyOptions
	_0_MyOptions = m_GetOpt.Companion_Options_.Create_Options_(_dafny.SeqOfString("MyProg"), _dafny.SeqOfString("does stuff"), _dafny.SeqOf(m_GetOpt.Companion_Param_.Create_Flag_(_dafny.SeqOfString("foo"), _dafny.SeqOfString("helpText"), m_GetOpt.Companion_Default___.NullChar(), false, false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfString("abc"), _dafny.SeqOf(_dafny.SeqOfString("def"), _dafny.SeqOfString("ghi"))), m_GetOpt.Companion_Param_.Create_Opt_(_dafny.SeqOfString("bar"), _dafny.SeqOfString("helpText"), _dafny.SeqOfString("arg"), m_GetOpt.Companion_Default___.NullChar(), m_GetOpt.Companion_Unused_.Create_UnusedOk_(), false, m_GetOpt.Companion_Visibility_.Create_Deprecated_(), _dafny.SeqOfChars(), _dafny.SeqOf(), m_GetOpt.Companion_Tri_.Create_No_()), m_GetOpt.Companion_Param_.Create_Opt_(_dafny.SeqOfString("two"), _dafny.SeqOfString("helpText"), _dafny.SeqOfString("arg"), _dafny.Char('t'), m_GetOpt.Companion_Unused_.Create_UnusedOk_(), false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf(), m_GetOpt.Companion_Tri_.Create_No_()), m_GetOpt.Companion_Param_.Create_Flag_(_dafny.SeqOfString("six"), _dafny.SeqOfString("helpText"), _dafny.Char('s'), false, false, m_GetOpt.Companion_Visibility_.Create_Deprecated_(), _dafny.SeqOfChars(), _dafny.SeqOf()), m_GetOpt.Companion_Param_.Create_Flag_(_dafny.SeqOfString("seven"), _dafny.SeqOfString("helpText"), _dafny.Char('v'), false, false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf())))
	var _1_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_GetOpt.Companion_Parsed_.Default())
	_ = _1_valueOrError0
	_1_valueOrError0 = m_GetOpt.Companion_Default___.GetOptions(_0_MyOptions, _dafny.SeqOf(_dafny.SeqOfString("cmd"), _dafny.SeqOfString("-abc"), _dafny.SeqOfString("--def"), _dafny.SeqOfString("--ghi")))
	if !(!((_1_valueOrError0).IsFailure())) {
		panic("test/GetOpt.dfy(95,13): " + (_1_valueOrError0).String())
	}
	var _2_x m_GetOpt.Parsed
	_ = _2_x
	_2_x = (_1_valueOrError0).Extract().(m_GetOpt.Parsed)
	if !(_dafny.Companion_Sequence_.Equal((_2_x).Dtor_params(), _dafny.SeqOf(m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("foo"), m_Wrappers.Companion_Option_.Create_None_()), m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("foo"), m_Wrappers.Companion_Option_.Create_None_()), m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("foo"), m_Wrappers.Companion_Option_.Create_None_()), m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("foo"), m_Wrappers.Companion_Option_.Create_None_()), m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("foo"), m_Wrappers.Companion_Option_.Create_None_())))) {
		panic("test/GetOpt.dfy(96,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal((_2_x).Dtor_files(), _dafny.SeqOf())) {
		panic("test/GetOpt.dfy(97,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestPositionalFail() {
	var _0_MyOptions m_GetOpt.Options
	_ = _0_MyOptions
	_0_MyOptions = m_GetOpt.Companion_Options_.Create_Options_(_dafny.SeqOfString("MyProg"), _dafny.SeqOfString("does stuff"), _dafny.SeqOf(m_GetOpt.Companion_Param_.Create_Flag_(_dafny.SeqOfString("foo"), _dafny.SeqOfString("helpText"), m_GetOpt.Companion_Default___.NullChar(), false, false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf()), m_GetOpt.Companion_Param_.Create_Opt_(_dafny.SeqOfString("two"), _dafny.SeqOfString("helpText"), _dafny.SeqOfString("arg"), m_GetOpt.Companion_Default___.NullChar(), m_GetOpt.Companion_Unused_.Create_UnusedOk_(), false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf(), m_GetOpt.Companion_Tri_.Create_Maybe_()), m_GetOpt.Companion_Param_.Create_Opt_(_dafny.SeqOfString("bar"), _dafny.SeqOfString("helpText"), _dafny.SeqOfString("arg"), m_GetOpt.Companion_Default___.NullChar(), m_GetOpt.Companion_Unused_.Create_UnusedOk_(), false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf(), m_GetOpt.Companion_Tri_.Create_Yes_())))
	var _1_x m_Wrappers.Result
	_ = _1_x
	_1_x = m_GetOpt.Companion_Default___.GetOptions(_0_MyOptions, _dafny.SeqOf(_dafny.SeqOfString("cmd"), _dafny.SeqOfString("stuff"), _dafny.SeqOfString("-123"), _dafny.SeqOfString("--foo")))
	if !((_1_x).Is_Failure()) {
		panic("test/GetOpt.dfy(108,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal((_1_x).Dtor_error().(_dafny.Sequence), _dafny.SeqOfString("Required positional argument 'bar' follows optional positional argument 'two'."))) {
		panic("test/GetOpt.dfy(109,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestPositional() {
	var _0_MyOptions m_GetOpt.Options
	_ = _0_MyOptions
	_0_MyOptions = m_GetOpt.Companion_Options_.Create_Options_(_dafny.SeqOfString("MyProg"), _dafny.SeqOfString("does stuff"), _dafny.SeqOf(m_GetOpt.Companion_Param_.Create_Flag_(_dafny.SeqOfString("foo"), _dafny.SeqOfString("helpText"), m_GetOpt.Companion_Default___.NullChar(), false, false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf()), m_GetOpt.Companion_Param_.Create_Opt_(_dafny.SeqOfString("bar"), _dafny.SeqOfString("helpText"), _dafny.SeqOfString("arg"), m_GetOpt.Companion_Default___.NullChar(), m_GetOpt.Companion_Unused_.Create_UnusedOk_(), false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf(), m_GetOpt.Companion_Tri_.Create_Yes_()), m_GetOpt.Companion_Param_.Create_Opt_(_dafny.SeqOfString("two"), _dafny.SeqOfString("helpText"), _dafny.SeqOfString("arg"), m_GetOpt.Companion_Default___.NullChar(), m_GetOpt.Companion_Unused_.Create_UnusedOk_(), false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf(), m_GetOpt.Companion_Tri_.Create_Maybe_())))
	var _1_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_GetOpt.Companion_Parsed_.Default())
	_ = _1_valueOrError0
	_1_valueOrError0 = m_GetOpt.Companion_Default___.GetOptions(_0_MyOptions, _dafny.SeqOf(_dafny.SeqOfString("cmd"), _dafny.SeqOfString("stuff"), _dafny.SeqOfString("-123"), _dafny.SeqOfString("--foo")))
	if !(!((_1_valueOrError0).IsFailure())) {
		panic("test/GetOpt.dfy(119,13): " + (_1_valueOrError0).String())
	}
	var _2_x m_GetOpt.Parsed
	_ = _2_x
	_2_x = (_1_valueOrError0).Extract().(m_GetOpt.Parsed)
	if !(_dafny.Companion_Sequence_.Equal((_2_x).Dtor_params(), _dafny.SeqOf(m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("bar"), m_Wrappers.Companion_Option_.Create_Some_(_dafny.SeqOfString("stuff"))), m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("two"), m_Wrappers.Companion_Option_.Create_Some_(_dafny.SeqOfString("-123"))), m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("foo"), m_Wrappers.Companion_Option_.Create_None_())))) {
		panic("test/GetOpt.dfy(120,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal((_2_x).Dtor_files(), _dafny.SeqOf())) {
		panic("test/GetOpt.dfy(121,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _3_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_GetOpt.Companion_Parsed_.Default())
	_ = _3_valueOrError1
	_3_valueOrError1 = m_GetOpt.Companion_Default___.GetOptions(_0_MyOptions, _dafny.SeqOf(_dafny.SeqOfString("cmd"), _dafny.SeqOfString("stuff"), _dafny.SeqOfString("--two=-123"), _dafny.SeqOfString("--foo")))
	if !(!((_3_valueOrError1).IsFailure())) {
		panic("test/GetOpt.dfy(123,9): " + (_3_valueOrError1).String())
	}
	_2_x = (_3_valueOrError1).Extract().(m_GetOpt.Parsed)
	if !(_dafny.Companion_Sequence_.Equal((_2_x).Dtor_params(), _dafny.SeqOf(m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("bar"), m_Wrappers.Companion_Option_.Create_Some_(_dafny.SeqOfString("stuff"))), m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("two"), m_Wrappers.Companion_Option_.Create_Some_(_dafny.SeqOfString("-123"))), m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("foo"), m_Wrappers.Companion_Option_.Create_None_())))) {
		panic("test/GetOpt.dfy(124,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal((_2_x).Dtor_files(), _dafny.SeqOf())) {
		panic("test/GetOpt.dfy(125,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _4_valueOrError2 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_GetOpt.Companion_Parsed_.Default())
	_ = _4_valueOrError2
	_4_valueOrError2 = m_GetOpt.Companion_Default___.GetOptions(_0_MyOptions, _dafny.SeqOf(_dafny.SeqOfString("cmd"), _dafny.SeqOfString("stuff"), _dafny.SeqOfString("--two=-123"), _dafny.SeqOfString("--foo"), _dafny.SeqOfString("--bar"), _dafny.SeqOfString("more-stuff")))
	if !(!((_4_valueOrError2).IsFailure())) {
		panic("test/GetOpt.dfy(127,9): " + (_4_valueOrError2).String())
	}
	_2_x = (_4_valueOrError2).Extract().(m_GetOpt.Parsed)
	if !(_dafny.Companion_Sequence_.Equal((_2_x).Dtor_params(), _dafny.SeqOf(m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("bar"), m_Wrappers.Companion_Option_.Create_Some_(_dafny.SeqOfString("stuff"))), m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("two"), m_Wrappers.Companion_Option_.Create_Some_(_dafny.SeqOfString("-123"))), m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("foo"), m_Wrappers.Companion_Option_.Create_None_()), m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("bar"), m_Wrappers.Companion_Option_.Create_Some_(_dafny.SeqOfString("more-stuff")))))) {
		panic("test/GetOpt.dfy(128,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal((_2_x).Dtor_files(), _dafny.SeqOf())) {
		panic("test/GetOpt.dfy(129,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _5_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_GetOpt.Companion_Parsed_.Default())
	_ = _5_valueOrError3
	_5_valueOrError3 = m_GetOpt.Companion_Default___.GetOptions(_0_MyOptions, _dafny.SeqOf(_dafny.SeqOfString("cmd"), _dafny.SeqOfString("stuff")))
	if !(!((_5_valueOrError3).IsFailure())) {
		panic("test/GetOpt.dfy(131,9): " + (_5_valueOrError3).String())
	}
	_2_x = (_5_valueOrError3).Extract().(m_GetOpt.Parsed)
	if !(_dafny.Companion_Sequence_.Equal((_2_x).Dtor_params(), _dafny.SeqOf(m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("bar"), m_Wrappers.Companion_Option_.Create_Some_(_dafny.SeqOfString("stuff")))))) {
		panic("test/GetOpt.dfy(132,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal((_2_x).Dtor_files(), _dafny.SeqOf())) {
		panic("test/GetOpt.dfy(133,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _6_y m_Wrappers.Result
	_ = _6_y
	_6_y = m_GetOpt.Companion_Default___.GetOptions(_0_MyOptions, _dafny.SeqOf(_dafny.SeqOfString("cmd"), _dafny.SeqOfString("--two=-123"), _dafny.SeqOfString("--foo"), _dafny.SeqOfString("--bar"), _dafny.SeqOfString("more-stuff")))
	if !((_6_y).Is_Failure()) {
		panic("test/GetOpt.dfy(136,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal((_6_y).Dtor_error().(_dafny.Sequence), _dafny.SeqOfString("Positional arg bar matched with invalid positional value '--two=-123'."))) {
		panic("test/GetOpt.dfy(137,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	_6_y = m_GetOpt.Companion_Default___.GetOptions(_0_MyOptions, _dafny.SeqOf(_dafny.SeqOfString("cmd")))
	if !((_6_y).Is_Failure()) {
		panic("test/GetOpt.dfy(140,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal((_6_y).Dtor_error().(_dafny.Sequence), _dafny.SeqOfString("Positional arg 'bar' is required, but we've run out of arguments."))) {
		panic("test/GetOpt.dfy(141,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestHelp() {
	var _0_MyOptions m_GetOpt.Options
	_ = _0_MyOptions
	_0_MyOptions = m_GetOpt.Companion_Options_.Create_Options_(_dafny.SeqOfString("MyProg"), _dafny.SeqOfString("does stuff"), _dafny.SeqOf(m_GetOpt.Companion_Param_.Create_Flag_(_dafny.SeqOfString("foo"), _dafny.SeqOfString("helpText"), m_GetOpt.Companion_Default___.NullChar(), false, false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf()), m_GetOpt.Companion_Param_.Create_Opt_(_dafny.SeqOfString("bar"), _dafny.SeqOfString("helpText"), _dafny.SeqOfString("arg"), m_GetOpt.Companion_Default___.NullChar(), m_GetOpt.Companion_Unused_.Create_UnusedOk_(), false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf(), m_GetOpt.Companion_Tri_.Create_No_()), m_GetOpt.Companion_Param_.Create_Opt_(_dafny.SeqOfString("two"), _dafny.SeqOfString("helpText"), _dafny.SeqOfString("arg"), _dafny.Char('t'), m_GetOpt.Companion_Unused_.Create_UnusedOk_(), false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf(), m_GetOpt.Companion_Tri_.Create_No_()), m_GetOpt.Companion_Param_.Create_Flag_(_dafny.SeqOfString("six"), _dafny.SeqOfString("helpText"), _dafny.Char('s'), false, false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf()), m_GetOpt.Companion_Param_.Create_Flag_(_dafny.SeqOfString("seven"), _dafny.SeqOfString("helpText"), _dafny.Char('v'), false, false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf())))
	var _1_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_GetOpt.Companion_Parsed_.Default())
	_ = _1_valueOrError0
	_1_valueOrError0 = m_GetOpt.Companion_Default___.GetOptions(_0_MyOptions, _dafny.SeqOf(_dafny.SeqOfString("cmd"), _dafny.SeqOfString("--help")))
	if !(!((_1_valueOrError0).IsFailure())) {
		panic("test/GetOpt.dfy(153,13): " + (_1_valueOrError0).String())
	}
	var _2_x m_GetOpt.Parsed
	_ = _2_x
	_2_x = (_1_valueOrError0).Extract().(m_GetOpt.Parsed)
	var _3_valueOrError1 m_Wrappers.Option = m_Wrappers.Companion_Option_.Default()
	_ = _3_valueOrError1
	_3_valueOrError1 = m_GetOpt.Companion_Default___.NeedsHelp(_0_MyOptions, _2_x, _dafny.SeqOfString(""))
	if !(!((_3_valueOrError1).IsFailure())) {
		panic("test/GetOpt.dfy(154,13): " + (_3_valueOrError1).String())
	}
	var _4_y _dafny.Sequence
	_ = _4_y
	_4_y = (_3_valueOrError1).Extract().(_dafny.Sequence)
	_dafny.Print((_dafny.SeqOfString("\n")).SetString())
	_dafny.Print((_4_y).SetString())
	_dafny.Print((_dafny.SeqOfString("\n")).SetString())
}
func (_static *CompanionStruct_Default___) TestHelpFail() {
	var _0_MyOptions m_GetOpt.Options
	_ = _0_MyOptions
	_0_MyOptions = m_GetOpt.Companion_Options_.Create_Options_(_dafny.SeqOfString("MyProg"), _dafny.SeqOfString("does stuff"), _dafny.SeqOf(m_GetOpt.Companion_Param_.Create_Flag_(_dafny.SeqOfString("foo"), _dafny.SeqOfString("helpText"), m_GetOpt.Companion_Default___.NullChar(), false, false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf()), m_GetOpt.Companion_Param_.Create_Opt_(_dafny.SeqOfString("bar"), _dafny.SeqOfString("helpText"), _dafny.SeqOfString("arg"), m_GetOpt.Companion_Default___.NullChar(), m_GetOpt.Companion_Unused_.Create_UnusedOk_(), false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf(), m_GetOpt.Companion_Tri_.Create_No_()), m_GetOpt.Companion_Param_.Create_Opt_(_dafny.SeqOfString("two"), _dafny.SeqOfString("helpText"), _dafny.SeqOfString("arg"), _dafny.Char('t'), m_GetOpt.Companion_Unused_.Create_UnusedOk_(), false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf(), m_GetOpt.Companion_Tri_.Create_No_()), m_GetOpt.Companion_Param_.Create_Flag_(_dafny.SeqOfString("six"), _dafny.SeqOfString("helpText"), _dafny.Char('s'), false, false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf()), m_GetOpt.Companion_Param_.Create_Flag_(_dafny.SeqOfString("seven"), _dafny.SeqOfString("helpText"), _dafny.Char('v'), false, false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf())))
	var _1_x m_Wrappers.Result
	_ = _1_x
	_1_x = m_GetOpt.Companion_Default___.GetOptions(_0_MyOptions, _dafny.SeqOf(_dafny.SeqOfString("cmd"), _dafny.SeqOfString("--help"), _dafny.SeqOfString("--foo")))
	if !((_1_x).Is_Failure()) {
		panic("test/GetOpt.dfy(168,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal((_1_x).Dtor_error().(_dafny.Sequence), _dafny.SeqOfString("Option 'help' used with other stuff, but must only be used alone."))) {
		panic("test/GetOpt.dfy(169,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestNested() {
	var _0_MyOptions m_GetOpt.Options
	_ = _0_MyOptions
	_0_MyOptions = m_GetOpt.Companion_Options_.Create_Options_(_dafny.SeqOfString("MyProg"), _dafny.SeqOfString("does stuff"), _dafny.SeqOf(m_GetOpt.Companion_Param_.Create_Flag_(_dafny.SeqOfString("foo"), _dafny.SeqOfString("Does foo things"), m_GetOpt.Companion_Default___.NullChar(), false, false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf()), m_GetOpt.Companion_Param_.Create_Opt_(_dafny.SeqOfString("two"), _dafny.SeqOfString("Does bar things to thingy"), _dafny.SeqOfString("thingy"), _dafny.Char('t'), m_GetOpt.Companion_Unused_.Create_UnusedOk_(), false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf(), m_GetOpt.Companion_Tri_.Create_No_()), m_GetOpt.Companion_Param_.Create_Command_(m_GetOpt.Companion_Options_.Create_Options_(_dafny.SeqOfString("command"), _dafny.SeqOfString("Does command stuff"), _dafny.SeqOf(m_GetOpt.Companion_Param_.Create_Opt_(_dafny.SeqOfString("five"), _dafny.SeqOfString("Does five things to thingy"), _dafny.SeqOfString("thingy"), _dafny.Char('h'), m_GetOpt.Companion_Unused_.Create_UnusedOk_(), false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf(), m_GetOpt.Companion_Tri_.Create_No_()), m_GetOpt.Companion_Param_.Create_Flag_(_dafny.SeqOfString("six"), _dafny.SeqOfString("Does six things"), m_GetOpt.Companion_Default___.NullChar(), false, true, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf())))), m_GetOpt.Companion_Param_.Create_Command_(m_GetOpt.Companion_Options_.Create_Options_(_dafny.SeqOfString("other"), _dafny.SeqOfString("Does other stuff"), _dafny.SeqOf(m_GetOpt.Companion_Param_.Create_Opt_(_dafny.SeqOfString("seven"), _dafny.SeqOfString("Does seven things to thingy"), _dafny.SeqOfString("thingy"), _dafny.Char('h'), m_GetOpt.Companion_Unused_.Create_UnusedOk_(), false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf(), m_GetOpt.Companion_Tri_.Create_No_()), m_GetOpt.Companion_Param_.Create_Flag_(_dafny.SeqOfString("eight"), _dafny.SeqOfString("Does eight things"), m_GetOpt.Companion_Default___.NullChar(), false, false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf()))))))
	var _1_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_GetOpt.Companion_Parsed_.Default())
	_ = _1_valueOrError0
	_1_valueOrError0 = m_GetOpt.Companion_Default___.GetOptions(_0_MyOptions, _dafny.SeqOf(_dafny.SeqOfString("MyProg"), _dafny.SeqOfString("--foo"), _dafny.SeqOfString("other"), _dafny.SeqOfString("--seven=siete"), _dafny.SeqOfString("--eight")))
	if !(!((_1_valueOrError0).IsFailure())) {
		panic("test/GetOpt.dfy(186,13): " + (_1_valueOrError0).String())
	}
	var _2_x m_GetOpt.Parsed
	_ = _2_x
	_2_x = (_1_valueOrError0).Extract().(m_GetOpt.Parsed)
	if !(_dafny.Companion_Sequence_.Equal((_2_x).Dtor_command(), _dafny.SeqOfString("MyProg"))) {
		panic("test/GetOpt.dfy(187,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal((_2_x).Dtor_params(), _dafny.SeqOf(m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("foo"), m_Wrappers.Companion_Option_.Create_None_())))) {
		panic("test/GetOpt.dfy(188,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal((_2_x).Dtor_files(), _dafny.SeqOf())) {
		panic("test/GetOpt.dfy(189,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(((_2_x).Dtor_subcommand()).Is_Some()) {
		panic("test/GetOpt.dfy(190,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _3_sub m_GetOpt.Parsed
	_ = _3_sub
	_3_sub = ((_2_x).Dtor_subcommand()).Dtor_value().(m_GetOpt.Parsed)
	if !(_dafny.Companion_Sequence_.Equal((_3_sub).Dtor_command(), _dafny.SeqOfString("other"))) {
		panic("test/GetOpt.dfy(192,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal((_3_sub).Dtor_params(), _dafny.SeqOf(m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("seven"), m_Wrappers.Companion_Option_.Create_Some_(_dafny.SeqOfString("siete"))), m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("eight"), m_Wrappers.Companion_Option_.Create_None_())))) {
		panic("test/GetOpt.dfy(193,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal((_3_sub).Dtor_files(), _dafny.SeqOf())) {
		panic("test/GetOpt.dfy(194,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(((_3_sub).Dtor_subcommand()).Is_None()) {
		panic("test/GetOpt.dfy(195,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _4_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_GetOpt.Companion_Parsed_.Default())
	_ = _4_valueOrError1
	_4_valueOrError1 = m_GetOpt.Companion_Default___.GetOptions(_0_MyOptions, _dafny.SeqOf(_dafny.SeqOfString("MyProg"), _dafny.SeqOfString("--help")))
	if !(!((_4_valueOrError1).IsFailure())) {
		panic("test/GetOpt.dfy(197,9): " + (_4_valueOrError1).String())
	}
	_2_x = (_4_valueOrError1).Extract().(m_GetOpt.Parsed)
	var _5_valueOrError2 m_Wrappers.Option = m_Wrappers.Companion_Option_.Default()
	_ = _5_valueOrError2
	_5_valueOrError2 = m_GetOpt.Companion_Default___.NeedsHelp(_0_MyOptions, _2_x, _dafny.SeqOfString(""))
	if !(!((_5_valueOrError2).IsFailure())) {
		panic("test/GetOpt.dfy(198,13): " + (_5_valueOrError2).String())
	}
	var _6_y _dafny.Sequence
	_ = _6_y
	_6_y = (_5_valueOrError2).Extract().(_dafny.Sequence)
	_dafny.Print((_dafny.SeqOfString("\n")).SetString())
	_dafny.Print((_6_y).SetString())
	_dafny.Print((_dafny.SeqOfString("\n")).SetString())
	var _7_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_GetOpt.Companion_Parsed_.Default())
	_ = _7_valueOrError3
	_7_valueOrError3 = m_GetOpt.Companion_Default___.GetOptions(_0_MyOptions, _dafny.SeqOf(_dafny.SeqOfString("MyProg"), _dafny.SeqOfString("command"), _dafny.SeqOfString("--help")))
	if !(!((_7_valueOrError3).IsFailure())) {
		panic("test/GetOpt.dfy(201,9): " + (_7_valueOrError3).String())
	}
	_2_x = (_7_valueOrError3).Extract().(m_GetOpt.Parsed)
	var _8_valueOrError4 m_Wrappers.Option = m_Wrappers.Companion_Option_.Default()
	_ = _8_valueOrError4
	_8_valueOrError4 = m_GetOpt.Companion_Default___.NeedsHelp(_0_MyOptions, _2_x, _dafny.SeqOfString(""))
	if !(!((_8_valueOrError4).IsFailure())) {
		panic("test/GetOpt.dfy(202,9): " + (_8_valueOrError4).String())
	}
	_6_y = (_8_valueOrError4).Extract().(_dafny.Sequence)
	_dafny.Print((_dafny.SeqOfString("\n")).SetString())
	_dafny.Print((_6_y).SetString())
	_dafny.Print((_dafny.SeqOfString("\n")).SetString())
}
func (_static *CompanionStruct_Default___) TestDefault() {
	var _0_MyOptions m_GetOpt.Options
	_ = _0_MyOptions
	_0_MyOptions = m_GetOpt.Companion_Options_.Create_Options_(_dafny.SeqOfString("MyProg"), _dafny.SeqOfString("does stuff"), _dafny.SeqOf(m_GetOpt.Companion_Param_.Create_Flag_(_dafny.SeqOfString("foo"), _dafny.SeqOfString("Does foo things"), m_GetOpt.Companion_Default___.NullChar(), false, false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf()), m_GetOpt.Companion_Param_.Create_Opt_(_dafny.SeqOfString("two"), _dafny.SeqOfString("Does bar things to thingy"), _dafny.SeqOfString("thingy"), _dafny.Char('t'), m_GetOpt.Companion_Unused_.Create_Default_(_dafny.SeqOfString("two_dflt")), false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf(), m_GetOpt.Companion_Tri_.Create_No_()), m_GetOpt.Companion_Param_.Create_Command_(m_GetOpt.Companion_Options_.Create_Options_(_dafny.SeqOfString("command"), _dafny.SeqOfString("Does command stuff"), _dafny.SeqOf(m_GetOpt.Companion_Param_.Create_Opt_(_dafny.SeqOfString("five"), _dafny.SeqOfString("Does five things to thingy"), _dafny.SeqOfString("thingy"), _dafny.Char('h'), m_GetOpt.Companion_Unused_.Create_Default_(_dafny.SeqOfString("five_dflt")), false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf(), m_GetOpt.Companion_Tri_.Create_No_()), m_GetOpt.Companion_Param_.Create_Flag_(_dafny.SeqOfString("six"), _dafny.SeqOfString("Does six things"), m_GetOpt.Companion_Default___.NullChar(), false, false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf())))), m_GetOpt.Companion_Param_.Create_Command_(m_GetOpt.Companion_Options_.Create_Options_(_dafny.SeqOfString("other"), _dafny.SeqOfString("Does other stuff"), _dafny.SeqOf(m_GetOpt.Companion_Param_.Create_Opt_(_dafny.SeqOfString("seven"), _dafny.SeqOfString("Does seven things to thingy"), _dafny.SeqOfString("thingy"), _dafny.Char('h'), m_GetOpt.Companion_Unused_.Create_Default_(_dafny.SeqOfString("seven_dflt")), false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf(), m_GetOpt.Companion_Tri_.Create_No_()), m_GetOpt.Companion_Param_.Create_Flag_(_dafny.SeqOfString("eight"), _dafny.SeqOfString("Does eight things"), m_GetOpt.Companion_Default___.NullChar(), false, false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf()))))))
	var _1_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_GetOpt.Companion_Parsed_.Default())
	_ = _1_valueOrError0
	_1_valueOrError0 = m_GetOpt.Companion_Default___.GetOptions(_0_MyOptions, _dafny.SeqOf(_dafny.SeqOfString("cmd"), _dafny.SeqOfString("--foo"), _dafny.SeqOfString("other"), _dafny.SeqOfString("--eight")))
	if !(!((_1_valueOrError0).IsFailure())) {
		panic("test/GetOpt.dfy(227,13): " + (_1_valueOrError0).String())
	}
	var _2_x m_GetOpt.Parsed
	_ = _2_x
	_2_x = (_1_valueOrError0).Extract().(m_GetOpt.Parsed)
	if !(_dafny.Companion_Sequence_.Equal((_2_x).Dtor_command(), _dafny.SeqOfString("cmd"))) {
		panic("test/GetOpt.dfy(228,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal((_2_x).Dtor_params(), _dafny.SeqOf(m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("foo"), m_Wrappers.Companion_Option_.Create_None_()), m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("two"), m_Wrappers.Companion_Option_.Create_Some_(_dafny.SeqOfString("two_dflt")))))) {
		panic("test/GetOpt.dfy(229,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal((_2_x).Dtor_files(), _dafny.SeqOf())) {
		panic("test/GetOpt.dfy(230,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(((_2_x).Dtor_subcommand()).Is_Some()) {
		panic("test/GetOpt.dfy(231,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _3_sub m_GetOpt.Parsed
	_ = _3_sub
	_3_sub = ((_2_x).Dtor_subcommand()).Dtor_value().(m_GetOpt.Parsed)
	if !(_dafny.Companion_Sequence_.Equal((_3_sub).Dtor_command(), _dafny.SeqOfString("other"))) {
		panic("test/GetOpt.dfy(233,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal((_3_sub).Dtor_params(), _dafny.SeqOf(m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("eight"), m_Wrappers.Companion_Option_.Create_None_()), m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("seven"), m_Wrappers.Companion_Option_.Create_Some_(_dafny.SeqOfString("seven_dflt")))))) {
		panic("test/GetOpt.dfy(234,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal((_3_sub).Dtor_files(), _dafny.SeqOf())) {
		panic("test/GetOpt.dfy(235,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(((_3_sub).Dtor_subcommand()).Is_None()) {
		panic("test/GetOpt.dfy(236,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _4_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_GetOpt.Companion_Parsed_.Default())
	_ = _4_valueOrError1
	_4_valueOrError1 = m_GetOpt.Companion_Default___.GetOptions(_0_MyOptions, _dafny.SeqOf(_dafny.SeqOfString("cmd"), _dafny.SeqOfString("--foo"), _dafny.SeqOfString("command"), _dafny.SeqOfString("--six")))
	if !(!((_4_valueOrError1).IsFailure())) {
		panic("test/GetOpt.dfy(238,9): " + (_4_valueOrError1).String())
	}
	_2_x = (_4_valueOrError1).Extract().(m_GetOpt.Parsed)
	if !(_dafny.Companion_Sequence_.Equal((_2_x).Dtor_command(), _dafny.SeqOfString("cmd"))) {
		panic("test/GetOpt.dfy(239,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal((_2_x).Dtor_params(), _dafny.SeqOf(m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("foo"), m_Wrappers.Companion_Option_.Create_None_()), m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("two"), m_Wrappers.Companion_Option_.Create_Some_(_dafny.SeqOfString("two_dflt")))))) {
		panic("test/GetOpt.dfy(240,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal((_2_x).Dtor_files(), _dafny.SeqOf())) {
		panic("test/GetOpt.dfy(241,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(((_2_x).Dtor_subcommand()).Is_Some()) {
		panic("test/GetOpt.dfy(242,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	_3_sub = ((_2_x).Dtor_subcommand()).Dtor_value().(m_GetOpt.Parsed)
	if !(_dafny.Companion_Sequence_.Equal((_3_sub).Dtor_command(), _dafny.SeqOfString("command"))) {
		panic("test/GetOpt.dfy(244,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal((_3_sub).Dtor_params(), _dafny.SeqOf(m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("six"), m_Wrappers.Companion_Option_.Create_None_()), m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("five"), m_Wrappers.Companion_Option_.Create_Some_(_dafny.SeqOfString("five_dflt")))))) {
		panic("test/GetOpt.dfy(245,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal((_3_sub).Dtor_files(), _dafny.SeqOf())) {
		panic("test/GetOpt.dfy(246,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(((_3_sub).Dtor_subcommand()).Is_None()) {
		panic("test/GetOpt.dfy(247,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	var _5_valueOrError2 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(m_GetOpt.Companion_Parsed_.Default())
	_ = _5_valueOrError2
	_5_valueOrError2 = m_GetOpt.Companion_Default___.GetOptions(_0_MyOptions, _dafny.SeqOf(_dafny.SeqOfString("cmd"), _dafny.SeqOfString("--foo")))
	if !(!((_5_valueOrError2).IsFailure())) {
		panic("test/GetOpt.dfy(249,9): " + (_5_valueOrError2).String())
	}
	_2_x = (_5_valueOrError2).Extract().(m_GetOpt.Parsed)
	if !(_dafny.Companion_Sequence_.Equal((_2_x).Dtor_command(), _dafny.SeqOfString("cmd"))) {
		panic("test/GetOpt.dfy(250,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal((_2_x).Dtor_params(), _dafny.SeqOf(m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("foo"), m_Wrappers.Companion_Option_.Create_None_()), m_GetOpt.Companion_OneArg_.Create_OneArg_(_dafny.SeqOfString("two"), m_Wrappers.Companion_Option_.Create_Some_(_dafny.SeqOfString("two_dflt")))))) {
		panic("test/GetOpt.dfy(251,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal((_2_x).Dtor_files(), _dafny.SeqOf())) {
		panic("test/GetOpt.dfy(252,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(((_2_x).Dtor_subcommand()).Is_None()) {
		panic("test/GetOpt.dfy(253,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) TestDdbec() {
	var _0_MyOptions m_GetOpt.Options
	_ = _0_MyOptions
	_0_MyOptions = m_GetOpt.Companion_Options_.Create_Options_(_dafny.SeqOfString("ddbec"), _dafny.SeqOfString("Test the ddbec"), _dafny.SeqOf(m_GetOpt.Companion_Param_.Create_Command_(m_GetOpt.Companion_Options_.Create_Options_(_dafny.SeqOfString("encrypt"), _dafny.SeqOfString("Encrypts record"), _dafny.SeqOf(m_GetOpt.Companion_Param_.Create_Opt_(_dafny.SeqOfString("output"), _dafny.SeqOfString("Write encrypted records to fileName."), _dafny.SeqOfString("fileName"), _dafny.Char('o'), m_GetOpt.Companion_Unused_.Create_UnusedOk_(), false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf(), m_GetOpt.Companion_Tri_.Create_No_())))), m_GetOpt.Companion_Param_.Create_Command_(m_GetOpt.Companion_Options_.Create_Options_(_dafny.SeqOfString("decrypt"), _dafny.SeqOfString("Decrypts Records"), _dafny.SeqOf(m_GetOpt.Companion_Param_.Create_Opt_(_dafny.SeqOfString("expected"), _dafny.SeqOfString("fileName contains expected plaintext records."), _dafny.SeqOfString("fileName"), _dafny.Char('e'), m_GetOpt.Companion_Unused_.Create_UnusedOk_(), false, m_GetOpt.Companion_Visibility_.Create_Normal_(), _dafny.SeqOfChars(), _dafny.SeqOf(), m_GetOpt.Companion_Tri_.Create_No_()))))))
}

// End of class Default__
