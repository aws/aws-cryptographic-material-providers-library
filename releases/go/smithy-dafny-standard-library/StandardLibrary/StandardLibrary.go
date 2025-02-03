// Package StandardLibrary
// Dafny module StandardLibrary compiled into Go

package StandardLibrary

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
	m_StandardLibrary_Sequence "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/StandardLibrary_Sequence"
	m_StandardLibrary_String "github.com/aws/aws-cryptographic-material-providers-library/releases/go/smithy-dafny-standard-library/StandardLibrary_String"
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
var _ m_StandardLibrary_Sequence.Dummy__
var _ m_StandardLibrary_String.Dummy__

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
	return "StandardLibrary.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) Join(ss _dafny.Sequence, joiner _dafny.Sequence) _dafny.Sequence {
	var _0___accumulator _dafny.Sequence = _dafny.SeqOf()
	_ = _0___accumulator
	goto TAIL_CALL_START
TAIL_CALL_START:
	if (_dafny.IntOfUint32((ss).Cardinality())).Cmp(_dafny.One) == 0 {
		return _dafny.Companion_Sequence_.Concatenate(_0___accumulator, (ss).Select(0).(_dafny.Sequence))
	} else {
		_0___accumulator = _dafny.Companion_Sequence_.Concatenate(_0___accumulator, _dafny.Companion_Sequence_.Concatenate((ss).Select(0).(_dafny.Sequence), joiner))
		var _in0 _dafny.Sequence = (ss).Drop(1)
		_ = _in0
		var _in1 _dafny.Sequence = joiner
		_ = _in1
		ss = _in0
		joiner = _in1
		goto TAIL_CALL_START
	}
}
func (_static *CompanionStruct_Default___) Split(s _dafny.Sequence, delim interface{}) _dafny.Sequence {
	var _0___accumulator _dafny.Sequence = _dafny.SeqOf()
	_ = _0___accumulator
	goto TAIL_CALL_START
TAIL_CALL_START:
	var _1_i m_Wrappers.Option = Companion_Default___.FindIndexMatching(s, delim, _dafny.Zero)
	_ = _1_i
	if (_1_i).Is_Some() {
		_0___accumulator = _dafny.Companion_Sequence_.Concatenate(_0___accumulator, _dafny.SeqOf((s).Take(((_1_i).Dtor_value().(_dafny.Int)).Uint32())))
		var _in0 _dafny.Sequence = (s).Drop((((_1_i).Dtor_value().(_dafny.Int)).Plus(_dafny.One)).Uint32())
		_ = _in0
		var _in1 interface{} = delim
		_ = _in1
		s = _in0
		delim = _in1
		goto TAIL_CALL_START
	} else {
		return _dafny.Companion_Sequence_.Concatenate(_0___accumulator, _dafny.SeqOf(s))
	}
}
func (_static *CompanionStruct_Default___) SplitOnce(s _dafny.Sequence, delim interface{}) _dafny.Tuple {
	var _0_i m_Wrappers.Option = Companion_Default___.FindIndexMatching(s, delim, _dafny.Zero)
	_ = _0_i
	return _dafny.TupleOf((s).Take(((_0_i).Dtor_value().(_dafny.Int)).Uint32()), (s).Drop((((_0_i).Dtor_value().(_dafny.Int)).Plus(_dafny.One)).Uint32()))
}
func (_static *CompanionStruct_Default___) SplitOnce_q(s _dafny.Sequence, delim interface{}) m_Wrappers.Option {
	var _0_valueOrError0 m_Wrappers.Option = Companion_Default___.FindIndexMatching(s, delim, _dafny.Zero)
	_ = _0_valueOrError0
	if (_0_valueOrError0).IsFailure() {
		return (_0_valueOrError0).PropagateFailure()
	} else {
		var _1_i _dafny.Int = (_0_valueOrError0).Extract().(_dafny.Int)
		_ = _1_i
		return m_Wrappers.Companion_Option_.Create_Some_(_dafny.TupleOf((s).Take((_1_i).Uint32()), (s).Drop(((_1_i).Plus(_dafny.One)).Uint32())))
	}
}
func (_static *CompanionStruct_Default___) FindIndexMatching(s _dafny.Sequence, c interface{}, i _dafny.Int) m_Wrappers.Option {
	return Companion_Default___.FindIndex(s, func(coer17 func(interface{}) bool) func(interface{}) bool {
		return func(arg18 interface{}) bool {
			return coer17(arg18)
		}
	}((func(_0_c interface{}) func(interface{}) bool {
		return func(_1_x interface{}) bool {
			return _dafny.AreEqual(_1_x, _0_c)
		}
	})(c)), i)
}
func (_static *CompanionStruct_Default___) FindIndex(s _dafny.Sequence, f func(interface{}) bool, i _dafny.Int) m_Wrappers.Option {
	goto TAIL_CALL_START
TAIL_CALL_START:
	if (i).Cmp(_dafny.IntOfUint32((s).Cardinality())) == 0 {
		return m_Wrappers.Companion_Option_.Create_None_()
	} else if (f)((s).Select((i).Uint32()).(interface{})) {
		return m_Wrappers.Companion_Option_.Create_Some_(i)
	} else {
		var _in0 _dafny.Sequence = s
		_ = _in0
		var _in1 func(interface{}) bool = f
		_ = _in1
		var _in2 _dafny.Int = (i).Plus(_dafny.One)
		_ = _in2
		s = _in0
		f = _in1
		i = _in2
		goto TAIL_CALL_START
	}
}
func (_static *CompanionStruct_Default___) Filter(s _dafny.Sequence, f func(interface{}) bool) _dafny.Sequence {
	var _0___accumulator _dafny.Sequence = _dafny.SeqOf()
	_ = _0___accumulator
	goto TAIL_CALL_START
TAIL_CALL_START:
	if (_dafny.IntOfUint32((s).Cardinality())).Sign() == 0 {
		return _dafny.Companion_Sequence_.Concatenate(_0___accumulator, _dafny.SeqOf())
	} else if (f)((s).Select(0).(interface{})) {
		_0___accumulator = _dafny.Companion_Sequence_.Concatenate(_0___accumulator, _dafny.SeqOf((s).Select(0).(interface{})))
		var _in0 _dafny.Sequence = (s).Drop(1)
		_ = _in0
		var _in1 func(interface{}) bool = f
		_ = _in1
		s = _in0
		f = _in1
		goto TAIL_CALL_START
	} else {
		var _in2 _dafny.Sequence = (s).Drop(1)
		_ = _in2
		var _in3 func(interface{}) bool = f
		_ = _in3
		s = _in2
		f = _in3
		goto TAIL_CALL_START
	}
}
func (_static *CompanionStruct_Default___) Min(a _dafny.Int, b _dafny.Int) _dafny.Int {
	if (a).Cmp(b) < 0 {
		return a
	} else {
		return b
	}
}
func (_static *CompanionStruct_Default___) Fill(value interface{}, n _dafny.Int) _dafny.Sequence {
	return _dafny.SeqCreate((n).Uint32(), func(coer18 func(_dafny.Int) interface{}) func(_dafny.Int) interface{} {
		return func(arg19 _dafny.Int) interface{} {
			return coer18(arg19)
		}
	}((func(_0_value interface{}) func(_dafny.Int) interface{} {
		return func(_1___v0 _dafny.Int) interface{} {
			return _0_value
		}
	})(value)))
}
func (_static *CompanionStruct_Default___) SeqToArray(s _dafny.Sequence) _dafny.Array {
	var a _dafny.Array = _dafny.NewArrayWithValue(nil, _dafny.IntOf(0))
	_ = a
	var _len0_0 _dafny.Int = _dafny.IntOfUint32((s).Cardinality())
	_ = _len0_0
	var _nw0 _dafny.Array
	_ = _nw0
	if _len0_0.Cmp(_dafny.Zero) == 0 {
		_nw0 = _dafny.NewArray(_len0_0)
	} else {
		var _init0 func(_dafny.Int) interface{} = (func(_0_s _dafny.Sequence) func(_dafny.Int) interface{} {
			return func(_1_i _dafny.Int) interface{} {
				return (_0_s).Select((_1_i).Uint32()).(interface{})
			}
		})(s)
		_ = _init0
		var _element0_0 = _init0(_dafny.Zero)
		_ = _element0_0
		_nw0 = _dafny.NewArrayFromExample(_element0_0, nil, _len0_0)
		(_nw0).ArraySet1(_element0_0, 0)
		var _nativeLen0_0 = (_len0_0).Int()
		_ = _nativeLen0_0
		for _i0_0 := 1; _i0_0 < _nativeLen0_0; _i0_0++ {
			(_nw0).ArraySet1(_init0(_dafny.IntOf(_i0_0)), _i0_0)
		}
	}
	a = _nw0
	return a
}
func (_static *CompanionStruct_Default___) LexicographicLessOrEqual(a _dafny.Sequence, b _dafny.Sequence, less func(interface{}, interface{}) bool) bool {
	return _dafny.Quantifier(_dafny.IntegerRange(_dafny.Zero, (_dafny.IntOfUint32((a).Cardinality())).Plus(_dafny.One)), false, func(_exists_var_0 _dafny.Int) bool {
		var _0_k _dafny.Int
		_0_k = interface{}(_exists_var_0).(_dafny.Int)
		return (((_0_k).Sign() != -1) && ((_0_k).Cmp(_dafny.IntOfUint32((a).Cardinality())) <= 0)) && (Companion_Default___.LexicographicLessOrEqualAux(a, b, func(coer19 func(interface{}, interface{}) bool) func(interface{}, interface{}) bool {
			return func(arg20 interface{}, arg21 interface{}) bool {
				return coer19(arg20, arg21)
			}
		}(less), _0_k))
	})
}
func (_static *CompanionStruct_Default___) LexicographicLessOrEqualAux(a _dafny.Sequence, b _dafny.Sequence, less func(interface{}, interface{}) bool, lengthOfCommonPrefix _dafny.Int) bool {
	return (((lengthOfCommonPrefix).Cmp(_dafny.IntOfUint32((b).Cardinality())) <= 0) && (_dafny.Quantifier(_dafny.IntegerRange(_dafny.Zero, lengthOfCommonPrefix), true, func(_forall_var_0 _dafny.Int) bool {
		var _0_i _dafny.Int
		_0_i = interface{}(_forall_var_0).(_dafny.Int)
		return !(((_0_i).Sign() != -1) && ((_0_i).Cmp(lengthOfCommonPrefix) < 0)) || (_dafny.AreEqual((a).Select((_0_i).Uint32()).(interface{}), (b).Select((_0_i).Uint32()).(interface{})))
	}))) && (((lengthOfCommonPrefix).Cmp(_dafny.IntOfUint32((a).Cardinality())) == 0) || (((lengthOfCommonPrefix).Cmp(_dafny.IntOfUint32((b).Cardinality())) < 0) && ((less)((a).Select((lengthOfCommonPrefix).Uint32()).(interface{}), (b).Select((lengthOfCommonPrefix).Uint32()).(interface{})))))
}
func (_static *CompanionStruct_Default___) SetToOrderedSequence(s _dafny.Set, less func(interface{}, interface{}) bool) _dafny.Sequence {
	var _0___accumulator _dafny.Sequence = _dafny.SeqOf()
	_ = _0___accumulator
	goto TAIL_CALL_START
TAIL_CALL_START:
	var _pat_let_tv0 = s
	_ = _pat_let_tv0
	var _pat_let_tv1 = less
	_ = _pat_let_tv1
	if (s).Equals(_dafny.SetOf()) {
		return _dafny.Companion_Sequence_.Concatenate(_0___accumulator, _dafny.SeqOf())
	} else {
		return func(_let_dummy_0 int) _dafny.Sequence {
			var _1_a _dafny.Sequence = _dafny.EmptySeq
			_ = _1_a
			{
				for _iter1 := _dafny.Iterate((s).Elements()); ; {
					_assign_such_that_0, _ok1 := _iter1()
					if !_ok1 {
						break
					}
					_1_a = interface{}(_assign_such_that_0).(_dafny.Sequence)
					if ((s).Contains(_1_a)) && (Companion_Default___.IsMinimum(_1_a, s, func(coer20 func(interface{}, interface{}) bool) func(interface{}, interface{}) bool {
						return func(arg22 interface{}, arg23 interface{}) bool {
							return coer20(arg22, arg23)
						}
					}(less))) {
						goto L_ASSIGN_SUCH_THAT_0
					}
				}
				panic("assign-such-that search produced no value")
				goto L_ASSIGN_SUCH_THAT_0
			}
		L_ASSIGN_SUCH_THAT_0:
			return _dafny.Companion_Sequence_.Concatenate(_dafny.SeqOf(_1_a), Companion_Default___.SetToOrderedSequence((_pat_let_tv0).Difference(_dafny.SetOf(_1_a)), _pat_let_tv1))
		}(0)
	}
}
func (_static *CompanionStruct_Default___) IsMinimum(a _dafny.Sequence, s _dafny.Set, less func(interface{}, interface{}) bool) bool {
	return ((s).Contains(a)) && (_dafny.Quantifier((s).Elements(), true, func(_forall_var_0 _dafny.Sequence) bool {
		var _0_z _dafny.Sequence
		_0_z = interface{}(_forall_var_0).(_dafny.Sequence)
		return !((s).Contains(_0_z)) || (Companion_Default___.LexicographicLessOrEqual(a, _0_z, func(coer21 func(interface{}, interface{}) bool) func(interface{}, interface{}) bool {
			return func(arg24 interface{}, arg25 interface{}) bool {
				return coer21(arg24, arg25)
			}
		}(less)))
	}))
}

// End of class Default__
