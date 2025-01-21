// Package Base64
// Dafny module Base64 compiled into Go

package Base64

import (
	os "os"

	m_BoundedInts "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/BoundedInts"
	m_DivInternals "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/DivInternals"
	m_DivInternalsNonlinear "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/DivInternalsNonlinear"
	m_DivMod "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/DivMod"
	m_FileIO "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/FileIO"
	m_FloatCompare "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/FloatCompare"
	m_Functions "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Functions"
	m_GeneralInternals "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/GeneralInternals"
	m_GetOpt "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/GetOpt"
	m_HexStrings "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/HexStrings"
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
	m_Sorting "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Sorting"
	m_StandardLibrary "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/StandardLibrary"
	m_StandardLibraryInterop "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/StandardLibraryInterop"
	m_StandardLibrary_Sequence "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/StandardLibrary_Sequence"
	m_StandardLibrary_String "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/StandardLibrary_String"
	m_StandardLibrary_UInt "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/StandardLibrary_UInt"
	m_Streams "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/Streams"
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
var _ m_StandardLibrary_Sequence.Dummy__
var _ m_StandardLibrary_String.Dummy__
var _ m_StandardLibrary.Dummy__
var _ m_Streams.Dummy__
var _ m_Sorting.Dummy__
var _ m_HexStrings.Dummy__
var _ m_GetOpt.Dummy__
var _ m_FloatCompare.Dummy__

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
	return "Base64.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) IsBase64Char(c _dafny.Char) bool {
	return (((((c) == (_dafny.Char('+'))) || ((c) == (_dafny.Char('/')))) || (((_dafny.Char('0')) <= (c)) && ((c) <= (_dafny.Char('9'))))) || (((_dafny.Char('A')) <= (c)) && ((c) <= (_dafny.Char('Z'))))) || (((_dafny.Char('a')) <= (c)) && ((c) <= (_dafny.Char('z'))))
}
func (_static *CompanionStruct_Default___) IsUnpaddedBase64String(s _dafny.Sequence) bool {
	return (((_dafny.IntOfUint32((s).Cardinality())).Modulo(_dafny.IntOfInt64(4))).Sign() == 0) && (_dafny.Quantifier((s).UniqueElements(), true, func(_forall_var_0 _dafny.Char) bool {
		var _0_k _dafny.Char
		_0_k = interface{}(_forall_var_0).(_dafny.Char)
		return !(_dafny.Companion_Sequence_.Contains(s, _0_k)) || (Companion_Default___.IsBase64Char(_0_k))
	}))
}
func (_static *CompanionStruct_Default___) IndexToChar(i uint8) _dafny.Char {
	if (i) == (uint8(63)) {
		return _dafny.Char('/')
	} else if (i) == (uint8(62)) {
		return _dafny.Char('+')
	} else if ((uint8(52)) <= (i)) && ((i) <= (uint8(61))) {
		return _dafny.Char(((i) - (func() uint8 { return (uint8(4)) })()))
	} else if ((uint8(26)) <= (i)) && ((i) <= (uint8(51))) {
		return (_dafny.Char((i))) + (_dafny.Char((_dafny.IntOfInt64(71)).Int32()))
	} else {
		return (_dafny.Char((i))) + (_dafny.Char((_dafny.IntOfInt64(65)).Int32()))
	}
}
func (_static *CompanionStruct_Default___) CharToIndex(c _dafny.Char) uint8 {
	if (c) == (_dafny.Char('/')) {
		return uint8(63)
	} else if (c) == (_dafny.Char('+')) {
		return uint8(62)
	} else if ((_dafny.Char('0')) <= (c)) && ((c) <= (_dafny.Char('9'))) {
		return uint8((c) + (_dafny.Char((_dafny.IntOfInt64(4)).Int32())))
	} else if ((_dafny.Char('a')) <= (c)) && ((c) <= (_dafny.Char('z'))) {
		return uint8((c) - (_dafny.Char((_dafny.IntOfInt64(71)).Int32())))
	} else {
		return uint8((c) - (_dafny.Char((_dafny.IntOfInt64(65)).Int32())))
	}
}
func (_static *CompanionStruct_Default___) UInt24ToSeq(x uint32) _dafny.Sequence {
	var _0_b0 uint8 = uint8((x) / (uint32(65536)))
	_ = _0_b0
	var _1_x0 uint32 = (x) - (func() uint32 { return ((uint32(_0_b0)) * (uint32(65536))) })()
	_ = _1_x0
	var _2_b1 uint8 = uint8((_1_x0) / (uint32(256)))
	_ = _2_b1
	var _3_b2 uint8 = uint8((_1_x0) % (uint32(256)))
	_ = _3_b2
	return _dafny.SeqOf(_0_b0, _2_b1, _3_b2)
}
func (_static *CompanionStruct_Default___) SeqToUInt24(s _dafny.Sequence) uint32 {
	return (((uint32((s).Select(0).(uint8))) * (uint32(65536))) + ((uint32((s).Select(1).(uint8))) * (uint32(256)))) + (uint32((s).Select(2).(uint8)))
}
func (_static *CompanionStruct_Default___) UInt24ToIndexSeq(x uint32) _dafny.Sequence {
	var _0_b0 uint8 = uint8((x) / (uint32(262144)))
	_ = _0_b0
	var _1_x0 uint32 = (x) - (func() uint32 { return ((uint32(_0_b0)) * (uint32(262144))) })()
	_ = _1_x0
	var _2_b1 uint8 = uint8((_1_x0) / (uint32(4096)))
	_ = _2_b1
	var _3_x1 uint32 = (_1_x0) - (func() uint32 { return ((uint32(_2_b1)) * (uint32(4096))) })()
	_ = _3_x1
	var _4_b2 uint8 = uint8((_3_x1) / (uint32(64)))
	_ = _4_b2
	var _5_b3 uint8 = uint8((_3_x1) % (uint32(64)))
	_ = _5_b3
	return _dafny.SeqOf(_0_b0, _2_b1, _4_b2, _5_b3)
}
func (_static *CompanionStruct_Default___) IndexSeqToUInt24(s _dafny.Sequence) uint32 {
	return ((((uint32((s).Select(0).(uint8))) * (uint32(262144))) + ((uint32((s).Select(1).(uint8))) * (uint32(4096)))) + ((uint32((s).Select(2).(uint8))) * (uint32(64)))) + (uint32((s).Select(3).(uint8)))
}
func (_static *CompanionStruct_Default___) DecodeBlock(s _dafny.Sequence) _dafny.Sequence {
	return Companion_Default___.UInt24ToSeq(Companion_Default___.IndexSeqToUInt24(s))
}
func (_static *CompanionStruct_Default___) EncodeBlock(s _dafny.Sequence) _dafny.Sequence {
	return Companion_Default___.UInt24ToIndexSeq(Companion_Default___.SeqToUInt24(s))
}
func (_static *CompanionStruct_Default___) DecodeRecursively(s _dafny.Sequence) _dafny.Sequence {
	var _0___accumulator _dafny.Sequence = _dafny.SeqOf()
	_ = _0___accumulator
	goto TAIL_CALL_START
TAIL_CALL_START:
	if (_dafny.IntOfUint32((s).Cardinality())).Sign() == 0 {
		return _dafny.Companion_Sequence_.Concatenate(_0___accumulator, _dafny.SeqOf())
	} else {
		_0___accumulator = _dafny.Companion_Sequence_.Concatenate(_0___accumulator, Companion_Default___.DecodeBlock((s).Take(4)))
		var _in0 _dafny.Sequence = (s).Drop(4)
		_ = _in0
		s = _in0
		goto TAIL_CALL_START
	}
}
func (_static *CompanionStruct_Default___) EncodeRecursively(b _dafny.Sequence) _dafny.Sequence {
	var _0___accumulator _dafny.Sequence = _dafny.SeqOf()
	_ = _0___accumulator
	goto TAIL_CALL_START
TAIL_CALL_START:
	if (_dafny.IntOfUint32((b).Cardinality())).Sign() == 0 {
		return _dafny.Companion_Sequence_.Concatenate(_0___accumulator, _dafny.SeqOf())
	} else {
		_0___accumulator = _dafny.Companion_Sequence_.Concatenate(_0___accumulator, Companion_Default___.EncodeBlock((b).Take(3)))
		var _in0 _dafny.Sequence = (b).Drop(3)
		_ = _in0
		b = _in0
		goto TAIL_CALL_START
	}
}
func (_static *CompanionStruct_Default___) FromCharsToIndices(s _dafny.Sequence) _dafny.Sequence {
	return _dafny.SeqCreate((_dafny.IntOfUint32((s).Cardinality())).Uint32(), func(coer27 func(_dafny.Int) uint8) func(_dafny.Int) interface{} {
		return func(arg31 _dafny.Int) interface{} {
			return coer27(arg31)
		}
	}((func(_0_s _dafny.Sequence) func(_dafny.Int) uint8 {
		return func(_1_i _dafny.Int) uint8 {
			return Companion_Default___.CharToIndex((_0_s).Select((_1_i).Uint32()).(_dafny.Char))
		}
	})(s)))
}
func (_static *CompanionStruct_Default___) FromIndicesToChars(b _dafny.Sequence) _dafny.Sequence {
	return _dafny.SeqCreate((_dafny.IntOfUint32((b).Cardinality())).Uint32(), func(coer28 func(_dafny.Int) _dafny.Char) func(_dafny.Int) interface{} {
		return func(arg32 _dafny.Int) interface{} {
			return coer28(arg32)
		}
	}((func(_0_b _dafny.Sequence) func(_dafny.Int) _dafny.Char {
		return func(_1_i _dafny.Int) _dafny.Char {
			return Companion_Default___.IndexToChar((_0_b).Select((_1_i).Uint32()).(uint8))
		}
	})(b))).SetString()
}
func (_static *CompanionStruct_Default___) DecodeUnpadded(s _dafny.Sequence) _dafny.Sequence {
	return Companion_Default___.DecodeRecursively(Companion_Default___.FromCharsToIndices(s))
}
func (_static *CompanionStruct_Default___) EncodeUnpadded(b _dafny.Sequence) _dafny.Sequence {
	return Companion_Default___.FromIndicesToChars(Companion_Default___.EncodeRecursively(b))
}
func (_static *CompanionStruct_Default___) Is1Padding(s _dafny.Sequence) bool {
	return ((((((_dafny.IntOfUint32((s).Cardinality())).Cmp(_dafny.IntOfInt64(4)) == 0) && (Companion_Default___.IsBase64Char((s).Select(0).(_dafny.Char)))) && (Companion_Default___.IsBase64Char((s).Select(1).(_dafny.Char)))) && (Companion_Default___.IsBase64Char((s).Select(2).(_dafny.Char)))) && (((Companion_Default___.CharToIndex((s).Select(2).(_dafny.Char))) % (uint8(4))) == (uint8(0)))) && (((s).Select(3).(_dafny.Char)) == (_dafny.Char('=')))
}
func (_static *CompanionStruct_Default___) Decode1Padding(s _dafny.Sequence) _dafny.Sequence {
	var _0_d _dafny.Sequence = Companion_Default___.DecodeBlock(_dafny.SeqOf(Companion_Default___.CharToIndex((s).Select(0).(_dafny.Char)), Companion_Default___.CharToIndex((s).Select(1).(_dafny.Char)), Companion_Default___.CharToIndex((s).Select(2).(_dafny.Char)), uint8(0)))
	_ = _0_d
	return _dafny.SeqOf((_0_d).Select(0).(uint8), (_0_d).Select(1).(uint8))
}
func (_static *CompanionStruct_Default___) Encode1Padding(b _dafny.Sequence) _dafny.Sequence {
	var _0_e _dafny.Sequence = Companion_Default___.EncodeBlock(_dafny.SeqOf((b).Select(0).(uint8), (b).Select(1).(uint8), uint8(0)))
	_ = _0_e
	return _dafny.SeqOfChars(Companion_Default___.IndexToChar((_0_e).Select(0).(uint8)), Companion_Default___.IndexToChar((_0_e).Select(1).(uint8)), Companion_Default___.IndexToChar((_0_e).Select(2).(uint8)), _dafny.Char('='))
}
func (_static *CompanionStruct_Default___) Is2Padding(s _dafny.Sequence) bool {
	return ((((((_dafny.IntOfUint32((s).Cardinality())).Cmp(_dafny.IntOfInt64(4)) == 0) && (Companion_Default___.IsBase64Char((s).Select(0).(_dafny.Char)))) && (Companion_Default___.IsBase64Char((s).Select(1).(_dafny.Char)))) && (((Companion_Default___.CharToIndex((s).Select(1).(_dafny.Char))) % (uint8(16))) == (uint8(0)))) && (((s).Select(2).(_dafny.Char)) == (_dafny.Char('=')))) && (((s).Select(3).(_dafny.Char)) == (_dafny.Char('=')))
}
func (_static *CompanionStruct_Default___) Decode2Padding(s _dafny.Sequence) _dafny.Sequence {
	var _0_d _dafny.Sequence = Companion_Default___.DecodeBlock(_dafny.SeqOf(Companion_Default___.CharToIndex((s).Select(0).(_dafny.Char)), Companion_Default___.CharToIndex((s).Select(1).(_dafny.Char)), uint8(0), uint8(0)))
	_ = _0_d
	return _dafny.SeqOf((_0_d).Select(0).(uint8))
}
func (_static *CompanionStruct_Default___) Encode2Padding(b _dafny.Sequence) _dafny.Sequence {
	var _0_e _dafny.Sequence = Companion_Default___.EncodeBlock(_dafny.SeqOf((b).Select(0).(uint8), uint8(0), uint8(0)))
	_ = _0_e
	return _dafny.SeqOfChars(Companion_Default___.IndexToChar((_0_e).Select(0).(uint8)), Companion_Default___.IndexToChar((_0_e).Select(1).(uint8)), _dafny.Char('='), _dafny.Char('='))
}
func (_static *CompanionStruct_Default___) IsBase64String(s _dafny.Sequence) bool {
	var _0_finalBlockStart _dafny.Int = (_dafny.IntOfUint32((s).Cardinality())).Minus(_dafny.IntOfInt64(4))
	_ = _0_finalBlockStart
	return (((_dafny.IntOfUint32((s).Cardinality())).Modulo(_dafny.IntOfInt64(4))).Sign() == 0) && ((Companion_Default___.IsUnpaddedBase64String(s)) || ((Companion_Default___.IsUnpaddedBase64String((s).Take((_0_finalBlockStart).Uint32()))) && ((Companion_Default___.Is1Padding((s).Drop((_0_finalBlockStart).Uint32()))) || (Companion_Default___.Is2Padding((s).Drop((_0_finalBlockStart).Uint32()))))))
}
func (_static *CompanionStruct_Default___) DecodeValid(s _dafny.Sequence) _dafny.Sequence {
	if _dafny.Companion_Sequence_.Equal(s, _dafny.SeqOfChars()) {
		return _dafny.SeqOf()
	} else {
		var _0_finalBlockStart _dafny.Int = (_dafny.IntOfUint32((s).Cardinality())).Minus(_dafny.IntOfInt64(4))
		_ = _0_finalBlockStart
		var _1_prefix _dafny.Sequence = (s).Take((_0_finalBlockStart).Uint32())
		_ = _1_prefix
		var _2_suffix _dafny.Sequence = (s).Drop((_0_finalBlockStart).Uint32())
		_ = _2_suffix
		if Companion_Default___.Is1Padding(_2_suffix) {
			return _dafny.Companion_Sequence_.Concatenate(Companion_Default___.DecodeUnpadded(_1_prefix), Companion_Default___.Decode1Padding(_2_suffix))
		} else if Companion_Default___.Is2Padding(_2_suffix) {
			return _dafny.Companion_Sequence_.Concatenate(Companion_Default___.DecodeUnpadded(_1_prefix), Companion_Default___.Decode2Padding(_2_suffix))
		} else {
			return Companion_Default___.DecodeUnpadded(s)
		}
	}
}
func (_static *CompanionStruct_Default___) Decode(s _dafny.Sequence) m_Wrappers.Result {
	if Companion_Default___.IsBase64String(s) {
		return m_Wrappers.Companion_Result_.Create_Success_(Companion_Default___.DecodeValid(s))
	} else {
		return m_Wrappers.Companion_Result_.Create_Failure_(_dafny.SeqOfString("The encoding is malformed"))
	}
}
func (_static *CompanionStruct_Default___) Encode(b _dafny.Sequence) _dafny.Sequence {
	if ((_dafny.IntOfUint32((b).Cardinality())).Modulo(_dafny.IntOfInt64(3))).Sign() == 0 {
		var _0_s _dafny.Sequence = Companion_Default___.EncodeUnpadded(b)
		_ = _0_s
		return _0_s
	} else if ((_dafny.IntOfUint32((b).Cardinality())).Modulo(_dafny.IntOfInt64(3))).Cmp(_dafny.One) == 0 {
		var _1_s1 _dafny.Sequence = Companion_Default___.EncodeUnpadded((b).Take(((_dafny.IntOfUint32((b).Cardinality())).Minus(_dafny.One)).Uint32()))
		_ = _1_s1
		var _2_s2 _dafny.Sequence = Companion_Default___.Encode2Padding((b).Drop(((_dafny.IntOfUint32((b).Cardinality())).Minus(_dafny.One)).Uint32()))
		_ = _2_s2
		var _3_s _dafny.Sequence = _dafny.Companion_Sequence_.Concatenate(_1_s1, _2_s2)
		_ = _3_s
		return _3_s
	} else {
		var _4_s1 _dafny.Sequence = Companion_Default___.EncodeUnpadded((b).Take(((_dafny.IntOfUint32((b).Cardinality())).Minus(_dafny.IntOfInt64(2))).Uint32()))
		_ = _4_s1
		var _5_s2 _dafny.Sequence = Companion_Default___.Encode1Padding((b).Drop(((_dafny.IntOfUint32((b).Cardinality())).Minus(_dafny.IntOfInt64(2))).Uint32()))
		_ = _5_s2
		var _6_s _dafny.Sequence = _dafny.Companion_Sequence_.Concatenate(_4_s1, _5_s2)
		_ = _6_s
		return _6_s
	}
}

