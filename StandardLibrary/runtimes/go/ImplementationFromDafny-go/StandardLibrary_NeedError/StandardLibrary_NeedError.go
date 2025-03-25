// Package StandardLibrary_NeedError
// Dafny module StandardLibrary_NeedError compiled into Go

package StandardLibrary_NeedError

import (
	os "os"

	m_BoundedInts "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/BoundedInts"
	m_DivInternals "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/DivInternals"
	m_DivInternalsNonlinear "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/DivInternalsNonlinear"
	m_DivMod "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/DivMod"
	m_FileIO "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/FileIO"
	m_Functions "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Functions"
	m_GeneralInternals "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/GeneralInternals"
	m_Logarithm "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Logarithm"
	m__Math "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Math_"
	m_ModInternals "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/ModInternals"
	m_ModInternalsNonlinear "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/ModInternalsNonlinear"
	m_Mul "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Mul"
	m_MulInternals "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/MulInternals"
	m_MulInternalsNonlinear "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/MulInternalsNonlinear"
	m_Power "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Power"
	m_Relations "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Relations"
	m_Seq "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Seq"
	m_Seq_MergeSort "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Seq_MergeSort"
	m_StandardLibraryInterop "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/StandardLibraryInterop"
	m_StandardLibrary_UInt "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/StandardLibrary_UInt"
	m_UnicodeStrings "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/UnicodeStrings"
	m__Unicode "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Unicode_"
	m_Utf16EncodingForm "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Utf16EncodingForm"
	m_Utf8EncodingForm "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Utf8EncodingForm"
	m_Wrappers "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Wrappers"
	m__System "github.com/dafny-lang/DafnyRuntimeGo/v4/System_"
	_dafny "github.com/dafny-lang/DafnyRuntimeGo/v4/dafny"
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
	return "StandardLibrary_NeedError.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) NeedOutcome(condition bool, error_ func() interface{}) Outcome2 {
	if condition {
		return Companion_Outcome2_.Create_Pass_()
	} else {
		return Companion_Outcome2_.Create_Fail_((error_)())
	}
}

// End of class Default__

// Definition of datatype Outcome2
type Outcome2 struct {
	Data_Outcome2_
}

func (_this Outcome2) Get_() Data_Outcome2_ {
	return _this.Data_Outcome2_
}

type Data_Outcome2_ interface {
	isOutcome2()
}

type CompanionStruct_Outcome2_ struct {
}

var Companion_Outcome2_ = CompanionStruct_Outcome2_{}

type Outcome2_Pass struct {
}

func (Outcome2_Pass) isOutcome2() {}

func (CompanionStruct_Outcome2_) Create_Pass_() Outcome2 {
	return Outcome2{Outcome2_Pass{}}
}

func (_this Outcome2) Is_Pass() bool {
	_, ok := _this.Get_().(Outcome2_Pass)
	return ok
}

type Outcome2_Fail struct {
	Error interface{}
}

func (Outcome2_Fail) isOutcome2() {}

func (CompanionStruct_Outcome2_) Create_Fail_(Error interface{}) Outcome2 {
	return Outcome2{Outcome2_Fail{Error}}
}

func (_this Outcome2) Is_Fail() bool {
	_, ok := _this.Get_().(Outcome2_Fail)
	return ok
}

func (CompanionStruct_Outcome2_) Default() Outcome2 {
	return Companion_Outcome2_.Create_Pass_()
}

func (_this Outcome2) Dtor_error() interface{} {
	return _this.Get_().(Outcome2_Fail).Error
}

func (_this Outcome2) String() string {
	switch data := _this.Get_().(type) {
	case nil:
		return "null"
	case Outcome2_Pass:
		{
			return "NeedError.Outcome2.Pass"
		}
	case Outcome2_Fail:
		{
			return "NeedError.Outcome2.Fail" + "(" + _dafny.String(data.Error) + ")"
		}
	default:
		{
			return "<unexpected>"
		}
	}
}

func (_this Outcome2) Equals(other Outcome2) bool {
	switch data1 := _this.Get_().(type) {
	case Outcome2_Pass:
		{
			_, ok := other.Get_().(Outcome2_Pass)
			return ok
		}
	case Outcome2_Fail:
		{
			data2, ok := other.Get_().(Outcome2_Fail)
			return ok && _dafny.AreEqual(data1.Error, data2.Error)
		}
	default:
		{
			return false // unexpected
		}
	}
}

func (_this Outcome2) EqualsGeneric(other interface{}) bool {
	typed, ok := other.(Outcome2)
	return ok && _this.Equals(typed)
}

func Type_Outcome2_() _dafny.TypeDescriptor {
	return type_Outcome2_{}
}

type type_Outcome2_ struct {
}

func (_this type_Outcome2_) Default() interface{} {
	return Companion_Outcome2_.Default()
}

func (_this type_Outcome2_) String() string {
	return "StandardLibrary_NeedError.Outcome2"
}
func (_this Outcome2) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = Outcome2{}

func (_this Outcome2) IsFailure() bool {
	{
		return (_this).Is_Fail()
	}
}
func (_this Outcome2) PropagateFailure() m_Wrappers.Outcome {
	{
		return m_Wrappers.Companion_Outcome_.Create_Fail_((_this).Dtor_error())
	}
}

// End of datatype Outcome2
