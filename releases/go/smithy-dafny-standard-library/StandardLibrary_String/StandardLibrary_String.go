// Package StandardLibrary_String
// Dafny module StandardLibrary_String compiled into Go

package StandardLibrary_String

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
	m_StandardLibrary_MemoryMath "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/StandardLibrary_MemoryMath"
	m_StandardLibrary_Sequence "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/StandardLibrary_Sequence"
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
var _ m_StandardLibrary_MemoryMath.Dummy__
var _ m_StandardLibrary_Sequence.Dummy__

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
func (_static *CompanionStruct_Default___) SearchAndReplace(source _dafny.Sequence, old__str _dafny.Sequence, new__str _dafny.Sequence) _dafny.Sequence {
	var o _dafny.Sequence = _dafny.EmptySeq
	_ = o
	var _0_x _dafny.Tuple
	_ = _0_x
	var _out0 _dafny.Tuple
	_ = _out0
	_out0 = Companion_Default___.SearchAndReplacePos(source, old__str, new__str, uint64(0))
	_0_x = _out0
	o = (*(_0_x).IndexInt(0)).(_dafny.Sequence)
	return o
	return o
}
func (_static *CompanionStruct_Default___) SearchAndReplacePos(source _dafny.Sequence, old__str _dafny.Sequence, new__str _dafny.Sequence, pos uint64) _dafny.Tuple {
	var o _dafny.Tuple = _dafny.TupleOf(_dafny.EmptySeq, m_Wrappers.Companion_Option_.Default())
	_ = o
	var _0_old__pos m_Wrappers.Option
	_ = _0_old__pos
	var _out0 m_Wrappers.Option
	_ = _out0
	_out0 = Companion_Default___.HasSubStringPos(source, old__str, pos)
	_0_old__pos = _out0
	if (_0_old__pos).Is_None() {
		o = _dafny.TupleOf(source, m_Wrappers.Companion_Option_.Create_None_())
		return o
	} else {
		var _1_source__len uint64
		_ = _1_source__len
		_1_source__len = uint64((source).Cardinality())
		var _2_old__str__len uint64
		_ = _2_old__str__len
		_2_old__str__len = uint64((old__str).Cardinality())
		var _3_new__str__len uint64
		_ = _3_new__str__len
		_3_new__str__len = uint64((new__str).Cardinality())
		o = _dafny.TupleOf(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate((source).Take(uint32((_0_old__pos).Dtor_value().(uint64))), new__str), (source).Drop(uint32(((_0_old__pos).Dtor_value().(uint64))+(_2_old__str__len)))), m_Wrappers.Companion_Option_.Create_Some_(m_StandardLibrary_MemoryMath.Companion_Default___.Add((_0_old__pos).Dtor_value().(uint64), _3_new__str__len)))
		o = o
		return o
	}
	return o
}
func (_static *CompanionStruct_Default___) BadStart(source _dafny.Sequence, pos uint64, chars _dafny.Sequence) bool {
	if (pos) == (uint64(0)) {
		return false
	} else {
		return _dafny.Companion_Sequence_.Contains(chars, (source).Select(uint32((pos)-(func() uint64 { return (uint64(1)) })())).(interface{}))
	}
}
func (_static *CompanionStruct_Default___) BadEnd(source _dafny.Sequence, pos uint64, match__len uint64, chars _dafny.Sequence) bool {
	var _0_source__len uint64 = uint64((source).Cardinality())
	_ = _0_source__len
	if (m_StandardLibrary_MemoryMath.Companion_Default___.Add(pos, match__len)) >= (_0_source__len) {
		return false
	} else {
		return _dafny.Companion_Sequence_.Contains(chars, (source).Select(uint32((pos)+(match__len))).(interface{}))
	}
}
func (_static *CompanionStruct_Default___) BadMatch(source _dafny.Sequence, pos uint64, match__len uint64, chars _dafny.Sequence) bool {
	return (Companion_Default___.BadStart(source, pos, chars)) || (Companion_Default___.BadEnd(source, pos, match__len, chars))
}
func (_static *CompanionStruct_Default___) SearchAndReplacePosWhole(source _dafny.Sequence, old__str _dafny.Sequence, new__str _dafny.Sequence, xpos uint64, chars _dafny.Sequence) _dafny.Tuple {
	var o _dafny.Tuple = _dafny.TupleOf(_dafny.EmptySeq, m_Wrappers.Companion_Option_.Default())
	_ = o
	var _0_old__str__len uint64
	_ = _0_old__str__len
	_0_old__str__len = uint64((old__str).Cardinality())
	var _1_pos uint64
	_ = _1_pos
	_1_pos = xpos
	for (_1_pos) < (uint64((source).Cardinality())) {
		var _2_old__pos m_Wrappers.Option
		_ = _2_old__pos
		var _out0 m_Wrappers.Option
		_ = _out0
		_out0 = Companion_Default___.HasSubStringPos(source, old__str, _1_pos)
		_2_old__pos = _out0
		if (_2_old__pos).Is_None() {
			o = _dafny.TupleOf(source, m_Wrappers.Companion_Option_.Create_None_())
			return o
		} else if Companion_Default___.BadMatch(source, (_2_old__pos).Dtor_value().(uint64), _0_old__str__len, chars) {
			_1_pos = ((_2_old__pos).Dtor_value().(uint64)) + (uint64(1))
		} else {
			var _3_source__len uint64
			_ = _3_source__len
			_3_source__len = uint64((source).Cardinality())
			var _4_new__str__len uint64
			_ = _4_new__str__len
			_4_new__str__len = uint64((new__str).Cardinality())
			o = _dafny.TupleOf(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate((source).Take(uint32((_2_old__pos).Dtor_value().(uint64))), new__str), (source).Drop(uint32(((_2_old__pos).Dtor_value().(uint64))+(_0_old__str__len)))), m_Wrappers.Companion_Option_.Create_Some_(m_StandardLibrary_MemoryMath.Companion_Default___.Add((_2_old__pos).Dtor_value().(uint64), _4_new__str__len)))
			o = o
			return o
		}
	}
	o = _dafny.TupleOf(source, m_Wrappers.Companion_Option_.Create_None_())
	return o
	return o
}
func (_static *CompanionStruct_Default___) SearchAndReplaceWhole(source _dafny.Sequence, old__str _dafny.Sequence, new__str _dafny.Sequence, chars _dafny.Sequence) _dafny.Tuple {
	var o _dafny.Tuple = _dafny.TupleOf(_dafny.EmptySeq, m_Wrappers.Companion_Option_.Default())
	_ = o
	var _out0 _dafny.Tuple
	_ = _out0
	_out0 = Companion_Default___.SearchAndReplacePosWhole(source, old__str, new__str, uint64(0), chars)
	o = _out0
	return o
}
func (_static *CompanionStruct_Default___) SearchAndReplaceAll(source__in _dafny.Sequence, old__str _dafny.Sequence, new__str _dafny.Sequence) _dafny.Sequence {
	var o _dafny.Sequence = _dafny.EmptySeq
	_ = o
	var _0_pos uint64
	_ = _0_pos
	_0_pos = uint64(0)
	var _1_source _dafny.Sequence
	_ = _1_source
	_1_source = source__in
	for true {
		var _2_res _dafny.Tuple
		_ = _2_res
		var _out0 _dafny.Tuple
		_ = _out0
		_out0 = Companion_Default___.SearchAndReplacePos(_1_source, old__str, new__str, _0_pos)
		_2_res = _out0
		if ((*(_2_res).IndexInt(1)).(m_Wrappers.Option)).Is_None() {
			_0_pos = uint64((_1_source).Cardinality())
			o = (*(_2_res).IndexInt(0)).(_dafny.Sequence)
			return o
		}
		_1_source = (*(_2_res).IndexInt(0)).(_dafny.Sequence)
		_0_pos = ((*(_2_res).IndexInt(1)).(m_Wrappers.Option)).Dtor_value().(uint64)
	}
	return o
}
func (_static *CompanionStruct_Default___) SearchAndReplaceAllWhole(source__in _dafny.Sequence, old__str _dafny.Sequence, new__str _dafny.Sequence, chars _dafny.Sequence) _dafny.Sequence {
	var o _dafny.Sequence = _dafny.EmptySeq
	_ = o
	var _0_pos uint64
	_ = _0_pos
	_0_pos = uint64(0)
	var _1_source _dafny.Sequence
	_ = _1_source
	_1_source = source__in
	for true {
		var _2_res _dafny.Tuple
		_ = _2_res
		var _out0 _dafny.Tuple
		_ = _out0
		_out0 = Companion_Default___.SearchAndReplacePosWhole(_1_source, old__str, new__str, _0_pos, chars)
		_2_res = _out0
		if ((*(_2_res).IndexInt(1)).(m_Wrappers.Option)).Is_None() {
			_0_pos = uint64((_1_source).Cardinality())
			o = (*(_2_res).IndexInt(0)).(_dafny.Sequence)
			return o
		}
		_1_source = (*(_2_res).IndexInt(0)).(_dafny.Sequence)
		_0_pos = ((*(_2_res).IndexInt(1)).(m_Wrappers.Option)).Dtor_value().(uint64)
	}
	return o
}
func (_static *CompanionStruct_Default___) HasSubString(haystack _dafny.Sequence, needle _dafny.Sequence) m_Wrappers.Option {
	var o m_Wrappers.Option = m_Wrappers.Companion_Option_.Default()
	_ = o
	if (uint64((haystack).Cardinality())) < (uint64((needle).Cardinality())) {
		o = m_Wrappers.Companion_Option_.Create_None_()
		return o
	}
	var _0_size uint64
	_ = _0_size
	_0_size = uint64((needle).Cardinality())
	var _1_limit uint64
	_ = _1_limit
	_1_limit = m_StandardLibrary_MemoryMath.Companion_Default___.Add((uint64((haystack).Cardinality()))-(func() uint64 { return (_0_size) })(), uint64(1))
	var _hi0 uint64 = _1_limit
	_ = _hi0
	for _2_index := uint64(0); _2_index < _hi0; _2_index++ {
		if m_StandardLibrary_Sequence.Companion_Default___.SequenceEqual(haystack, needle, _2_index, uint64(0), _0_size) {
			o = m_Wrappers.Companion_Option_.Create_Some_(_dafny.IntOfUint64(_2_index))
			return o
		}
	}
	o = m_Wrappers.Companion_Option_.Create_None_()
	return o
	return o
}
func (_static *CompanionStruct_Default___) HasSubStringPos(haystack _dafny.Sequence, needle _dafny.Sequence, pos uint64) m_Wrappers.Option {
	var o m_Wrappers.Option = m_Wrappers.Companion_Option_.Default()
	_ = o
	if ((uint64((haystack).Cardinality())) - (func() uint64 { return (pos) })()) < (uint64((needle).Cardinality())) {
		o = m_Wrappers.Companion_Option_.Create_None_()
		return o
	}
	var _0_size uint64
	_ = _0_size
	_0_size = uint64((needle).Cardinality())
	var _1_limit uint64
	_ = _1_limit
	_1_limit = m_StandardLibrary_MemoryMath.Companion_Default___.Add((uint64((haystack).Cardinality()))-(func() uint64 { return (_0_size) })(), uint64(1))
	var _hi0 uint64 = _1_limit
	_ = _hi0
	for _2_index := pos; _2_index < _hi0; _2_index++ {
		if m_StandardLibrary_Sequence.Companion_Default___.SequenceEqual(haystack, needle, _2_index, uint64(0), _0_size) {
			o = m_Wrappers.Companion_Option_.Create_Some_(_2_index)
			return o
		}
	}
	o = m_Wrappers.Companion_Option_.Create_None_()
	return o
	return o
}
func (_static *CompanionStruct_Default___) Base10() _dafny.Sequence {
	return _dafny.SeqOfChars(_dafny.Char('0'), _dafny.Char('1'), _dafny.Char('2'), _dafny.Char('3'), _dafny.Char('4'), _dafny.Char('5'), _dafny.Char('6'), _dafny.Char('7'), _dafny.Char('8'), _dafny.Char('9'))
}
func (_static *CompanionStruct_Default___) AlphaNumeric() _dafny.Sequence {
	return _dafny.SeqOfString("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
}
func (_static *CompanionStruct_Default___) AlphaNumericUnder() _dafny.Sequence {
	return _dafny.SeqOfString("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_")
}

// End of class Default__
