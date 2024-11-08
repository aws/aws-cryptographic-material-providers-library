// Package HKDF
// Dafny module HKDF compiled into Go

package HKDF

import (
	os "os"

	m_AESEncryption "github.com/aws/aws-cryptographic-material-providers-library/primitives/AESEncryption"
	m_AwsCryptographyPrimitivesTypes "github.com/aws/aws-cryptographic-material-providers-library/primitives/AwsCryptographyPrimitivesTypes"
	m_Digest "github.com/aws/aws-cryptographic-material-providers-library/primitives/Digest"
	m_HMAC "github.com/aws/aws-cryptographic-material-providers-library/primitives/HMAC"
	m_Random "github.com/aws/aws-cryptographic-material-providers-library/primitives/Random"
	m_WrappedHMAC "github.com/aws/aws-cryptographic-material-providers-library/primitives/WrappedHMAC"
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
var _ m_AwsCryptographyPrimitivesTypes.Dummy__
var _ m_Random.Dummy__
var _ m_AESEncryption.Dummy__
var _ m_Digest.Dummy__
var _ m_HMAC.Dummy__
var _ m_WrappedHMAC.Dummy__

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
	return "HKDF.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) Extract(hmac m_HMAC.HMac, salt _dafny.Sequence, ikm _dafny.Sequence) _dafny.Sequence {
	var prk _dafny.Sequence = _dafny.EmptySeq
	_ = prk
	(hmac).Init(salt)
	(hmac).BlockUpdate(ikm)
	var _out0 _dafny.Sequence
	_ = _out0
	_out0 = (hmac).GetResult()
	prk = _out0
	prk = prk
	return prk
	return prk
}
func (_static *CompanionStruct_Default___) Expand(hmac m_HMAC.HMac, prk _dafny.Sequence, info _dafny.Sequence, expectedLength _dafny.Int, digest m_AwsCryptographyPrimitivesTypes.DigestAlgorithm) _dafny.Sequence {
	var okm _dafny.Sequence = _dafny.EmptySeq
	_ = okm
	var _0_hashLength _dafny.Int
	_ = _0_hashLength
	_0_hashLength = m_Digest.Companion_Default___.Length(digest)
	var _1_n _dafny.Int
	_ = _1_n
	_1_n = (((_0_hashLength).Plus(expectedLength)).Minus(_dafny.One)).DivBy(_0_hashLength)
	(hmac).Init(prk)
	var _2_t__prev _dafny.Sequence
	_ = _2_t__prev
	_2_t__prev = _dafny.SeqOf()
	var _3_t__n _dafny.Sequence
	_ = _3_t__n
	_3_t__n = _2_t__prev
	var _4_i _dafny.Int
	_ = _4_i
	_4_i = _dafny.One
	for (_4_i).Cmp(_1_n) <= 0 {
		(hmac).BlockUpdate(_2_t__prev)
		(hmac).BlockUpdate(info)
		(hmac).BlockUpdate(_dafny.SeqOf((_4_i).Uint8()))
		var _out0 _dafny.Sequence
		_ = _out0
		_out0 = (hmac).GetResult()
		_2_t__prev = _out0
		_3_t__n = _dafny.Companion_Sequence_.Concatenate(_3_t__n, _2_t__prev)
		_4_i = (_4_i).Plus(_dafny.One)
	}
	okm = _3_t__n
	if (expectedLength).Cmp(_dafny.IntOfUint32((okm).Cardinality())) < 0 {
		okm = (okm).Take((expectedLength).Uint32())
	}
	return okm
}
func (_static *CompanionStruct_Default___) Hkdf(digest m_AwsCryptographyPrimitivesTypes.DigestAlgorithm, salt m_Wrappers.Option, ikm _dafny.Sequence, info _dafny.Sequence, L _dafny.Int) _dafny.Sequence {
	var okm _dafny.Sequence = _dafny.EmptySeq
	_ = okm
	if (L).Sign() == 0 {
		okm = _dafny.SeqOf()
		return okm
	}
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_HMAC.Companion_HMac_.Build(digest)
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("src/HKDF/HKDF.dfy(222,16): " + (_0_valueOrError0).String())
	}
	var _1_hmac m_HMAC.HMac
	_ = _1_hmac
	_1_hmac = m_HMAC.Companion_HMac_.CastTo_((_0_valueOrError0).Extract())
	var _2_hashLength _dafny.Int
	_ = _2_hashLength
	_2_hashLength = m_Digest.Companion_Default___.Length(digest)
	var _3_nonEmptySalt _dafny.Sequence = _dafny.EmptySeq
	_ = _3_nonEmptySalt
	var _source0 m_Wrappers.Option = salt
	_ = _source0
	{
		{
			if _source0.Is_None() {
				_3_nonEmptySalt = m_StandardLibrary.Companion_Default___.Fill(uint8(0), _2_hashLength)
				goto Lmatch0
			}
		}
		{
			var _4_s _dafny.Sequence = _source0.Get_().(m_Wrappers.Option_Some).Value.(_dafny.Sequence)
			_ = _4_s
			_3_nonEmptySalt = _4_s
		}
		goto Lmatch0
	}
Lmatch0:
	var _5_prk _dafny.Sequence
	_ = _5_prk
	var _out1 _dafny.Sequence
	_ = _out1
	_out1 = Companion_Default___.Extract(_1_hmac, _3_nonEmptySalt, ikm)
	_5_prk = _out1
	var _out2 _dafny.Sequence
	_ = _out2
	_out2 = Companion_Default___.Expand(_1_hmac, _5_prk, info, L, digest)
	okm = _out2
	return okm
}

// End of class Default__
