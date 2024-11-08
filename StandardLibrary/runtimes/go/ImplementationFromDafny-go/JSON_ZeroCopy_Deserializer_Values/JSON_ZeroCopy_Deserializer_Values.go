// Package JSON_ZeroCopy_Deserializer_Values
// Dafny module JSON_ZeroCopy_Deserializer_Values compiled into Go

package JSON_ZeroCopy_Deserializer_Values

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
	m_JSON_ConcreteSyntax_Spec "github.com/dafny-lang/DafnyStandardLibGo/JSON_ConcreteSyntax_Spec"
	m_JSON_ConcreteSyntax_SpecProperties "github.com/dafny-lang/DafnyStandardLibGo/JSON_ConcreteSyntax_SpecProperties"
	m_JSON_Deserializer "github.com/dafny-lang/DafnyStandardLibGo/JSON_Deserializer"
	m_JSON_Deserializer_ByteStrConversion "github.com/dafny-lang/DafnyStandardLibGo/JSON_Deserializer_ByteStrConversion"
	m_JSON_Deserializer_Uint16StrConversion "github.com/dafny-lang/DafnyStandardLibGo/JSON_Deserializer_Uint16StrConversion"
	m_JSON_Errors "github.com/dafny-lang/DafnyStandardLibGo/JSON_Errors"
	m_JSON_Grammar "github.com/dafny-lang/DafnyStandardLibGo/JSON_Grammar"
	m_JSON_Serializer "github.com/dafny-lang/DafnyStandardLibGo/JSON_Serializer"
	m_JSON_Serializer_ByteStrConversion "github.com/dafny-lang/DafnyStandardLibGo/JSON_Serializer_ByteStrConversion"
	m_JSON_Spec "github.com/dafny-lang/DafnyStandardLibGo/JSON_Spec"
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
	m_JSON_Values "github.com/dafny-lang/DafnyStandardLibGo/JSON_Values"
	m_JSON_ZeroCopy_Deserializer_ArrayParams "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer_ArrayParams"
	m_JSON_ZeroCopy_Deserializer_Arrays "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer_Arrays"
	m_JSON_ZeroCopy_Deserializer_Constants "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer_Constants"
	m_JSON_ZeroCopy_Deserializer_Core "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer_Core"
	m_JSON_ZeroCopy_Deserializer_Numbers "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer_Numbers"
	m_JSON_ZeroCopy_Deserializer_ObjectParams "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer_ObjectParams"
	m_JSON_ZeroCopy_Deserializer_Objects "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer_Objects"
	m_JSON_ZeroCopy_Deserializer_Strings "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Deserializer_Strings"
	m_JSON_ZeroCopy_Serializer "github.com/dafny-lang/DafnyStandardLibGo/JSON_ZeroCopy_Serializer"
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
var _ m_JSON_Values.Dummy__
var _ m_JSON_Spec.Dummy__
var _ m_JSON_Grammar.Dummy__
var _ m_JSON_Serializer_ByteStrConversion.Dummy__
var _ m_JSON_Serializer.Dummy__
var _ m_JSON_Deserializer_Uint16StrConversion.Dummy__
var _ m_JSON_Deserializer_ByteStrConversion.Dummy__
var _ m_JSON_Deserializer.Dummy__
var _ m_JSON_ConcreteSyntax_Spec.Dummy__
var _ m_JSON_ConcreteSyntax_SpecProperties.Dummy__
var _ m_JSON_ZeroCopy_Serializer.Dummy__
var _ m_JSON_ZeroCopy_Deserializer_Core.Dummy__
var _ m_JSON_ZeroCopy_Deserializer_Strings.Dummy__
var _ m_JSON_ZeroCopy_Deserializer_Numbers.Dummy__
var _ m_JSON_ZeroCopy_Deserializer_ObjectParams.Dummy__
var _ m_JSON_ZeroCopy_Deserializer_Objects.Dummy__
var _ m_JSON_ZeroCopy_Deserializer_ArrayParams.Dummy__
var _ m_JSON_ZeroCopy_Deserializer_Arrays.Dummy__
var _ m_JSON_ZeroCopy_Deserializer_Constants.Dummy__

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
	return "JSON_ZeroCopy_Deserializer_Values.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) Value(cs m_JSON_Utils_Cursors.Cursor__) m_Wrappers.Result {
	var _0_c int16 = (cs).Peek()
	_ = _0_c
	if (_0_c) == (int16(_dafny.Char('{'))) {
		var _1_valueOrError0 m_Wrappers.Result = m_JSON_ZeroCopy_Deserializer_Objects.Companion_Default___.Object(cs, Companion_Default___.ValueParser(cs))
		_ = _1_valueOrError0
		if (_1_valueOrError0).IsFailure() {
			return (_1_valueOrError0).PropagateFailure()
		} else {
			var _let_tmp_rhs0 m_JSON_Utils_Cursors.Split = (_1_valueOrError0).Extract().(m_JSON_Utils_Cursors.Split)
			_ = _let_tmp_rhs0
			var _2_obj m_JSON_Grammar.Bracketed = _let_tmp_rhs0.Get_().(m_JSON_Utils_Cursors.Split_SP).T.(m_JSON_Grammar.Bracketed)
			_ = _2_obj
			var _3_cs_k m_JSON_Utils_Cursors.Cursor__ = _let_tmp_rhs0.Get_().(m_JSON_Utils_Cursors.Split_SP).Cs
			_ = _3_cs_k
			var _4_v m_JSON_Grammar.Value = m_JSON_Grammar.Companion_Value_.Create_Object_(_2_obj)
			_ = _4_v
			var _5_sp m_JSON_Utils_Cursors.Split = m_JSON_Utils_Cursors.Companion_Split_.Create_SP_(_4_v, _3_cs_k)
			_ = _5_sp
			return m_Wrappers.Companion_Result_.Create_Success_(_5_sp)
		}
	} else if (_0_c) == (int16(_dafny.Char('['))) {
		var _6_valueOrError1 m_Wrappers.Result = m_JSON_ZeroCopy_Deserializer_Arrays.Companion_Default___.Array(cs, Companion_Default___.ValueParser(cs))
		_ = _6_valueOrError1
		if (_6_valueOrError1).IsFailure() {
			return (_6_valueOrError1).PropagateFailure()
		} else {
			var _let_tmp_rhs1 m_JSON_Utils_Cursors.Split = (_6_valueOrError1).Extract().(m_JSON_Utils_Cursors.Split)
			_ = _let_tmp_rhs1
			var _7_arr m_JSON_Grammar.Bracketed = _let_tmp_rhs1.Get_().(m_JSON_Utils_Cursors.Split_SP).T.(m_JSON_Grammar.Bracketed)
			_ = _7_arr
			var _8_cs_k m_JSON_Utils_Cursors.Cursor__ = _let_tmp_rhs1.Get_().(m_JSON_Utils_Cursors.Split_SP).Cs
			_ = _8_cs_k
			var _9_v m_JSON_Grammar.Value = m_JSON_Grammar.Companion_Value_.Create_Array_(_7_arr)
			_ = _9_v
			var _10_sp m_JSON_Utils_Cursors.Split = m_JSON_Utils_Cursors.Companion_Split_.Create_SP_(_9_v, _8_cs_k)
			_ = _10_sp
			return m_Wrappers.Companion_Result_.Create_Success_(_10_sp)
		}
	} else if (_0_c) == (int16(_dafny.Char('"'))) {
		var _11_valueOrError2 m_Wrappers.Result = m_JSON_ZeroCopy_Deserializer_Strings.Companion_Default___.String(cs)
		_ = _11_valueOrError2
		if (_11_valueOrError2).IsFailure() {
			return (_11_valueOrError2).PropagateFailure()
		} else {
			var _let_tmp_rhs2 m_JSON_Utils_Cursors.Split = (_11_valueOrError2).Extract().(m_JSON_Utils_Cursors.Split)
			_ = _let_tmp_rhs2
			var _12_str m_JSON_Grammar.Jstring = _let_tmp_rhs2.Get_().(m_JSON_Utils_Cursors.Split_SP).T.(m_JSON_Grammar.Jstring)
			_ = _12_str
			var _13_cs_k m_JSON_Utils_Cursors.Cursor__ = _let_tmp_rhs2.Get_().(m_JSON_Utils_Cursors.Split_SP).Cs
			_ = _13_cs_k
			return m_Wrappers.Companion_Result_.Create_Success_(m_JSON_Utils_Cursors.Companion_Split_.Create_SP_(m_JSON_Grammar.Companion_Value_.Create_String_(_12_str), _13_cs_k))
		}
	} else if (_0_c) == (int16(_dafny.Char('t'))) {
		var _14_valueOrError3 m_Wrappers.Result = m_JSON_ZeroCopy_Deserializer_Constants.Companion_Default___.Constant(cs, m_JSON_Grammar.Companion_Default___.TRUE())
		_ = _14_valueOrError3
		if (_14_valueOrError3).IsFailure() {
			return (_14_valueOrError3).PropagateFailure()
		} else {
			var _let_tmp_rhs3 m_JSON_Utils_Cursors.Split = (_14_valueOrError3).Extract().(m_JSON_Utils_Cursors.Split)
			_ = _let_tmp_rhs3
			var _15_cst m_JSON_Utils_Views_Core.View__ = _let_tmp_rhs3.Get_().(m_JSON_Utils_Cursors.Split_SP).T.(m_JSON_Utils_Views_Core.View__)
			_ = _15_cst
			var _16_cs_k m_JSON_Utils_Cursors.Cursor__ = _let_tmp_rhs3.Get_().(m_JSON_Utils_Cursors.Split_SP).Cs
			_ = _16_cs_k
			return m_Wrappers.Companion_Result_.Create_Success_(m_JSON_Utils_Cursors.Companion_Split_.Create_SP_(m_JSON_Grammar.Companion_Value_.Create_Bool_(_15_cst), _16_cs_k))
		}
	} else if (_0_c) == (int16(_dafny.Char('f'))) {
		var _17_valueOrError4 m_Wrappers.Result = m_JSON_ZeroCopy_Deserializer_Constants.Companion_Default___.Constant(cs, m_JSON_Grammar.Companion_Default___.FALSE())
		_ = _17_valueOrError4
		if (_17_valueOrError4).IsFailure() {
			return (_17_valueOrError4).PropagateFailure()
		} else {
			var _let_tmp_rhs4 m_JSON_Utils_Cursors.Split = (_17_valueOrError4).Extract().(m_JSON_Utils_Cursors.Split)
			_ = _let_tmp_rhs4
			var _18_cst m_JSON_Utils_Views_Core.View__ = _let_tmp_rhs4.Get_().(m_JSON_Utils_Cursors.Split_SP).T.(m_JSON_Utils_Views_Core.View__)
			_ = _18_cst
			var _19_cs_k m_JSON_Utils_Cursors.Cursor__ = _let_tmp_rhs4.Get_().(m_JSON_Utils_Cursors.Split_SP).Cs
			_ = _19_cs_k
			return m_Wrappers.Companion_Result_.Create_Success_(m_JSON_Utils_Cursors.Companion_Split_.Create_SP_(m_JSON_Grammar.Companion_Value_.Create_Bool_(_18_cst), _19_cs_k))
		}
	} else if (_0_c) == (int16(_dafny.Char('n'))) {
		var _20_valueOrError5 m_Wrappers.Result = m_JSON_ZeroCopy_Deserializer_Constants.Companion_Default___.Constant(cs, m_JSON_Grammar.Companion_Default___.NULL())
		_ = _20_valueOrError5
		if (_20_valueOrError5).IsFailure() {
			return (_20_valueOrError5).PropagateFailure()
		} else {
			var _let_tmp_rhs5 m_JSON_Utils_Cursors.Split = (_20_valueOrError5).Extract().(m_JSON_Utils_Cursors.Split)
			_ = _let_tmp_rhs5
			var _21_cst m_JSON_Utils_Views_Core.View__ = _let_tmp_rhs5.Get_().(m_JSON_Utils_Cursors.Split_SP).T.(m_JSON_Utils_Views_Core.View__)
			_ = _21_cst
			var _22_cs_k m_JSON_Utils_Cursors.Cursor__ = _let_tmp_rhs5.Get_().(m_JSON_Utils_Cursors.Split_SP).Cs
			_ = _22_cs_k
			return m_Wrappers.Companion_Result_.Create_Success_(m_JSON_Utils_Cursors.Companion_Split_.Create_SP_(m_JSON_Grammar.Companion_Value_.Create_Null_(_21_cst), _22_cs_k))
		}
	} else {
		var _23_valueOrError6 m_Wrappers.Result = m_JSON_ZeroCopy_Deserializer_Numbers.Companion_Default___.Number(cs)
		_ = _23_valueOrError6
		if (_23_valueOrError6).IsFailure() {
			return (_23_valueOrError6).PropagateFailure()
		} else {
			var _let_tmp_rhs6 m_JSON_Utils_Cursors.Split = (_23_valueOrError6).Extract().(m_JSON_Utils_Cursors.Split)
			_ = _let_tmp_rhs6
			var _24_num m_JSON_Grammar.Jnumber = _let_tmp_rhs6.Get_().(m_JSON_Utils_Cursors.Split_SP).T.(m_JSON_Grammar.Jnumber)
			_ = _24_num
			var _25_cs_k m_JSON_Utils_Cursors.Cursor__ = _let_tmp_rhs6.Get_().(m_JSON_Utils_Cursors.Split_SP).Cs
			_ = _25_cs_k
			var _26_v m_JSON_Grammar.Value = m_JSON_Grammar.Companion_Value_.Create_Number_(_24_num)
			_ = _26_v
			var _27_sp m_JSON_Utils_Cursors.Split = m_JSON_Utils_Cursors.Companion_Split_.Create_SP_(_26_v, _25_cs_k)
			_ = _27_sp
			return m_Wrappers.Companion_Result_.Create_Success_(_27_sp)
		}
	}
}
func (_static *CompanionStruct_Default___) ValueParser(cs m_JSON_Utils_Cursors.Cursor__) m_JSON_Utils_Parsers.SubParser__ {
	var _0_pre func(m_JSON_Utils_Cursors.Cursor__) bool = (func(_1_cs m_JSON_Utils_Cursors.Cursor__) func(m_JSON_Utils_Cursors.Cursor__) bool {
		return func(_2_ps_k m_JSON_Utils_Cursors.Cursor__) bool {
			return ((_2_ps_k).Length()) < ((_1_cs).Length())
		}
	})(cs)
	_ = _0_pre
	var _3_fn func(m_JSON_Utils_Cursors.Cursor__) m_Wrappers.Result = (func(_4_pre func(m_JSON_Utils_Cursors.Cursor__) bool) func(m_JSON_Utils_Cursors.Cursor__) m_Wrappers.Result {
		return func(_5_ps_k m_JSON_Utils_Cursors.Cursor__) m_Wrappers.Result {
			return Companion_Default___.Value(_5_ps_k)
		}
	})(_0_pre)
	_ = _3_fn
	return m_JSON_Utils_Parsers.Companion_SubParser___.Create_SubParser_(func(coer59 func(m_JSON_Utils_Cursors.Cursor__) m_Wrappers.Result) func(m_JSON_Utils_Cursors.Cursor__) m_Wrappers.Result {
		return func(arg63 m_JSON_Utils_Cursors.Cursor__) m_Wrappers.Result {
			return coer59(arg63)
		}
	}(_3_fn))
}

// End of class Default__