// End of class Default__

// Definition of class Index
type Index struct {
}

func New_Index_() *Index {
	_this := Index{}

	return &_this
}

type CompanionStruct_Index_ struct {
}

var Companion_Index_ = CompanionStruct_Index_{}

func (*Index) String() string {
	return "Base64.Index"
}
func (_this *Index) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Index{}

func (_this *CompanionStruct_Index_) IntegerRange(lo _dafny.Int, hi _dafny.Int) _dafny.Iterator {
	iter := _dafny.IntegerRange(lo, hi)
	return func() (interface{}, bool) {
		next, ok := iter()
		if !ok {
			return uint8(0), false
		}
		return next.(_dafny.Int).Uint8(), true
	}
}

// End of class Index

func Type_Index_() _dafny.TypeDescriptor {
	return type_Index_{}
}

type type_Index_ struct {
}

func (_this type_Index_) Default() interface{} {
	return uint8(0)
}

func (_this type_Index_) String() string {
	return "Base64.Index"
}
func (_this *CompanionStruct_Index_) Is_(__source uint8) bool {
	var _0_x _dafny.Int = _dafny.IntOfUint8(__source)
	_ = _0_x
	return ((_0_x).Sign() != -1) && ((_0_x).Cmp(_dafny.IntOfInt64(64)) < 0)
}

