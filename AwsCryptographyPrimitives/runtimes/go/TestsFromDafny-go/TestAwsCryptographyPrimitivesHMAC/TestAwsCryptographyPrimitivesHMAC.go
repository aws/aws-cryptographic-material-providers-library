// Package TestAwsCryptographyPrimitivesHMAC
// Dafny module TestAwsCryptographyPrimitivesHMAC compiled into Go

package TestAwsCryptographyPrimitivesHMAC

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
	m_ConstantTime "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/ConstantTime"
	m_ConstantTimeTest "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/ConstantTimeTest"
	m_TestAwsCryptographyPrimitivesAesKdfCtr "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestAwsCryptographyPrimitivesAesKdfCtr"
	m_TestAwsCryptographyPrimitivesDigest "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestAwsCryptographyPrimitivesDigest"
	m_TestAwsCryptographyPrimitivesGenerateRandomBytes "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestAwsCryptographyPrimitivesGenerateRandomBytes"
	m_TestAwsCryptographyPrimitivesHKDF "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestAwsCryptographyPrimitivesHKDF"
	m_TestAwsCryptographyPrimitivesHMacDigest "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestAwsCryptographyPrimitivesHMacDigest"
	m_TestAwsCryptographyPrimitivesRSA "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestAwsCryptographyPrimitivesRSA"
	m_TestECDH "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestECDH"
	m_TestHKDF__Rfc5869TestVectors "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestHKDF__Rfc5869TestVectors"
	m_TestKDF "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestKDF"
	m_TestKDFK__TestVectors "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestKDFK__TestVectors"
	m_TestSignature "github.com/aws/aws-cryptographic-material-providers-library/primitives/test/TestSignature"
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
var _ m_TestAwsCryptographyPrimitivesDigest.Dummy__
var _ m_ConstantTime.Dummy__
var _ m_ConstantTimeTest.Dummy__
var _ m_TestAwsCryptographyPrimitivesAesKdfCtr.Dummy__
var _ m_TestSignature.Dummy__
var _ m_TestHKDF__Rfc5869TestVectors.Dummy__
var _ m_TestAwsCryptographyPrimitivesRSA.Dummy__

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
	return "TestAwsCryptographyPrimitivesHMAC.Default__"
}
func (_this *Default__) ParentTraits_() []*_dafny.TraitID {
	return [](*_dafny.TraitID){}
}

var _ _dafny.TraitOffspring = &Default__{}

