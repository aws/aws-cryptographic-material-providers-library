// Package JSON_ZeroCopy_Serializer
// Dafny module JSON_ZeroCopy_Serializer compiled into Go

package JSON_ZeroCopy_Serializer

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
	return "JSON_ZeroCopy_Serializer.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) Serialize(js m_JSON_Grammar.Structural) m_Wrappers.Result {
	var rbs m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.NewArrayWithValue(nil, _dafny.IntOf(0)))
	_ = rbs
	var _0_writer m_JSON_Utils_Views_Writers.Writer__
	_ = _0_writer
	_0_writer = Companion_Default___.Text(js)
	var _1_valueOrError0 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
	_ = _1_valueOrError0
	_1_valueOrError0 = m_Wrappers.Companion_Default___.Need((_0_writer).Unsaturated_q(), m_JSON_Errors.Companion_SerializationError_.Create_OutOfMemory_())
	if (_1_valueOrError0).IsFailure() {
		rbs = (_1_valueOrError0).PropagateFailure()
		return rbs
	}
	var _2_bs _dafny.Array
	_ = _2_bs
	var _out0 _dafny.Array
	_ = _out0
	_out0 = (_0_writer).ToArray()
	_2_bs = _out0
	rbs = m_Wrappers.Companion_Result_.Create_Success_(_2_bs)
	return rbs
	return rbs
}
func (_static *CompanionStruct_Default___) SerializeTo(js m_JSON_Grammar.Structural, dest _dafny.Array) m_Wrappers.Result {
	var len_ m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(uint32(0))
	_ = len_
	var _0_writer m_JSON_Utils_Views_Writers.Writer__
	_ = _0_writer
	_0_writer = Companion_Default___.Text(js)
	var _1_valueOrError0 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
	_ = _1_valueOrError0
	_1_valueOrError0 = m_Wrappers.Companion_Default___.Need((_0_writer).Unsaturated_q(), m_JSON_Errors.Companion_SerializationError_.Create_OutOfMemory_())
	if (_1_valueOrError0).IsFailure() {
		len_ = (_1_valueOrError0).PropagateFailure()
		return len_
	}
	var _2_valueOrError1 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
	_ = _2_valueOrError1
	_2_valueOrError1 = m_Wrappers.Companion_Default___.Need((_dafny.IntOfUint32((_0_writer).Dtor_length())).Cmp(_dafny.ArrayLen((dest), 0)) <= 0, m_JSON_Errors.Companion_SerializationError_.Create_OutOfMemory_())
	if (_2_valueOrError1).IsFailure() {
		len_ = (_2_valueOrError1).PropagateFailure()
		return len_
	}
	(_0_writer).CopyTo(dest)
	len_ = m_Wrappers.Companion_Result_.Create_Success_((_0_writer).Dtor_length())
	return len_
	return len_
}
func (_static *CompanionStruct_Default___) Text(js m_JSON_Grammar.Structural) m_JSON_Utils_Views_Writers.Writer__ {
	return Companion_Default___.JSON(js, m_JSON_Utils_Views_Writers.Companion_Writer___.Empty())
}
func (_static *CompanionStruct_Default___) JSON(js m_JSON_Grammar.Structural, writer m_JSON_Utils_Views_Writers.Writer__) m_JSON_Utils_Views_Writers.Writer__ {
	return (((writer).Append((js).Dtor_before())).Then((func(_0_js m_JSON_Grammar.Structural) func(m_JSON_Utils_Views_Writers.Writer__) m_JSON_Utils_Views_Writers.Writer__ {
		return func(_1_wr m_JSON_Utils_Views_Writers.Writer__) m_JSON_Utils_Views_Writers.Writer__ {
			return Companion_Default___.Value((_0_js).Dtor_t().(m_JSON_Grammar.Value), _1_wr)
		}
	})(js))).Append((js).Dtor_after())
}
func (_static *CompanionStruct_Default___) Value(v m_JSON_Grammar.Value, writer m_JSON_Utils_Views_Writers.Writer__) m_JSON_Utils_Views_Writers.Writer__ {
	var _source0 m_JSON_Grammar.Value = v
	_ = _source0
	{
		if _source0.Is_Null() {
			var _0_n m_JSON_Utils_Views_Core.View__ = _source0.Get_().(m_JSON_Grammar.Value_Null).N
			_ = _0_n
			return (writer).Append(_0_n)
		}
	}
	{
		if _source0.Is_Bool() {
			var _1_b m_JSON_Utils_Views_Core.View__ = _source0.Get_().(m_JSON_Grammar.Value_Bool).B
			_ = _1_b
			var _2_wr m_JSON_Utils_Views_Writers.Writer__ = (writer).Append(_1_b)
			_ = _2_wr
			return _2_wr
		}
	}
	{
		if _source0.Is_String() {
			var _3_str m_JSON_Grammar.Jstring = _source0.Get_().(m_JSON_Grammar.Value_String).Str
			_ = _3_str
			var _4_wr m_JSON_Utils_Views_Writers.Writer__ = Companion_Default___.String(_3_str, writer)
			_ = _4_wr
			return _4_wr
		}
	}
	{
		if _source0.Is_Number() {
			var _5_num m_JSON_Grammar.Jnumber = _source0.Get_().(m_JSON_Grammar.Value_Number).Num
			_ = _5_num
			var _6_wr m_JSON_Utils_Views_Writers.Writer__ = Companion_Default___.Number(_5_num, writer)
			_ = _6_wr
			return _6_wr
		}
	}
	{
		if _source0.Is_Object() {
			var _7_obj m_JSON_Grammar.Bracketed = _source0.Get_().(m_JSON_Grammar.Value_Object).Obj
			_ = _7_obj
			var _8_wr m_JSON_Utils_Views_Writers.Writer__ = Companion_Default___.Object(_7_obj, writer)
			_ = _8_wr
			return _8_wr
		}
	}
	{
		var _9_arr m_JSON_Grammar.Bracketed = _source0.Get_().(m_JSON_Grammar.Value_Array).Arr
		_ = _9_arr
		var _10_wr m_JSON_Utils_Views_Writers.Writer__ = Companion_Default___.Array(_9_arr, writer)
		_ = _10_wr
		return _10_wr
	}
}
func (_static *CompanionStruct_Default___) String(str m_JSON_Grammar.Jstring, writer m_JSON_Utils_Views_Writers.Writer__) m_JSON_Utils_Views_Writers.Writer__ {
	return (((writer).Append((str).Dtor_lq())).Append((str).Dtor_contents())).Append((str).Dtor_rq())
}
func (_static *CompanionStruct_Default___) Number(num m_JSON_Grammar.Jnumber, writer m_JSON_Utils_Views_Writers.Writer__) m_JSON_Utils_Views_Writers.Writer__ {
	var _0_wr m_JSON_Utils_Views_Writers.Writer__ = ((writer).Append((num).Dtor_minus())).Append((num).Dtor_num())
	_ = _0_wr
	var _1_wr m_JSON_Utils_Views_Writers.Writer__ = (func() m_JSON_Utils_Views_Writers.Writer__ {
		if ((num).Dtor_frac()).Is_NonEmpty() {
			return ((_0_wr).Append((((num).Dtor_frac()).Dtor_t().(m_JSON_Grammar.Jfrac)).Dtor_period())).Append((((num).Dtor_frac()).Dtor_t().(m_JSON_Grammar.Jfrac)).Dtor_num())
		}
		return _0_wr
	})()
	_ = _1_wr
	var _2_wr m_JSON_Utils_Views_Writers.Writer__ = (func() m_JSON_Utils_Views_Writers.Writer__ {
		if ((num).Dtor_exp()).Is_NonEmpty() {
			return (((_1_wr).Append((((num).Dtor_exp()).Dtor_t().(m_JSON_Grammar.Jexp)).Dtor_e())).Append((((num).Dtor_exp()).Dtor_t().(m_JSON_Grammar.Jexp)).Dtor_sign())).Append((((num).Dtor_exp()).Dtor_t().(m_JSON_Grammar.Jexp)).Dtor_num())
		}
		return _1_wr
	})()
	_ = _2_wr
	return _2_wr
}
func (_static *CompanionStruct_Default___) StructuralView(st m_JSON_Grammar.Structural, writer m_JSON_Utils_Views_Writers.Writer__) m_JSON_Utils_Views_Writers.Writer__ {
	return (((writer).Append((st).Dtor_before())).Append((st).Dtor_t().(m_JSON_Utils_Views_Core.View__))).Append((st).Dtor_after())
}
func (_static *CompanionStruct_Default___) Object(obj m_JSON_Grammar.Bracketed, writer m_JSON_Utils_Views_Writers.Writer__) m_JSON_Utils_Views_Writers.Writer__ {
	var _0_wr m_JSON_Utils_Views_Writers.Writer__ = Companion_Default___.StructuralView((obj).Dtor_l(), writer)
	_ = _0_wr
	var _1_wr m_JSON_Utils_Views_Writers.Writer__ = Companion_Default___.Members(obj, _0_wr)
	_ = _1_wr
	var _2_wr m_JSON_Utils_Views_Writers.Writer__ = Companion_Default___.StructuralView((obj).Dtor_r(), _1_wr)
	_ = _2_wr
	return _2_wr
}
func (_static *CompanionStruct_Default___) Array(arr m_JSON_Grammar.Bracketed, writer m_JSON_Utils_Views_Writers.Writer__) m_JSON_Utils_Views_Writers.Writer__ {
	var _0_wr m_JSON_Utils_Views_Writers.Writer__ = Companion_Default___.StructuralView((arr).Dtor_l(), writer)
	_ = _0_wr
	var _1_wr m_JSON_Utils_Views_Writers.Writer__ = Companion_Default___.Items(arr, _0_wr)
	_ = _1_wr
	var _2_wr m_JSON_Utils_Views_Writers.Writer__ = Companion_Default___.StructuralView((arr).Dtor_r(), _1_wr)
	_ = _2_wr
	return _2_wr
}
func (_static *CompanionStruct_Default___) Members(obj m_JSON_Grammar.Bracketed, writer m_JSON_Utils_Views_Writers.Writer__) m_JSON_Utils_Views_Writers.Writer__ {
	var wr m_JSON_Utils_Views_Writers.Writer__ = m_JSON_Utils_Views_Writers.Companion_Writer_.Witness()
	_ = wr
	var _out0 m_JSON_Utils_Views_Writers.Writer__
	_ = _out0
	_out0 = Companion_Default___.MembersImpl(obj, writer)
	wr = _out0
	return wr
}
func (_static *CompanionStruct_Default___) Items(arr m_JSON_Grammar.Bracketed, writer m_JSON_Utils_Views_Writers.Writer__) m_JSON_Utils_Views_Writers.Writer__ {
	var wr m_JSON_Utils_Views_Writers.Writer__ = m_JSON_Utils_Views_Writers.Companion_Writer_.Witness()
	_ = wr
	var _out0 m_JSON_Utils_Views_Writers.Writer__
	_ = _out0
	_out0 = Companion_Default___.ItemsImpl(arr, writer)
	wr = _out0
	return wr
}
func (_static *CompanionStruct_Default___) MembersImpl(obj m_JSON_Grammar.Bracketed, writer m_JSON_Utils_Views_Writers.Writer__) m_JSON_Utils_Views_Writers.Writer__ {
	var wr m_JSON_Utils_Views_Writers.Writer__ = m_JSON_Utils_Views_Writers.Companion_Writer_.Witness()
	_ = wr
	wr = writer
	var _0_members _dafny.Sequence
	_ = _0_members
	_0_members = (obj).Dtor_data()
	var _hi0 _dafny.Int = _dafny.IntOfUint32((_0_members).Cardinality())
	_ = _hi0
	for _1_i := _dafny.Zero; _1_i.Cmp(_hi0) < 0; _1_i = _1_i.Plus(_dafny.One) {
		wr = Companion_Default___.Member((_0_members).Select((_1_i).Uint32()).(m_JSON_Grammar.Suffixed), wr)
	}
	return wr
}
func (_static *CompanionStruct_Default___) ItemsImpl(arr m_JSON_Grammar.Bracketed, writer m_JSON_Utils_Views_Writers.Writer__) m_JSON_Utils_Views_Writers.Writer__ {
	var wr m_JSON_Utils_Views_Writers.Writer__ = m_JSON_Utils_Views_Writers.Companion_Writer_.Witness()
	_ = wr
	wr = writer
	var _0_items _dafny.Sequence
	_ = _0_items
	_0_items = (arr).Dtor_data()
	var _hi0 _dafny.Int = _dafny.IntOfUint32((_0_items).Cardinality())
	_ = _hi0
	for _1_i := _dafny.Zero; _1_i.Cmp(_hi0) < 0; _1_i = _1_i.Plus(_dafny.One) {
		wr = Companion_Default___.Item((_0_items).Select((_1_i).Uint32()).(m_JSON_Grammar.Suffixed), wr)
	}
	return wr
}
func (_static *CompanionStruct_Default___) Member(m m_JSON_Grammar.Suffixed, writer m_JSON_Utils_Views_Writers.Writer__) m_JSON_Utils_Views_Writers.Writer__ {
	var _0_wr m_JSON_Utils_Views_Writers.Writer__ = Companion_Default___.String(((m).Dtor_t().(m_JSON_Grammar.JKeyValue)).Dtor_k(), writer)
	_ = _0_wr
	var _1_wr m_JSON_Utils_Views_Writers.Writer__ = Companion_Default___.StructuralView(((m).Dtor_t().(m_JSON_Grammar.JKeyValue)).Dtor_colon(), _0_wr)
	_ = _1_wr
	var _2_wr m_JSON_Utils_Views_Writers.Writer__ = Companion_Default___.Value(((m).Dtor_t().(m_JSON_Grammar.JKeyValue)).Dtor_v(), _1_wr)
	_ = _2_wr
	var _3_wr m_JSON_Utils_Views_Writers.Writer__ = (func() m_JSON_Utils_Views_Writers.Writer__ {
		if ((m).Dtor_suffix()).Is_Empty() {
			return _2_wr
		}
		return Companion_Default___.StructuralView(((m).Dtor_suffix()).Dtor_t().(m_JSON_Grammar.Structural), _2_wr)
	})()
	_ = _3_wr
	return _3_wr
}
func (_static *CompanionStruct_Default___) Item(m m_JSON_Grammar.Suffixed, writer m_JSON_Utils_Views_Writers.Writer__) m_JSON_Utils_Views_Writers.Writer__ {
	var _0_wr m_JSON_Utils_Views_Writers.Writer__ = Companion_Default___.Value((m).Dtor_t().(m_JSON_Grammar.Value), writer)
	_ = _0_wr
	var _1_wr m_JSON_Utils_Views_Writers.Writer__ = (func() m_JSON_Utils_Views_Writers.Writer__ {
		if ((m).Dtor_suffix()).Is_Empty() {
			return _0_wr
		}
		return Companion_Default___.StructuralView(((m).Dtor_suffix()).Dtor_t().(m_JSON_Grammar.Structural), _0_wr)
	})()
	_ = _1_wr
	return _1_wr
}

// End of class Default__
