// Package JSON_Values
// Dafny module JSON_Values compiled into Go

package JSON_Values

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
	m_JSON_Errors "github.com/dafny-lang/DafnyStandardLibGo/JSON_Errors"
	m_JSON_Utils_Cursors "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Cursors"
	m_JSON_Utils_Lexers_Core "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Lexers_Core"
	m_JSON_Utils_Lexers_Strings "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Lexers_Strings"
	m_JSON_Utils_Parsers "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Parsers"
	m_JSON_Utils_Seq "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Seq"
	m_JSON_Utils_Str "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Str"
	m_JSON_Utils_Str_CharStrConversion "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Str_CharStrConversion"
	m_JSON_Utils_Str_CharStrEscaping "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Str_CharStrEscaping"
	m_JSON_Utils_Vectors "github.com/dafny-lang/DafnyStandardLibGo/JSON_Utils_Vectors"
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
var _ m_JSON_Utils_Lexers_Strings.Dummy__
var _ m_JSON_Utils_Cursors.Dummy__
var _ m_JSON_Utils_Parsers.Dummy__
var _ m_JSON_Utils_Str_CharStrConversion.Dummy__
var _ m_JSON_Utils_Str_CharStrEscaping.Dummy__
var _ m_JSON_Utils_Str.Dummy__
var _ m_JSON_Utils_Seq.Dummy__
var _ m_JSON_Utils_Vectors.Dummy__
var _ m_JSON_Errors.Dummy__

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
	return "JSON_Values.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) Int(n _dafny.Int) Decimal {
	return Companion_Decimal_.Create_Decimal_(n, _dafny.Zero)
}

// End of class Default__

// Definition of datatype Decimal
type Decimal struct {
	Data_Decimal_
}

func (_this Decimal) Get_() Data_Decimal_ {
	return _this.Data_Decimal_
}

type Data_Decimal_ interface {
	isDecimal()
}

type CompanionStruct_Decimal_ struct {
}

var Companion_Decimal_ = CompanionStruct_Decimal_{}

type Decimal_Decimal struct {
	N   _dafny.Int
	E10 _dafny.Int
}

func (Decimal_Decimal) isDecimal() {}

func (CompanionStruct_Decimal_) Create_Decimal_(N _dafny.Int, E10 _dafny.Int) Decimal {
	return Decimal{Decimal_Decimal{N, E10}}
}

func (_this Decimal) Is_Decimal() bool {
	_, ok := _this.Get_().(Decimal_Decimal)
	return ok
}

func (CompanionStruct_Decimal_) Default() Decimal {
	return Companion_Decimal_.Create_Decimal_(_dafny.Zero, _dafny.Zero)
}

func (_this Decimal) Dtor_n() _dafny.Int {
	return _this.Get_().(Decimal_Decimal).N
}

func (_this Decimal) Dtor_e10() _dafny.Int {
	return _this.Get_().(Decimal_Decimal).E10
}