func (_static *CompanionStruct_Default___) HMACTests() {
	Companion_Default___.BasicHMACTest(m_AwsCryptographyPrimitivesTypes.Companion_DigestAlgorithm_.Create_SHA__256_(), _dafny.SeqOf(uint8(1), uint8(2), uint8(3), uint8(4)), _dafny.SeqOf(uint8(97), uint8(115), uint8(100), uint8(102)), _dafny.SeqOf(uint8(55), uint8(107), uint8(186), uint8(241), uint8(51), uint8(255), uint8(154), uint8(169), uint8(106), uint8(133), uint8(2), uint8(248), uint8(54), uint8(230), uint8(193), uint8(147), uint8(212), uint8(179), uint8(154), uint8(66), uint8(43), uint8(52), uint8(108), uint8(181), uint8(144), uint8(152), uint8(19), uint8(101), uint8(117), uint8(99), uint8(204), uint8(134)))
	Companion_Default___.BasicHMACTest(m_AwsCryptographyPrimitivesTypes.Companion_DigestAlgorithm_.Create_SHA__384_(), _dafny.SeqOf(uint8(1), uint8(2), uint8(3), uint8(4)), _dafny.SeqOf(uint8(97), uint8(115), uint8(100), uint8(102)), _dafny.SeqOf(uint8(90), uint8(206), uint8(234), uint8(81), uint8(173), uint8(76), uint8(235), uint8(148), uint8(203), uint8(139), uint8(195), uint8(46), uint8(251), uint8(14), uint8(97), uint8(110), uint8(146), uint8(49), uint8(147), uint8(24), uint8(240), uint8(1), uint8(17), uint8(231), uint8(58), uint8(104), uint8(146), uint8(53), uint8(144), uint8(167), uint8(11), uint8(112), uint8(7), uint8(39), uint8(122), uint8(15), uint8(58), uint8(53), uint8(144), uint8(91), uint8(16), uint8(223), uint8(51), uint8(98), uint8(30), uint8(88), uint8(23), uint8(166)))
	Companion_Default___.BasicHMACTest(m_AwsCryptographyPrimitivesTypes.Companion_DigestAlgorithm_.Create_SHA__512_(), _dafny.SeqOf(uint8(1), uint8(2), uint8(3), uint8(4)), _dafny.SeqOf(uint8(97), uint8(115), uint8(100), uint8(102)), _dafny.SeqOf(uint8(100), uint8(23), uint8(173), uint8(215), uint8(39), uint8(67), uint8(51), uint8(165), uint8(149), uint8(53), uint8(87), uint8(84), uint8(145), uint8(58), uint8(221), uint8(155), uint8(239), uint8(182), uint8(249), uint8(134), uint8(147), uint8(191), uint8(143), uint8(224), uint8(140), uint8(165), uint8(190), uint8(221), uint8(183), uint8(15), uint8(6), uint8(102), uint8(203), uint8(77), uint8(238), uint8(64), uint8(10), uint8(138), uint8(61), uint8(64), uint8(219), uint8(79), uint8(248), uint8(249), uint8(90), uint8(102), uint8(217), uint8(188), uint8(13), uint8(2), uint8(101), uint8(96), uint8(217), uint8(242), uint8(73), uint8(254), uint8(190), uint8(217), uint8(134), uint8(33), uint8(163), uint8(137), uint8(151), uint8(183)))
}
func (_static *CompanionStruct_Default___) BasicHMACTest(digestAlgorithm m_AwsCryptographyPrimitivesTypes.DigestAlgorithm, key _dafny.Sequence, message _dafny.Sequence, expectedDigest _dafny.Sequence) {
	var _0_valueOrError0 m_Wrappers.Result = m_Wrappers.Result{}
	_ = _0_valueOrError0
	var _out0 m_Wrappers.Result
	_ = _out0
	_out0 = m_AtomicPrimitives.Companion_Default___.AtomicPrimitives(m_AtomicPrimitives.Companion_Default___.DefaultCryptoConfig())
	_0_valueOrError0 = _out0
	if !(!((_0_valueOrError0).IsFailure())) {
		panic("test/TestAwsCryptographyPrimitivesHMAC.dfy(66,18): " + (_0_valueOrError0).String())
	}
	var _1_client *m_AtomicPrimitives.AtomicPrimitivesClient
	_ = _1_client
	_1_client = (_0_valueOrError0).Extract().(*m_AtomicPrimitives.AtomicPrimitivesClient)
	var _2_input m_AwsCryptographyPrimitivesTypes.HMacInput
	_ = _2_input
	_2_input = m_AwsCryptographyPrimitivesTypes.Companion_HMacInput_.Create_HMacInput_(digestAlgorithm, key, message)
	var _3_valueOrError1 m_Wrappers.Result = m_Wrappers.Companion_Result_.Default(_dafny.EmptySeq)
	_ = _3_valueOrError1
	_3_valueOrError1 = (_1_client).HMac(_2_input)
	if !(!((_3_valueOrError1).IsFailure())) {
		panic("test/TestAwsCryptographyPrimitivesHMAC.dfy(74,18): " + (_3_valueOrError1).String())
	}
	var _4_output _dafny.Sequence
	_ = _4_output
	_4_output = (_3_valueOrError1).Extract().(_dafny.Sequence)
	if !((_dafny.IntOfUint32((_4_output).Cardinality())).Cmp(m_Digest.Companion_Default___.Length(digestAlgorithm)) == 0) {
		panic("test/TestAwsCryptographyPrimitivesHMAC.dfy(75,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
	if !(_dafny.Companion_Sequence_.Equal(_4_output, expectedDigest)) {
		panic("test/TestAwsCryptographyPrimitivesHMAC.dfy(76,4): " + (_dafny.SeqOfString("expectation violation")).String())
	}
}

// End of class Default__
