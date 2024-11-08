// Package TestAwsCryptographyPrimitivesDigest
// Dafny module TestAwsCryptographyPrimitivesDigest compiled into Go

package TestAwsCryptographyPrimitivesDigest

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
	m_TestAwsCryptographyPrimitivesGenerateRandomBytes "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestAwsCryptographyPrimitivesGenerateRandomBytes"
	m_TestAwsCryptographyPrimitivesHKDF "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestAwsCryptographyPrimitivesHKDF"
	m_TestAwsCryptographyPrimitivesHMacDigest "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestAwsCryptographyPrimitivesHMacDigest"
	m_TestECDH "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestECDH"
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
var _ m_TestAwsCryptographyPrimitivesHMacDigest.Dummy__
var _ m_TestECDH.Dummy__
var _ m_TestAwsCryptographyPrimitivesHKDF.Dummy__
var _ m_TestAwsCryptographyPrimitivesGenerateRandomBytes.Dummy__

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
	return "TestAwsCryptographyPrimitivesDigest.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) DigestTests() {
	Companion_Default___.BasicDigestTest(m_AwsCryptographyPrimitivesTypes.Companion_DigestAlgorithm_.Create_SHA__256_(), _dafny.SeqOf(uint8(97), uint8(115), uint8(100), uint8(102)), _dafny.SeqOf(uint8(240), uint8(228), uint8(194), uint8(247), uint8(108), uint8(88), uint8(145), uint8(110), uint8(194), uint8(88), uint8(242), uint8(70), uint8(133), uint8(27), uint8(234), uint8(9), uint8(29), uint8(20), uint8(212), uint8(36), uint8(122), uint8(47), uint8(195), uint8(225), uint8(134), uint8(148), uint8(70), uint8(27), uint8(24), uint8(22), uint8(225), uint8(59)))
	Companion_Default___.BasicDigestTest(m_AwsCryptographyPrimitivesTypes.Companion_DigestAlgorithm_.Create_SHA__384_(), _dafny.SeqOf(uint8(97), uint8(115), uint8(100), uint8(102)), _dafny.SeqOf(uint8(166), uint8(158), uint8(125), uint8(243), uint8(11), uint8(36), uint8(192), uint8(66), uint8(236), uint8(84), uint8(12), uint8(203), uint8(189), uint8(191), uint8(177), uint8(86), uint8(44), uint8(133), uint8(120), uint8(112), uint8(56), uint8(200), uint8(133), uint8(116), uint8(156), uint8(30), uint8(64), uint8(142), uint8(45), uint8(98), uint8(250), uint8(54), uint8(100), uint8(44), uint8(208), uint8(7), uint8(95), uint8(163), uint8(81), uint8(232), uint8(34), uint8(226), uint8(184), uint8(165), uint8(145), uint8(57), uint8(205), uint8(157)))
	Companion_Default___.BasicDigestTest(m_AwsCryptographyPrimitivesTypes.Companion_DigestAlgorithm_.Create_SHA__512_(), _dafny.SeqOf(uint8(97), uint8(115), uint8(100), uint8(102)), _dafny.SeqOf(uint8(64), uint8(27), uint8(9), uint8(234), uint8(179), uint8(192), uint8(19), uint8(212), uint8(202), uint8(84), uint8(146), uint8(43), uint8(184), uint8(2), uint8(190), uint8(200), uint8(253), uint8(83), uint8(24), uint8(25), uint8(43), uint8(10), uint8(117), uint8(242), uint8(1), uint8(216), uint8(179), uint8(114), uint8(116), uint8(41), uint8(8), uint8(15), uint8(179), uint8(55), uint8(89), uint8(26), uint8(189), uint8(62), uint8(68), uint8(69), uint8(59), uint8(149), uint8(69), uint8(85), uint8(183), uint8(160), uint8(129), uint8(46), uint8(16), uint8(129), uint8(195), uint8(155), uint8(116), uint8(2), uint8(147), uint8(247), uint8(101), uint8(234), uint8(231), uint8(49), uint8(245), uint8(166), uint8(94), uint8(209)))
}
func (_static *CompanionStruct_Default___) BasicDigestTest(digestAlgorithm m_AwsCryptographyPrimitivesTypes.DigestAlgorithm, message _dafny.Sequence, expectedDigest _dafny.Sequence) {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_AtomicPrimitives.Companion_Default___.AtomicPrimitives(m_AtomicPrimitives.Companion_Default___.DefaultCryptoConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("test/TestDigest.dfy(61,18): " + (_0_valueOrError0).String())
	}
	var _1_client *m_AtomicPrimitives.AtomicPrimitivesClient
	_ = _1_client
	_1_client = (_0_valueOrError0).Extract().(*m_AtomicPrimitives.AtomicPrimitivesClient)
	var _2_input m_AwsCryptographyPrimitivesTypes.DigestInput
	_ = _2_input
	_2_input = m_AwsCryptographyPrimitivesTypes.Companion_DigestInput_.Create_DigestInput_(digestAlgorithm, message)
	var _3_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _3_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = (_1_client).Digest(_2_input)
	_3_valueOrError1 = _out1
	if !(!((_3_valueOrError1).IsFailure())) {
		panic("test/TestDigest.dfy(68,18): " + (_3_valueOrError1).String())
	}
	var _4_output _dafny.Sequence
	_ = _4_output
	_4_output = (_3_valueOrError1).Extract().(_dafny.Sequence)
	if !((_dafny.IntOfUint32((_4_output).Cardinality())).Cmp(m_Digest.Companion_Default___.Length(digestAlgorithm)) == 0) {
		panic("test/TestDigest.dfy(69,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(_4_output, expectedDigest)) {
		panic("test/TestDigest.dfy(70,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}

// End of class Default__
