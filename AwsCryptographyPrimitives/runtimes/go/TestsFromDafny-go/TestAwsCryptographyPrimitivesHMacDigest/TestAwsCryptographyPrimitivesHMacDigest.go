// Package TestAwsCryptographyPrimitivesHMacDigest
// Dafny module TestAwsCryptographyPrimitivesHMacDigest compiled into Go

package TestAwsCryptographyPrimitivesHMacDigest

import (
	os "os"

	m_AESEncryption "github.com/aws/aws-cryptographic-material-providers-library/primitives/AESEncryption"
	m_AtomicPrimitives "github.com/aws/aws-cryptographic-material-providers-library/primitives/AtomicPrimitives"
	m_AwsCryptographyPrimitivesOperations "github.com/aws/aws-cryptographic-material-providers-library/primitives/AwsCryptographyPrimitivesOperations"
	m_AwsCryptographyPrimitivesTypes "github.com/aws/aws-cryptographic-material-providers-library/primitives/AwsCryptographyPrimitivesTypes"
	m_Digest "github.com/aws/aws-cryptographic-material-providers-library/primitives/Digest"
	m_ECDH "github.com/aws/aws-cryptographic-material-providers-library/primitives/ECDH"
	m_HKDF "github.com/aws/aws-cryptographic-material-providers-library/primitives/HKDF"
	m_HMAC "github.com/aws/aws-cryptographic-material-providers-library/primitives/HMAC"
	m_KdfCtr "github.com/aws/aws-cryptographic-material-providers-library/primitives/KdfCtr"
	m_RSAEncryption "github.com/aws/aws-cryptographic-material-providers-library/primitives/RSAEncryption"
	m_Random "github.com/aws/aws-cryptographic-material-providers-library/primitives/Random"
	m_Signature "github.com/aws/aws-cryptographic-material-providers-library/primitives/Signature"
	m_WrappedHKDF "github.com/aws/aws-cryptographic-material-providers-library/primitives/WrappedHKDF"
	m_WrappedHMAC "github.com/aws/aws-cryptographic-material-providers-library/primitives/WrappedHMAC"
	m_TestKDF "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestKDF"
	m_TestKDFK__TestVectors "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestKDFK__TestVectors"
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
var _ m_BoundedInts.Dummy__
var _ m_StandardLibrary_UInt.Dummy__
var _ m_StandardLibrary_String.Dummy__
var _ m_StandardLibrary.Dummy__
var _ m_AwsCryptographyPrimitivesTypes.Dummy__
var _ m_Random.Dummy__
var _ m_AESEncryption.Dummy__
var _ m_Digest.Dummy__
var _ m_HMAC.Dummy__
var _ m_WrappedHMAC.Dummy__
var _ m_HKDF.Dummy__
var _ m_WrappedHKDF.Dummy__
var _ m_Signature.Dummy__
var _ m_KdfCtr.Dummy__
var _ m_RSAEncryption.Dummy__
var _ m_ECDH.Dummy__
var _ m_AwsCryptographyPrimitivesOperations.Dummy__
var _ m_AtomicPrimitives.Dummy__
var _ m_Relations.Dummy__
var _ m_Seq_MergeSort.Dummy__
var _ m__Math.Dummy__
var _ m_Seq.Dummy__
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
var _ m_Streams.Dummy__
var _ m_Sorting.Dummy__
var _ m_HexStrings.Dummy__
var _ m_GetOpt.Dummy__
var _ m_FloatCompare.Dummy__
var _ m_Base64.Dummy__
var _ m_Base64Lemmas.Dummy__
var _ m_Actions.Dummy__
var _ m_TestKDF.Dummy__
var _ m_TestKDFK__TestVectors.Dummy__

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
	return "TestAwsCryptographyPrimitivesHMacDigest.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) DigestTests() {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_AtomicPrimitives.Companion_Default___.AtomicPrimitives(m_AtomicPrimitives.Companion_Default___.DefaultCryptoConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("test/TestHMAC.dfy(14,18): " + (_0_valueOrError0).String())
	}
	var _1_client *m_AtomicPrimitives.AtomicPrimitivesClient
	_ = _1_client
	_1_client = (_0_valueOrError0).Extract().(*m_AtomicPrimitives.AtomicPrimitivesClient)
	Companion_Default___.HmacSHA__256(_1_client)
	Companion_Default___.HmacSHA__384(_1_client)
	Companion_Default___.HmacSHA__512(_1_client)
}
func (_static *CompanionStruct_Default___) HmacSHA__256(client m_AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient) {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.TupleOf())
	_ = _0_valueOrError0
	_0_valueOrError0 = Companion_Default___.BasicHMacTest(client, m_AwsCryptographyPrimitivesTypes.Companion_HMacInput_.Create_HMacInput_(m_AwsCryptographyPrimitivesTypes.Companion_DigestAlgorithm_.Create_SHA__256_(), _dafny.SeqOf(uint8(1), uint8(1), uint8(1), uint8(1)), _dafny.SeqOf(uint8(97), uint8(115), uint8(100), uint8(102))), _dafny.SeqOf(uint8(93), uint8(12), uint8(86), uint8(145), uint8(123), uint8(239), uint8(169), uint8(72), uint8(195), uint8(226), uint8(204), uint8(179), uint8(103), uint8(94), uint8(195), uint8(83), uint8(134), uint8(128), uint8(226), uint8(185), uint8(184), uint8(203), uint8(98), uint8(100), uint8(115), uint8(32), uint8(7), uint8(44), uint8(172), uint8(11), uint8(81), uint8(16)))
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("test/TestHMAC.dfy(26,13): " + (_0_valueOrError0).String())
	}
	var _1___v0 _dafny.Tuple
	_ = _1___v0
	_1___v0 = (_0_valueOrError0).Extract().(_dafny.Tuple)
}
func (_static *CompanionStruct_Default___) HmacSHA__384(client m_AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient) {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.TupleOf())
	_ = _0_valueOrError0
	_0_valueOrError0 = Companion_Default___.BasicHMacTest(client, m_AwsCryptographyPrimitivesTypes.Companion_HMacInput_.Create_HMacInput_(m_AwsCryptographyPrimitivesTypes.Companion_DigestAlgorithm_.Create_SHA__384_(), _dafny.SeqOf(uint8(1), uint8(1), uint8(1), uint8(1)), _dafny.SeqOf(uint8(97), uint8(115), uint8(100), uint8(102))), _dafny.SeqOf(uint8(219), uint8(44), uint8(51), uint8(60), uint8(217), uint8(57), uint8(186), uint8(208), uint8(8), uint8(69), uint8(115), uint8(185), uint8(190), uint8(136), uint8(136), uint8(1), uint8(69), uint8(143), uint8(151), uint8(148), uint8(7), uint8(66), uint8(149), uint8(193), uint8(16), uint8(225), uint8(51), uint8(85), uint8(92), uint8(176), uint8(139), uint8(249), uint8(56), uint8(93), uint8(189), uint8(11), uint8(150), uint8(21), uint8(135), uint8(54), uint8(153), uint8(37), uint8(76), uint8(68), uint8(70), uint8(77), uint8(154), uint8(124)))
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("test/TestHMAC.dfy(47,13): " + (_0_valueOrError0).String())
	}
	var _1___v1 _dafny.Tuple
	_ = _1___v1
	_1___v1 = (_0_valueOrError0).Extract().(_dafny.Tuple)
}
func (_static *CompanionStruct_Default___) HmacSHA__512(client m_AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient) {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.TupleOf())
	_ = _0_valueOrError0
	_0_valueOrError0 = Companion_Default___.BasicHMacTest(client, m_AwsCryptographyPrimitivesTypes.Companion_HMacInput_.Create_HMacInput_(m_AwsCryptographyPrimitivesTypes.Companion_DigestAlgorithm_.Create_SHA__512_(), _dafny.SeqOf(uint8(1), uint8(1), uint8(1), uint8(1)), _dafny.SeqOf(uint8(97), uint8(115), uint8(100), uint8(102))), _dafny.SeqOf(uint8(49), uint8(213), uint8(21), uint8(219), uint8(23), uint8(169), uint8(195), uint8(39), uint8(177), uint8(1), uint8(15), uint8(162), uint8(233), uint8(182), uint8(208), uint8(84), uint8(226), uint8(3), uint8(27), uint8(120), uint8(75), uint8(78), uint8(85), uint8(46), uint8(220), uint8(5), uint8(166), uint8(206), uint8(79), uint8(47), uint8(25), uint8(94), uint8(88), uint8(119), uint8(211), uint8(192), uint8(148), uint8(23), uint8(252), uint8(155), uint8(98), uint8(218), uint8(97), uint8(225), uint8(38), uint8(93), uint8(83), uint8(113), uint8(139), uint8(95), uint8(101), uint8(222), uint8(154), uint8(98), uint8(244), uint8(206), uint8(88), uint8(229), uint8(6), uint8(115), uint8(226), uint8(188), uint8(152), uint8(173)))
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("test/TestHMAC.dfy(69,13): " + (_0_valueOrError0).String())
	}
	var _1___v2 _dafny.Tuple
	_ = _1___v2
	_1___v2 = (_0_valueOrError0).Extract().(_dafny.Tuple)
}
func (_static *CompanionStruct_Default___) BasicHMacTest(client m_AwsCryptographyPrimitivesTypes.IAwsCryptographicPrimitivesClient, input m_AwsCryptographyPrimitivesTypes.HMacInput, expectedDigest _dafny.Sequence) m_Wrappers.Result {
	var _0_valueOrError0 m_Wrappers.Result = (client).HMac(input)
	_ = _0_valueOrError0
	if (_0_valueOrError0).IsFailure() {
		return (_0_valueOrError0).PropagateFailure()
	} else {
		var _1_output _dafny.Sequence = (_0_valueOrError0).Extract().(_dafny.Sequence)
		_ = _1_output
		var _2_valueOrError1 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need((_dafny.IntOfUint32((_1_output).Cardinality())).Cmp(m_Digest.Companion_Default___.Length((input).Dtor_digestAlgorithm())) == 0, m_AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(_dafny.SeqOfString("Error")))
		_ = _2_valueOrError1
		if (_2_valueOrError1).IsFailure() {
			return (_2_valueOrError1).PropagateFailure()
		} else {
			var _3_valueOrError2 m_Wrappers.Outcome = m_Wrappers.Companion_Default___.Need(_dafny.Companion_Sequence_.Equal(_1_output, expectedDigest), m_AwsCryptographyPrimitivesTypes.Companion_Error_.Create_AwsCryptographicPrimitivesError_(_dafny.SeqOfString("Error")))
			_ = _3_valueOrError2
			if (_3_valueOrError2).IsFailure() {
				return (_3_valueOrError2).PropagateFailure()
			} else {
				return m_Wrappers.Companion_Result_.Create_Success_(_dafny.TupleOf())
			}
		}
	}
}

// End of class Default__
