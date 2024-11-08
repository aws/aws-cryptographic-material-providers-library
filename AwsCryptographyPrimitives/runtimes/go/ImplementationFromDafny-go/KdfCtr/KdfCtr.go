// Package KdfCtr
// Dafny module KdfCtr compiled into Go

package KdfCtr

import (
	os "os"

	m_AESEncryption "github.com/aws/aws-cryptographic-material-providers-library/primitives/AESEncryption"
	m_AwsCryptographyPrimitivesTypes "github.com/aws/aws-cryptographic-material-providers-library/primitives/AwsCryptographyPrimitivesTypes"
	m_Digest "github.com/aws/aws-cryptographic-material-providers-library/primitives/Digest"
	m_HKDF "github.com/aws/aws-cryptographic-material-providers-library/primitives/HKDF"
	m_HMAC "github.com/aws/aws-cryptographic-material-providers-library/primitives/HMAC"
	m_Random "github.com/aws/aws-cryptographic-material-providers-library/primitives/Random"
	m_Signature "github.com/aws/aws-cryptographic-material-providers-library/primitives/Signature"
	m_WrappedHKDF "github.com/aws/aws-cryptographic-material-providers-library/primitives/WrappedHKDF"
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
var _ m_HKDF.Dummy__
var _ m_WrappedHKDF.Dummy__
var _ m_Signature.Dummy__

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
	return "KdfCtr.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) KdfCounterMode(input m_AwsCryptographyPrimitivesTypes.KdfCtrInput) m_Wrappers.Result {
	var output m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = output
	var _0_valueOrError0 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
	_ = _0_valueOrError0
	_0_valueOrError0 = m_Wrappers.Companion_Default___.Need(((((((((input).Dtor_digestAlgorithm()).Equals(m_AwsCryptographyPrimitivesTypes.Companion_DigestAlgorithm_.Create_SHA__256_())) || (((input).Dtor_digestAlgorithm()).Equals(m_AwsCryptographyPrimitivesTypes.Companion_DigestAlgorithm_.Create_SHA__384_()))) && ((((_dafny.IntOfUint32(((input).Dtor_ikm()).Cardinality())).Cmp(_dafny.IntOfInt64(32)) == 0) || ((_dafny.IntOfUint32(((input).Dtor_ikm()).Cardinality())).Cmp(_dafny.IntOfInt64(48)) == 0)) || ((_dafny.IntOfUint32(((input).Dtor_ikm()).Cardinality())).Cmp(_dafny.IntOfInt64(66)) == 0))) && (((input).Dtor_nonce()).Is_Some())) && (((_dafny.IntOfUint32((((input).Dtor_nonce()).Dtor_value().(_dafny.Sequence)).Cardinality())).Cmp(_dafny.IntOfInt64(16)) == 0) || ((_dafny.IntOfUint32((((input).Dtor_nonce()).Dtor_value().(_dafny.Sequence)).Cardinality())).Cmp(_dafny.IntOfInt64(32)) == 0))) && ((((input).Dtor_expectedLength()) == (int32(32))) || (((input).Dtor_expectedLength()) == (int32(64))))) && ((((_dafny.IntOfInt32((input).Dtor_expectedLength())).Times(_dafny.IntOfInt64(8))).Sign() == 1) && (((_dafny.IntOfInt32((input).Dtor_expectedLength())).Times(_dafny.IntOfInt64(8))).Cmp(m_StandardLibrary_UInt.Companion_Default___.INT32__MAX__LIMIT()) < 0)), m_AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(_dafny.SeqOfString("Kdf in Counter Mode input is invalid.")))
	if (_0_valueOrError0).IsFailure() {
		output = (_0_valueOrError0).PropagateFailure()
		return output
	}
	var _1_ikm _dafny.Sequence
	_ = _1_ikm
	_1_ikm = (input).Dtor_ikm()
	var _2_label__ _dafny.Sequence
	_ = _2_label__
	_2_label__ = ((input).Dtor_purpose()).UnwrapOr(_dafny.SeqOf()).(_dafny.Sequence)
	var _3_info _dafny.Sequence
	_ = _3_info
	_3_info = ((input).Dtor_nonce()).UnwrapOr(_dafny.SeqOf()).(_dafny.Sequence)
	var _4_okm _dafny.Sequence
	_ = _4_okm
	_4_okm = _dafny.SeqOf()
	var _5_internalLength uint32
	_ = _5_internalLength
	_5_internalLength = (((_dafny.IntOfInt64(4)).Plus(_dafny.IntOfUint32((Companion_Default___.SEPARATION__INDICATOR()).Cardinality()))).Plus(_dafny.IntOfInt64(4))).Uint32()
	var _6_valueOrError1 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
	_ = _6_valueOrError1
	_6_valueOrError1 = m_Wrappers.Companion_Default___.Need((true) && ((((_dafny.IntOfUint32(_5_internalLength)).Plus(_dafny.IntOfUint32((_2_label__).Cardinality()))).Plus(_dafny.IntOfUint32((_3_info).Cardinality()))).Cmp(m_StandardLibrary_UInt.Companion_Default___.INT32__MAX__LIMIT()) < 0), m_AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(_dafny.SeqOfString("Input Length exceeds INT32_MAX_LIMIT")))
	if (_6_valueOrError1).IsFailure() {
		output = (_6_valueOrError1).PropagateFailure()
		return output
	}
	var _7_lengthBits _dafny.Sequence
	_ = _7_lengthBits
	_7_lengthBits = m_StandardLibrary_UInt.Companion_Default___.UInt32ToSeq(uint32(((input).Dtor_expectedLength()) * (int32(8))))
	var _8_explicitInfo _dafny.Sequence
	_ = _8_explicitInfo
	_8_explicitInfo = _dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_dafny.Companion_Sequence_.Concatenate(_2_label__, Companion_Default___.SEPARATION__INDICATOR()), _3_info), _7_lengthBits)
	var _9_valueOrError2 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
	_ = _9_valueOrError2
	_9_valueOrError2 = m_Wrappers.Companion_Default___.Need(((_dafny.IntOfInt64(4)).Plus(_dafny.IntOfUint32((_8_explicitInfo).Cardinality()))).Cmp(m_StandardLibrary_UInt.Companion_Default___.INT32__MAX__LIMIT()) < 0, m_AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(_dafny.SeqOfString("PRF input length exceeds INT32_MAX_LIMIT.")))
	if (_9_valueOrError2).IsFailure() {
		output = (_9_valueOrError2).PropagateFailure()
		return output
	}
	var _10_valueOrError3 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _10_valueOrError3
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = Companion_Default___.RawDerive(_1_ikm, _8_explicitInfo, (input).Dtor_expectedLength(), int32(0), (input).Dtor_digestAlgorithm())
	_10_valueOrError3 = _out0
	if (_10_valueOrError3).IsFailure() {
		output = (_10_valueOrError3).PropagateFailure()
		return output
	}
	_4_okm = (_10_valueOrError3).Extract().(_dafny.Sequence)
	output = m_Wrappers.Companion_Result_.Create_Success_(_4_okm)
	return output
	return output
}
func (_static *CompanionStruct_Default___) RawDerive(ikm _dafny.Sequence, explicitInfo _dafny.Sequence, length int32, offset int32, digestAlgorithm m_AwsCryptographyPrimitivesTypes.DigestAlgorithm) m_Wrappers.Result {
	var output m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = output
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_HMAC.Companion_HMac_.Build(digestAlgorithm)
	_0_valueOrError0 = _out0
	if (_0_valueOrError0).IsFailure() {
		output = (_0_valueOrError0).PropagateFailure()
		return output
	}
	var _1_hmac m_HMAC.HMac
	_ = _1_hmac
	_1_hmac = m_HMAC.Companion_HMac_.CastTo_((_0_valueOrError0).Extract())
	(_1_hmac).Init(ikm)
	var _2_macLengthBytes int32
	_ = _2_macLengthBytes
	_2_macLengthBytes = (m_Digest.Companion_Default___.Length(digestAlgorithm)).Int32()
	var _3_iterations int32
	_ = _3_iterations
	_3_iterations = _dafny.DivInt32(((length)+(_2_macLengthBytes))-(int32(1)), _2_macLengthBytes)
	var _4_buffer _dafny.Sequence
	_ = _4_buffer
	_4_buffer = _dafny.SeqOf()
	var _5_i _dafny.Sequence
	_ = _5_i
	_5_i = m_StandardLibrary_UInt.Companion_Default___.UInt32ToSeq(Companion_Default___.COUNTER__START__VALUE())
	var _hi0 int32 = (_3_iterations) + (int32(1))
	_ = _hi0
	for _6_iteration := int32(1); _6_iteration < _hi0; _6_iteration++ {
		(_1_hmac).BlockUpdate(_5_i)
		(_1_hmac).BlockUpdate(explicitInfo)
		var _7_tmp _dafny.Sequence
		_ = _7_tmp
		var _out1 _dafny.Sequence
		_ = _out1
		_out1 = (_1_hmac).GetResult()
		_7_tmp = _out1
		_4_buffer = _dafny.Companion_Sequence_.Concatenate(_4_buffer, _7_tmp)
		var _8_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
		_ = _8_valueOrError1
		_8_valueOrError1 = Companion_Default___.Increment(_5_i)
		if (_8_valueOrError1).IsFailure() {
			output = (_8_valueOrError1).PropagateFailure()
			return output
		}
		_5_i = (_8_valueOrError1).Extract().(_dafny.Sequence)
	}
	var _9_valueOrError2 m_Wrappers.Outcome = m_Wrappers.Companion_Outcome_.Default()
	_ = _9_valueOrError2
	_9_valueOrError2 = m_Wrappers.Companion_Default___.Need((_dafny.IntOfUint32((_4_buffer).Cardinality())).Cmp(_dafny.IntOfInt32(length)) >= 0, m_AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(_dafny.SeqOfString("Failed to derive key of requested length")))
	if (_9_valueOrError2).IsFailure() {
		output = (_9_valueOrError2).PropagateFailure()
		return output
	}
	output = m_Wrappers.Companion_Result_.Create_Success_((_4_buffer).Take(uint32(length)))
	return output
	return output
}
func (_static *CompanionStruct_Default___) Increment(x _dafny.Sequence) m_Wrappers.Result {
	if ((x).Select(3).(uint8)) < (uint8(255)) {
		return m_Wrappers.Companion_Result_.Create_Success_(_dafny.SeqOf((x).Select(0).(uint8), (x).Select(1).(uint8), (x).Select(2).(uint8), ((x).Select(3).(uint8))+(uint8(1))))
	} else if ((x).Select(2).(uint8)) < (uint8(255)) {
		return m_Wrappers.Companion_Result_.Create_Success_(_dafny.SeqOf((x).Select(0).(uint8), (x).Select(1).(uint8), ((x).Select(2).(uint8))+(uint8(1)), uint8(0)))
	} else if ((x).Select(1).(uint8)) < (uint8(255)) {
		return m_Wrappers.Companion_Result_.Create_Success_(_dafny.SeqOf((x).Select(0).(uint8), ((x).Select(1).(uint8))+(uint8(1)), uint8(0), uint8(0)))
	} else if ((x).Select(0).(uint8)) < (uint8(255)) {
		return m_Wrappers.Companion_Result_.Create_Success_(_dafny.SeqOf(((x).Select(0).(uint8))+(uint8(1)), uint8(0), uint8(0), uint8(0)))
	} else {
		return m_Wrappers.Companion_Result_.Create_Failure_(m_AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(_dafny.SeqOfString("Unable to derive key material; may have exceeded limit.")))
	}
}
func (_static *CompanionStruct_Default___) SEPARATION__INDICATOR() _dafny.Sequence {
	return _dafny.SeqOf(uint8(0))
}
func (_static *CompanionStruct_Default___) COUNTER__START__VALUE() uint32 {
	return uint32(1)
}

// End of class Default__
