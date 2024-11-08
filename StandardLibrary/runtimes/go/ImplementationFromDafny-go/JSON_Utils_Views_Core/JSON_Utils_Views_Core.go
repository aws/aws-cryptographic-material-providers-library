// Package JSON_Utils_Views_Core
// Dafny module JSON_Utils_Views_Core compiled into Go

package JSON_Utils_Views_Core

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
	return "JSON_Utils_Views_Core.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) Adjacent(lv View__, rv View__) bool {
	return (((lv).Dtor_end()) == ((rv).Dtor_beg())) && (_dafny.Companion_Sequence_.Equal((lv).Dtor_s(), (rv).Dtor_s()))
}
func (_static *CompanionStruct_Default___) Merge(lv View__, rv View__) View__ {
	var _0_dt__update__tmp_h0 View__ = lv
	_ = _0_dt__update__tmp_h0
	var _1_dt__update_hend_h0 uint32 = (rv).Dtor_end()
	_ = _1_dt__update_hend_h0
	return Companion_View___.Create_View_((_0_dt__update__tmp_h0).Dtor_s(), (_0_dt__update__tmp_h0).Dtor_beg(), _1_dt__update_hend_h0)
}

// End of class Default__

// Definition of class View
type View struct {
}

func New_View_() *View {
	_this := View{}

	return &_this
}

type CompanionStruct_View_ struct {
}

var Companion_View_ = CompanionStruct_View_{}

func (*View) String() string {
	return "JSON_Utils_Views_Core.View"
}
func (_this *CompanionStruct_View_) Witness() View__ {
	return Companion_View___.Create_View_(_dafny.SeqOf(), uint32(0), uint32(0))
}

// End of class View

func Type_View_() _dafny.TypeDescriptor {
	return type_View_{}
}

type type_View_ struct {
}

func (_this type_View_) Default() interface{} {
	return Companion_View_.Witness()
}

func (_this type_View_) String() string {
	return "JSON_Utils_Views_Core.View"
}

// Definition of datatype View__
type View__ struct {
	Data_View___
}

func (_this View__) Get_() Data_View___ {
	return _this.Data_View___
}

type Data_View___ interface {
	isView__()
}

type CompanionStruct_View___ struct {
}

var Companion_View___ = CompanionStruct_View___{}

type View___View struct {
	S   _dafny.Sequence
	Beg uint32
	End uint32
}

func (View___View) isView__() {}

func (CompanionStruct_View___) Create_View_(S _dafny.Sequence, Beg uint32, End uint32) View__ {
	return View__{View___View{S, Beg, End}}
}

func (_this View__) Is_View() bool {
	_, ok := _this.Get_().(View___View)
	return ok
}

func (CompanionStruct_View___) Default() View__ {
	return Companion_View___.Create_View_(_dafny.EmptySeq, uint32(0), uint32(0))
}

func (_this View__) Dtor_s() _dafny.Sequence {
	return _this.Get_().(View___View).S
}

func (_this View__) Dtor_beg() uint32 {
	return _this.Get_().(View___View).Beg
}

func (_this View__) Dtor_end() uint32 {
	return _this.Get_().(View___View).End
}

func (_this View__) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case View___View:
		{
			return "Core.View_.View" + "(" + _dafny.String(data.S) + ", " + _dafny.String(data.Beg) + ", " + _dafny.String(data.End) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this View__) Equals(other View__) bool {
	switch data1 := _this.Get_().(type) {
	case View___View:
		{
			data2, ok := other.Get_().(View___View)
			return ok && data1.S.Equals(data2.S) && data1.Beg == data2.Beg && data1.End == data2.End
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this View__) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(View__)
	return ok && _this.Equals(typed)
}

func Type_View___() _dafny.TypeDescriptor {
	return type_View___{}
}

type type_View___ struct {
}

func (_this type_View___) Default() interface{} {
	return Companion_View___.Default()
}

func (_this type_View___) String() string {
	return "JSON_Utils_Views_Core.View__"
}
func (_this View__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = View__{}

func (_this View__) Length() uint32 {
	{
		return ((_this).Dtor_end()) - (func() uint32 { return ((_this).Dtor_beg()) })()
	}
}
func (_this View__) Bytes() _dafny.Sequence {
	{
		return ((_this).Dtor_s()).Subsequence(uint32((_this).Dtor_beg()), uint32((_this).Dtor_end()))
	}
}
func (_static CompanionStruct_View___) OfBytes(bs _dafny.Sequence) View__ {
	return Companion_View___.Create_View_(bs, uint32(0), uint32((bs).Cardinality()))
}
func (_static CompanionStruct_View___) OfString(s _dafny.Sequence) _dafny.Sequence {
	return _dafny.SeqCreate((_dafny.IntOfUint32((s).Cardinality())).Uint32(), func(coer31 func(_dafny.Int) uint8) func(_dafny.Int) interface{} {
		return func(arg35 _dafny.Int) interface{} {
			return coer31(arg35)
		}
	}((func(_0_s _dafny.Sequence) func(_dafny.Int) uint8 {
		return func(_1_i _dafny.Int) uint8 {
			return uint8((_0_s).Select((_1_i).Uint32()).(_dafny.Char))
		}
	})(s)))
}
func (_this View__) Byte_q(c uint8) bool {
	{
		var _hresult bool = false
		_ = _hresult
		_hresult = (((_this).Length()) == (uint32(1))) && (((_this).At(uint32(0))) == (c))
		return _hresult
		return _hresult
	}
}
func (_this View__) Char_q(c _dafny.Char) bool {
	{
		return (_this).Byte_q(uint8(c))
	}
}
func (_this View__) At(idx uint32) uint8 {
	{
		return ((_this).Dtor_s()).Select(uint32(((_this).Dtor_beg()) + (idx))).(uint8)
	}
}
func (_this View__) Peek() int16 {
	{
		if (_this).Empty_q() {
			return int16(-1)
		} else {
			return int16((_this).At(uint32(0)))
		}
	}
}
func (_this View__) CopyTo(dest _dafny.Array, start uint32) {
	{
		var _hi0 uint32 = (_this).Length()
		_ = _hi0
		for _0_idx := uint32(0); _0_idx < _hi0; _0_idx++ {
			var _index0 uint32 = (start) + (_0_idx)
			_ = _index0
			(dest).ArraySet1Byte(((_this).Dtor_s()).Select(uint32(((_this).Dtor_beg())+(_0_idx))).(uint8), int(_index0))
		}
	}
}
func (_static CompanionStruct_View___) Empty() View__ {
	return Companion_View___.Create_View_(_dafny.SeqOf(), uint32(0), uint32(0))
}
func (_this View__) Empty_q() bool {
	{
		return ((_this).Dtor_beg()) == ((_this).Dtor_end())
	}
}

// End of datatype View__