func (_this Decimal) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case Decimal_Decimal:
		{
			return "Values.Decimal.Decimal" + "(" + _dafny.String(data.N) + ", " + _dafny.String(data.E10) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this Decimal) Equals(other Decimal) bool {
	switch data1 := _this.Get_().(type) {
	case Decimal_Decimal:
		{
			data2, ok := other.Get_().(Decimal_Decimal)
			return ok && data1.N.Cmp(data2.N) == 0 && data1.E10.Cmp(data2.E10) == 0
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this Decimal) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(Decimal)
	return ok && _this.Equals(typed)
}

func Type_Decimal_() _dafny.TypeDescriptor {
	return type_Decimal_{}
}

type type_Decimal_ struct {
}

func (_this type_Decimal_) Default() interface{} {
	return Companion_Decimal_.Default()
}

func (_this type_Decimal_) String() string {
	return "JSON_Values.Decimal"
}
func (_this Decimal) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = Decimal{}

// End of datatype Decimal

// Definition of datatype JSON
type JSON struct {
	Data_JSON_
}

func (_this JSON) Get_() Data_JSON_ {
	return _this.Data_JSON_
}

type Data_JSON_ interface {
	isJSON()
}

type CompanionStruct_JSON_ struct {
}

var Companion_JSON_ = CompanionStruct_JSON_{}

type JSON_Null struct {
}

func (JSON_Null) isJSON() {}

func (CompanionStruct_JSON_) Create_Null_() JSON {
	return JSON{JSON_Null{}}
}

func (_this JSON) Is_Null() bool {
	_, ok := _this.Get_().(JSON_Null)
	return ok
}

type JSON_Bool struct {
	B bool
}

func (JSON_Bool) isJSON() {}

func (CompanionStruct_JSON_) Create_Bool_(B bool) JSON {
	return JSON{JSON_Bool{B}}
}

func (_this JSON) Is_Bool() bool {
	_, ok := _this.Get_().(JSON_Bool)
	return ok
}

type JSON_String struct {
	Str _dafny.Sequence
}

func (JSON_String) isJSON() {}

func (CompanionStruct_JSON_) Create_String_(Str _dafny.Sequence) JSON {
	return JSON{JSON_String{Str}}
}

func (_this JSON) Is_String() bool {
	_, ok := _this.Get_().(JSON_String)
	return ok
}

type JSON_Number struct {
	Num Decimal
}

func (JSON_Number) isJSON() {}

func (CompanionStruct_JSON_) Create_Number_(Num Decimal) JSON {
	return JSON{JSON_Number{Num}}
}

func (_this JSON) Is_Number() bool {
	_, ok := _this.Get_().(JSON_Number)
	return ok
}

type JSON_Object struct {
	Obj _dafny.Sequence
}

func (JSON_Object) isJSON() {}

func (CompanionStruct_JSON_) Create_Object_(Obj _dafny.Sequence) JSON {
	return JSON{JSON_Object{Obj}}
}

func (_this JSON) Is_Object() bool {
	_, ok := _this.Get_().(JSON_Object)
	return ok
}

type JSON_Array struct {
	Arr _dafny.Sequence
}

func (JSON_Array) isJSON() {}

func (CompanionStruct_JSON_) Create_Array_(Arr _dafny.Sequence) JSON {
	return JSON{JSON_Array{Arr}}
}

func (_this JSON) Is_Array() bool {
	_, ok := _this.Get_().(JSON_Array)
	return ok
}

func (CompanionStruct_JSON_) Default() JSON {
	return Companion_JSON_.Create_Null_()
}

func (_this JSON) Dtor_b() bool {
	return _this.Get_().(JSON_Bool).B
}

func (_this JSON) Dtor_str() _dafny.Sequence {
	return _this.Get_().(JSON_String).Str
}

func (_this JSON) Dtor_num() Decimal {
	return _this.Get_().(JSON_Number).Num
}

func (_this JSON) Dtor_obj() _dafny.Sequence {
	return _this.Get_().(JSON_Object).Obj
}

func (_this JSON) Dtor_arr() _dafny.Sequence {
	return _this.Get_().(JSON_Array).Arr
}

func (_this JSON) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case JSON_Null:
		{
			return "Values.JSON.Null"
		}
	case JSON_Bool:
		{
			return "Values.JSON.Bool" + "(" + _dafny.String(data.B) + ")"
		}
	case JSON_String:
		{
			return "Values.JSON.String" + "(" + _dafny.String(data.Str) + ")"
		}
	case JSON_Number:
		{
			return "Values.JSON.Number" + "(" + _dafny.String(data.Num) + ")"
		}
	case JSON_Object:
		{
			return "Values.JSON.Object" + "(" + _dafny.String(data.Obj) + ")"
		}
	case JSON_Array:
		{
			return "Values.JSON.Array" + "(" + _dafny.String(data.Arr) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this JSON) Equals(other JSON) bool {
	switch data1 := _this.Get_().(type) {
	case JSON_Null:
		{
			_, ok := other.Get_().(JSON_Null)
			return ok
		}
	case JSON_Bool:
		{
			data2, ok := other.Get_().(JSON_Bool)
			return ok && data1.B == data2.B
		}
	case JSON_String:
		{
			data2, ok := other.Get_().(JSON_String)
			return ok && data1.Str.Equals(data2.Str)
		}
	case JSON_Number:
		{
			data2, ok := other.Get_().(JSON_Number)
			return ok && data1.Num.Equals(data2.Num)
		}
	case JSON_Object:
		{
			data2, ok := other.Get_().(JSON_Object)
			return ok && data1.Obj.Equals(data2.Obj)
		}
	case JSON_Array:
		{
			data2, ok := other.Get_().(JSON_Array)
			return ok && data1.Arr.Equals(data2.Arr)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this JSON) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(JSON)
	return ok && _this.Equals(typed)
}

func Type_JSON_() _dafny.TypeDescriptor {
	return type_JSON_{}
}

type type_JSON_ struct {
}

func (_this type_JSON_) Default() interface{} {
	return Companion_JSON_.Default()
}

func (_this type_JSON_) String() string {
	return "JSON_Values.JSON"
}
func (_this JSON) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = JSON{}

// End of datatype JSON