// Definition of class Uint24
type Uint24 struct {
}

func New_Uint24_() *Uint24 {
	_this := Uint24{}

	return &_this
}

type CompanionStruct_Uint24_ struct {
}

var Companion_Uint24_ = CompanionStruct_Uint24_{}

func (*Uint24) String() string {
	return "Base64.Uint24"
}
func (_this *Uint24) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Uint24{}

func (_this *CompanionStruct_Uint24_) IntegerRange(lo _dafny.Int, hi _dafny.Int) _dafny.Iterator {
	iter := _dafny.IntegerRange(lo, hi)
	return func() (interface{}, bool) {
		next, ok := iter()
		if !ok {
			return uint32(0), false
		}
		return next.(_dafny.Int).Uint32(), true
	}
}

// End of class Uint24

func Type_Uint24_() _dafny.TypeDescriptor {
	return type_Uint24_{}
}

type type_Uint24_ struct {
}

func (_this type_Uint24_) Default() interface{} {
	return uint32(0)
}

func (_this type_Uint24_) String() string {
	return "Base64.Uint24"
}
func (_this *CompanionStruct_Uint24_) Is_(__source uint32) bool {
	var _1_x _dafny.Int = _dafny.IntOfUint32(__source)
	_ = _1_x
	return ((_1_x).Sign() != -1) && ((_1_x).Cmp(_dafny.IntOfInt64(16777216)) < 0)
}
