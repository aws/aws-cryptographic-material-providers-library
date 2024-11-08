// Package TestAwsCryptographyPrimitivesHKDF
// Dafny module TestAwsCryptographyPrimitivesHKDF compiled into Go

package TestAwsCryptographyPrimitivesHKDF

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
	return "TestAwsCryptographyPrimitivesHKDF.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) TestCase1() {
	var _0_hash m_AwsCryptographyPrimitivesTypes.DigestAlgorithm
	_ = _0_hash
	_0_hash = m_AwsCryptographyPrimitivesTypes.Companion_DigestAlgorithm_.Create_SHA__256_()
	var _1_IKM _dafny.Sequence
	_ = _1_IKM
	_1_IKM = _dafny.SeqOf(uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11), uint8(11))
	var _2_salt _dafny.Sequence
	_ = _2_salt
	_2_salt = _dafny.SeqOf(uint8(0), uint8(1), uint8(2), uint8(3), uint8(4), uint8(5), uint8(6), uint8(7), uint8(8), uint8(9), uint8(10), uint8(11), uint8(12))
	var _3_info _dafny.Sequence
	_ = _3_info
	_3_info = _dafny.SeqOf(uint8(240), uint8(241), uint8(242), uint8(243), uint8(244), uint8(245), uint8(246), uint8(247), uint8(248), uint8(249))
	var _4_L int32
	_ = _4_L
	_4_L = int32(42)
	var _5_PRK _dafny.Sequence
	_ = _5_PRK
	_5_PRK = _dafny.SeqOf(uint8(7), uint8(119), uint8(9), uint8(54), uint8(44), uint8(46), uint8(50), uint8(223), uint8(13), uint8(220), uint8(63), uint8(13), uint8(196), uint8(123), uint8(186), uint8(99), uint8(144), uint8(182), uint8(199), uint8(59), uint8(181), uint8(15), uint8(156), uint8(49), uint8(34), uint8(236), uint8(132), uint8(74), uint8(215), uint8(194), uint8(179), uint8(229))
	var _6_OKM _dafny.Sequence
	_ = _6_OKM
	_6_OKM = _dafny.SeqOf(uint8(60), uint8(178), uint8(95), uint8(37), uint8(250), uint8(172), uint8(213), uint8(122), uint8(144), uint8(67), uint8(79), uint8(100), uint8(208), uint8(54), uint8(47), uint8(42), uint8(45), uint8(45), uint8(10), uint8(144), uint8(207), uint8(26), uint8(90), uint8(76), uint8(93), uint8(176), uint8(45), uint8(86), uint8(236), uint8(196), uint8(197), uint8(191), uint8(52), uint8(0), uint8(114), uint8(8), uint8(213), uint8(184), uint8(135), uint8(24), uint8(88), uint8(101))
	Companion_Default___.BasicExtractTest(m_AwsCryptographyPrimitivesTypes.Companion_HkdfExtractInput_.Create_HkdfExtractInput_(_0_hash, m_Wrappers.Companion_Option_.Create_Some_(_2_salt), _1_IKM), _5_PRK)
	Companion_Default___.BasicExpandTest(m_AwsCryptographyPrimitivesTypes.Companion_HkdfExpandInput_.Create_HkdfExpandInput_(_0_hash, _5_PRK, _3_info, _4_L), _6_OKM)
	Companion_Default___.BasicHkdfTest(m_AwsCryptographyPrimitivesTypes.Companion_HkdfInput_.Create_HkdfInput_(_0_hash, m_Wrappers.Companion_Option_.Create_Some_(_2_salt), _1_IKM, _3_info, _4_L), _6_OKM)
}
func (_static *CompanionStruct_Default___) BasicExtractTest(input m_AwsCryptographyPrimitivesTypes.HkdfExtractInput, expectedPRK _dafny.Sequence) {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_AtomicPrimitives.Companion_Default___.AtomicPrimitives(m_AtomicPrimitives.Companion_Default___.DefaultCryptoConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("test/TestAwsCryptographyPrimitivesHKDF.dfy(86,18): " + (_0_valueOrError0).String())
	}
	var _1_client *m_AtomicPrimitives.AtomicPrimitivesClient
	_ = _1_client
	_1_client = (_0_valueOrError0).Extract().(*m_AtomicPrimitives.AtomicPrimitivesClient)
	var _2_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _2_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = (_1_client).HkdfExtract(input)
	_2_valueOrError1 = _out1
	if !(!((_2_valueOrError1).IsFailure())) {
		panic("test/TestAwsCryptographyPrimitivesHKDF.dfy(88,18): " + (_2_valueOrError1).String())
	}
	var _3_output _dafny.Sequence
	_ = _3_output
	_3_output = (_2_valueOrError1).Extract().(_dafny.Sequence)
	if !((_dafny.IntOfUint32((_3_output).Cardinality())).Cmp(m_Digest.Companion_Default___.Length((input).Dtor_digestAlgorithm())) == 0) {
		panic("test/TestAwsCryptographyPrimitivesHKDF.dfy(89,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(_3_output, expectedPRK)) {
		panic("test/TestAwsCryptographyPrimitivesHKDF.dfy(90,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) BasicExpandTest(input m_AwsCryptographyPrimitivesTypes.HkdfExpandInput, expectedOKM _dafny.Sequence) {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_AtomicPrimitives.Companion_Default___.AtomicPrimitives(m_AtomicPrimitives.Companion_Default___.DefaultCryptoConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("test/TestAwsCryptographyPrimitivesHKDF.dfy(98,18): " + (_0_valueOrError0).String())
	}
	var _1_client *m_AtomicPrimitives.AtomicPrimitivesClient
	_ = _1_client
	_1_client = (_0_valueOrError0).Extract().(*m_AtomicPrimitives.AtomicPrimitivesClient)
	var _2_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _2_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = (_1_client).HkdfExpand(input)
	_2_valueOrError1 = _out1
	if !(!((_2_valueOrError1).IsFailure())) {
		panic("test/TestAwsCryptographyPrimitivesHKDF.dfy(100,18): " + (_2_valueOrError1).String())
	}
	var _3_output _dafny.Sequence
	_ = _3_output
	_3_output = (_2_valueOrError1).Extract().(_dafny.Sequence)
	if !((_dafny.IntOfUint32((_3_output).Cardinality())).Cmp(_dafny.IntOfInt32((input).Dtor_expectedLength())) == 0) {
		panic("test/TestAwsCryptographyPrimitivesHKDF.dfy(101,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(_3_output, expectedOKM)) {
		panic("test/TestAwsCryptographyPrimitivesHKDF.dfy(102,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}
func (_static *CompanionStruct_Default___) BasicHkdfTest(input m_AwsCryptographyPrimitivesTypes.HkdfInput, expectedOKM _dafny.Sequence) {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_AtomicPrimitives.Companion_Default___.AtomicPrimitives(m_AtomicPrimitives.Companion_Default___.DefaultCryptoConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("test/TestAwsCryptographyPrimitivesHKDF.dfy(110,18): " + (_0_valueOrError0).String())
	}
	var _1_client *m_AtomicPrimitives.AtomicPrimitivesClient
	_ = _1_client
	_1_client = (_0_valueOrError0).Extract().(*m_AtomicPrimitives.AtomicPrimitivesClient)
	var _2_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _2_valueOrError1
	var _out1 m_Wrappers.Result
	_ = _out1
	_out1 = (_1_client).Hkdf(input)
	_2_valueOrError1 = _out1
	if !(!((_2_valueOrError1).IsFailure())) {
		panic("test/TestAwsCryptographyPrimitivesHKDF.dfy(112,18): " + (_2_valueOrError1).String())
	}
	var _3_output _dafny.Sequence
	_ = _3_output
	_3_output = (_2_valueOrError1).Extract().(_dafny.Sequence)
	if !((_dafny.IntOfUint32((_3_output).Cardinality())).Cmp(_dafny.IntOfInt32((input).Dtor_expectedLength())) == 0) {
		panic("test/TestAwsCryptographyPrimitivesHKDF.dfy(113,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(_3_output, expectedOKM)) {
		panic("test/TestAwsCryptographyPrimitivesHKDF.dfy(114,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}

// End of class Default__
